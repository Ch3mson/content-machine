#!/usr/bin/env python3
"""Shared fal.ai helpers for the tools/fal scripts.

Covers: FAL_KEY lookup (shell env, then repo .env), local file -> data URI,
synchronous runs (fal.run), queued runs with polling (queue.fal.run), storage
uploads, and result downloads. Standard library only.
"""

from __future__ import annotations

import base64
import json
import mimetypes
import os
import socket
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Callable

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SYNC_BASE = "https://fal.run"
QUEUE_BASE = "https://queue.fal.run"
STORAGE_INITIATE = "https://rest.alpha.fal.ai/storage/upload/initiate"

SEEDREAM_TEXT = "bytedance/seedream/v5/pro/text-to-image"
SEEDREAM_EDIT = "bytedance/seedream/v5/pro/edit"
KLING_I2V = "fal-ai/kling-video/v3/pro/image-to-video"

IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp"}


class FalError(RuntimeError):
    """Raised for HTTP or payload errors from fal."""


def load_dotenv_value(name: str) -> str | None:
    env_path = PROJECT_ROOT / ".env"
    if not env_path.exists():
        return None
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        if key.strip() == name:
            return value.strip().strip('"').strip("'")
    return None


def get_api_key() -> str:
    api_key = os.environ.get("FAL_KEY") or load_dotenv_value("FAL_KEY")
    if not api_key:
        raise SystemExit("Missing FAL_KEY. Set it in the shell or in the repo .env file.")
    return api_key


def file_to_data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "image/jpeg"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def _headers(api_key: str, content_type: str | None = "application/json") -> dict[str, str]:
    headers = {"Authorization": f"Key {api_key}", "Accept": "application/json"}
    if content_type:
        headers["Content-Type"] = content_type
    return headers


def _request_json(
    url: str,
    api_key: str,
    payload: dict | None = None,
    method: str = "POST",
    timeout: int = 120,
) -> dict:
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    request = urllib.request.Request(url, data=data, headers=_headers(api_key), method=method)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise FalError(f"fal request failed ({exc.code}) for {url}: {detail}") from exc


def _is_retryable(exc: BaseException) -> bool:
    if isinstance(exc, FalError):
        text = str(exc)
        return any(f"({code})" in text for code in (500, 502, 503, 504, 429))
    return isinstance(exc, (urllib.error.URLError, socket.timeout, TimeoutError))


def run_sync(model: str, payload: dict, api_key: str, timeout: int = 240, retries: int = 1) -> dict:
    """POST to fal.run/{model} and return the JSON body. Retries once on 5xx/429/timeouts."""
    attempt = 0
    while True:
        try:
            return _request_json(f"{SYNC_BASE}/{model}", api_key, payload, timeout=timeout)
        except Exception as exc:  # noqa: BLE001 - we re-raise unless retryable
            if attempt >= retries or not _is_retryable(exc):
                raise
            attempt += 1
            time.sleep(3 * attempt)


def submit_queue(model: str, payload: dict, api_key: str) -> tuple[str, str, str]:
    body = _request_json(f"{QUEUE_BASE}/{model}", api_key, payload, timeout=30)
    request_id = body.get("request_id")
    if not request_id:
        raise FalError(f"No request_id in queue response: {body}")
    status_url = body.get("status_url") or f"{QUEUE_BASE}/{model}/requests/{request_id}/status"
    response_url = body.get("response_url") or f"{QUEUE_BASE}/{model}/requests/{request_id}"
    return request_id, status_url, response_url


def poll_queue(
    status_url: str,
    response_url: str,
    api_key: str,
    timeout: int = 600,
    interval: int = 5,
    log: Callable[[str], None] | None = print,
) -> dict:
    start = time.time()
    while time.time() - start < timeout:
        time.sleep(interval)
        try:
            status_body = _request_json(status_url, api_key, method="GET", timeout=30)
        except FalError as exc:
            if log:
                log(f"poll error, retrying: {exc}")
            continue
        status = status_body.get("status")
        if log:
            log(f"[{int(time.time() - start)}s] {status} (queue position {status_body.get('queue_position', 0)})")
        if status == "COMPLETED":
            return _request_json(response_url, api_key, method="GET", timeout=60)
        if status in ("FAILED", "CANCELLED"):
            raise FalError(f"queue job {status}: {status_body}")
    raise TimeoutError(f"queue job timed out after {timeout}s")


def run_queue(model: str, payload: dict, api_key: str, timeout: int = 600, log=print) -> dict:
    request_id, status_url, response_url = submit_queue(model, payload, api_key)
    if log:
        log(f"submitted to {model}, request {request_id}")
    return poll_queue(status_url, response_url, api_key, timeout=timeout, log=log)


def upload_file(path: Path, api_key: str) -> str:
    """Upload a local file to fal storage and return its public URL."""
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    init = _request_json(
        STORAGE_INITIATE,
        api_key,
        {"file_name": path.name, "content_type": mime},
        timeout=30,
    )
    put_request = urllib.request.Request(
        init["upload_url"],
        data=path.read_bytes(),
        headers={"Content-Type": mime},
        method="PUT",
    )
    with urllib.request.urlopen(put_request, timeout=120) as response:
        if response.status not in (200, 201):
            raise FalError(f"upload failed for {path.name}: HTTP {response.status}")
    return init["file_url"]


def download(url: str, out_path: Path, timeout: int = 120) -> Path:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=timeout) as response:
        out_path.write_bytes(response.read())
    return out_path


def first_image_url(body: dict) -> str:
    images = body.get("images") or []
    if not images or not images[0].get("url"):
        raise FalError(f"No image URL in fal response: {body}")
    return images[0]["url"]


def parse_size(value: str) -> tuple[int, int]:
    """Parse 'WIDTHxHEIGHT' into a tuple."""
    try:
        width, height = value.lower().split("x", 1)
        return int(width), int(height)
    except ValueError as exc:
        raise SystemExit(f"--size must look like 1080x1440, got {value!r}") from exc


def resolve_repo_path(value: str | Path) -> Path:
    """Resolve a path given relative to the repo root or the cwd."""
    path = Path(value).expanduser()
    if path.is_absolute():
        return path
    if (PROJECT_ROOT / path).exists():
        return (PROJECT_ROOT / path).resolve()
    return path.resolve()


def list_images(path: Path) -> list[Path]:
    """Return image files for a file or directory path (non-recursive, sorted)."""
    if path.is_file():
        return [path] if path.suffix.lower() in IMAGE_SUFFIXES else []
    if path.is_dir():
        return sorted(p for p in path.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES)
    return []

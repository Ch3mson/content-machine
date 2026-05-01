#!/usr/bin/env python3
"""
Fetch a transcript for a public TikTok video using Supadata.

The script does not download the video. It calls Supadata's transcript endpoint
and saves the returned transcript as markdown for hook-idea analysis.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "references" / "hook-ideas" / "inbox" / "transcripts"
API_BASE = "https://api.supadata.ai/v1/transcript"


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
    api_key = os.environ.get("SUPADATA_API_KEY") or load_dotenv_value("SUPADATA_API_KEY")
    if not api_key:
        raise SystemExit(
            "Missing SUPADATA_API_KEY. Set it in your shell or local .env file:\n"
            "  SUPADATA_API_KEY=your_key_here"
        )
    return api_key


def request_json(url: str, api_key: str) -> tuple[int, dict[str, Any], dict[str, str]]:
    request = urllib.request.Request(
        url,
        headers={
            "x-api-key": api_key,
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            body = response.read().decode("utf-8")
            headers = {k.lower(): v for k, v in response.headers.items()}
            return response.status, json.loads(body), headers
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        try:
            payload = json.loads(body)
        except json.JSONDecodeError:
            payload = {"error": body}
        headers = {k.lower(): v for k, v in exc.headers.items()}
        return exc.code, payload, headers


def build_slug(video_url: str) -> str:
    match = re.search(r"/(?:video|photo)/(\d+)", video_url)
    if match:
        return f"tiktok-{match.group(1)}"
    digest = hashlib.sha1(video_url.encode("utf-8")).hexdigest()[:10]
    return f"tiktok-{digest}"


def format_time(ms: int | float | None) -> str:
    if ms is None:
        return "00:00"
    seconds = int(ms // 1000)
    return f"{seconds // 60:02d}:{seconds % 60:02d}"


def content_to_markdown(content: Any) -> str:
    if isinstance(content, str):
        return content.strip()

    if isinstance(content, list):
        lines: list[str] = []
        for item in content:
            if not isinstance(item, dict):
                continue
            text = str(item.get("text", "")).strip()
            if not text:
                continue
            lines.append(f"[{format_time(item.get('offset'))}] {text}")
        return "\n".join(lines).strip()

    return json.dumps(content, indent=2, ensure_ascii=False)


def poll_job(job_id: str, api_key: str, interval: float, max_polls: int) -> tuple[dict[str, Any], dict[str, str]]:
    job_url = f"{API_BASE}/{urllib.parse.quote(job_id)}"
    last_headers: dict[str, str] = {}

    for _ in range(max_polls):
        status_code, payload, headers = request_json(job_url, api_key)
        last_headers = headers
        if status_code >= 400:
            raise SystemExit(f"Supadata job polling failed ({status_code}): {payload}")

        status = payload.get("status")
        if status == "completed":
            return payload, headers
        if status == "failed":
            raise SystemExit(f"Supadata transcript job failed: {payload.get('error', payload)}")
        time.sleep(interval)

    raise SystemExit(f"Supadata transcript job did not finish after {max_polls} polls.")


def fetch_transcript(args: argparse.Namespace) -> tuple[dict[str, Any], dict[str, str]]:
    api_key = get_api_key()
    query = {
        "url": args.url,
        "mode": args.mode,
        "text": "true" if args.plain_text else "false",
    }
    if args.lang:
        query["lang"] = args.lang

    endpoint = f"{API_BASE}?{urllib.parse.urlencode(query)}"
    status_code, payload, headers = request_json(endpoint, api_key)

    if status_code == 202 and "jobId" in payload:
        return poll_job(payload["jobId"], api_key, args.poll_interval, args.max_polls)

    if status_code >= 400 or status_code == 206:
        raise SystemExit(f"Supadata transcript request failed ({status_code}): {payload}")

    return payload, headers


def write_markdown(args: argparse.Namespace, payload: dict[str, Any], headers: dict[str, str]) -> Path:
    output_path = Path(args.out).expanduser().resolve() if args.out else None
    if output_path is None:
        slug = args.slug or build_slug(args.url)
        output_path = DEFAULT_OUTPUT_DIR / f"{date.today().isoformat()}-{slug}.md"

    output_path.parent.mkdir(parents=True, exist_ok=True)

    content = payload.get("content")
    if "result" in payload and content is None:
        result = payload["result"]
        content = result.get("content") if isinstance(result, dict) else result

    transcript = content_to_markdown(content)
    lang = payload.get("lang", "")
    available_langs = payload.get("availableLangs", [])
    billable = headers.get("x-billable-requests", "")

    output_path.write_text(
        "\n".join(
            [
                f"# Video Transcript: {args.slug or build_slug(args.url)}",
                "",
                f"- Source URL: {args.url}",
                "- Source type: TikTok video",
                "- Method: Supadata transcript API",
                f"- Mode: {args.mode}",
                f"- Language: {lang}",
                f"- Available languages: {', '.join(available_langs) if available_langs else ''}",
                f"- Billable requests: {billable}",
                "",
                "## Transcript",
                "",
                transcript,
                "",
            ]
        ),
        encoding="utf-8",
    )
    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch a TikTok video transcript from Supadata without downloading the video."
    )
    parser.add_argument("url", help="Public TikTok video URL")
    parser.add_argument("--out", help="Output markdown path")
    parser.add_argument("--slug", help="Slug for the default output filename")
    parser.add_argument("--lang", default="en", help="Preferred transcript language. Default: en")
    parser.add_argument(
        "--mode",
        default="auto",
        choices=["native", "auto", "generate"],
        help="Supadata transcript mode. Default: auto",
    )
    parser.add_argument(
        "--plain-text",
        action="store_true",
        help="Request plain text instead of timestamped chunks.",
    )
    parser.add_argument("--poll-interval", type=float, default=1.0)
    parser.add_argument("--max-polls", type=int, default=120)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    payload, headers = fetch_transcript(args)
    output_path = write_markdown(args, payload, headers)
    print(f"Saved transcript: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

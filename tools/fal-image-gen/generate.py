#!/usr/bin/env python3
"""Generate a still with Fal Seedream 5.0 Pro. Reads FAL_KEY from repo .env."""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
TEXT_MODEL = "bytedance/seedream/v5/pro/text-to-image"
EDIT_MODEL = "bytedance/seedream/v5/pro/edit"
DEFAULT_OUT_DIR = PROJECT_ROOT / "tools" / "fal-image-gen" / "out"


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
        raise SystemExit("Missing FAL_KEY. Set it in the repo .env file.")
    return api_key


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a Seedream still via Fal.")
    parser.add_argument("--prompt", required=True, help="Image prompt")
    parser.add_argument("--out", help="Output image path")
    parser.add_argument("--width", type=int, default=1080)
    parser.add_argument("--height", type=int, default=1920)
    parser.add_argument("--format", choices=("jpeg", "png"), default="jpeg")
    parser.add_argument(
        "--ref",
        action="append",
        default=[],
        help="Local reference image. Repeatable. Switches to the edit endpoint.",
    )
    return parser.parse_args()


def file_to_data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "image/jpeg"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def main() -> int:
    args = parse_args()
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    out_path = Path(args.out).expanduser().resolve() if args.out else (
        DEFAULT_OUT_DIR / f"{stamp}.{args.format}"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)

    refs = [Path(p).expanduser().resolve() for p in args.ref]
    for ref in refs:
        if not ref.exists():
            raise SystemExit(f"Reference image not found: {ref}")

    model = EDIT_MODEL if refs else TEXT_MODEL
    payload = {
        "prompt": args.prompt,
        "image_size": {"width": args.width, "height": args.height},
        "num_images": 1,
        "output_format": args.format,
        "enable_safety_checker": True,
    }
    if refs:
        payload["image_urls"] = [file_to_data_uri(ref) for ref in refs]

    request = urllib.request.Request(
        f"https://fal.run/{model}",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Key {get_api_key()}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            body = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Fal request failed ({exc.code}): {detail}") from exc

    images = body.get("images") or []
    if not images or not images[0].get("url"):
        raise SystemExit(f"No image URL in Fal response: {body}")

    image_url = images[0]["url"]
    with urllib.request.urlopen(image_url, timeout=120) as image_response:
        out_path.write_bytes(image_response.read())

    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

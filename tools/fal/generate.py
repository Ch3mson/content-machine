#!/usr/bin/env python3
"""Generate a still with Fal Seedream 5 Pro.

No --ref: text-to-image. One or more --ref: the edit endpoint, with the
references passed in order (Figure 1, Figure 2, ...). For the locked avatar
face-swap use swap_avatar.py instead; it carries the identity-lock prompt.
"""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

from _client import (
    PROJECT_ROOT,
    SEEDREAM_EDIT,
    SEEDREAM_TEXT,
    download,
    file_to_data_uri,
    first_image_url,
    get_api_key,
    resolve_repo_path,
    run_sync,
)

DEFAULT_OUT_DIR = PROJECT_ROOT / "tools" / "fal" / "out"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a Seedream still via fal.")
    parser.add_argument("--prompt", required=True, help="Image prompt")
    parser.add_argument("--out", help="Output image path (default: tools/fal/out/{stamp}.{format})")
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


def main() -> int:
    args = parse_args()
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    out_path = resolve_repo_path(args.out) if args.out else DEFAULT_OUT_DIR / f"{stamp}.{args.format}"

    refs = [resolve_repo_path(p) for p in args.ref]
    for ref in refs:
        if not ref.exists():
            raise SystemExit(f"Reference image not found: {ref}")

    model = SEEDREAM_EDIT if refs else SEEDREAM_TEXT
    payload = {
        "prompt": args.prompt,
        "image_size": {"width": args.width, "height": args.height},
        "num_images": 1,
        "output_format": args.format,
        "enable_safety_checker": True,
    }
    if refs:
        payload["image_urls"] = [file_to_data_uri(ref) for ref in refs]

    body = run_sync(model, payload, get_api_key(), timeout=240)
    download(first_image_url(body), out_path)
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

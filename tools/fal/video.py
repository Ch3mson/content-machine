#!/usr/bin/env python3
"""Image-to-video with fal (default: Kling v3 Pro).

Uploads the still to fal storage, submits to the queue, polls, downloads the mp4.
"""

from __future__ import annotations

import argparse

from _client import KLING_I2V, download, get_api_key, resolve_repo_path, run_queue, upload_file


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Animate a still into a short clip via fal.")
    parser.add_argument("--image", required=True, help="Start frame (local path)")
    parser.add_argument("--prompt", required=True, help="Motion / scene prompt")
    parser.add_argument("--out", required=True, help="Output .mp4 path")
    parser.add_argument("--model", default=KLING_I2V)
    parser.add_argument("--duration", default="5", help="Seconds, as the model expects (default 5)")
    parser.add_argument("--no-audio", action="store_true", help="Disable generated audio")
    parser.add_argument("--timeout", type=int, default=600)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    image_path = resolve_repo_path(args.image)
    if not image_path.exists():
        raise SystemExit(f"Image not found: {image_path}")
    out_path = resolve_repo_path(args.out)

    api_key = get_api_key()
    image_url = upload_file(image_path, api_key)
    print(f"uploaded {image_path.name} -> {image_url}")

    payload = {
        "start_image_url": image_url,
        "prompt": args.prompt,
        "duration": args.duration,
        "generate_audio": not args.no_audio,
    }
    result = run_queue(args.model, payload, api_key, timeout=args.timeout)
    video_url = (result.get("video") or {}).get("url")
    if not video_url:
        raise SystemExit(f"No video URL in result: {result}")

    download(video_url, out_path)
    print(f"{out_path} ({out_path.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

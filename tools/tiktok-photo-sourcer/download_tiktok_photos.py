#!/usr/bin/env python3
"""
Download TikTok photo carousel images into a slideshow reference folder.

This is a small project wrapper around gallery-dl. It intentionally does not
use cookies, and it only asks gallery-dl for TikTok photos.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_BASE_DIR = PROJECT_ROOT / "references" / "social-accounts"


def normalize_post_label(value: str) -> str:
    cleaned = value.strip()
    if not cleaned:
        raise argparse.ArgumentTypeError("post cannot be empty")
    if cleaned.isdigit():
        return f"Post {cleaned}"
    return cleaned


def resolve_gallery_dl() -> list[str]:
    executable = shutil.which("gallery-dl")
    if executable:
        return [executable]

    try:
        subprocess.run(
            [sys.executable, "-m", "gallery_dl", "--version"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except (OSError, subprocess.CalledProcessError):
        raise SystemExit(
            "gallery-dl is not available. Install it with:\n"
            "  python -m pip install gallery-dl"
        )

    return [sys.executable, "-m", "gallery_dl"]


def build_output_dir(args: argparse.Namespace) -> Path:
    if args.out:
        return Path(args.out).expanduser().resolve()

    if not args.account or not args.post:
        raise SystemExit("Use --out, or provide both --account and --post.")

    return (DEFAULT_BASE_DIR / args.account.strip() / normalize_post_label(args.post)).resolve()


def build_command(args: argparse.Namespace, output_dir: Path) -> list[str]:
    return [
        *resolve_gallery_dl(),
        "-D",
        str(output_dir),
        "-f",
        args.filename,
        "-o",
        "extractor.tiktok.audio=false",
        "-o",
        "extractor.tiktok.videos=false",
        "-o",
        "extractor.tiktok.photos=true",
        "--sleep-request",
        args.sleep_request,
        args.url,
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download photos from a TikTok photo post without using cookies."
    )
    parser.add_argument("url", help="TikTok photo post URL")
    parser.add_argument(
        "--account",
        help="Reference account folder under references/social-accounts, e.g. legendperform",
    )
    parser.add_argument(
        "--post",
        help='Post folder label or number, e.g. "Post 5" or 5',
    )
    parser.add_argument(
        "--out",
        help="Explicit output directory. Overrides --account/--post.",
    )
    parser.add_argument(
        "--filename",
        default="{num}.{extension}",
        help='gallery-dl filename template. Default: "{num}.{extension}"',
    )
    parser.add_argument(
        "--sleep-request",
        default="2-5",
        help='gallery-dl request delay. Default: "2-5"',
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the gallery-dl command without downloading.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_dir = build_output_dir(args)
    output_dir.mkdir(parents=True, exist_ok=True)

    command = build_command(args, output_dir)
    print("Saving TikTok photos to:")
    print(f"  {output_dir}")

    if args.dry_run:
        print("Command:")
        print("  " + subprocess.list2cmdline(command))
        return 0

    return subprocess.run(command).returncode


if __name__ == "__main__":
    raise SystemExit(main())

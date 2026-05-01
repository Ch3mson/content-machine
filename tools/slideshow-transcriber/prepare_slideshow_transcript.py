#!/usr/bin/env python3
"""
Create a slide-by-slide transcript scaffold for a folder of slideshow images.

This does not perform OCR. The agent should inspect each image and fill in the
visible text, preserving line breaks where they matter.
"""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "references" / "hook-ideas" / "inbox" / "slideshows"
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def natural_key(path: Path) -> list[object]:
    parts = re.split(r"(\d+)", path.stem.lower())
    return [int(part) if part.isdigit() else part for part in parts]


def list_images(image_dir: Path) -> list[Path]:
    return sorted(
        [p for p in image_dir.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_EXTENSIONS],
        key=natural_key,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare a markdown transcript scaffold for slideshow images."
    )
    parser.add_argument("image_dir", help="Folder containing slide images")
    parser.add_argument("--out", help="Output markdown path")
    parser.add_argument("--slug", help="Slug for default output filename")
    parser.add_argument("--source-url", help="Original post URL, if known")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    image_dir = Path(args.image_dir).expanduser().resolve()
    if not image_dir.exists():
        raise SystemExit(f"Image folder not found: {image_dir}")

    images = list_images(image_dir)
    if not images:
        raise SystemExit(f"No slideshow images found in: {image_dir}")

    slug = args.slug or image_dir.name.lower().replace(" ", "-")
    output_path = Path(args.out).expanduser().resolve() if args.out else (
        DEFAULT_OUTPUT_DIR / f"{date.today().isoformat()}-{slug}.md"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        f"# Slideshow Transcript: {slug}",
        "",
        f"- Source URL: {args.source_url or ''}",
        f"- Image folder: {image_dir}",
        "- Method: visual slide-by-slide transcription",
        "",
        "## Slide Text",
        "",
    ]

    for index, image in enumerate(images, start=1):
        lines.extend(
            [
                f"### Slide {index}",
                "",
                f"- Image: {image}",
                "- Visible text:",
                "",
                "```text",
                "",
                "```",
                "",
                "- Visual notes:",
                "",
            ]
        )

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Prepared slideshow transcript scaffold: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

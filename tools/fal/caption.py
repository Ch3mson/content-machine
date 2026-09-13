#!/usr/bin/env python3
"""Render the approved caption onto a still (TikTok/IG single-image look).

Bold white TikTok Sans with a black outline, every line centered, manual line
breaks preserved. Emoji render with Apple Color Emoji on macOS. Writes
{stem}_caption.jpg next to the clean still unless --out is given.

Examples:
  python tools/fal/caption.py --image accounts/antigpt/posts/2/image.jpg \
      --text "Things I WISH I knew\\nbefore my first all-nighter"
  python tools/fal/caption.py --image in.jpg --text "one line" --anchor top --y 0.18 --size 40
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from _client import PROJECT_ROOT, resolve_repo_path

DEFAULT_FONT = PROJECT_ROOT / "accounts" / "antigpt" / "assets" / "fonts" / "TikTokSans-Bold.ttf"
EMOJI_FONT_PATH = Path("/System/Library/Fonts/Apple Color Emoji.ttc")
EMOJI_STRIKES = [20, 32, 40, 48, 64, 96, 160]
EMOJI_EXTRA = {0x2640, 0x2642, 0x2600, 0x2764, 0x200D, 0xFE0F}
EMOJI_GAP = 6


def is_emoji(char: str) -> bool:
    code = ord(char)
    return code > 0x1F000 or code in EMOJI_EXTRA


def split_segments(text: str) -> list[tuple[str, bool]]:
    segments: list[tuple[str, bool]] = []
    buffer: list[str] = []
    for char in text:
        if is_emoji(char):
            if buffer:
                segments.append(("".join(buffer), False))
                buffer = []
            segments.append((char, True))
        else:
            buffer.append(char)
    if buffer:
        segments.append(("".join(buffer), False))
    return segments


def emoji_image(char: str, target: int) -> Image.Image | None:
    if not EMOJI_FONT_PATH.exists():
        return None
    higher = [s for s in EMOJI_STRIKES if s >= target]
    strike = min(higher) if higher else max(EMOJI_STRIKES)
    font = ImageFont.truetype(str(EMOJI_FONT_PATH), strike)
    box = font.getbbox(char)
    canvas = Image.new("RGBA", (box[2] - box[0] + strike, box[3] - box[1] + strike), (0, 0, 0, 0))
    ImageDraw.Draw(canvas).text((strike // 2 - box[0], strike // 2 - box[1]), char, font=font, embedded_color=True)
    bbox = canvas.getbbox()
    if bbox:
        canvas = canvas.crop(bbox)
    ratio = target / max(1, canvas.height)
    return canvas.resize((max(1, int(canvas.width * ratio)), max(1, int(canvas.height * ratio))), Image.Resampling.LANCZOS)


def measure(line: str, font: ImageFont.FreeTypeFont, size: int) -> int:
    width = 0
    for segment, emoji in split_segments(line):
        if emoji:
            image = emoji_image(segment, size)
            width += (image.width + EMOJI_GAP) if image else font.getlength(segment)
        else:
            width += font.getlength(segment)
    return int(width)


def draw_line(
    overlay: Image.Image,
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    line: str,
    font: ImageFont.FreeTypeFont,
    size: int,
    stroke: int,
) -> None:
    cursor = x
    for segment, emoji in split_segments(line):
        if emoji:
            image = emoji_image(segment, size)
            if image is None:
                draw.text((cursor, y), segment, font=font, fill="white", stroke_width=stroke, stroke_fill=(0, 0, 0, 240))
                cursor += int(font.getlength(segment))
                continue
            overlay.paste(image, (cursor + EMOJI_GAP // 2, y + max(0, (size - image.height) // 2)), image)
            cursor += image.width + EMOJI_GAP
        else:
            draw.text((cursor, y), segment, font=font, fill="white", stroke_width=stroke, stroke_fill=(0, 0, 0, 240))
            cursor += int(font.getlength(segment))


def render(
    image_path: Path,
    out_path: Path,
    lines: list[str],
    font_path: Path,
    size: int,
    anchor: str,
    y_fraction: float,
    gap: int,
    stroke: int,
    max_width: float,
) -> Path:
    base = Image.open(image_path).convert("RGBA")
    width, height = base.size
    font = ImageFont.truetype(str(font_path), size)

    ascent, descent = font.getmetrics()
    line_height = ascent + descent
    block_height = len(lines) * line_height + (len(lines) - 1) * gap
    start_y = int(height * y_fraction - block_height / 2) if anchor == "center" else int(height * y_fraction)

    widths = [measure(line, font, size) for line in lines]
    limit = int(width * max_width)
    for line, line_width in zip(lines, widths):
        if line_width > limit:
            print(f"warning: line wider than {max_width:.0%} of the image: {line!r}", file=sys.stderr)

    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    y = start_y
    for line, line_width in zip(lines, widths):
        draw_line(overlay, draw, (width - line_width) // 2, y, line, font, size, stroke)
        y += line_height + gap

    Image.alpha_composite(base, overlay).convert("RGB").save(out_path, quality=95)
    return out_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render a centered caption onto a still.")
    parser.add_argument("--image", required=True, help="Clean still")
    parser.add_argument("--text", required=True, help="Caption text. Use \\n for manual line breaks.")
    parser.add_argument("--out", help="Output path (default: {stem}_caption.jpg beside the input)")
    parser.add_argument("--anchor", choices=("center", "top"), default="center",
                        help="center: block centered on --y. top: first line starts at --y.")
    parser.add_argument("--y", type=float, default=None,
                        help="Vertical position as a fraction of height (default 0.48 center, 0.22 top)")
    parser.add_argument("--size", type=int, default=42, help="Font size in px (default 42)")
    parser.add_argument("--gap", type=int, default=14, help="Extra px between lines (default 14)")
    parser.add_argument("--stroke", type=int, default=5, help="Outline width in px (default 5)")
    parser.add_argument("--font", help=f"TTF path (default {DEFAULT_FONT.relative_to(PROJECT_ROOT)})")
    parser.add_argument("--max-width", type=float, default=0.86, help="Warn when a line exceeds this fraction of width")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    image_path = resolve_repo_path(args.image)
    if not image_path.exists():
        raise SystemExit(f"Image not found: {image_path}")
    font_path = resolve_repo_path(args.font) if args.font else DEFAULT_FONT
    if not font_path.exists():
        raise SystemExit(f"Font not found: {font_path}")

    out_path = resolve_repo_path(args.out) if args.out else image_path.with_name(f"{image_path.stem}_caption.jpg")
    y_fraction = args.y if args.y is not None else (0.48 if args.anchor == "center" else 0.22)
    lines = [line for line in args.text.replace("\\n", "\n").split("\n")]
    if not any(line.strip() for line in lines):
        raise SystemExit("--text is empty")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    render(image_path, out_path, lines, font_path, args.size, args.anchor, y_fraction, args.gap, args.stroke, args.max_width)
    print(out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

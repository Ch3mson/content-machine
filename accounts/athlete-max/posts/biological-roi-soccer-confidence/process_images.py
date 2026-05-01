"""Render athlete-max slides with unsourced reference-photo placeholders.

The copy source is flow.md. This script parses the slide JSON blocks and
preserves the manual line breaks defined there.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
FLOW = ROOT / "flow.md"
OUT_DIR = ROOT / "processed"
SOURCED_DIR = ROOT / "sourced"

W, H = 1080, 1350
BG = "#FFFFFF"
BLACK = "#111111"
DARK_GRAY = "#444444"
LIGHT_GRAY = "#F2F2F2"
MID_GRAY = "#D0D0D0"
ACCENT = "#B00000"

FONT_REG = "C:/Windows/Fonts/arial.ttf"
FONT_BOLD = "C:/Windows/Fonts/arialbd.ttf"

MARGIN_LR = 72
SAFE_WIDTH = W - (MARGIN_LR * 2)

FRAME_W = 800
FRAME_H = 450
FRAME_X = (W - FRAME_W) // 2
FRAME_Y = 486
FRAME_BOTTOM = FRAME_Y + FRAME_H


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size)


F_HERO = font(FONT_BOLD, 94)
F_SUB = font(FONT_REG, 34)
F_LABEL = font(FONT_REG, 30)
F_TITLE = font(FONT_BOLD, 56)
F_BODY = font(FONT_REG, 28)
F_BODY_BOLD = font(FONT_BOLD, 28)
F_FRAME_LABEL = font(FONT_BOLD, 28)
F_SOURCE = font(FONT_REG, 19)


def load_slides() -> list[dict]:
    text = FLOW.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*(\{.*?\})\s*```", text, flags=re.S)
    slides = []
    for block in blocks:
        data = json.loads(block)
        if "slide" in data:
            slides.append(data)
    return sorted(slides, key=lambda item: item["slide"])


def text_width(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> int:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0]


def center_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    y: int,
    fnt: ImageFont.FreeTypeFont,
    fill: str = BLACK,
) -> None:
    x = (W - text_width(draw, text, fnt)) // 2
    draw.text((x, y), text, font=fnt, fill=fill)


def parse_rich_line(line: str) -> list[tuple[str, ImageFont.FreeTypeFont, str]]:
    pieces: list[tuple[str, ImageFont.FreeTypeFont, str]] = []
    pos = 0
    for match in re.finditer(r"\*\*(.+?)\*\*", line):
        if match.start() > pos:
            pieces.append((line[pos : match.start()], F_BODY, BLACK))
        pieces.append((match.group(1), F_BODY_BOLD, BLACK))
        pos = match.end()
    if pos < len(line):
        pieces.append((line[pos:], F_BODY, BLACK))
    return pieces


def draw_centered_rich(
    draw: ImageDraw.ImageDraw,
    pieces: list[tuple[str, ImageFont.FreeTypeFont, str]],
    y: int,
) -> None:
    total = sum(text_width(draw, text, fnt) for text, fnt, _ in pieces)
    x = (W - total) // 2
    for text, fnt, fill in pieces:
        draw.text((x, y), text, font=fnt, fill=fill)
        x += text_width(draw, text, fnt)


def draw_lines(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    y: int,
    line_gap: int = 8,
) -> int:
    cur = y
    for line in lines:
        pieces = parse_rich_line(line)
        plain = re.sub(r"\*\*(.+?)\*\*", r"\1", line)
        width = text_width(draw, plain, F_BODY)
        if width > SAFE_WIDTH:
            print(f"WARNING slide text exceeds safe width: {plain}")
        draw_centered_rich(draw, pieces, cur)
        cur += F_BODY.size + line_gap
    return cur


def draw_placeholder_frame(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    w: int,
    h: int,
    label: str,
) -> None:
    draw.rectangle((x, y, x + w, y + h), fill=LIGHT_GRAY, outline=MID_GRAY, width=3)
    draw.line((x, y, x + w, y + h), fill=MID_GRAY, width=2)
    draw.line((x + w, y, x, y + h), fill=MID_GRAY, width=2)

    label_w = text_width(draw, label, F_FRAME_LABEL)
    pad_x, pad_y = 18, 10
    cx = x + w // 2
    cy = y + h // 2
    draw.rectangle(
        (
            cx - label_w // 2 - pad_x,
            cy - F_FRAME_LABEL.size // 2 - pad_y,
            cx + label_w // 2 + pad_x,
            cy + F_FRAME_LABEL.size // 2 + pad_y,
        ),
        fill=BG,
        outline=MID_GRAY,
        width=2,
    )
    draw.text(
        (cx - label_w // 2, cy - F_FRAME_LABEL.size // 2 - 2),
        label,
        font=F_FRAME_LABEL,
        fill=DARK_GRAY,
    )


def find_sourced_image(slide_num: int) -> Path | None:
    for ext in ("png", "jpg", "jpeg", "webp"):
        candidate = SOURCED_DIR / f"slide_{slide_num}.{ext}"
        if candidate.exists():
            return candidate
    return None


def crop_image_to_frame(path: Path, w: int, h: int) -> Image.Image:
    img = Image.open(path).convert("RGB")
    target_ratio = w / h
    current_ratio = img.width / img.height
    if current_ratio > target_ratio:
        new_w = int(img.height * target_ratio)
        left = (img.width - new_w) // 2
        img = img.crop((left, 0, left + new_w, img.height))
    else:
        new_h = int(img.width / target_ratio)
        top = (img.height - new_h) // 2
        img = img.crop((0, top, img.width, top + new_h))
    return img.resize((w, h), Image.Resampling.LANCZOS)


def render_hero(slide: dict) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    sourced = find_sourced_image(slide["slide"])
    if sourced:
        hero = Image.open(sourced).convert("RGBA")
        bbox = hero.getbbox()
        if bbox:
            hero = hero.crop(bbox)
        max_w, max_h = 500, 900
        scale = min(max_w / hero.width, max_h / hero.height)
        hero = hero.resize(
            (int(hero.width * scale), int(hero.height * scale)),
            Image.Resampling.LANCZOS,
        )
        hero_x = W - hero.width - 8
        hero_y = H - hero.height
        img.paste(hero.convert("RGB"), (hero_x, hero_y), hero)
    else:
        hero_x, hero_y, hero_w, hero_h = 585, 0, 495, H
        draw_placeholder_frame(draw, hero_x, hero_y, hero_w, hero_h, "[hero photo]")

    y = 270
    for index, line in enumerate(slide["title_lines"]):
        fill = ACCENT if index == len(slide["title_lines"]) - 1 else BLACK
        draw.text((72, y), line, font=F_HERO, fill=fill)
        y += 104
    draw.text((76, y + 18), slide["subtitle"], font=F_SUB, fill=DARK_GRAY)
    return img


def render_body(slide: dict) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    center_text(draw, slide["label"], 80, F_LABEL)
    center_text(draw, slide["title"], 130, F_TITLE)

    top_bottom = draw_lines(draw, slide["top_lines"], 205)
    if top_bottom > FRAME_Y - 40:
        print(f"WARNING slide {slide['slide']} top text near frame: y={top_bottom}")

    sourced = find_sourced_image(slide["slide"])
    if sourced:
        img.paste(crop_image_to_frame(sourced, FRAME_W, FRAME_H), (FRAME_X, FRAME_Y))
    else:
        draw_placeholder_frame(draw, FRAME_X, FRAME_Y, FRAME_W, FRAME_H, "[reference photo]")

    lower_y = FRAME_BOTTOM + 65
    lower_bottom = draw_lines(draw, slide["lower_lines"], lower_y)

    source = slide.get("source", "")
    if source:
        source_y = 1268
        if lower_bottom > source_y - 32:
            print(f"WARNING slide {slide['slide']} lower text near source: y={lower_bottom}")
        center_text(draw, source, source_y, F_SOURCE, DARK_GRAY)

    return img


def main() -> None:
    OUT_DIR.mkdir(exist_ok=True)
    slides = load_slides()
    if not slides:
        raise SystemExit("No slide JSON blocks found in flow.md")

    for slide in slides:
        rendered = render_hero(slide) if slide["layout"] == "hero" else render_body(slide)
        out = OUT_DIR / f"slide_{slide['slide']}.png"
        rendered.save(out)
        if rendered.size != (W, H):
            raise SystemExit(f"{out} has wrong size: {rendered.size}")
        print(f"saved {out} ({W}x{H})")


if __name__ == "__main__":
    main()

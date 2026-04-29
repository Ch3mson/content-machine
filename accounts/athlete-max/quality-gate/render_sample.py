from pathlib import Path
import re
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "sample-slide.png"

W, H = 1080, 1350
BG = "#FFFFFF"
BLACK = "#111111"
GRAY = "#444444"
LIGHT_GRAY = "#F2F2F2"
MID_GRAY = "#D9D9D9"
RED = "#B00000"

FONT_REG = "C:/Windows/Fonts/arial.ttf"
FONT_BOLD = "C:/Windows/Fonts/arialbd.ttf"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size)


F_LABEL = font(FONT_BOLD, 34)
F_TITLE = font(FONT_BOLD, 58)
F_BODY = font(FONT_REG, 31)
F_BODY_BOLD = font(FONT_BOLD, 31)
F_PLACEHOLDER = font(FONT_BOLD, 30)
F_SOURCE = font(FONT_REG, 20)


def text_width(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont) -> int:
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0]


def center_text(draw: ImageDraw.ImageDraw, text: str, y: int, fnt: ImageFont.FreeTypeFont, fill=BLACK):
    x = (W - text_width(draw, text, fnt)) // 2
    draw.text((x, y), text, font=fnt, fill=fill)


def draw_centered_lines(
    draw: ImageDraw.ImageDraw,
    lines: list[str],
    y: int,
    fnt: ImageFont.FreeTypeFont,
    fill=BLACK,
    line_gap: int = 8,
) -> int:
    current_y = y
    for line in lines:
        if not line:
            current_y += int(fnt.size * 0.58)
            continue
        center_text(draw, line, current_y, fnt, fill)
        current_y += fnt.size + line_gap
    return current_y


def draw_centered_rich_line(
    draw: ImageDraw.ImageDraw,
    segments: list[tuple[str, ImageFont.FreeTypeFont, str]],
    y: int,
):
    total = sum(text_width(draw, text, fnt) for text, fnt, _ in segments)
    x = (W - total) // 2
    for text, fnt, fill in segments:
        draw.text((x, y), text, font=fnt, fill=fill)
        x += text_width(draw, text, fnt)


def main():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Exact copy from sample-copy.md, manually line-broken to fit the fixed design.
    label = "what to avoid:"
    title = "starting training dehydrated"
    top_lines = [
        "if you play forward, your first 5 meters decide the chance.",
        "mild dehydration makes that first step cost more.",
        "",
        "you lose water overnight. when you start practice down",
        "even 2% of body mass, your blood carries less fluid",
        "and your heart works harder at the same pace.",
    ]
    fix_head = "the fix:"
    fix_text = " 500 ml water + electrolytes within 30 min of waking."
    lower_lines = [
        "this restores fluid volume before your first high-speed run,",
        "so your brain and legs are not catching up during finishing drills.",
    ]
    source_lines = [
        "source: journal of the international society of sports nutrition / nih",
        "medicine & science in sports & exercise / nih",
        "(pmid: 20799932, 21738326)",
    ]

    center_text(draw, label, 80, F_LABEL, RED)
    center_text(draw, title, 126, F_TITLE, BLACK)
    draw_centered_lines(draw, top_lines, 212, F_BODY, BLACK, 7)

    frame_x, frame_y, frame_w, frame_h = 140, 515, 800, 450
    draw.rounded_rectangle(
        (frame_x, frame_y, frame_x + frame_w, frame_y + frame_h),
        radius=0,
        fill=LIGHT_GRAY,
        outline=MID_GRAY,
        width=3,
    )
    draw.line((frame_x, frame_y, frame_x + frame_w, frame_y + frame_h), fill=MID_GRAY, width=2)
    draw.line((frame_x + frame_w, frame_y, frame_x, frame_y + frame_h), fill=MID_GRAY, width=2)
    center_text(draw, "placeholder image frame", frame_y + 188, F_PLACEHOLDER, GRAY)
    center_text(draw, "soccer forward + hydration cue", frame_y + 228, F_SOURCE, GRAY)

    draw_centered_rich_line(draw, [(fix_head, F_BODY_BOLD, BLACK), (fix_text, F_BODY, BLACK)], 1018)
    draw_centered_lines(draw, lower_lines, 1070, F_BODY, BLACK, 8)
    draw_centered_lines(draw, source_lines, 1214, F_SOURCE, GRAY, 4)

    img.save(OUT)
    assert img.size == (1080, 1350), img.size
    print(f"saved {OUT} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()

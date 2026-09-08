"""
Font / caption-style tests for antigpt.

Same hook copy and photo as post 2 slide 1. Each variant is a different
TikTok-native treatment. Does not overwrite published posts.

Run from repo root:
    python3 accounts/antigpt/quality-gate/attempts/attempt-006-2026-09-08-caption-fonts/render_font_tests.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

TARGET_W, TARGET_H = 1080, 1920
TARGET_RATIO = TARGET_W / TARGET_H
SCALE = 3
RW, RH = TARGET_W * SCALE, TARGET_H * SCALE

PHOTO = (
    Path(__file__).resolve().parents[3]
    / "posts"
    / "2-essay-writing-tips"
    / "sourced"
    / "slide3.jpg"
)
OUT = Path(__file__).parent

HOOK = "3 tips for writing essays\nthat get an A in english\nswipe →"
FONTS = Path(__file__).resolve().parents[3] / "assets" / "fonts"

VARIANTS = [
    {
        "id": "a-current-stroke",
        "label": "A  current\nArial Bold + black stroke",
        "style": "stroke",
        "font": "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "size": 38,
    },
    {
        "id": "b-tiktok-boxed",
        "label": "B  tiktok boxed\nTikTok Sans + rounded highlight",
        "style": "boxed",
        "font": str(FONTS / "TikTokSans-Bold.ttf"),
        "size": 40,
    },
    {
        "id": "c-montserrat-boxed",
        "label": "C  montserrat boxed\nMontserrat ExtraBold + highlight",
        "style": "boxed",
        "font": str(Path.home() / "Library/Fonts/Montserrat-ExtraBold.ttf"),
        "size": 40,
    },
    {
        "id": "d-arial-rounded-boxed",
        "label": "D  classic 2020\nArial Rounded + highlight",
        "style": "boxed",
        "font": "/System/Library/Fonts/Supplemental/Arial Rounded Bold.ttf",
        "size": 40,
    },
    {
        "id": "e-hormozi",
        "label": "E  hormozi\nImpact + black box + yellow word",
        "style": "hormozi",
        "font": "/System/Library/Fonts/Supplemental/Impact.ttf",
        "size": 48,
    },
    {
        "id": "f-montserrat-block",
        "label": "F  montserrat block\nC font + E solid highlight",
        "style": "block",
        "font": str(Path.home() / "Library/Fonts/Montserrat-ExtraBold.ttf"),
        "size": 40,
    },
]


def load_font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size * SCALE)


def photo_bg() -> Image.Image:
    img = Image.open(PHOTO).convert("RGB")
    w, h = img.size
    ratio = w / h
    if ratio > TARGET_RATIO:
        new_w = int(h * TARGET_RATIO)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    elif ratio < TARGET_RATIO:
        new_h = int(w / TARGET_RATIO)
        if new_h <= h:
            top = (h - new_h) // 2
            img = img.crop((0, top, w, top + new_h))
    img = img.resize((RW, RH), Image.LANCZOS)
    img = ImageEnhance.Contrast(img).enhance(1.12)
    img = ImageEnhance.Color(img).enhance(0.85)
    overlay = Image.new("RGB", (RW, RH), (0, 0, 0))
    return Image.blend(img, overlay, 0.55)


def draw_label(draw: ImageDraw.ImageDraw, text: str) -> None:
    font = load_font("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 22)
    y = 80 * SCALE
    for line in text.split("\n"):
        draw.text((60 * SCALE, y), line, font=font, fill=(255, 220, 80), stroke_width=4 * SCALE, stroke_fill="black")
        y += 32 * SCALE


def block_height(lines: list[str], font: ImageFont.FreeTypeFont, gap: int) -> int:
    total = 0
    for line in lines:
        b = font.getbbox(line)
        total += (b[3] - b[1]) + gap
    return total - gap


def draw_stroke(draw, lines, font, gap) -> None:
    h = block_height(lines, font, gap)
    y = (RH - h) // 2
    for line in lines:
        b = font.getbbox(line)
        lw, lh = b[2] - b[0], b[3] - b[1]
        x = (RW - lw) // 2
        draw.text((x, y), line, font=font, fill="white", stroke_width=3 * SCALE, stroke_fill="black")
        y += lh + gap


def draw_boxed(draw, lines, font, gap) -> None:
    pad_x, pad_y = 22 * SCALE, 10 * SCALE
    radius = 18 * SCALE
    h = 0
    sizes = []
    for line in lines:
        b = font.getbbox(line)
        lw, lh = b[2] - b[0], b[3] - b[1]
        sizes.append((lw, lh))
        h += lh + pad_y * 2 + gap
    h -= gap
    y = (RH - h) // 2
    for line, (lw, lh) in zip(lines, sizes):
        box_w = lw + pad_x * 2
        box_h = lh + pad_y * 2
        x = (RW - box_w) // 2
        draw.rounded_rectangle([x, y, x + box_w, y + box_h], radius=radius, fill=(0, 0, 0))
        draw.text((x + pad_x, y + pad_y), line, font=font, fill="white")
        y += box_h + gap


def draw_hormozi(draw, lines, font, gap) -> None:
    # One shared black box; last content word of line 2 in yellow.
    pad_x, pad_y = 28 * SCALE, 18 * SCALE
    sizes = []
    for line in lines:
        b = font.getbbox(line)
        sizes.append((b[2] - b[0], b[3] - b[1]))
    box_w = max(s[0] for s in sizes) + pad_x * 2
    box_h = sum(s[1] for s in sizes) + gap * (len(lines) - 1) + pad_y * 2
    x0 = (RW - box_w) // 2
    y0 = (RH - box_h) // 2
    draw.rounded_rectangle([x0, y0, x0 + box_w, y0 + box_h], radius=8 * SCALE, fill=(0, 0, 0))
    y = y0 + pad_y
    for i, line in enumerate(lines):
        lw, lh = sizes[i]
        x = (RW - lw) // 2
        if i == 1 and " A " in f" {line} ":
            # paint "A" yellow, rest white
            parts = line.split(" A ", 1)
            left, right = parts[0] + " ", " A " + (parts[1] if len(parts) > 1 else "")
            # simpler: whole line white except the isolated A
            cursor = x
            tokens = line.split(" ")
            for ti, tok in enumerate(tokens):
                fill = (255, 230, 0) if tok == "A" else "white"
                draw.text((cursor, y), tok, font=font, fill=fill)
                cursor += font.getlength(tok + (" " if ti < len(tokens) - 1 else ""))
        else:
            draw.text((x, y), line, font=font, fill="white")
        y += lh + gap


def draw_block(draw, lines, font, gap) -> None:
    """One solid highlight behind every line, no air between rows (E fill, any font)."""
    pad_x, pad_y = 26 * SCALE, 16 * SCALE
    sizes = []
    for line in lines:
        b = font.getbbox(line)
        sizes.append((b[2] - b[0], b[3] - b[1]))
    box_w = max(s[0] for s in sizes) + pad_x * 2
    box_h = sum(s[1] for s in sizes) + gap * (len(lines) - 1) + pad_y * 2
    x0 = (RW - box_w) // 2
    y0 = (RH - box_h) // 2
    draw.rounded_rectangle([x0, y0, x0 + box_w, y0 + box_h], radius=10 * SCALE, fill=(0, 0, 0))
    y = y0 + pad_y
    for line, (lw, lh) in zip(lines, sizes):
        draw.text(((RW - lw) // 2, y), line, font=font, fill="white")
        y += lh + gap


def render(variant: dict) -> Path:
    img = photo_bg()
    draw = ImageDraw.Draw(img)
    font = load_font(variant["font"], variant["size"])
    lines = HOOK.split("\n")
    gap = 14 * SCALE
    if variant["style"] == "stroke":
        draw_stroke(draw, lines, font, gap)
    elif variant["style"] == "boxed":
        draw_boxed(draw, lines, font, 10 * SCALE)
    elif variant["style"] == "hormozi":
        draw_hormozi(draw, lines, font, 12 * SCALE)
    elif variant["style"] == "block":
        draw_block(draw, lines, font, 12 * SCALE)
    draw_label(draw, variant["label"])
    out = img.resize((TARGET_W, TARGET_H), Image.LANCZOS)
    path = OUT / f"{variant['id']}.png"
    out.save(path, "PNG")
    print(f"Saved {path.name}")
    return path


def contact_sheet(paths: list[Path]) -> None:
    thumbs = [Image.open(p) for p in paths]
    s = 0.28
    tw, th = int(TARGET_W * s), int(TARGET_H * s)
    gap = 16
    sheet = Image.new("RGB", (tw * len(thumbs) + gap * (len(thumbs) + 1), th + gap * 2), (30, 30, 30))
    for i, im in enumerate(thumbs):
        sheet.paste(im.resize((tw, th), Image.LANCZOS), (gap + i * (tw + gap), gap))
    sheet.save(OUT / "contact-sheet.png", "PNG")
    print("Saved contact-sheet.png")


def main() -> None:
    paths = [render(v) for v in VARIANTS]
    contact_sheet(paths)
    # unlabeled F so the style can be judged without the yellow note
    f = next(v for v in VARIANTS if v["id"] == "f-montserrat-block")
    img = photo_bg()
    draw = ImageDraw.Draw(img)
    font = load_font(f["font"], f["size"])
    draw_block(draw, HOOK.split("\n"), font, 12 * SCALE)
    clean = img.resize((TARGET_W, TARGET_H), Image.LANCZOS)
    clean.save(OUT / "f-montserrat-block-clean.png", "PNG")
    print("Saved f-montserrat-block-clean.png")


if __name__ == "__main__":
    main()

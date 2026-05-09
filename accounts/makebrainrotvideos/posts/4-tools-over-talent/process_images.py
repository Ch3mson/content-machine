"""
Render all 7 slides for: Tools > Talent (The Automation Stack)

Format: tyronetrains-style — numbered header + explanation paragraph
Rendering: athlete-stories circular outline technique

Design source: accounts/makebrainrotvideos/design.md (Locked)
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

# --- Canvas ---
TARGET_W = 1080
TARGET_H = 1920
TARGET_RATIO = TARGET_W / TARGET_H

# --- Text config ---
HEADER_SIZE = 40
BODY_SIZE = 30
HOOK_SIZE = 38
CTA_LABEL_SIZE = 34
CTA_URL_SIZE = 44
OUTLINE_WIDTH = 3
LINE_SPACING = 16
HEADER_BODY_GAP = 30
MARGIN_X = 140

# --- Sourced images ---
SOURCED_DIR = Path(__file__).parent / "sourced"
IMAGE_MAP = {
    1: "slide1.jpg",
    2: "slide2.jpg",
    3: "slide3.jpg",
    4: "slide4.jpg",
    5: "slide5.jpg",
    6: "slide6.jpg",
    7: "slide7.jpg",
}

# --- Slide definitions with manual line breaks ---
SLIDES = [
    {
        "id": 1,
        "role": "hook",
        "header": None,
        "body": "The top 1% of creators aren't\nmore talented than you.",
        "overlay_pct": 0.65,
    },
    {
        "id": 2,
        "role": "step",
        "header": "1. They Use Systems",
        "body": "The biggest channels operate like factories.\nThey don't wait for inspiration;\nthey rely on automation.",
        "overlay_pct": 0.75,
    },
    {
        "id": 3,
        "role": "step",
        "header": "2. Automate Research",
        "body": "Stop scrolling for ideas.\nUse AI to scrape viral hooks and\nrewrite them for your niche.",
        "overlay_pct": 0.75,
    },
    {
        "id": 4,
        "role": "step",
        "header": "3. Automate Visuals",
        "body": "Don't spend hours searching for B-roll.\nGenerate dynamic, high-retention\nbackgrounds instantly.",
        "overlay_pct": 0.75,
    },
    {
        "id": 5,
        "role": "step",
        "header": "4. Automate Audio",
        "body": "Your voiceover needs to sound professional.\nUse high-end AI voices\nto keep viewers hooked.",
        "overlay_pct": 0.75,
    },
    {
        "id": 6,
        "role": "step",
        "header": "5. Scale the Output",
        "body": "Automating these 4 steps lets you\neasily post 3 times a day.\nVolume beats talent.",
        "overlay_pct": 0.75,
    },
    {
        "id": 7,
        "role": "cta",
        "header": None,
        "body": "The all-in-one system I use\nto automate everything:",
        "cta_url": "MakeBrainrotVideos.com",
        "overlay_pct": 0.50,
    },
]


def load_font(size: int, bold: bool = True) -> ImageFont.FreeTypeFont:
    if bold:
        candidates = [
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
            "arialbd.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        ]
    else:
        candidates = [
            "/System/Library/Fonts/Supplemental/Arial.ttf",
            "arial.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    # Fallback: try bold even for regular
    for path in [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def normalize_to_9_16(img: Image.Image) -> Image.Image:
    """Center-crop and resize to 1080x1920."""
    w, h = img.size
    current_ratio = w / h

    if current_ratio > TARGET_RATIO:
        new_w = int(h * TARGET_RATIO)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    elif current_ratio < TARGET_RATIO:
        new_h = int(w / TARGET_RATIO)
        if new_h <= h:
            top = (h - new_h) // 2
            img = img.crop((0, top, w, top + new_h))

    return img.resize((TARGET_W, TARGET_H), Image.LANCZOS)


def apply_treatment(img: Image.Image) -> Image.Image:
    """Contrast boost + slight desaturation per image.md."""
    img = ImageEnhance.Contrast(img).enhance(1.12)
    img = ImageEnhance.Color(img).enhance(0.85)
    return img


def apply_dark_overlay(img: Image.Image, opacity: float) -> Image.Image:
    overlay = Image.new("RGB", (TARGET_W, TARGET_H), (0, 0, 0))
    return Image.blend(img, overlay, opacity)


def make_dark_bg() -> Image.Image:
    """Solid dark background for CTA slide (fallback)."""
    img = Image.new("RGB", (TARGET_W, TARGET_H))
    draw = ImageDraw.Draw(img)
    for y in range(TARGET_H):
        ratio = y / TARGET_H
        v = int(5 + 10 * ratio)
        draw.line([(0, y), (TARGET_W, y)], fill=(v, v, int(v * 1.5)))
    return img


def draw_text_block(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.FreeTypeFont,
    start_y: int,
) -> int:
    """Draw centered text with circular outline. Returns y after last line."""
    lines = text.split("\n")

    current_y = start_y
    for line in lines:
        bbox = font.getbbox(line)
        line_w = bbox[2] - bbox[0]
        line_h = bbox[3] - bbox[1]
        x = (TARGET_W - line_w) // 2

        # Clamp to margin
        if x < MARGIN_X:
            x = MARGIN_X

        # Circular outline
        for dx in range(-OUTLINE_WIDTH, OUTLINE_WIDTH + 1):
            for dy in range(-OUTLINE_WIDTH, OUTLINE_WIDTH + 1):
                if dx * dx + dy * dy <= OUTLINE_WIDTH * OUTLINE_WIDTH:
                    draw.text(
                        (x + dx, current_y + dy), line, font=font, fill="black"
                    )

        # White text on top
        draw.text((x, current_y), line, font=font, fill="white")
        current_y += line_h + LINE_SPACING

    return current_y


def calc_text_height(text: str, font: ImageFont.FreeTypeFont) -> int:
    """Calculate total height of a text block."""
    lines = text.split("\n")
    total = 0
    for line in lines:
        bbox = font.getbbox(line)
        total += bbox[3] - bbox[1] + LINE_SPACING
    return total - LINE_SPACING


def render_slide(slide: dict) -> Image.Image:
    # Background
    photo_file = IMAGE_MAP.get(slide["id"])
    if photo_file:
        photo_path = SOURCED_DIR / photo_file
        if photo_path.exists():
            img = Image.open(photo_path).convert("RGB")
            img = normalize_to_9_16(img)
            img = apply_treatment(img)
            img = apply_dark_overlay(img, slide["overlay_pct"])
        else:
            img = make_dark_bg()
    else:
        img = make_dark_bg()

    draw = ImageDraw.Draw(img)
    role = slide["role"]

    if role == "hook":
        font = load_font(HOOK_SIZE, bold=True)
        text_h = calc_text_height(slide["body"], font)
        start_y = (TARGET_H - text_h) // 2
        draw_text_block(draw, slide["body"], font, start_y)

    elif role == "step":
        header_font = load_font(HEADER_SIZE, bold=True)
        body_font = load_font(BODY_SIZE, bold=False)

        header_h = calc_text_height(slide["header"], header_font)
        body_h = calc_text_height(slide["body"], body_font)
        total_h = header_h + HEADER_BODY_GAP + body_h

        # Center the full text block vertically
        start_y = (TARGET_H - total_h) // 2

        y = draw_text_block(draw, slide["header"], header_font, start_y)
        y += HEADER_BODY_GAP - LINE_SPACING
        draw_text_block(draw, slide["body"], body_font, y)

    elif role == "cta":
        label_font = load_font(CTA_LABEL_SIZE, bold=False)
        url_font = load_font(CTA_URL_SIZE, bold=True)

        label_h = calc_text_height(slide["body"], label_font)
        url_h = calc_text_height(slide["cta_url"], url_font)
        total_h = label_h + 40 + url_h
        start_y = (TARGET_H - total_h) // 2

        y = draw_text_block(draw, slide["body"], label_font, start_y)
        y += 40 - LINE_SPACING
        draw_text_block(draw, slide["cta_url"], url_font, y)

    return img


def main() -> None:
    out_dir = Path(__file__).parent / "processed"
    out_dir.mkdir(exist_ok=True)

    for slide in SLIDES:
        img = render_slide(slide)
        out_path = out_dir / f"slide_{slide['id']:02d}.png"
        img.save(out_path, "PNG")
        print(f"Saved: {out_path}")

    print(f"\nDone. {len(SLIDES)} slides rendered to {out_dir}")


if __name__ == "__main__":
    main()

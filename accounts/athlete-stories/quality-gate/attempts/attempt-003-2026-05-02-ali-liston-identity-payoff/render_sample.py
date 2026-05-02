"""
Render the full 12-slide Ali vs. Liston quality-gate sample.

Usage:
    python render_sample.py

Output: slide_1.png through slide_12.png in this directory.

Each slide renders as:
    - 1080x1920 PNG
    - Full-bleed photo, center-cropped to 9:16
    - B&W conversion, 1.3x contrast
    - Vintage paper overlay + vignette
    - Centered white Arial Bold 36pt text with black 3px outline
"""

import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

ATTEMPT_DIR = Path(__file__).resolve().parent
ACCOUNT_DIR = Path(__file__).resolve().parents[3]
PROJECT_DIR = Path(__file__).resolve().parents[5]
ALI_SOURCED_DIR = ACCOUNT_DIR / "Muhammad Ali" / "sourced"
PRODUCT_PHONE_IMAGE = PROJECT_DIR / "product" / "assets" / "phone-holding" / "9x16-boxing-02.jpeg"

TARGET_W = 1080
TARGET_H = 1920
TARGET_RATIO = TARGET_W / TARGET_H
CONTRAST_FACTOR = 1.3
FONT_SIZE = 36
OUTLINE_WIDTH = 3
LINE_SPACING = 16
MARGIN_X = 140
UPSCALE_SHORT_EDGE = 2160

SEED = 5032026  # consistent overlay across all slides in this attempt

SLIDE_TEXTS = {
    1: (
        "They called Liston a monster.\n"
        "Mob ties. Prison record.\n"
        "He had flattened Floyd Patterson —\n"
        "a former heavyweight champion —\n"
        "in 124 seconds."
    ),
    2: (
        "Clay was 22.\n"
        "His hands were small.\n"
        "The odds said he would not survive three rounds."
    ),
    3: (
        'At the weigh-in, Clay went wild.\n'
        '"I\'m gonna get you, sucker!"\n'
        "Reporters laughed. The commission threatened a fine.\n"
        "Liston never blinked."
    ),
    4: (
        "But that was the game.\n"
        "Clay needed Liston angry.\n"
        "An angry Liston comes forward.\n"
        "A forward Liston is there\n"
        "when the round comes."
    ),
    5: (
        "Three nights before the fight.\n"
        "2 AM. Liston's motel.\n"
        "Clay walks onto the lawn\n"
        "in a field jacket and screams."
    ),
    6: (
        '"Round seven. Round seven. Round seven."\n'
        "Over and over until the floodlights came on.\n"
        "Guests watching from windows.\n"
        "A 22-year-old screaming\n"
        "like he was predicting the future\n"
        "at a man who had never lost."
    ),
    7: (
        "Reporters called it a breakdown.\n"
        "Fear, they said. The moment caught up to him."
    ),
    8: (
        "He was planting the future.\n"
        "Until his mind and body believed\n"
        "the words he shouted."
    ),
    9: (
        "Round seven. Liston does not answer the bell.\n"
        "The exact round Clay had been screaming\n"
        "into the Chicago night."
    ),
    10: (
        "Before Clay was Muhammad Ali,\n"
        "he kept rehearsing these moments.\n"
        "Shouted words into existence\n"
        "until he shaped his identity\n"
        "into something unstoppable.\n"
        "The mind forces the body to change."
    ),
    11: (
        "I use w(inner) the same way.\n"
        "It builds personalized visualization tracks\n"
        "so I can imagine myself winning,\n"
        "performing at my potential.\n"
        "I rewired my brain so my body followed."
    ),
    12: (
        '"I figured I whooped him\n'
        'in my mind\n'
        'before the fight ever started."\n'
        '— Muhammad Ali'
    ),
}

SOURCE_IMAGES = {
    1: [ALI_SOURCED_DIR / "liston_portrait.png"],
    2: [ALI_SOURCED_DIR / "ali_young.png"],
    3: [ALI_SOURCED_DIR / "ali_liston_weighin.jpg"],
    4: [ALI_SOURCED_DIR / "slide_7.jpg"],
    5: [ALI_SOURCED_DIR / "ali_fight_1.jpg"],
    6: [ALI_SOURCED_DIR / "ali_liston_fight.jpg"],
    7: [ALI_SOURCED_DIR / "slide_12.jpg"],
    8: [ALI_SOURCED_DIR / "slide_8.jpg"],
    9: [ALI_SOURCED_DIR / "slide_9.jpg", ALI_SOURCED_DIR / "ali_liston_fight.jpg"],
    10: [ALI_SOURCED_DIR / "slide_10.jpg", ALI_SOURCED_DIR / "ali_fight_1.jpg"],
    11: [PRODUCT_PHONE_IMAGE],
    12: [ALI_SOURCED_DIR / "ali_portrait.jpg"],
}


def load_font() -> ImageFont.FreeTypeFont:
    for path in ["C:/Windows/Fonts/arialbd.ttf", "arialbd.ttf"]:
        try:
            return ImageFont.truetype(path, FONT_SIZE)
        except OSError:
            continue
    return ImageFont.load_default()


def normalize_to_9_16(img: Image.Image) -> Image.Image:
    """Center-crop or pad the image to 9:16, then resize to 1080x1920."""
    img = img.convert("RGB")
    w, h = img.size
    current_ratio = w / h

    if current_ratio > TARGET_RATIO:
        # Image is wider than 9:16 — crop sides
        new_w = int(h * TARGET_RATIO)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    elif current_ratio < TARGET_RATIO:
        # Image is taller than 9:16 — pad with black bars
        new_h = int(w / TARGET_RATIO)
        if new_h <= h:
            top = (h - new_h) // 2
            img = img.crop((0, top, w, top + new_h))
        else:
            background = Image.new("RGB", (w, new_h), (0, 0, 0))
            top = (new_h - h) // 2
            background.paste(img, (0, top))
            img = background

    return img.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)


def upscale_and_sharpen(img: Image.Image) -> Image.Image:
    """Improve low-resolution source photos before crop and treatment."""
    img = img.convert("RGB")
    w, h = img.size
    short_edge = min(w, h)
    if short_edge < UPSCALE_SHORT_EDGE:
        scale = UPSCALE_SHORT_EDGE / short_edge
        new_size = (round(w * scale), round(h * scale))
        img = img.resize(new_size, Image.Resampling.LANCZOS)

    img = img.filter(ImageFilter.UnsharpMask(radius=1.2, percent=135, threshold=3))
    return img


def convert_to_bw(img: Image.Image) -> Image.Image:
    img = img.convert("L")
    img = ImageEnhance.Contrast(img).enhance(CONTRAST_FACTOR)
    return img.convert("RGB")


def create_paper_overlay(width: int, height: int, seed: int) -> Image.Image:
    random.seed(seed)
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    pixels = overlay.load()

    for y in range(height):
        for x in range(width):
            pixels[x, y] = (
                random.randint(180, 220),
                random.randint(160, 195),
                random.randint(130, 160),
                random.randint(15, 35),
            )

    for _ in range(width * height // 80):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        color = (
            random.randint(100, 150),
            random.randint(80, 130),
            random.randint(60, 100),
            random.randint(10, 30),
        )
        for dx in range(random.randint(1, 3)):
            for dy in range(random.randint(1, 3)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    pixels[nx, ny] = color

    vignette = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    v_pixels = vignette.load()
    cx, cy = width // 2, height // 2
    max_dist = (cx**2 + cy**2) ** 0.5

    for y in range(height):
        for x in range(width):
            dist = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
            ratio = dist / max_dist
            alpha = min(int(ratio * ratio * 80), 120)
            v_pixels[x, y] = (0, 0, 0, alpha)

    return Image.alpha_composite(overlay, vignette)


def add_text_overlay(img: Image.Image, text: str, font: ImageFont.ImageFont) -> Image.Image:
    draw = ImageDraw.Draw(img)
    lines = text.split("\n")
    line_heights = []

    for line in lines:
        bbox = font.getbbox(line)
        line_heights.append(bbox[3] - bbox[1])

    total_height = sum(line_heights) + LINE_SPACING * (len(lines) - 1)
    y = (img.height - total_height) // 2

    for index, line in enumerate(lines):
        bbox = font.getbbox(line)
        line_width = bbox[2] - bbox[0]
        x = (img.width - line_width) // 2
        if x < MARGIN_X:
            x = MARGIN_X
        draw.text(
            (x, y),
            line,
            font=font,
            fill="white",
            stroke_width=OUTLINE_WIDTH,
            stroke_fill="black",
        )
        y += line_heights[index] + LINE_SPACING

    return img


def find_source_image(slide_num: int) -> Path | None:
    for source_path in SOURCE_IMAGES[slide_num]:
        if source_path.exists():
            return source_path
    return None


def render_slide(slide_num: int, output_dir: Path) -> None:
    source_path = find_source_image(slide_num)
    if source_path is None:
        candidates = "\n    ".join(str(path) for path in SOURCE_IMAGES[slide_num])
        print(f"  WARNING: No source image for slide {slide_num}. Checked:\n    {candidates}")
        return

    output_path = output_dir / f"slide_{slide_num}.png"

    img = Image.open(source_path)
    img = upscale_and_sharpen(img)
    img = normalize_to_9_16(img)
    img = convert_to_bw(img)
    img = Image.alpha_composite(
        img.convert("RGBA"),
        create_paper_overlay(TARGET_W, TARGET_H, SEED),
    ).convert("RGB")
    img = add_text_overlay(img, SLIDE_TEXTS[slide_num], load_font())
    img.save(output_path, "PNG")
    print(f"  Created: {output_path}")


def main() -> None:
    if not ALI_SOURCED_DIR.exists():
        print(f"ERROR: No Ali sourced directory found at {ALI_SOURCED_DIR}")
        return

    if not PRODUCT_PHONE_IMAGE.exists():
        print(f"ERROR: No product phone image found at {PRODUCT_PHONE_IMAGE}")
        return

    print(f"Rendering {len(SLIDE_TEXTS)} slides...")
    for num in sorted(SLIDE_TEXTS.keys()):
        render_slide(num, ATTEMPT_DIR)

    print("Done.")


if __name__ == "__main__":
    main()

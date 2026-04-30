from pathlib import Path
import random

from PIL import Image, ImageDraw, ImageEnhance, ImageFont


ATTEMPT_DIR = Path(__file__).resolve().parent
ACCOUNT_DIR = Path(__file__).resolve().parents[3]
SOURCE_IMAGE = ACCOUNT_DIR / "Michael Jordan" / "sourced" / "the-grind-pistons-foul.jpg"
OUTPUT_IMAGE = ATTEMPT_DIR / "sample-slide.png"

TARGET_W = 1080
TARGET_H = 1920
TARGET_RATIO = TARGET_W / TARGET_H
CONTRAST_FACTOR = 1.3
FONT_SIZE = 36
OUTLINE_WIDTH = 3
LINE_SPACING = 16
MARGIN_X = 140

SAMPLE_TEXT = "Detroit owned him.\nThree straight years.\nThe Pistons called it the Jordan Rules.\nHe kept coming back."


def load_font() -> ImageFont.FreeTypeFont:
    for path in ["C:/Windows/Fonts/arialbd.ttf", "arialbd.ttf"]:
        try:
            return ImageFont.truetype(path, FONT_SIZE)
        except OSError:
            continue
    return ImageFont.load_default()


def normalize_to_9_16(img: Image.Image) -> Image.Image:
    img = img.convert("RGB")
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
        else:
            background = Image.new("RGB", (w, new_h), (0, 0, 0))
            top = (new_h - h) // 2
            background.paste(img, (0, top))
            img = background

    return img.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)


def convert_to_bw(img: Image.Image) -> Image.Image:
    img = img.convert("L")
    img = ImageEnhance.Contrast(img).enhance(CONTRAST_FACTOR)
    return img.convert("RGB")


def create_paper_overlay(width: int, height: int) -> Image.Image:
    random.seed(4292026)
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
        x = max((img.width - line_width) // 2, MARGIN_X)
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


def main() -> None:
    if not SOURCE_IMAGE.exists():
        raise FileNotFoundError(f"Source image missing: {SOURCE_IMAGE}")

    img = Image.open(SOURCE_IMAGE)
    img = normalize_to_9_16(img)
    img = convert_to_bw(img)
    img = Image.alpha_composite(img.convert("RGBA"), create_paper_overlay(TARGET_W, TARGET_H)).convert("RGB")
    img = add_text_overlay(img, SAMPLE_TEXT, load_font())
    img.save(OUTPUT_IMAGE, "PNG")
    print(f"Created: {OUTPUT_IMAGE}")


if __name__ == "__main__":
    main()

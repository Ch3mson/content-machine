from pathlib import Path
import random
import re

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[3]
ATTEMPT_DIR = Path(__file__).resolve().parent
SOURCE_IMAGE = ROOT / "CR7" / "sourced" / "the-weight-empty-stadium.jpg"
OUTPUT = ATTEMPT_DIR / "sample-slide.png"
WIDTH, HEIGHT = 1080, 1920
SIDE_MARGIN = 140
FONT_PATH = Path("C:/Windows/Fonts/arialbd.ttf")
FONT_SIZE = 36
STROKE_WIDTH = 3
LINE_SPACING = 16


def read_copy() -> str:
    copy_md = (ATTEMPT_DIR / "sample-copy.md").read_text(encoding="utf-8")
    match = re.search(r"```text\n(.*?)\n```", copy_md, re.S)
    if not match:
        raise ValueError("sample-copy.md must contain a text code block")
    return match.group(1)


def center_crop(image: Image.Image) -> Image.Image:
    image = image.convert("RGB")
    src_w, src_h = image.size
    target_ratio = WIDTH / HEIGHT
    src_ratio = src_w / src_h

    if src_ratio > target_ratio:
        new_w = int(src_h * target_ratio)
        left = (src_w - new_w) // 2
        image = image.crop((left, 0, left + new_w, src_h))
    else:
        new_h = int(src_w / target_ratio)
        top = max((src_h - new_h) // 2, 0)
        image = image.crop((0, top, src_w, top + new_h))

    return image.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)


def fallback_background() -> Image.Image:
    image = Image.new("RGB", (WIDTH, HEIGHT), (22, 22, 22))
    draw = ImageDraw.Draw(image)
    for y in range(HEIGHT):
        shade = int(18 + (y / HEIGHT) * 55)
        draw.line([(0, y), (WIDTH, y)], fill=(shade, shade, shade))
    return image


def apply_account_treatment(image: Image.Image) -> Image.Image:
    image = ImageEnhance.Contrast(image.convert("L")).enhance(1.3).convert("RGB")

    random.seed(29)
    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    pixels = overlay.load()
    for _ in range(24000):
        x = random.randrange(WIDTH)
        y = random.randrange(HEIGHT)
        if random.random() < 0.78:
            color = (
                random.randint(180, 220),
                random.randint(160, 195),
                random.randint(130, 160),
                random.randint(15, 35),
            )
        else:
            color = (
                random.randint(100, 150),
                random.randint(80, 130),
                random.randint(60, 100),
                random.randint(10, 30),
            )
        pixels[x, y] = color

    vignette = Image.new("L", (WIDTH, HEIGHT), 0)
    vd = ImageDraw.Draw(vignette)
    max_radius = int((WIDTH**2 + HEIGHT**2) ** 0.5 / 2)
    center = (WIDTH // 2, HEIGHT // 2)
    for radius in range(max_radius, 0, -18):
        alpha = int(120 * (1 - radius / max_radius) ** 1.7)
        bbox = (
            center[0] - radius,
            center[1] - radius,
            center[0] + radius,
            center[1] + radius,
        )
        vd.ellipse(bbox, outline=alpha, width=18)
    vignette = vignette.filter(ImageFilter.GaussianBlur(48))
    dark = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 130))
    overlay = Image.alpha_composite(overlay, Image.merge("RGBA", [dark.getchannel(0), dark.getchannel(1), dark.getchannel(2), vignette]))

    return Image.alpha_composite(image.convert("RGBA"), overlay).convert("RGB")


def draw_centered_text(image: Image.Image, text: str) -> None:
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(str(FONT_PATH), FONT_SIZE)
    lines = text.splitlines()
    line_heights = []
    line_widths = []

    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font, stroke_width=STROKE_WIDTH)
        line_widths.append(bbox[2] - bbox[0])
        line_heights.append(bbox[3] - bbox[1])

    max_width = max(line_widths)
    if max_width > WIDTH - (SIDE_MARGIN * 2):
        raise ValueError(f"Text exceeds safe margins: {max_width}px")

    total_height = sum(line_heights) + LINE_SPACING * (len(lines) - 1)
    y = (HEIGHT - total_height) // 2
    for line, line_width, line_height in zip(lines, line_widths, line_heights):
        x = (WIDTH - line_width) // 2
        draw.text(
            (x, y),
            line,
            font=font,
            fill="#FFFFFF",
            stroke_width=STROKE_WIDTH,
            stroke_fill="#000000",
        )
        y += line_height + LINE_SPACING


def main() -> None:
    if SOURCE_IMAGE.exists():
        image = center_crop(Image.open(SOURCE_IMAGE))
    else:
        image = fallback_background()
    image = apply_account_treatment(image)
    draw_centered_text(image, read_copy())
    image.save(OUTPUT)


if __name__ == "__main__":
    main()

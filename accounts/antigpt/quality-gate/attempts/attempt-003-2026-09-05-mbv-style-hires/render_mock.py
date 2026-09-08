"""
Render the attempt-003 mock for antigpt: makebrainrotvideos styling, high-res text.

Same layout and sizes as attempt-002 (copied from
accounts/makebrainrotvideos/posts/5-ugly-content-strategy/process_images.py).
Two rendering changes for clean text edges:
  1. Supersample: draw at SCALE x (3240x5760) and downsample with Lanczos.
  2. Outline via Pillow's anti-aliased stroke_width instead of stamping the
     glyph at many pixel offsets.
All design values below are in final-canvas pixels; SCALE is applied at draw time.

Run from the repo root:
    python3 accounts/antigpt/quality-gate/attempts/attempt-003-2026-09-05-mbv-style-hires/render_mock.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

# --- Canvas ---
TARGET_W = 1080
TARGET_H = 1920
TARGET_RATIO = TARGET_W / TARGET_H
SCALE = 3  # supersampling factor for text rendering
RW, RH = TARGET_W * SCALE, TARGET_H * SCALE

# --- Text config (identical to makebrainrotvideos post 5) ---
HEADER_SIZE = 40
BODY_SIZE = 30
HOOK_SIZE = 38
CTA_LABEL_SIZE = 34
CTA_URL_SIZE = 44
OUTLINE_WIDTH = 3
LINE_SPACING = 16
HEADER_BODY_GAP = 30
MARGIN_X = 140

# --- Sourced images (empty for now: solid black) ---
SOURCED_DIR = Path(__file__).parent / "sourced"
IMAGE_MAP: dict[int, str] = {}

# --- Slide definitions with manual line breaks (mirror copy.md) ---
SLIDES = [
    {
        "id": 1,
        "role": "hook",
        "header": None,
        "body": "You reread your notes four times\nand still blanked in the exam.",
        "overlay_pct": 0.65,
    },
    {
        "id": 2,
        "role": "step",
        "header": "1. Why It Fails",
        "body": "Rereading feels productive because\nthe page looks familiar. Familiar is\nnot the same as retrievable.",
        "overlay_pct": 0.75,
    },
    {
        "id": 3,
        "role": "step",
        "header": "2. Blurting",
        "body": "Read one page. Close it. On a blank\nsheet, write everything you remember.\nOpen the page. Mark what you missed in red.",
        "overlay_pct": 0.75,
    },
    {
        "id": 4,
        "role": "step",
        "header": "3. The Red Is Your Study Plan",
        "body": "Reread only the red. Blurt the same\npage again tomorrow. Two rounds\nof this beats four rereads.",
        "overlay_pct": 0.75,
    },
    {
        "id": 5,
        "role": "cta",
        "header": None,
        "body": "If ChatGPT drafted your essay, run it\nthrough this before you submit.\nIt sounds like you and bypasses Turnitin:",
        "cta_url": "AntiGPT.me",
        "overlay_pct": 0.50,
    },
]


def load_font(size: int, bold: bool = True) -> ImageFont.FreeTypeFont:
    size = size * SCALE
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
    for path in [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    print("[font fallback] Arial not found; using default")
    return ImageFont.load_default()


def normalize_to_9_16(img: Image.Image) -> Image.Image:
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
    return img.resize((RW, RH), Image.LANCZOS)


def apply_treatment(img: Image.Image) -> Image.Image:
    img = ImageEnhance.Contrast(img).enhance(1.12)
    img = ImageEnhance.Color(img).enhance(0.85)
    return img


def apply_dark_overlay(img: Image.Image, opacity: float) -> Image.Image:
    overlay = Image.new("RGB", (RW, RH), (0, 0, 0))
    return Image.blend(img, overlay, opacity)


def make_black_bg() -> Image.Image:
    return Image.new("RGB", (RW, RH), (0, 0, 0))


def draw_text_block(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, start_y: int) -> int:
    """Centered white text with anti-aliased black stroke. Coordinates in render (scaled) px."""
    lines = text.split("\n")
    stroke = OUTLINE_WIDTH * SCALE
    spacing = LINE_SPACING * SCALE
    margin = MARGIN_X * SCALE
    current_y = start_y
    for line in lines:
        bbox = font.getbbox(line)
        line_w = bbox[2] - bbox[0]
        line_h = bbox[3] - bbox[1]
        x = (RW - line_w) // 2
        if x < margin:
            x = margin
        draw.text((x, current_y), line, font=font, fill="white", stroke_width=stroke, stroke_fill="black")
        current_y += line_h + spacing
    return current_y


def calc_text_height(text: str, font: ImageFont.FreeTypeFont) -> int:
    total = 0
    for line in text.split("\n"):
        bbox = font.getbbox(line)
        total += bbox[3] - bbox[1] + LINE_SPACING * SCALE
    return total - LINE_SPACING * SCALE


def render_slide(slide: dict) -> Image.Image:
    photo_file = IMAGE_MAP.get(slide["id"])
    if photo_file and (SOURCED_DIR / photo_file).exists():
        img = Image.open(SOURCED_DIR / photo_file).convert("RGB")
        img = normalize_to_9_16(img)
        img = apply_treatment(img)
        img = apply_dark_overlay(img, slide["overlay_pct"])
    else:
        if photo_file:
            print(f"[slide {slide['id']}] missing sourced/{photo_file}, using black")
        img = make_black_bg()

    draw = ImageDraw.Draw(img)
    role = slide["role"]

    if role == "hook":
        font = load_font(HOOK_SIZE, bold=True)
        text_h = calc_text_height(slide["body"], font)
        draw_text_block(draw, slide["body"], font, (RH - text_h) // 2)

    elif role == "step":
        header_font = load_font(HEADER_SIZE, bold=True)
        body_font = load_font(BODY_SIZE, bold=False)
        header_h = calc_text_height(slide["header"], header_font)
        body_h = calc_text_height(slide["body"], body_font)
        total_h = header_h + HEADER_BODY_GAP * SCALE + body_h
        y = draw_text_block(draw, slide["header"], header_font, (RH - total_h) // 2)
        y += (HEADER_BODY_GAP - LINE_SPACING) * SCALE
        draw_text_block(draw, slide["body"], body_font, y)

    elif role == "cta":
        label_font = load_font(CTA_LABEL_SIZE, bold=False)
        url_font = load_font(CTA_URL_SIZE, bold=True)
        label_h = calc_text_height(slide["body"], label_font)
        url_h = calc_text_height(slide["cta_url"], url_font)
        total_h = label_h + 40 * SCALE + url_h
        y = draw_text_block(draw, slide["body"], label_font, (RH - total_h) // 2)
        y += (40 - LINE_SPACING) * SCALE
        draw_text_block(draw, slide["cta_url"], url_font, y)

    return img.resize((TARGET_W, TARGET_H), Image.LANCZOS)


def main() -> None:
    out_dir = Path(__file__).parent
    for slide in SLIDES:
        img = render_slide(slide)
        assert img.size == (TARGET_W, TARGET_H)
        out_path = out_dir / f"slide_{slide['id']}.png"
        img.save(out_path, "PNG")
        print(f"Saved: {out_path.name}")

    # Contact sheet for quick review
    imgs = [Image.open(out_dir / f"slide_{s['id']}.png") for s in SLIDES]
    s = 0.3
    tw, th = int(TARGET_W * s), int(TARGET_H * s)
    sheet = Image.new("RGB", (tw * len(imgs) + 20 * (len(imgs) + 1), th + 40), (40, 40, 40))
    for i, im in enumerate(imgs):
        sheet.paste(im.resize((tw, th)), (20 + i * (tw + 20), 20))
    sheet.save(out_dir / "contact-sheet.png", "PNG")
    print(f"Done. {len(SLIDES)} slides + contact sheet.")


if __name__ == "__main__":
    main()

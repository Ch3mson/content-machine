"""
Process images for antigpt post 2: "3 tips for writing essays that get an A in english".

Copy tone: casual lowercase "study with me" voice with a "swipe →" cue on the hook
(same as post 1 / quality-gate attempt-005). Same photos as post 1.

Slide copy below mirrors flow.md exactly, including manual line breaks.

Run from the repo root:
    python3 accounts/antigpt/posts/2-essay-writing-tips/process_images.py
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
LOGO_PATH = Path(__file__).resolve().parents[2] / "assets" / "logo-white.png"  # accounts/antigpt/assets/
LOGO_W = 150       # final-canvas px
LOGO_GAP = 36      # gap between brand name baseline and logo top, final px

# --- Sourced images (empty for now: solid black) ---
SOURCED_DIR = Path(__file__).parent / "sourced"
IMAGE_MAP: dict[int, str] = {
    1: "slide3.jpg",  # black desk setup — different cover from post 1
    2: "slide4.jpg",  # library, student writing
    3: "slide5.jpg",  # bright window / iPad (needs heavier overlay)
    4: "slide1.jpg",  # hotel-style desk, laptop + iPad
    5: "slide2.jpg",  # bedroom desk (450x800, upscaled)
}

# --- Slide definitions with manual line breaks (mirror copy.md) ---
SLIDES = [
    {
        "id": 1,
        "role": "hook",
        "header": None,
        "body": "3 tips for writing essays\nthat get an A in english\nswipe \u2192",
        "overlay_pct": 0.70,
    },
    {
        "id": 2,
        "role": "step",
        "header": "1. first line is the grade",
        "body": "teachers skim the opening of each\nparagraph. if it restates the topic,\nyou already lost the A. make it the argument.",
        "overlay_pct": 0.75,
    },
    {
        "id": 3,
        "role": "step",
        "header": "2. the quote is not the point",
        "body": "drop the evidence. then write what it does.\nthey mark your sentence, not shakespeare's.",
        "overlay_pct": 0.78,
    },
    {
        "id": 4,
        "role": "step",
        "header": "3. let AI draft it first",
        "body": "chatgpt the first pass. don't submit that.\nyour job is the argument. the bot fills the page.",
        "overlay_pct": 0.75,
    },
    {
        "id": 5,
        "role": "cta",
        "header": None,
        "body": "run that AI draft through this.\nit passes the human threshold\non turnitin and AI detectors",
        "cta_url": "AntiGPT",
        "overlay_pct": 0.72,
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
        logo = Image.open(LOGO_PATH).convert("RGBA")
        lw = LOGO_W * SCALE
        lh = round(logo.height * lw / logo.width)
        logo = logo.resize((lw, lh), Image.LANCZOS)
        total_h = label_h + 40 * SCALE + url_h + LOGO_GAP * SCALE + lh
        y = draw_text_block(draw, slide["body"], label_font, (RH - total_h) // 2)
        y += (40 - LINE_SPACING) * SCALE
        y = draw_text_block(draw, slide["cta_url"], url_font, y)
        y += (LOGO_GAP - LINE_SPACING) * SCALE
        img.paste(logo, ((RW - lw) // 2, y), logo)

    return img.resize((TARGET_W, TARGET_H), Image.LANCZOS)


def main() -> None:
    out_dir = Path(__file__).parent / "processed"
    out_dir.mkdir(exist_ok=True)
    for slide in SLIDES:
        img = render_slide(slide)
        assert img.size == (TARGET_W, TARGET_H)
        out_path = out_dir / f"slide_{slide['id']:02d}.png"
        img.save(out_path, "PNG")
        print(f"Saved: processed/{out_path.name}")

    # Contact sheet for quick review (post root, not part of the publish set)
    imgs = [Image.open(out_dir / f"slide_{s['id']:02d}.png") for s in SLIDES]
    s = 0.3
    tw, th = int(TARGET_W * s), int(TARGET_H * s)
    sheet = Image.new("RGB", (tw * len(imgs) + 20 * (len(imgs) + 1), th + 40), (40, 40, 40))
    for i, im in enumerate(imgs):
        sheet.paste(im.resize((tw, th)), (20 + i * (tw + 20), 20))
    sheet.save(Path(__file__).parent / "contact-sheet.png", "PNG")
    print(f"Done. {len(SLIDES)} slides + contact sheet.")


if __name__ == "__main__":
    main()

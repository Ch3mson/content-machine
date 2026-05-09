"""
Quality Gate Attempt 001 — Render a non-hero step slide.

Slide: "Step 1: Pick a viral prompt"
Design source: accounts/makebrainrotvideos/design.md
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# --- Canvas ---
WIDTH = 1080
HEIGHT = 1920
SAFE_MARGIN = 120
BG_COLOR_TOP = (10, 10, 30)       # Near-black with slight blue
BG_COLOR_BOTTOM = (15, 15, 45)    # Slightly lighter for gradient feel

# --- Text ---
TEXT_COLOR = (255, 255, 255)
STROKE_COLOR = (0, 0, 0)
STROKE_WIDTH = 2

# --- Copy ---
STEP_LABEL = "Step 1"
BODY_TEXT = "Pick a viral prompt"


def find_font(size: int) -> ImageFont.FreeTypeFont:
    """Try common bold font paths, fall back to default."""
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def draw_gradient(draw: ImageDraw.ImageDraw) -> None:
    """Draw a vertical dark gradient background."""
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = int(BG_COLOR_TOP[0] + (BG_COLOR_BOTTOM[0] - BG_COLOR_TOP[0]) * ratio)
        g = int(BG_COLOR_TOP[1] + (BG_COLOR_BOTTOM[1] - BG_COLOR_TOP[1]) * ratio)
        b = int(BG_COLOR_TOP[2] + (BG_COLOR_BOTTOM[2] - BG_COLOR_TOP[2]) * ratio)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))


def render() -> None:
    img = Image.new("RGB", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(img)

    # Background gradient
    draw_gradient(draw)

    # Fonts
    step_font = find_font(54)
    body_font = find_font(42)

    # --- Step label ---
    step_bbox = draw.textbbox((0, 0), STEP_LABEL, font=step_font)
    step_w = step_bbox[2] - step_bbox[0]
    step_x = (WIDTH - step_w) // 2
    step_y = HEIGHT // 2 - 80  # Slightly above center

    draw.text(
        (step_x, step_y),
        STEP_LABEL,
        font=step_font,
        fill=TEXT_COLOR,
        stroke_width=STROKE_WIDTH,
        stroke_fill=STROKE_COLOR,
    )

    # --- Body text ---
    body_bbox = draw.textbbox((0, 0), BODY_TEXT, font=body_font)
    body_w = body_bbox[2] - body_bbox[0]
    body_x = (WIDTH - body_w) // 2
    body_y = step_y + 90  # Below step label

    draw.text(
        (body_x, body_y),
        BODY_TEXT,
        font=body_font,
        fill=TEXT_COLOR,
        stroke_width=STROKE_WIDTH,
        stroke_fill=STROKE_COLOR,
    )

    # --- Placeholder frame indicator ---
    # Light border showing where a photo would go (full bleed)
    placeholder_color = (40, 40, 60)
    draw.rectangle(
        [SAFE_MARGIN, SAFE_MARGIN, WIDTH - SAFE_MARGIN, HEIGHT - SAFE_MARGIN],
        outline=placeholder_color,
        width=1,
    )

    # --- Safe margin label ---
    margin_font = find_font(18)
    draw.text(
        (SAFE_MARGIN + 8, SAFE_MARGIN + 8),
        "safe area (120px)",
        font=margin_font,
        fill=(60, 60, 80),
    )

    # Save
    out_path = Path(__file__).parent / "sample-slide.png"
    img.save(out_path, "PNG")
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    render()

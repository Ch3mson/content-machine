# Image Processing Agent Workflow

Use this document when generating processed slideshow images from raw photos and copy.

The agent's job is to take raw photos and slide copy, then produce final 9:16 slideshow images with B&W treatment and text overlay. The order of operations is critical. Do not skip or reorder steps.

## Pipeline Order

The pipeline has four steps. They must run in this exact order:

1. **Normalize to 9:16** — Crop and resize every image to 1080x1920 (9:16).
2. **Convert to black and white** — Apply grayscale + contrast enhancement.
3. **Apply paper overlay** — Vintage paper texture with warm sepia tint, grain, and vignette.
4. **Add text overlay** — Centered white text with black outline.

Do not add text before normalizing. Do not convert to B&W before normalizing. Do not apply paper overlay before B&W conversion. The text positioning depends on the final 9:16 canvas.

## Step 1: Normalize to 9:16

### Rules

- Target resolution: **1080 x 1920 pixels** (9:16 aspect ratio).
- Crop from center. Never stretch or distort the image.
- If the source image is wider than 9:16, crop the sides to fit.
- If the source image is taller than 9:16, crop the top and bottom to fit.
- If the source image is narrower than 9:16, pad with black bars on the sides. Do not stretch.
- Save the normalized image before proceeding to step 2.

### Implementation

```python
from PIL import Image

TARGET_W = 1080
TARGET_H = 1920
TARGET_RATIO = TARGET_W / TARGET_H  # 0.5625 (9:16)

def normalize_to_9_16(input_path, output_path):
    img = Image.open(input_path)
    w, h = img.size
    current_ratio = w / h

    if current_ratio > TARGET_RATIO:
        # Image is wider than 9:16 — crop sides
        new_w = int(h * TARGET_RATIO)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    elif current_ratio < TARGET_RATIO:
        # Image is narrower than 9:16 — pad with black bars on sides
        new_h = int(w / TARGET_RATIO)
        if new_h <= h:
            # Crop top/bottom instead
            top = (h - new_h) // 2
            img = img.crop((0, top, w, top + new_h))
        else:
            # Need padding
            background = Image.new("RGB", (w, new_h), (0, 0, 0))
            top = (new_h - h) // 2
            background.paste(img, (0, top))
            img = background

    img = img.resize((TARGET_W, TARGET_H), Image.LANCZOS)
    img.save(output_path, "PNG")
    return output_path
```

## Step 2: Convert to Black and White

### Rules

- Convert to grayscale.
- Increase contrast by 1.3x to make text readable against the background.
- Do not over-contrast. Faces and key details must remain visible.
- Apply the same contrast setting to all images in a slideshow for consistency.

### Implementation

```python
from PIL import Image, ImageEnhance

CONTRAST_FACTOR = 1.3

def convert_to_bw(input_path, output_path):
    img = Image.open(input_path)
    img = img.convert("L")  # Grayscale
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(CONTRAST_FACTOR)
    img = img.convert("RGB")  # Back to RGB for text overlay
    img.save(output_path, "PNG")
    return output_path
```

## Step 3: Apply Paper Overlay

### Rules

- Apply a vintage paper texture over the B&W image.
- The overlay consists of three layers: warm sepia grain, darker grain spots, and a vignette.
- Warm sepia grain: random pixels with R 180-220, G 160-195, B 130-160, alpha 15-35.
- Darker grain spots: small clusters of R 100-150, G 80-130, B 60-100, alpha 10-30.
- Vignette: dark edges that increase in opacity toward corners. Max alpha 120 at corners.
- Use the same overlay for all slides in a slideshow for consistency.
- The overlay must be subtle enough to not obscure faces or text, but visible enough to create a vintage feel.

### Implementation

```python
import random
from PIL import Image

def create_paper_overlay(width, height):
    """Create a vintage paper texture overlay."""
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    pixels = overlay.load()

    for y in range(height):
        for x in range(width):
            r = random.randint(180, 220)
            g = random.randint(160, 195)
            b = random.randint(130, 160)
            a = random.randint(15, 35)
            pixels[x, y] = (r, g, b, a)

    for _ in range(width * height // 80):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        r = random.randint(100, 150)
        g = random.randint(80, 130)
        b = random.randint(60, 100)
        a = random.randint(10, 30)
        for dx in range(random.randint(1, 3)):
            for dy in range(random.randint(1, 3)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    pixels[nx, ny] = (r, g, b, a)

    vignette = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    v_pixels = vignette.load()
    cx, cy = width // 2, height // 2
    max_dist = (cx**2 + cy**2) ** 0.5

    for y in range(height):
        for x in range(width):
            dist = ((x - cx)**2 + (y - cy)**2) ** 0.5
            ratio = dist / max_dist
            alpha = int(ratio * ratio * 80)
            alpha = min(alpha, 120)
            v_pixels[x, y] = (0, 0, 0, alpha)

    overlay = Image.alpha_composite(overlay, vignette)
    return overlay

def apply_paper_overlay(img, overlay):
    """Blend paper overlay onto the image."""
    img_rgba = img.convert("RGBA")
    result = Image.alpha_composite(img_rgba, overlay)
    return result.convert("RGB")
```

## Step 4: Add Text Overlay

### Rules

- **Font**: Bold sans-serif. Use `arialbd.ttf` (Arial Bold) at 48pt. Fall back to default if unavailable.
- **Color**: White (#FFFFFF).
- **Outline**: Black stroke, 4px width, for readability against any background.
- **Alignment**: Centered horizontally and vertically on the canvas.
- **Line breaks**: Break lines for rhythm, not just to fit width. Follow the copy in `flow.md` exactly.
- **Line spacing**: 16px between lines.
- **Padding**: Leave at least 80px margin on left and right. Text should not touch the edges.
- **Max characters per line**: 36. If a line exceeds 36 characters, break it at the nearest word boundary.

### Implementation

```python
from PIL import Image, ImageDraw, ImageFont
import os

FONT_SIZE = 48
OUTLINE_WIDTH = 4
LINE_SPACING = 10
MAX_CHARS_PER_LINE = 36
MARGIN_X = 80

def load_font():
    font_paths = [
        "arialbd.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
        "/usr/share/fonts/truetype/msttcorefonts/Arial_Bold.ttf",
    ]
    for path in font_paths:
        try:
            return ImageFont.truetype(path, FONT_SIZE)
        except:
            continue
    return ImageFont.load_default()

def wrap_text(text, font, max_width):
    """Break text into lines that fit within max_width."""
    lines = []
    for paragraph in text.split('\n'):
        if not paragraph:
            lines.append('')
            continue
        words = paragraph.split()
        current_line = ''
        for word in words:
            test_line = f"{current_line} {word}".strip()
            bbox = font.getbbox(test_line)
            if bbox[2] - bbox[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)
    return lines

def add_text_with_outline(draw, text, x, y, font, fill="white", outline="black"):
    for dx in range(-OUTLINE_WIDTH, OUTLINE_WIDTH + 1):
        for dy in range(-OUTLINE_WIDTH, OUTLINE_WIDTH + 1):
            if dx * dx + dy * dy <= OUTLINE_WIDTH * OUTLINE_WIDTH:
                draw.text((x + dx, y + dy), text, font=font, fill=outline)
    draw.text((x, y), text, font=font, fill=fill)

def add_text_overlay(input_path, output_path, text, font=None):
    if font is None:
        font = load_font()
    
    img = Image.open(input_path)
    draw = ImageDraw.Draw(img)
    
    max_text_width = img.width - (2 * MARGIN_X)
    lines = wrap_text(text, font, max_text_width)
    
    # Calculate total text height
    line_heights = []
    for line in lines:
        bbox = font.getbbox(line)
        line_heights.append(bbox[3] - bbox[1])
    total_height = sum(line_heights) + LINE_SPACING * (len(lines) - 1)
    
    # Start y position (centered)
    current_y = (img.height - total_height) // 2
    
    for i, line in enumerate(lines):
        bbox = font.getbbox(line)
        line_width = bbox[2] - bbox[0]
        x = (img.width - line_width) // 2
        add_text_with_outline(draw, line, x, current_y, font)
        current_y += line_heights[i] + LINE_SPACING
    
    img.save(output_path, "PNG")
    return output_path
```

## Full Pipeline

### Input Requirements

Before running the pipeline, the agent needs:

- **Raw photos**: In the account's image folder (e.g., `accounts/athlete-stories/Lebron/`).
- **Slide map**: From `flow.md` — which photo maps to which slide and what copy goes on it.
- **Image rules**: From `image.md` — B&W treatment, text style, product slide handling.

### Output

- Save all processed images to a `processed/` subfolder inside the account's image folder.
- Name files `slide_1.png`, `slide_2.png`, etc.
- All images must be exactly 1080x1920 pixels.

### Pipeline Script

```python
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import random
import os

# --- Configuration ---
INPUT_DIR = r"C:\Users\samue\Downloads\Slideshow Test\accounts\athlete-stories\Lebron"
OUTPUT_DIR = os.path.join(INPUT_DIR, "processed")
TARGET_W = 1080
TARGET_H = 1920
TARGET_RATIO = TARGET_W / TARGET_H
CONTRAST_FACTOR = 1.3
FONT_SIZE = 48
OUTLINE_WIDTH = 4
LINE_SPACING = 16
MARGIN_X = 80

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Slide mapping: (filename, text)
# Copy this from flow.md
slides = [
    ("lebron1.jpg", "Twelve years old. Sleeping on couches.\nMother working three jobs.\nSchool flagging him for truancy."),
    ("a571febb96890fec4d1c46883968bf67.jpg", "Basketball was the only thing that\nkept him showing up.\nHe told his coach he'd play in the NBA.\nThe coach laughed."),
    ("9b284a10e408e392a9bacca499a399c6.jpg", "He watched film until his eyes burned.\nRehearsed every possession.\nSaw the court before the ball moved.\nWhile other kids played, he studied."),
    ("lebron meditating.jpg", "He visualized every game, every possession,\nevery shot, running through scenarios in his head\nuntil the court felt like home before he even\nstepped on it. He saw it before it happened."),
    ("6e3eb22d3cb436a8bd0466d9e1a6a8bf.jpg", "Number one pick. Straight from high school.\nThe kid from Akron who refused to disappear\nbecame the greatest to ever play."),
    ("native hold.jpeg", "I use w(inner) before my games.\nIt runs a visualization track built for\nmy position and my matchup."),
    ("e59acbc2f78cd411738943d2ce515559.jpg", '"I knew what I was going to be\nbefore I knew what I was."\n\u2014 LeBron James'),
]

def load_font():
    for path in ["arialbd.ttf", "C:/Windows/Fonts/arialbd.ttf"]:
        try:
            return ImageFont.truetype(path, FONT_SIZE)
        except:
            continue
    return ImageFont.load_default()

def normalize_to_9_16(img):
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

    return img.resize((TARGET_W, TARGET_H), Image.LANCZOS)

def convert_to_bw(img):
    img = img.convert("L")
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(CONTRAST_FACTOR)
    return img.convert("RGB")

def create_paper_overlay(width, height):
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    pixels = overlay.load()

    for y in range(height):
        for x in range(width):
            r = random.randint(180, 220)
            g = random.randint(160, 195)
            b = random.randint(130, 160)
            a = random.randint(15, 35)
            pixels[x, y] = (r, g, b, a)

    for _ in range(width * height // 80):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        r = random.randint(100, 150)
        g = random.randint(80, 130)
        b = random.randint(60, 100)
        a = random.randint(10, 30)
        for dx in range(random.randint(1, 3)):
            for dy in range(random.randint(1, 3)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    pixels[nx, ny] = (r, g, b, a)

    vignette = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    v_pixels = vignette.load()
    cx, cy = width // 2, height // 2
    max_dist = (cx**2 + cy**2) ** 0.5

    for y in range(height):
        for x in range(width):
            dist = ((x - cx)**2 + (y - cy)**2) ** 0.5
            ratio = dist / max_dist
            alpha = int(ratio * ratio * 80)
            alpha = min(alpha, 120)
            v_pixels[x, y] = (0, 0, 0, alpha)

    overlay = Image.alpha_composite(overlay, vignette)
    return overlay

def apply_paper_overlay(img, overlay):
    img_rgba = img.convert("RGBA")
    result = Image.alpha_composite(img_rgba, overlay)
    return result.convert("RGB")

def wrap_text(text, font, max_width):
    lines = []
    for paragraph in text.split('\n'):
        if not paragraph:
            lines.append('')
            continue
        words = paragraph.split()
        current_line = ''
        for word in words:
            test_line = f"{current_line} {word}".strip()
            bbox = font.getbbox(test_line)
            if bbox[2] - bbox[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)
    return lines

def add_text_overlay(img, text, font):
    draw = ImageDraw.Draw(img)
    max_text_width = img.width - (2 * MARGIN_X)
    lines = wrap_text(text, font, max_text_width)

    line_heights = []
    for line in lines:
        bbox = font.getbbox(line)
        line_heights.append(bbox[3] - bbox[1])
    total_height = sum(line_heights) + LINE_SPACING * (len(lines) - 1)

    current_y = (img.height - total_height) // 2

    for i, line in enumerate(lines):
        bbox = font.getbbox(line)
        line_width = bbox[2] - bbox[0]
        x = (img.width - line_width) // 2
        # Outline
        for dx in range(-OUTLINE_WIDTH, OUTLINE_WIDTH + 1):
            for dy in range(-OUTLINE_WIDTH, OUTLINE_WIDTH + 1):
                if dx * dx + dy * dy <= OUTLINE_WIDTH * OUTLINE_WIDTH:
                    draw.text((x + dx, current_y + dy), line, font=font, fill="black")
        # Main text
        draw.text((x, current_y), line, font=font, fill="white")
        current_y += line_heights[i] + LINE_SPACING

    return img

# --- Run Pipeline ---
font = load_font()
paper_overlay = create_paper_overlay(TARGET_W, TARGET_H)

for i, (filename, text) in enumerate(slides):
    filepath = os.path.join(INPUT_DIR, filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename} - not found")
        continue

    img = Image.open(filepath)
    
    # Step 1: Normalize to 9:16
    img = normalize_to_9_16(img)
    
    # Step 2: Convert to B&W
    img = convert_to_bw(img)
    
    # Step 3: Apply paper overlay
    img = apply_paper_overlay(img, paper_overlay)
    
    # Step 4: Add text overlay
    img = add_text_overlay(img, text, font)
    
    # Save
    output_path = os.path.join(OUTPUT_DIR, f"slide_{i + 1}.png")
    img.save(output_path, "PNG")
    print(f"Created: {output_path}")

print("\nAll slides processed!")
```

## Agent Rules

- Always normalize to 9:16 before any other processing.
- Never skip the normalize step. Text positioning breaks on non-9:16 images.
- Apply the same B&W contrast setting to all images in a slideshow.
- Apply the same paper overlay to all images in a slideshow for consistency.
- Use the exact copy from `flow.md`. Do not reword or reformat.
- Save processed images to `processed/` subfolder with `slide_N.png` naming.
- All output images must be exactly 1080x1920 pixels.
- If a source image is missing, skip it and report which file was not found.
- If the font is unavailable, fall back to default but flag it in the output.
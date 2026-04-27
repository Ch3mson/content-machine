from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
import random
import os

# --- Configuration ---
INPUT_DIR = r"C:\Users\samue\Downloads\Slideshow Test\accounts\athlete-stories\Lebron"
OUTPUT_DIR = os.path.join(INPUT_DIR, "processed")
TARGET_W = 1080
TARGET_H = 1920
TARGET_RATIO = TARGET_W / TARGET_H
CONTRAST_FACTOR = 1.3
FONT_SIZE = 36
OUTLINE_WIDTH = 3
LINE_SPACING = 16
MARGIN_X = 140

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Slide mapping: (filename, text)
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
    """Create a vintage paper texture overlay."""
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    pixels = overlay.load()

    for y in range(height):
        for x in range(width):
            # Base paper tint: warm sepia
            r = random.randint(180, 220)
            g = random.randint(160, 195)
            b = random.randint(130, 160)
            # Low opacity for subtlety
            a = random.randint(15, 35)
            pixels[x, y] = (r, g, b, a)

    # Add some darker grain spots
    for _ in range(width * height // 80):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        r = random.randint(100, 150)
        g = random.randint(80, 130)
        b = random.randint(60, 100)
        a = random.randint(10, 30)
        # Small cluster
        for dx in range(random.randint(1, 3)):
            for dy in range(random.randint(1, 3)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    pixels[nx, ny] = (r, g, b, a)

    # Add vignette effect (darker edges)
    vignette = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    v_pixels = vignette.load()
    cx, cy = width // 2, height // 2
    max_dist = (cx**2 + cy**2) ** 0.5

    for y in range(height):
        for x in range(width):
            dist = ((x - cx)**2 + (y - cy)**2) ** 0.5
            ratio = dist / max_dist
            # Vignette intensity increases toward edges
            alpha = int(ratio * ratio * 80)
            alpha = min(alpha, 120)
            v_pixels[x, y] = (0, 0, 0, alpha)

    # Combine paper texture with vignette
    overlay = Image.alpha_composite(overlay, vignette)
    return overlay

def apply_paper_overlay(img, overlay):
    """Blend paper overlay onto the image."""
    img_rgba = img.convert("RGBA")
    result = Image.alpha_composite(img_rgba, overlay)
    return result.convert("RGB")

def add_text_overlay(img, text, font):
    draw = ImageDraw.Draw(img)
    # Respect manual line breaks exactly — do not auto-wrap
    lines = text.split('\n')

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

# Pre-generate paper overlay (same for all slides for consistency)
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
    
    # Step 3: Apply paper overlay (vintage effect)
    img = apply_paper_overlay(img, paper_overlay)
    
    # Step 4: Add text overlay
    img = add_text_overlay(img, text, font)
    
    # Save
    output_path = os.path.join(OUTPUT_DIR, f"slide_{i + 1}.png")
    img.save(output_path, "PNG")
    print(f"Created: {output_path}")

print("\nAll slides processed!")
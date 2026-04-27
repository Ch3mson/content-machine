from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import random
import os

# --- Configuration ---
INPUT_DIR = r"C:\Users\samue\Downloads\Slideshow Test\accounts\athlete-stories\Michael Jordan"
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
    ("3.jpg", "You want to play like him.\nAre you willing to bleed for it?"),
    ("2 (2).jpg", "Detroit owned him. Three straight years.\nThe Pistons called it the Jordan Rules.\nHe bled in the post and still lost."),
    ("1.jpg", "He played every game like it was his last.\nThe championship weight sat on his chest.\nHe couldn't sleep after the eliminations."),
    ("2.jpg", "He trained his body.\nAdded 25 pounds in one summer.\nStill couldn't sleep after the losses.\nThe edge had to come from somewhere deeper."),
    ("4.jpg", "He sat with headphones\nand ran every possession in his mind\nuntil the court in his mind\nfelt more familiar than\nthe one under his feet.\nBy the time the game came,\nhe had already been there."),
    (r"..\Lebron\native hold.jpeg", "I use w(inner) the same way.\nIt builds a visualization track until the game\nfeels familiar before it starts."),
    ("abd6315c9640e16d7bde23130af09dfc.jpg", '"You have to expect things of yourself\nbefore you can do them."\n— Michael Jordan'),
]


def load_font():
    for path in ["arialbd.ttf", "C:/Windows/Fonts/arialbd.ttf"]:
        try:
            return ImageFont.truetype(path, FONT_SIZE)
        except Exception:
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
            dist = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
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


def add_text_overlay(img, text, font):
    draw = ImageDraw.Draw(img)
    lines = text.split("\n")

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
        if x < MARGIN_X:
            x = MARGIN_X
        for dx in range(-OUTLINE_WIDTH, OUTLINE_WIDTH + 1):
            for dy in range(-OUTLINE_WIDTH, OUTLINE_WIDTH + 1):
                if dx * dx + dy * dy <= OUTLINE_WIDTH * OUTLINE_WIDTH:
                    draw.text((x + dx, current_y + dy), line, font=font, fill="black")
        draw.text((x, current_y), line, font=font, fill="white")
        current_y += line_heights[i] + LINE_SPACING

    return img


font = load_font()
paper_overlay = create_paper_overlay(TARGET_W, TARGET_H)

for i, (filename, text) in enumerate(slides):
    filepath = os.path.normpath(os.path.join(INPUT_DIR, filename))
    if not os.path.exists(filepath):
        print(f"Skipping {filename} - not found")
        continue

    img = Image.open(filepath)
    img = normalize_to_9_16(img)
    img = convert_to_bw(img)
    img = apply_paper_overlay(img, paper_overlay)
    img = add_text_overlay(img, text, font)

    output_path = os.path.join(OUTPUT_DIR, f"slide_{i + 1}.png")
    img.save(output_path, "PNG")
    print(f"Created: {output_path}")

print("\nAll slides processed!")

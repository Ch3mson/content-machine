from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

# Canvas size — 3:4 portrait for Instagram carousel
WIDTH = 1080
HEIGHT = 1440

# Layout constants
MARGIN_X = 60
TEXT_WIDTH = WIDTH - (MARGIN_X * 2)  # 960

# Image placeholder (16:9) — consistent across all body slides
IMG_W = 960
IMG_H = 540
IMG_X = MARGIN_X
IMG_Y = 450  # centered around middle of 1440 canvas (720 - 270)

# Text areas
TOP_TEXT_Y_START = 50
TOP_TEXT_Y_END = IMG_Y - 20  # 430

BOTTOM_TEXT_Y_START = IMG_Y + IMG_H + 20  # 1010
BOTTOM_TEXT_Y_END = 1360

SOURCE_Y = 1380

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)

# Fonts
FONT_PATH_BODY = r"C:\Windows\Fonts\arial.ttf"
FONT_PATH_BOLD = r"C:\Windows\Fonts\arialbd.ttf"

FONT_SIZE_BODY = 34
FONT_SIZE_SOURCE = 24
FONT_SIZE_PLACEHOLDER = 28

def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

font_body = load_font(FONT_PATH_BODY, FONT_SIZE_BODY)
font_source = load_font(FONT_PATH_BODY, FONT_SIZE_SOURCE)
font_placeholder = load_font(FONT_PATH_BODY, FONT_SIZE_PLACEHOLDER)

def wrap_text(text, font, max_width):
    """Wrap text to fit within max_width pixels."""
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + " " + word if current_line else word
        bbox = font.getbbox(test_line)
        line_width = bbox[2] - bbox[0]
        if line_width <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines

def draw_text_block(draw, lines, font, color, x, y_start, y_end, align="center"):
    """Draw wrapped text block vertically centered within y_start to y_end."""
    line_height = font.getbbox("Ay")[3] - font.getbbox("Ay")[1] + 12
    total_height = len(lines) * line_height
    # Center vertically in the available space
    y = y_start + max(0, (y_end - y_start - total_height) // 2)
    for line in lines:
        bbox = font.getbbox(line)
        line_width = bbox[2] - bbox[0]
        if align == "center":
            x_pos = x + (TEXT_WIDTH - line_width) // 2
        else:
            x_pos = x
        draw.text((x_pos, y), line, font=font, fill=color)
        y += line_height
    return y

def create_slide(filename, top_text, bottom_text, source_text=""):
    img = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
    draw = ImageDraw.Draw(img)
    
    # Draw image placeholder
    draw.rectangle([IMG_X, IMG_Y, IMG_X + IMG_W, IMG_Y + IMG_H], outline=DARK_GRAY, width=2)
    # Diagonal lines to indicate placeholder
    draw.line([(IMG_X, IMG_Y), (IMG_X + IMG_W, IMG_Y + IMG_H)], fill=GRAY, width=2)
    draw.line([(IMG_X + IMG_W, IMG_Y), (IMG_X, IMG_Y + IMG_H)], fill=GRAY, width=2)
    
    # Placeholder label
    placeholder_label = "[ IMAGE PLACEHOLDER ]"
    bbox = font_placeholder.getbbox(placeholder_label)
    label_w = bbox[2] - bbox[0]
    label_h = bbox[3] - bbox[1]
    label_x = IMG_X + (IMG_W - label_w) // 2
    label_y = IMG_Y + (IMG_H - label_h) // 2
    draw.text((label_x, label_y), placeholder_label, font=font_placeholder, fill=DARK_GRAY)
    
    # Draw top text
    if top_text.strip():
        lines = wrap_text(top_text, font_body, TEXT_WIDTH)
        draw_text_block(draw, lines, font_body, BLACK, MARGIN_X, TOP_TEXT_Y_START, TOP_TEXT_Y_END)
    
    # Draw bottom text
    if bottom_text.strip():
        lines = wrap_text(bottom_text, font_body, TEXT_WIDTH)
        draw_text_block(draw, lines, font_body, BLACK, MARGIN_X, BOTTOM_TEXT_Y_START, BOTTOM_TEXT_Y_END)
    
    # Draw source text
    if source_text.strip():
        lines = wrap_text(source_text, font_source, TEXT_WIDTH)
        total_h = len(lines) * (font_source.getbbox("Ay")[3] - font_source.getbbox("Ay")[1] + 6)
        y = SOURCE_Y + max(0, (40 - total_h) // 2)
        for line in lines:
            bbox = font_source.getbbox(line)
            line_w = bbox[2] - bbox[0]
            x_pos = MARGIN_X + (TEXT_WIDTH - line_w) // 2
            draw.text((x_pos, y), line, font=font_source, fill=DARK_GRAY)
            y += font_source.getbbox("Ay")[3] - font_source.getbbox("Ay")[1] + 6
    
    img.save(filename, "PNG")
    print(f"Saved {filename}")

# Define slides
slides = [
    (
        "slide_1.png",
        "There are two versions of you. The training winger is fluid. Fast. Feared. The game winger is tense. Safe. Forgettable. Your coach says you need more reps. Your coach is wrong.",
        "",
        ""
    ),
    (
        "slide_2.png",
        "Elite wingers face over 20 1v1 situations per match. [VERIFY] Most youth wingers spend 70% of technical training on isolated drills. [VERIFY] That gap is the problem. You are preparing for a situation that never shows up in the game.",
        "Travassos et al. (2012): training transfers better when it preserves the information the game gives you. Your drills stripped away defender cues, timing, and consequence. You practiced the move. The game demands the read.",
        "Source: Travassos et al. (2012)"
    ),
    (
        "slide_3.png",
        "Blocked practice feels good. You see progress. You feel sharp. Your coach praised your clean technique. Your coach was praising the wrong thing.",
        "Shea & Morgan (1979): variable practice feels messier but produces better transfer. The training lied. The progress was fake. So what actually transfers? Reps where the cue changes every time. Same technique, different decision.",
        "Source: Shea & Morgan (1979)"
    ),
    (
        "slide_4.png",
        "Under pressure, your brain defaults to automatic. If automatic was learned without game cues, it does not transfer.",
        "Your body needs to feel pressure before the real match. Even in a simple cone drill, imagine a defender on your back. Feel them closing in. Now your touch changes. You do not need a full team to train game pressure. You need imagination that makes your body react.",
        "Source: Travassos et al. (2012)"
    ),
    (
        "slide_5.png",
        "Your body cannot train under match pressure every day. But your brain still needs the game picture.",
        "What if your brain could not tell the difference between a vivid mental rep and a physical one? PETTLEP imagery activates the same neural circuits as real play. Spend five minutes before bed replaying one match moment. First-person. Full emotion.",
        "Source: Holmes & Collins (2001)"
    ),
    (
        "slide_6.png",
        "Generic imagery fails because it is too vague. You need your position, your opponent, your exact pressure moment.",
        "w(inner) generates personalized visualization audio for your sport, position, and scenario. It builds mental reps that match your real game. When your body rests, your brain trains.",
        ""
    ),
    (
        "slide_7.png",
        "Stop being the player who only shows up in training. Start training the picture.",
        "The game does not reward clean technique. It rewards correct decisions under uncertainty.",
        ""
    ),
]

output_dir = r"C:\Users\samue\Downloads\Slideshow Test\accounts\science-athlete\posts\winger-training-transfer\processed"
os.makedirs(output_dir, exist_ok=True)

for filename, top, bottom, source in slides:
    filepath = os.path.join(output_dir, filename)
    create_slide(filepath, top, bottom, source)

print("\nAll slides generated.")

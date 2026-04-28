from PIL import Image, ImageDraw, ImageFont
import os

# Canvas settings - 3:4 carousel for science-athlete
WIDTH = 1080
HEIGHT = 1440
MARGIN = 140
CONTENT_WIDTH = WIDTH - (MARGIN * 2)

# Colors
BG_COLOR = "#FFFFFF"
TEXT_COLOR = "#000000"
SOURCE_COLOR = "#444444"

# Font paths
FONT_DIR = "C:/Windows/Fonts/"
FONT_BOLD = os.path.join(FONT_DIR, "arialbd.ttf")
FONT_REGULAR = os.path.join(FONT_DIR, "arial.ttf")

# Load fonts
try:
    font_header = ImageFont.truetype(FONT_BOLD, 44)
    font_title = ImageFont.truetype(FONT_BOLD, 64)
    font_body = ImageFont.truetype(FONT_REGULAR, 28)
    font_bold_body = ImageFont.truetype(FONT_BOLD, 28)
    font_source = ImageFont.truetype(FONT_REGULAR, 20)
except:
    font_header = ImageFont.load_default()
    font_title = ImageFont.load_default()
    font_body = ImageFont.load_default()
    font_bold_body = ImageFont.load_default()
    font_source = ImageFont.load_default()

def wrap_text(draw, text, font, max_width):
    """Wrap text to fit within max_width, respecting manual line breaks."""
    lines = []
    for paragraph in text.split('\n'):
        words = paragraph.split(' ')
        current_line = []
        for word in words:
            test_line = ' '.join(current_line + [word])
            bbox = draw.textbbox((0, 0), test_line, font=font)
            if bbox[2] - bbox[0] <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
        if current_line:
            lines.append(' '.join(current_line))
    return lines

def draw_wrapped_text(draw, text, font, x, y, max_width, line_spacing=10, bold_phrases=None, color=TEXT_COLOR):
    """Draw wrapped text, optionally bolding specific phrases."""
    lines = wrap_text(draw, text, font, max_width)
    current_y = y
    for line in lines:
        if bold_phrases:
            words = line.split(' ')
            current_x = x
            for word in words:
                is_bold = any(bp.lower() in word.lower() for bp in bold_phrases)
                use_font = font_bold_body if is_bold else font
                word_with_space = word + ' '
                draw.text((current_x, current_y), word_with_space, fill=color, font=use_font)
                bbox = draw.textbbox((0, 0), word_with_space, font=use_font)
                current_x += bbox[2] - bbox[0]
        else:
            draw.text((x, current_y), line, fill=color, font=font)
        bbox = draw.textbbox((0, 0), "Ag", font=font)
        current_y += (bbox[3] - bbox[1]) + line_spacing
    return current_y

def create_slide():
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    y = 60
    
    # === HEADER ===
    header_text = "what to avoid:"
    draw.text((MARGIN, y), header_text, fill=TEXT_COLOR, font=font_header)
    bbox = draw.textbbox((MARGIN, y), header_text, font=font_header)
    y = bbox[3] + 12
    
    # === TITLE ===
    title_text = "static wall passes"
    draw.text((MARGIN, y), title_text, fill=TEXT_COLOR, font=font_title)
    bbox = draw.textbbox((MARGIN, y), title_text, font=font_title)
    y = bbox[3] + 24
    
    # === BODY ===
    body_text = ("the wall is the most common solo training tool. it is also the most misleading. "
                 "the wall gives you a perfect bounce. same angle. same speed. same height. "
                 "your brain learns one return pattern. in games, passes arrive with backspin, "
                 "from odd angles, after a deflection. your first touch fails not because your "
                 "technique is bad, but because your afferent feedback [the sensory information "
                 "your brain uses to prepare a movement] is expecting the wrong ball. your foot "
                 "prepares for the perfect bounce. the messy bounce wins.")
    
    bold_phrases = ["expecting the wrong ball", "afferent feedback"]
    y = draw_wrapped_text(draw, body_text, font_body, MARGIN, y, CONTENT_WIDTH, 
                          line_spacing=8, bold_phrases=bold_phrases)
    y += 24
    
    # === IMAGE ===
    image_path = "C:/Users/samue/Downloads/Slideshow Test/accounts/science-athlete/posts/Soccer_training_diagram_202604271357.jpeg"
    if os.path.exists(image_path):
        diagram = Image.open(image_path)
        # Target width is content width, height max 340
        target_width = CONTENT_WIDTH
        ratio = target_width / diagram.width
        target_height = int(diagram.height * ratio)
        if target_height > 340:
            target_height = 340
            ratio = target_height / diagram.height
            target_width = int(diagram.width * ratio)
        
        diagram = diagram.resize((target_width, target_height), Image.LANCZOS)
        img_x = (WIDTH - diagram.width) // 2
        img_y = y
        img.paste(diagram, (img_x, img_y))
        y = img_y + diagram.height + 24
    else:
        print(f"Warning: Image not found at {image_path}")
        y += 180
    
    # === THE FIX ===
    fix_header = "the fix:"
    draw.text((MARGIN, y), fix_header, fill=TEXT_COLOR, font=font_bold_body)
    bbox = draw.textbbox((MARGIN, y), fix_header, font=font_bold_body)
    y = bbox[3] + 6
    
    fix_text = ("break the pattern yourself. vary the distance from three yards to ten yards "
                "in the same session. kick the ball at an angle so it returns off-center. or train "
                "on uneven ground so the bounce is unpredictable. you are not practicing the pass. "
                "you are practicing error correction [adjusting your movement plan based on unexpected "
                "sensory input]. this is the actual skill. a rebounder net with uneven tension works "
                "even better. it sends the ball back at random heights and speeds.")
    
    bold_phrases = ["error correction"]
    y = draw_wrapped_text(draw, fix_text, font_body, MARGIN, y, CONTENT_WIDTH,
                          line_spacing=8, bold_phrases=bold_phrases)
    y += 18
    
    # === PROGRESSION ===
    prog_header = "progression:"
    draw.text((MARGIN, y), prog_header, fill=TEXT_COLOR, font=font_bold_body)
    bbox = draw.textbbox((MARGIN, y), prog_header, font=font_bold_body)
    y = bbox[3] + 6
    
    prog_text = ("force one-touch returns on the bad bounces only. if the ball comes back clean, "
                 "take two touches. if it comes back messy, one touch into space. this trains "
                 "rapid recalculation under uncertainty.")
    
    bold_phrases = ["rapid recalculation"]
    y = draw_wrapped_text(draw, prog_text, font_body, MARGIN, y, CONTENT_WIDTH,
                          line_spacing=8, bold_phrases=bold_phrases)
    y += 18
    
    # === SOURCE ===
    source_text = "scientific source: experimental brain research - sensorimotor adaptation in human motor control."
    draw.text((MARGIN, y), source_text, fill=SOURCE_COLOR, font=font_source)
    
    # Save
    output_dir = "C:/Users/samue/Downloads/Slideshow Test/accounts/science-athlete/posts/test-slide3"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "slide_3.png")
    img.save(output_path, "PNG")
    print(f"Saved: {output_path}")
    return output_path

if __name__ == "__main__":
    create_slide()

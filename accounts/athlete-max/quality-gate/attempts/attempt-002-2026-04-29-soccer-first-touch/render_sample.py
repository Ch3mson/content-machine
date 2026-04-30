"""A3 quality-gate renderer for athlete-max — attempt 002 soccer body slide.

Source of truth for layout: ../design.md
Source of truth for copy:   ./sample-copy.md
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "sample-slide.png"

W, H = 1080, 1350
BG = "#FFFFFF"
BLACK = "#111111"
DARK_GRAY = "#444444"
LIGHT_GRAY = "#F2F2F2"
MID_GRAY = "#D0D0D0"

FONT_REG = "C:/Windows/Fonts/arial.ttf"
FONT_BOLD = "C:/Windows/Fonts/arialbd.ttf"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size)


F_LABEL = font(FONT_REG, 32)
F_TITLE = font(FONT_BOLD, 60)
F_BODY = font(FONT_REG, 30)
F_BODY_BOLD = font(FONT_BOLD, 30)
F_FRAME_LABEL = font(FONT_BOLD, 28)
F_SOURCE = font(FONT_REG, 20)


def text_width(draw, text, fnt):
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0]


def center_text(draw, text, y, fnt, fill=BLACK):
    x = (W - text_width(draw, text, fnt)) // 2
    draw.text((x, y), text, font=fnt, fill=fill)


def draw_centered_lines(draw, lines, y, fnt, fill=BLACK, line_gap=10):
    cur = y
    for line in lines:
        if line == "":
            cur += int(fnt.size * 0.55)
            continue
        center_text(draw, line, cur, fnt, fill)
        cur += fnt.size + line_gap
    return cur


def draw_centered_rich(draw, segments, y):
    total = sum(text_width(draw, t, f) for t, f, _ in segments)
    x = (W - total) // 2
    for t, f, fill in segments:
        draw.text((x, y), t, font=f, fill=fill)
        x += text_width(draw, t, f)


def draw_rich_paragraph(draw, lines, y, line_gap=8):
    cur = y
    for segs in lines:
        if not segs:
            cur += int(F_BODY.size * 0.55)
            continue
        max_size = max(f.size for _, f, _ in segs)
        draw_centered_rich(draw, segs, cur)
        cur += max_size + line_gap
    return cur


def draw_placeholder_frame(draw):
    fx, fy, fw, fh = 140, 515, 800, 450
    draw.rectangle((fx, fy, fx + fw, fy + fh), fill=LIGHT_GRAY, outline=MID_GRAY, width=3)
    draw.line((fx, fy, fx + fw, fy + fh), fill=MID_GRAY, width=2)
    draw.line((fx + fw, fy, fx, fy + fh), fill=MID_GRAY, width=2)
    label = "[reference photo]"
    lw = text_width(draw, label, F_FRAME_LABEL)
    pad_x, pad_y = 18, 10
    cx = fx + fw // 2
    cy = fy + fh // 2
    draw.rectangle(
        (cx - lw // 2 - pad_x, cy - F_FRAME_LABEL.size // 2 - pad_y,
         cx + lw // 2 + pad_x, cy + F_FRAME_LABEL.size // 2 + pad_y),
        fill="#FFFFFF", outline=MID_GRAY, width=2,
    )
    draw.text((cx - lw // 2, cy - F_FRAME_LABEL.size // 2 - 2), label,
              font=F_FRAME_LABEL, fill=DARK_GRAY)


def main():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Label (10 words)
    center_text(draw, "what to avoid when your legs start feeling heavy:", 92, F_LABEL, BLACK)

    # Title (two bold lines: 9 words, 11 words)
    title_lines = [
        "your late-game touch is not caused by tired legs",
        "it is a nervous system problem that starts in your brain",
    ]
    draw_centered_lines(draw, title_lines, 152, F_TITLE, BLACK, line_gap=6)

    # Top explanation (5 lines, all 12-15 words)
    top_paragraph = [
        [("by minute 70 your brain fires the foot signal late and your touch starts to slip", F_BODY, BLACK)],
        [("your first touch lands ", F_BODY, BLACK),
         ("30-40 cm farther", F_BODY_BOLD, BLACK),
         (" than it did in the first half", F_BODY, BLACK)],
        [("your nervous system is dialing precision down to protect you from total exhaustion", F_BODY, BLACK)],
        [("this is why your clean first-half touch disappears even when your legs still feel fine", F_BODY, BLACK)],
        [("which means your foot reaches the ball late while the defender closes the space first", F_BODY, BLACK)],
    ]
    draw_rich_paragraph(draw, top_paragraph, 305, line_gap=6)

    # Reference photo frame at the design.md spec
    draw_placeholder_frame(draw)

    # Lower section: the fix (3 lines, 15 words each)
    fix_paragraph = [
        [("the fix:", F_BODY_BOLD, BLACK),
         (" drill 6-8 first touches into a shoebox-sized target during the last 15 minutes", F_BODY, BLACK)],
        [("of your training session when your legs are already gone and your brain is tired", F_BODY, BLACK)],
        [("so your nervous system learns to keep precision even when your muscles feel empty", F_BODY, BLACK)],
    ]
    cur = draw_rich_paragraph(draw, fix_paragraph, 990, line_gap=6)

    # Payoff (2 lines, 15-16 words each)
    payoff_paragraph = [
        [("the payoff:", F_BODY_BOLD, BLACK),
         (" the ball still drops at your foot in minute 80 when the defender expects", F_BODY, BLACK)],
        [("you to lose possession but you keep control because your brain stayed sharp under fatigue", F_BODY, BLACK)],
    ]
    draw_rich_paragraph(draw, payoff_paragraph, cur + 16, line_gap=6)

    # Source line — bottom centered, 9 words
    center_text(draw, "Mohr, Krustrup & Bangsbo — J Sports Sci 2003",
                1280, F_SOURCE, DARK_GRAY)

    img.save(OUT)
    assert img.size == (W, H), img.size
    print(f"saved {OUT} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()

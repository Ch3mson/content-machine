"""A3 quality-gate renderer for athlete-max — attempt 003 soccer body slide.

Source of truth for layout: ../../../design.md
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
F_TITLE = font(FONT_BOLD, 48)
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

    # Label
    center_text(draw, "what to avoid when fatigue affects your late-game touch:", 92, F_LABEL, BLACK)

    # Title (two bold lines at 48px to fit 9-word minimum)
    title_lines = [
        "your late-game touch is not a conditioning problem,",
        "it is a motor cortex issue that begins under fatigue"
    ]
    draw_centered_lines(draw, title_lines, 152, F_TITLE, BLACK, line_gap=6)

    # Top explanation — TAP-R mechanism, all lines 9+ words
    top_paragraph = [
        [("by minute 70, your motor cortex (the brain region that plans", F_BODY, BLACK)],
        [("precise foot placement) suppresses fine motor output to protect", F_BODY, BLACK)],
        [("overall function, so the signal to your foot arrives weaker", F_BODY, BLACK)],
        [("and later. elite midfielders miscontrol 23% more touches after", F_BODY, BLACK)],
        [("minute 70. that is why your touch lands 30-40 cm farther than it did", F_BODY, BLACK)],
        [("in the first half while the defender closes the space and takes", F_BODY, BLACK)],
        [("the ball away from you before you can react.", F_BODY, BLACK)],
    ]
    draw_rich_paragraph(draw, top_paragraph, 275, line_gap=6)

    # Reference photo frame at the design.md spec
    draw_placeholder_frame(draw)

    # Lower section — fix + payoff embedded in one block, 9+ words per line
    fix_paragraph = [
        [("the fix: after your main session, spend 10 minutes on wall", F_BODY_BOLD, BLACK),
         (" passes alone. constraint: every third touch must be one-timed into", F_BODY, BLACK)],
        [("a shoebox-sized target you tape to the wall. the smaller target", F_BODY, BLACK)],
        [("forces your motor cortex to maintain precision when fatigue would", F_BODY, BLACK)],
        [("normally let it shut down, so your touch stays clean and relaxed", F_BODY, BLACK)],
        [("in minute 80 even when the defender expects you to lose the ball", F_BODY, BLACK)],
        [("because your brain stays sharp even under late-game pressure.", F_BODY, BLACK)],
    ]
    draw_rich_paragraph(draw, fix_paragraph, 990, line_gap=6)

    # Source line — bottom centered, ≥32 px above bottom margin
    center_text(draw, "Mohr, Krustrup & Bangsbo — J Sports Sci 2003",
                1280, F_SOURCE, DARK_GRAY)

    img.save(OUT)
    assert img.size == (W, H), img.size
    print(f"saved {OUT} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()

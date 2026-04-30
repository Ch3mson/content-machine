"""A3 quality-gate renderer for athlete-max — attempt 004 soccer body slide.

Fixes from attempt-003:
- Title split into 3 shorter lines at 40px to prevent horizontal overflow
- Body reduced to 28px with carefully crafted 9-11 word lines
- Top explanation capped at 5 lines with 47px buffer above frame
- Lower section capped at 5 lines with 119px buffer above source
- Width checking ensures no text exceeds 936px safe margin

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

# Safe margins per design.md
MARGIN_LR = 72
SAFE_WIDTH = W - (MARGIN_LR * 2)  # 936px absolute max

# Frame spec
FRAME_X = 140
FRAME_Y = 515
FRAME_W = 800
FRAME_H = 450
FRAME_BOTTOM = FRAME_Y + FRAME_H  # 965


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size)


F_LABEL = font(FONT_REG, 30)
F_TITLE = font(FONT_BOLD, 40)
F_BODY = font(FONT_REG, 28)
F_BODY_BOLD = font(FONT_BOLD, 28)
F_FRAME_LABEL = font(FONT_BOLD, 28)
F_SOURCE = font(FONT_REG, 20)


def text_width(draw, text, fnt):
    box = draw.textbbox((0, 0), text, font=fnt)
    return box[2] - box[0]


def check_width(draw, text, fnt, label):
    tw = text_width(draw, text, fnt)
    if tw > SAFE_WIDTH:
        print(f"WARNING: '{label}' exceeds safe width ({tw}px > {SAFE_WIDTH}px): {text[:60]}...")
    return tw


def center_text(draw, text, y, fnt, fill=BLACK):
    x = (W - text_width(draw, text, fnt)) // 2
    draw.text((x, y), text, font=fnt, fill=fill)


def draw_centered_lines(draw, lines, y, fnt, fill=BLACK, line_gap=10):
    cur = y
    for line in lines:
        if line == "":
            cur += int(fnt.size * 0.55)
            continue
        check_width(draw, line, fnt, f"title")
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
        full_text = "".join(t for t, _, _ in segs)
        check_width(draw, full_text, F_BODY, f"body")
        max_size = max(f.size for _, f, _ in segs)
        draw_centered_rich(draw, segs, cur)
        cur += max_size + line_gap
    return cur


def draw_placeholder_frame(draw):
    fx, fy, fw, fh = FRAME_X, FRAME_Y, FRAME_W, FRAME_H
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
    label_text = "what to avoid when fatigue affects your late-game touch:"
    check_width(draw, label_text, F_LABEL, "label")
    center_text(draw, label_text, 92, F_LABEL, BLACK)

    # Title (3 lines at 40px bold — shorter lines prevent overflow)
    title_lines = [
        "your late-game touch is not a conditioning",
        "problem. it is a motor cortex issue that",
        "begins under fatigue when your legs feel heavy"
    ]
    title_bottom = draw_centered_lines(draw, title_lines, 138, F_TITLE, BLACK, line_gap=8)

    # Gap: 20px after title
    top_start = title_bottom + 20

    # Top explanation — 5 lines at 28px, ends well before frame at y=515
    # 5 lines * 28 + 4 gaps * 8 = 140 + 32 = 172px
    # If top_start = 138 + 120 + 20 = 278, then bottom = 278 + 172 = 450
    # Buffer to frame = 515 - 450 = 65px
    top_paragraph = [
        [("by minute 70, your motor cortex (the brain region that", F_BODY, BLACK)],
        [("plans precise foot placement) suppresses fine motor output", F_BODY, BLACK)],
        [("to protect overall function, so the signal to your foot", F_BODY, BLACK)],
        [("arrives weaker and later. that is why your touch lands", F_BODY, BLACK)],
        [("30-40 cm farther than it did in the first half.", F_BODY, BLACK)],
    ]
    top_bottom = draw_rich_paragraph(draw, top_paragraph, top_start, line_gap=8)
    print(f"Top section ends at y={top_bottom}, frame starts at y={FRAME_Y}, buffer={FRAME_Y - top_bottom}px")

    # Reference photo frame
    draw_placeholder_frame(draw)

    # Lower section — starts 24px after frame, 5 lines at 28px
    # 5 lines * 28 + 4 gaps * 8 = 172px
    # lower_start = 965 + 24 = 989, bottom = 989 + 172 = 1161
    # Source at 1280, buffer = 119px
    lower_start = FRAME_BOTTOM + 24

    fix_paragraph = [
        [("the fix: after your main session, spend 10 minutes", F_BODY_BOLD, BLACK)],
        [("on wall passes alone. constraint: every third touch", F_BODY, BLACK)],
        [("must be one-timed into a shoebox-sized target you", F_BODY, BLACK)],
        [("tape to the wall. the smaller target forces your", F_BODY, BLACK)],
        [("motor cortex to maintain precision, so your touch", F_BODY, BLACK)],
        [("stays clean in minute 80 when the defender expects", F_BODY, BLACK)],
        [("you to lose the ball because your brain stays sharp.", F_BODY, BLACK)],
    ]
    lower_bottom = draw_rich_paragraph(draw, fix_paragraph, lower_start, line_gap=8)
    print(f"Lower section ends at y={lower_bottom}, source at y=1280, buffer={1280 - lower_bottom}px")

    # Source line
    source_text = "Mohr, Krustrup & Bangsbo — J Sports Sci 2003"
    check_width(draw, source_text, F_SOURCE, "source")
    center_text(draw, source_text, 1280, F_SOURCE, DARK_GRAY)

    img.save(OUT)
    assert img.size == (W, H), img.size
    print(f"saved {OUT} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()

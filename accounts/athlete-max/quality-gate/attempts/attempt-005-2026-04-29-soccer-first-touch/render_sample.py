"""A3 quality-gate renderer for athlete-max — attempt 005 soccer body slide.

Structural change from attempt-004:
- Title IS the topic label (like verified_byhumans: "passive reading (synaptic pruning)")
- No separate small label above title
- Old contrarian hook embedded into top explanation
- Title at 60px bold, short topic name with optional technical parenthetical

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

# Safe margins
MARGIN_LR = 72
SAFE_WIDTH = W - (MARGIN_LR * 2)  # 936px

# Frame spec
FRAME_X = 140
FRAME_Y = 515
FRAME_W = 800
FRAME_H = 450
FRAME_BOTTOM = FRAME_Y + FRAME_H  # 965


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size)


F_TITLE = font(FONT_BOLD, 60)
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

    # Title — topic name only, large bold (like verified_byhumans)
    # "late-game touch (motor cortex)" at 60px bold
    title_text = "late-game touch (motor cortex)"
    check_width(draw, title_text, F_TITLE, "title")
    center_text(draw, title_text, 110, F_TITLE, BLACK)

    # Small gap then top explanation
    top_start = 185

    # Top explanation — contrarian hook + TAP-R mechanism, 5 lines
    top_paragraph = [
        [("your late-game touch is not a conditioning problem. by minute 70,", F_BODY, BLACK)],
        [("your motor cortex (the brain region that plans precise foot placement)", F_BODY, BLACK)],
        [("suppresses fine motor output to protect overall function, so the", F_BODY, BLACK)],
        [("signal to your foot arrives weaker and later. that is why your touch", F_BODY, BLACK)],
        [("lands 30-40 cm farther than it did in the first half.", F_BODY, BLACK)],
    ]
    top_bottom = draw_rich_paragraph(draw, top_paragraph, top_start, line_gap=8)
    print(f"Top section ends at y={top_bottom}, frame starts at y={FRAME_Y}, buffer={FRAME_Y - top_bottom}px")

    # Reference photo frame
    draw_placeholder_frame(draw)

    # Lower section — fix + payoff embedded, starts 24px after frame
    lower_start = FRAME_BOTTOM + 24

    fix_paragraph = [
        [("the fix: after your main session, spend 10 minutes", F_BODY_BOLD, BLACK)],
        [("on wall passes alone. constraint: every third touch must be", F_BODY, BLACK)],
        [("one-timed into a shoebox-sized target you tape to the wall.", F_BODY, BLACK)],
        [("the smaller target forces your motor cortex to maintain", F_BODY, BLACK)],
        [("precision, so your touch stays clean in minute 80 when the", F_BODY, BLACK)],
        [("defender expects you to lose the ball because your brain", F_BODY, BLACK)],
        [("stays sharp under late-game pressure.", F_BODY, BLACK)],
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

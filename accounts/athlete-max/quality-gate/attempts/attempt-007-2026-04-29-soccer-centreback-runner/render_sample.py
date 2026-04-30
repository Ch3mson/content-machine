"""A3 quality-gate renderer for athlete-max — attempt 007 soccer centreback body slide.

Structural format: verified_byhumans Post 1 listing style.
- Label: "what to avoid:" (small regular)
- Title: short topic name (large bold)
- Explanation with contrarian hook embedded
- Photo centered
- Fix + payoff embedded
- Source

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

# Frame spec — centered on canvas
FRAME_W = 800
FRAME_H = 450
FRAME_X = (W - FRAME_W) // 2  # 140

# Recalculated for attempt 007 (6-line top, 6-line lower)
# label 80, title 130, top_start 205
# top returned = 205 + 6*36 = 421
# gap = 65, frame_y = 486, frame_bottom = 936
# lower_start = 936 + 65 = 1001
# lower returned = 1001 + 6*36 = 1217
# source at 1270 (53px gap), source bottom = 1290, bottom margin = 60px
FRAME_Y = 486
FRAME_BOTTOM = FRAME_Y + FRAME_H  # 936


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size)


F_LABEL = font(FONT_REG, 30)
F_TITLE = font(FONT_BOLD, 56)
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
        check_width(draw, full_text, F_BODY, "body")
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
    label_text = "what to avoid:"
    check_width(draw, label_text, F_LABEL, "label")
    center_text(draw, label_text, 80, F_LABEL, BLACK)

    # Title
    title_text = "runners getting in behind you"
    check_width(draw, title_text, F_TITLE, "title")
    center_text(draw, title_text, 130, F_TITLE, BLACK)

    # Top explanation starts after title
    top_start = 205

    top_paragraph = [
        [("your late-game reads are not a reaction problem. by minute 70,", F_BODY, BLACK)],
        [("central fatigue narrows your attention around the ball so your", F_BODY, BLACK)],
        [("brain filters out the runner behind your shoulder. that is why the", F_BODY, BLACK)],
        [("runner gets in behind your line in the final 15 minutes even though", F_BODY, BLACK)],
        [("you watched the pass and never saw them until the ball was played", F_BODY, BLACK)],
        [("and they were already through on goal before you could recover.", F_BODY, BLACK)],
    ]
    top_bottom = draw_rich_paragraph(draw, top_paragraph, top_start, line_gap=8)
    print(f"Top section ends at y={top_bottom}, frame starts at y={FRAME_Y}, buffer={FRAME_Y - top_bottom}px")

    # Reference photo frame
    draw_placeholder_frame(draw)

    # Lower section
    lower_start = FRAME_BOTTOM + 65  # 936 + 65 = 1001

    fix_paragraph = [
        [("the fix:", F_BODY_BOLD, BLACK),
         (" after your main session, spend 10 minutes scanning from", F_BODY, BLACK)],
        [("the ball to the space behind you in a deliberate two-second rhythm.", F_BODY, BLACK)],
        [("constraint:", F_BODY_BOLD, BLACK),
         (" you must call out the runner before you turn back to", F_BODY, BLACK)],
        [("the ball. this keeps your peripheral vision active, so you still", F_BODY, BLACK)],
        [("see the late run in minute 80 when your legs are tired and the", F_BODY, BLACK)],
        [("striker expects to slip in behind you without you noticing.", F_BODY, BLACK)],
    ]
    lower_bottom = draw_rich_paragraph(draw, fix_paragraph, lower_start, line_gap=8)
    print(f"Lower section ends at y={lower_bottom}, source at y=1270, buffer={1270 - lower_bottom}px")

    # Source line
    source_text = "Williams, Hodges & Elliott — J Sports Sci 1999, PMID: 10408340"
    check_width(draw, source_text, F_SOURCE, "source")
    center_text(draw, source_text, 1270, F_SOURCE, DARK_GRAY)

    img.save(OUT)
    assert img.size == (W, H), img.size
    print(f"saved {OUT} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()

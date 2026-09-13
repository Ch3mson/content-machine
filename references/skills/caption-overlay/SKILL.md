---
name: caption-overlay
description: Render approved caption text onto an antigpt still with tools/fal/caption.py (TikTok Sans, white with black outline, centered). Use when the user says caption this, overlay text, put the line on the still, add the text, or wants the WISH / pain line rendered on a post image.
---

# Caption Overlay

## Overview

The still is done; this step puts the words on it. Copy is approved in chat
before anything is rendered. The renderer preserves manual line breaks, so the
approved lines are exactly what appears.

Read `accounts/antigpt/account-brief.md` (Copy Rules For The Still) and the
hook pattern in
`references/hook-ideas/cards/2026-09-08-bellajobtips-crying-girl-single.md`
before drafting.

## Step 1: Draft and approve the copy

1. Write 2-4 candidate captions. Each is one idea, two to three short lines,
   first person, no lists.
2. Run Stop Slop (`references/skills/stop-slop/SKILL.md`) on each.
3. If a line names AntiGPT or a detector, use wording from
   `product/antigpt-claim-bank.md` only.
4. Paste the candidates in chat with explicit line breaks and wait for the user
   to approve one. Do not render before approval.
5. Save the approved lines under "Approved copy" in `posts/N/caption.md`.

## Step 2: Render

```bash
python tools/fal/caption.py --image accounts/antigpt/posts/2/image.jpg \
  --text "Things I WISH I knew\nbefore my first all-nighter"
```

Writes `accounts/antigpt/posts/2/image_caption.jpg`. The clean `image.jpg`
stays untouched.

Defaults are the accepted look: TikTok Sans Bold 42 px, 5 px black outline,
block centered at 48% height, 14 px between lines. Adjust only when the user
asks:

| Ask | Flag |
| --- | --- |
| Higher / lower | `--y 0.40` (fraction of image height) |
| Bigger / smaller | `--size 48` |
| Top-of-image caption like the source posts | `--anchor top --y 0.18` |
| Tighter lines | `--gap 8` |
| Thinner outline | `--stroke 4` |

Show the rendered file to the user. If a line prints a "wider than" warning,
shorten the line or add a manual break rather than shrinking the font below
36 px.

## Rules

- Never render unapproved copy, including placeholder text on a post still.
  Test renders go to `/tmp`.
- Preserve the approved line breaks exactly. Do not reflow.
- Emoji are allowed when approved; they render with Apple Color Emoji.
- Justified text and per-word spacing tricks are banned; centered only.
- Keep the CTA out of the hook line. An on-image CTA, if approved, is its own
  short final line.

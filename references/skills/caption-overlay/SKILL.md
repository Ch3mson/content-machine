---
name: caption-overlay
description: Add approved text to antigpt images or slideshow slides using the current account style. Use when the user says caption this, overlay text, put the line on the still, add the text, or wants a study-tip headline rendered on a post image.
---

# Caption Overlay

## Overview

The still is done; this step puts the words on it. Copy is normally approved in
chat before rendering. A request for complete slideshow drafts to review after
assembly authorizes rendering draft copy in the working timeline; final visual
approval still gates permanent exports. The renderer preserves manual line breaks, so the
approved lines are exactly what appears.

Read `accounts/antigpt/account-brief.md` (Copy Rules For Slides) before drafting.
For slideshow copy, fetch the relevant Notion writing examples linked in
`references/notion.md`. Current user direction supersedes older single-still
and first-person complaint rules.

## Step 1: Draft and approve the copy

1. Draft the requested slides or candidate headlines following the current
   account brief. The hook promises a specific academic payoff. Each content
   slide has one numbered technique/title block and optionally a second block
   with one short explanatory sentence. Keep the top heading brief; the lower
   block may be slightly more elaborative per the latest account brief.
   No paragraphs. Preserve an approved `>>>` cue.
2. Run Stop Slop (`references/skills/stop-slop/SKILL.md`) on each.
3. If a line names AntiGPT or a detector, use wording from
   `product/antigpt-claim-bank.md` only.
4. Paste the candidates in chat with explicit line breaks. Normally wait for
   copy approval; when Benson asks for finished drafts to review together,
   assemble the draft copy and leave final approval for the complete result.
5. For a slideshow, keep working copy in
   `accounts/antigpt/outputs/slideshow-draft/posts/N/caption.md` until final visual
   approval; an existing unfinished post can keep its current record. Archive
   the approved version in `posts/N/caption.md` with its finished outputs.
   Include `posts/N/caption.txt` with the posting TITLE and DESCRIPTION for
   quick copy/paste; keep the plain text synchronized with the record.
   For the legacy single-still format, save approved lines directly in its post record.

## Step 2: Render

The current approved slideshow style is dark purple text (#552082) on light
purple highlights (#E9D5FF), on a 9:16 canvas with separate top and bottom text
layers. Use native CapCut layers for CapCut requests. Enable the background
highlight on every text layer; color values alone do not activate it. See the
account brief and post 3 for the approved settings.

Append to the existing CapCut timeline in 15-second post sections, preserving
earlier posts. Follow [the CapCut workflow](../../capcut-slideshow-workflow.md):
after approval of the finished post following modifications, capture ordered
slide images for TikTok and export an MP4 for Instagram Reels into `posts/N/`
for that post's range. Save `01.png`–`05.png` directly beside `reel.mp4` and
the caption files. Keep clean sources in `assets/post-sources/N/` so the post
folder stays flat. Keep the accumulated timeline intact. Copy approval alone
does not finalize that package.

The current command renders one centered text block on one still. Independent
heading/explanation placement and highlighted backgrounds need additional CLI
implementation. Do not use the legacy command's white-text default as the
current account style or claim it already implements the CapCut layout.

```bash
python tools/fal/caption.py --image accounts/antigpt/posts/2/image.jpg \
  --text "Things I WISH I knew\nbefore my first all-nighter"
```

Writes `accounts/antigpt/posts/2/image_caption.jpg`. The clean `image.jpg`
stays untouched.

Legacy CLI defaults are TikTok Sans Bold 42 px, 5 px black outline, a block
centered at 48% height, and 14 px between lines. These describe the existing
script, not the current approved purple-highlight look. Its available controls:

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

- Render new draft copy only when the user requests assembly for later review;
  otherwise get copy approval first. Never treat draft or placeholder copy as
  an approved post. Test renders go to `/tmp`.
- Preserve the approved line breaks exactly. Do not reflow.
- Emoji are allowed when approved; they render with Apple Color Emoji.
- Justified text and per-word spacing tricks are banned; centered only.
- Keep the CTA out of the hook line. An on-image CTA, if approved, is its own
  short final line.

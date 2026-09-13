---
name: avatar-face-swap
description: Face-swap the locked antigpt avatar onto composition boards with fal Seedream edit using tools/fal/swap_avatar.py. Use when the user says face swap, swap her onto, put the avatar on, put her in this, new still from this board, batch these boards, or wants a new selfie still for a post.
---

# Avatar Face-Swap

## Overview

Every posted still is the one locked girl (`accounts/antigpt/avatar/anchor.jpg`)
edited onto someone else's study photo (a "board"). The script carries the
identity-lock prompt, so you never type it. Your job is to get the boards in
place, run the batch, show the contact sheet, and promote the keeper.

Read `accounts/antigpt/README.md` first for the boards and posts tables.

## Step 1: Get the boards

| User gave | Do this |
| --- | --- |
| Files already in `accounts/antigpt/boards/` | Use them directly |
| A local photo or folder (Pinterest saves, screenshots) | Copy into `accounts/antigpt/boards/` with a descriptive slug like `cafe-headphones-latte.jpg` |
| A TikTok photo URL | `python tools/tiktok-photo-sourcer/download_tiktok_photos.py --out accounts/antigpt/boards "<url>"`, then rename the numbered files to slugs |
| An Instagram URL | `gallery-dl --cookies-from-browser chrome -D accounts/antigpt/boards "<url>"`, then rename |

Add one row per new board to the Boards table in `accounts/antigpt/README.md`
(file, one-line composition, source).

## Step 2: Run the swap

Batch every board into a review folder with a contact sheet:

```bash
python tools/fal/swap_avatar.py accounts/antigpt/boards
```

Selected boards, two takes each, extra scene direction:

```bash
python tools/fal/swap_avatar.py accounts/antigpt/boards/study-selfie-03.jpg accounts/antigpt/boards/study-selfie-05.jpg \
  --variants 2 --scene "warm late-night lamp light, tired but calm"
```

Output lands in `accounts/antigpt/review/{stamp}/` (gitignored) as
`{board-stem}.jpg` plus `contact-sheet.jpg`. Show the contact sheet to the user
and list the per-board paths.

Useful flags: `--dry-run` (plan only), `--prompt-only` (print the prompt),
`--keep-text` (do not strip source text), `--size 1080x1920` (full vertical),
`--workers 3`, `--out-dir`.

## Step 3: Promote the keeper

When the user picks a specific review image, copy that exact file to the next
unused `accounts/antigpt/posts/N/image.jpg`. Create `caption.md` by hand using
the structure in `posts/2/caption.md`, recording the selected board and review
path with no approved copy unless approval already exists. Check the target
and status before copying; never silently overwrite an existing post.

For a requested fresh render from a board directly into a post folder, use:

```bash
python tools/fal/swap_avatar.py accounts/antigpt/boards/study-selfie-03.jpg --post 3
```

This generates from the board (one fresh call), writes
`accounts/antigpt/posts/3/image.jpg`, and creates `caption.md` if missing. It
does not preserve a selected review image; do not use it as a copy command.

Then add the row to the Posts table in `accounts/antigpt/README.md`.

Captioning is a separate step: `references/skills/caption-overlay/SKILL.md`.

## Rules

- Never generate a different girl. If the anchor is missing, stop and ask.
- The board decides pose, outfit, crop, scene, and facial expression. The
  anchor decides face, ears, hair type, and earrings. Do not add the anchor
  pout unless the user asks. Do not "improve" the board composition in the
  prompt unless the user asks; put small adjustments in `--scene`.
- Source on-screen text, stickers, and watermarks are stripped by default. Only
  pass `--keep-text` when the user says so.
- `--post` refuses to overwrite an existing `posts/N/image.jpg`. Do not pass
  `--force` on a post marked Posted without the user saying so.
- Boards are other people's photos. They stay in `boards/` and are never
  posted or captioned.
- Default size is 1080x1440 (3:4 portrait). Use 1080x1920 only when the user
  asks for full-screen TikTok.
- One fal edit costs a few cents and takes 20-60 s. Batches of 6 with 3 workers
  finish in about two minutes; tell the user before starting anything over 12
  calls.

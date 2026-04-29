# Workflow C: Image Processing

Use this when the user says `workflow c`, `process images`, `render slides`, or
when Workflow B reaches image rendering.

Goal: produce final PNG slideshow images from mapped raw photos and slide copy,
using the target account's `design.md` as the layout source of truth.

## Read First

1. `../AGENTS.md`
2. Target account `design.md`
3. Target account `image.md`
4. Target account `writing.md`, only to preserve copy rhythm and line breaks;
   read indexed writing subfiles only if `writing.md` says they affect rendering
   or manual line breaks
5. Target post `flow.md`
6. Existing target post `process_images.py`, if present

## Pipeline Order

Run the image operations in this exact order:

1. Create the final canvas at the size specified in account `design.md`.
2. Crop or frame each selected photo according to account `design.md`.
3. Apply the account visual treatment from `image.md`.
4. Add text overlay according to account `design.md`.

Do not add text before normalization. Text placement depends on the final canvas.

## Default Processing Rules

Account `design.md` overrides canvas, placement, typography, and text layout.
Account `image.md` overrides photo treatment.

| Setting | Default |
| --- | --- |
| Canvas | Use account `design.md`; fallback `1080x1920` PNG |
| Crop | Center crop, no stretching |
| B&W | Grayscale plus 1.3 contrast |
| Overlay | Same subtle paper overlay for every slide |
| Font | Arial Bold |
| Font size | 36 pt |
| Text color | White |
| Text outline | Black, 3 px |
| Line spacing | 16 px |
| Side margins | 140 px |
| Wrapping | Respect manual line breaks from `flow.md`; do not auto-rewrite copy |

## Procedure

1. Parse `flow.md`:
   - Extract slide number, role, image filename, and final copy.
   - Preserve quote marks and manual line breaks.

2. Confirm source images:
   - Resolve image paths relative to the post folder.
   - Use `sourced/` when the flow points there.
   - Report missing images by filename and slide number.

3. Create or update `process_images.py`:
   - Keep the script post-specific.
   - Store slide mappings in the script.
   - Use canvas dimensions, photo frame placement, typography, margins, and
     section layout from account `design.md`.
   - Load `C:/Windows/Fonts/arial.ttf` and `C:/Windows/Fonts/arialbd.ttf` if
     available.
   - Save outputs to `processed/`.

4. Run the script:
   - Command pattern: `python accounts/{account}/{post-name}/process_images.py`.
   - Do not skip failed images silently. The script should print skipped files.

5. Verify outputs:
   - Use Pillow or image metadata to confirm every PNG matches the canvas size in
     account `design.md`.
   - Check that the number of processed slides matches the flow.
   - If text exceeds margins, edit line breaks in `flow.md` and rerun.

## Agent Rules

- Use exact copy from `flow.md`.
- Do not reword copy inside the image script.
- Use `design.md` for layout, typography, text hierarchy, reference-photo
  framing, and final output size.
- Use the same overlay for all slides in one post.
- Preserve the account's visual rules even when source photos differ.
- Report font fallback if Arial Bold is unavailable.

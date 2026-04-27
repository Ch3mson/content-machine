# Workflow C: Image Processing

Use this when the user says `workflow c`, `process images`, `render slides`, or
when Workflow B reaches image rendering.

Goal: produce final 9:16 PNG slideshow images from mapped raw photos and slide
copy.

## Read First

1. `../AGENTS.md`
2. Target account `image.md`
3. Target account `writing.md`, only to preserve copy rhythm and line breaks
4. Target post `flow.md`
5. Existing target post `process_images.py`, if present

## Pipeline Order

Run the image operations in this exact order:

1. Normalize every source image to 1080x1920.
2. Convert to black and white.
3. Apply the account paper/texture/overlay treatment.
4. Add text overlay.

Do not add text before normalization. Text placement depends on the final canvas.

## Default Processing Rules

Account `image.md` overrides these defaults.

| Setting | Default |
| --- | --- |
| Canvas | 1080x1920 PNG |
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
   - Load `C:/Windows/Fonts/arialbd.ttf` if available.
   - Save outputs to `processed/`.

4. Run the script:
   - Command pattern: `python accounts/{account}/{post-name}/process_images.py`.
   - Do not skip failed images silently. The script should print skipped files.

5. Verify outputs:
   - Use Pillow or image metadata to confirm every PNG is exactly 1080x1920.
   - Check that the number of processed slides matches the flow.
   - If text exceeds margins, edit line breaks in `flow.md` and rerun.

## Agent Rules

- Use exact copy from `flow.md`.
- Do not reword copy inside the image script.
- Use the same overlay for all slides in one post.
- Preserve the account's visual rules even when source photos differ.
- Report font fallback if Arial Bold is unavailable.

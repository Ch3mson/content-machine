# Image Rules: Athlete Stories Account

Use this file for photo direction, visual treatment, and selected-photo
suitability. Use `design.md` for canvas size, layout, typography, text
placement, crop dimensions, and renderer-facing format rules.

Do not use this file as the source of truth for text layout.

## Visual Treatment

- Convert all selected photos to black and white.
- Increase contrast by 1.3x so the athlete and text remain readable.
- Apply the same vintage paper overlay to every slide in a post.
- Keep faces, body posture, and the main sport action clear after treatment.
- Avoid photos where the subject disappears into a dark background after B&W.

## Pipeline Order

The processing pipeline must run in this order:

1. Frame the selected photo according to `design.md`.
2. Convert the framed photo to B&W.
3. Apply the paper overlay.
4. Add text according to `design.md`.

## Paper Overlay Rules

- Apply the same paper overlay to all slides in a slideshow for consistency.
- Warm sepia grain: random pixels with R 180-220, G 160-195, B 130-160, alpha 15-35.
- Darker grain spots: small clusters of R 100-150, G 80-130, B 60-100, alpha 10-30.
- Vignette: dark edges that increase in opacity toward corners. Max alpha 120.
- The overlay must be subtle enough to not obscure faces or text, but visible
  enough to create a vintage feel.

## Photo Crop Notes

- Target canvas and crop dimensions come from `design.md`.
- Crop from center. Never stretch or distort the image.
- Keep the athlete, face, or key action in the readable center of the frame.
- If a source image is too narrow for the canvas, pad with black bars instead of
  stretching.

## Product Slide Treatment

- The product slide uses a native phone-in-hand photo.
- Keep the same B&W and paper overlay treatment as the rest of the post.
- No additional branding or logos on the image.
- Product mention is woven into the copy, not the design.

## Image Role Notes

- Use `design.md` for slide count, layout, typography, text placement, and renderer-facing rules.
- Use `writing.md` and the target `flow.md` for copy rhythm and slide text.
- Use this file only to decide whether a selected photo fits the intended slide role and visual treatment.

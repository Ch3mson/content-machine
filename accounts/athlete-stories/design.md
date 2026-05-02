# Design System: Athlete Stories

Status: `Locked`

This is the account source of truth for slide composition, typography, text
placement, and renderer-facing layout rules. Use `image.md` for photo subject
direction and visual treatment details.

## Canvas

- Output size: `1080x1920` PNG.
- Aspect ratio: `9:16`.
- Background: full-bleed selected photo on every slide.
- Safe margins: `140px` minimum on left and right.
- Slide count pattern: locked 7-slide story arc.

## Reference Photo Framing

- Placement: full canvas, behind all text.
- Size: fill the full `1080x1920` canvas.
- Crop behavior: center crop to 9:16; never stretch or distort.
- Alignment: keep the athlete, face, or key action readable after crop.
- Consistency rule: every slide uses the same full-bleed framing system.
- Do not: add inset frames, cards, logos, decorative borders, or ad-style
  product layouts.

## Typography

- Primary font: Arial Bold.
- Font file preference: `C:/Windows/Fonts/arialbd.ttf`.
- Body font: Arial Bold.
- Quote font: Arial Bold.
- Letter spacing: `0`.
- Text color: white `#FFFFFF`.
- Text outline: black stroke, `3px`.
- Text alignment: centered horizontally and vertically.
- Line spacing: `16px` between manual lines.

## Text Hierarchy

| Element | Font / weight | Size | Placement | Notes |
| --- | --- | --- | --- | --- |
| Story copy | Arial Bold | 36 pt | Centered on slide | Use exact `flow.md` copy. |
| Product copy | Arial Bold | 36 pt | Centered on slide | Same treatment as story slides. |
| Closing quote | Arial Bold | 36 pt | Centered on slide | No narrator text after the quote. |

## Slide Layouts

### Slide 1: The Beginning

- Photo: athlete origin, struggle, or identity context.
- Text: centered, short, staccato, fact-led unless the selected preset says a
  second-person challenge is required.

### Slides 2-3: The Grind / The Weight

- Photo: training, pressure, isolation, rivalry, or study context.
- Text: centered and slightly longer than Slide 1, with one clear story beat.

### Slide 4 or 5: The Peak / Mental Turn

- Photo: focused, meditating, visualizing, headphones, film study, or composed
  pre-performance context.
- Text: centered. This may be the longest slide when the preset needs the
  visualization reveal to breathe.

### Slide 5 or 6: The Transformation / Product Bridge

- Photo: transformation, iconic moment, or native phone-in-hand context.
- Text: centered. The product slide must use the same typography, crop, and
  treatment as the rest of the post.

### Slide 7: The Legend

- Photo: iconic athlete moment.
- Text: centered quote only. Do not add commentary after the quote.

## Bold And Highlight Rules

- All visible text uses the same bold treatment.
- Do not bold individual words inside the slide copy.
- Do not add highlight colors, callout boxes, or underline treatments.
- The design gets emphasis from short copy, centered placement, and contrast.

## Renderer Rules

- Use exact text from `flow.md`.
- Preserve manual line breaks from `flow.md`.
- Normalize and crop the selected photo before adding text.
- Keep text centered on every slide.
- Keep the same font, outline, line spacing, and safe margins across all slides.
- Check line width before final render. If any line leaks past the `140px` safe margins, fix the manual line break in the copy source before rendering again; do not let the renderer silently shrink or rewrite copy.
- Final PNGs must be exactly `1080x1920`.

## QA Checklist

- [ ] Every slide is `1080x1920`.
- [ ] Photo is full bleed and not stretched.
- [ ] Text is centered and inside the `140px` side margins.
- [ ] Long lines have been manually split in the copy source before render.
- [ ] White text remains readable against the photo.
- [ ] Product slide does not look like a separate ad.
- [ ] Manual line breaks from `flow.md` are preserved.

## Quality Gate Notes

- Latest approved sample: `quality-gate/attempts/attempt-002-2026-04-29-ronaldo-product-bridge/sample-slide.png`.
- Current blocker: none. Workflow A3 approved a representative non-hero rendered sample on 2026-04-29.
- Last revision notes: Existing visual system preserved. Design authority remains in this file; `image.md` stays limited to photo direction and visual treatment. The approved sample validated full-bleed B&W treatment, centered Arial Bold text, outline readability, manual line breaks, and safe margins. Ali/Liston quality-gate redo added a render QA rule: long lines must be manually split before render if they exceed safe margins.

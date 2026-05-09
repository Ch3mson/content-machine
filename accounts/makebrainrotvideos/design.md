# Design System — makebrainrotvideos

## Status

- **Stage**: Locked
- **Last updated**: 2026-05-07
- **Locked**: Yes — approved in quality gate attempt 001 (2026-05-07).
- **Approved sample**: `quality-gate/attempts/attempt-001-2026-05-07-tool-step/sample-slide.png`

## Canvas

- **Output size**: 1080 x 1920 px
- **Aspect ratio**: 9:16 (TikTok and Instagram native)
- **Background**: Full-bleed photo with dark overlay, or solid dark background
  (#0A0A0A to #1A1A2E range)
- **Safe margins**: 120px all sides. No text or critical visual elements outside
  the safe area.
- **Slide count**: 5-7 per post. Minimum 5, maximum 8.
- **Export format**: PNG

## Reference Photo Framing

- **Placement**: Full-bleed behind text. Photo fills the entire 1080x1920 canvas.
- **Size**: Cover crop. No letterboxing, no borders.
- **Crop behavior**: Center crop. Maintain subject focus. If the subject is a
  person or object, keep it roughly centered.
- **Alignment**: Photo content should not compete with text. If the photo has a
  busy area, position text over a calmer region or increase overlay opacity.
- **Consistency**: All body slides in a post should use the same overlay opacity
  and text placement style. Do not mix dark and light treatments within one post.
- **Do not**: Use multiple photos per slide. Use photo collages. Place photos in
  frames or borders. Use clipart or illustrations (exception: the 1.5M viral
  infographic style, which can be used sparingly).

## Typography

- **Primary font**: Arial Bold or Inter Bold. System sans-serif fallback.
- **Letter spacing**: 0 to +2%. No tight tracking.
- **Text color**: White (#FFFFFF) for all slide text.
- **Text shadow/stroke**: 2-3px black stroke outline OR drop shadow (0px 2px 8px
  rgba(0,0,0,0.7)) for readability over photos. Use one method consistently
  per post.
- **Alignment**: Center-aligned horizontally. Vertically centered in safe area,
  or placed in lower-center third for hook slides with dominant imagery above.
- **Line breaks**: Manual line breaks to keep each line 3-6 words. Never let
  text auto-wrap to create unbalanced lines.

## Text Hierarchy

| Element | Size | Weight | Use |
| --- | --- | --- | --- |
| Hook title | 72-96pt | Bold | Slide 1 only. The scroll-stopping line. |
| Step label | 48-60pt | Bold | "Step 1:", "Step 2:", etc. on body slides. |
| Body text | 36-48pt | Bold | Description text below step labels. One line. |
| CTA / reveal | 48-60pt | Bold | Last slide. Product name or call to action. |
| Small text | 24-28pt | Regular or Bold | URL, "link in bio", attribution. Bottom of slide. |

All text remains white. No colored text, no highlight backgrounds, no underlines.

## Slide Layouts

### Hook Slide (Slide 1)

- Full-bleed lifestyle/money photo with 60-70% black overlay.
- Hook text centered in the middle-to-lower third.
- Hook text at 72-96pt, bold, white with stroke.
- No step labels, no product mentions.
- Optional: small "Swipe →" indicator at bottom-right (24pt, 50% opacity white).

### Body / Step Slides (Slides 2-6)

- Full-bleed photo with 65-80% black overlay (slightly darker than hook to
  prioritize text readability).
- Step label ("Step 1:") at 48-60pt, centered, upper portion of safe area.
- Body text below step label at 36-48pt, centered. One line only.
- Each slide uses a different photo that matches the step content:
  - Niche/topic steps → relevant lifestyle imagery.
  - Tool steps → screenshot of the tool or platform UI.
  - Results steps → earnings screenshots, view counts, dashboard.
- Alternative (non-step slides): single centered text at 48-60pt. No step label.

### Product / CTA Slide (Last Slide)

- Always use a sourced background image with a dark overlay (40-60%). Do not use a solid dark background.
- Keep it clean. One visual element, one text element.

## Bold and Highlight Rules

- All text is bold by default. No mixing of regular and bold within slides.
- No colored highlights, no underlines, no italic.
- No emoji in slide text (emoji OK in captions only).
- If emphasis is needed, increase font size by one tier (e.g., 48pt → 60pt).

## Renderer Rules

These are concrete instructions for Workflow C or any rendering script.

1. Load the source photo at 1080x1920, center-cropped.
2. Apply black overlay at the specified opacity (see slide type).
3. Render text centered horizontally in the safe area (120px margins).
4. Apply 2-3px black stroke to all white text.
5. Export as PNG at 1080x1920, no compression artifacts.
6. File naming: `slide_01.png`, `slide_02.png`, etc.
7. Verify all text fits within safe margins on export. If text overflows, reduce
   font size by one tier before re-rendering.

## QA Checklist

### Canvas
- [ ] Output is 1080x1920 PNG.
- [ ] Background is dark (not white, not bright).
- [ ] All text within 120px safe margins.

### Photo
- [ ] Full-bleed, center-cropped, no borders or frames.
- [ ] Overlay opacity matches slide type (60-70% hook, 65-80% body, 40-50% product).
- [ ] Photo subject does not compete with text readability.

### Text
- [ ] All text is white with black stroke or shadow.
- [ ] Font sizes match hierarchy table.
- [ ] No slide has more than 2 text elements (label + body).
- [ ] Lines are manually broken at 3-6 words each.
- [ ] No colored text, highlights, underlines, or emoji.

### Consistency
- [ ] All slides in the post use the same overlay method.
- [ ] All slides use the same font and stroke style.
- [ ] Slide count is 5-7.

### Safety
- [ ] No copyrighted logos or brand marks (except MakeBrainrotVideos.com).
- [ ] No identifiable faces without rights.
- [ ] No fabricated earnings screenshots.

## Quality Gate Notes

- Ready for Workflow A3: render one non-hero sample slide using these rules.
- After user approval, mark this file as `Locked`.
- Design rules are candidates until quality gate passes.

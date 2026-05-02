# Design System: Athlete User Soccer

Status: `Pending quality gate`

This is the account source of truth for slide composition, typography, text
placement, and renderer-facing layout rules. Use `image.md` for photo subject
direction and visual treatment details.

## Canvas

- Output size: `1080x1920` PNG.
- Aspect ratio: `9:16`.
- Background: full-bleed selected photo on every slide.
- Safe margins: `140px` minimum on left and right.
- Slide count: variable — 4-6 slides per post depending on format. Lists of 3-4 items typically run 4-5 slides; identity/contrast posts run 4-6 slides. No fixed arc.

## Reference Photo Framing

- Placement: full canvas, behind all text.
- Size: fill the full `1080x1920` canvas.
- Crop behavior: center crop to 9:16; never stretch or distort.
- Alignment: keep the player, face, or key action readable after crop.
- Consistency rule: every slide uses the same full-bleed framing system.
- Do not: add inset frames, cards, logos, decorative borders, or ad-style product layouts.

## Typography

- Primary font: Arial Bold.
- Font file preference: `C:/Windows/Fonts/arialbd.ttf`.
- Body font: Arial Bold.
- Letter spacing: `0`.
- Text color: white `#FFFFFF`.
- Text outline: black stroke, `3px`.
- Text alignment: centered horizontally and vertically.
- Line spacing: `16px` between manual lines.

## Text Hierarchy

| Element | Font / weight | Size | Placement | Notes |
| --- | --- | --- | --- | --- |
| Hook / headline | Arial Bold | 44 pt | Centered on slide | First slide of the post. Shorter, punchier copy. |
| Body copy | Arial Bold | 36 pt | Centered on slide | List items, rules, contrasts. Use exact `flow.md` copy. |
| Emphasis word | Arial Bold | 36 pt | Centered on slide | One emphasized word per slide if needed — no bold or highlight needed, use copy positioning instead. |
| Final item / closing line | Arial Bold | 36 pt | Centered on slide | Last slide. Usually the final list item, not a separate moral. No explicit CTA. |
| Product copy | Arial Bold | 36 pt | Centered on slide | Same treatment as body slides. |

Note: The 44pt hook size is aspirational at setup stage. Renderers should test readability with 3px outline at 44pt against varied photo backgrounds before locking. Fall back to 36pt if readability drops.

## Slide Layouts

### Slide 1: Hook

- Photo: soccer context — training, stadium, game action, or player-focused shot. Should make the niche immediately clear.
- Text: centered hook. Short (1-3 lines). Identity promise, avoid-list opener, contrast, or invisible-competition line.
- No explanation on the hook slide. Just the tension.

### Slides 2-4 (or 2-5): List / Rules / Contrasts

- Photo: varied action or training photos. Each slide can use a different photo.
- Text: centered. One item per slide. For avoid-lists: the "avoid X" line then the replacement. For identity posts: one rule per slide. For contrasts: the wrong behavior then the right behavior.
- Line length: 2-4 lines maximum per slide.

### Last Slide: Final List Item / Close

- Photo: strong image that reinforces the overall message. Not necessarily different from interior slides.
- Text: centered. Prefer the strongest final list item. Avoid separate moral/conclusion slides unless the post specifically calls for one. No "save this" or "follow for more."
- For product posts: this is where the native mention lands, same visual treatment.

## Bold And Highlight Rules

- All visible text uses the same bold treatment.
- Do not bold individual words inside the slide copy.
- Do not add highlight colors, callout boxes, or underline treatments.
- The design gets emphasis from short copy, centered placement, and contrast with the photo.

## Renderer Rules

- Use exact text from `flow.md`.
- Preserve manual line breaks from `flow.md`.
- Normalize and crop the selected photo before adding text.
- Keep text centered on every slide.
- Keep the same font, outline, line spacing, and safe margins across all slides.
- Final PNGs must be exactly `1080x1920`.

## QA Checklist

- [ ] Every slide is `1080x1920`.
- [ ] Photo is full bleed and not stretched.
- [ ] Text is centered and inside the `140px` side margins.
- [ ] White text remains readable against the photo.
- [ ] Product slide does not look like a separate ad.
- [ ] Manual line breaks from `flow.md` are preserved.
- [ ] Hook slide uses 44pt (fallback to 36pt if readability fails).
- [ ] List-first posts end on a final item, not a separate moral/conclusion slide.

## Quality Gate Notes

- Latest approved sample: None (account setup stage)
- Current blocker: Baseline writing and design are drafted; first sample needed in Workflow A3
- Last revision notes: Derived from athlete-stories design system. Adaptations: variable slide count (4-6 vs fixed 7), 44pt hook size, no story arc structure. Updated to support list-first endings after user correction.

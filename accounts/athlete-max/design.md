# Design System: Athlete Max

Status: `Locked` (approved via quality gate attempt-006)

Use this file as the account-level source of truth for slideshow composition,
format, typography, text hierarchy, reference-photo framing, and renderer-facing
layout rules. Use `image.md` for photo subject direction and visual treatment.

## Canvas

- Output size: `1080x1350` PNG for the initial quality-gate carousel system.
- Aspect ratio: `4:5`, matching the primary design references in
  `references/social-accounts/verified_byhumans/`.
- Platform note: TikTok and Instagram are equal priorities. This A2 extraction
  starts with the reference-native `1080x1350` system. A `1080x1920` TikTok-safe
  adaptation can be added after the 4:5 baseline passes Workflow A3.
- Background: pure white `#FFFFFF`.
- Safe margins: `72px` left/right minimum, `80px` top minimum, `60px` bottom
  minimum. Body slides should target a `840px` text width.
- Slide count pattern: usually 5-7 slides: hero, 3-5 mechanism/fix body slides,
  and a close/source/product slide when needed.

## Reference Photo Framing

- Hero placement: right-side or full-height athlete portrait with open left-side
  space for the title.
- Hero size: photo may bleed to the top, right, and bottom edges. Keep the face or
  sport cue inside the right 40-50% of the canvas.
- Body slide placement: centered evidence photo/diagram frame between the upper
  explanation and lower fix/result section.
- Body slide frame size: default `760x430` to `820x460`; quality-gate renderer
  should use `800x450` unless a specific image requires a minor crop adjustment.
- Body slide frame position: centered at `x=140`, approximate `y=515` for the
  default `800x450` frame.
- Crop behavior: center crop into the frame. Never stretch or distort.
- Alignment: keep the key visual cue, athlete action, or scientific mechanism
  readable in 3 seconds.
- Consistency rule: keep the same body-frame size and position across every body
  slide in a post.
- Do not: use a body photo as the full background, add decorative borders, move
  the frame to solve copy overflow, or place text over body-frame imagery.

## Typography

- Primary font: Arial or Inter. Use Arial for local renderer reliability on
  Windows unless Inter is explicitly installed.
- Bold font: Arial Bold or Inter Black/Bold.
- Body font: Arial Regular or Inter Regular.
- Source / footer font: Arial Bold or Arial Regular, smaller and visually
  secondary.
- Font file preference: `C:/Windows/Fonts/arial.ttf` and
  `C:/Windows/Fonts/arialbd.ttf`.
- Letter spacing: `0` for body text; optional `-0.02em` equivalent for large hero
  titles if the renderer supports it.
- Text color: near-black `#111111` or black `#000000`.
- Source text color: dark gray `#333333` to `#444444`.
- Accent color: deep red `#B00000` to `#CC0000`; use sparingly.
- Text alignment: hero slides are left-aligned; body slides are center-aligned;
  source lines are center-aligned.

## Text Hierarchy

| Element | Font / weight | Size | Placement | Notes |
| --- | --- | --- | --- | --- |
| Hero title | Arial Bold / 900-style | 90-120 px | Left side, stacked natural phrases | One keyword or phrase may use red accent. |
| Hero subtitle | Arial Regular | 30-40 px | Under hero title | Parenthetical, short, secondary. |
| Body label | Arial Regular or Bold | 28-36 px | Top center | Examples: `what to avoid:`, `the biological roi (why it works):`. |
| Body title | Arial Bold | 48-64 px | Under label, center | Names the mistake, mechanism, or protocol. |
| Top explanation | Arial Regular with rare bold phrases | 28-34 px | Above photo frame | Problem + mechanism. Keep to 3-6 lines. |
| Reference photo / diagram | N/A | `800x450` | Centered at `x=140`, approx `y=515` | Same placement across body slides. |
| Lower fix/result section | Arial Regular with bold label | 28-34 px | Below photo frame | Starts with `the fix:` or `the result:`. |
| Source line | Arial Bold or Regular | 18-22 px | Bottom center | Journal/source line only; visually secondary. |

## Slide Layouts

### Hero Slide

- Text placement: left 50-60% of the canvas, with strong top-left alignment and
  generous whitespace.
- Photo placement: right 40-50% of the canvas, full-height bleed when possible.
- Line break behavior: stack natural phrases. Do not break every word onto a new
  line unless the title is intentionally poster-like.
- Accent / highlight rule: one word or short phrase may use red. Never use more
  than one accent phrase on a hero slide.
- Background: white or very light neutral. Avoid dark full-bleed hero slides for
  the baseline system.

### Body Slide

- Upper section: label, title, and short mechanism explanation.
- Reference photo frame: `800x450`, centered at `x=140`, approximate `y=515`.
- Lower section: begins with a bold label (`the fix:`, `the result:`, `the cue:`)
  followed by the actionable or explanatory payoff.
- Source line: optional but required for strong biological or causal claims;
  bottom centered and separated from lower text by at least `32px`.
- Overflow rule: shorten copy or revise manual line breaks in `flow.md`; do not
  shrink text below hierarchy minimums or move the photo frame.

### Close / Product Slide

- Layout: use the same body-slide structure unless the slide is a clean source or
  protocol card.
- Product or brand treatment: camouflaged and native. No logo-forward ads, CTA
  buttons, pricing, app-store language, or sales framing.
- Text placement: centered, with the same hierarchy and margins as body slides.
- Product mention style: treat w(inner) as a tool, protocol companion, or source
  extension only after the science-backed problem has been established.

## Bold And Highlight Rules

- Bold is reserved for: hierarchy labels, biological mechanisms, actionable
  verbs, key numeric thresholds, and the one phrase the reader should remember.
- Highlight color is reserved for: hero-title emphasis only until Workflow A3
  approves body-slide red accents.
- Avoid bolding: entire sentences, generic drama words, filler phrases, or more
  than one unrelated concept in a paragraph.
- Maximum emphasis per slide: one red phrase total and 3-5 bold terms total.

## Renderer Rules

- Use exact text from `flow.md`.
- Preserve manual line breaks where the flow marks them as intentional.
- Body slides may wrap paragraphs to fit fixed text areas, but the renderer must
  not rewrite copy.
- Before rendering, measure each text block's line widths. If any line in a
  block fills less than 80% of the longest line, reject the copy back to
  `flow.md` for rewriting. Do not fix line fill by changing font size, column
  width, or layout.
- **Line-fill consistency:** every text block on a slide must form a visual
  rectangle, not a diamond or ragged triangle. Each line within a paragraph
  should fill 85-95% of the text column width. Short trailing lines (orphans)
  and noticeably shorter interior lines break the dense, substantive rhythm of
  the reference accounts. If a paragraph wraps to create uneven lines, the copy
  must be reworded in `flow.md` to fill evenly — do not pad with filler words
  and do not adjust font size or layout to compensate. This is a writing
  constraint enforced at render time: the renderer checks line widths and
  rejects blocks where any line falls below 80% of the longest line in the
  same block.
- Keep body-slide reference photo frame fixed at `800x450`, centered at `x=140`,
  approximate `y=515`.
- Do not move the reference photo frame to solve copy overflow; shorten copy or
  adjust line breaks in `flow.md`.
- Desaturate hero images to B&W and boost contrast before compositing.
- Body images should be neutral, desaturated, or B&W unless color is necessary to
  understand the mechanism.
- Final PNGs must be exactly `1080x1350` for this baseline system.

## QA Checklist

- [ ] Canvas is exactly `1080x1350`.
- [ ] Background is white or very light neutral.
- [ ] Body slide photo frame is `800x450`, centered, and consistent across slides.
- [ ] Text stays inside safe margins.
- [ ] Upper text does not overlap the photo frame.
- [ ] Lower fix/result section does not overlap the source line.
- [ ] Every text block forms a visual rectangle — no orphan lines, no line
  falls below 80% of the longest line in the same block.
- [ ] Bold/highlight choices match hierarchy rules.
- [ ] Source lines appear on slides with strong biological or causal claims.
- [ ] Product slides follow the same account design system and do not look like ads.

## Quality Gate Notes

- Latest approved sample: attempt-007-2026-04-29-soccer-centreback-runner (non-hero body slide). Approved 2026-04-29.
- Current blocker: None. Baseline body-slide design system is approved and locked.
- Next step: Hero-slide format and 1080x1920 TikTok-safe adaptation can be tested now.
- Last revision notes: Initial A2 extraction completed from verified_byhumans
  design/image references and chasingpeaks0 contrast references on 2026-04-28.
  Attempt 007 confirmed the Post 1 listing format (label + title + explanation + photo + fix + source) scales to taller copy blocks with recalculated spacing.

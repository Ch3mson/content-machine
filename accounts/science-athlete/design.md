# Design System: Science Athlete

This is the account source of truth for slide composition, typography, text
placement, reference-photo framing, and renderer-facing layout rules. Use
`image.md` for photo subject direction and visual treatment details.

## Canvas

- Output size: `1080x1350` PNG.
- Aspect ratio: `4:5`, matching `references/social-accounts/verified_byhumans/`.
- Background: white `#FFFFFF` or a very light neutral.
- Safe margins: `90px` minimum for hero slides, `120px` minimum for body slides.
- Body content width: target `840px`.
- Slide count pattern: usually 6 slides, with a hero, body slides, and a close.

## Reference Photo Framing

- Body slide placement: centered fixed 16:9 frame.
- Body slide frame size: `800x450`.
- Body slide frame position: `x=140`, `y=500`.
- Crop behavior: center crop the selected reference photo into the frame; never
  stretch or distort.
- Alignment: keep the key visual cue readable inside the frame.
- Consistency rule: keep the same frame size and position across every body
  slide in the post.
- Do not: move the photo frame up or down to solve copy overflow, use decorative
  frames, or place the photo as a background on body slides.

## Typography

- Primary font: Arial.
- Bold font: Arial Bold.
- Font file preference: `C:/Windows/Fonts/arial.ttf` and
  `C:/Windows/Fonts/arialbd.ttf`.
- Letter spacing: `0`.
- Text color: black `#000000`.
- Source text color: dark gray `#444444`.
- Text alignment: centered on body slides.

## Text Hierarchy

| Element | Font / weight | Size | Placement | Notes |
| --- | --- | --- | --- | --- |
| Hero title | Arial Bold | 90-120 px | Left aligned or centered depending on photo crop | Stack natural phrases, not single words. |
| Hero subtitle | Arial Regular | 34-42 px | Under hero title | Keep short and parenthetical when needed. |
| Body header | Arial Bold | 40-44 px | Top center | Example: `what to avoid:`. |
| Body title | Arial Bold | 54-64 px | Under header | Names the mistake, read, or slide concept. |
| Top explanation | Arial Regular with rare bold phrases | 30-36 px | Above photo frame | Felt problem plus mechanism. |
| Lower actionable section | Arial Regular with a bold label (e.g., `the fix:`) | 30-36 px | Below photo frame | Actionable takeaway (practical correction, cue, or read) plus why it works. |
| Source line | Arial Bold or Regular | 20-24 px | Bottom center | Short, secondary, and inside safe margin. |

## Slide Layouts

### Hero Slide

- Photo placement: full-height or side-weighted athlete image with clean open
  space for type.
- Text placement: large stacked title in the open space.
- Line break behavior: stack natural phrases.
- Accent rule: one optional accent word or phrase may use a single account
  accent color. Do not use multiple accent colors.
- Avoid: breaking every word onto its own line.

### Body Slide

- Upper section: header, title, and top explanation.
- Reference photo frame: `800x450`, centered at `x=140`, `y=500`.
- Lower section: starts with a bold actionable label (e.g., `the fix:`, `the cue:`, `the read:`) followed by the practical takeaway in the same paragraph.
- Source line: optional, bottom centered, visually secondary.
- Overflow rule: shorten copy or revise manual line breaks in `flow.md`; do not
  move the photo frame.

### Close / Product Slide

- Layout: use the same body-slide structure unless the slide is a statement
  card.
- Product treatment: native text bridge only after the physical or mental fix
  has been established.
- Text placement: centered, using the same hierarchy and safe margins as body
  slides.
- Do not: turn the slide into an ad, add product logos as decoration, or make the
  product the whole solution.

## Bold And Highlight Rules

- Bold is reserved for hierarchy: header, title, actionable labels (e.g., `the fix:`), source label, and
  at most one key mechanism or correction phrase inside a paragraph.
- Good inline bold choices: the exact hidden problem, the key science term, the
  correction cue, or the phrase the reader should remember.
- Avoid bolding generic drama words, whole sentences, or multiple unrelated
  phrases.
- Maximum inline emphasis: one phrase in the top explanation and one phrase in
  the lower actionable section.

## Renderer Rules

- Use exact text from `flow.md`.
- Preserve intentional line breaks on hero slides.
- Body slides may wrap paragraphs to fit the fixed text areas, but must not
  rewrite copy inside the renderer.
- Keep the reference-photo frame fixed at `800x450`, `x=140`, `y=500`.
- Keep source lines short enough to sit below the lower section without overlap.
- Final PNGs must be exactly `1080x1350`.

## QA Checklist

- [ ] Every slide is `1080x1350`.
- [ ] Body slide photo frame is `800x450` at `x=140`, `y=500`.
- [ ] Upper text does not overlap the photo frame.
- [ ] Lower actionable section (e.g., `the fix:`) does not overlap the source line.
- [ ] Body text is centered and readable.
- [ ] Bold choices match hierarchy and do not create random emphasis.
- [ ] Product slides follow the same carousel system and do not look like ads.

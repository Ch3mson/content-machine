# Design Analysis: Athlete Max

Use this file for lower-authority visual observations from reference posts. The
canonical layout rules live in `../design.md`; photo direction lives in
`../image.md`.

## Sources Reviewed

| Reference | Location | Role | Notes |
| --- | --- | --- | --- |
| verified_byhumans Post 1 | `references/social-accounts/verified_byhumans/post 1/` | Primary design + image reference | Clean white background, large black type, one red accent, centered body sections, source citation footer. |
| verified_byhumans Post 2 | `references/social-accounts/verified_byhumans/Post 2/` | Primary design + image reference | B&W athlete hero image, high-whitespace body slides, image as central evidence, repeated label/result/source pattern. |
| chasingpeaks0 Post 1 | `references/social-accounts/chasingpeaks0/Post 1/` | Contrast reference | Dark full-bleed images, dense overlaid text, emoji arrows. Useful for writing energy, not baseline visual system. |
| chasingpeaks0 Post 2 | `references/social-accounts/chasingpeaks0/Post 2/` | Contrast reference | Dark/cinematic optimization aesthetic with grid text. Strong attention, lower clinical polish. |

## Extracted Visual Principles

### 1. White space creates authority

verified_byhumans uses plain white backgrounds and generous margins. The slides
feel clinical because nothing competes with the text hierarchy. athlete-max
should keep this restraint instead of chasing dark, high-noise meme aesthetics.

### 2. Typography carries the hierarchy

The reference system does not rely on boxes, shadows, borders, or decorative
icons. Size, weight, alignment, and scarce red color create the entire hierarchy.

### 3. Red works because it is rare

Red appears as a single emphasis color on hero slides or key title words. If red
appears throughout body copy, it loses authority and starts to feel like an ad or
alarm graphic.

### 4. Photos act as evidence, not decoration

Hero photos establish identity and seriousness. Body photos or illustrations sit
between explanation and result/fix, functioning as a visual proof point or cue.

### 5. Body slides need repeatable geometry

The strongest reference slides repeat the same upper text → image → lower text →
source structure. athlete-max should preserve this fixed geometry for renderer
consistency and faster production.

## Reference-Specific Notes

### verified_byhumans Post 1

- Strongest pattern: `what to avoid:` label, large mistake title, explanation,
  centered image, `the fix:` section, source line.
- Visual tone: clinical, sparse, almost like a designed research handout.
- Risk if copied too closely: lowercase-only styling may feel like direct mimicry;
  keep as a candidate, not a locked rule.

### verified_byhumans Post 2

- Strongest pattern: B&W hero portrait with bold left-side title and red accent.
- Body slides create trust by repeating `the biological roi (why it works):`,
  image, `the result:`, and scientific source.
- Risk: some slides rely on broad evolutionary claims; athlete-max should tighten
  image/source support for sports-science claims.

### chasingpeaks0 Contrast

- Strongest reusable element: attention-grabbing density and high-contrast
  emphasis.
- What to avoid visually: dark full-bleed backgrounds as the default, white text
  with heavy stroke, emoji bullets, and overcrowded copy blocks.

## Open Design Decisions For A3

- Test whether lowercase headings feel native or too derivative.
- Test whether the red accent should be `#B00000` or `#CC0000`.
- Test whether `1080x1350` is sufficient for TikTok photo posts or whether a
  `1080x1920` adaptation should become the default after baseline approval.
- Test if body images should always be `800x450` landscape or if square images
  can be cropped into the same frame without weakening consistency.

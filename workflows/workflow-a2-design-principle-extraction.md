# Workflow A2: Design Principle Extraction

Use this when the user says `workflow a2`, `design extraction`, `design
principles`, or when Workflow A reaches visual-system extraction.

Goal: create the account design system while keeping photo direction and image
sourcing separate.

## Read First

1. `../AGENTS.md`
2. `workflow-a-new-account.md`
3. `workflow-a0-account-intake-reference-map.md`
4. `../accounts/{account}/account-brief.md`
5. `../accounts/{account}/extractions/reference-map.md`
6. `../references/templates/account-design.md`
7. Design-relevant references named in `reference-map.md`
8. Existing `../accounts/{account}/design.md` and `../accounts/{account}/image.md`, if present

## Procedure

1. Confirm design material is sufficient.
   - Use references marked `design` or `image` in `reference-map.md`.
   - Stop and ask for screenshots or image examples if layout, typography, and
     framing cannot be extracted.

2. Extract visual principles.
   - Canvas size and aspect ratio.
   - Safe margins and content width.
   - Typography, font weights, sizes, line spacing, and alignment.
   - Text hierarchy and emphasis rules.
   - Image or placeholder frame size, crop, placement, and consistency rules.
   - Slide layout variants.
   - Renderer-facing rules and visual QA.

3. Write `design.md`.
   - Use `../references/templates/account-design.md`.
   - Make it the canonical layout source of truth.
   - Include status: `Pending quality gate`.
   - Do not include sourcing queries, image-generation prompts, or strategy notes.

4. Write or update `image.md`.
   - Keep photo subject direction, visual treatment, selected-photo suitability,
     and image prompt direction here.
   - Do not make `image.md` the authority for layout, typography, or frame
     placement.

5. Stop for Workflow A3.
   - Do not mark `design.md` locked until the writing/design quality gate
     renders an approved non-hero sample slide.

## Outputs

- `accounts/{account}/design.md`
- `accounts/{account}/image.md`
- Optional `accounts/{account}/extractions/design-analysis.md` when detailed
  reference notes are useful.

## Agent Rules

- Separate design rules from image direction.
- Preserve exact measured layout rules when references show them.
- If geometry is uncertain, state the uncertainty instead of inventing exact
  pixel values.
- Keep renderer rules concrete enough for Workflow C or a quality-gate renderer.

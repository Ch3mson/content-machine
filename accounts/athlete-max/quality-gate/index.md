# Quality Gate Attempt Index

Use this file as the attempt ledger for athlete-max Workflow A3 runs. New
user-reviewable quality-gate samples must live under
`attempts/{attempt-id}/`. Root-level artifacts in this folder are legacy
artifacts from before attempt folders were required.

## Attempt Naming

Format: `attempt-###-YYYY-MM-DD-{short-topic-slug}`

- Increment `###` from existing folders in `attempts/`.
- Create one folder per user-reviewable sample.
- Keep pre-review fit fixes inside the same attempt as render notes.
- Create a new attempt folder after user feedback if another sample is rendered
  for review.

## Attempts

| Attempt | Date | Topic | Slide Type | Status | Review Decision | Blocking Persona Failures | Design Findings | Path |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| attempt-001-2026-04-28-soccer-first-touch | 2026-04-28 | First touch fading in final 20 minutes | Non-hero body slide | Rendered | Rejected | None after rewrites | Body-slide vertical budget is tight at upper typography ranges; line word-count inconsistent (3-8 word lines mixed with longer lines) | `accounts/athlete-max/quality-gate/attempts/attempt-001-2026-04-28-soccer-first-touch/` |
| attempt-002-2026-04-29-soccer-first-touch | 2026-04-29 | First touch fading in final 20 minutes | Non-hero body slide | Rendered | Rejected | None | All lines meet 9-word minimum; frame position unchanged; but copy still uses "tired legs," vague "dialing precision down," separate fix/payoff sections, and team drill | `accounts/athlete-max/quality-gate/attempts/attempt-002-2026-04-29-soccer-first-touch/` |
| attempt-003-2026-04-29-soccer-first-touch | 2026-04-29 | First touch fading in final 20 minutes | Non-hero body slide | Rendered | Rejected | None after TAP-R rewrites | Horizontal overflow: title at 48px exceeded canvas width; top explanation at 30px/7 lines overlapped photo frame; lower section combined segment was 1372px wide; insufficient vertical buffers | `accounts/athlete-max/quality-gate/attempts/attempt-003-2026-04-29-soccer-first-touch/` |
| attempt-004-2026-04-29-soccer-first-touch | 2026-04-29 | First touch fading in final 20 minutes | Non-hero body slide | Rendered | Rejected | None after layout fixes | User requested title-as-label structure per verified_byhumans Post 5; separate small label + long contrarian title should be replaced with topic name as large bold title, hook embedded in explanation | `accounts/athlete-max/quality-gate/attempts/attempt-004-2026-04-29-soccer-first-touch/` |
| attempt-005-2026-04-29-soccer-first-touch | 2026-04-29 | First touch fading in final 20 minutes | Non-hero body slide | Rendered | Rejected | None after structural redesign | User requested Post 1 listing format with label + short title; photo should be more centered; needs "what to avoid:" label | `accounts/athlete-max/quality-gate/attempts/attempt-005-2026-04-29-soccer-first-touch/` |
| attempt-006-2026-04-29-soccer-first-touch | 2026-04-29 | First touch fading in final 20 minutes | Non-hero body slide | Rendered | **Approved** | None after Post 1 format redesign + pre-review fit fixes | Label "what to avoid:" at 30px regular; title "losing your late-game touch" at 56px bold (grammatically congruent); contrarian hook embedded in explanation; photo centered at y=444 with equal 80px spacing above and below; bold limited to structural labels (the fix:, constraint:); matches verified_byhumans Post 1 listing format | `accounts/athlete-max/quality-gate/attempts/attempt-006-2026-04-29-soccer-first-touch/` |
| attempt-007-2026-04-29-soccer-centreback-runner | 2026-04-29 | Centreback missing runners in behind in final 15 minutes | Non-hero body slide | Rendered | **Approved** | None | Label "what to avoid:" at 30px regular; title "runners getting in behind you" at 56px bold; contrarian hook embedded; 6-line upper explanation + 6-line lower fix; frame at y=486 with 65px gaps; source at 1270 with 60px bottom margin; all body lines ≥10 words; matches verified_byhumans Post 1 listing format | `accounts/athlete-max/quality-gate/attempts/attempt-007-2026-04-29-soccer-centreback-runner/` |

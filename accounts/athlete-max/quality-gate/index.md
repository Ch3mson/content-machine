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
| legacy-root-2026-04-28-soccer-first-touch | 2026-04-28 | First touch fading in final 20 minutes | Non-hero body slide | Rendered | Pending user review | None after rewrites | Body-slide vertical budget is tight at upper typography ranges | `accounts/athlete-max/quality-gate/` |

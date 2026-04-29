# Workflow A: New Account Orchestrator

Use this when the user says `workflow a`, `workflow-a`, `new account`, or asks to
create/onboard an account playbook.

Goal: create account-level source-of-truth files through small, reviewable
workflows. Do not try to extract strategy, write final docs, validate quality,
and create presets in one pass.

## Read First

1. `../AGENTS.md`
2. This file
3. The next workflow in the sequence:
   - `workflow-a0-account-intake-reference-map.md`
   - `workflow-a1-writing-principle-extraction.md`
   - `workflow-a2-design-principle-extraction.md`
   - `workflow-a3-writing-design-quality-gate.md`
   - `workflow-a4-angle-extraction-to-presets.md`, only after baseline quality passes
4. Product files only when the account or copy mentions w(inner), the app, or a
   product claim:
   - `../product/app-brief.md`
   - `../product/claim-bank.md`
5. Existing `../accounts/{account}/` files, if present.

## Workflow Sequence

Run these in order unless the user explicitly asks for only one stage.

| Stage | File | Purpose | Stop Point |
| --- | --- | --- | --- |
| A0 | `workflow-a0-account-intake-reference-map.md` | Define the account and organize inspiration/reference inputs. | Stop if account basics or reference material are missing. |
| A1 | `workflow-a1-writing-principle-extraction.md` | Extract baseline writing principles and create the indexed writing folder. | Stop with `writing.md` marked `Pending quality gate`. |
| A2 | `workflow-a2-design-principle-extraction.md` | Extract visual/layout rules and separate image direction from design rules. | Stop with `design.md` marked `Pending quality gate`. |
| A3 | `workflow-a3-writing-design-quality-gate.md` | Test writing and design by rendering one non-hero sample slide. | Repeat until the user approves the sample. |
| A4 | `workflow-a4-angle-extraction-to-presets.md` | Extract repeatable angle patterns into presets. | Optional; run only after baseline docs are locked. |

## Account Outputs

Baseline account files:

- `accounts/{account}/account-brief.md`
- `accounts/{account}/extractions/reference-map.md`
- `accounts/{account}/writing.md`
- `accounts/{account}/writing/principles.md`
- `accounts/{account}/writing/refinement-personas.md`
- `accounts/{account}/writing/pattern-extractions.md`
- `accounts/{account}/writing/copywriting-principles.md`
- `accounts/{account}/writing/banned-patterns.md`
- `accounts/{account}/writing/sample-posts.md`
- `accounts/{account}/writing/qa.md`
- `accounts/{account}/design.md`
- `accounts/{account}/image.md`
- `accounts/{account}/sources.md`
- `accounts/{account}/quality-gate/index.md`, after Workflow A3
- `accounts/{account}/quality-gate/attempts/{attempt-id}/`, after each
  Workflow A3 attempt

Supplemental files:

- `accounts/{account}/presets.md`, only after Workflow A4 validates repeatable
  angle or flow patterns.

## Required Inputs

Collect or explicitly mark missing:

- Account niche and audience.
- Platform priority.
- Primary goal: saves, shares, follows, comments, product awareness, or another goal.
- Competitor or inspiration slideshow references.
- Design references for layout, typography, spacing, image placement, and visual hierarchy.
- Copy examples, transcripts, screenshots, or tone notes.
- Product relationship to w(inner).
- Research sensitivity and claim-risk topics.

Ask in short rounds. Do not ask for every missing item at once.

## Locking Rules

- `writing.md` and `design.md` start as `Draft` or `Pending quality gate`.
- Do not mark either file `Locked` until Workflow A3 produces an approved
  non-hero rendered sample slide.
- If the user returns from an isolated quality-gate session with revision notes,
  update the relevant source-of-truth docs before running or accepting another
  quality-gate sample.
- If the user rejects a quality-gate sample, update
  `writing/refinement-personas.md` with the calibrated criticism before the
  next sample attempt.
- Every new user-reviewable quality-gate sample must be saved as a new attempt
  folder under `quality-gate/attempts/`; never overwrite a prior attempt folder.
- Treat the user's feedback as higher priority than the initial extraction.
- If the user also tagged Workflow B, continue to Workflow B only after the
  required account docs exist and the baseline writing/design gate is approved.

## Agent Rules

- Do not invent final account rules when user input is missing.
- Use placeholders only when a file must exist before inputs are ready.
- Copy competitor structure and principles only, not wording, identity, or assets.
- Keep product claims inside approved claim-bank boundaries.
- Use fewer, better questions.
- Prefer iterative workflows over one large account setup pass.

---
name: account-quality-gate
description: Test draft account writing and design source-of-truth files by generating a representative non-hero slideshow sample. Use when validating new account writing.md/design.md, checking whether extracted competitor principles produce usable output, or running Workflow A3.
---

# Account Quality Gate

## Goal

Validate draft `writing.md` and `design.md` by producing one representative
non-hero rendered sample slide. The sample tests copy tone, information flow,
typography, spacing, placeholder or image-frame behavior, and renderer-facing
layout rules before the account docs are locked.

## Read First

Use the smallest relevant set:

1. `AGENTS.md`
2. `workflows/workflow-a3-writing-design-quality-gate.md`
3. `accounts/{account}/account-brief.md`
4. `accounts/{account}/writing.md`
5. Only indexed writing subfiles required by `writing.md`
6. `accounts/{account}/writing/refinement-personas.md`
7. `accounts/{account}/design.md`
8. `accounts/{account}/image.md`, only for placeholder or visual treatment
9. `accounts/{account}/sources.md`, only if the sample uses claims
10. `references/skills/stop-slop/SKILL.md`
11. Product files only if the sample mentions w(inner)

## Contracts

- Generate a non-hero sample. Do not use a hero slide.
- Use `writing.md` as the highest-authority writing source.
- Use `design.md` as the highest-authority layout source.
- Use `image.md` only for photo suitability, visual treatment, or placeholder
  direction.
- Do not source images unless the user explicitly asks. Use a placeholder frame
  when no image is available.
- Do not edit `writing.md` or `design.md` by default. Record feedback so the
  main account session can revise the source docs.
- Save each user-reviewable quality-gate sample in its own attempt folder under
  `accounts/{account}/quality-gate/attempts/`; never overwrite a prior attempt.
- Keep `accounts/{account}/quality-gate/index.md` as the attempt ledger.
- Run the draft sample through the three account refinement personas before
  rendering.
- If the Athlete Skeptic flags sport terminology, verify only the flagged terms.
  Use teammate/coach plausibility first, then external research when needed.
  Terms that are not clearly `Native` or `Acceptable` must be rewritten in
  plain, observable athlete language.
- If `design.md` lacks enough geometry to render, stop and report the missing
  design rules instead of inventing them.

## Procedure

1. Summarize what will be tested.
   - Writing voice and rhythm.
   - Information structure.
   - Typography and hierarchy.
   - Frame spacing and safe margins.
   - Any uncertainty that could affect the render.

2. Ask before generating.
   - Ask the user whether to proceed with one non-hero sample slide.
   - Keep the summary short enough for fast approval.

3. Create a sample brief.
   - Choose a body, list, explanation, or middle slide.
   - Avoid hero slides and closing slides.
   - Use an account-native topic, but keep claims low-risk unless sources are
     already available.

4. Draft the sample copy.
   - Follow `writing.md` and required subfiles.
   - Apply `writing/refinement-personas.md`.
   - Prepare Bored Athlete, Account-Native Scroller, and Athlete Skeptic
     critique before rendering.
   - Preserve the account's intended rhythm.
   - Do not use a preset unless the baseline docs already say it is validated.

5. Create the attempt workspace.
   - Create `accounts/{account}/quality-gate/` if needed.
   - Create `accounts/{account}/quality-gate/attempts/` if needed.
   - Create or update `accounts/{account}/quality-gate/index.md`.
   - Create a new folder named
     `attempt-###-YYYY-MM-DD-{short-topic-slug}`, using the next available
     number from existing attempt folders.
   - If root-level legacy artifacts exist in `quality-gate/`, leave them in
     place and add a legacy note to `index.md`.

6. Render the PNG.
   - Save all files inside the attempt folder:
     - `attempt-summary.md`
     - `sample-brief.md`
     - `sample-copy.md`
     - `render_sample.py`
     - `sample-slide.png`
     - `iteration-notes.md`
   - Record Bored Athlete, Account-Native Scroller, and Athlete Skeptic
     critique in `iteration-notes.md`.
   - If pre-review fit fixes require multiple renders, keep them in this same
     attempt folder and document the changes in `iteration-notes.md`.
   - Use Python/Pillow when a renderer is needed.
   - Keep placeholder image spacing faithful to `design.md`.

7. Update the attempt ledger.
   - Add or update one row in `quality-gate/index.md` for the attempt.
   - Track attempt id, date, topic, slide type, status, review decision,
     blocking persona failures, design findings, and path to the attempt folder.

8. Review with the user.
   - Show or link the PNG.
   - Ask whether the sample proves the docs are strong enough.
   - If approved, record approval in `iteration-notes.md`.
   - If revisions are requested, record exact feedback and which source file
     likely needs revision.
   - Classify rejected-sample criticism under the matching persona or design
     feedback.
   - Update `writing/refinement-personas.md` before the next sample attempt.
   - Promote rejection feedback to `writing.md`, `writing/principles.md`,
     `writing/qa.md`, or `design.md` only when it is explicit, repeated, or
     changes durable account rules.
   - If another user-reviewable sample is generated after feedback, create a new
     attempt folder. Pre-review fit fixes may stay inside the same attempt as
     render notes.

## Approval Criteria

- The slide looks like it came from the target account.
- The copy follows the account's voice without sounding templated.
- The draft passed all blocking checks in the three-persona protocol.
- The layout follows `design.md` without manual hacks.
- The placeholder or image frame has the right spacing and visual priority.
- The sample exposes enough of the system to trust future body slides.

## Failure Modes

- Copy fits only because the renderer silently rewrote it.
- A new attempt overwrites an older sample instead of creating a new attempt
  folder.
- `quality-gate/index.md` does not record the attempt status and review
  decision.
- The sample uses a hero slide and avoids testing repeatable body structure.
- The design file lacks exact canvas, typography, spacing, or frame rules.
- The writing folder contains broad advice but no actionable voice rules.
- The three personas contain generic advice instead of account-specific pass
  criteria, blocking failures, and rewrite actions.
- The product mention feels like an ad or uses unapproved claims.

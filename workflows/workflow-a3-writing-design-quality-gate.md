# Workflow A3: Writing And Design Quality Gate

Use this when the user says `workflow a3`, `quality gate`, `test writing/design`,
or when Workflow A has draft `writing.md` and `design.md`.

Goal: verify that the draft writing and design source-of-truth files can produce
a strong representative non-hero slide before they are locked.

## Read First

1. `../AGENTS.md`
2. `workflow-a-new-account.md`
3. `../references/skills/account-quality-gate/SKILL.md`
4. `../accounts/{account}/account-brief.md`
5. `../accounts/{account}/writing.md`
6. Only the indexed writing subfiles required by `writing.md`
7. `../accounts/{account}/writing/refinement-personas.md`
8. `../accounts/{account}/design.md`
9. `../accounts/{account}/image.md`, only for placeholder or photo treatment
10. `../accounts/{account}/sources.md`, only if factual or product claims appear

## Procedure

1. Run the gate from an isolated session when possible.
   - The isolated session should use `account-quality-gate` and the account
     files, not the full prior chat.
   - The main account-building session should wait for the user to return with
     approval or revision notes.

2. Summarize the extraction.
   - Give a short summary of the writing principles and design rules being
     tested.
   - Ask before generating the sample slide.

3. Generate one non-hero sample slide.
   - Use a body slide, list slide, middle slide, or explanation slide.
   - Do not use a hero slide, because hero slides can hide weak repeatability.
   - Use the draft `writing.md` and `design.md` exactly as source of truth.
   - Use a placeholder image frame if no real image is available.
   - Before rendering, run the draft through all three personas in
     `writing/refinement-personas.md`.
   - Save the three-persona critique in `quality-gate/iteration-notes.md`.
   - If the Athlete Skeptic flags sport terminology, verify only the flagged
     terms. Use teammate/coach plausibility first, then external research if
     needed. If a term is not clearly `Native` or `Acceptable`, rewrite it into
     plain, observable athlete language before rendering.

4. Save artifacts in `accounts/{account}/quality-gate/`.
   - `sample-brief.md`
   - `sample-copy.md`
   - `render_sample.py`
   - `sample-slide.png`
   - `iteration-notes.md`

5. User reviews the rendered PNG.
   - If approved, mark the latest sample in `iteration-notes.md`.
   - If revisions are requested, update `iteration-notes.md` with exact feedback.
   - Classify the rejection under The Bored Athlete, The Account-Native
     Scroller, The Athlete Skeptic, or design feedback.
   - Update `writing/refinement-personas.md` with the calibrated criticism
     before the next sample attempt.
   - Update `writing/sample-posts.md` only if the rejected sample is useful as a
     cautionary example.
   - Update `writing/qa.md`, `writing.md`, writing subfiles, or `design.md`
     only when the feedback changes durable approval criteria, account voice, or
     design rules.
   - Do not promote one-off rejection feedback into a locked rule unless the
     user states it as durable or it repeats across samples.

6. Lock only after approval.
   - Change `writing.md` status to `Locked`.
   - Change `design.md` status to `Locked`.
   - Link the approved sample in both files when practical.

## Outputs

- Approved non-hero sample PNG.
- Quality-gate notes.
- Locked `writing.md` and `design.md` after approval.

## Agent Rules

- Do not skip the rendered sample.
- Do not use `image.md` as a substitute for layout rules.
- Do not edit slide copy inside the renderer to make the sample fit.
- If the sample fails because docs are underspecified, revise the docs before
  rendering again.

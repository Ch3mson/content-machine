# Workflow A4: Angle Extraction To Presets

Use this when the user says `workflow a4`, `angle extraction`, `preset
extraction`, or asks to extract repeatable post angles from stored posts.

Goal: turn validated angle and flow patterns into `presets.md` only after the
baseline account writing and design system have passed the quality gate.

## Read First

1. `../AGENTS.md`
2. `workflow-a-new-account.md`
3. `workflow-a3-writing-design-quality-gate.md`
4. `../references/skills/angle-extraction/SKILL.md`
5. `../references/skills/angle-variants/SKILL.md`
6. `../accounts/{account}/account-brief.md`
7. `../accounts/{account}/writing.md`
8. Only the indexed writing subfiles required by `writing.md`
9. `../accounts/{account}/design.md`
10. `../accounts/{account}/quality-gate/iteration-notes.md`, if present
11. Stored post sets or inspiration references named by the user

## Preconditions

- `writing.md` status is `Locked`.
- `design.md` status is `Locked`.
- At least one non-hero sample slide has passed Workflow A3.

If any precondition is missing, run or repeat Workflow A3 first.

## Procedure

1. Inventory the stored post set.
   - List every inspiration post, account post, screenshot sequence, transcript,
     or note being analyzed.
   - Record the viewer problem, hook, swipe reason, emotional lever, credibility
     method, slide sequence, close, and visual role.

2. Extract angle candidates.
   - Start from why the viewer cares, not the technical mechanism.
   - Identify the core desire, private gap, tension, curiosity driver, and fix
     direction.
   - Use `angle-variants` principles to ensure candidates are meaningfully
     different.

3. Test candidates against the locked baseline.
   - Apply the candidate angle to the existing `writing.md` voice.
   - Check that the flow can fit `design.md` without layout hacks.
   - Reject candidates that require a different voice or a different visual
     system unless the user explicitly wants a new account direction.

4. Run a copy plus render pass.
   - Create a non-hero test slide or short sample through Workflow A3.
   - Save angle-specific quality-gate notes under `quality-gate/`.
   - Do not add to `presets.md` before user approval.

5. Update `presets.md` after approval.
   - Add the preset as a supplemental pattern.
   - Include use case, hook behavior, flow structure, copy rhythm, product fit,
     examples, and risks.
   - Link to the approved quality-gate sample or notes.

## Outputs

- `accounts/{account}/extractions/angle-analysis.md`
- Optional `accounts/{account}/quality-gate/angle-*` sample artifacts
- Validated `accounts/{account}/presets.md` additions

## Agent Rules

- Do not make presets the source of baseline voice.
- Do not promote a pattern because it appears often; promote it only when it
  survives writing/design validation.
- Do not copy competitor hooks or exact wording.
- Treat `presets.md` as a supplement to `writing.md`.

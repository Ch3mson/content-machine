---
name: angle-extraction
description: Extract repeatable slideshow angle and flow patterns from stored competitor, inspiration, or approved account posts. Use when analyzing why posts work from the viewer's perspective, creating angle candidates, or validating additions to presets.md after writing.md/design.md pass the quality gate.
---

# Angle Extraction

## Goal

Analyze stored post sets to find repeatable angle patterns that can become
supplemental `presets.md` entries. Baseline account voice comes first; presets
are added only after the account's `writing.md` and `design.md` have passed the
quality gate.

## Read First

Use the smallest relevant set:

1. `AGENTS.md`
2. `workflows/workflow-a4-angle-extraction-to-presets.md`
3. `references/skills/angle-variants/SKILL.md`
4. `references/skills/account-quality-gate/SKILL.md`, when rendering a test
5. `accounts/{account}/account-brief.md`
6. `accounts/{account}/writing.md`
7. Only indexed writing subfiles required by `writing.md`
8. `accounts/{account}/design.md`
9. `accounts/{account}/quality-gate/iteration-notes.md`, if present
10. Stored post folders, screenshots, transcripts, or notes being analyzed
11. Product files only if the angle includes w(inner)

## Preconditions

- `writing.md` status is `Locked`.
- `design.md` status is `Locked`.
- The account has at least one approved non-hero quality-gate sample.

If these are missing, run Workflow A3 first.

## Analysis Lens

Start from the viewer, not the mechanism.

For each post, extract:

- Why the viewer stops.
- What private gap, desire, fear, or frustration the post names.
- Why the viewer keeps swiping.
- How the post earns trust.
- What emotional lever drives the angle.
- What mechanism explains the pain.
- What fix direction the post implies.
- How the flow creates momentum.
- What visual structure supports the angle.

## Procedure

1. Inventory the post set.
   - Create or update `accounts/{account}/extractions/angle-analysis.md`.
   - List each reference, location, post topic, viewer promise, and status.

2. Extract candidate angle patterns.
   - Use `angle-variants` to ensure candidates differ by reader entry point,
     not just technical mechanism.
   - For each candidate, include:
     - concept name
     - core desire
     - private gap
     - emotional lever
     - curiosity driver
     - mechanism in play
     - flow structure
     - fix direction
     - design implications
     - risks or claims to verify

3. Test against the locked baseline.
   - Check whether the candidate can use current `writing.md`.
   - Check whether it fits current `design.md`.
   - Reject candidates that require a different account voice or visual system.

4. Generate a validation sample.
   - Use the account-quality-gate process.
   - Render a non-hero slide or short sample from the candidate.
   - Save notes under `quality-gate/`.

5. Promote only after approval.
   - Add the pattern to `presets.md` only when the user approves the sample.
   - Include use case, hook behavior, flow structure, copy rhythm, product fit,
     example references, and risks.
   - Link to validation notes or the approved sample.

## Quality Bar

- The pattern explains why the viewer cares.
- The pattern is not just a renamed mechanism.
- The pattern can produce multiple future posts without copying a competitor.
- The sample follows `writing.md` without diluting the voice.
- The sample fits `design.md` without layout hacks.
- The preset remains supplemental to the baseline writing system.

# Workflow A1: Writing Principle Extraction

Use this when the user says `workflow a1`, `writing extraction`, `writing
principles`, or when Workflow A reaches baseline copy extraction.

Goal: create the indexed account writing system before any presets exist.

## Read First

1. `../AGENTS.md`
2. `workflow-a-new-account.md`
3. `workflow-a0-account-intake-reference-map.md`
4. `../accounts/{account}/account-brief.md`
5. `../accounts/{account}/extractions/reference-map.md`
6. `../references/templates/account-writing.md`
7. `../references/templates/writing/*.md`
8. `../references/skills/stop-slop/SKILL.md`
9. Writing-relevant references named in `reference-map.md`
10. Existing `../accounts/{account}/writing.md` and `../accounts/{account}/writing/`, if present

## Procedure

1. Confirm writing material is sufficient.
   - Use only references marked `writing` or `angle` in `reference-map.md`.
   - If examples are missing, stop and ask for copy samples, transcripts,
     screenshots, or post folders.

2. Analyze from the viewer's perspective.
   - Ask why the reader would stop, swipe, trust, save, or share.
   - Extract hook behavior, emotional lever, implied promise, copy rhythm,
     sentence shape, pacing, authority style, and weak patterns to avoid.
   - Capture observations in `writing/pattern-extractions.md`.

3. Create account-specific writing principles.
   - Convert repeated observations into stable principles.
   - Keep raw observations out of the top-level `writing.md`.
   - Write `writing/principles.md`.

4. Create supporting writing files.
   - `writing/copywriting-principles.md`: general persuasion logic that explains
     why the style works.
   - `writing/banned-patterns.md`: account-specific weak moves and replacements.
   - `writing/sample-posts.md`: approved or candidate samples with notes on why
     they work.
   - `writing/qa.md`: final copy checks and scoring.

5. Write `writing.md` as the retrieval hub.
   - Use `../references/templates/account-writing.md`.
   - Include status: `Pending quality gate`.
   - Include document authority, table of contents, conflict rule, core voice
     snapshot, locked rules, and quality-gate notes.
   - Make `writing.md` the highest-authority copy file.

6. Stop before presets.
   - Do not create `presets.md` in this workflow.
   - Angle and flow presets belong to Workflow A4 after baseline quality passes.

## Required Indexed Structure

```text
accounts/{account}/writing.md
accounts/{account}/writing/principles.md
accounts/{account}/writing/pattern-extractions.md
accounts/{account}/writing/copywriting-principles.md
accounts/{account}/writing/banned-patterns.md
accounts/{account}/writing/sample-posts.md
accounts/{account}/writing/qa.md
```

## Authority Hierarchy

`writing.md` must include this hierarchy. If files conflict, follow the
higher-priority file and note the conflict for cleanup.

| Priority | File | Use For |
| --- | --- | --- |
| 1 | `writing.md` | Current account voice, retrieval map, non-negotiable rules |
| 2 | `writing/principles.md` | Stable extracted account principles |
| 3 | `writing/qa.md` | Final copy checks |
| 4 | `writing/banned-patterns.md` | Account-specific weak moves |
| 5 | `writing/sample-posts.md` | Approved examples in use |
| 6 | `writing/pattern-extractions.md` | Raw or semi-processed observations |
| 7 | `writing/copywriting-principles.md` | General persuasion logic |

## Outputs

- `accounts/{account}/writing.md`
- `accounts/{account}/writing/` subfiles

## Agent Rules

- Do not treat a preset as the source of voice.
- Do not copy competitor wording.
- Do not turn raw observations into locked rules unless multiple examples or
  user feedback support them.
- Mark uncertain rules as candidates until the quality gate validates them.

---
name: writing-feedback-compounding
description: Capture, organize, and distill user writing critiques from brainstorming sessions so account writing guidance improves over time. Use when the user says save this writing feedback, record this writing preference, compound my suggestions, distill today's feedback, strengthen the writing rule, or says the AI repeated a writing mistake during hook/angle/copy brainstorming.
compatibility: opencode
metadata:
  repo_skill: references/skills/writing-feedback-compounding/SKILL.md
---

# Skill: Writing Feedback Compounding

Use this when the user gives reusable writing taste feedback during hook ideas,
Creative DNA ideation, angle variants, copy drafting, or Workflow B review.

The goal is simple: every useful critique becomes memory, so future brainstorming
needs less repeated correction.

This skill is the default destination for writing feedback. Do not put reusable
copy, hook, angle, wording, voice, or slide-flow criticism only into `BUGS.md`.
`BUGS.md` is for workflow/tooling failures; account writing feedback belongs in
the target account's writing memory files so drafting agents read it later.

## Trigger Phrases

- `save this as writing feedback`
- `record this writing preference`
- `remember this for the account`
- `compound this suggestion`
- `this is the same mistake as before`
- `strengthen the rule`
- `distill today's feedback`
- `update the writing rules from my critiques`
- `make the AI stop doing this in hooks`

## Read First

Use the smallest relevant set:

1. `AGENTS.md`
2. Full repo skill, if more detail is needed:
   `references/skills/writing-feedback-compounding/SKILL.md`
3. Target account files:
   - `accounts/{account}/account-brief.md`, if present
   - `accounts/{account}/writing.md`
   - `accounts/{account}/writing/refinement-personas.md`, if present
   - `accounts/{account}/writing/pattern-extractions.md`, if present
   - `accounts/{account}/presets.md`, if feedback concerns hook/angle presets
4. Current post concept/copy files only if the feedback refers to an active post.
5. Product files only if the feedback concerns product/app/claim language.

If no account is named, use the active locked account from `README.md` unless the
conversation clearly implies another account.

## Memory Hierarchy

Never skip the account writing files and record only a bug entry. If the critique
is worth remembering, at minimum capture it in `writing/pattern-extractions.md`.

### 1. Raw session feedback

Append messy, fast notes to:

```text
accounts/{account}/writing/pattern-extractions.md
```

Use for one-off notes, examples, rejected phrases, and before/after pairs.

### 2. Refinement behavior

Update when future drafts should self-check before being shown:

```text
accounts/{account}/writing/refinement-personas.md
```

### 3. Account writing law

Update only for stable, repeated, high-confidence rules:

```text
accounts/{account}/writing.md
```

## Command A: Capture Raw Feedback

When the user says `save this`, `record this`, or gives a reusable critique,
append this shape to `writing/pattern-extractions.md`:

```md
## YYYY-MM-DD — Brainstorming feedback

### Context
- Account:
- Post or session:
- Stage: hook ideas | Creative DNA | angle variants | copy draft | other

### Raw correction
"User's wording or close paraphrase."

### Before
Weak wording, pattern, or suggestion that triggered the correction.

### Better direction
Preferred wording, pattern, or strategic direction.

### Possible rule
Draft one reusable rule in plain language.

### Confidence
Low | Medium | High
```

Rules:

- Preserve the user's wording when possible.
- Capture before/after pairs whenever possible.
- Keep one-off notes out of `writing.md`.
- Mark repeated or explicitly important feedback as `High` confidence.

## Command B: Strengthen Existing Rule

When the user says `same mistake as before`, `strengthen the rule`, or similar:

1. Search account writing files for the closest existing rule.
2. Append the new raw feedback to `pattern-extractions.md`.
3. Update `writing/refinement-personas.md` with a sharper preflight check.
4. Update `writing.md` only if the rule is stable and account-level.

Use plain-language rules like:

```md
### Avoid [bad pattern]

Do not [specific repeated mistake]. This usually sounds like [examples]. Instead,
use [preferred pattern], especially when writing [hooks / transitions / CTA / proof].
```

## Command C: Distill Session Feedback

When the user says `distill today's feedback` or asks to update rules:

1. Read recent notes in `writing/pattern-extractions.md`.
2. Group critiques by repeated pattern:
   - hook voice
   - emotional lever
   - sentence rhythm
   - specificity/proof
   - banned phrases
   - account safety/claims
   - slide flow
   - CTA style
3. Promote stable patterns into `writing.md`.
4. Add/refine self-checks in `writing/refinement-personas.md`.
5. Leave one-off notes in `pattern-extractions.md` until they repeat.

## Promotion Rules

Promote feedback into `writing.md` when at least one is true:

- The user says it is important or repeated.
- The same critique appears across multiple sessions.
- It corrects a high-risk account voice issue.
- It changes hook/copy generation every time.
- It resolves a contradiction in current writing guidance.

Do not promote when it only applies to one post, conflicts with higher-authority
account rules, or is too vague to become durable guidance.

Ask one clarifying question if promotion would materially change account voice.

## Graphify Update

After changing durable feedback or writing-memory files, refresh the graph so
Creative DNA and future brainstorming can retrieve the new preference:

```text
graphify update .
```

Run this after edits to:

- `accounts/{account}/writing.md`
- `accounts/{account}/writing/refinement-personas.md`
- `accounts/{account}/writing/pattern-extractions.md`
- Creative DNA extraction or account-profile files
- Feedback-routing docs such as `AGENTS.md` or this skill file

If `graphify` is unavailable, tell the user the writing memory was updated but
the graph refresh could not be completed.

## Response Style

After capture, keep the reply short:

```md
Saved to `accounts/{account}/writing/pattern-extractions.md` as raw writing feedback.

Possible rule captured: [short rule].
```

After distillation, summarize only changed files.

## Constraints

- Do not rewrite approved final slide copy unless asked.
- Do not create or modify `flow.md` from this skill alone.
- Do not use `BUGS.md` as the primary memory for writing preferences. If a bug
  entry is genuinely needed, make it secondary and link the account writing file
  that received the durable rule or raw note.
- Do not invent account rules from vague feedback; capture vague feedback as raw
  notes first.
- Prefer before/after examples over abstract rules.
- Keep `writing.md` clean and high-authority.
- Verify product/app claim feedback against `product/claim-bank.md` before making
  it permanent.

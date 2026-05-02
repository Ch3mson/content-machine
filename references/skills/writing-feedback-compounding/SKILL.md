---
name: writing-feedback-compounding
description: Capture, organize, and distill user writing critiques from brainstorming sessions so account writing guidance improves over time. Use when the user says save this writing feedback, record this preference, compound my suggestions, distill today's feedback, strengthen the writing rule, or says the AI repeated a writing mistake during hook/angle/copy brainstorming.
---

# Skill: Writing Feedback Compounding

Use this skill when the user gives writing taste feedback during brainstorming,
hook generation, Creative DNA ideation, angle variants, copy drafts, or Workflow B
copy review.

The goal is to make the user's corrections compound, so future brainstorming needs
less critique.

This skill is the default destination for writing feedback. Do not put reusable
copy, hook, angle, wording, voice, or slide-flow criticism only into `BUGS.md`.
`BUGS.md` is for workflow/tooling failures; account writing feedback belongs in
the target account's writing memory files so drafting agents read it later.

## Trigger Phrases

Use this skill for phrases like:

- `save this as writing feedback`
- `record this writing preference`
- `remember this for the account`
- `compound this suggestion`
- `this is the same mistake as before`
- `strengthen the rule`
- `distill today's feedback`
- `update the writing rules from my critiques`
- `make the AI stop doing this in hooks`
- `I keep having to tell it not to write like this`

Also use it when the user rejects wording in a way that reveals a reusable writing
rule, even if they do not use the exact trigger phrase.

## Read First

Use the smallest relevant set:

1. `AGENTS.md`
2. This file
3. Target account files:
   - `accounts/{account}/account-brief.md`, if present
   - `accounts/{account}/writing.md`
   - `accounts/{account}/writing/refinement-personas.md`, if present
   - `accounts/{account}/writing/pattern-extractions.md`, if present
   - `accounts/{account}/presets.md`, if the feedback concerns angles/hooks tied
     to presets
4. Current post concept/copy files only if the feedback refers to an active post:
   - `accounts/{account}/posts/{post-slug}/concept/session-state.md`
   - `accounts/{account}/posts/{post-slug}/concept/copy-review.md`
   - `accounts/{account}/posts/{post-slug}/concept/copy-options.md`
5. Product files only if the feedback concerns product/app/claim language:
   - `product/app-brief.md`
   - `product/claim-bank.md`

If the account is not named, use the active locked account from `README.md` unless
the conversation clearly implies another account.

## Memory Hierarchy

Keep feedback in three layers.

Never skip the account writing files and record only a bug entry. If the critique
is worth remembering, at minimum capture it in `writing/pattern-extractions.md`.

### 1. Raw session feedback

Primary file:

```text
accounts/{account}/writing/pattern-extractions.md
```

Use this for messy, fast, high-volume notes. Do not over-polish. Preserve the
user's actual language when possible.

### 2. Refinement behavior

Primary file:

```text
accounts/{account}/writing/refinement-personas.md
```

Use this when the feedback should change how future drafts are self-critiqued
before being shown to the user.

### 3. Account writing law

Primary file:

```text
accounts/{account}/writing.md
```

Use this only for stable, repeated, high-confidence rules. Do not pollute the
main writing guide with every one-off correction.

## Commands

### Command A: Capture Raw Feedback

When the user says `save this`, `record this`, or gives a clear reusable critique,
append a note to `writing/pattern-extractions.md`.

Use this format:

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

- Capture the before/after pair whenever possible.
- If there is no exact before wording, describe the rejected pattern.
- Mark confidence `Low` for one-off taste notes.
- Mark confidence `Medium` when it matches existing writing guidance.
- Mark confidence `High` when the user says this is repeated or important.
- Do not update `writing.md` unless the user asks to distill or strengthen rules.

### Command B: Strengthen Existing Rule

When the user says `same mistake as before`, `strengthen the rule`, or similar:

1. Search the account writing files for the closest existing rule.
2. Append the new raw feedback to `pattern-extractions.md`.
3. Update `writing/refinement-personas.md` if the mistake should be caught before
   drafts are shown.
4. Update `writing.md` only if the critique is clearly stable and account-level.

Use this update style:

```md
### Avoid [bad pattern]

Do not [specific repeated mistake]. This usually sounds like [examples]. Instead,
use [preferred pattern], especially when writing [hooks / transitions / CTA / proof].
```

### Command C: Distill Session Feedback

When the user says `distill today's feedback`, `update the writing rules`, or asks
for compounding at the end of a session:

1. Read recent raw notes in `writing/pattern-extractions.md`.
2. Group critiques by repeated pattern:
   - hook voice
   - emotional lever
   - sentence rhythm
   - specificity/proof
   - banned phrases
   - account safety/claims
   - slide flow
   - CTA style
3. Promote only stable patterns into `writing.md`.
4. Add or refine self-checks in `writing/refinement-personas.md`.
5. Leave one-off notes in `pattern-extractions.md` as raw observations.

## Distillation Rules

Promote feedback into `writing.md` when at least one is true:

- The user says it is important or repeated.
- The same critique appears across multiple brainstorming sessions.
- It corrects a high-risk account voice issue.
- It changes how hooks/copy should be generated every time.
- It resolves a contradiction in the current writing guide.

Do not promote when:

- The feedback only applies to one post.
- The user is reacting to a specific phrase but not a general pattern.
- The rule would conflict with higher-authority account writing guidance.
- You cannot tell whether it is a permanent preference.

Ask one clarifying question if promotion would materially change the account
voice.

## Chat Response After Capturing

Keep the response short. Example:

```md
Saved to `accounts/{account}/writing/pattern-extractions.md` as raw writing feedback.

Possible rule captured: avoid generic motivational hook language; prefer private,
slightly uncomfortable self-recognition.
```

## Chat Response After Distilling

Summarize only what changed:

```md
Distilled today's feedback into:

- `accounts/{account}/writing.md`: added hook voice rule about private self-recognition.
- `accounts/{account}/writing/refinement-personas.md`: added a preflight check for generic motivational phrasing.
- Left 2 one-off notes in `pattern-extractions.md` until they repeat.
```

## Graphify Update

After changing any durable feedback or writing-memory file, refresh the project
graph so Creative DNA and future brainstorming can retrieve the new preference.

Run:

```text
graphify update .
```

Do this after edits to:

- `accounts/{account}/writing.md`
- `accounts/{account}/writing/refinement-personas.md`
- `accounts/{account}/writing/pattern-extractions.md`
- Creative DNA extraction or account-profile files
- Feedback-routing docs such as `AGENTS.md` or this skill file

If `graphify` is unavailable, tell the user the writing memory was updated but
the graph refresh could not be completed.

## Important Constraints

- Do not rewrite approved final slide copy unless the user asks.
- Do not create or modify `flow.md` from this skill alone.
- Do not use `BUGS.md` as the primary memory for writing preferences. If a bug
  entry is genuinely needed, make it secondary and link the account writing file
  that received the durable rule or raw note.
- Do not invent account rules from vague feedback. Capture vague feedback as raw
  notes first.
- Preserve the user's wording when recording criticism.
- Prefer before/after examples over abstract rules.
- Keep `writing.md` clean and high-authority; use `pattern-extractions.md` for
  noisy accumulation.
- If feedback involves product/app claims, verify against `product/claim-bank.md`
  before making it a permanent rule.

## Suggested User Macros

The user can use these shortcuts during brainstorming:

```text
Save this as writing feedback: [critique]
```

```text
This is the same mistake as before. Strengthen the rule: [critique]
```

```text
Distill today's writing feedback into the account rules.
```

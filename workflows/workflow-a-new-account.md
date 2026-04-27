# Workflow A: New Account Onboarding

Use this when the user says `workflow a`, `workflow-a`, `new account`, or asks to
create/onboard an account playbook.

Goal: create or update account-level source-of-truth files without guessing at
missing strategy.

## Read First

1. `../AGENTS.md`
2. `../product/app-brief.md`
3. `../product/claim-bank.md`
4. `../references/research/README.md`
5. `../references/templates/account-brief.md`
6. `../references/templates/account-sources.md`
7. Existing `../accounts/{account}/` files, if present

## Account Outputs

Create or update these files:

- `accounts/{account}/account-brief.md`
- `accounts/{account}/writing.md`
- `accounts/{account}/image.md`
- `accounts/{account}/sources.md`
- `accounts/{account}/presets.md`, if the account has multiple repeatable styles

Keep raw interpretation in `accounts/{account}/extractions/`.

## Required Inputs

Collect or explicitly mark missing:

- Account niche and audience.
- Platform priority.
- Primary goal: saves, shares, follows, comments, product awareness, or another goal.
- Competitor slideshow references for flow.
- Design references for image direction.
- Copy examples or tone notes.
- Product relationship to w(inner).
- Research sensitivity and claim-risk topics.

Ask in short rounds. Do not ask for every missing item at once.

## Procedure

1. Account intent interview:
   - Clarify the account niche, audience, POV, emotional tone, and what it should
     never sound like.
   - Write or update `account-brief.md`.

2. Competitor flow intake:
   - Inspect any screenshots, links, transcripts, or notes the user provides.
   - Extract hook type, slide count, slide roles, pacing, tension curve, CTA, and
     product-fit risk.
   - Save raw notes to `extractions/flow-analysis.md`.
   - Draft `flow.md` only after showing a short sample flow or getting enough
     explicit direction.

3. Design intake:
   - Inspect design references for typography, crop, spacing, texture, color,
     overlay, product fit, and slide consistency.
   - Save raw notes to `extractions/design-analysis.md`.
   - Write `image.md` as a practical visual system, not vague mood words.

4. Copy and tone:
   - Use `../references/skills/stop-slop/SKILL.md` as the base writing QA.
   - Show three short copy samples if the voice is not already locked.
   - Write `writing.md` with rhythm rules, banned patterns, examples, and QA.

5. Product mention rules:
   - Read `../product/app-brief.md` and `../product/claim-bank.md`.
   - Decide whether w(inner) is invisible, implied, softly mentioned, shown in
     product slide, caption-only, comments-only, or excluded.
   - Do not approve claims that the claim bank marks as flagged or rejected.

6. Research rules:
   - Use `../references/research/README.md`.
   - Create `sources.md` with content pillars, claim risk, preferred sources,
     claims to verify, and wording to avoid.

7. Lock:
   - Treat the user's feedback as higher priority than initial extraction.
   - Mark open questions inside `account-brief.md`.
   - If the user also tagged Workflow B, continue to Workflow B after required
     account files exist.

## Agent Rules

- Do not invent final account rules when user input is missing.
- Use placeholders only when a file must exist before inputs are ready.
- Copy competitor structure only, not wording, identity, or assets.
- Keep product claims inside approved claim-bank boundaries.
- Use fewer, better questions.

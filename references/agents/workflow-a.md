# Workflow A: New Account Onboarding

Use this document when creating a new slideshow account playbook.

The agent's job is not to fill markdown files from assumptions. The agent must interview the user, inspect provided references, show brief samples, get feedback, and only then lock source-of-truth files.

For creating new posts on an existing account, use `references/agents/workflow-b.md`.

---

## File Index

### Reference Files (read-only, shared across accounts)

| File | Purpose |
|------|---------|
| `references/agents/workflow-a.md` | This file. New account onboarding workflow. |
| `references/agents/workflow-b.md` | New post workflow for existing accounts. |
| `references/agents/image-processing.md` | Image pipeline: normalize → B&W → paper overlay → text. Includes full Python script. |
| `references/skills/stop-slop/SKILL.md` | Writing quality rules. Base standard for all copy. |
| `references/skills/stop-slop/references/phrases.md` | Banned phrases and filler to remove. |
| `references/skills/stop-slop/references/structures.md` | Banned sentence structures to avoid. |
| `references/skills/stop-slop/references/examples.md` | Before/after writing examples. |
| `references/research/README.md` | Research intake guide. Claim risk levels and source types. |
| `references/templates/account-brief.md` | Template for the account brief file. |
| `references/templates/account-sources.md` | Template for the sources file. |
| `product/app-brief.md` | w(inner) product source of truth. Read before any product mention. |
| `product/claim-bank.md` | Approved and flagged product claims. Read before any product mention. |

### Account-Level Files (one set per account)

| File | Purpose | When Locked |
|------|---------|-------------|
| `accounts/{account-name}/account-brief.md` | Account intent, audience, POV, product relationship. | After Phase 1 interview. |
| `accounts/{account-name}/writing.md` | Voice, tone, rhythm rules, banned patterns, copy samples. | After Phase 4 feedback. |
| `accounts/{account-name}/image.md` | Design system: layout, typography, color treatment, pipeline order, slide role mapping. | After Phase 3 feedback. |
| `accounts/{account-name}/sources.md` | Content pillars, claim risk levels, approved sources, banned claims. | After Phase 6 feedback. |
| `accounts/{account-name}/prompts.md` | Prompt templates for generating new posts. | After Phase 8 lock. |
| `accounts/{account-name}/extractions/flow-analysis.md` | Raw competitor flow extraction. Not source of truth. | After Phase 2. |
| `accounts/{account-name}/extractions/design-analysis.md` | Raw design reference extraction. Not source of truth. | After Phase 3. |

### Post-Level Files (one set per post)

| File | Purpose | When Created |
|------|---------|-------------|
| `accounts/{account-name}/{post-name}/flow.md` | Slide-by-slide mapping: role, image file, copy. | During post creation. |
| `accounts/{account-name}/{post-name}/process_images.py` | Image processing script for this post. References `image.md` rules. | During post creation. |
| `accounts/{account-name}/{post-name}/processed/` | Final processed slide images (slide_1.png through slide_N.png). | After running pipeline. |

---

## Required Inputs

Before finalizing an account, collect or explicitly mark missing:

- Account niche.
- Target audience.
- Platform priority, if TikTok and Instagram should differ.
- Primary performance goal: saves/shares, follows, comments, product awareness, or another goal.
- Competitor slideshow references for flow.
- Pinterest/design references for image direction.
- Copy examples or tone notes.
- Product relationship to w(inner).
- Research sensitivity and claim-risk topics.

## Rule For Questions

Ask questions in short rounds. Do not ask for everything at once.

Each round should do one job:

1. Define account intent.
2. Understand the user and niche.
3. Understand competitor flow inputs.
4. Understand design references.
5. Understand copy/tone.
6. Understand product mention boundaries.
7. Confirm research and claim risks.

After each round, summarize what changed in the account direction.

## Phase 1: Account Intent Interview

Ask until these are clear:

- What is the account about?
- Who should follow it?
- What does the audience already believe?
- What does the audience want but struggle to get?
- What emotion should the account create?
- What should the account never sound like?
- What should a high-performing slideshow make someone do?

Write answers into `account-brief.md`.

## Phase 2: Competitor Flow Intake

Ask the user for competitor slideshow examples before writing `flow.md`.

Accept:

- Local screenshots.
- Links.
- Transcripts.
- Notes about why the format works.

Then extract:

- Hook type.
- Slide count.
- Slide roles.
- Pacing.
- Tension curve.
- Repeated format mechanics.
- What changes across slides.
- Whether the competitor uses a CTA.
- Whether w(inner) could fit natively or should stay in comments/bio.

Write raw findings to `extractions/flow-analysis.md`.

Before finalizing `flow.md`, show the user a short flow sample:

```text
Sample flow:
1. [Hero slide role + example hook]
2. [Slide role + example point]
3. [Slide role + example point]
4. [Slide role + example point]
5. [Closing role + example ending]

Potential soft product mention:
[include or reject, with reason]
```

Ask for feedback on:

- Too close to competitor or safe to use?
- Right amount of product presence?
- Missing slide role?
- Wrong pacing?

Only then update `flow.md`.

## Phase 3: Design Reference Intake

Ask the user for Pinterest/design references before writing `image.md`.

For each reference, ask what the user likes if it is not obvious:

- Typography.
- Spacing.
- Overlay treatment.
- Crop.
- Mood.
- Color.
- Texture.
- Slide consistency.
- Product placement potential.

Write raw findings to `extractions/design-analysis.md`.

Before finalizing `image.md`, show the user a brief design interpretation:

```text
Design read:
- Typography: [one sentence]
- Layout: [one sentence]
- Image treatment: [one sentence]
- Overlay system: [one sentence]
- Slide 1 vs middle vs closing behavior: [one sentence]
- Product asset fit: [use app-in-hand / screenshot / implied / exclude]
```

Ask for feedback on:

- Does this match what you saw in the references?
- Should the system be cleaner, louder, darker, more editorial, more raw, more premium, or more native?
- Does product imagery feel natural or sponsored?

Only then update `image.md`.

## Phase 4: Copy And Tone Interview

Use Stop Slop as the base, but do not assume the account voice from Stop Slop alone.

Ask:

- Should the voice be first person, second person, or detached editorial?
- Should it feel coach-like, peer-like, analyst-like, confrontational, calm, aspirational, or blunt?
- What words should appear often?
- What words should be banned?
- Should posts use claims, stories, lists, mistakes, comparisons, or personal observations?
- How much research should appear in the copy?

Then show 3 short copy samples before writing `writing.md`.

Each sample should be small:

```text
Sample A - blunt coach:
Slide 1: [hook]
Slide 2: [body line]
Slide 3: [body line]

Sample B - calm performance:
Slide 1: [hook]
Slide 2: [body line]
Slide 3: [body line]

Sample C - sharper editorial:
Slide 1: [hook]
Slide 2: [body line]
Slide 3: [body line]
```

Ask the user:

- Which sample is closest?
- Which words feel wrong?
- Which line sounds most like the account?
- Which line sounds least like the account?
- Should the account become more direct, more premium, more raw, more emotional, or more practical?

Update `writing.md` only after this feedback.

## Phase 5: Product Mention Interview

Use `product/app-brief.md` and `product/claim-bank.md`.

Ask:

- Should w(inner) be invisible, implied, softly mentioned, or occasionally shown?
- Should product references live in the slideshow, caption, comments, or bio?
- Which app angle fits this account: confidence, pressure, mental reps, identity, match-day prep, slump recovery, or another angle?
- Which claims feel too salesy?

If no competitor CTA exists, generate three hypotheses:

| Hypothesis | Placement | Native reason | Sponsored-feeling risk | Recommendation |
| --- | --- | --- | --- | --- |

Do not finalize product rules until the user picks or rejects a direction.

## Phase 6: Research Interview

Use `references/research/README.md`.

Ask:

- Which topics will this account talk about often?
- Which topics could be harmful or misleading if wrong?
- Which claims need external support?
- Which claims can be opinion or observation?
- Which sources should be trusted?
- Which source types should be avoided?

Show a draft content-pillar risk map before writing `sources.md`:

| Content pillar | Claim risk | Source type needed | Notes |
| --- | --- | --- | --- |

Update `sources.md` after user confirmation.

## Phase 7: First Full Sample

After the initial `flow.md`, `writing.md`, `image.md`, and `sources.md` drafts exist, create one small sample concept.

Return:

- 5-8 slide flow.
- Draft slide copy.
- Image direction for each slide.
- Product mention decision.
- Flagged claims.
- Stop Slop QA score.
- Questions for user feedback.

The sample is a calibration artifact, not final content.

## Phase 8: Lock Source Of Truth

Only lock the account files after the user has reacted to:

- One flow sample.
- One design interpretation.
- Three copy samples.
- One content-pillar risk map.
- One full sample slideshow concept.

Then update:

- `account-brief.md`
- `flow.md`
- `writing.md`
- `image.md`
- `sources.md`
- `prompts.md`

---

## Agent Rules

- Do not invent final account rules when user input is missing.
- Use placeholders only when a file must exist before inputs are ready.
- Keep raw interpretation in `extractions/`.
- Keep final rules in source-of-truth files.
- Ask fewer, better questions per round.
- Always show brief samples before asking the user to judge tone or style.
- Treat the user's feedback as higher priority than the initial extraction.
- Copy competitor structure only, not wording, identity, or assets.
- Do not force w(inner) into the slideshow.
- Flag unapproved product claims.
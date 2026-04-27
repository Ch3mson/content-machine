# Account Onboarding Agent Workflow

Use this document when creating a new slideshow account playbook or creating new posts for an existing account.

The agent's job is not to fill markdown files from assumptions. The agent must interview the user, inspect provided references, show brief samples, get feedback, and only then lock source-of-truth files.

---

## File Index

### Reference Files (read-only, shared across accounts)

| File | Purpose |
|------|---------|
| `references/agents/account-onboarding.md` | This file. Full workflow for onboarding and post creation. |
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

## Workflow A: New Account Onboarding

Use this workflow when setting up a brand new account that does not yet have source-of-truth files.

### Required Inputs

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

### Rule For Questions

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

### Phase 1: Account Intent Interview

Ask until these are clear:

- What is the account about?
- Who should follow it?
- What does the audience already believe?
- What does the audience want but struggle to get?
- What emotion should the account create?
- What should the account never sound like?
- What should a high-performing slideshow make someone do?

Write answers into `account-brief.md`.

### Phase 2: Competitor Flow Intake

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

### Phase 3: Design Reference Intake

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

### Phase 4: Copy And Tone Interview

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

### Phase 5: Product Mention Interview

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

### Phase 6: Research Interview

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

### Phase 7: First Full Sample

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

### Phase 8: Lock Source Of Truth

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

## Workflow B: New Post for Existing Account

Use this workflow when an account already has locked source-of-truth files and you need to create a new post.

### Prerequisites

Before starting, confirm these files exist and are locked:

- `accounts/{account-name}/writing.md` — voice, tone, rhythm rules.
- `accounts/{account-name}/image.md` — design system, pipeline specs, slide role mapping.
- `accounts/{account-name}/sources.md` — claim risk levels, approved sources.

If any file is missing, go back to Workflow A.

### Step 1: Gather Post Inputs

Ask the user for:

1. **Athlete or subject** — Who is this post about?
2. **Photos** — Raw images for each slide role. The user provides these. Ask which photo maps to which role if not obvious.
3. **Product shot** — Phone-in-hand image for slide 6, if the account uses one.
4. **Any specific copy direction** — If the user has a quote, angle, or fact they want included.

If the user does not have photos yet, pause and ask them to provide them before continuing.

### Step 2: Write the Flow

Using `writing.md` rules and `image.md` slide role mapping, write `flow.md` for the post.

The flow must follow the account's established structure. For the athlete-stories account, this is:

| Slide | Role | Copy Rhythm |
|-------|------|-------------|
| 1 | The Beginning | Short. Staccato. 2-5 words per sentence. |
| 2 | The Grind | Medium. 8-14 words. Building context. |
| 3 | The Weight | Medium. Tension rising. |
| 4 | The Peak | Longest. 15-25 words. The visualization reveal. |
| 5 | The Transformation | Medium. The payoff. |
| 6 | The Product | Short. Grounded product mention. |
| 7 | The Legend | Athlete quote. |

Rules for writing the flow:

- Follow `writing.md` rhythm rules exactly. Do not invent new patterns.
- Follow `writing.md` banned patterns. Run the Stop Slop QA checklist before finalizing.
- Use the product mention style defined in `account-brief.md`. Do not make product claims that are not in `product/claim-bank.md`.
- Flag any claims that need source verification per `sources.md`.
- The product slide must feel native to the story. Do not force w(inner) if the flow does not support it.

Show the user the draft flow and ask:

- Does the rhythm match the account style?
- Is the product mention native or does it break the story?
- Any claims that feel off or too salesy?
- Any slide that feels weak or out of order?

Only proceed after user approval.

### Step 3: Map Images to Roles

Using the user's provided photos, assign each image to a slide role.

Rules:

- The user specifies which photo is slide 1 and which is the visualization/peak slide. The agent assigns the rest based on narrative fit.
- All images must follow the `image.md` design system.
- If a photo does not fit a role well, flag it and suggest an alternative.

Write the image mapping into `flow.md`.

### Step 4: Process Images

Run the image processing pipeline defined in `references/agents/image-processing.md`.

The pipeline must run in this exact order:

1. **Normalize to 9:16** — Crop and resize every image to 1080x1920.
2. **Convert to B&W** — Grayscale + 1.3x contrast.
3. **Apply paper overlay** — Vintage paper texture with sepia grain, dark spots, and vignette.
4. **Add text overlay** — Centered white text, Arial Bold 36pt, 3px black outline, 16px line spacing, 140px side margins.

Generate `process_images.py` for the post using the slide mapping from `flow.md`.

Run the script and save output to `accounts/{account-name}/{post-name}/processed/`.

Show the user the processed slides and ask:

- Is the text readable against each background?
- Is the spacing clean and consistent?
- Does the paper overlay feel right or too strong/too weak?
- Does the product slide feel native?

Only proceed after user approval.

### Step 5: Final Review

Before delivering, run these checks:

- [ ] Does every slide follow the `writing.md` rhythm rules?
- [ ] Does every slide follow the `writing.md` banned patterns? Run the Stop Slop QA checklist.
- [ ] Does the product mention follow `account-brief.md` and `product/claim-bank.md`?
- [ ] Are all claims flagged per `sources.md` risk levels?
- [ ] Are all images exactly 1080x1920?
- [ ] Are all images B&W with paper overlay applied?
- [ ] Is text centered with 140px side margins?
- [ ] Is line spacing 16px between lines?
- [ ] Does the flow follow the account's established slide role structure?

Deliver the final `processed/` folder with all slides.

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
- When creating a new post for an existing account, always read the account's `writing.md`, `image.md`, and `sources.md` before writing any copy.
- When processing images, always follow the pipeline order in `references/agents/image-processing.md`. Never skip the normalize step.
- Never auto-wrap text. Respect manual line breaks from `flow.md` exactly.
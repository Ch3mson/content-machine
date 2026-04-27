# Workflow B: New Post for Existing Account

Use this document when an account already has locked source-of-truth files and you need to create a new post.

For setting up a brand new account, use `references/agents/workflow-a.md`.

---

## File Index

### Reference Files (read-only, shared across accounts)

| File | Purpose |
|------|---------|
| `references/agents/workflow-a.md` | New account onboarding workflow. |
| `references/agents/workflow-b.md` | This file. New post workflow for existing accounts. |
| `references/agents/image-processing.md` | Image pipeline: normalize → B&W → paper overlay → text. Includes full Python script. |
| `references/skills/stop-slop/SKILL.md` | Writing quality rules. Base standard for all copy. |
| `references/skills/stop-slop/references/phrases.md` | Banned phrases and filler to remove. |
| `references/skills/stop-slop/references/structures.md` | Banned sentence structures to avoid. |
| `references/skills/stop-slop/references/examples.md` | Before/after writing examples. |
| `references/research/README.md` | Research intake guide. Claim risk levels and source types. |
| `product/app-brief.md` | w(inner) product source of truth. Read before any product mention. |
| `product/claim-bank.md` | Approved and flagged product claims. Read before any product mention. |

### Account-Level Files (must exist before starting)

| File | Purpose |
|------|---------|
| `accounts/{account-name}/writing.md` | Voice, tone, rhythm rules, banned patterns, copy samples. |
| `accounts/{account-name}/image.md` | Design system: layout, typography, color treatment, pipeline order, slide role mapping. |
| `accounts/{account-name}/sources.md` | Content pillars, claim risk levels, approved sources, banned claims. |
| `accounts/{account-name}/account-brief.md` | Account intent, audience, POV, product relationship. |

### Post-Level Files (created during this workflow)

| File | Purpose | When Created |
|------|---------|-------------|
| `accounts/{account-name}/{post-name}/flow.md` | Slide-by-slide mapping: role, image file, copy. | Step 2. |
| `accounts/{account-name}/{post-name}/process_images.py` | Image processing script for this post. References `image.md` rules. | Step 4. |
| `accounts/{account-name}/{post-name}/processed/` | Final processed slide images (slide_1.png through slide_N.png). | Step 4. |

---

## Prerequisites

Before starting, confirm these files exist and are locked:

- `accounts/{account-name}/writing.md` — voice, tone, rhythm rules.
- `accounts/{account-name}/image.md` — design system, pipeline specs, slide role mapping.
- `accounts/{account-name}/sources.md` — claim risk levels, approved sources.

If any file is missing, go back to Workflow A (`references/agents/workflow-a.md`).

---

## Step 1: Gather Post Inputs

Ask the user for:

1. **Athlete or subject** — Who is this post about?
2. **Photos** — Raw images for each slide role. The user provides these. Ask which photo maps to which role if not obvious.
3. **Product shot** — Phone-in-hand image for slide 6, if the account uses one.
4. **Any specific copy direction** — If the user has a quote, angle, or fact they want included.

If the user does not have photos yet, pause and ask them to provide them before continuing.

---

## Step 2: Write the Flow

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

---

## Step 3: Map Images to Roles

Using the user's provided photos, assign each image to a slide role.

Rules:

- The user specifies which photo is slide 1 and which is the visualization/peak slide. The agent assigns the rest based on narrative fit.
- All images must follow the `image.md` design system.
- If a photo does not fit a role well, flag it and suggest an alternative.

Write the image mapping into `flow.md`.

---

## Step 4: Process Images

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

---

## Step 5: Final Review

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

- Always read the account's `writing.md`, `image.md`, and `sources.md` before writing any copy.
- Always follow the pipeline order in `references/agents/image-processing.md`. Never skip the normalize step.
- Never auto-wrap text. Respect manual line breaks from `flow.md` exactly.
- Do not force w(inner) into the slideshow.
- Flag unapproved product claims.
- Treat the user's feedback as higher priority than the initial draft.
- If account source-of-truth files are missing, go back to Workflow A.
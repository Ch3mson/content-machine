---
name: post-concept-flow
description: Guide a slideshow post from broad avatar and pain-point idea through confirmation, online VOC research, angle issue selection, flow architecture variants, copy variants, and image handoff. Use when the user wants a structured new-post ideation process, says concept flow, VOC research, avatar pain point, sophisticate an idea, or asks to develop a new post before writing flow.md.
---

# Post Concept Flow

## Goal

Use this before Workflow B writes final `flow.md` when the user has a broad post idea but the angle, structure, and slide copy are not locked.

This skill is a chat-led decision flow. Pause at each approval gate. Do not skip ahead because the user gave a strong starting idea.

## Read First

Use the smallest relevant set:

1. `AGENTS.md`
2. `workflows/workflow-b-new-post.md`
3. `references/skills/angle-variants/SKILL.md`
4. Target account files, if an account is named or obvious:
   - `accounts/{account}/account-brief.md`
   - `accounts/{account}/presets.md`, if present
   - `accounts/{account}/writing.md`
   - `accounts/{account}/design.md`
   - `accounts/{account}/image.md`
   - `accounts/{account}/sources.md`
5. `references/skills/stop-slop/SKILL.md` before writing copy variants.
6. `product/app-brief.md` and `product/claim-bank.md` before any product mention, app mention, or product claim.

If the account is missing and not obvious, ask the smallest clarifying question before continuing.

## Terms

- Avatar: the target reader or user segment, such as a soccer winger, hockey player, anxious founder, or injured runner.
- Pain point: the specific frustration, fear, identity gap, performance gap, or hidden problem the post targets.
- Angle issue: the issue and psychological lens. It is not final slide copy and not the final hook.
- Flow architecture: the slide sequence concept, such as "do not do this, reason 1, reason 2" or "top 5 routines in order."
- Copy variation: complete draft text for each slide.

## Workspace Files

Create or use a post workspace. Preferred shape:

```text
accounts/{account}/posts/{post-name}/
  concept/
    intake.md
    voc-research.md
    angle-options.md
    selected-angle.md
    flow-options.md
    session-state.md
    copy-options.md
  flow.md
```

For legacy post folders, create the `concept/` directory inside the existing post folder.

If `{post-name}` is unknown, wait until the intake is confirmed, then create a short slug from the avatar and pain point. Do not create `flow.md` until the user approves a copy direction.

## Approval Gates

Follow these gates in order:

1. Intake summary confirmed by the user.
2. VOC research and angle issue options reviewed by the user.
3. One angle issue selected by the user.
4. Three flow architectures reviewed by the user.
5. One flow architecture selected by the user.
6. `session-state.md` written before deeper copy work.
7. Three copy variations reviewed by the user.
8. One copy variation selected or combined into final `flow.md`.

Accepted confirmations include "confirm", "yes", "agreed", "same page", or a clear selection.

## Stage 1: Intake And Confirmation

Start from the user's broad idea. Collect only what is needed:

- account or post workspace
- avatar
- pain point
- desired identity, outcome, or transformation
- sport, role, niche, or context
- product relevance, if any
- claim sensitivity, if obvious

If enough context exists, summarize before doing research:

```md
Here is what I think so far:

- Target avatar:
- Pain point:
- Desired transformation:
- Likely emotional lever:
- What the post should avoid:
- Product or claim constraints:

Reply "confirm" if this is right, or correct the parts that feel off.
```

Do not research yet. Wait for confirmation or corrections.

After confirmation, write `concept/intake.md`.

## Stage 2: VOC Research And Angle Issues

Research online after the intake gate. Use current web access when available. If the environment has no browsing capability, ask the user for sources or permission to proceed from provided materials.

Research for voice of customer, not just facts. Useful sources include:

- Reddit threads, forums, Discord-style community posts, and Q&A pages
- YouTube comments, creator comments, and coaching breakdowns
- TikTok or Instagram comment patterns when accessible
- product reviews, app reviews, and competitor comment sections
- coaching blogs, newsletters, podcasts, or expert explainers

Treat community language as audience evidence, not factual proof. Use reliable sources for factual, health, performance, or scientific claims.

Write `concept/voc-research.md` with:

- confirmed intake
- search queries used
- source list with URLs and access dates
- repeated complaints and phrases, paraphrased unless short quotes are necessary
- desire language and identity language
- objections, skepticism, and shame points
- mechanisms that may explain the pain
- claim-risk notes from the account `sources.md`

Then read and apply `references/skills/angle-variants/SKILL.md`. Write `concept/angle-options.md` with 3 to 6 angle issue options. Each option should cover:

- concept name
- core desire
- private gap
- emotional lever
- mechanism in play
- why the reader would keep reading
- fix direction

Present a concise research summary and the strongest angle issue options in chat. Ask the user to choose one angle or revise the direction. Do not write final slide copy.

## Stage 3: Selected Angle And Flow Architectures

After the user selects an angle issue, write `concept/selected-angle.md` with:

- selected angle issue
- target avatar
- pain point
- promised self or desired identity
- private gap
- emotional lever
- mechanism in play
- fix direction
- claims to verify or avoid
- words, frames, or tones to avoid

Generate exactly 3 flow architecture options and save them in `concept/flow-options.md`.

Each flow architecture must include:

- concept name
- clickbait hero direction, not polished final copy
- slide count range
- sequential slide jobs
- curiosity engine
- why this structure fits the selected angle
- image implications
- claim-risk notes

Keep this at the structure level. Do not write exact slide copy yet.

Ask the user to choose one architecture or combine parts.

## Stage 4: Session Checkpoint Before Copy

After the user chooses a flow architecture, write `concept/session-state.md` before producing copy variants.

The checkpoint must let a new session continue without rereading the full chat:

```md
# Session State

## Account And Post

## Confirmed Intake

## Research Summary

## Selected Angle

## Selected Flow Architecture

## Source List

## Claims To Verify Or Avoid

## Next Step
Generate 3 copy variations for the selected flow architecture.
```

Only after this file exists, proceed to copy variants.

## Stage 5: Copy Variations

Read `references/skills/stop-slop/SKILL.md`, the account `writing.md`, and the
account `design.md`.

Create `concept/copy-options.md` with exactly 3 complete copy variations for the selected architecture:

- Variation A: direct and sharp
- Variation B: more curiosity-led
- Variation C: more identity or emotion-led

Each variation should include:

- slide number
- slide role
- draft slide text
- notes on manual line breaks if needed
- claim-risk notes when relevant

Use the account's writing rules. Avoid generic motivation, empty hype, and AI-pattern phrasing. Use only approved product claims.
Use the account's design rules so slide copy fits the intended section layout,
typography hierarchy, manual line breaks, and photo-frame placement.

Present the 3 options in chat with a short recommendation. Ask the user to choose one, combine parts, or request edits.

## Stage 6: Final Flow And Image Handoff

After the user approves a copy direction:

1. Write final `flow.md` in the post folder.
2. Follow Workflow B, the account `design.md` slide format, and the account
   `image.md` slide roles.
3. Preserve manual line breaks that matter for rendering.
4. If the user asked for an end-to-end post, continue into image sourcing and image processing.
5. If the user only asked for ideation or copy, stop after `flow.md` and state the next command or workflow to run.

For image sourcing, use the post `image_preset.json` when present or create it from the account image rules. For image processing, run Workflow C.

## Quality Bar

Before moving between gates, check:

- The avatar and pain are specific enough to make the reader feel recognized.
- Research surfaced audience language, not just expert explanations.
- The selected angle is an issue and psychological lens, not a hook.
- The 3 flow architectures differ in sequence logic, not just wording.
- The checkpoint file captures enough context to survive a new session.
- Final copy follows account rules and Stop Slop QA.
- Product and factual claims are sourced or removed.

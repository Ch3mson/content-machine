---
name: hook-idea-extraction
description: Extract reusable hook ideas, scroll-stopping mechanics, and transferable post patterns from video transcripts, captions, slideshow screenshots, image carousels, or inspiration posts. Use when the user says hook ideas, hook bank, pull the hook, analyze this hook, transcript inspiration, slideshow inspiration, save this inspo, or asks whether a post's hook can be reused for other accounts.
---

# Hook Idea Extraction

## Overview

Use this skill to turn watched videos, transcripts, screenshots, or slideshow folders into reusable hook cards in `references/hook-ideas/`. The goal is to capture account-agnostic inspiration without accidentally promoting it into final account rules.

## Read First

1. `AGENTS.md`
2. `references/hook-ideas/README.md`
3. The user-provided transcript, caption text, screenshot sequence, slideshow folder, or raw post notes
4. Target account files only if the user asks whether the idea fits a specific account

## Input Handling

- If the user pastes a transcript or caption export, analyze it directly.
- If the user provides a TikTok video URL, fetch a transcript with `tools/tiktok-transcript-sourcer/download_tiktok_transcript.py`. Do not download the video.
- If the user provides a TikTok photo/slideshow URL, use `references/skills/tiktok-photo-sourcing/SKILL.md` and `tools/tiktok-photo-sourcer/download_tiktok_photos.py --out references/hook-ideas/inbox/slideshows/{slug}/images "{url}"`, then transcribe the visible words slide by slide.
- If the user provides a slideshow screenshot folder, inspect the visible slide text and image sequence.
- If the user provides images in chat, analyze the first-frame hook, slide order, visual hierarchy, and implied swipe reason.
- If the user gives a video URL from a platform Supadata supports, use the transcript sourcer when possible. If the video is private, restricted, or unsupported, ask for a transcript/caption export.
- If the user says to save it, bank it, or put it in the hook ideas folder, create a card and update `references/hook-ideas/index.md`.
- If the user only asks for a quick opinion, answer in chat and do not write files unless they approve saving.

## TikTok Video Transcript Path

Use:

```powershell
python tools/tiktok-transcript-sourcer/download_tiktok_transcript.py "{tiktok-video-url}"
```

The script reads `SUPADATA_API_KEY` from the shell or local `.env`, calls Supadata's transcript endpoint, and saves markdown under `references/hook-ideas/inbox/transcripts/`.

Use `--mode native` only when the user wants to avoid AI transcription costs. Default `--mode auto` may generate a transcript if native subtitles are unavailable.

## TikTok Photo Slideshow Path

1. Download images into the hook-ideas inbox, not a specific account, unless the user asks for an account reference folder:

```powershell
python tools/tiktok-photo-sourcer/download_tiktok_photos.py `
  --out "references/hook-ideas/inbox/slideshows/{slug}/images" `
  "{tiktok-photo-url}"
```

2. Prepare a transcript scaffold:

```powershell
python tools/slideshow-transcriber/prepare_slideshow_transcript.py `
  "references/hook-ideas/inbox/slideshows/{slug}/images" `
  --source-url "{tiktok-photo-url}" `
  --slug "{slug}"
```

3. Inspect each slide image visually and fill the scaffold with the exact visible text. Preserve slide order and meaningful line breaks.
4. Analyze the full slide flow after transcription, not just slide 1.

## Extraction Lens

Extract the reusable move, not the source's exact wording.

For each source, identify:

- Original hook or first-frame promise.
- Scroll-stop reason.
- Retention reason: why someone keeps watching or swiping.
- Flow map: each beat, its job, and the retention mechanic.
- Hook archetype.
- Emotional lever.
- Curiosity engine.
- Proof or credibility device.
- Surface topic versus deeper viewer desire.
- Private pain, identity gap, status threat, or contradiction.
- Transferable pattern and safe rewrite formula.
- Account types that could use the pattern.
- Risks: claim burden, copycat wording, niche mismatch, or weak payoff.

## Saving Cards

When saving, use:

```text
references/hook-ideas/cards/YYYY-MM-DD-source-slug.md
```

Start from `references/hook-ideas/templates/hook-card.md`. Update `references/hook-ideas/index.md` in the same turn.

If the raw transcript or manual slide text is not already stored elsewhere, save it under:

```text
references/hook-ideas/inbox/transcripts/
references/hook-ideas/inbox/slideshows/
```

## Relationship To Existing Workflows

- Use this skill for raw, universal inspiration.
- Use `angle-variants` when turning an idea into 3 account-aware angle concepts.
- Use `post-concept-flow` when building a real post from a broad idea.
- Use `angle-extraction` only when validating a repeated pattern into a specific account's `presets.md`.

## Hard Rules

- Do not copy hooks verbatim into account posts.
- Do not treat a hook card as a validated account preset.
- Do not invent a transcript. If the video text is unavailable, ask for it.
- Do not invent product claims from inspiration sources.

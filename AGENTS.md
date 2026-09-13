# Agent Router

This is a docs-first workspace for the **antigpt** Instagram/TikTok account. One
post format is live: a single still of the locked avatar face-swapped onto a
study composition board, one short first-person line rendered on it, and a CTA.
Start here, then read only the files the request needs.

## Pipeline Ownership

Codex owns building and maintaining the UGC pipeline in this repo: sourcing,
avatar production, copy handoff, rendering, post records, and learning from
results. Carry requested improvements through implementation and verification.
The current production format stays the single avatar still described below;
new formats can be added when Benson asks for them.

- Read `FOLDERS.md` before adding or reorganizing files.
- Read `references/ugc-pipeline.md` for pipeline development and remaining gaps.
- Read `references/notion.md` when using the connected research knowledge base.
- Keep account preferences and production decisions in the account files so
  future sessions inherit them. Link supporting Notion research where useful.
- Benson approves copy and publishes social posts. Building the pipeline does
  not itself authorize social publishing or changing the research bots.

## Tags Are Commands

If the user says one of these, start the matching file without waiting for another prompt:

| User intent | Start here |
| --- | --- |
| `face swap`, `swap her onto`, `put the avatar on`, `put her in this`, `new still`, `batch these boards` | `references/skills/avatar-face-swap/SKILL.md` |
| `caption this`, `overlay text`, `put the line on the still`, `add the text` | `references/skills/caption-overlay/SKILL.md` |
| `hook ideas`, `hook bank`, `pull the hook`, `analyze hook`, `slideshow inspo`, TikTok post analysis | `references/skills/hook-idea-extraction/SKILL.md` + `references/hook-ideas/README.md` |
| `TikTok photos`, `TikTok carousel`, `source TikTok`, `download TikTok`, `source board` | `references/skills/tiktok-photo-sourcing/SKILL.md` + `tools/tiktok-photo-sourcer/README.md` |
| `stop slop`, `anti-AI writing`, `clean copy` | `references/skills/stop-slop/SKILL.md` |
| `save this connection`, `graphify this connection`, `remember this link`, `capture this reasoning` | `references/skills/graphify-connection-capture/SKILL.md` |
| product / app / claim / AntiGPT / detector mention | `product/antigpt-brief.md` + `product/antigpt-claim-bank.md` before writing |
| end-to-end "make a new post from this board" | `references/skills/avatar-post-producer/SKILL.md` |
| build / improve / fix the UGC pipeline | `references/ugc-pipeline.md` + `FOLDERS.md` |
| Notion knowledge / Grok research / winning formats | `references/notion.md` |

Codex discovers skills through `.agents/skills/` links; Cursor uses
`.cursor/skills/` wrappers. Canonical bodies live in `references/skills/`.
Codex's optional project agent is `.codex/agents/ugc-pipeline-builder.toml`;
setup details live in `.codex/README.md`. The primary agent can run the same
workflows directly without spawning a subagent.

## Read Order

1. Selected skill.
2. `accounts/antigpt/README.md` (format, avatar identity, boards table, posts table, commands).
3. `accounts/antigpt/account-brief.md` when drafting copy or judging fit.
4. Product files only if the copy mentions AntiGPT, antigpt.me, or a detector.
5. `references/hook-ideas/cards/2026-09-08-bellajobtips-crying-girl-single.md` when ideating lines.
6. Tool docs only when the skill calls for that tool.

## Workspace Contracts

- Account source of truth is `accounts/antigpt/`. `README.md` is the hub;
  `account-brief.md` is audience and voice memory.
- `accounts/antigpt/avatar/asian-girl-avatar.jpg` is the identity lock. It is Figure 1 on
  every fal edit. Never generate or post a different girl.
- `accounts/antigpt/boards/` holds other people's photos used as Figure 2
  composition inputs. Boards are never posted. Each board has a row in the hub
  README.
- `accounts/antigpt/outputs/{stamp}/` holds face-swap candidates plus
  `contact-sheet.jpg`. It is gitignored scratch; copy the exact chosen render
  into a post. `swap_avatar.py <board> --post N` generates a fresh still.
- `accounts/antigpt/posts/N/` holds `image.jpg` (clean still),
  `image_caption.jpg` (captioned render), and `caption.md` (status, board,
  approved copy). Update the Posts table in the hub README by hand.
- Hook inspiration lives in `references/hook-ideas/`. Cards are raw inspiration,
  not account rules or final copy.
- Raw reference posts from other accounts live in `references/social-accounts/{account}/`.
- `tools/` is only for runnable utilities. Strategy notes belong in `references/`
  or `product/`.
- Python tooling is standard library plus Pillow; `FAL_KEY` lives in the repo
  `.env` (gitignored).

## Commands And Gotchas

- Batch face-swap every board into a review folder with a contact sheet:
  `python tools/fal/swap_avatar.py accounts/antigpt/boards`
- One board straight into a post: `python tools/fal/swap_avatar.py <board.jpg> --post N`
  (refuses to overwrite an existing `image.jpg` without `--force`).
- Plan without spending: add `--dry-run`. Print the identity-lock prompt: `--prompt-only`.
- Caption an approved line: `python tools/fal/caption.py --image accounts/antigpt/posts/N/image.jpg --text "line 1\nline 2"`
  writes `image_caption.jpg` beside the still. Test renders go to `/tmp`.
- Free-form still or edit: `python tools/fal/generate.py --prompt "..." [--ref a.jpg --ref b.jpg]`
- Short clip from a still (Kling): `python tools/fal/video.py --image <still> --prompt "..." --out <clip.mp4>`
- TikTok photo post into boards: `python tools/tiktok-photo-sourcer/download_tiktok_photos.py --out accounts/antigpt/boards "<url>"`, then rename to slugs.
- Instagram needs a logged-in browser: `gallery-dl --cookies-from-browser chrome -D accounts/antigpt/boards "<url>"`.
- Run every script from the repo root. Paths may be repo-relative or absolute.

## Hard Rules

- Do not invent product claims; use `product/antigpt-claim-bank.md`.
- Copy goes in chat first. Paste the exact lines with line breaks, wait for
  explicit approval, then render. Never render placeholder text onto a post still.
- Preserve approved wording and manual line breaks exactly when rendering.
- Never generate a different girl. If `avatar/asian-girl-avatar.jpg` is missing, stop and ask.
- Strip source on-screen text and watermarks in every swap unless the user asks
  to keep them.
- Never overwrite a still whose `caption.md` says Posted without the user saying so.
- Keep the clean still and the captioned still as separate files.
- Do not copy hooks verbatim from `references/hook-ideas/`; abstract the pattern
  and rewrite it in the account voice.
- Use `BUGS.md` only for real tooling failures. Voice and format feedback goes
  into `accounts/antigpt/account-brief.md` or the hub README rules.

## graphify

Graphify is optional local retrieval at `graphify-out/`. If the graph/report
is absent, inspect the repo files directly; do not claim it is available.

Rules:
- Before answering architecture or codebase questions, read graphify-out/GRAPH_REPORT.md if present for god nodes and community structure
- If graphify-out/wiki/index.md exists, navigate it instead of reading raw files
- For cross-module "how does X relate to Y" questions, prefer `graphify query "<question>"`, `graphify path "<A>" "<B>"`, or `graphify explain "<concept>"` over grep — these traverse the graph's EXTRACTED + INFERRED edges instead of scanning files
- After modifying code files in this session, run `graphify update .` to keep the graph current (AST-only, no API cost)
- After modifying account memory files (`accounts/antigpt/README.md`, `accounts/antigpt/account-brief.md`) or feedback-routing docs, run `graphify update .` so future drafting and hook ideation can retrieve the new preference. If graphify is unavailable, state that the memory was updated but graph refresh failed.

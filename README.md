# Content Machine

Docs-first workspace for the **antigpt** account (antigpt.me). One post format:
a single still of the locked avatar face-swapped onto a study photo, one short
first-person line on it, and a CTA.

Start with `AGENTS.md`. It routes phrases like `face swap`, `caption this`, and
`hook ideas` to the right skill and script.

Codex owns pipeline development here. See [Codex setup](.codex/README.md),
[folder guidelines](FOLDERS.md), and [pipeline priorities](references/ugc-pipeline.md).
The connected [Notion knowledge base](references/notion.md) holds broader
research; account rules, skills, claims, and production records stay in Git.

## Pipeline

```text
board (someone's study photo)  +  avatar/anchor.jpg
        │
        ▼  python tools/fal/swap_avatar.py <boards>          (fal Seedream edit)
accounts/antigpt/review/{stamp}/*.jpg + contact-sheet.jpg
        │  pick one
        ▼  copy the exact selected review image + create caption.md
accounts/antigpt/posts/N/image.jpg
        │  approve copy in chat
        ▼  python tools/fal/caption.py --image ... --text "..."
accounts/antigpt/posts/N/image_caption.jpg  ->  post it
```

## Directory Map

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Router and workspace contract for agents. |
| `FOLDERS.md` | Folder ownership, naming, knowledge retention, and Git guidelines. |
| `.agents/skills/` | Codex skill discovery links to the canonical workflows. |
| `.codex/` | Codex setup and optional UGC pipeline builder agent. |
| `accounts/antigpt/` | The account: hub README, brief, `avatar/`, `boards/`, `posts/`, fonts. |
| `product/` | AntiGPT product brief and claim bank. Read before any product mention. |
| `references/skills/` | Canonical workflows, including the end-to-end avatar-post-producer. |
| `references/notion.md` | Research knowledge-base entrypoints and source boundaries. |
| `references/ugc-pipeline.md` | Current capabilities and development priorities. |
| `references/hook-ideas/` | Hook inspiration bank (bellajobtips crying-girl card and raw inbox). |
| `references/social-accounts/` | Raw reference posts from other accounts. |
| `tools/fal/` | fal scripts: `swap_avatar.py`, `caption.py`, `generate.py`, `video.py`. |
| `tools/tiktok-photo-sourcer/` | Download TikTok photo posts (boards or references). |
| `.cursor/` | Cursor skill wrappers, rules, hooks, and the `avatar-post-producer` subagent. |
| `BUGS.md` | Tooling failures only. |

## Setup

- Python 3.11+ with Pillow (`python -m pip install pillow`).
- Commands use `python`; use `python3` if that is the interpreter on your machine.
- `FAL_KEY=...` in a repo-root `.env` (gitignored).
- Optional: `gallery-dl` for TikTok/Instagram downloads, `ffmpeg` for clips.

## Definition Of Done For A Post

- Still uses the locked avatar only; the board was not posted.
- Caption copy was approved in chat before rendering and matches the render exactly.
- Any AntiGPT wording comes from `product/antigpt-claim-bank.md`.
- `accounts/antigpt/posts/N/caption.md` has the status and approved copy, and the
  Posts table in `accounts/antigpt/README.md` has the row.

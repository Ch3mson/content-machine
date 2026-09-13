# Content Machine

Docs-first workspace for the **antigpt** account (antigpt.me). Current creative
format: TikTok photo slideshows with the locked avatar, a practical hook, and
short numbered technique slides. Each content slide gets one heading block
and one short explanatory sentence below; keep the top heading brief.

Start with `AGENTS.md`. It routes phrases like `face swap`, `caption this`, and
`hook ideas` to the right skill and script.

Codex owns pipeline development here. See [Codex setup](.codex/README.md),
[folder guidelines](FOLDERS.md), and [pipeline priorities](references/ugc-pipeline.md).
The connected [Notion knowledge base](references/notion.md) holds broader
research; account rules, skills, claims, and production records stay in Git.

Images and videos stay local and are ignored by Git. The post folders on this
Mac still contain the finished media. A fresh clone contains the workflow,
captions, and source records; copy the required media from the production Mac
before generating or editing posts on another machine.

The current [CapCut workflow](references/capcut-slideshow-workflow.md) continually
appends posts to one CapCut timeline in 15-second sections. Preserve earlier
sections. After final approval, archive that post's ordered slide screenshots
for TikTok and its 15-second MP4 for Instagram Reels in `accounts/antigpt/posts/N/`.

## Make the next batch

In Claude Code, open this repo and run:

```text
/make-slideshows 10 new posts
```

In Codex, use `$make-slideshows 10 new posts`. You can also say “continue the
slideshow batch” or “save the approved slideshows”; the workflow resumes from
the post records. If no count is supplied for a new batch, the default is ten.

The [shared skill](references/skills/make-slideshows/SKILL.md) covers new selfie
selection, copy, editable CapCut assembly, HTML review, revisions, and approved
post folders. It inherits the account's Harvard wording, larger purple
highlights, EsDeeKid music, and longer captions without `#AntiGPT`. Final folders
are flat: `01.png`–`05.png`, a separate 15-second `reel.mp4`, and caption files
including `caption.txt` with the title and description. Exact clean sources
stay in `accounts/antigpt/assets/post-sources/N/`. Posts 6–15 are the completed
batch reference. CapCut assembly requires local desktop-control access.

Claude discovery is a project skill in `.claude/skills/make-slideshows/`, per
the [Claude Code skill documentation](https://code.claude.com/docs/en/skills).
`CLAUDE.md` routes shared instructions to `AGENTS.md`; all clients read one
canonical workflow. Start a new session if a newly added skill is not listed.

## Existing Still Production Tools

These create the image assets. The native workflow handles separate text
blocks and ordered exports; the legacy CLI remains a single-block still renderer.

```text
board (someone's study photo)  +  avatar/asian-girl-avatar.jpg
        │
        ▼  python tools/fal/swap_avatar.py <boards>          (fal Seedream edit)
accounts/antigpt/outputs/{stamp}/*.jpg + contact-sheet.jpg
        │  pick one
        ▼  copy the exact selected output image + create caption.md
accounts/antigpt/posts/N/image.jpg
        │  approve copy in chat
        ▼  python tools/fal/caption.py --image ... --text "..."
accounts/antigpt/posts/N/image_caption.jpg  ->  post it
```

## Directory Map

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Router and workspace contract for agents. |
| `CLAUDE.md` + `.claude/skills/` | Claude Code entrypoint and `/make-slideshows` discovery. |
| `FOLDERS.md` | Folder ownership, naming, knowledge retention, and Git guidelines. |
| `.agents/skills/` | Codex skill discovery links to the canonical workflows. |
| `.codex/` | Codex setup and optional UGC pipeline builder agent. |
| `accounts/antigpt/` | The account: hub README, brief, `avatar/`, `boards/`, `posts/`, fonts. |
| `product/` | AntiGPT product brief and claim bank. Read before any product mention. |
| `references/skills/` | Canonical workflows, including make-slideshows and the still producer. |
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
- Copy matches the render exactly. Get approval before rendering unless Benson
  requests complete drafts for review after assembly; final approval gates exports.
- Any AntiGPT wording comes from `product/antigpt-claim-bank.md`.
- `accounts/antigpt/posts/N/caption.md` has the status and approved copy, and the
  Posts table in `accounts/antigpt/README.md` has the row.

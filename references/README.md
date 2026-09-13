# References

Shared materials that inform the account and the skills.

| Path | Purpose |
| --- | --- |
| `notion.md` | Connected knowledge-base map, retrieval, and what stays local. |
| `ugc-pipeline.md` | Pipeline ownership, current capabilities, and next development work. |
| `capcut-slideshow-workflow.md` | Native editing, batch review, export checks, and session recovery. |
| `skills/make-slideshows/` | Slideshow batch workflow shared by Claude Code, Codex, and Cursor. |
| `skills/avatar-post-producer/` | End-to-end avatar post workflow shared by Codex and Cursor. |
| `skills/avatar-face-swap/` | Swap the locked avatar onto composition boards with `tools/fal/swap_avatar.py`. |
| `skills/caption-overlay/` | Render approved copy onto a still with `tools/fal/caption.py`. |
| `skills/hook-idea-extraction/` | Extract reusable hook patterns from reference posts into `hook-ideas/cards/`. |
| `skills/tiktok-photo-sourcing/` | Download TikTok photo posts as boards or references. |
| `skills/stop-slop/` | Vendored writing QA skill for removing AI writing patterns. |
| `skills/graphify-connection-capture/` | Save reasoning connections for the knowledge graph. |
| `hook-ideas/` | Hook inspiration bank: cards, raw inbox, index, reuse ledger. |
| `social-accounts/` | Raw reference posts from other accounts (`{account}/Post {id}/`). |

Codex discovery links live in `.agents/skills/`; Claude Code command links live
in `.claude/skills/`; Cursor wrappers live in `.cursor/skills/`.
Edit the canonical body here, then mirror any frontmatter
change into the Cursor wrapper. See `../FOLDERS.md` before adding new folders.

Broad research belongs in Notion. Keep local material needed by production
and link its source; see `notion.md` before removing any knowledge files.

Do not put runnable scripts here. Scripts belong in `../tools/`.

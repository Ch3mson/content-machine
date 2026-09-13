# Cursor workspace config

Canonical workflows live in `references/skills/` and `AGENTS.md`. This folder
makes them discoverable and runnable in Cursor.

Codex uses the same context through `AGENTS.md` and `.agents/skills/` links;
see [Codex setup](../.codex/README.md). Folder ownership is in
[FOLDERS.md](../FOLDERS.md).

| Path | Purpose |
| --- | --- |
| `rules/agents-router.mdc` | Always-on rule: follow `AGENTS.md`, start tagged skills immediately, approve copy before rendering. |
| `rules/graphify.mdc` | Always-on rule for the graphify knowledge graph (only useful once `graphify` is installed and `graphify-out/` exists). |
| `hooks.json` + `hooks/graphify-session.py` | Session-start hook that surfaces the graph report when `graphify-out/graph.json` exists. |
| `skills/{name}/SKILL.md` | Thin wrappers, one per repo skill (table below). |
| `agents/avatar-post-producer.md` | Project subagent for the still pipeline. Invoke with `/avatar-post-producer ...`. |

## Skills

| Wrapper | Canonical skill | Use |
| --- | --- | --- |
| `skills/make-slideshows/` | `references/skills/make-slideshows/SKILL.md` | Make, review, revise, and save slideshow batches |
| `skills/avatar-post-producer/` | `references/skills/avatar-post-producer/SKILL.md` | Run the full still workflow |
| `skills/avatar-face-swap/` | `references/skills/avatar-face-swap/SKILL.md` | Swap the locked avatar onto boards with fal |
| `skills/caption-overlay/` | `references/skills/caption-overlay/SKILL.md` | Render approved copy onto a still |
| `skills/hook-idea-extraction/` | `references/skills/hook-idea-extraction/SKILL.md` | Pull reusable hook patterns from reference posts |
| `skills/tiktok-photo-sourcing/` | `references/skills/tiktok-photo-sourcing/SKILL.md` | Download TikTok photo posts as boards or references |
| `skills/stop-slop/` | `references/skills/stop-slop/SKILL.md` | Remove AI writing patterns from copy |
| `skills/graphify-connection-capture/` | `references/skills/graphify-connection-capture/SKILL.md` | Save reasoning connections for the graph |

Do not edit skill bodies here. Change `references/skills/{name}/SKILL.md`, then
mirror any frontmatter change into the `.cursor/skills/` wrapper.
The producer agent also delegates its procedure to the canonical producer skill.

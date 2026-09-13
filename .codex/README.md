# Codex workspace setup

Codex reads the root [AGENTS.md](../AGENTS.md) as project instructions.
The account files supply durable production context, and
[FOLDERS.md](../FOLDERS.md) defines where new work belongs.

| Cursor | Codex | Shared content |
| --- | --- | --- |
| `rules/agents-router.mdc` | Root `AGENTS.md` | Routing and workspace rules |
| `.cursor/skills/{name}/SKILL.md` | `.agents/skills/{name}` | `references/skills/{name}/SKILL.md` |
| `.cursor/agents/avatar-post-producer.md` | `$avatar-post-producer` skill | End-to-end still workflow |
| Project agent definitions | `.codex/agents/ugc-pipeline-builder.toml` | Pipeline development context in `references/ugc-pipeline.md` |

The `.agents/skills/` entries are relative directory symlinks into
`references/skills/`. Codex supports these links, so skill bodies and supporting
resources stay together with no duplicate copy to maintain. Preserve symlinks
when cloning this repo. If new skills do not appear, reopen the project/start a
new Codex session. `AGENTS.md` also routes directly to each canonical file.

Examples:

- `$make-slideshows 10 new posts` — native slideshow batch, review, and approved exports
- `$avatar-post-producer make a new post from this board`
- `$avatar-face-swap batch these boards`
- `$caption-overlay add the approved text to post 2`
- `Improve the UGC pipeline using references/ugc-pipeline.md`

Claude Code uses `/make-slideshows` through `.claude/skills/`; both discovery
links resolve to `references/skills/make-slideshows/`. The root `CLAUDE.md`
points to the same shared instructions.

The primary Codex agent owns pipeline development through `AGENTS.md`.
`ugc-pipeline-builder` is an optional custom agent for a delegated development
task when requested. It inherits the parent model, permissions, and available
tools. No project config overrides or background jobs are needed for this setup.

Notion authentication belongs to the user's connected app, not this repo.
Start with [the knowledge map](../references/notion.md) when research is needed.
Cursor hooks are not installed as Codex hooks; optional graph retrieval is
covered by `AGENTS.md` in both tools.

Verified against official docs on 2026-09-13:
[project instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md),
[skill discovery and symlinks](https://learn.chatgpt.com/docs/build-skills), and
[custom agents](https://learn.chatgpt.com/docs/agent-configuration/subagents).

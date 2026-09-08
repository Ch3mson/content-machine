# Cursor workspace config

Cursor-native equivalent of `.opencode/`. Canonical workflows still live in
`references/skills/` and `AGENTS.md`. This folder only makes them discoverable
and runnable in Cursor.

| OpenCode | Cursor |
| --- | --- |
| `.opencode/skills/` | `.cursor/skills/` |
| `AGENTS.md` + OpenCode instructions | `.cursor/rules/` |
| `.opencode/plugins/graphify.js` | `.cursor/hooks/graphify-session.py` |
| `.opencode/plugins/notify.ts` | Cursor built-in notifications |
| `.opencode/plugins/worktree/` | cmux/OpenCode only; not ported |

Do not edit skill bodies here. Change `references/skills/{name}/SKILL.md`.

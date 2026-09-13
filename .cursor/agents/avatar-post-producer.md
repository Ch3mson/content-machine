---
name: avatar-post-producer
description: Produces antigpt avatar stills end to end. Face-swaps the locked avatar onto composition boards with tools/fal/swap_avatar.py, returns the contact sheet, promotes a chosen board to a post folder, and renders an already-approved caption with tools/fal/caption.py. Use proactively when the user asks to swap or put the avatar or "her" onto a board, batch boards, make a new selfie still, or render an approved caption.
model: inherit
---

Read `AGENTS.md`, then load and follow
`references/skills/avatar-post-producer/SKILL.md`.

The canonical workflow is shared with Codex. Keep procedure changes there;
this file only supplies the Cursor agent entrypoint. Respect the scope and
existing approvals passed by the parent conversation.

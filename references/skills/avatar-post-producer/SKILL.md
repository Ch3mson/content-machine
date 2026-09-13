---
name: avatar-post-producer
description: Produce an antigpt avatar still from a composition board through candidate review, selected-image promotion, copy approval, and caption rendering. Use for an end-to-end new post request; use the individual swap or caption skill for a single stage.
---

# Avatar Post Producer

Run the current still workflow using `accounts/antigpt/README.md` and the
canonical skills below. This workflow can run in the main conversation or
through a requested agent; it does not depend on Cursor.

1. Read `references/skills/avatar-face-swap/SKILL.md`. Confirm the locked
   `accounts/antigpt/avatar/asian-girl-avatar.jpg` exists and resolve the requested boards.
   Add source rows for new boards.
2. Run the requested swap batch from the repo root. For more than 12 planned
   fal calls, use `--dry-run` and report the count before starting.
3. Show the contact sheet when one exists and link the individual candidates.
   If the user requested review, let them select the keeper. If they already
   specified a board and post number for a fresh render, honor that scope.
4. When a specific review candidate is chosen, copy that exact image into the
   next unused `posts/N/image.jpg`, create `caption.md` with its board/source,
   and update the Posts table. `swap_avatar.py <board> --post N` generates a
   new image; use it only for a requested fresh render. Respect overwrite rules.
5. Read `references/skills/caption-overlay/SKILL.md` when copy is involved.
   Draft using the account brief, Stop Slop, and the claim bank as applicable.
   Show exact lines in chat and obtain approval before rendering. Existing
   explicit approval remains valid; do not request it again.
6. Save approved wording/line breaks in `caption.md`, render, and inspect the
   output. Keep `image.jpg` and `image_caption.jpg` separate. Any proposed copy
   change needed for fit goes back to the user before rendering changed words.
7. Return the final image, caption text, and paths with the actual status.
   Update hook reuse when applicable. Social publication remains Benson's step
   unless explicitly requested; a completed render is not a posted post.

If approval or a selection is still needed, return the finished work available
so far and identify that specific handoff. Never render placeholder copy or
generate a substitute identity to bypass a missing avatar image.

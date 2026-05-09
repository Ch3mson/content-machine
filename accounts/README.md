# Accounts

Each account folder is a source-of-truth playbook plus post workspaces.

## Quick Navigation

- [Accounts index](INDEX.md): fastest page for ready-to-post packs, flows needing review, concept drafts, and account source-of-truth links.
- [Cross-account post dashboard](../POST_STATUS.md): generated global table of every known post and next action.
- Account dashboards:
  - [athlete-max](athlete-max/post-status.md)
  - [athlete-stories](athlete-stories/post-status.md)
  - [Athlete-user-soccer](Athlete-user-soccer/post-status.md)
  - [makebrainrotvideos](makebrainrotvideos/account-brief.md)

## Folder Contract

Required account files:

- `account-brief.md`: audience, POV, product relationship, open questions.
- `writing.md`: voice, rhythm, banned patterns, copy QA.
- `image.md`: visual system and processing rules.
- `sources.md`: claim risk, approved sources, wording to avoid.
- `presets.md`: optional style presets for repeatable post patterns.

Universal cross-account writing skills live in `../references/skills/`. Use
`../references/skills/angle-variants/SKILL.md` whenever a user asks for 3
variants, angle concepts, or brainstorming from an overall idea. It produces
account-adapted concepts in chat before any slide copy or `flow.md` is written.

Preferred new post folders live under `posts/`:

```text
accounts/{account}/posts/{post-slug}/
```

Each post folder should contain:

- `concept/`: optional research, draft copy, and review notes before approval.
- `flow.md`: slide roles, source images, and final copy.
- `image_preset.json`: optional image sourcing queries.
- `sourced/`: raw sourced photos.
- `process_images.py`: post-specific processing script.
- `processed/`: final rendered slides.

Each account also has a post dashboard and a clean publishing funnel:

```text
accounts/{account}/post-status.md
accounts/{account}/ready-to-post/{post-slug}/
```

Use `post-status.md` to see each post's status, stage, next action, source
workspace, ready pack, and flow. Finished publish packs under `ready-to-post/`
contain only `flow.md` and final `slide_*.png` files. Keep edits in the source
workspace, then refresh the dashboard and publish packs:

```powershell
python tools/post-tracker/update_post_status.py
```

Use `../workflows/workflow-a-new-account.md` for new accounts and
`../workflows/workflow-b-new-post.md` for new posts.

Workflow B shows the full slide-by-slide copy in chat and waits for explicit
approval before final `flow.md`, image sourcing, processing, or PNG rendering.

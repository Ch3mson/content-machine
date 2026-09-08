# antigpt Post Status

Updated: 2026-09-08 (manual; see note below)

## Account Funnel

- Work in `posts/{post-slug}/` for new posts.
- This account does not use a `ready-to-post/` folder (user decision,
  2026-09-08). Post directly from `posts/{post-slug}/processed/`.
- Note: `tools/post-tracker/update_post_status.py` recreates `ready-to-post/`
  for every account. Do not run it for antigpt until it has a per-account
  opt-out, or delete the folder again afterwards.

## Posts

| Post | Status | Stage | Publish from | Next action |
| --- | --- | --- | --- | --- |
| [1-straight-a-hacks](posts/1-straight-a-hacks/) | Done | Rendered, ready to post | [processed/](posts/1-straight-a-hacks/processed/) `slide_01..05.png` + [flow](posts/1-straight-a-hacks/flow.md) caption | Post to Instagram |
| [2-essay-writing-tips](posts/2-essay-writing-tips/) | Done | Rendered, ready to post | [processed/](posts/2-essay-writing-tips/processed/) `slide_01..05.png` + [flow](posts/2-essay-writing-tips/flow.md) caption | Post to Instagram |

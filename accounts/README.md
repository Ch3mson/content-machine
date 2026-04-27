# Accounts

Each account folder is a source-of-truth playbook plus post workspaces.

Required account files:

- `account-brief.md`: audience, POV, product relationship, open questions.
- `writing.md`: voice, rhythm, banned patterns, copy QA.
- `image.md`: visual system and processing rules.
- `sources.md`: claim risk, approved sources, wording to avoid.
- `presets.md`: optional style presets for repeatable post patterns.

Preferred new post folders live under `posts/`:

```text
accounts/{account}/posts/{post-slug}/
```

Each post folder should contain:

- `flow.md`: slide roles, source images, and final copy.
- `image_preset.json`: optional image sourcing queries.
- `sourced/`: raw sourced photos.
- `process_images.py`: post-specific processing script.
- `processed/`: final rendered slides.

Use `../workflows/workflow-a-new-account.md` for new accounts and
`../workflows/workflow-b-new-post.md` for new posts.

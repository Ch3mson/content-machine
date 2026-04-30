# Post Tracker

Updates the post status dashboard and per-account ready-to-post folders.

Run from the workspace root:

```powershell
python tools/post-tracker/update_post_status.py
```

The updater scans account post workspaces, writes:

- `POST_STATUS.md`
- `accounts/{account}/post-status.md`
- `accounts/{account}/ready-to-post/README.md`

For posts classified as `Done`, it also copies a clean publish pack to:

```text
accounts/{account}/ready-to-post/{post-name}/
```

Each publish pack contains only:

- `flow.md`
- `slide_1.png`, `slide_2.png`, etc.

Do not edit from `ready-to-post/`. Edit the original post workspace, rerender if
needed, then rerun the tracker.

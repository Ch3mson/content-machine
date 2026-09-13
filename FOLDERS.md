# Folder System

Use this map when adding or moving files. Prefer an existing home; create a
new folder only when it has a distinct purpose and actual contents.

| Home | What belongs here |
| --- | --- |
| `AGENTS.md` | Shared agent entrypoint, task routing, ownership, essential rules. |
| `CLAUDE.md` + `.claude/skills/` | Claude Code entrypoint and discovery links to canonical repo skills. |
| `README.md` | Human entrypoint, setup, current pipeline, links to these guidelines. |
| `.agents/skills/` | Codex discovery links to the canonical repo skills. |
| `.codex/` | Codex-specific agent definitions and setup notes. |
| `.cursor/` | Cursor-specific wrappers, rules, hooks, and agent entrypoints. |
| `accounts/{account}/` | Account decisions, voice, identity assets, boards, and produced posts. |
| `product/` | Product facts and the approved/caution/blocked claim bank used by production. |
| `references/skills/` | One canonical body per reusable workflow. Tool-specific wrappers point here. |
| `references/hook-ideas/` | Local source captures and hook patterns needed for production; link Notion sources. |
| `references/social-accounts/{creator}/` | Raw third-party reference posts with source provenance. |
| `references/connection-captures/` | Concise reusable connections, created only when there is one to save. |
| `references/notion.md` | Knowledge-base links, retrieval guidance, and known source gaps. |
| `references/ugc-pipeline.md` | Current pipeline capabilities and development priorities. |
| `references/capcut-slideshow-workflow.md` | Approved native CapCut assembly, timing, styling, and verification workflow. |
| `tools/{tool}/` | Runnable utilities and their usage docs. Shared helpers stay beside their callers. |
| `BUGS.md` | Reproduced tooling failures, causes, and fixes. |
| Notion | Broad research, full research material, research-bot output, winning-format research, and cross-channel knowledge. |

## Account layout

`accounts/antigpt/README.md` is the account hub. It owns the current format,
Boards table, and Posts table. `account-brief.md` owns audience and voice.

```text
accounts/antigpt/
  README.md
  account-brief.md
  avatar/asian-girl-avatar.jpg
  assets/fonts/
  assets/study-backgrounds/    # reusable study photos + source index + overview
  assets/post-sources/{N}/     # exact clean sources used by an approved post
  boards/{descriptive-slug}.jpg
  outputs/{timestamp}/          # ignored candidates + contact sheet
  outputs/slideshow-draft/      # mutable files for the shared CapCut project
    timeline.json              # post IDs, ranges, approval/export status
    posts/{N}/                 # each appended draft's copy and clean media
  posts/{N}/
    01.png ... 05.png          # approved TikTok slides captured from CapCut
    reel.mp4                  # same approved edit for Instagram Reels
    caption.md                # approval/status, sources, exact copy, export details
    caption.txt               # plain-text TITLE + DESCRIPTION for quick copy/paste
    captions.srt              # optional timed text import for CapCut
    image.jpg                 # clean still for the legacy single-image format
    image_caption.jpg         # captioned still for the legacy format
```

- Use descriptive lowercase hyphenated names for new boards and documents.
  Dated captures use `YYYY-MM-DD-source-slug.md`. Preserve external creator
  names and post IDs where they identify a source.
- Use the next unused integer for a post directory. Never renumber old posts.
  Retain existing reference folders such as `Post {id}/`; new guidelines do
  not require renaming the archive.
- Record the source URL, creator/post ID, and selected slide when available.
  If a source is unknown, say so; do not invent provenance.
- Keep third-party boards separate from avatar outputs. Review candidates
  stay in `outputs/`; only a chosen still enters `posts/`.
- Reusable study photos belong in `assets/study-backgrounds/`, with a source
  pin URL for every file. Choose from that library and copy the selected
  backgrounds into `assets/post-sources/N/` when archiving an approved video. Keep original source
  photos unchanged; the contact sheet is only an overview.
- When a specific review image is selected, preserve those exact bytes on
  promotion. `swap_avatar.py --post N` generates a fresh image; it is not a
  copy operation.
- Treat `posts/N/caption.md` as the detailed production record and keep the
  hub's Posts row consistent. Mark Posted only after confirmed publication;
  add the live URL/date when supplied.
- Keep `posts/N/caption.txt` synchronized with the posting title and description
  in `caption.md`. Use clear TITLE and DESCRIPTION labels, actual line breaks,
  and only the copy the user should paste into the platform.
- Continually append new posts to the same native CapCut timeline in separate
  15-second sections; preserve earlier posts. Work in
  `outputs/slideshow-draft/posts/N/` until final approval after modifications.
  Record reserved post IDs and ranges in `outputs/slideshow-draft/timeline.json`.
  Then save ordered canvas-only screenshots as `posts/N/01.png`–`05.png`
  beside `posts/N/reel.mp4`; preserve clean sources in `assets/post-sources/N/`.
- Post folders are flat (Benson, 2026-09-13): finished PNGs, reel, and caption
  files share one level. Do not create nested image or clean-source folders
  inside a post. Keep original sources in the asset library and working media
  paths stable for CapCut; record the source archive in `caption.md`.
- Record the shared project name/path and the post's timeline range in
  `caption.md`, along with approval and export details. Export each approved
  section as its own 15-second video; keep the accumulated timeline intact.
  Exported images/video preserve past posts even when the shared timeline changes.
- Keep existing unfinished post folders and their media paths intact. Complete
  an existing draft in its own folder; do not duplicate or relabel it as ready
  simply because clean backgrounds or a CapCut project exist.

## Knowledge and memory

Keep the instructions needed to run this repo in Git: skills, account voice,
identity rules, claims, post records, and tool docs. Use Notion for the broad
research library. See [Notion knowledge](references/notion.md).

Image/video media stays on the local machine and is ignored by Git (Benson,
2026-09-14). This includes avatar photos, boards, source backgrounds, reference
screenshots, finished slide PNGs, and reels. Keep captions, source URLs/hashes,
and production decisions tracked. Cloning the repo does not restore the media;
copy the required files from the production machine before continuing there.

A useful research finding becomes a local operating rule only when it is
adopted for this account. Save the concise decision in its owning file and link
the source; do not mirror the whole knowledge base into Markdown. Existing
local hook cards and source captures remain until a replacement is verified
and their callers have been updated. A Notion connection alone is not proof
that a local file has a complete remote copy.

## Changes and Git

- Keep reusable production instructions out of editor-specific folders. Edit
  the canonical skill; update Cursor wrapper metadata if its trigger changes.
  Add matching relative discovery links under `.agents/skills/` and, for
  Claude commands, `.claude/skills/`. Preserve directory symlinks in Git.
- When moving a file, update its callers and nearest README in the same change.
  Do not add competing status trackers, generic knowledge dumps, or dated
  backup folders. Git preserves history.
- Keep `.env`, credentials, cookies, local tool state, review batches, caches,
  and throwaway renders out of Git. Use `/tmp` for test renders.
- Keep image/video files local, including selected identity/board/post assets.
  Do not force-add ignored media. Commit source records and captions, not the
  binary images/videos. Files already in older Git history are not purged by
  ignore rules; avoid rewriting published history just to change this policy.
- Before a requested push, inspect the whole staged change (including prior
  cleanup), check for secrets and broken active references, and run relevant
  local checks. Use a normal push; preserve existing work and history.

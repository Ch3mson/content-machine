# Folder System

Use this map when adding or moving files. Prefer an existing home; create a
new folder only when it has a distinct purpose and actual contents.

| Home | What belongs here |
| --- | --- |
| `AGENTS.md` | Shared agent entrypoint, task routing, ownership, essential rules. |
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
  boards/{descriptive-slug}.jpg
  outputs/{timestamp}/          # ignored candidates + contact sheet
  posts/{N}/
    image.jpg                 # clean production still
    image_caption.jpg         # approved words rendered onto the still
    caption.md                # status, board/source, exact approved copy
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
- When a specific review image is selected, preserve those exact bytes on
  promotion. `swap_avatar.py --post N` generates a fresh image; it is not a
  copy operation.
- Treat `posts/N/caption.md` as the detailed production record and keep the
  hub's Posts row consistent. Mark Posted only after confirmed publication;
  add the live URL/date when supplied.

## Knowledge and memory

Keep the instructions needed to run this repo in Git: skills, account voice,
identity rules, claims, post records, and tool docs. Use Notion for the broad
research library. See [Notion knowledge](references/notion.md).

A useful research finding becomes a local operating rule only when it is
adopted for this account. Save the concise decision in its owning file and link
the source; do not mirror the whole knowledge base into Markdown. Existing
local hook cards and source captures remain until a replacement is verified
and their callers have been updated. A Notion connection alone is not proof
that a local file has a complete remote copy.

## Changes and Git

- Keep reusable production instructions out of editor-specific folders. Edit
  the canonical skill; update Cursor wrapper metadata if its trigger changes.
  Add the matching relative link under `.agents/skills/` for a new repo skill.
- When moving a file, update its callers and nearest README in the same change.
  Do not add competing status trackers, generic knowledge dumps, or dated
  backup folders. Git preserves history.
- Keep `.env`, credentials, cookies, local tool state, review batches, caches,
  and throwaway renders out of Git. Use `/tmp` for test renders.
- Commit selected identity/board/post assets and source captures required by
  the workflow. Avoid adding unrelated downloads or duplicate exports.
- Before a requested push, inspect the whole staged change (including prior
  cleanup), check for secrets and broken active references, and run relevant
  local checks. Use a normal push; preserve existing work and history.

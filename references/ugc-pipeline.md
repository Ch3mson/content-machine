# UGC Pipeline

Owner: Codex for pipeline development and maintenance. Benson chooses creative
direction, approves copy, and publishes. Current account:
[`accounts/antigpt/`](../accounts/antigpt/README.md).

## Current production path

| Stage | Implementation | Output / handoff |
| --- | --- | --- |
| Research | Notion + local hook extraction skills | Linked source and a pattern adapted to account voice |
| Source boards | Local images or TikTok photo sourcer | `boards/` image + account Boards row |
| Generate | `tools/fal/swap_avatar.py` | Locked avatar on board; candidates + contact sheet in `review/` |
| Select | User chooses a candidate, or requests a direct post render | Exact selected still copied, or a fresh `--post N` render, into `posts/N/image.jpg` |
| Approve copy | Caption skill + account brief + claim bank when needed | Exact lines approved in chat and saved in `caption.md` |
| Render | `tools/fal/caption.py` | `image_caption.jpg`, preserving the clean still |
| Deliver | Show final image and caption text | Benson posts natively; update Posted status only after confirmation |
| Learn | Supplied feedback/results | Voice → brief; format → hub; hook reuse → ledger; failures → `BUGS.md` |

The still workflow is live. `tools/fal/video.py` exists as an optional clip
utility; a repeatable video format, publishing integration, and automated
performance ingestion have not been built. No scheduled jobs are configured
by this project setup.

## Development priorities

These are concrete next improvements, not claims of completed automation.
Choose the one that serves the user's next request instead of building all of
them just because this list exists.

1. **Preserve selected candidates.** Add a local promotion command that copies
   the chosen review image exactly, records its board/run, and protects existing
   posts. Today `--post N` spends a new generation call and can change the image;
   exact promotion is manual.
2. **Record batch provenance.** Save source board, anchor identity, prompt,
   model/settings, result paths, failures, and request IDs with each run. This
   would support selective retries and explain which input produced a keeper.
3. **Make the post handoff reliable.** Keep `caption.md` and the hub in sync,
   validate required assets, and package the approved image/caption for phone
   posting. Preserve manual line breaks and never invent approval or status.
4. **Close the feedback loop.** Record actual supplied post URLs and results,
   link them to hooks/boards, and use that evidence to choose the next batch.
   Inspect the existing Notion logs before creating another tracker.

## How to develop here

- Start from [the folder system](../FOLDERS.md) and the smallest relevant skill
  and tool. Keep the current format working while changing a stage.
- Use [Notion research](notion.md) when a creative or workflow decision needs
  evidence. Adopt specific findings; do not turn another bot's full playbook
  into always-loaded instructions.
- Use syntax/import checks, CLI help, dry runs, and temporary local fixtures
  for routine verification. Test observable invariants when changing output
  handling, identity/reference order, overwrite behavior, or copy rendering.
- A dry run does not verify the fal endpoint or visual quality. State when a
  live generation was not exercised, and inspect images when it is exercised.
- Keep this file current when capabilities change. Record voice preferences
  in the account brief, not in this development list.

# UGC Pipeline

Owner: Codex for pipeline development and maintenance. Benson chooses creative
direction, approves copy, and publishes. Current account:
[`accounts/antigpt/`](../accounts/antigpt/README.md).

## Current production path

Start slideshow production with
[`make-slideshows`](skills/make-slideshows/SKILL.md): `/make-slideshows` in
Claude Code or `$make-slideshows` in Codex. The shared procedure covers source
selection, copy, native CapCut assembly, HTML review, revisions, final exports,
and recovery from post records in a later session. The table below describes
the still tools used when producing image assets for that flow.

| Stage | Implementation | Output / handoff |
| --- | --- | --- |
| Research | Notion + local hook extraction skills | Linked source and a pattern adapted to account voice |
| Source boards | Local images or TikTok photo sourcer | `boards/` image + account Boards row |
| Generate | `tools/fal/swap_avatar.py` | Locked avatar on board; candidates + contact sheet in `outputs/` |
| Select | User chooses a candidate, or requests a direct post render | Exact selected still copied, or a fresh `--post N` render, into `posts/N/image.jpg` |
| Approve copy | Caption skill + account brief + claim bank when needed | Exact lines approved in chat and saved in `caption.md` |
| Render | `tools/fal/caption.py` | `image_caption.jpg`, preserving the clean still |
| Deliver | Show final image and caption text | Benson posts natively; update Posted status only after confirmation |
| Learn | Supplied feedback/results | Voice → brief; format → hub; hook reuse → ledger; failures → `BUGS.md` |

Creative direction is TikTok photo slideshows (Benson, 2026-09-13): a hook and
short technique slides with at most two text blocks each. The existing CLI
tools produce still assets and one text block per render. Native CapCut
assembly was verified for post 3: five backgrounds, ten editable top/bottom
text layers, 9:16, and purple highlights. The approved default is now three
seconds per slide, or 15 seconds for five slides. Follow the
[CapCut slideshow workflow](capcut-slideshow-workflow.md) for repeat production.
Continually append new posts to one native CapCut timeline in 15-second sections,
preserving earlier posts. Keep draft copy/media by reserved post ID and record
each section's time range; Benson reviews completed drafts together.
After final approval following modifications, the required package is ordered
CapCut slide screenshots as `posts/N/01.png`–`05.png` for TikTok, beside
`posts/N/reel.mp4` for Instagram Reels. Keep the post folder flat with the
approval/copy record and `caption.txt` containing the posting TITLE and DESCRIPTION.
Preserve clean backgrounds separately in `assets/post-sources/N/`.
Export each approved section separately and retain the timeline. This handoff
is now the default. Posts 6–15 demonstrate the completed batch: 50 native
1080 × 1920 PNGs, ten separate 15-second EsDeeKid reels, clean sources, and
copy-ready title/descriptions are exported and verified. Their native timeline
sections span 45–195 seconds, preserving posts 3–5 at 0–45 seconds.
Independent text-block placement and highlighted backgrounds remain gaps in
the CLI renderer; reusable automated CapCut assembly/export is not yet built.

The still workflow is live. `tools/fal/video.py` exists as an optional clip
utility. Native slideshow review and both exports are verified procedures;
headless automatic dual-format export,
publishing integration, and performance ingestion have not been built. No scheduled jobs are configured
by this project setup.

## Development priorities

These are concrete next improvements, not claims of completed automation.
Choose the one that serves the user's next request instead of building all of
them just because this list exists.

1. **Preserve selected candidates.** Add a local promotion command that copies
   the chosen review image exactly, records its board/run, and protects existing
   posts. Today `--post N` spends a new generation call and can change the image;
   exact promotion is manual.
2. **Record batch provenance.** Save source board, avatar identity, prompt,
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

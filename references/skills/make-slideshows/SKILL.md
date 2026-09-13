---
name: make-slideshows
description: Make or continue antigpt TikTok photo slideshows and matching Instagram Reels, from locked-avatar selfies and copy through native CapCut assembly, HTML review, revisions, and approved post folders. Use for make-slideshows, another slideshow batch, or saving reviewed slideshows.
---

# Make Slideshows

Run the account's established slideshow workflow in the current conversation.
All paths below are relative to the repository root. Honor the user's current
count, topics, selected selfies, revisions, and existing approvals.

## Start or resume

1. Read `AGENTS.md`, `FOLDERS.md`, `accounts/antigpt/README.md`, and
   `accounts/antigpt/account-brief.md`. Read
   `references/capcut-slideshow-workflow.md` for native assembly and batch
   review/export details. These files own the current rules; older examples
   do not override newer feedback.
2. Inspect the hub's Posts and Working timeline tables, relevant
   `posts/N/caption.md` records, and any
   `accounts/antigpt/outputs/slideshow-draft/timeline.json` and per-post
   `draft.json` files. Resume the requested draft at its next unfinished stage.
   Do not regenerate approved selfies, redraft approved copy, or repeat completed
   exports merely because the conversation is new.
3. For a new batch, use the requested count; if none is given or established
   in context, use ten, matching the latest batch. Allocate IDs above the
   highest existing or reserved ID, including IDs in the hub, and append at
   the verified current timeline end. Never fill historical ID gaps or assume
   the post number determines its start time. Reconcile conflicting records
   before changing the affected timeline section.

The workflow is an agent procedure, not a headless CapCut renderer. Native
assembly needs local CapCut and a supported desktop-control tool. Use the
current environment's browser/computer-use instructions; do not depend on a
previous session's tool handles, screen coordinates, or `/tmp` scripts. If
desktop access is unavailable, finish the independent source/copy preparation
and record the specific assembly step that needs that access. Do not substitute
a claimed native export or patch the live project behind CapCut.

Image/video files are local-only and Git-ignored. Keep exports and exact clean
sources at their documented paths, but commit only captions, source records,
and workflow/code changes. On a fresh clone, verify the required local media
exists; restore it from the production machine rather than claiming the clone
contains it or generating a replacement for the locked avatar.

## Selfies and copy

4. Use the user's chosen, approved selfie batch when available. Otherwise
   review the latest approved selfies for framing, lighting, expression, and
   phone-photo feel; source enough varied composition boards and follow
   `references/skills/avatar-face-swap/SKILL.md`. The locked avatar is Figure 1,
   the board is Figure 2. Strip source text/watermarks. Show new candidates as
   a contact sheet for selection; continue other preparation while waiting.
   Copy each selected render's exact bytes into stable draft media paths.
   Do not rerun `--post N` to promote a chosen image: that generates again.
5. Read `references/notion.md` and retrieve the relevant saved writing examples
   before drafting. Use `references/skills/stop-slop/SKILL.md` for copy and
   the product brief/claim bank for the CTA. If remote examples cannot be
   retrieved, say so and use the account brief and approved local post copy;
   do not claim to have read the missing examples.
6. Create five slides per post: selfie hook, three numbered techniques, CTA.
   Favor practical AI research, GPT outlining, and drafting from source notes.
   Keep headings brief and the separate lower block slightly more explanatory.
   Harvard is already confirmed for this account; use the account's Harvard
   hook phrasing without asking for the credential again. Vary the topics and
   prompts from previous posts; do not just reskin the last ten hooks.
7. Draft the posting title and longer Instagram/TikTok description alongside
   the slides. Save `caption.txt` with TITLE and DESCRIPTION labels, useful
   short paragraphs, at most five relevant hashtags, and no `#AntiGPT`.
   Keep it synchronized with `caption.md`.
8. Preserve the approval mode in `AGENTS.md`: exact copy goes in chat before
   rendering unless the user requests assembled drafts to review. A request
   to repeat this batch flow means prepare complete drafts for review, as in
   the approved posts 6–15 flow. Approval of existing wording or selfies
   carries forward; final review applies to the finished version.

## Assemble and review

9. Prepare one working folder per reserved post under
   `accounts/antigpt/outputs/slideshow-draft/posts/N/`. Record exact copy and
   line breaks, selected sources/hashes, music, timeline range, and current
   stage. Update the hub when reserving the IDs so a future session can find
   them even if ignored working files are missing.
10. Follow the native workflow: one shared timeline, five three-second slides
    per post, 9:16, ten editable text blocks. Use the larger approved purple
    highlight style, dim study backgrounds, and the white CTA logo. Adjust
    placement for each face. Keep the original EsDeeKid source cut and volume
    for every post. Keep CapCut open and preserve all earlier sections.
11. Inspect every slide in CapCut, then create or update a local HTML review
    page containing all five slide previews, a separate 15-second video with
    music, and the title/description for each post. Use the current reviewed
    native export for these previews; prevent stale browser caching after
    revisions. See the batch review section of the workflow for paths and
    server instructions.
12. Show the assembled batch, apply requested revisions, and get final approval
    of that version. A request such as “save all of them to the posts folders”
    after review authorizes the final local exports; do not ask again. Do not
    interpret approval of one sample, selfie, or color as approval of the batch.

## Save and verify

13. After approval, capture five full-resolution native CapCut PNGs and export
    each post's own 15-second reel into its reserved `posts/N/` folder. Save
    `01.png`–`05.png` directly beside `reel.mp4` and the caption files. Keep the
    folder flat; archive exact clean sources in
    `accounts/antigpt/assets/post-sources/N/`, outside the posting folder. Never deliver the
    accumulated timeline as an individual post or replace native PNGs with
    HTML preview thumbnails. Existing drafts are completed in place.
14. Verify ordered PNGs, image/video dimensions, complete copy, music, all
    five slide boundaries, and 15-second video duration. Inspect the saved
    images and play the videos. Confirm the earlier approved post files and
    timeline sections remain intact. Record actual checks, approval, native
    project/range, sources, and export paths in `caption.md`.
15. Synchronize the hub, working records, and `caption.txt`. Mark complete
    packages **Ready, not posted**; Benson publishes. Return the post-folder
    links and the actual completion status. An HTML page with draft previews
    is review progress, not proof that the permanent folders are complete.

When interrupted, write the completed stage, remaining work, exact approval
scope, stable media paths, and current timeline range in the existing records.
Keep adopted feedback in the account brief, operational discoveries in the
CapCut workflow, and reusable code in `tools/`. Neither this chat nor ignored
outputs should be the only place a future session can learn how to continue.

# CapCut slideshow workflow

Benson approved this production flow on 2026-09-13 and asked to preserve it as
`/make-slideshows`. Start with the
[batch skill](skills/make-slideshows/SKILL.md). Posts 6–15 are the latest
completed batch reference; post 3 is the original style reference.
Account voice and styling decisions live in
[`account-brief.md`](../accounts/antigpt/account-brief.md).

## Default post

- Five slides: one Asian girl avatar selfie hook, three short numbered tips,
  then a CTA that follows naturally from the tips.
- **Three seconds per slide; 15 seconds total.** This replaces the initial
  five-second timing.
- **1080 × 1920, 9:16.** Fill the vertical canvas with each background.
- At most two editable text layers per slide: a short heading near the top and
  one slightly fuller sentence below. Latest feedback keeps the heading brief
  and allows more explanation in the lower block (start around 10–18 words,
  then check readability). Preserve approved words and manual line breaks.
- Every text block uses **#552082 dark purple** on an enabled **#E9D5FF light
  purple highlight**, full opacity, 14% corner rounding, 10% width padding,
  and 8% height padding. Use the latest approved posts 6–15 text scale below.
- Use TikTok Sans Bold. Check the preview for wrapping, readable size, and
  space around the face and important objects.
- Hook-only adjustment (Benson, 2026-09-13): slightly larger text, with both
  blocks slightly closer to the center. New draft reference: heading size 9.25
  and explanation size 7.1. After the final downward nudge requested by Benson,
  their centers are approximately 18% and 73% of canvas height. Keep the
  avatar's face clear. Later feedback for posts 6–15 increases every text
  block to 110% scale, including tips and CTA; keep their separate positions.
- Continually append to the same native CapCut timeline (Benson, 2026-09-13).
  Each post occupies 15 seconds: 0–15, 15–30, 30–45, then 45–60, and so on.
  Preserve earlier sections so Benson can review finished drafts together.
  New sections get their own photos, copy, positioning, music, and CTA logo.
- After Benson approves the finished version following modifications, save
  both ordered slide images for TikTok and an MP4 for Instagram Reels in
  `accounts/antigpt/posts/N/`. This is standing authorization to capture and
  export that approved version; no separate export permission is needed.

## Produce the next post

1. Read the account brief and relevant Notion writing examples. Use
   @sophia.study as the main writing reference. Draft a hook, three concise
   tips, and a connected CTA. For the essay-speed angle, the approved pattern
   is AI research → GPT outline → drafting from notes → AntiGPT wording CTA.
   Read the product claim bank before writing product copy.
2. Show the exact copy in chat and get approval unless Benson requests complete
   drafts to review after assembly, as with the appended batch on 2026-09-13.
   That request authorizes rendering draft copy in the working timeline. Final
   visual approval still gates permanent exports. Keep each tip to a numbered
   title plus a short explanation, rather than paragraphs.
3. Choose an approved avatar selfie for the hook. Copy the selected image
   exactly; do not generate it again. For later slides, rotate study-background
   images and combinations. Black backgrounds are acceptable during assembly
   when requested, as in post 3.
   Rotate the hook selfie when the previous one was already used. Slightly dim
   the later photo backgrounds while keeping the hook and text at full opacity.
   Benson approved 80% photo opacity over a black canvas on slides 2–5.
   Place the white AntiGPT logo below the CTA explanation as its own overlay.
4. When sourcing backgrounds on Pinterest, search `study aesthetic` and favor
   varied desks, notebooks, cafés, libraries, and lighting. Preview the actual
   images. If Benson asks to watch and approve, keep the browser visible and
   pause on each batch before saving it. Do not count unapproved candidates as
   part of the saved library.
5. Keep reusable study backgrounds under
   `accounts/antigpt/assets/study-backgrounds/`, with descriptive filenames and
   source pin URLs. These backgrounds are separate from `boards/`, which holds
   photos used for avatar face swaps. Avoid introducing another person's face
   into the account. Use `accounts/antigpt/outputs/slideshow-draft/posts/N/` for
   each new draft's media and copy; record its reserved post ID and range in
   `outputs/slideshow-draft/timeline.json`. Use distinct basenames such as
   `p04-01-selfie.jpg` across posts so media relinking cannot match the wrong
   image. Keep imported paths stable while editing.
6. Append the new section at the current timeline end, with five background
   clips, five heading clips, five explanation clips, and a CTA logo. Keep
   the existing tracks and earlier sections intact. Align the new clips at
   start + 0, 3, 6, 9, and 12 seconds, ending at start + 15. Preserve the approved
   music template in the new section unless Benson asks for different music.
   Latest correction: retain the original EsDeeKid beat for all posts, using
   its original 0–15-second source cut in every 15-second post section. Benson
   rejected the alternate music selections after review.
   Adjust text positioning for the new photos; keep text editable and retain
   the approved highlight style on every text block.
7. Check every slide in CapCut: vertical framing, wrapping, highlights,
   top/bottom placement, complete copy, and three-second timing. Check that
   the media and font paths resolve. Show the result, apply Benson's requested
   modifications, and wait for approval of the finished version. Approval of
   copy or a style sample alone is not approval of the complete post.
8. After final approval, archive each section into its reserved `posts/N/`
   folder. Export that section's five frames and its own 15-second MP4; keep
   the accumulated timeline intact. If revising an existing unfinished post,
   complete its existing folder rather than creating a duplicate.

## Approved post package

```text
accounts/antigpt/posts/N/
  01.png ... 05.png           # finished TikTok slides, including all text
  reel.mp4                   # Instagram Reels version of the same edit
  caption.md                 # approval, exact copy, sources, timing, verification
  caption.txt                # copy-ready TITLE and DESCRIPTION for posting
  captions.srt               # optional timed text helper
```

Keep this folder flat. Archive exact clean backgrounds and any source logo
under `accounts/antigpt/assets/post-sources/N/`, outside the post folder, and
record that path in `caption.md`. This replaces nested image/source folders
following Benson's flattening request on 2026-09-13.

- Screenshot each finished slide from the CapCut preview, capturing only the
  vertical canvas. Include its approved text and highlights; exclude editor UI,
  pointer, selection outlines, and transform handles. Save PNGs in slide order.
  Use CapCut's full-resolution frame snapshot if available; otherwise capture
  the largest clean preview and record its actual dimensions. Do not label a
  smaller screenshot as a 1080 × 1920 render.
- Export the approved post's range from CapCut as `reel.mp4`, targeting
  1080 × 1920, with the agreed timing. For the default five-slide post this is
  15 seconds. These two outputs serve different uploads: images for TikTok,
  video for Instagram Reels.
  Each post folder must contain only its own range: post 4 is 15–30s and post 5
  is 30–45s. If a full CapCut master was already rendered, keep it in ignored
  working outputs and extract frame-accurate 15-second sections for the post
  packages. Verify 450 frames at 30 fps and check both ends of every slide.
- Inspect every saved image and play the MP4. Check that slide order, wording,
  positioning, framing, colors, and timing match the approved CapCut version.
- Preserve the exact clean backgrounds in `assets/post-sources/N/`. Record final approval,
  capture/export date, project name/path, copy, sources, and actual image/video
  dimensions in `caption.md`; update the hub's Posts row.
- An approved and exported package is **Ready, not posted** until Benson
  confirms publication. Existing unfinished post folders remain drafts; their
  clean backgrounds do not count as finished TikTok slide images.

## Batch assembly and review

The ten-post run on 2026-09-13 verified 50 slides, 100 editable text blocks,
ten CTA logos, and ten separate music sections. Its post records, including
[`posts/6/caption.md`](../accounts/antigpt/posts/6/caption.md), preserve copy,
source hashes, music identity, approval, and export verification. They are
durable examples; the ignored review page and working JSON are optional
resumption aids, not the only copy of the workflow.

For each draft, keep `posts/N/draft.json` under
`accounts/antigpt/outputs/slideshow-draft/`. Record post ID, status, start/end
seconds, title, description, and five ordered slide records. Each slide needs
its source path/URL, exact clean-source SHA-256, stable working path, heading,
explanation, framing, and brightness treatment. Record the music source cut,
volume, native project, and approval scope too. The previous run's
`next-ten-copy.json` is a combined view of the same per-post information; use
the existing structure when resuming rather than creating a competing tracker.

For efficient native import, the verified batch used uniquely named
three-second background clips (`p06-01.mp4`, etc.), plus separate SRT imports
for headings and explanations. Optional FFmpeg preparation may crop/scale
backgrounds to 1080 × 1920 and dim slides 2–5 to 80% brightness. Keep exact
clean images separately; if dimming is baked into the temporary background
clip, do not also reduce native opacity. Text and the CTA logo remain native
editable overlays, not baked into these background clips. Use global timeline
times for SRT entries and preserve existing caption tracks when importing.
Verify the resulting start/end positions in CapCut rather than assuming the
importer preserved them. The legacy caption CLI does not produce this layout.

Use these verified values as starting points, then inspect the actual canvas:

| Text layer | Native font size | Scale | Center from canvas top |
| --- | --- | --- | --- |
| Hook heading | 9.25 | 110% | About 18%; move for the face |
| Hook explanation | 7.1 | 110% | About 73% |
| Tip / CTA heading | 8.5 | 110% | About 29% |
| Tip / CTA explanation | 6.5 | 110% | About 65% |

Posts 8 and 14 needed their hook heading near 42% to avoid covering faces.
That is a composition adjustment, not a new position for all hook slides.
Native size units depend on the project; copying a recent approved text layer
and inspecting the preview is more reliable than interpreting them as pixels.

Duplicate the original EsDeeKid audio section through the editor. Source title:
`【FREE BEAT】“脏” jerk EsDeeKid x Fakemink x Yhpojj`; CapCut music ID
`7642550205040183330`. Every post uses source 0–15 seconds, native volume 1.0,
aligned to its own timeline start. Do not take source 15–30 seconds for the
second post or choose a different track with a similar genre/name. Cached
audio paths are machine-specific; inspect the existing native material when
needed. Keep the timeline tracks editable after assembly.

Build the HTML review page inside `outputs/slideshow-draft/`. Each post card
must show its post ID/title, five ordered slide previews, its own 15-second
video with music, and copy-ready title/description. Render previews from the
actual current CapCut export. A combined export may be kept here and split
at exact frame boundaries; calculate offsets relative to that export's start,
not zero on the full timeline. The previous batch's master covered 45–195s,
so post 6 began at offset 0 in that file despite starting at 45s in CapCut.
JPEG preview frames are sufficient for the HTML page; native PNGs are still
required for the final post package. Replace cache versions after revisions
so the browser cannot play an earlier video with rejected music or old copy.

Serve from the repo root using an available local port; reuse an existing
correct server rather than starting duplicates:

```bash
python3 -m http.server 8765 --bind 127.0.0.1 --directory accounts/antigpt/outputs/slideshow-draft
```

Open the actual page URL in the available browser. The previous page was
`http://127.0.0.1:8765/next-ten-review.html`; use a descriptive name for a new
batch. The HTML references files on disk, it does not contain the full post
packages. After approval, verify and promote the assets into `posts/N/` even
if the preview page already works. Label preview and final archive status
accurately.

## Recover in a future session

Read the account hub and the affected post records before editing. At the end
of the verified batch, posts 3–15 occupied 0–195 seconds and the next new ID
was 16. This is a historical checkpoint, not a permanent allocation rule:
derive current IDs/ranges from the hub, existing folders, and actual project.
Never reuse deleted IDs 1 or 2 merely because those directories are absent.

The shared native project on Benson's Mac was:
`~/Movies/CapCut/User Data/Projects/com.lveditor.draft/AntiGPT - Essay Writing with AI`.
Confirm the project in CapCut; read-only inspection of `draft_info.json` can
check timeline duration, clip ranges, text styles, audio, and source paths.
Do not write that live JSON. Desktop-control element IDs and coordinates
expire; inspect the current editor rather than replaying old session handles.

Ignored `outputs/`, `/tmp` helpers, preview servers, and browser tabs may be
gone in a new context or clone. Reconstruct missing working metadata from
the hub and `posts/N/caption.md`; approved clean sources are in `assets/post-sources/N/` and
finished native images/videos remain in the post folders. If native imported
media paths are missing, restore the exact corresponding source files and
relink through CapCut. Image/video media is now Git-ignored, including the
avatar, clean source archive, and finished exports; those files must be copied
from the production machine when setting up a fresh clone. A Git checkout also
does not restore the external CapCut project or its cached audio. Inspect what is available before claiming
the editable timeline was restored.

Before stopping midway, update the existing draft record and the hub's row
with the completed stage, remaining actions, approval scope, stable paths,
and reserved range. For approval or source decisions that must survive loss
of ignored files, save them in `posts/N/caption.md` as a draft record. Only
final approved media go directly into `01.png`–`05.png` and `reel.mp4`. Reuse that same folder
on resumption, and carry prior explicit approvals forward.

## Native project handling

The shared working project is currently **AntiGPT - Essay Writing with AI**, linked from
[`posts/3/caption.md`](../accounts/antigpt/posts/3/caption.md). Its backgrounds
are clean source files; each post's ten text blocks live in the native CapCut project.
An optional `captions.srt` must use the same slide timing, but does not replace
the native two-block layout.

The live project accumulates posts. Record the exact time range in each post's
notes; the project name alone does not identify its section. Keep prior media
paths stable and do not replace or trim earlier sections when appending or
exporting. Approved `01.png`–`05.png` and `reel.mp4` files remain the permanent handoff.

Keep CapCut open and use its editor controls for adjustments. Benson explicitly
asked on 2026-09-13 to stop closing and reopening it during editing. The native
file procedure below is only for a later explicitly requested offline recovery;
it is not permission to quit CapCut as part of this workflow.
Never modify a live draft file behind the app. For authorized offline native draft edits, first save
and quit CapCut, wait for the app process to exit, and back up the affected
files outside the repo. Otherwise autosave can overwrite the edit. Preserve
material IDs, approved text, styling, and media paths. Update the main draft,
timeline copies, and project duration metadata consistently, then reopen and
verify in CapCut. The approved highlight uses `check_flag & 16`; assigning its
color without enabling that flag does not display the background.

CapCut reports decoded photo dimensions rounded up to even pixels (for example,
the 986 × 1307 research JPEG imports as 986 × 1308). Use the dimensions from a
native import when replacing material metadata; mismatches can trigger a missing
media dialog even when the file exists. Photo material duration is separate from
the three-second timeline segment duration. Preserve the native import values.
If Computer Use captures only the floating EditPilot button, clicking that
button can expose the main editor; then close its side panel to restore the
timeline space.

Native assembly, styling, and both exports have been verified for posts 3–15.
Use the player menu → **Export still frames** for each slide: 1080P, PNG,
ordered filename, `posts/N/`, and Import project off. This produces
1080 × 1920 images without editor UI. Seek 0.5 seconds into each slide, e.g.
post start + 0.5, 3.5, 6.5, 9.5, and 12.5 seconds, and confirm the time before
capturing. The batch can export to a working capture directory with unique
`pNN-SS.png` names and then copy exact bytes to the final ordered filenames.
Raise/focus the main editor when its player menu closes unexpectedly; inspect
fresh UI state before retrying. In the destination dialog, entering the exact
path is more reliable than clicking a virtualized folder row. Confirm where
the resulting file was actually saved.

Export video as H.264, MP4, 1080P,
30 fps to `posts/N/reel.mp4`; preserve user-added music and turn cloud sync off
for a local-only export. Mark only the post's in/out range. For a batch master,
split by decoded frames and re-encode as needed; stream-copy cuts can land on
the wrong keyframe. Check 450 frames, 15 seconds, 1080 × 1920, 30 fps, and an
audio stream for every saved reel. Listen to confirm the actual approved music.
Inspect frames 0/89, 90/179, 180/269, 270/359, and 360/449 against the five
native PNGs. This catches neighboring slides leaking across a range boundary.
Allow normal compression differences; compressed video pixels need not equal
the native PNG bytes. Compare clean-source and copied-review hashes exactly.

Posts 6–15 passed these checks for all 50 PNGs and ten reels. Record completed
checks in each post's `caption.md`, with the actual approval quote/date and
project range; do not treat an old batch's verification as evidence for a new
one. A reusable headless assembly/export utility has not been built: the skill
orchestrates this native editor procedure with the current environment's tools.

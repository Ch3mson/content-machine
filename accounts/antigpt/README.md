# antigpt

Study / AntiGPT account. One locked Asian girl avatar. Current format:
**TikTok photo slideshow** (Benson, 2026-09-13).

1. **Hook slide** — the locked avatar plus a practical headline, such as “top 3 techniques to ace your essays >>>”
2. **Technique slides** — one short numbered heading per slide, plus one slightly fuller explanation below (one short sentence)
3. **Optional close** — comment, follow, save, or an approved AntiGPT line after the useful content

Primary writing reference: [@sophia.study](https://www.tiktok.com/@sophia.study?lang=en)
(Benson, 2026-09-13). Read her saved slides and the Notion examples linked in
`references/notion.md` before drafting. Keep slides brief; no paragraphs.
The current request is a hook plus
three technique slides. Only the locked avatar appears when a person is shown.
Default visual style: **9:16**, separate top/bottom text blocks, **#552082 purple
text on #E9D5FF light purple highlights**. See the account brief for the full
approved style. Existing still commands below remain available; the CLI renderer
does not yet implement this highlight layout. Post 3 uses native CapCut text layers.
Default timing: **three seconds per slide**, 15 seconds for five slides.
Repeat the approved [CapCut workflow](../../references/capcut-slideshow-workflow.md).
Continually append new posts to the same CapCut timeline, in 15-second sections.
Keep earlier posts in place. Each post folder stays flat: numbered PNGs,
`reel.mp4`, and caption files at the same level. Keep clean sources separately
in `assets/post-sources/N/`. After final approval following modifications, archive finished
slide screenshots for TikTok in `posts/N/01.png`–`05.png` and an Instagram Reels video
in `posts/N/reel.mp4`. Export each post's own range; retain the accumulated timeline.

Git storage preference (2026-09-14): all image/video files remain local and
are ignored. This hub, captions, source records, and workflow instructions stay
tracked. The completed media packages listed below exist on this production
Mac; a clone alone will not include them.

## Working timeline

Benson approved the two appended posts on 2026-09-13 after lowering their hook
headings. The shared project is **AntiGPT - Essay Writing with AI**. Each post
has its own finished images and 15-second video in `posts/N/`; draft media remain
under `outputs/slideshow-draft/posts/N/` for the editable timeline. Posts 6–15
now occupy 45–195 seconds and have approved PNG and MP4 archives. The next available section
begins at 195 seconds.

| Timeline range | Repo post | Content | Status |
| --- | --- | --- | --- |
| 0–15s | 3 | Essay writing with AI | Approved; PNGs and MP4 archived |
| 15–30s | 4 | AI shortcuts for essay research | Approved; PNGs and separate 15-second MP4 archived |
| 30–45s | 5 | GPT prompts for stronger essays | Approved; PNGs and separate 15-second MP4 archived |
| 45–60s | 6 | 3 GPT shortcuts to start your essay | Approved; five PNGs + separate 15-second MP4 archived |
| 60–75s | 7 | 3 ways to use your rubric with GPT | Approved; five PNGs + separate 15-second MP4 archived |
| 75–90s | 8 | 3 AI shortcuts for finding essay sources | Approved; five PNGs + separate 15-second MP4 archived |
| 90–105s | 9 | 3 GPT prompts for reading papers faster | Approved; five PNGs + separate 15-second MP4 archived |
| 105–120s | 10 | 3 ways GPT can turn notes into a draft | Approved; five PNGs + separate 15-second MP4 archived |
| 120–135s | 11 | 3 GPT prompts for better essay paragraphs | Approved; five PNGs + separate 15-second MP4 archived |
| 135–150s | 12 | 3 GPT shortcuts for writing your introduction | Approved; five PNGs + separate 15-second MP4 archived |
| 150–165s | 13 | 3 AI shortcuts for your literature review | Approved; five PNGs + separate 15-second MP4 archived |
| 165–180s | 14 | 3 GPT prompts to cut your word count | Approved; five PNGs + separate 15-second MP4 archived |
| 180–195s | 15 | 3 GPT checks before you finish your essay | Approved; five PNGs + separate 15-second MP4 archived |

## Asian girl avatar (identity lock)

`avatar/asian-girl-avatar.jpg` is Figure 1 on every fal edit. Keep her face. Keep her hair type (long dark wavy messy, or a bun of that same hair when the pose needs it). Change only pose, outfit, and scene.

- 20-year-old East Asian college student
- Long dark wavy messy hair, loose side part, face-framing layers; bun of that same hair is allowed
- Soft oval face, dark eyes, silver hoop earrings
- Default outfit: black zip-up hoodie over a plain white tank
- On a board swap: keep the exact board pose, expression, gaze, head angle, hand placement, and face occlusion (looking at the iPad, writing, eyes closed). Only swap identity: face, ears, hair, earrings. Do not transfer the avatar's reference pout. Use `--size source` to preserve the board's crop and dimensions.

## Folders

| Path | What it is |
| --- | --- |
| `avatar/asian-girl-avatar.jpg` | Identity lock. Never regenerate a different girl. |
| `boards/` | Composition boards (other people's photos). Figure 2 inputs only, never posted. |
| `outputs/{stamp}/` | Face-swap candidates + `contact-sheet.jpg`. Gitignored scratch; copy the exact keeper into a post. `--post N` generates a fresh still. |
| `posts/N/image.jpg` | Clean promoted still. `image_caption.jpg` is the captioned render. `caption.md` holds status and approved copy. |
| `posts/N/01.png`–`05.png` + `reel.mp4` | Finished slideshow package, saved after final approval: ordered CapCut slide captures for TikTok and MP4 for Instagram Reels. |
| `posts/N/caption.txt` | Copy-ready plain-text TITLE and DESCRIPTION; synchronized with the approved caption in `caption.md`. |
| `outputs/slideshow-draft/` | Mutable working media and copy for the shared CapCut project. |
| `assets/fonts/TikTokSans-Bold.ttf` | Overlay font |
| `assets/study-backgrounds/` | Reusable Pinterest study photos; `README.md` has the source index and `contact-sheet.jpg` previews the set. |
| `assets/logo-white.png` | Brand mark |
| `assets/post-sources/N/` | Exact clean sources retained outside each flat post folder. |
| `account-brief.md` | Audience, POV, product rules |

## Boards

| File | Composition | Source |
| --- | --- | --- |
| `library-head-on-hand.jpg` | Grand library reading room, seated at a long desk, head resting on hand, laptop open | @sophia.study photo 7629054163342658838 slide 1 (`references/social-accounts/user-sophia.study-study/`) |
| `study-selfie-01.jpg` | Coffee shop, grey hoodie, over-ear headphones, sipping an iced latte, sticker-covered laptop, mural behind | Pinterest |
| `study-selfie-02.jpg` | Cafe booth, black hoodie, beige cap, headphones, glasses, hand on chin, writing beside a tablet, two coffee cups | Pinterest |
| `study-selfie-03.jpg` | Late-night cafe, navy LA cap pulled low, grey hoodie, iPad and pencil on lap, iced drink | Pinterest |
| `study-selfie-04.jpg` | Empty brick-wall classroom, black shell jacket, ponytail, gold hoops, side profile at a laptop | Pinterest |
| `study-selfie-05.jpg` | Library, high bun, grey hoodie, writing on an iPad, coffee cup and laptop, face angled down | Pinterest |
| `study-selfie-06.jpg` | Overhead lying-back desk selfie, white long-sleeve, grey sweats, laptop, eyes closed, hand on face (crashout) | Pinterest |

| `study-selfie-07-library-glance.jpg` | Library seat, hand to cheek, laptop on lap, over-shoulder glance | [Pinterest](https://www.pinterest.com/pin/15551561210472593/) |
| `study-selfie-08-window-headphones.jpg` | Close selfie by a window, white top, glasses, over-ear headphones, cheek resting on hand | [Pinterest](https://www.pinterest.com/pin/807411039490112783/) |
| `study-selfie-09-elevator-coffee.jpg` | Elevator mirror selfie, navy sweatshirt, grey sweatpants, laptop/books and coffee held at waist | [Pinterest](https://www.pinterest.com/pin/492649954002492/) |
| `study-selfie-10-evening-cafe-mug.jpg` | Evening cafe armchair, black leather jacket, laptop and white mug, side profile | [Pinterest](https://www.pinterest.com/pin/587438345192599601/) |
| `study-selfie-11-cafe-brown-hoodie.jpg` | Bright cafe, brown hoodie, seated behind laptop with wired earphones, looking down | [Pinterest](https://www.pinterest.com/pin/696861742392192711/) |
| `study-selfie-12-laptop-sleeve-pose.jpg` | Black sweater at marble table, laptop foreground, sleeve to mouth, camera glance | [Pinterest](https://www.pinterest.com/pin/684124999686518091/) |
| `study-selfie-13-window-desk-overhead.jpg` | Overhead desk selfie by open window, white tee, monitor/laptop and tablet, looking down | [Pinterest](https://www.pinterest.com/pin/341007003059447561/) |
| `study-selfie-14-library-book-selfie.jpg` | Arm-length overhead selfie at library table, navy zip top, open book and pink keyboard | [Pinterest](https://www.pinterest.com/pin/783133822751210403/) |
| `study-selfie-15-laptop-chin-rest.jpg` | Low-angle desk selfie, black sweater, chin on hand, silver laptop in foreground | [Pinterest](https://www.pinterest.com/pin/1041387113908744411/) |
| `study-selfie-16-classroom-sweater.jpg` | Classroom selfie at long desk, burgundy sweater, laptop and notebook, looking toward camera | [Pinterest](https://www.pinterest.com/pin/978266350332629944/) |

Add a board: drop the photo in `boards/` with a descriptive slug and add a row here. TikTok carousels: `python tools/tiktok-photo-sourcer/download_tiktok_photos.py --out accounts/antigpt/boards "<url>"`, then rename.

## Posts

| Post | Status | Board | Notes |
| --- | --- | --- | --- |
| 1 (historical) | Posted; local files removed | Arena selfie (original avatar scene) | Previous still package is retained in Git history. Keep this ID reserved. |
| 2 (historical) | Draft removed; not posted | `library-head-on-hand.jpg` | Previous unapproved still package is retained in Git history. Keep this ID reserved. |
| `posts/3/` | Ready, not posted | `study-selfie-01.jpg` | Approved café selfie + four study photos dimmed 20%, purple highlights, CTA logo. Five 1080 × 1920 PNGs directly in the post folder and 15-second MP4 with music in `reel.mp4`. Copy, sources, and export checks in `caption.md`. |
| `posts/4/` | Ready, not posted | `study-selfie-02.jpg` | AI research shortcuts. Lowered hook heading, five 1080 × 1920 TikTok PNGs and separate 15-second MP4 with music, covering 15–30s. Details in `caption.md`. |
| `posts/5/` | Ready, not posted | `study-selfie-05.jpg` | GPT essay prompts. Lowered hook heading, five 1080 × 1920 TikTok PNGs and separate 15-second MP4 with music, covering 30–45s. Details in `caption.md`. |
| `posts/6/` | Ready, not posted | `study-selfie-07-library-glance.jpg` | 3 GPT shortcuts to start your essay. 45–60s; five 1080 × 1920 native PNGs, separate 15-second EsDeeKid `reel.mp4`, clean sources in `assets/post-sources/6/`, and copy-ready `caption.txt`. |
| `posts/7/` | Ready, not posted | `study-selfie-08-window-headphones.jpg` | 3 ways to use your rubric with GPT. 60–75s; five 1080 × 1920 native PNGs, separate 15-second EsDeeKid `reel.mp4`, clean sources in `assets/post-sources/7/`, and copy-ready `caption.txt`. |
| `posts/8/` | Ready, not posted | `study-selfie-09-elevator-coffee.jpg` | 3 AI shortcuts for finding essay sources. 75–90s; five 1080 × 1920 native PNGs, separate 15-second EsDeeKid `reel.mp4`, clean sources in `assets/post-sources/8/`, and copy-ready `caption.txt`. |
| `posts/9/` | Ready, not posted | `study-selfie-10-evening-cafe-mug.jpg` | 3 GPT prompts for reading papers faster. 90–105s; five 1080 × 1920 native PNGs, separate 15-second EsDeeKid `reel.mp4`, clean sources in `assets/post-sources/9/`, and copy-ready `caption.txt`. |
| `posts/10/` | Ready, not posted | `study-selfie-11-cafe-brown-hoodie.jpg` | 3 ways GPT can turn notes into a draft. 105–120s; five 1080 × 1920 native PNGs, separate 15-second EsDeeKid `reel.mp4`, clean sources in `assets/post-sources/10/`, and copy-ready `caption.txt`. |
| `posts/11/` | Ready, not posted | `study-selfie-12-laptop-sleeve-pose.jpg` | 3 GPT prompts for better essay paragraphs. 120–135s; five 1080 × 1920 native PNGs, separate 15-second EsDeeKid `reel.mp4`, clean sources in `assets/post-sources/11/`, and copy-ready `caption.txt`. |
| `posts/12/` | Ready, not posted | `study-selfie-13-window-desk-overhead.jpg` | 3 GPT shortcuts for writing your introduction. 135–150s; five 1080 × 1920 native PNGs, separate 15-second EsDeeKid `reel.mp4`, clean sources in `assets/post-sources/12/`, and copy-ready `caption.txt`. |
| `posts/13/` | Ready, not posted | `study-selfie-14-library-book-selfie.jpg` | 3 AI shortcuts for your literature review. 150–165s; five 1080 × 1920 native PNGs, separate 15-second EsDeeKid `reel.mp4`, clean sources in `assets/post-sources/13/`, and copy-ready `caption.txt`. |
| `posts/14/` | Ready, not posted | `study-selfie-15-laptop-chin-rest.jpg` | 3 GPT prompts to cut your word count. 165–180s; five 1080 × 1920 native PNGs, separate 15-second EsDeeKid `reel.mp4`, clean sources in `assets/post-sources/14/`, and copy-ready `caption.txt`. |
| `posts/15/` | Ready, not posted | `study-selfie-16-classroom-sweater.jpg` | 3 GPT checks before you finish your essay. 180–195s; five 1080 × 1920 native PNGs, separate 15-second EsDeeKid `reel.mp4`, clean sources in `assets/post-sources/15/`, and copy-ready `caption.txt`. |

Approved visual baseline (Benson, 2026-09-13): all seven final swaps in
`outputs/2026-09-13-asian-girl-avatar-board-poses/` are visually approved.
Use the seven images directly in that folder and `contact-sheet.jpg` as the
reference for future swaps: Asian girl avatar identity, board pose/expression,
source proportions, and preserved face occlusions. The subfolders contain
earlier attempts, not the approved set. Copy is not yet approved for this batch.

Earlier outputs: `outputs/2026-09-13-study-selfies-v2/` is the tighter identity + hair pass (down waves or a bun of her hair). First pass is in `outputs/2026-09-13-study-selfies/`.

## Commands

Make or continue a slideshow batch:

```text
/make-slideshows 10 new posts      # Claude Code
$make-slideshows 10 new posts      # Codex
```

The [canonical skill](../../references/skills/make-slideshows/SKILL.md) reads
this hub and the brief, resumes existing work, and carries the batch through
selfie selection, copy, CapCut, HTML review, revisions, and final post folders.
The completed posts 6–15 establish the latest flow and style. Use the current
tables above to find the next post ID and timeline range; do not hardcode them.

Batch face-swap the avatar onto every board (writes to `outputs/{stamp}/` + contact sheet):

```bash
python tools/fal/swap_avatar.py accounts/antigpt/boards --size source
```

One board, straight into a post folder:

```bash
python tools/fal/swap_avatar.py accounts/antigpt/boards/study-selfie-03.jpg --post 3
```

Caption an approved line onto a still (writes `image_caption.jpg` next to it):

```bash
python tools/fal/caption.py --image accounts/antigpt/posts/3/image.jpg --text "Things I WISH I knew\nbefore my first all-nighter"
```

Optional short clip from a still:

```bash
python tools/fal/video.py --image accounts/antigpt/posts/3/image.jpg --prompt "..." --out accounts/antigpt/posts/3/clip.mp4
```

## Rules

- Copy goes in chat first. A request to assemble complete slideshow drafts for
  review authorizes draft rendering; final approval gates the post exports.
- Any AntiGPT mention uses `product/antigpt-claim-bank.md` wording.
- Strip every bit of on-screen text or watermark from the source board during the swap.
- Never overwrite a posted `posts/N/image.jpg`; `swap_avatar.py --post` refuses unless `--force`.
- Keep the clean still and the captioned still as separate files.

## Next production batch

Benson approved all ten selfies on 2026-09-13 and asked to use each in a new
TikTok/Reel. The exact approved files in `outputs/2026-09-13-ten-study-selfies/`
are assigned in review order to posts 6–15. No regeneration on promotion.

All ten five-slide drafts are assembled in the shared CapCut project, covering
45–195 seconds. Each hook uses “from a harvard student >>>”; Benson confirmed
Harvard is accurate. All 100 new text blocks use 110% scale and the approved
purple highlights, with fuller explanations below. Hook headings on posts 8
and 14 sit lower to leave the faces clear.

Benson rejected the alternate music selections after review. All ten drafts
now reuse the original EsDeeKid beat, with the same 0–15-second source cut per post.
The working `outputs/slideshow-draft/next-ten-review.html` shows every slide,
each post’s own 15-second preview, and its longer title/description caption.
Benson requested saving all ten after review on 2026-09-13. Posts 6–15 now
contain their five native PNGs beside the separate 15-second `reel.mp4` and
copy-ready `caption.txt`. Exact clean backgrounds are preserved outside the
flat post folders in `assets/post-sources/6/`–`15/`. They are ready, not posted.

# antigpt

Study / AntiGPT account. One locked girl, one post format: **selfie + text + CTA**.

1. **Selfie** — the locked avatar, face-swapped onto a study composition board
2. **Text** — one short WISH / pain line rendered on the still
3. **CTA** — comment, follow, save, or an approved AntiGPT line in the caption or on-image close

No slideshows. No other generated faces on a posted still.

## Avatar (identity lock)

`avatar/anchor.jpg` is Figure 1 on every fal edit. Keep her face. Keep her hair type (long dark wavy messy, or a bun of that same hair when the pose needs it). Change only pose, outfit, and scene.

- 20-year-old East Asian college student
- Long dark wavy messy hair, loose side part, face-framing layers; bun of that same hair is allowed
- Soft oval face, dark eyes, silver hoop earrings
- Default outfit: black zip-up hoodie over a plain white tank
- On a board swap: keep the board's expression and gaze (looking at the iPad, writing, eyes closed). Only swap face, ears, hair, earrings. Do not force the anchor pout.

## Folders

| Path | What it is |
| --- | --- |
| `avatar/anchor.jpg` | Identity lock. Never regenerate a different girl. |
| `boards/` | Composition boards (other people's photos). Figure 2 inputs only, never posted. |
| `review/{stamp}/` | Face-swap candidates + `contact-sheet.jpg`. Gitignored scratch; copy the exact keeper into a post. `--post N` generates a fresh still. |
| `posts/N/image.jpg` | Clean promoted still. `image_caption.jpg` is the captioned render. `caption.md` holds status and approved copy. |
| `assets/fonts/TikTokSans-Bold.ttf` | Overlay font |
| `assets/logo-white.png` | Brand mark |
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

Add a board: drop the photo in `boards/` with a descriptive slug and add a row here. TikTok carousels: `python tools/tiktok-photo-sourcer/download_tiktok_photos.py --out accounts/antigpt/boards "<url>"`, then rename.

## Posts

| Post | Status | Board | Notes |
| --- | --- | --- | --- |
| `posts/1/` | Posted | Arena selfie (original anchor scene) | Navy arena selfie, extras swapped. Caption TBD. |
| `posts/2/` | Draft, not posted | `library-head-on-hand.jpg` | Library face-swap. No approved copy yet. |

Pending review: `review/2026-09-13-study-selfies-v2/` is the tighter identity + hair pass (down waves or a bun of her hair). First pass is still in `review/2026-09-13-study-selfies/`.

## Commands

Batch face-swap the avatar onto every board (writes to `review/{stamp}/` + contact sheet):

```bash
python tools/fal/swap_avatar.py accounts/antigpt/boards
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

- Copy goes in chat first. Render a caption only after the user approves the exact lines.
- Any AntiGPT mention uses `product/antigpt-claim-bank.md` wording.
- Strip every bit of on-screen text or watermark from the source board during the swap.
- Never overwrite a posted `posts/N/image.jpg`; `swap_avatar.py --post` refuses unless `--force`.
- Keep the clean still and the captioned still as separate files.

# Download Manifest: antigpt study references

Purpose: fetch raw slideshow images for the `antigpt` account's Workflow A2
design extraction. The local machine is behind a VPN that blocks TikTok, so run
this from a Cursor Cloud Agent or a VPN-off terminal in the repo root.

Created: 2026-09-05
Owner account: `accounts/antigpt/`
Reference map: `accounts/antigpt/extractions/reference-map.md`

## Why these downloads

`references/social-accounts/post-index.md` already indexes the hooks and
patterns for `user-sophia.study-study` Posts 1-5 and `chasingpeaks0` Posts 1, 4,
5, but the raw slide folders are not on this machine. Writing extraction (A1)
can use the text index; design and image extraction (A2) need the slides.

## Confirmed source accounts (verified 2026-09-05)

| Indexed as | Live handle | Profile URL | Stats | Notes |
| --- | --- | --- | --- | --- |
| `user-sophia.study-study` | `@sophia.study` | https://www.tiktok.com/@sophia.study | 33.1K followers, 1.67M likes, 435 posts | `@sophia.study.study` does not exist; this is the account. Bio: "Study motivation and tips". |
| `chasingpeaks0` | `@chasingpeaks0` | https://www.tiktok.com/@chasingpeaks0 | 22.4K followers, 791K likes, 184 posts | Bio: "Pursuit of Human Potential". |

## Step 1: locate the photo posts

TikTok profile pages do not embed the post list, so open each profile (or use
TikTok search) and find the photo posts with these first-slide hooks. Copy each
`https://www.tiktok.com/@{handle}/photo/{id}` URL.

### @sophia.study

| Indexed post | First-slide hook to find |
| --- | --- |
| Post 1 | "My dad is 2nd highest paid professor at Oxford and he taught me a brain hack that changed how I study forever." |
| Post 2 | "My grandpa is the 2nd highest paid professor at Harvard, yet nobody believes him when he says these things." |
| Post 3 | "How Harvard students ACTUALLY study" |
| Post 4 | "Ranking all the study methods I've tried as a neuroscience student at Harvard." |
| Post 5 | "The most effective study method for each subject" |

### @chasingpeaks0

| Indexed post | First-slide hook to find |
| --- | --- |
| Post 1 | "How to Learn a Language Like a PEAK Human. According to neuroscience." |
| Post 4 | "The HIGHEST ROI Habits for Self Improvement. Ranked by science." |
| Post 5 | "How You Build a PEAK HUMAN Memory. According to neuroscience." |

### New study-aesthetic references (find 3-5)

Search TikTok for photo posts (not videos) under `#studytok`, `#studytips`,
`#activerecall`, `#howtostudy`, `#studygram` with hooks like:

- "study methods ranked"
- "how to memorize anything before an exam"
- "the order I write an essay in"
- "stop rereading your notes"
- "blurting method" / "Feynman technique" / "spaced repetition"

Prefer posts with: warm desk photography, notebooks, flashcards, laptop, bold
method label plus one-line explanation, 5-8 slides, and a save-for-later close.
Skip posts that are mostly selfies or motivational quotes.

Log each new account in `references/social-accounts/account-map.md` and each
post in `post-index.md` after download.

## Step 2: download

Run from the repo root. Post numbers must match the indexed post numbers so the
existing `post-index.md` rows stay valid.

```bash
python -m pip install gallery-dl  # only if not installed

# @sophia.study -> keep the indexed folder name
python tools/tiktok-photo-sourcer/download_tiktok_photos.py --account user-sophia.study-study --post 1 "<URL for Post 1>"
python tools/tiktok-photo-sourcer/download_tiktok_photos.py --account user-sophia.study-study --post 2 "<URL for Post 2>"
python tools/tiktok-photo-sourcer/download_tiktok_photos.py --account user-sophia.study-study --post 3 "<URL for Post 3>"
python tools/tiktok-photo-sourcer/download_tiktok_photos.py --account user-sophia.study-study --post 4 "<URL for Post 4>"
python tools/tiktok-photo-sourcer/download_tiktok_photos.py --account user-sophia.study-study --post 5 "<URL for Post 5>"

# @chasingpeaks0
python tools/tiktok-photo-sourcer/download_tiktok_photos.py --account chasingpeaks0 --post 1 "<URL for Post 1>"
python tools/tiktok-photo-sourcer/download_tiktok_photos.py --account chasingpeaks0 --post 4 "<URL for Post 4>"
python tools/tiktok-photo-sourcer/download_tiktok_photos.py --account chasingpeaks0 --post 5 "<URL for Post 5>"

# New references: use the creator handle as --account and number posts from 1
python tools/tiktok-photo-sourcer/download_tiktok_photos.py --account <handle> --post 1 "<URL>"
```

Expected output: `references/social-accounts/{account}/Post {n}/1.jpg, 2.jpg, ...`

## Step 3: record

- Paste the resolved URLs into the table below.
- Update `accounts/antigpt/extractions/reference-map.md`: change the matching
  rows from `slides pending download` to `ready`.
- Run `python tools/slideshow-transcriber/prepare_slideshow_transcript.py <image-folder>`
  on any new post that is not yet indexed.

| Account | Post | URL | Downloaded (Y/N) | Slides |
| --- | --- | --- | --- | --- |
| user-sophia.study-study | 1 |  |  |  |
| user-sophia.study-study | 2 |  |  |  |
| user-sophia.study-study | 3 |  |  |  |
| user-sophia.study-study | 4 |  |  |  |
| user-sophia.study-study | 5 |  |  |  |
| chasingpeaks0 | 1 |  |  |  |
| chasingpeaks0 | 4 |  |  |  |
| chasingpeaks0 | 5 |  |  |  |

## Instagram (no VPN issue, needs a logged-in browser)

Instagram refuses anonymous fetches. Audit `https://www.instagram.com/antigpt.me/`
with the browser harness: start Chrome with `--remote-debugging-port=9222`, then
`python tools/browser-harness/connect_my_chrome.py`. Record post count, formats,
visual style, and any carousels in the reference map. Screenshots from the user
are an acceptable substitute.

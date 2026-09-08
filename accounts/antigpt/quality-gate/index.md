# Quality Gate Ledger — antigpt

Each user-reviewable sample gets its own attempt folder. Never overwrite a prior
attempt; create a new one.

| Attempt | Date | Type | Files | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| [attempt-001-2026-09-05-mock-blurting](attempts/attempt-001-2026-09-05-mock-blurting/) | 2026-09-05 | 5-slide mock (pre-A1/A2) | `copy.md`, `render_mock.py`, `slide_1..5.png`, `contact-sheet.png` | Rejected | Cream notebook, serif, 1080x1350. User: format not liked; text on rule lines and spacing read as AI. Superseded by 002. |
| [attempt-002-2026-09-05-mbv-style-black](attempts/attempt-002-2026-09-05-mbv-style-black/) | 2026-09-05 | 5-slide mock, makebrainrotvideos styling | `copy.md`, `render_mock.py`, `slide_1..5.png`, `contact-sheet.png` | Style approved ("yea do this sorta style"); text edges pixelated | Exact copy of makebrainrotvideos post-5 renderer: 1080x1920, Arial, white text, 3px circular outline, centered, numbered header + paragraph. Solid black background until photos are dropped into `sourced/`. |
| [attempt-003-2026-09-05-mbv-style-hires](attempts/attempt-003-2026-09-05-mbv-style-hires/) | 2026-09-05 | 5-slide mock, same as 002 with clean text | `copy.md`, `render_mock.py`, `slide_1..5.png`, `contact-sheet.png` | Pending user reaction | Identical layout/sizes to 002. Renders at 3x (3240x5760) and downsamples with Lanczos; outline uses Pillow `stroke_width` (anti-aliased) instead of stamping offset glyphs. This is the renderer to carry into the account `process_images.py` template. |
| [attempt-004-2026-09-08-straight-a-hacks](attempts/attempt-004-2026-09-08-straight-a-hacks/) | 2026-09-08 | 5-slide mock, user-supplied hook "3 study hacks that straight A students never tell you about" | `copy.md`, `render_mock.py`, `slide_1..5.png`, `contact-sheet.png` | Approved; promoted to `posts/1-straight-a-hacks/` | Same renderer as 003. Copy: past papers first, ugly draft first, ask the professor; CTA bridges from hack 2. Revisions during review: CTA label cut to two lines, brand shown as "AntiGPT" (no .me), site logo added under the name, user's Pinterest photos 1-5 mapped 1:1, CTA overlay raised to 78%. First real post for the account. |
| [attempt-005-2026-09-08-study-with-me-tone](attempts/attempt-005-2026-09-08-study-with-me-tone/) | 2026-09-08 | Post 1 re-toned: casual lowercase "study with me" voice, `swipe →` cue on hook | `copy.md`, `render_mock.py`, `slide_1..5.png`, `contact-sheet.png` | Approved; applied to `posts/1-straight-a-hacks/` | Reference @lovely.studyy photo 7402819041850592517. Same photos and layout as post 1; only copy tone and the swipe cue changed. Post flow.md, process_images.py, and processed/ updated 2026-09-08. |
| [attempt-006-2026-09-08-caption-fonts](attempts/attempt-006-2026-09-08-caption-fonts/) | 2026-09-08 | Font / caption-style tests on post 2 hook | `render_font_tests.py`, `a..e-*.png`, `contact-sheet.png` | Pending user pick | Five treatments of the same hook: A current stroke, B TikTok Sans boxed pills, C Montserrat boxed, D Arial Rounded boxed, E Hormozi Impact + yellow word. Published posts not overwritten. |

## Design direction on file

- User direction (2026-09-05): use makebrainrotvideos styling. When Workflow A2
  runs, start `design.md` from `accounts/makebrainrotvideos/design.md` and
  change only what the study niche needs (photo subject matter, overlay
  strength for lighter desk photos).
- Rendering rule for this account: supersample 3x + Lanczos downsample, and
  anti-aliased `stroke_width` outlines. Record in `design.md` under renderer
  rules so every post script inherits it.

## Rules

- `writing.md` and `design.md` do not exist yet; nothing is locked.
- Record the user's reaction in the attempt's `copy.md` and, if rejected, in
  `writing/refinement-personas.md` once Workflow A1 creates it.

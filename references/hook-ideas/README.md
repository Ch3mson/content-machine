# Hook Ideas

Universal, account-agnostic inspiration bank for hooks, retention mechanics,
and reusable post ideas pulled from videos, transcripts, slideshow screenshots,
and image carousels.

## Authority

This folder is lower authority than account files. Treat it as inspiration, not
as final copy, account voice, product claims, or validated presets.

Use `accounts/{account}/writing.md`, `design.md`, and approved `presets.md` when
turning an idea into a real post.

## Folder Structure

```text
references/hook-ideas/
  README.md
  index.md
  inbox/
    transcripts/   Raw pasted video transcripts or caption exports.
    slideshows/    Downloaded slideshow images + slide transcript scaffolds.
  cards/           One analyzed hook idea card per source post.
  exports/         Optional grouped digests for reuse sessions.
  templates/       Reusable card templates.
```

## Step-by-Step Workflow

### Step 1: Identify the Source Type

Ask: what did the user provide?

| User gave | Source type | Path to follow |
| --- | --- | --- |
| TikTok video URL | Video transcript | Step 2A |
| TikTok photo/slideshow URL | Slideshow screenshots | Step 2B |
| Folder of screenshot images | Existing image folder | Step 2C |
| Pasted transcript or caption text | Raw text | Step 2D |

### Step 2A: TikTok Video URL → Fetch Transcript

Run:

```powershell
python tools/tiktok-transcript-sourcer/download_tiktok_transcript.py "{tiktok-video-url}"
```

- Reads `SUPADATA_API_KEY` from `.env` or shell.
- Saves transcript to `inbox/transcripts/YYYY-MM-DD-tiktok-{video-id}.md`.
- Do not download the video file.
- If the video is private, restricted, or unsupported, ask the user for a transcript or caption export.

### Step 2B: TikTok Photo/Slideshow URL → Download + Transcribe

1. Download images into the hook-ideas inbox:

```powershell
python tools/tiktok-photo-sourcer/download_tiktok_photos.py `
  --out "references/hook-ideas/inbox/slideshows/{slug}/images" `
  "{tiktok-photo-url}"
```

2. Generate a slide transcript scaffold:

```powershell
python tools/slideshow-transcriber/prepare_slideshow_transcript.py `
  "references/hook-ideas/inbox/slideshows/{slug}/images" `
  --source-url "{tiktok-photo-url}" `
  --slug "{slug}"
```

3. Inspect each slide image visually and fill the scaffold with the exact visible text. Preserve slide order and meaningful line breaks.

### Step 2C: Existing Image Folder → Transcribe Only

Skip downloading. Run the transcriber directly on the folder:

```powershell
python tools/slideshow-transcriber/prepare_slideshow_transcript.py "{folder-path}"
```

Then fill the scaffold with visible text from each slide.

### Step 2D: Pasted Transcript or Caption Text → Save Directly

Save the raw text to `inbox/transcripts/YYYY-MM-DD-{source-slug}.md` with a header noting the source, date, and how it was obtained.

### Step 3: Analyze the Source

Read the full transcript or filled slide scaffold. Extract:

- **Original hook** — the opening line or first-frame promise.
- **Scroll-stop reason** — why someone pauses on this.
- **Retention reason** — why someone keeps watching or swiping.
- **Flow map** — each beat, its job, and the retention mechanic.
- **Hook archetype** — the category of hook (ranked list, contradiction, story open, etc.).
- **Emotional lever** — fear, status, identity gap, curiosity, desire, relief, etc.
- **Curiosity engine** — what question keeps the viewer engaged.
- **Proof or credibility device** — what makes it feel real.
- **Idea payload** — surface topic vs. deeper viewer desire vs. private pain.
- **Transferable pattern** — the abstract move that can be reused safely.
- **Account fit** — which account types could use it, which should avoid it.
- **Risks** — claim burden, copycat wording, niche mismatch, weak payoff.

### Step 4: Create the Hook Card

1. Start from `templates/hook-card.md`.
2. Fill every section based on the analysis.
3. Save to `cards/YYYY-MM-DD-{source-slug}.md`.
4. Keep exact source wording only in the "Original Hook" section for reference. All other sections should use abstracted, reusable language.

### Step 5: Update the Index

Add a row to `index.md` with:

| Column | What to put |
| --- | --- |
| Date | Capture date (YYYY-MM-DD) |
| Source | Creator name + platform + video/post ID |
| Type | Video transcript / Slideshow screenshots / Image carousel / Raw text |
| Card | Relative path to the card file |
| Hook Archetype | Short name (e.g. "Escalating ranked code") |
| Transferable Pattern | One-line summary of the reusable move |
| Tags | 4-8 hyphenated tags |
| Account Fit | 3-6 account types that could use this |
| Status | raw inspiration / candidate for account concept / candidate for angle extraction |

### Step 6: Using a Card for a Real Post

- Run `post-concept-flow` or `angle-variants` to adapt the pattern.
- Do **not** copy the original hook verbatim into account posts.
- Use the account's `writing.md`, `design.md`, and `presets.md` to shape the final copy.

## What To Extract

- Original hook or first-frame promise.
- Why someone stops scrolling.
- Why someone keeps watching or swiping.
- Emotional lever: fear, status, identity gap, curiosity, contradiction,
  urgency, proof, shame, desire, or relief.
- Transferable pattern: the abstract hook move that can be reused safely.
- Idea payload: what the post is really about underneath the surface topic.
- Account fit: which account types could use it, and which should avoid it.
- Rewrite boundary: what must not be copied because it is too source-specific.

## Source Type Rules

- Video URLs use transcript-only capture. Do not download the video.
- Photo carousel URLs use image extraction, then slide-by-slide visible-text
  transcription. Preserve slide order and manual line breaks.
- If the input is already a folder of images, skip downloading and transcribe
  that folder directly.

## Value Add

This is useful because it separates raw inspiration from account-specific
presets. `angle-extraction` validates patterns into a specific account after
quality gates. This folder captures ideas before they are ready for that.

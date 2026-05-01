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
    slideshows/    Notes pointing to slideshow folders or OCR/manual slide text.
  cards/           One analyzed hook idea card per source post.
  exports/         Optional grouped digests for reuse sessions.
  templates/       Reusable card templates.
```

## Workflow

1. Save or reference the raw input.
   - TikTok video: fetch transcript with `tools/tiktok-transcript-sourcer/`.
   - TikTok photo carousel: download images with `tools/tiktok-photo-sourcer/`
     into `inbox/slideshows/{slug}/images/`, then create a slide transcript
     scaffold with `tools/slideshow-transcriber/`.
   - Existing image folder: reference its path instead of duplicating images.
2. Create an analysis card from `templates/hook-card.md` in `cards/`.
3. Update `index.md` with the source, hook archetype, transferable pattern,
   tags, and account-fit notes.
4. When using a card for a real post, run `post-concept-flow` or
   `angle-variants`; do not copy the original hook verbatim.

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

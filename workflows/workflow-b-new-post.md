# Workflow B: New Post For Existing Account

Use this when the user says `workflow b`, `workflow-b`, `new post`, or asks to
make a slideshow for an existing account.

Goal: create the post flow, source or map images, process the images, and verify
the final slides.

## Read First

1. `../AGENTS.md`
2. `../accounts/{account}/account-brief.md`
3. `../accounts/{account}/presets.md`, if present
4. `../accounts/{account}/writing.md`
5. `../accounts/{account}/image.md`
6. `../accounts/{account}/sources.md`
7. `../product/app-brief.md` and `../product/claim-bank.md` before product copy

If required account files are missing, run Workflow A first:
`workflow-a-new-account.md`.

## Post Folder

Preferred shape:

```text
accounts/{account}/posts/{post-name}/
  flow.md
  image_preset.json
  sourced/
  process_images.py
  processed/
```

Existing legacy folders such as `accounts/athlete-stories/Lebron/` are valid.
Work in the folder the user names or the closest existing post folder.

## Procedure

1. Resolve the account and subject:
   - Identify `{account}` and `{post-name}` from the user prompt.
   - If the user only gives a subject, use the active or obvious account.

2. Select account preset:
   - Read `presets.md` if present.
   - Choose the preset that matches the subject's narrative.
   - If no preset fits, use `writing.md` and `image.md` directly and note the
     assumption in `flow.md`.

3. Gather or source images:
   - If raw images already exist, map them to slide roles.
   - If an `image_preset.json` exists, run:
     `python tools/image-sourcer/source_images.py <preset>`.
   - If no preset exists and the user did not provide images, create a preset
     from the account slide roles and subject, then run the image sourcer.
   - If a slide uses `"source": "ask_user"` or a product photo is required, ask
     only for that missing image.
   - If browser sourcing cannot start because Chrome remote debugging is not
     available, follow `../tools/image-sourcer/README.md` and report the exact
     blocker.

4. Write `flow.md`:
   - Follow the selected preset and `writing.md`.
   - Use exact slide roles from `image.md`.
   - Keep product mentions native and claim-bank approved.
   - Flag research-sensitive claims per `sources.md`.
   - Use manual line breaks when they matter for final rendering.

5. Process images:
   - Run Workflow C: `workflow-c-image-processing.md`.
   - Use the post `process_images.py` if it exists.
   - If it does not exist, create it from the workflow and account `image.md`.

6. Verify:
   - Confirm every final PNG is 1080x1920.
   - Confirm output files are named `slide_1.png`, `slide_2.png`, etc.
   - Check that the image count matches `flow.md`.
   - Report any skipped or missing source images.

## Agent Rules

- Do not stop after a draft if the user asked for an end-to-end post.
- Do not force w(inner) into a story where the account brief says it should stay
  invisible or caption-only.
- Do not invent athlete facts that need sources. Mark them as claims to verify.
- Use Stop Slop QA before final copy.
- Respect manual line breaks from `flow.md` during processing.

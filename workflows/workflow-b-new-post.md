# Workflow B: New Post For Existing Account

Use this when the user says `workflow b`, `workflow-b`, `new post`, or asks to
make a slideshow for an existing account.

Goal: create the post flow, source or map images, process the images, and verify
the final slides.

## Read First

1. `../AGENTS.md`
2. `../accounts/{account}/account-brief.md`
3. `../accounts/{account}/writing.md`
4. Only the indexed writing subfiles required by `writing.md` for this post
5. `../accounts/{account}/presets.md`, if present and validated
6. `../accounts/{account}/design.md`
7. `../accounts/{account}/image.md`
8. `../accounts/{account}/sources.md`
9. `../product/app-brief.md` and `../product/claim-bank.md` before product copy

If required account files are missing, run Workflow A first:
`workflow-a-new-account.md`.
If `writing.md` or `design.md` is marked `Pending quality gate`, do not use the
account for a production post unless the user explicitly accepts draft status.

## Post Folder

Preferred shape:

```text
accounts/{account}/posts/{post-name}/
  concept/
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
   - Read `writing.md` first. If it has a table of contents for indexed
     writing subfiles, read only the subfiles relevant to the current post.
   - Read `presets.md` only after the baseline voice is clear. Treat presets as
     supplemental angle or flow patterns, not as the source of account voice.
   - If the user starts from a broad avatar, pain point, or concept instead of
     an approved post angle and slide copy, run
     `../references/skills/post-concept-flow/SKILL.md` before creating final
     `flow.md`.
   - Store concept-stage research, decisions, and copy options in the post
     folder's `concept/` directory.
   - Choose a preset only when it matches the subject's narrative and does not
     conflict with `writing.md`.
   - If no preset fits, use `writing.md`, `design.md`, and `image.md` directly
     and note the assumption in `flow.md`.
   - If the user asks for 3 variants, angle concepts, or brainstorming before a
     post is locked, use `../references/skills/angle-variants/SKILL.md` and
     answer in chat. Do not create `flow.md` until the user chooses an angle or
     asks for a full post.

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
   - Follow `writing.md` and its relevant indexed subfiles.
   - Follow the selected preset only as a supplemental structure.
   - Follow `design.md` for slide format, section limits, typography-driven line
     breaks, and renderer-facing layout constraints.
   - Use exact slide roles from `image.md`.
   - Keep product mentions native and claim-bank approved.
   - Flag research-sensitive claims per `sources.md`.
   - Use manual line breaks when they matter for final rendering.

5. Process images:
   - Run Workflow C: `workflow-c-image-processing.md`.
   - Use the post `process_images.py` if it exists.
   - If it does not exist, create it from the workflow, account `design.md`, and
     account `image.md`.

6. Verify:
   - Confirm every final PNG matches the canvas size in account `design.md`.
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

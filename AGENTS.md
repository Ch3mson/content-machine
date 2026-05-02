# Agent Router

This is a docs-first workspace for w(inner) social slideshow playbooks and rendered TikTok/Instagram slides. Start here, then read only the workflow/account/post files needed for the request.

## Tags Are Commands

If the user says one of these, start the matching file without waiting for another prompt:

| User intent | Start here |
| --- | --- |
| `workflow a`, `new account`, `onboard account` | `workflows/workflow-a-new-account.md` |
| `workflow a0`, `account intake`, `reference map` | `workflows/workflow-a0-account-intake-reference-map.md` |
| `workflow a1`, `writing extraction`, `writing principles` | `workflows/workflow-a1-writing-principle-extraction.md` |
| `workflow a2`, `design extraction`, `design principles` | `workflows/workflow-a2-design-principle-extraction.md` |
| `workflow a3`, `quality gate`, `test writing/design` | `workflows/workflow-a3-writing-design-quality-gate.md` + `references/skills/account-quality-gate/SKILL.md` |
| `workflow a4`, `angle extraction`, `preset extraction` | `workflows/workflow-a4-angle-extraction-to-presets.md` + `references/skills/angle-extraction/SKILL.md` |
| `workflow b`, `new post`, `make post` | `workflows/workflow-b-new-post.md` |
| broad post idea, `post concept`, `VOC research`, avatar + pain point | `references/skills/post-concept-flow/SKILL.md` before final `flow.md` |
| `hook ideas`, `hook bank`, `pull the hook`, `analyze hook`, `transcript inspo`, `slideshow inspo`, TikTok video/slideshow hook analysis | `references/skills/hook-idea-extraction/SKILL.md` + `references/hook-ideas/README.md` |
| `creative DNA`, out-of-niche hooks, viral principles, cross-niche ideas, mechanism transfer, account-specific ideas from references | `references/creative-dna/README.md` + `references/creative-dna/owned-account-idea-router.md` + target profile in `references/creative-dna/account-profiles/` + `graphify-out/creative-dna/GRAPH_REPORT.md` |
| `save this connection`, `graphify this connection`, `remember this link`, `capture this reasoning`, `add this to the graph`, mechanism transfer memory | `references/skills/graphify-connection-capture/SKILL.md` |
| `workflow c`, `process images`, `render slides` | `workflows/workflow-c-image-processing.md` |
| `source images`, `find images`, `Pinterest images` | `tools/image-sourcer/README.md` |
| `TikTok photos`, `TikTok carousel`, `source TikTok`, `download TikTok` | `references/skills/tiktok-photo-sourcing/SKILL.md` + `tools/tiktok-photo-sourcer/README.md` |
| `3 variants`, `3 angles`, `angle concepts`, brainstorming | `references/skills/angle-variants/SKILL.md`; answer in chat, not `flow.md` |
| `save this as writing feedback`, `record this writing preference`, `compound my suggestions`, `distill today's feedback`, `strengthen the rule`, repeated copy criticism, user says the agent keeps making the same writing mistake | `references/skills/writing-feedback-compounding/SKILL.md` |
| `stop slop`, `anti-AI writing`, `clean copy` | `references/skills/stop-slop/SKILL.md` |
| product/app/claim/w(inner) mention | `product/app-brief.md` + `product/claim-bank.md` before writing |

If the user tags multiple workflows, run them in order. Workflow B must pause at
the copy approval gate before sourcing images or running Workflow C. After the
user explicitly approves the full copy, continue into sourcing and Workflow C
when the user asked for an end-to-end post.

## Read Order

1. Selected workflow or skill.
2. Product files only if the copy mentions w(inner), the app, or a product claim.
3. Target account files, including account-specific `README.md` when present:
   - `account-brief.md`, `writing.md`, `presets.md` if present, `design.md`, `image.md`, `sources.md`
   - If `writing.md` has an indexed writing folder table of contents, read only the subfiles it names for the current task.
   - `prompts.md` if the account README lists it, such as `accounts/science-athlete/`
4. Only the post folder being worked on.
5. Tool docs only when a workflow calls for that tool.

Root `README.md` currently names `accounts/athlete-stories/` as the active locked account. If the user names another account, use that account instead.

## Creative DNA Retrieval Rule

Use this rule for any request involving post ideas, hook ideas, angle ideas,
viral inspiration, out-of-niche examples, cross-niche transfer, creative
principles, mechanism families, account-specific concepts, or phrases like
`creative DNA`.

Creative DNA is the repo's cross-niche idea engine. Its job is to connect:

```text
viral reference post
→ reusable mechanism family
→ psychological / emotional lever
→ hook archetype or proof pattern
→ target account fit
→ account-safe concept seed
→ correct workflow route
```

Mandatory retrieval path before answering Creative DNA requests:

1. Read `references/creative-dna/README.md`.
2. Read `references/creative-dna/owned-account-idea-router.md`.
3. Read `references/creative-dna/cross-niche-principle-map.md`.
4. Read the target profile in `references/creative-dna/account-profiles/{account}.md`.
5. Read `graphify-out/creative-dna/GRAPH_REPORT.md` when present.
6. Read 1-3 relevant extraction files from `references/creative-dna/extractions/`
   based on the selected mechanism families.
7. Then read target account source-of-truth files only as needed for constraints:
   `account-brief.md`, `writing.md`, `design.md`, `image.md`, `sources.md`,
   and `presets.md` if present.

Required output shape for Creative DNA ideation:

- mechanism family
- source reference post / niche
- reusable principle
- why it transfers to the target account
- account constraints or risks
- concept seed or hook direction
- best workflow route (`post-concept-flow`, `angle-variants`, hook extraction,
  or Workflow B)

Hard rules for Creative DNA:

- Do not answer from general knowledge alone when the user asks for Creative DNA.
- Do not invent out-of-niche examples unless clearly labeled as a new hypothesis;
  prefer existing Creative DNA extractions and hook/reference docs.
- Do not copy source hooks verbatim. Abstract the mechanism, then adapt it
  through target account rules.
- Do not jump to final slide copy unless the user explicitly asks; default to
  concept seeds / hook directions.
- If no target account is named, use the active locked account unless the request
  clearly implies another account.
- If the target account profile is missing or empty, state that Creative DNA
  routing is incomplete and ask whether to use normal account files instead.

## Workspace Contracts

- Account source-of-truth files live in `accounts/{account}/`; preferred new post workspaces live in `accounts/{account}/posts/{post-slug}/`.
- `writing.md` is the required entrypoint and highest-authority retrieval map for account copy. For indexed accounts, detailed writing files live under `accounts/{account}/writing/`.
- `writing/refinement-personas.md` customizes the three required refinement personas for the account. Use it before rendering quality-gate samples, and update it when the user rejects a sample.
- `writing/pattern-extractions.md` is the account memory for raw, iterative writing feedback. When the user gives reusable critique on hooks, angles, slide copy, voice, wording, or repeated writing mistakes, route it through `references/skills/writing-feedback-compounding/SKILL.md` and write it into the target account's writing files; do not default to `BUGS.md`.
- `design.md` is the account source of truth for canvas size, layout, typography, text hierarchy, reference-photo framing, and renderer-facing format rules.
- `image.md` is for photo direction, visual treatment, and selected-photo suitability; do not rely on it for layout decisions that belong in `design.md`.
- Quality-gate attempts live in `accounts/{account}/quality-gate/attempts/{attempt-id}/`, with an attempt ledger at `accounts/{account}/quality-gate/index.md`.
- `presets.md` is supplemental. Create or update it only after baseline `writing.md` and `design.md` pass the quality gate, unless the user explicitly asks for legacy behavior.
- Universal hook inspiration lives in `references/hook-ideas/`. Treat those cards as raw inspiration, not account rules, final copy, or validated presets.
- Legacy post folders such as `accounts/athlete-stories/Lebron/` and `Michael Jordan/` are valid; work in the folder the user names or the closest existing post folder.
- Standard post files: `flow.md`, `image_preset.json`, `sourced/`, post-specific `process_images.py`, `processed/`.
- Draft copy review files may live in `accounts/{account}/posts/{post-slug}/concept/`.
  The final `flow.md` is written only after the user approves the full slide copy.
- Cross-account post status lives in `POST_STATUS.md`; each account also has `accounts/{account}/post-status.md`.
- Finished publish packs live in `accounts/{account}/ready-to-post/{post-slug}/` and contain only `flow.md` plus final `slide_*.png` files. Do not edit from publish packs; edit the source workspace and refresh the tracker.
- `tools/` is only for runnable utilities. Put strategy docs, templates, research notes, and product references in `references/` or `product/`.
- There is no root app manifest; Python tooling is local to scripts, with `tools/browser-harness/pyproject.toml` requiring Python >=3.11.

## Commands And Gotchas

- Source images: `python tools/image-sourcer/source_images.py <path-to-image_preset.json>`.
- Source TikTok photo carousels without cookies: `python tools/tiktok-photo-sourcer/download_tiktok_photos.py --account <reference-account> --post <number-or-label> <tiktok-photo-url>`. Missing post folders are created automatically.
- Fetch TikTok video transcripts without downloading video: `python tools/tiktok-transcript-sourcer/download_tiktok_transcript.py <tiktok-video-url>`. Requires `SUPADATA_API_KEY` in the shell or local `.env`.
- Prepare photo slideshow text transcription: `python tools/slideshow-transcriber/prepare_slideshow_transcript.py <image-folder>`.
- Browser-backed sourcing needs Chrome running with remote debugging on port 9222, then `python tools/browser-harness/connect_my_chrome.py` if auto-detection fails.
- `tools/browser-harness/_compat.py` is a local Windows TCP-socket patch for browser-harness; do not remove it as an upstream mismatch.
- Process images with the target post script: `python accounts/{account}/{post}/process_images.py` or `python accounts/{account}/posts/{post}/process_images.py`.
- If a post has no processor, create one from `workflows/workflow-c-image-processing.md`, the account `design.md`, and the account `image.md`; keep slide mappings in the post script.
- Final processed slides must be PNG files named `slide_1.png`, `slide_2.png`, etc., exactly matching the canvas size in account `design.md`.
- Refresh post dashboards and ready-to-post packs after post changes: `python tools/post-tracker/update_post_status.py`.

## Hard Rules

- Do not invent product claims; use `product/claim-bank.md`.
- Do not invent final account rules when Workflow A inputs are missing; ask the smallest next question.
- Writing feedback is not a software bug by default. If feedback reveals a reusable account voice/copy preference, update the account writing memory hierarchy instead: `writing/pattern-extractions.md` for raw notes, `writing/refinement-personas.md` for preflight/self-critique behavior, and `writing.md` only for stable account-level rules.
- Use `BUGS.md` only for real workflow/tooling failures or implementation bugs. If a writing critique also exposes a process bug, the BUGS entry must point to the account writing files that were updated so the feedback compounds where drafting agents retrieve it.
- Do not lock new account `writing.md` or `design.md` until Workflow A3 or `account-quality-gate` produces an approved non-hero sample slide.
- If a quality-gate sample is rejected, capture the raw criticism in the current attempt's `iteration-notes.md` and update `writing/refinement-personas.md` before the next attempt.
- Do not overwrite prior quality-gate attempts; create a new attempt subfolder for each new user-reviewable quality-gate sample.
- Do not create `presets.md` before baseline writing/design quality passes; use Workflow A4 for validated angle-to-preset extraction.
- Do not copy hooks verbatim from `references/hook-ideas/`; abstract the reusable pattern and adapt it through account writing rules.
- If a broad post idea is not a locked angle and final copy, use the concept flow before creating `flow.md`.
- For Workflow B and copy iteration requests, paste the full slide-by-slide copy
  in chat first. Do not write final `flow.md`, source images, run Workflow C, or
  render PNGs until the user explicitly approves the copy.
- After copy approval, write `flow.md` from the approved copy exactly. Preserve
  approved wording and manual line breaks during rendering.
- Preserve manual line breaks from `flow.md` during rendering; do not rewrite slide copy inside `process_images.py`.

## graphify

This project has a graphify knowledge graph at graphify-out/.

Rules:
- Before answering architecture or codebase questions, read graphify-out/GRAPH_REPORT.md for god nodes and community structure
- If graphify-out/wiki/index.md exists, navigate it instead of reading raw files
- For cross-module "how does X relate to Y" questions, prefer `graphify query "<question>"`, `graphify path "<A>" "<B>"`, or `graphify explain "<concept>"` over grep — these traverse the graph's EXTRACTED + INFERRED edges instead of scanning files
- After modifying code files in this session, run `graphify update .` to keep the graph current (AST-only, no API cost)
- After modifying account writing memory files (`accounts/{account}/writing.md`, `writing/refinement-personas.md`, `writing/pattern-extractions.md`) or feedback-routing docs, run `graphify update .` so future account drafting, Creative DNA, and hook ideation can retrieve the new writing preference. If graphify is unavailable, state that the writing memory was updated but graph refresh failed.

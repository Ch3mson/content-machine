# Agent Router

This file is the first document an agent should read in this workspace.

The user's workflow tag is an instruction, not a topic mention. If the user says
`workflow a`, `workflow b`, `workflow c`, `source images`, `process images`, or
asks for angle/variant brainstorming, start the matching workflow or skill and
use the listed tools without waiting for another prompt.

## Workflow Tags

| User tag or intent | Start here | What to do |
| --- | --- | --- |
| `workflow a`, `workflow-a`, `new account`, `onboard account` | `workflows/workflow-a-new-account.md` | Create or update a new account playbook. |
| `workflow b`, `workflow-b`, `new post`, `make post`, `existing account post` | `workflows/workflow-b-new-post.md` | Create a slideshow post for an existing account. |
| `workflow c`, `image processing`, `process images`, `render slides` | `workflows/workflow-c-image-processing.md` | Turn mapped raw images and copy into final 9:16 slides. |
| `source images`, `find images`, `Pinterest images` | `tools/image-sourcer/README.md` | Use the image sourcing tool and the post `image_preset.json`. |
| `stop slop`, `anti-AI writing`, `clean copy` | `references/skills/stop-slop/SKILL.md` | Apply writing cleanup and QA rules. |
| `3 variants`, `three variants`, `3 angles`, `angle concepts`, `brainstorm variants`, `overall angle` | `references/skills/angle-variants/SKILL.md` | Generate three account-adapted angle concepts in chat, not slide copy. |
| `product`, `w(inner)`, `claim`, `app mention` | `product/app-brief.md` and `product/claim-bank.md` | Check product facts and approved claims before writing. |

If the user tags multiple workflows, run them in the order stated. Example:
`workflow a and workflow b` means onboard or update the account first, then create
the post once the required account files exist.

## Retrieval Order

Use the smallest relevant set of files.

1. Read this `AGENTS.md`.
2. Read the selected workflow in `workflows/` or skill in `references/skills/`.
3. Read `product/app-brief.md` and `product/claim-bank.md` before any product
   mention or product claim.
4. Read the target account files:
   - `accounts/{account}/account-brief.md`
   - `accounts/{account}/presets.md`, if present
   - `accounts/{account}/writing.md`
   - `accounts/{account}/image.md`
   - `accounts/{account}/sources.md`
5. Read only the post folder being worked on.
6. Read tool docs only when the workflow calls for a tool.

## Directory Contract

| Directory | Contents |
| --- | --- |
| `workflows/` | Agent procedures and trigger behavior. |
| `accounts/` | Account playbooks and post workspaces. |
| `product/` | Shared w(inner) product facts, claims, and assets. |
| `references/` | Templates, research rules, inspiration accounts, and vendored writing skills. |
| `tools/` | Runnable utilities only. Do not store strategy docs here. |

## Tool Rules

- For image sourcing, use `python tools/image-sourcer/source_images.py <path-to-image_preset.json>`.
- For image processing, use the target post's `process_images.py` if it exists.
  If it does not exist, create it from `workflows/workflow-c-image-processing.md`
  and the account `image.md`.
- If browser image sourcing needs Chrome remote debugging, use
  `python tools/browser-harness/connect_my_chrome.py` or follow
  `tools/image-sourcer/README.md`.
- Do not invent product claims. Use the claim bank.
- Do not invent final account rules when Workflow A inputs are missing. Ask the
  smallest next question.
- Do not stop after drafting when the user asked for an end-to-end post. Continue
  through sourcing, processing, and verification unless a required input is
  missing or the user explicitly asks to review first.

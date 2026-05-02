# Slideshow Test

Docs-first workspace for building social slideshow account playbooks and rendered
TikTok/Instagram carousel slides for w(inner).

Start with `AGENTS.md`. It routes user tags like `workflow a`, `workflow b`,
`process images`, and `source images` to the right workflow and tool chain.

## Quick Routing

| User says | Agent starts |
| --- | --- |
| `workflow a` | `workflows/workflow-a-new-account.md` |
| `workflow a0` or `reference map` | `workflows/workflow-a0-account-intake-reference-map.md` |
| `workflow a1` or `writing extraction` | `workflows/workflow-a1-writing-principle-extraction.md` |
| `workflow a2` or `design extraction` | `workflows/workflow-a2-design-principle-extraction.md` |
| `workflow a3` or `quality gate` | `workflows/workflow-a3-writing-design-quality-gate.md` |
| `workflow a4` or `angle extraction` | `workflows/workflow-a4-angle-extraction-to-presets.md` |
| `workflow b` | `workflows/workflow-b-new-post.md` |
| `workflow c` or `process images` | `workflows/workflow-c-image-processing.md` |
| `source images` | `tools/image-sourcer/README.md` |

## Directory Map

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Mandatory router and retrieval contract for agents. |
| `POST_STATUS.md` | Cross-account post dashboard showing finished posts, in-progress posts, stage, next action, and ready-to-post packs. |
| `workflows/` | Step-by-step procedures for account setup, post creation, and image processing. |
| `accounts/` | Account source-of-truth files, indexed writing folders, quality-gate artifacts, post workspaces, and the quick [accounts index](accounts/INDEX.md). |
| `product/` | w(inner) app brief, claim bank, and product assets. |
| `references/` | Research rules, templates, social references, repo-local skills, and writing QA skill. |
| `tools/` | Runnable utilities such as image sourcing and browser harness. |
| `winner-brief.md` | Raw product brief used to build `product/app-brief.md`. |

## Current Account

`accounts/athlete-max/` is the active account (A0 intake complete, pending A1-A3).

`accounts/athlete-stories/` is a locked reference account. It contains:

- `account-brief.md`
- `presets.md`
- `writing.md`
- `design.md`
- `image.md`
- `sources.md`
- example post folders for LeBron and Michael Jordan

## Common Tasks

Create or update an account:

```text
workflow a for athlete-stories
```

Create a post for an existing account:

```text
workflow b for athlete-stories about Messi
```

Source images from a preset:

```powershell
python tools/image-sourcer/source_images.py accounts/athlete-stories/Lebron/image_preset.json
```

Process a post's images:

```powershell
python accounts/athlete-stories/Lebron/process_images.py
```

Refresh the post dashboard and ready-to-post folders:

```powershell
python tools/post-tracker/update_post_status.py
```

## Definition Of Done

- The selected workflow was followed from `workflows/`.
- Product mentions match `product/app-brief.md` and `product/claim-bank.md`.
- Account copy follows `writing.md`, its indexed subfiles when required, and the
  Stop Slop QA rules.
- Visual layout follows account `design.md`; photo direction and treatment follow
  account `image.md`.
- New account `writing.md` and `design.md` are not locked until a Workflow A3
  non-hero sample slide is approved.
- Processed slides match the canvas size in account `design.md`.

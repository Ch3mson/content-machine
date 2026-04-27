# Slideshow Test

Docs-first workspace for building social slideshow account playbooks and rendered
TikTok/Instagram carousel slides for w(inner).

Start with `AGENTS.md`. It routes user tags like `workflow a`, `workflow b`,
`process images`, and `source images` to the right workflow and tool chain.

## Quick Routing

| User says | Agent starts |
| --- | --- |
| `workflow a` | `workflows/workflow-a-new-account.md` |
| `workflow b` | `workflows/workflow-b-new-post.md` |
| `workflow c` or `process images` | `workflows/workflow-c-image-processing.md` |
| `source images` | `tools/image-sourcer/README.md` |

## Directory Map

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Mandatory router and retrieval contract for agents. |
| `workflows/` | Step-by-step procedures for account setup, post creation, and image processing. |
| `accounts/` | Account source-of-truth files and post workspaces. |
| `product/` | w(inner) app brief, claim bank, and product assets. |
| `references/` | Research rules, templates, social references, and writing QA skill. |
| `tools/` | Runnable utilities such as image sourcing and browser harness. |
| `winner-brief.md` | Raw product brief used to build `product/app-brief.md`. |

## Current Account

`accounts/athlete-stories/` is the active locked account. It contains:

- `account-brief.md`
- `presets.md`
- `writing.md`
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

## Definition Of Done

- The selected workflow was followed from `workflows/`.
- Product mentions match `product/app-brief.md` and `product/claim-bank.md`.
- Account copy follows `writing.md` and the Stop Slop QA rules.
- Visual output follows `image.md`.
- Processed slides are exactly 1080x1920 PNG files.

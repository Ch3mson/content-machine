# Accounts Index

Use this as the fast navigation page for account playbooks, posts that are ready to publish, flows that need review, and active draft workspaces.

Primary dashboards:

- [Cross-account post status](../POST_STATUS.md)
- [Accounts README / folder contract](README.md)

Refresh the dashboards and ready-to-post packs after post changes:

```powershell
python tools/post-tracker/update_post_status.py
```

## Table Of Contents

- [Ready To Post](#ready-to-post)
- [Processed / Rendered Slides](#processed--rendered-slides)
- [Flows Or Posts Needing Review](#flows-or-posts-needing-review)
- [Active Draft / Concept Workspaces](#active-draft--concept-workspaces)
- [Account Dashboards](#account-dashboards)
- [Account Source Of Truth](#account-source-of-truth)
- [Standard Folder Map](#standard-folder-map)

## Ready To Post

These folders are clean publish packs. They should contain only `flow.md` and final `slide_*.png` files.

| Account | Post | Ready pack | Flow | Slides |
| --- | --- | --- | --- | --- |
| athlete-stories | Lebron | [ready-to-post/Lebron](athlete-stories/ready-to-post/Lebron) | [flow](athlete-stories/ready-to-post/Lebron/flow.md) | 7 |
| athlete-stories | Messi | [ready-to-post/Messi](athlete-stories/ready-to-post/Messi) | [flow](athlete-stories/ready-to-post/Messi/flow.md) | 7 |
| athlete-stories | Michael Jordan | [ready-to-post/Michael Jordan](athlete-stories/ready-to-post/Michael%20Jordan) | [flow](athlete-stories/ready-to-post/Michael%20Jordan/flow.md) | 7 |

## Processed / Rendered Slides

Use this table when you mainly want to inspect the rendered PNGs for each account. These are source workspace renders; the clean publishing copies still live in [Ready To Post](#ready-to-post).

| Account | Post | Processed slides | Flow | Slides | Status |
| --- | --- | --- | --- | --- | --- |
| athlete-max | mistake-confidence-loop | [processed](athlete-max/posts/mistake-confidence-loop/processed) | [flow](athlete-max/posts/mistake-confidence-loop/flow.md) | 13 | Rendered workspace |
| athlete-max | biological-roi-soccer-confidence | [processed](athlete-max/posts/biological-roi-soccer-confidence/processed) | [flow](athlete-max/posts/biological-roi-soccer-confidence/flow.md) | 7 | Rendered, assets still marked pending |
| athlete-max | center-back-late-runner | [processed](athlete-max/posts/center-back-late-runner/processed) | [flow](athlete-max/posts/center-back-late-runner/flow.md) | 6 | Rendered draft |
| athlete-stories | Lebron | [processed](athlete-stories/Lebron/processed) | [flow](athlete-stories/Lebron/flow.md) | 7 | Source render; publish pack ready |
| athlete-stories | Messi | [processed](athlete-stories/Messi/processed) | [flow](athlete-stories/Messi/flow.md) | 7 | Source render; publish pack ready |
| athlete-stories | Michael Jordan | [processed](athlete-stories/Michael%20Jordan/processed) | [flow](athlete-stories/Michael%20Jordan/flow.md) | 7 | Source render; publish pack ready |

## Flows Or Posts Needing Review

Use this section when you want to find work that is not ready to publish yet.

| Account | Post | Current stage | Next action | Workspace | Flow / Draft |
| --- | --- | --- | --- | --- | --- |
| athlete-max | biological-roi-soccer-confidence | Rendered, assets still marked pending | Source/map final images or remove pending markers, then rerun tracker | [workspace](athlete-max/posts/biological-roi-soccer-confidence) | [flow](athlete-max/posts/biological-roi-soccer-confidence/flow.md) |
| athlete-max | center-back-late-runner | Rendered draft | Approve final copy/assets, update flow status, then rerun tracker | [workspace](athlete-max/posts/center-back-late-runner) | [flow](athlete-max/posts/center-back-late-runner/flow.md) |
| athlete-stories | CR7 | Images collected, no flow | Draft/approve copy and map images | [legacy workspace](athlete-stories/CR7) | - |

## Active Draft / Concept Workspaces

Concept folders are pre-approval materials: intake, VOC, source checks, selected angle, copy options, and review notes. Final `flow.md` should only be written after explicit copy approval.

| Account | Post | Concept folder | Key draft files | Rendered draft |
| --- | --- | --- | --- | --- |
| athlete-max | biological-roi-soccer-confidence | [concept](athlete-max/posts/biological-roi-soccer-confidence/concept) | [copy review](athlete-max/posts/biological-roi-soccer-confidence/concept/copy-review.md), [copy options](athlete-max/posts/biological-roi-soccer-confidence/concept/copy-options.md), [VOC research](athlete-max/posts/biological-roi-soccer-confidence/concept/voc-research.md) | [processed](athlete-max/posts/biological-roi-soccer-confidence/processed) |
| athlete-max | center-back-late-runner | [concept](athlete-max/posts/center-back-late-runner/concept) | [intake](athlete-max/posts/center-back-late-runner/concept/intake.md), [selected angle](athlete-max/posts/center-back-late-runner/concept/selected-angle.md), [source check](athlete-max/posts/center-back-late-runner/concept/source-check.md) | [processed](athlete-max/posts/center-back-late-runner/processed) |

## Account Dashboards

| Account | Dashboard | Posts folder | Ready-to-post folder | Notes |
| --- | --- | --- | --- | --- |
| athlete-max | [post-status](athlete-max/post-status.md) | [posts](athlete-max/posts) | `ready-to-post/` not present yet | Active account workspaces. |
| athlete-stories | [post-status](athlete-stories/post-status.md) | [posts](athlete-stories/posts) | [ready-to-post](athlete-stories/ready-to-post) | Locked reference account with completed examples. |
| Athlete-user-soccer | [post-status](Athlete-user-soccer/post-status.md) | `posts/` not present yet | `ready-to-post/` not present yet | No post workspaces found yet. |
| makebrainrotvideos | - | `posts/` not present yet | `ready-to-post/` not present yet | New account. A0 intake complete. Needs references for A1/A2. |

## Account Source Of Truth

Open these before writing or rendering for an account.

| Account | Brief | Writing | Design | Image | Sources | Presets | README |
| --- | --- | --- | --- | --- | --- | --- | --- |
| athlete-max | [brief](athlete-max/account-brief.md) | [writing](athlete-max/writing.md) | [design](athlete-max/design.md) | [image](athlete-max/image.md) | - | [presets](athlete-max/presets.md) | [README](athlete-max/README.md) |
| athlete-stories | [brief](athlete-stories/account-brief.md) | [writing](athlete-stories/writing.md) | [design](athlete-stories/design.md) | [image](athlete-stories/image.md) | [sources](athlete-stories/sources.md) | [presets](athlete-stories/presets.md) | [README](athlete-stories/README.md) |
| Athlete-user-soccer | - | - | - | - | - | - | - |
| makebrainrotvideos | [brief](makebrainrotvideos/account-brief.md) | [writing](makebrainrotvideos/writing.md) | [design](makebrainrotvideos/design.md) | [image](makebrainrotvideos/image.md) | - | - | - |

## Standard Folder Map

```text
accounts/
  INDEX.md                         # this navigation page
  README.md                        # account folder rules and workflow contract
  {account}/
    post-status.md                 # account-specific post dashboard
    account-brief.md               # audience, POV, product relationship, open questions
    writing.md                     # voice, rhythm, banned patterns, copy QA
    design.md                      # canvas, layout, typography, rendering rules
    image.md                       # photo direction and visual treatment
    sources.md                     # approved claim/source constraints, if needed
    presets.md                     # validated repeatable post patterns, if present
    posts/{post-slug}/             # source workspace for active/new posts
      concept/                     # pre-approval research and draft copy
      flow.md                      # approved slide copy and image mapping
      processed/                   # rendered draft slides
    ready-to-post/{post-slug}/     # clean publishing pack only
      flow.md
      slide_*.png
```

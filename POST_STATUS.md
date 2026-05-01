# Post Status Dashboard

Generated: 2026-05-01

Use this as the quick view for every account and post. In-progress work stays in the source workspace; finished posting packs are copied to each account's `ready-to-post/` folder.

## Funnel

| Stage | Where it lives | What it means |
| --- | --- | --- |
| Concept / copy review | `accounts/{account}/posts/{post}/concept/` or legacy post folder | Idea, VOC, angle, or draft copy exists, but final `flow.md` is not ready. |
| Flow approved | post workspace `flow.md` | Copy is ready, but images or rendering are not complete. |
| Images sourced | post workspace `sourced/` | Raw images exist and need mapping/rendering. |
| Rendered draft | post workspace `processed/` | PNGs exist, but the flow still marks draft or pending assets. |
| Ready to post | `accounts/{account}/ready-to-post/{post}/` | Folder contains only `flow.md` and final `slide_*.png` files. |

## Global Table

| Account | Post | Status | Stage | Slides | Next action | Workspace | Ready pack | Flow |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [athlete-max](accounts/athlete-max/post-status.md) | biological-roi-soccer-confidence | In Progress | Rendered, assets still marked pending | 7 | Source/map final images or remove pending markers, then rerun tracker | [posts/biological-roi-soccer-confidence](accounts/athlete-max/posts/biological-roi-soccer-confidence) | - | [flow](accounts/athlete-max/posts/biological-roi-soccer-confidence/flow.md) |
| [athlete-max](accounts/athlete-max/post-status.md) | center-back-late-runner | In Progress | Rendered draft | 6 | Approve final copy/assets, update flow status, then rerun tracker | [posts/center-back-late-runner](accounts/athlete-max/posts/center-back-late-runner) | - | [flow](accounts/athlete-max/posts/center-back-late-runner/flow.md) |
| [athlete-stories](accounts/athlete-stories/post-status.md) | Lebron | Done | Ready to post | 7 | Post from ready-to-post pack | [Lebron](accounts/athlete-stories/Lebron) | [Lebron](accounts/athlete-stories/ready-to-post/Lebron) | [flow](accounts/athlete-stories/ready-to-post/Lebron/flow.md) |
| [athlete-stories](accounts/athlete-stories/post-status.md) | Messi | Done | Ready to post | 7 | Post from ready-to-post pack | [Messi](accounts/athlete-stories/Messi) | [Messi](accounts/athlete-stories/ready-to-post/Messi) | [flow](accounts/athlete-stories/ready-to-post/Messi/flow.md) |
| [athlete-stories](accounts/athlete-stories/post-status.md) | Michael Jordan | Done | Ready to post | 7 | Post from ready-to-post pack | [Michael Jordan](accounts/athlete-stories/Michael%20Jordan) | [Michael Jordan](accounts/athlete-stories/ready-to-post/Michael%20Jordan) | [flow](accounts/athlete-stories/ready-to-post/Michael%20Jordan/flow.md) |
| [athlete-stories](accounts/athlete-stories/post-status.md) | CR7 | In Progress | Images collected, no flow | - | Draft/approve copy and map images | [CR7](accounts/athlete-stories/CR7) | - | - |

## Account Dashboards

- [athlete-max](accounts/athlete-max/post-status.md)
- [athlete-stories](accounts/athlete-stories/post-status.md)
- [Athlete-user-soccer](accounts/Athlete-user-soccer/post-status.md)

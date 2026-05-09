# Post Status Dashboard

Generated: 2026-05-02

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

| makebrainrotvideos | 1-3k-month-ai-videos | Done | Ready to post | 6 | Post from ready-to-post pack | [posts/1-3k-month-ai-videos](accounts/makebrainrotvideos/posts/1-3k-month-ai-videos) | [ready-to-post/1-3k-month-ai-videos](accounts/makebrainrotvideos/ready-to-post/1-3k-month-ai-videos) | [flow](accounts/makebrainrotvideos/ready-to-post/1-3k-month-ai-videos/flow.md) |
| makebrainrotvideos | 2-5-viral-faceless-formats | Done | Ready to post | 7 | Post from ready-to-post pack | [posts/2-5-viral-faceless-formats](accounts/makebrainrotvideos/posts/2-5-viral-faceless-formats) | [ready-to-post/2-5-viral-faceless-formats](accounts/makebrainrotvideos/ready-to-post/2-5-viral-faceless-formats) | [flow](accounts/makebrainrotvideos/ready-to-post/2-5-viral-faceless-formats/flow.md) |
| makebrainrotvideos | 3-stuck-at-200-views | Done | Ready to post | 7 | Post from ready-to-post pack | [posts/3-stuck-at-200-views](accounts/makebrainrotvideos/posts/3-stuck-at-200-views) | [ready-to-post/3-stuck-at-200-views](accounts/makebrainrotvideos/ready-to-post/3-stuck-at-200-views) | [flow](accounts/makebrainrotvideos/ready-to-post/3-stuck-at-200-views/flow.md) |

## Account Dashboards


- makebrainrotvideos

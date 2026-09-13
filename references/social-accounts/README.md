# Social Accounts Reference Memory

Raw reference posts from other accounts. The photos are evidence for hook
extraction and composition boards, not account rules.

## Layout

```text
references/social-accounts/
  {account}/Post {id}/1.jpg, 2.jpg, ...   # raw slides as downloaded
```

Current folders:

| Account | Post | What it is | Used for |
| --- | --- | --- | --- |
| `user-sophia.study-study` | `Post 7629054163342658838` | @sophia.study library study carousel | Slide 1 became `accounts/antigpt/boards/library-head-on-hand.jpg` |

## Adding a reference

TikTok photo post:

```bash
python tools/tiktok-photo-sourcer/download_tiktok_photos.py --account {handle} --post {id} "{url}"
```

If a slide is a good composition for the avatar, copy it to
`accounts/antigpt/boards/{descriptive-slug}.jpg` and add the row to the Boards
table in `accounts/antigpt/README.md`. The raw post stays here as the source.

If the post has a reusable hook, extract it with
`references/skills/hook-idea-extraction/SKILL.md` into `../hook-ideas/cards/`.

## Usage Rule

Do not copy source hooks verbatim. Pull the transferable pattern, rewrite it in
the account voice, and log the reuse in `../hook-ideas/usage-ledger.md`.

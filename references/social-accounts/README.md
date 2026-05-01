# Social Accounts Reference Memory

This folder stores raw reference slideshow screenshots from outside accounts.
The screenshots are evidence, not the memory system. Use these index files to
find reusable hooks, patterns, and account fits without re-opening every image.

## Start Here

| File | Use |
| --- | --- |
| `account-map.md` | Pick a reference account by niche, content role, and reuse value. |
| `visual-index.md` | Jump to each account folder, account overview sheet, and per-post combined sheet. |
| `post-index.md` | Find a specific post by hook, pattern, niche, account fit, and extraction status. |
| `taxonomy.md` | Understand the reusable hook and post-pattern labels used in the index. |
| `{account}/README.md` | Account-local table of contents for raw post folders and review sheets. |
| `{account}/review/` | Account-local visual review sheets generated from that account's raw post folders. |
| `_review/contact-sheets/` | Cross-account review sheets only. Do not put account-specific combined posts here. |
| `../hook-ideas/usage-ledger.md` | Track where extracted hooks or patterns have been used in your own accounts. |
| `../../tools/hook-extraction/` | Update hook card, hook index, post index, taxonomy, and usage ledger from one extraction manifest. |

## Memory Layers

1. Raw post folders preserve the source screenshots.
2. Account-local `review/` folders make each post visually scannable.
3. `post-index.md` turns each raw post into a searchable strategic record.
4. Hook cards in `../hook-ideas/cards/` store high-value reusable patterns.
5. `../hook-ideas/usage-ledger.md` records reuse so a pattern does not become invisible or overused.

## Status Labels

| Status | Meaning |
| --- | --- |
| `raw-indexed` | Visually reviewed and classified, but no full hook card exists yet. |
| `raw-unindexed` | Raw slides and/or visual sheets exist, but the post has not been strategically classified yet. |
| `candidate-hook-card` | Strong enough to extract into `references/hook-ideas/cards/`. |
| `hook-carded` | Extracted into a hook card and linked from the hook index. |
| `candidate-angle` | Could become an account-specific angle after adaptation. |
| `reference-only` | Useful for visual style or niche context, but weak as a portable hook. |
| `empty-folder` | Folder exists, but no source slides were present during review. |

## Extraction Automation

When extracting a social-account post into a hook card:

1. Fill `../hook-ideas/templates/social-post-extraction.json` with the analysis.
2. Run `python tools/hook-extraction/update_hook_extraction.py <manifest-path> --dry-run`.
3. If the dry run is clean, rerun without `--dry-run`.

The updater keeps dependent docs moving together: hook card, hook index,
source-post status, taxonomy derivation link, and optional usage-ledger rows.

## Usage Rule

Do not copy source hooks verbatim. Pull the transferable pattern, adapt it
through the target account's `writing.md`, and log the reuse in
`../hook-ideas/usage-ledger.md`.

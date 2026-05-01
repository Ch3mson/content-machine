# Hook Extraction Updater

Use this after a social-account post has been analyzed and you want the
extraction to update all memory documents in one pass.

## Command

```powershell
python tools/hook-extraction/update_hook_extraction.py `
  references/hook-ideas/templates/social-post-extraction.json
```

Pass `--dry-run` to validate the manifest without writing files.

## What It Updates

Given one extraction manifest, the updater can:

- Create or replace one hook card in `references/hook-ideas/cards/`.
- Add or update the row in `references/hook-ideas/index.md`.
- Mark the source row in `references/social-accounts/post-index.md` as `hook-carded`.
- Add the source post link to the matching archetype in `references/social-accounts/taxonomy.md`.
- Append optional usage rows to `references/hook-ideas/usage-ledger.md`.

This is intentionally one transaction-like command instead of separate manual
edits. True parallel writes to the same markdown files would create avoidable
merge conflicts; this gives the same workflow benefit while keeping the docs
consistent.

## Manifest Rule

The manifest is the extraction source of truth. Fill it from the post analysis,
then run the updater. Do not edit the generated hook-card row in one file and
forget the other indexes.


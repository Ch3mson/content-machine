# Notion Knowledge Map

Connected workspace: **Antigpt**. Inspected 2026-09-13 via Notion MCP.
Notion is the broad research library; the repo holds the operational context
and artifacts needed to produce posts. No automatic two-way sync is configured.

## Entry points

| Source | Use |
| --- | --- |
| [AntiGPT Knowledge](https://app.notion.com/p/3c796b26bfaa8182b55de5fc6d115d93) | Main hub; links to product/brand pages, research, decisions, and databases. |
| [Research](https://app.notion.com/p/3c796b26bfaa8170b44ff7419271df7d) | Daily research split by X, Instagram, and TikTok. |
| [Winning formats](https://app.notion.com/p/7ba526c8524942feaca49a97b9e245fc) | Research-bot keepers and source formats to adapt. |
| [Draft queue](https://app.notion.com/p/1a48be3ddfb44f74aa829708193d2d93) | Cross-channel draft ideas; not the status authority for local numbered posts. |
| [Winner log](https://app.notion.com/p/ddbd1cd1457c429391831fae528cce39) | Existing knowledge-base log; inspect its schema before recording results. |
| [Decisions](https://app.notion.com/p/3c796b26bfaa817c8ecfcfb311802a07) | Dated decisions; check platform, date, and applicability to current work. |
| [Organic App Growth Playbook](https://app.notion.com/p/3d896b26bfaa810cb395f7c49d99291a) | Research about problem-first content and testing. Source claims are hypotheses, not account commitments. |

The hub, Decisions, and Organic App Growth Playbook pages were fetched for
this setup. Other links above were discovered through the hub/search; their
complete contents and database schemas have not been audited.

## Retrieval

1. Read the relevant local account/skill instructions to establish the task.
2. If connection access is unknown, fetch `self`. Choose `ai_search` when its
   reported status is available; otherwise use `search` with short keywords.
   Keyword search and page fetch worked on 2026-09-13; AI search was plan-gated.
3. Fetch a known page directly, or search for one topic (for example `UGC`,
   `study`, `sophia`, or a creator name), then fetch the relevant results.
4. Check source dates, platform, original links, and incomplete/truncated
   content. Fetch a database/data-source schema before trying to query it.
5. Cite the page used in the hook card, post record, or adopted account rule.
   Distinguish what the source says from the choice we make for this account.

If Notion is unavailable, use the local operational files and identify the
research gap. Do not claim to have fetched or verified a source that failed.
Read access does not imply a request to modify Notion or the bots' routines.

## What stays in Git

- `AGENTS.md`, `FOLDERS.md`, and the canonical skills: how agents work here.
- `accounts/antigpt/README.md` and `account-brief.md`: current format and voice.
- `product/antigpt-brief.md` and `antigpt-claim-bank.md`: production facts and
  wording boundaries, with their dates and sources.
- Post records and media, the avatar lock, selected boards, and tool docs.
- Existing hook cards/source captures that production skills reference.

Keep new broad research in Notion. A local note should add an operational
decision, source evidence required by a tool, or a reusable pattern tied to a
production task. Link to Notion instead of exporting entire pages by default.

## Known differences and gaps

- The fetched Decisions page still describes September 10 slideshow packs
  and X workflows. This repo's current account hub specifies a single avatar
  still. Do not silently restore slideshows from older research.
- Notion's older no-bypass wording differs from the repo's claim bank. Surface
  that conflict when it matters to copy; use the current user's instruction
  and the applicable local production contract. Research never creates a new
  approved product claim by itself.
- The knowledge hub's visible site label contains a link to `antigpt.app`;
  that is a different product. This repo uses `antigpt.me`.
- The page titled “Organic App Growth Playbook full PDF” contains analysis
  and references `/workspace/brainextends-organic-playbook.pdf`, its text
  extract, and `/workspace/brainextends-playbook-analysis.md` on another
  machine. The fetched page does not contain the complete PDF/transcript.
  A page title or external filesystem path is not a verified backup.

Before removing a local knowledge file, confirm the complete replacement is
accessible, preserve any unique decisions/evidence, and update every active
caller. This setup retains the remaining local knowledge files; it does not
assert that Claude's earlier deleted files were migrated into Notion.

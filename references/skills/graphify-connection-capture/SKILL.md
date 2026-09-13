---
name: graphify-connection-capture
description: Save useful reasoning connections, analogy links, mechanism transfers, and cross-file insights from a response into markdown artifacts that Graphify can index. Use when the user says save this connection, graphify this connection, remember this link, capture this reasoning, add this to the graph, or wants an idea/insight from brainstorming preserved for future retrieval.
---

# Skill: Graphify Connection Capture

Use this when a conversation produces a useful connection that should become
retrievable later through Graphify or account ideation.

This skill does **not** save private chain-of-thought. It saves a concise,
user-visible reasoning artifact: the connection, why it matters, source nodes,
target nodes, and how it should be reused.

## Trigger Phrases

- `save this connection`
- `graphify this connection`
- `remember this link`
- `capture this reasoning`
- `add this to the graph`
- `save the connection you made`
- `make this retrievable later`
- `store this mechanism transfer`

Also use this when the user explicitly wants the relationships behind an answer
preserved for future brainstorming.

## When To Use This vs Existing Skills

Use **this skill** when the memory is a relationship:

```text
source idea → mechanism → transferable principle → target account/use case
```

When the memory is a writing taste correction (bad phrase → better phrase →
account rule), write it into `accounts/antigpt/account-brief.md` under Copy
Rules For The Still instead of using this skill.

When the connection is a reusable hook mechanic from a reference post, prefer a
hook card via `references/skills/hook-idea-extraction/SKILL.md`.

## Read First

Use the smallest relevant set:

1. `AGENTS.md`
2. This file
3. `graphify-out/GRAPH_REPORT.md`, if present
4. `references/hook-ideas/index.md` when the connection concerns hooks or
   reference posts
5. Account files only if account constraints matter:
   - `accounts/antigpt/README.md`
   - `accounts/antigpt/account-brief.md`

## Storage Locations

Default connection file (create the folder if it does not exist):

```text
references/connection-captures/{yyyy-mm-dd}-{short-slug}.md
```

If the connection changes how captions are written, also add the rule to
`accounts/antigpt/account-brief.md` and link the capture file from it.

## Capture Format

Create or append a markdown artifact using this structure:

```md
# Connection Capture: [short descriptive title]

Date: YYYY-MM-DD
Status: raw | validated | promoted
Scope: general | hook-mechanic | account-specific | product | workflow

## Source Nodes

- [source idea, file, post, niche, user prompt, or concept]

## Target Nodes

- [target account, post idea, workflow, writing rule, product claim, or use case]

## Connection

[One concise paragraph explaining the relationship.]

## Transferable Principle

[The abstract reusable pattern.]

## Why It Matters

[How this improves future ideation, writing, hooks, workflow decisions, or graph retrieval.]

## Reuse Instructions

- Use when:
- Avoid when:
- Best workflow route:

## Related Files

- `path/to/source.md`
- `path/to/target.md`

## Graph Tags

- mechanism: [name]
- lever: [psychological/emotional lever]
- account: [account or none]
- workflow: [workflow/skill]
```

## Rules For Capturing Reasoning

- Do not reveal hidden chain-of-thought.
- Save only a concise explanation the user can read and reuse.
- Prefer explicit node names and file paths so Graphify can connect the artifact.
- If the insight came from multiple sources, list each source under `Source Nodes`.
- If the connection is speculative, mark `Status: raw`.
- If the user approved it or it has evidence from source files, mark `Status: validated`.
- If it is merged into account rules or a hook card, mark `Status: promoted` and
  link the promoted file.

## Graphify Update

After writing or editing a connection artifact, refresh Graphify:

```text
graphify update .
```

If the connection is mostly semantic docs/content and the lightweight update says
docs need a fuller update, tell the user:

```text
Saved the connection. Lightweight Graphify update ran, but a fuller semantic
Graphify update may be needed for deeper doc-level retrieval.
```

## Chat Response

Keep it short:

```md
Saved the connection to `references/connection-captures/{file}.md` and refreshed Graphify.

Connection captured: [source] → [principle] → [target/reuse].
```

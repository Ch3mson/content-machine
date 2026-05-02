---
name: graphify-connection-capture
description: Save useful reasoning connections, analogy links, mechanism transfers, and cross-file insights from a response into markdown artifacts that Graphify can index. Use when the user says save this connection, graphify this connection, remember this link, capture this reasoning, add this to the graph, or wants an idea/insight from brainstorming preserved for future retrieval.
---

# Skill: Graphify Connection Capture

Use this when a conversation produces a useful connection that should become
retrievable later through Graphify, Creative DNA, or account ideation.

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
- `this is a useful Creative DNA connection`
- `store this mechanism transfer`

Also use this when the user explicitly wants the relationships behind an answer
preserved for future brainstorming.

## When To Use This vs Existing Skills

Use **this skill** when the memory is a relationship:

```text
source idea → mechanism → transferable principle → target account/use case
```

Use `writing-feedback-compounding` instead when the memory is a writing taste
correction:

```text
bad phrase/style → better phrase/style → account writing rule
```

Use Creative DNA files when the connection is specifically a cross-niche viral
mechanism that should become part of the Creative DNA system.

## Read First

Use the smallest relevant set:

1. `AGENTS.md`
2. This file
3. `graphify-out/GRAPH_REPORT.md`
4. Creative DNA files only if the connection concerns viral mechanisms,
   cross-niche inspiration, hooks, or account idea transfer:
   - `references/creative-dna/README.md`
   - `references/creative-dna/owned-account-idea-router.md`
   - `references/creative-dna/cross-niche-principle-map.md`
5. Target account files only if account constraints matter:
   - `accounts/{account}/account-brief.md`
   - `accounts/{account}/writing.md`
   - `accounts/{account}/presets.md`, if present

## Storage Locations

Default general connection file:

```text
references/connection-captures/{yyyy-mm-dd}-{short-slug}.md
```

For Creative DNA mechanism transfers, prefer:

```text
references/creative-dna/extractions/{short-slug}.md
```

For account-specific ideation memories, use:

```text
accounts/{account}/writing/pattern-extractions.md
```

only if the connection changes writing behavior; otherwise keep it in
`references/connection-captures/` and link the account in the metadata.

## Capture Format

Create or append a markdown artifact using this structure:

```md
# Connection Capture: [short descriptive title]

Date: YYYY-MM-DD
Status: raw | validated | promoted
Scope: general | Creative DNA | account-specific | product | workflow

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
- If it is merged into Creative DNA/account rules, mark `Status: promoted` and link
  the promoted file.

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

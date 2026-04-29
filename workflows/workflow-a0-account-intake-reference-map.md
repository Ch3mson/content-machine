# Workflow A0: Account Intake And Reference Map

Use this when the user says `workflow a0`, `account intake`, `reference map`, or
when Workflow A starts a new account.

Goal: define the account and organize every competitor, inspiration, image, and
post reference before extraction begins.

## Read First

1. `../AGENTS.md`
2. `workflow-a-new-account.md`
3. `../references/templates/account-brief.md`
4. Existing `../accounts/{account}/` files, if present
5. Product files only if the account may mention w(inner):
   - `../product/app-brief.md`
   - `../product/claim-bank.md`

## Procedure

1. Resolve the account.
   - Identify `{account}` from the user prompt or use the active account only if
     the user did not name another account. Before begining, make sure to gain
     clarification on what account(s) the user wants to reference.
   - Use `accounts/{account}/` as the workspace.

2. Clarify account intent.
   - Capture niche, audience, platform priority, primary performance goal,
     product relationship, claim sensitivity, emotional tone, and what the
     account should never sound like.
   - Ask the smallest next question if any of those decisions are missing.

3. Create or update `account-brief.md`.
   - Use `../references/templates/account-brief.md`.
   - Mark unknowns in `Open Questions`; do not invent them.

4. Build `extractions/reference-map.md`.
   - List every inspiration account, screenshot folder, post, transcript, image,
     source note, or user-provided example.
   - Mark what each reference informs: `writing`, `design`, `image`, `angle`,
     `research`, or `product`.
   - Record why the user likes it and what should not be copied.

5. Stop if the material is not enough.
   - Do not proceed to writing extraction without writing-relevant examples.
   - Do not proceed to design extraction without design-relevant examples.
   - Ask only for the missing reference type.

## `reference-map.md` Format

```md
# Reference Map

## Account

- Account:
- Stage:
- Last updated:

## References

| Reference | Location | Format                                        | Informs                                     | Why it matters | Do not copy | Status  |
| --------- | -------- | --------------------------------------------- | ------------------------------------------- | -------------- | ----------- | ------- |
|           |          | screenshot / transcript / notes / post folder | writing / design / image / angle / research |                |             | pending |

## Extraction Notes

- Writing references ready:
- Design references ready:
- Image references ready:
- Angle references ready:
- Missing:
```

## Outputs

- `accounts/{account}/account-brief.md`
- `accounts/{account}/extractions/reference-map.md`

## Agent Rules

- Do not analyze deeply in this workflow; organize inputs for later workflows.
- Do not create `writing.md`, `design.md`, or `presets.md` here.
- If the user provides a broad post idea instead of account references, route
  post development to `references/skills/post-concept-flow/SKILL.md`.

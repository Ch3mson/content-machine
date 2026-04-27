# Slideshow Account Playbook Workflow

This workspace is a docs-first system for building account-specific slideshow rules for TikTok and Instagram.

V1 does not generate final post images. It turns your inputs into reusable source-of-truth files that future AI sessions can use for copy, image direction, and slide structure.

## Workflow Order

1. Use `winner-brief.md` as the raw product brief and keep `product/app-brief.md` as the cleaned global app source of truth.
2. Use `references/agents/account-onboarding.md` to interview the user before finalizing any account files.
3. Create or update the account's `account-brief.md` from the conversation.
4. Add product assets to `product/assets/`, especially app-in-hand images if they help the account feel native.
5. Add competitor slideshow references to `accounts/mens-fitness/inputs/competitor-flow/`.
6. Add Pinterest or design references to `accounts/mens-fitness/inputs/design-images/`.
7. Add optional liked or disliked copy samples to `accounts/mens-fitness/inputs/copy-samples/`.
8. Show brief flow, design, and copy samples to the user for calibration.
9. Run the extraction prompts in `accounts/mens-fitness/prompts.md`.
10. Review the raw extraction files in `accounts/mens-fitness/extractions/`.
11. Distill approved rules into `flow.md`, `writing.md`, and `image.md`.
12. Generate one sample slideshow concept and QA it against the account files.

## Folder Map

- `winner-brief.md`: raw uploaded app brief.
- `product/`: cleaned global app context shared by all accounts.
- `product/claim-bank.md`: approved, rejected, and flagged app claims.
- `references/skills/stop-slop/`: vendored writing skill used as the anti-AI-writing base.
- `references/agents/account-onboarding.md`: agent workflow for interviewing the user, showing samples, and filling account reference files.
- `references/research/README.md`: niche-agnostic guide for deciding what research a new account needs.
- `references/templates/account-brief.md`: generic starter for a new account's conversational brief.
- `references/templates/account-sources.md`: generic `sources.md` starter for future account niches.
- `accounts/mens-fitness/`: pilot account playbook.
- `accounts/mens-fitness/inputs/`: user-provided competitor, design, and copy inputs.
- `accounts/mens-fitness/extractions/`: raw analysis before rules become final.
- `accounts/mens-fitness/flow.md`: slideshow structure source of truth.
- `accounts/mens-fitness/writing.md`: copy voice source of truth.
- `accounts/mens-fitness/image.md`: image and typography source of truth.
- `accounts/mens-fitness/prompts.md`: reusable extraction, generation, and QA prompts.
- `accounts/mens-fitness/sources.md`: lightweight research bank for athlete mental performance claims.

## Creating Another Account

Before writing a new account's source-of-truth files, use `references/agents/account-onboarding.md`.

Then copy `references/templates/account-brief.md` into the new account folder as `account-brief.md`, copy `references/templates/account-sources.md` as `sources.md`, and customize both through the interview and sample-calibration process.

## Definition Of Done For One Account

- `flow.md` explains the competitor-derived format without copying wording, identity, or assets.
- `writing.md` adapts Stop Slop into short slideshow copy rules for the niche.
- `image.md` turns Pinterest/design inputs into practical image generation and editing rules.
- `product/claim-bank.md` separates approved claims from bold claims that need approval.
- The user has reacted to brief flow, design, and copy samples before rules are locked.
- One sample 5-8 slide concept passes the QA checklist in `prompts.md`.

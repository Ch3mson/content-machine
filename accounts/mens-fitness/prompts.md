# Reusable Prompts

Use these prompts to run the account workflow. Replace bracketed fields before use.

## 1. Competitor Flow Extraction

```text
You are extracting slideshow structure for the men's fitness account.

The product is w(inner), a mobile mental performance app for athletes. Do not force it into the slideshow. Identify whether the competitor flow creates a native place for a soft product mention.

Read:
- product/app-brief.md
- product/claim-bank.md
- accounts/mens-fitness/flow.md
- accounts/mens-fitness/writing.md

Analyze these competitor inputs:
[list file paths, screenshots, links, or transcripts]

Extract only structure, not exact wording, visual identity, or assets.

Return markdown for accounts/mens-fitness/extractions/flow-analysis.md with:
- input set
- hook mechanics
- slide order
- slide roles
- pacing and tension
- visual-copy rhythm
- native CTA behavior, if any
- three soft app mention hypotheses if there is no native CTA slot
- whether the app should stay in slideshow, comments, caption, or bio
- what to keep, modify, reject, and ask the user about
```

## 2. Flow Distillation

```text
Using accounts/mens-fitness/extractions/flow-analysis.md, update the final rules for accounts/mens-fitness/flow.md.

Keep:
- reusable structure
- slide roles
- pacing
- native soft mention rules

Reject:
- exact competitor wording
- exact competitor identity
- exact competitor assets
- any product mention that feels sponsored
- any app claim that is not supported by product/claim-bank.md

Flag uncertain decisions instead of hiding them.
```

## 3. Design Principle Extraction

```text
You are extracting visual principles for the men's fitness account.

The product is w(inner), a premium athlete mental performance app. Product imagery should feel like part of an athlete's preparation routine, not a generic app ad.

Read:
- accounts/mens-fitness/flow.md
- accounts/mens-fitness/writing.md
- product/app-brief.md

Analyze these design inputs:
[list Pinterest/reference image paths]

Return markdown for accounts/mens-fitness/extractions/design-analysis.md with:
- input set
- typography hierarchy
- spacing and safe zones
- image crop behavior
- overlays and annotations
- color, contrast, texture, and image treatment
- product asset fit, if relevant
- whether product assets should be app-in-hand, screenshot, implied routine, or excluded
- mapping from visual rules to flow.md slide roles
- what to keep, modify, reject, and ask the user about
```

## 4. Image Rule Distillation

```text
Using accounts/mens-fitness/extractions/design-analysis.md and accounts/mens-fitness/flow.md, update accounts/mens-fitness/image.md.

The final image rules must:
- depend on slide roles from flow.md
- explain typography behavior
- explain overlay behavior
- explain image crop and treatment
- state when product/app-in-hand assets are allowed
- preserve reference principles without copying exact compositions
```

## 5. Copy Drafting

```text
Draft a [slide count] slide concept for the men's fitness account.

The account should speak to athletes and athletic men who care about performance under pressure, not generic gym motivation.

Read:
- product/app-brief.md
- product/claim-bank.md
- accounts/mens-fitness/flow.md
- accounts/mens-fitness/writing.md
- accounts/mens-fitness/sources.md
- references/skills/stop-slop/SKILL.md
- references/skills/stop-slop/references/phrases.md
- references/skills/stop-slop/references/structures.md

Topic:
[topic]

Constraints:
- optimize for saves and shares
- no hard in-slideshow CTA
- app mention only if flow.md supports it
- flag unverified app claims
- do not frame w(inner) as therapy, meditation, or a guaranteed performance fix
- one idea per slide
- no Stop Slop banned structures

Return:
- slide-by-slide copy
- slide role for each slide
- source or claim notes
- soft app mention decision
- flagged product claims, if any
- Stop Slop QA score
```

## 6. Image Direction Drafting

```text
Create image direction for the drafted slideshow.

Read:
- accounts/mens-fitness/flow.md
- accounts/mens-fitness/writing.md
- accounts/mens-fitness/image.md
- accounts/mens-fitness/extractions/design-analysis.md

For each slide, return:
- slide role
- image concept
- subject and crop
- typography placement
- overlay behavior
- text-safe area
- product asset use or rejection
- product placement should feel like athlete preparation, not an app ad
- image generation prompt
- editing notes
```

## 7. Full QA

```text
QA this slideshow concept against the account playbook.

Read:
- product/app-brief.md
- product/claim-bank.md
- accounts/mens-fitness/flow.md
- accounts/mens-fitness/writing.md
- accounts/mens-fitness/image.md
- accounts/mens-fitness/sources.md
- references/skills/stop-slop/

Check:
- competitor structure preserved at format level only
- original wording and visual direction
- save/share value
- no hard CTA
- soft app mention feels native or is moved to comments/bio
- unverified app claims are flagged
- copy passes Stop Slop
- image direction follows slide roles

Return:
- pass/fail
- issues by severity
- exact edits needed
- final approval recommendation
```

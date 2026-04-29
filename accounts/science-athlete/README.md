# Science Athlete Account

Use this account for sport-agnostic slideshow posts that translate sport science,
neuroscience, motor learning, perception, pressure, and mental rehearsal into
practical training advice athletes can use immediately.

This account is **not** athlete biography content. It is for the athlete who says:

> I look good in drills, but I feel stiff, late, or robotic in games.

## Read Order For Any Post

1. `account-brief.md`
2. `presets.md`
3. `writing.md`
4. `design.md`
5. `image.md`
6. `sources.md`
7. `prompts.md`
8. The target post folder under `posts/`

## Primary Inspiration

Use `references/social-accounts/verified_byhumans/` as the core model for:

- clean 4:5 carousel design
- white background
- high whitespace
- simple educational slide rhythm
- bold, easy-to-digest list framing
- strong body-slide structure with a 16:9 middle image
- source-backed explanation without motivational fluff

Do **not** treat `verified_byhumans` as an anti-reference.

## Text Spacing Rules (Critical)

Study the reference slides before writing any copy. Do not guess the format.

**Hero slide:** Stack natural phrases, not single words.

- Good: `how to / stop / drills / from killing / your fluidity:`
- Bad: `the / drills / you / trust / are / ruining / your / fluidity`

**Body slides:** Use full paragraphs with bold section labels. Do not break sentences into dramatic word fragments.

- Good: `what to avoid:` followed by a full paragraph explanation, then `the fix:` followed by the practical correction.
- Bad: `you / watch / the / ball / through / every / cone` or breaking every sentence into its own line.

**Never** invent a new spacing style. Match the reference exactly.

## Copy Workflow Rule

When the user says "give me the copy" or asks to iterate on copy, **do not write it to a file first**. Paste the copy directly into chat for fast back-and-forth revision. Only write `flow.md` after the user approves the final version.

## Current Locked Direction

| Area | Rule |
| --- | --- |
| Core audience | Competitive athletes who want to improve skill transfer, fluidity, game confidence, and decision speed |
| Sport scope | Sport-agnostic; adapt language to soccer, basketball, boxing, tennis, etc. |
| Writing promise | Explain why common training feels good but fails under game pressure, then give a practical correction |
| Authority style | Sport language first, research-backed explanation second |
| Product bridge | w(inner) appears only when visualization or mental reps naturally extend the fix |
| Hero image | User supplies hero image |
| Body images | Fixed 16:9 middle-frame reference photos or visuals, framed according to `design.md` |

## Post Workspace Convention

Use:

```text
accounts/science-athlete/posts/{post-slug}/
```

Each post may contain:

- `flow.md` — final slide roles, copy, image concepts, and source notes
- `image_preset.json` — sourcing queries for 16:9 middle-frame images
- `sourced/` — raw source images
- `process_images.py` — post-specific renderer if needed
- `processed/` — final slide images

# Prompt Templates: Science Athlete

Use these prompts to generate posts that follow the account style.

## Full Post Prompt

```text
Create a 6-slide carousel for the Science Athlete account.

Sport: [sport]
Skill/desire: [what the athlete wants, e.g. more fluid on the ball, better handles, calmer sparring]
Felt problem: [what happens in games]
Preset: [Skill Transfer List / Read System / Drill Upgrade / Pressure State]
Product presence: [none / soft mental reps bridge / final close]

Rules:
- Write in the athlete's language first.
- Keep each rendered body slide/post image under 130 total words.
- Keep the top section under 70 words and the bottom **the fix:** section under 70 words.
- Treat those caps as hard ceilings but aim close to them when the idea needs explanation. Most body slides should land around 110-130 total words.
- Do not over-compress useful mechanism or drill detail just to be shorter.
- Do not write a separate **progression:** section. Fold any progression into **the fix:** if needed.
- Make the first sentence of each body slide instantly understandable.
- Use one science term per slide max.
- Explain unfamiliar science terms in brackets.
- Use stats only if they make the claim more convincing. Mark draft stats [VERIFY].
- Include source lines for research-backed claims.
- Give practical fixes that are easy to try.
- Explain why the fix works neurologically, cognitively, or perceptually.
- If a slide gives a drill, include a 16:9 image generation prompt using purposeful arrows.
- Do not force w(inner). Mention it only when visualization or mental reps naturally fit.

Return:
- Slide 1 hero copy.
- Slides 2-5 body copy as: top section, centered image prompt when needed, **the fix:** section, optional short source line.
- Slide 6 close.
- Source notes and [VERIFY] flags.
```

## Body Slide Prompt

```text
Write one Science Athlete body slide.

Sport: [sport]
Slide topic: [problem/read/drill/habit]
Athlete feeling: [what the athlete feels in games]
Practical fix: [simple drill/habit/rehearsal]
Science concept: [optional]
Source: [optional]

Rules:
- Start with the athlete's felt experience or a source-backed fact.
- Keep the rendered slide/post image under 130 total words.
- Keep the top section under 70 words and **the fix:** under 70 words.
- Aim close to the limits when useful: around 55-68 words per section and 110-130 words total.
- If the slide is under 100 words, add one concrete cue, mechanism, or fix detail unless the idea is already complete.
- Use only one visible bottom label: **the fix:**. Do not add **progression:**.
- Use one clear science term max and explain it in brackets.
- Keep the explanation smart but easy to follow.
- Make the outcome a natural conclusion of the explanation.
- Give a practical fix and explain why it works.
- If this is a drill, include a clear top-down 16:9 diagram prompt.
```

## Training Diagram Prompt Template

```text
Create a clean [sport] training diagram that an athlete can understand in 3 seconds. Use a top-down coach's whiteboard style on a plain white background, 16:9 aspect ratio.

Show [where the athlete starts]. Show [equipment/cues/defender/wall/gates]. Show [target or exit area].

Use purposeful arrows only: dashed arrows show [ball/object path], solid arrows show [athlete movement], curved arrows near the head show [scan/shoulder check/gaze shift], bold arrows show [final exit/attack/finish], and small circular arrows show [reset/repeat if needed]. Do not add decorative arrows.

Number the steps: 1 [start], 2 [read/scan/cue], 3 [movement], 4 [finish/exit/reset]. Add short athlete-friendly labels.

The diagram should clearly show where the athlete starts, what they look at, what cue triggers the movement, where the ball or object travels, and where the athlete moves next.
```

## Product Bridge Prompt

```text
Write a native w(inner) bridge for this slide.

Context: [physical fix or pressure scenario]
Sport: [sport]
Scenario: [position-specific situation]

Rules:
- Do not make w(inner) the whole solution.
- Present it as mental reps or visualization that extends the physical fix.
- Use approved wording only: w(inner) generates personalized visualization audio for your sport, position, and scenario.
- Avoid guarantees, therapy language, or performance promises.
- Keep it brief and practical.
```

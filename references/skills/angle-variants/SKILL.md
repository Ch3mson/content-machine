---
name: angle-variants
description: Brainstorm three differentiated slideshow angle concepts from a broad idea, overall angle, or variant request. Use when the user asks for 3 variants, 3 angles, angle concepts, brainstorming, or concept-only alternatives before final slide copy.
---

# Skill: Angle Variant Brainstorming

Use this when the user asks for variants or angle concepts based on an overall
idea, especially phrases like:

- `give me 3 variants`
- `give me three angles`
- `brainstorm variants`
- `angle concepts`
- `overall angle`
- `not slide copy, just the concept`

## Output Goal

Return exactly **3 differentiated angle concepts** in chat unless the user
explicitly asks for a file.

Do **not** write final slide copy, captions, `flow.md`, hooks, or rendered-post
text unless the user asks for them. This skill is for deciding why each post
variant is different and why a reader would keep reading.

## Read First

Use the smallest relevant set:

1. `AGENTS.md`
2. This file
3. Target account files, if an account is named or obvious:
   - `accounts/{account}/account-brief.md`
   - `accounts/{account}/writing.md`
   - `accounts/{account}/presets.md`, if present
   - `accounts/{account}/sources.md`, if claims, science, research, or product
     mentions may appear
4. `product/app-brief.md` and `product/claim-bank.md` only if the
   angle includes w(inner), product claims, or product-adjacent language.

If the account is missing and not obvious from context, ask the smallest
clarifying question. If the account is obvious from the current session, proceed.

## Core Principle

Start with the reader's **core desire**, not the mechanism.

Weak angle generation starts with: `scanning`, `hip angle`, `practice design`,
`visualization`, `pressure response`, or another technical explanation.

Strong angle generation starts with:

- what the reader wants to become
- what they secretly hate about how they currently perform
- what identity gap they feel but cannot explain
- what fear, shame, ambition, status desire, or frustration makes the topic feel
  urgent

The mechanism should explain the pain after the reader recognizes themselves.
It should not be the main reason to keep reading.

## Thought Process

For each set of three variants:

1. **Name the promised self.** What does this person want to feel like or be seen
   as? Examples: fluid, fearless, dangerous, composed, creative, trusted,
   unplayable, clutch, respected.
2. **Name the private gap.** What do they hate about the current version of
   themselves? Examples: robotic, safe, rushed, predictable, invisible,
   overthinking, hiding, wasting potential.
3. **Choose the emotional lever.** Use one primary lever per variant:
   - identity gap: `I am not playing like the version I believe I can be`
   - safety/hiding: `I am protecting myself from mistakes`
   - overthinking: `my mind is interrupting my body`
   - status frustration: `people see me as useful, not dangerous`
   - bad training resentment: `my training rewarded a fake version of the skill`
   - fear of wasted potential: `I have the tools, but cannot access them when it matters`
   - expression desire: `I want to play with freedom, not survival`
4. **Attach one mechanism.** Use the account's language to explain why the gap
   happens. Examples: pressure response, perception-action coupling, visual
   information, decision load, timing, rhythm, constraints, body orientation,
   practice transfer, mental rehearsal.
5. **Point toward a fix direction.** Keep it conceptual and practical. Do not turn
   it into final slide copy.

## Variant Differentiation Rules

The three variants should not be the same emotional idea with three different
technical mechanisms. Each variant needs a different reader entry point.

Good set:

- Variant 1 attacks the reader's identity gap.
- Variant 2 attacks the reader's overthinking loop.
- Variant 3 attacks the reader's fear/safety behavior.

Weak set:

- Variant 1 is about scanning.
- Variant 2 is about hip angle.
- Variant 3 is about cone drills.

The weak set may be scientifically useful, but it is not emotionally strong
enough unless each mechanism is tied to a core desire or private frustration.

## Response Format

Use this format unless the user asks for a different one:

```md
### Variant 1: [Sharp concept name]

**Core concept:** Explain the identity-level or desire-level premise in 2-4
sentences. Name what the reader wants, what is blocking them, and why this angle
would feel personal.

**Why this variant is different:** Explain the unique lens. Make clear how it is
not just another tip or mechanism.

**Viral/curiosity driver:** Explain why the reader would keep reading, save, or
share. Use curiosity, shock, self-recognition, contradiction, status threat, or
private shame. Avoid generic hype.

**Mechanism in play:** Name the simple mechanism that explains the pain. Use the
account's language and keep unfamiliar science terms bracketed.

**Fix direction:** Describe the kind of correction, drill, reframe, or mental rep
the post would naturally lead toward. Keep this conceptual, not final slide copy.
```

## Quality Bar

Before answering, check:

- Would the target reader feel called out in a useful way?
- Does each variant speak to desire, fear, identity, or wasted potential before
  explaining the mechanism?
- Can the reader think, `this is exactly me`, before they learn the science?
- Are the three variants meaningfully different from each other?
- Did you avoid final slide copy unless asked?
- Did you obey the account's `writing.md` tone and banned patterns?

## Examples

These examples are sport-specific, but the principles above are sport-agnostic.
Use the same structure for any account, sport, position, or audience.

### Example A: Soccer winger who wants to play more fluidly

#### Variant 1: The Fastest Robot on the Pitch

**Core concept:** The winger has speed, control, and clean technique, but every
attack feels pre-programmed. They are useful, but not scary. The desire is to be
unplayable, not just reliable.

**Why this variant is different:** It frames the problem as an identity trap:
the athlete became clean enough to avoid mistakes, but that cleanliness removed
the unpredictability that makes a winger dangerous.

**Viral/curiosity driver:** It challenges a painful belief: being a "good" player
can be what keeps you from becoming a feared player. The self-recognition is the
winger who trains hard but secretly feels forgettable.

**Mechanism in play:** Over-rehearsed patterns can narrow decision options. The
body repeats the safest solution instead of reading the defender in real time.

**Fix direction:** Practice reps with random exits or defender cues so the player
has to read before acting instead of performing a memorized route.

#### Variant 2: The Mind That Won't Shut Up

**Core concept:** The winger wants to play on instinct, but every touch triggers
a mental checklist. By the time they choose, the defender has already solved
them. The desire is to feel the game slow down while the body moves freely.

**Why this variant is different:** It does not blame technique. It blames the gap
between conscious analysis and automatic execution.

**Viral/curiosity driver:** It names an invisible frustration: technically smart
players often look slower because they are still thinking through actions that
should be read and triggered.

**Mechanism in play:** Decision load slows the perception-action loop [the link
between what you see and how your body responds].

**Fix direction:** Use simple cue-based reps where one visual signal decides the
exit, so the read becomes faster and less verbal.

#### Variant 3: The Winger Who Plays Not to Lose

**Core concept:** The winger says they are linking play, but deep down they know
they are avoiding risk. They pass backward early, avoid the 1v1, and choose safe
touches before pressure truly arrives. The desire is to attack defenders instead
of surviving possession.

**Why this variant is different:** It makes fluidity emotional, not just
technical. The issue is not that the player lacks moves; it is that one mistake
feels like proof they do not belong.

**Viral/curiosity driver:** It touches private shame without turning into empty
motivation. Many players recognize the hidden bargain: stay safe, keep your
spot, and slowly become less dangerous.

**Mechanism in play:** Pressure can shrink perceived options. The body chooses
the lowest-risk action before the player consciously realizes they are hiding.

**Fix direction:** Create low-cost risk reps: one required attacking action per
receive, then review the read instead of judging only success or failure.

### Example B: Basketball guard whose handle disappears in games

#### Variant 1: The Mixtape Handle That Vanishes Under Contact

**Core concept:** The guard wants to look loose and creative, but the handle only
feels alive when nobody can touch them. In games, the same moves become tight and
protective.

**Why this variant is different:** It separates performing moves from owning the
ball under consequence.

**Viral/curiosity driver:** It exposes a common status gap: you can look skilled
online or in workouts while still not being trusted late in games.

**Mechanism in play:** Pressure and contact change rhythm, posture, and visual
attention.

**Fix direction:** Add controlled bumps, random reaches, or late visual cues so
the handle adapts instead of just repeating a clean pattern.

#### Variant 2: The Guard Who Dribbles to Feel Safe

**Core concept:** The guard keeps the ball alive because stopping would force a
decision. The desire is to control the game, but the behavior becomes hiding
inside extra dribbles.

**Why this variant is different:** It makes over-dribbling a confidence and read
problem, not just a bad habit.

**Viral/curiosity driver:** The reader keeps going because the post says the
quiet part: sometimes the extra combo is not creativity, it is delay.

**Mechanism in play:** Unclear reads increase decision load, so the body buys
time with familiar movement.

**Fix direction:** Use constraint reps with a two-dribble decision limit and one
predefined read cue.

#### Variant 3: The Player Whose Body Knows Moves but Not Moments

**Core concept:** The guard has the move package, but not the timing. They can do
the crossover, but not feel when the defender's weight gives permission.

**Why this variant is different:** It shifts the post from skill collection to
moment recognition.

**Viral/curiosity driver:** It creates curiosity by saying the missing skill is
not another move; it is seeing the exact moment a move becomes available.

**Mechanism in play:** Affordances [the actions your body sees as possible]
change when the defender's balance, hips, and feet change.

**Fix direction:** Train moves from defender cues instead of from a memorized
combo order.

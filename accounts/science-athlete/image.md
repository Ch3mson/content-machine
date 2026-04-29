# Image Rules: Science Athlete Account

Use this file for photo direction, visual treatment, and selected-photo
suitability. Use `design.md` for canvas size, layout, typography, text
placement, reference-photo frame dimensions, and renderer-facing format rules.

Do not use this file as the source of truth for text layout.

## Visual Model

Use `references/social-accounts/verified_byhumans/` as the primary visual model
for clean, high-whitespace educational carousel visuals. The extracted layout
system from that reference lives in `design.md`.

## Reference Photo Framing

- Body-slide reference photos or visuals must be placed inside the fixed frame
  specified in `design.md`.
- Crop selected images to fit the frame without stretching or distorting.
- Keep the key sport cue, diagram, body position, or product context readable
  inside the frame.
- Do not move or resize the frame to compensate for long copy.

## Body Image Principle

Every body slide needs a clear reference visual, but the visual type depends on
the slide.

| Slide content type | Image direction |
| --- | --- |
| Training drill fix | Top-down coach whiteboard diagram |
| Game scenario | Simple field/court/ring diagram or in-game crop showing pressure/cue |
| Neurological explanation | Minimal brain, visual-system, attention, or threat-response diagram |
| At-home habit | Lifestyle visual: headphones, journal, phone timer, recovery setup |
| Product / visualization | Athlete mentally rehearsing, headphones, phone, or subtle app-context visual |
| Source slide | Research paper, abstract visual, citation card, or clean note graphic |

Do not use a drill diagram when the slide is about a habit, brain mechanism,
source, or product unless the slide gives a spatial setup.

## Training Drill Diagram Rules

Training drill diagrams must look like a coach explaining the drill on a
whiteboard.

They must answer in 3 seconds:

1. Where does the athlete start?
2. What do they look at?
3. What cue triggers the action?
4. Where does the ball/object go?
5. Where does the athlete move?
6. What is the final action?

## Arrow Rules

Arrows must be purposeful. Do not add decorative arrows.

Use this convention in every training image prompt:

- Dashed arrow: ball path, puck path, glove cue, pass, rebound, or object movement.
- Solid arrow: athlete movement path.
- Curved arrow near head: scan, shoulder check, head turn, or gaze shift.
- Bold arrow: explosive exit, final attack, burst, finish, or decisive action.
- Small circular arrow: reset and repeat.
- Dotted sight line: where the athlete should look.

If a prompt uses an arrow, it must say what the arrow means.

## Training Prompt Template

Use this structure whenever a slide gives a drill or spatial setup:

```text
Create a clean [sport] training diagram that an athlete can understand in 3 seconds. Use a top-down coach's whiteboard style on a plain white background, 16:9 aspect ratio.

Show [starting position]. Show [equipment/cues/defender/wall/gates]. Show [target or exit area].

Use purposeful arrows only: dashed arrows show [ball/object path], solid arrows show [athlete movement], curved arrows near the head show [scan/shoulder check], bold arrows show [final action], and small circular arrows show [reset/repeat if needed]. Do not add decorative arrows.

Number the steps: 1 [start], 2 [read/scan/cue], 3 [movement], 4 [finish/exit/reset]. Add short athlete-friendly labels: [labels].

The diagram should clearly show where the athlete starts, what they look at, what cue triggers the movement, and where they move next.
```

## Example: Soccer Wall + Exit Gate

```text
Create a clean soccer training diagram that an athlete can understand in 3 seconds. Use a top-down coach's whiteboard style on a plain white background, 16:9 aspect ratio.

Show a straight vertical boundary line on the left representing a wall. Place a player icon in the center with a small arrowhead showing open hips. To the right, place two cone gates, one slightly higher and one slightly lower.

Use purposeful arrows only: dashed arrows show the ball being passed into the wall and rebounding back, a curved arrow near the player's head shows the shoulder check toward the gates, a solid arrow shows the player receiving across the body, and a bold arrow shows the exit through one gate. Do not add decorative arrows.

Number the steps: 1 pass, 2 scan, 3 receive across body, 4 exit through gate. The diagram should clearly show where the player starts, what they look at, how the ball rebounds, and where they move next.
```

## Non-Drill Image Rules

For neurological explanation slides:

- Use simple labels.
- Show one mechanism only.
- Explain unfamiliar brain regions visually.
- Avoid medical-looking complexity.

For habit slides:

- Show the athlete doing the habit, not a generic stock pose.
- Keep the visual specific to the sport when possible.

For product/visualization slides:

- Do not make the product look like an ad.
- Prefer athlete-in-context: headphones, quiet gym, locker room, field/court
  edge, or post-training recovery.
- If app UI is used, it must match approved product visuals.

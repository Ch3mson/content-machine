# Image Rules: Athlete Max

Use this file for photo direction, visual treatment, selected-photo suitability,
and image prompt direction. Use `design.md` for canvas size, typography, text
placement, reference-photo frame dimensions, and renderer-facing layout rules.

Do not use this file as the source of truth for layout, margins, font sizes, or
frame placement.

## Visual Model

- Primary image model: `references/social-accounts/verified_byhumans/` for clean,
  clinical, high-whitespace authority.
- Secondary contrast model: `references/social-accounts/chasingpeaks0/` shows dark,
  cinematic, dense full-bleed imagery. Use only as contrast; athlete-max should
  not default to dark meme-style overlays.

## Photo Subject Direction

### Hero Images

- Competitive athletes, head-to-mid-torso or waist-up crop.
- Focused gaze, pre-performance tension, recovery setup, or sport-specific gear.
- Strong anatomy or equipment cues: hands wrapped, running spikes, court/field
  context, weights, recovery tools, sweat, chalk, tape, heart-rate strap.
- Clean negative space on the left or right for large type.
- The photo should feel like evidence of performance, not a motivational poster.

### Body Images

- Use a visual that clarifies the mechanism or protocol on the slide.
- Strong options: sport action crop, anatomical/physiology diagram, equipment
  close-up, recovery setup, training environment, research-style visual.
- Body images must be understandable in 3 seconds when placed inside the fixed
  frame defined in `design.md`.
- If the slide explains a mechanism, prefer a simple diagram or clear anatomical
  visual over a generic athlete photo.

## Visual Treatment

- Hero images: convert to black-and-white, increase contrast, avoid vintage grain
  or heavy filters.
- Body images: prefer neutral, desaturated, or B&W treatment. Use color only when
  it helps explain the cue, diagram, or mechanism.
- Backgrounds: clean, uncluttered, high-key, or easily cropped.
- Lighting: directional, sharp, clinical, high contrast.
- Avoid: saturated Instagram filters, gym selfie lighting, collage effects,
  decorative overlays, and fake cinematic grain.

## Selected-Photo Suitability

Use an image when it meets most of these:

- The athlete, body part, equipment, or mechanism is immediately legible.
- The crop has negative space or can fit the design frame without losing the key
  cue.
- The image feels scientific, clinical, or performance-specific.
- The visual supports the exact slide claim instead of merely decorating it.
- The image does not introduce a sport-specific promise that the copy does not
  support.

Reject an image when:

- It looks like generic stock fitness.
- It has busy backgrounds that fight the typography.
- It is a flexing selfie, motivational montage, or influencer-style gym shot.
- It requires text to sit on top of the image to make sense.
- It is medically inaccurate or too complex for a carousel slide.

## Body Image Types

| Slide content type | Image direction |
| --- | --- |
| Biological mechanism | Simple anatomy, brain, muscle, tendon, mitochondria, nervous-system, or sleep-cycle visual |
| Training protocol | Athlete executing the movement, coach-style diagram, stopwatch/timer, equipment setup |
| Recovery habit | Sleep environment, hydration/electrolytes, mobility work, cool room, phone/light exposure cue |
| Nutrition / supplementation | Ingredient, meal timing setup, bottle/capsule only if claim-safe and not ad-like |
| Injury prevention | Joint/tendon/muscle close-up, clean rehab exercise, anatomical overlay if accurate |
| Research/source slide | Paper abstract, journal screenshot-style crop, citation card, or minimal data visual |
| Product / w(inner) mention | Athlete-in-context with phone/headphones/journal; app presence must be subtle and not ad-like |

## Image Prompt Direction

Use this structure when generating or sourcing a visual:

```text
Find or create a clean, clinical sports-science image for a carousel slide about
[specific mechanism/protocol]. The image should show [athlete/body part/equipment]
in a way that is understandable in 3 seconds. Use high contrast, minimal clutter,
and a white or neutral background. The image will be cropped into a centered
16:9 frame, so keep the key cue in the middle. Avoid motivational poster style,
gym selfies, saturated filters, and decorative text.
```

For hero images:

```text
Find or create a high-contrast black-and-white portrait of a competitive athlete
showing [sport/context]. Use a head-to-torso crop, focused expression, visible
sport-specific detail, and clean negative space for large left-aligned text.
Avoid influencer gym poses, fantasy edits, motivational lighting, and cluttered
backgrounds.
```

## Reference Photo Framing Reminder

- Body images must be placed inside the fixed frame specified in `design.md`.
- Do not move or resize the frame to compensate for long copy.
- Crop selected images to fit without stretching.
- Keep the key sport cue, diagram, body position, or product context readable.

## Product / w(inner) Image Rules

- Product visuals must feel native and almost invisible.
- Avoid app-logo hero shots, CTA buttons, pricing, product mockup walls, or
  promotional device framing.
- Prefer athlete-in-context: locker room, quiet gym, sideline, recovery setup,
  headphones, phone, notebook, or post-training routine.
- If app UI is shown, it must match approved product visuals and be secondary to
  the athlete/science story.

# Avatar Image-Gen Account

This folder stores single-image photo posts using our consistent 20-year-old student avatar (dirty blonde hair in a messy bun, relatable college dorm mirror selfie aesthetic) inspired by the high-performing `@bellajobtips` TikTok format.

## Avatar Profile

- **Identity**: 20-year-old Caucasian college student girl
- **Key Features**: Dirty blonde hair in a casual messy high bun with loose face-framing strands, natural soft facial structure, light eyes.
- **Base Reference Still**: `tools/fal-image-gen/out/batch_crying_girls/white_01.jpg`
- **Model Endpoint**: Fal Seedream 5.0 Pro Edit (`bytedance/seedream/v5/pro/edit`)
- **Visual Aesthetic**: Handheld iPhone mirror selfie in college dorm room, lying on stomach on dorm bed facing mirror reflection, phone visible, looking slightly down and off-axis.
- **Tone / Mood**: Less intensely red-eyed; quiet emotional exhaustion, pensive vulnerability, and relatable student fatigue.

## Reference Benchmarks

- **Natural Tear Level & Emotional Benchmark**: `accounts/image-gen/references/test-asian-girl-mirror-crying-v2.jpg` (Guide: `references/tear-level-reference.md`).
  - Single delicate tear track, glassy watery eyes, subtle natural flush, no swollen eyelids or bloodshot redness.

## Posts

| Post | Folder | Image | Outfit | Expression / Angle |
| --- | --- | --- | --- | --- |
| 1 | `accounts/image-gen/1/` | `image.jpg` | Classic heather grey hoodie | Propped on elbows holding phone, gazing slightly down/away |
| 2 | `accounts/image-gen/2/` | `image.jpg` | Cream ribbed crewneck | Propping chin in palm, pensive off-axis glance |
| 3 | `accounts/image-gen/3/` | `image.jpg` | Washed navy crewneck | Propped on elbows looking down at phone screen |

Each subfolder contains:
- `caption.md`: Recommended on-image text overlays (Job Market and College/AntiGPT variants), social captions, and generation prompts.
- `image.jpg`, `image.png`, and `image`: High-res 1080x1920 stills ready for caption overlay or posting.

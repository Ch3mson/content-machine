#!/usr/bin/env python3
"""Generate 3 avatar variations (less sad, consistent face/identity from white_01.jpg)
and save them into accounts/image-gen/[1, 2, 3]/ with caption.md and images.
"""

from __future__ import annotations

import concurrent.futures
import json
import os
import shutil
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from PIL import Image

PROJECT_ROOT = Path(__file__).resolve().parents[2]
EDIT_MODEL = "bytedance/seedream/v5/pro/edit"
ACCOUNTS_DIR = PROJECT_ROOT / "accounts" / "image-gen"
REF_IMAGE = PROJECT_ROOT / "tools" / "fal-image-gen" / "out" / "batch_crying_girls" / "white_01.jpg"


def load_dotenv_value(name: str) -> str | None:
    env_path = PROJECT_ROOT / ".env"
    if not env_path.exists():
        return None
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        if key.strip() == name:
            return value.strip().strip('"').strip("'")
    return None


def get_api_key() -> str:
    api_key = os.environ.get("FAL_KEY") or load_dotenv_value("FAL_KEY")
    if not api_key:
        raise SystemExit("Missing FAL_KEY. Set it in the repo .env file.")
    return api_key


def file_to_data_uri(path: Path) -> str:
    import base64
    import mimetypes
    mime = mimetypes.guess_type(path.name)[0] or "image/jpeg"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


POST_SPECS = [
    {
        "num": "1",
        "title": "Post 1 - Quiet Exhaustion (Classic Grey Hoodie)",
        "prompt": (
            "A vertical 9:16 authentic handheld iPhone mirror selfie in a college dorm room. "
            "The subject is the exact same 20-year-old Caucasian college student girl from Figure 1 "
            "(exact same facial features, soft jawline, light eyes, dirty blonde hair in a messy high bun with loose face-framing strands). "
            "She is lying on her stomach on an unmade dorm bed, propped up on her elbows facing directly into a bedroom mirror. "
            "She holds a black iPhone pointed into the mirror to take the photo, phone back and camera lenses clearly visible in the reflection. "
            "Her face faces the camera/mirror, but her eyes look slightly down and away from the camera lens with a somber, overwhelmed expression. "
            "Quiet emotional exhaustion, gentle vulnerability, but less sad and calm: natural clear eyes, absolutely NO heavy red swelling, "
            "NO bloodshot veins, and NO puffy eyelids. "
            "Wearing an oversized light heather grey hooded sweatshirt with drawstring. "
            "Dorm room background with an unmade beige linen duvet, white cinderblock wall with small art postcards, warm bedside reading lamp. "
            "Casual amateur smartphone snapshot aesthetic, relatable TikTok UGC style. Pure photograph, completely clean: no text, no captions, no words, no watermarks."
        ),
        "hook_job": "Day was going well until I got the email saying I didn't get the Wendy's job... with a 3.9 GPA and a masters degree... This market is unreal 😭",
        "hook_study": "Studied 14 hours a day for two weeks straight just to get a 62% on the midterm... I don't even know what I'm doing wrong anymore 😭",
        "caption": "how is this even real?? #college #collegelife #jobmarket #student #finalsweek #relatable",
    },
    {
        "num": "2",
        "title": "Post 2 - Pensive Heartbreak (Chin in Palm / Oatmeal Crewneck)",
        "prompt": (
            "A vertical 9:16 authentic handheld iPhone mirror selfie in a college dorm room. "
            "The subject is the exact same 20-year-old Caucasian college student girl from Figure 1 "
            "(exact same facial features, soft jawline, light eyes, dirty blonde hair in a messy high bun with loose wispy strands). "
            "She is lying on her stomach on her dorm bed, propping her chin or cheek gently in the palm of one hand, facing toward the bedroom mirror. "
            "With her other hand she holds a dark smartphone in front taking the mirror selfie, phone camera lenses reflected. "
            "Her face is turned toward the mirror, but her eyes gaze pensively off to the side, lost in quiet contemplation and sadness. "
            "Gently sad, vulnerable, and defeated, but less sad than crying: clean natural clear eyes, NO heavy redness, NO swollen eyelids, NO bloodshot eyes. "
            "Wearing an oversized cozy oatmeal-cream fleece crewneck sweatshirt. "
            "Warm lived-in dorm room with unmade beige linen duvet, wooden nightstand, desk with books softly visible, warm amber bedside lamp glow. "
            "Authentic handheld TikTok snapshot aesthetic. Pure photograph, completely clean: no text, no captions, no words, no watermarks."
        ),
        "hook_job": "Nearly 18 months out of college, 1600+ job apps and still nothing... am I actually unemployable or is this whole system broken 😭",
        "hook_study": "Spent all weekend writing a 12-page research paper just for the AI detector to flag my own writing at 84%... I literally wrote every word 😭",
        "caption": "tell me I'm not the only one going through this rn 😭 #studentproblems #turnitin #collegelife #relatable #studygram",
    },
    {
        "num": "3",
        "title": "Post 3 - Deflated Defeat (Navy Slouchy Sweatshirt)",
        "prompt": (
            "A vertical 9:16 authentic handheld iPhone mirror selfie in a university dorm bedroom. "
            "The subject is the exact same 20-year-old Caucasian college student girl from Figure 1 "
            "(exact same facial features, soft jawline, light eyes, dirty blonde hair in a messy high bun with loose strands). "
            "She is lying on her stomach on her dorm bed, propped up on both forearms facing the mirror reflection. "
            "She holds a black smartphone pointed at the mirror taking the selfie, phone visible in reflection. "
            "Her face is positioned toward the camera/mirror, but she looks downward toward her hands with a deflated, tired, heartbroken expression, biting her lower lip gently. "
            "Quiet relatable sadness, feeling defeated after a rejection, but natural and calm: clear eyes, NO swollen red puffy eyes, NO bloodshot marks. "
            "Wearing an oversized washed vintage navy blue university crewneck sweatshirt. "
            "Dorm room background with beige rumpled sheets, cinderblock wall, soft warm ambient lighting from a table lamp. "
            "Raw candid smartphone camera snapshot aesthetic, relatable TikTok UGC style. Pure photograph, completely clean: no text, no captions, no words, no watermarks."
        ),
        "hook_job": "I get that the job market is awful right now, people with degrees can't even land entry level roles... so who tf is actually getting hired? Bc I haven't seen a single person 😭",
        "hook_study": "When your professor assigns a 3000-word paper due tomorrow and says 'it shouldn't take more than 2 hours if you've been paying attention' 😭",
        "caption": "genuinely at my breaking point today 😭 #collegelife #university #study #relatable #studentlife",
    },
]


def generate_post(spec: dict, api_key: str, ref_data_uri: str) -> None:
    num = spec["num"]
    post_dir = ACCOUNTS_DIR / num
    post_dir.mkdir(parents=True, exist_ok=True)

    img_jpg_path = post_dir / "image.jpg"
    img_png_path = post_dir / "image.png"
    caption_path = post_dir / "caption.md"

    # 1. Generate image if not already present
    if not img_jpg_path.exists() or img_jpg_path.stat().st_size < 10000:
        print(f"[{num}] Generating image for: {spec['title']}...")
        payload = {
            "prompt": spec["prompt"],
            "image_size": {"width": 1080, "height": 1920},
            "num_images": 1,
            "output_format": "jpeg",
            "enable_safety_checker": True,
            "image_urls": [ref_data_uri],
        }

        request = urllib.request.Request(
            f"https://fal.run/{EDIT_MODEL}",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Key {api_key}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            method="POST",
        )

        t0 = time.time()
        try:
            with urllib.request.urlopen(request, timeout=240) as response:
                body = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"[{num}] Fal request failed ({exc.code}): {detail}") from exc

        images = body.get("images") or []
        if not images or not images[0].get("url"):
            raise RuntimeError(f"[{num}] No image URL in Fal response: {body}")

        image_url = images[0]["url"]
        with urllib.request.urlopen(image_url, timeout=120) as image_response:
            img_jpg_path.write_bytes(image_response.read())

        print(f"[{num}] Generated image in {time.time() - t0:.1f}s -> {img_jpg_path}")

    # 2. Also save PNG and extensionless 'image' file / symlink so all path variations resolve cleanly
    if not img_png_path.exists():
        with Image.open(img_jpg_path) as im:
            im.save(img_png_path, "PNG")
        print(f"[{num}] Saved PNG -> {img_png_path}")

    # Extensionless 'image' file (copy of image.jpg)
    raw_img_file = post_dir / "image"
    if not raw_img_file.exists():
        shutil.copy2(img_jpg_path, raw_img_file)

    # 3. Write caption.md
    caption_content = f"""# Post {num}: {spec['title']}

- **Avatar**: 20yo Caucasian student girl (dirty blonde messy high bun, natural soft features)
- **Format**: Single-image TikTok / Instagram Reels photo post (Bella Job Tips formula)
- **Image**: `image.jpg` (also available as `image.png` and `image`)
- **Visual Vibe**: Authentic handheld iPhone mirror selfie on dorm bed, looking slightly off-axis, less sad / natural clear eyes (no heavy redness or swollen lids).

---

## On-Image Text Overlay (Hook Options)

### Option A: Job Market / Career Despair (Bella Formula)
```text
{spec['hook_job']}
```

### Option B: College / Academic Pain (AntiGPT / Student Formula)
```text
{spec['hook_study']}
```

---

## Social Post Caption & Hashtags

```text
{spec['caption']}
```

---

## Visual & Generation Details

- **Model**: Fal Seedream 5.0 Pro Edit (`bytedance/seedream/v5/pro/edit`)
- **Reference Image**: `tools/fal-image-gen/out/batch_crying_girls/white_01.jpg`
- **Resolution**: 1080 x 1920 (9:16 vertical)
- **Prompt**:
> {spec['prompt']}
"""
    caption_path.write_text(caption_content, encoding="utf-8")
    print(f"[{num}] Wrote caption.md -> {caption_path}")


def main():
    if not REF_IMAGE.exists():
        raise SystemExit(f"Reference image not found: {REF_IMAGE}")

    ACCOUNTS_DIR.mkdir(parents=True, exist_ok=True)
    api_key = get_api_key()

    print("Encoding avatar reference image...")
    ref_data_uri = file_to_data_uri(REF_IMAGE)

    print("Starting generation of 3 avatar variations in parallel...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(generate_post, spec, api_key, ref_data_uri)
            for spec in POST_SPECS
        ]
        for f in concurrent.futures.as_completed(futures):
            f.result()

    print("\nAll 3 posts successfully generated!")


if __name__ == "__main__":
    main()

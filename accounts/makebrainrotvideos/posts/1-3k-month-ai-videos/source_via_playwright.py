"""
Source portrait-friendly images from Pexels for slideshow backgrounds.
Dark aesthetic: computer setups, cash flex, dark lifestyle shots.
"""

import urllib.request
from pathlib import Path

from PIL import Image

OUT_DIR = Path(__file__).parent / "sourced"
OUT_DIR.mkdir(exist_ok=True)

SLIDE_SOURCES = {
    1: {
        "role": "hook_money",
        "urls": [
            "https://images.pexels.com/photos/4386431/pexels-photo-4386431.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750",
            "https://images.pexels.com/photos/6289065/pexels-photo-6289065.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750",
        ],
    },
    2: {
        "role": "trending_niche",
        "urls": [
            "https://images.pexels.com/photos/1714208/pexels-photo-1714208.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750",
            "https://images.pexels.com/photos/1181675/pexels-photo-1181675.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750",
        ],
    },
    3: {
        "role": "mass_generate",
        "urls": [
            "https://images.pexels.com/photos/546819/pexels-photo-546819.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750",
            "https://images.pexels.com/photos/1779487/pexels-photo-1779487.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750",
        ],
    },
    4: {
        "role": "post_daily",
        "urls": [
            "https://images.pexels.com/photos/4549408/pexels-photo-4549408.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750",
            "https://images.pexels.com/photos/5926382/pexels-photo-5926382.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750",
        ],
    },
    5: {
        "role": "monetize",
        "urls": [
            "https://images.pexels.com/photos/4386476/pexels-photo-4386476.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750",
            "https://images.pexels.com/photos/3943716/pexels-photo-3943716.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750",
        ],
    },
}

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"


def download(url: str, dest: Path) -> bool:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=20) as r:
            data = r.read()
            if len(data) < 5000:
                return False
            with open(dest, "wb") as f:
                f.write(data)
        return True
    except Exception as e:
        print(f"  Failed: {e}")
        return False


def main():
    for slide_num, info in SLIDE_SOURCES.items():
        role = info["role"]
        print(f"\nSlide {slide_num}: {role}")

        success = False
        for url in info["urls"]:
            print(f"  Trying: {url[:80]}...")
            dest = OUT_DIR / f"slide_{slide_num:02d}_{role}.jpg"
            if download(url, dest):
                try:
                    with Image.open(dest) as img:
                        w, h = img.size
                        print(f"  Downloaded: {w}x{h}")
                        img.convert("RGB").save(dest, "JPEG", quality=92)
                        success = True
                        break
                except Exception as e:
                    print(f"  Invalid image: {e}")
                    dest.unlink(missing_ok=True)

        if not success:
            print(f"  => NO IMAGE for slide {slide_num}")

    print(f"\nDone. Check: {OUT_DIR.resolve()}")


if __name__ == "__main__":
    main()

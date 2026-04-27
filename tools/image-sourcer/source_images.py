#!/usr/bin/env python3
"""
Image Sourcing Tool for Slideshow Accounts

Uses browser-harness to search Pinterest (or DuckDuckGo) for images per slide,
downloads candidates, filters for 9:16 aspect ratio, and saves the best match.

Usage:
    python tools/image-sourcer/source_images.py accounts/athlete-stories/Lebron/image_preset.json

Requirements:
    - Chrome/Edge running with remote debugging enabled
    - browser-harness daemon (auto-started)
    - Pillow for image dimension checks
"""
import hashlib
import json
import math
import os
import shutil
import sys
import tempfile
import time
import urllib.request
import urllib.parse
from pathlib import Path

# Add browser-harness to import path
_bh = Path(__file__).parent.parent / "browser-harness"
sys.path.insert(0, str(_bh))

from admin import ensure_daemon  # noqa: E402
from helpers import new_tab, wait_for_load, wait, js, goto_url  # noqa: E402


def _ua():
    return "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"


def search_pinterest(query, max_images=30):
    """Search Pinterest and return a list of image URLs.
    Tries to upgrade thumbnails to higher-res versions."""
    url = f"https://www.pinterest.com/search/pins/?q={urllib.parse.quote(query)}"
    print(f"    Navigating: {url[:90]}...")
    new_tab(url)
    wait_for_load()
    wait(3)

    # Scroll to trigger lazy-load
    for i in range(5):
        js("window.scrollBy(0, 1000)")
        wait(1.5)

    # Extract pinimg URLs — include srcset for higher-res variants
    urls = js("""
        (function(){
            const out = [];
            document.querySelectorAll('img').forEach(i => {
                if (i.srcset) {
                    const candidates = i.srcset.split(',').map(s => s.trim().split(' ')[0]);
                    out.push(...candidates);
                }
                if (i.src) out.push(i.src);
                if (i.getAttribute('data-src')) out.push(i.getAttribute('data-src'));
            });
            return [...new Set(out.filter(u => u && u.includes('pinimg.com')))];
        })()
    """)

    # Upgrade URLs to higher res and deduplicate
    seen = set()
    out = []
    for u in (urls or []):
        if not u or not u.startswith("http"):
            continue
        # Upgrade size hints to larger versions
        hi = u.replace("/236x/", "/736x/").replace("/474x/", "/736x/")
        hi = hi.replace("/170x/", "/736x/").replace("/600x/", "/736x/")
        # Try originals path as well
        orig = hi.replace("/736x/", "/originals/")
        for candidate in (orig, hi, u):
            base = candidate.split("?")[0]
            if base in seen:
                continue
            seen.add(base)
            out.append(candidate)
            if len(out) >= max_images:
                break
        if len(out) >= max_images:
            break
    return out


def search_duckduckgo(query, max_images=30):
    """Search DuckDuckGo Images and return a list of image URLs."""
    url = f"https://duckduckgo.com/?q={urllib.parse.quote(query)}&iax=images&ia=images"
    print(f"    Navigating: {url[:90]}...")
    new_tab(url)
    wait_for_load()
    wait(2.5)

    for i in range(3):
        js("window.scrollBy(0, 900)")
        wait(1.0)

    urls = js("""
        [...new Set(
            [...document.querySelectorAll('img')]
            .map(i => i.src || i.getAttribute('data-src'))
            .filter(u => u && u.startsWith('http'))
        )]
    """)

    seen = set()
    out = []
    for u in (urls or []):
        if not u or not u.startswith("http"):
            continue
        base = u.split("?")[0]
        if base in seen:
            continue
        seen.add(base)
        out.append(u)
        if len(out) >= max_images:
            break
    return out


def download_image(url, dest, timeout=15):
    """Download an image to dest. Returns True on success."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": _ua()})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read()
            if len(data) < 1024:
                return False  # Too small — probably a tracking pixel
            with open(dest, "wb") as f:
                f.write(data)
        return True
    except Exception as e:
        print(f"      download failed: {e}")
        return False


def get_image_info(path):
    """Return (aspect_ratio, width, height) or (None, 0, 0)."""
    try:
        # Try to use Pillow if available
        from PIL import Image as PILImage
        with PILImage.open(path) as img:
            w, h = img.size
            return w / h, w, h
    except Exception:
        pass

    # Fallback: try parsing file headers for JPG/PNG
    try:
        with open(path, "rb") as f:
            header = f.read(24)
        # PNG
        if header[:8] == b"\\x89PNG\\r\\n\\x1a\\n":
            w = int.from_bytes(header[16:20], "big")
            h = int.from_bytes(header[20:24], "big")
            return w / h, w, h
        # JPEG SOF0/SOF2 markers
        if header[:2] == b"\\xff\\xd8":
            with open(path, "rb") as f:
                data = f.read()
            for i in range(2, len(data) - 10):
                if data[i] == 0xFF and data[i + 1] in (0xC0, 0xC2):
                    h = int.from_bytes(data[i + 5:i + 7], "big")
                    w = int.from_bytes(data[i + 7:i + 9], "big")
                    return w / h, w, h
    except Exception:
        pass
    return None, 0, 0


def run_preset(preset_path):
    preset_path = Path(preset_path)
    with open(preset_path, "r", encoding="utf-8") as f:
        preset = json.load(f)

    account = preset.get("account", "unknown")
    subject = preset.get("subject", "unknown")
    source = preset.get("source", "duckduckgo")
    output_dir = Path(preset["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)

    filters = preset.get("filters", {})
    target_ratio = filters.get("target_ratio", 1080 / 1920)
    tolerance = filters.get("ratio_tolerance", 0.2)
    min_width = filters.get("min_width", 400)
    min_height = filters.get("min_height", 700)
    max_candidates = filters.get("max_candidates_per_slide", 15)
    download_timeout = filters.get("download_timeout", 15)

    print(f"Image Sourcing: {account}/{subject}")
    print(f"Source: {source}")
    print(f"Output: {output_dir.resolve()}")
    print(f"Target ratio: {target_ratio:.4f} (tolerance ±{tolerance})")
    print("-" * 50)

    # Ensure browser-harness daemon is up
    print("Ensuring browser-harness daemon...")
    if not os.environ.get("BU_CDP_WS"):
        # Try auto-detecting local Chrome on port 9222
        import socket, urllib.request
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect(("127.0.0.1", 9222))
            s.close()
            req = urllib.request.Request("http://127.0.0.1:9222/json/version")
            data = json.loads(urllib.request.urlopen(req, timeout=5).read())
            os.environ["BU_CDP_WS"] = data.get("webSocketDebuggerUrl", "")
            print("Auto-detected Chrome on port 9222.")
        except Exception:
            print("\nERROR: No Chrome remote debugging detected.")
            print("Run this first to connect your Chrome:")
            print("  python tools/browser-harness/connect_my_chrome.py")
            sys.exit(1)
    ensure_daemon()
    print("Daemon ready.\n")

    search_fn = search_pinterest if source == "pinterest" else search_duckduckgo

    # Temp dir for downloads
    tmp_dir = Path(tempfile.gettempdir()) / f"img_sourcer_{subject}_{int(time.time())}"
    tmp_dir.mkdir(exist_ok=True)

    try:
        for slide_def in preset["slides"]:
            slide_num = slide_def["slide"]
            role = slide_def["role"]
            queries = slide_def["queries"]
            slide_source = slide_def.get("source", source)

            print(f"\nSlide {slide_num}: {role}")

            if slide_source == "ask_user":
                print("  => USER IMAGE REQUIRED — please place your product photo in the output folder.")
                print(f"     Expected: slide_{slide_num:02d}_{role.lower().replace(' ', '_')}.jpg")
                continue

            best_match = None
            best_score = float("inf")
            best_path = None

            for query in queries:
                if best_match and best_score < tolerance * 0.5:
                    break  # Already found a great one

                print(f"  Query: {query}")
                try:
                    urls = search_fn(query, max_images=max_candidates)
                except Exception as e:
                    print(f"    Search failed: {e}")
                    continue

                print(f"    {len(urls)} unique URLs")

                for url in urls:
                    # Derive safe filename
                    h = hashlib.sha256(url.encode()).hexdigest()[:12]
                    ext = url.split("?")[0].split(".")[-1].lower()
                    if ext not in ("jpg", "jpeg", "png", "webp", "gif"):
                        ext = "jpg"
                    tmp_path = tmp_dir / f"s{slide_num}_{h}.{ext}"

                    if download_image(url, tmp_path, timeout=download_timeout):
                        ratio, w, h_dim = get_image_info(tmp_path)
                        if ratio is None:
                            tmp_path.unlink(missing_ok=True)
                            continue

                        if w < min_width or h_dim < min_height:
                            print(f"      {w}x{h_dim} -> too small, skipping")
                            tmp_path.unlink(missing_ok=True)
                            continue

                        score = abs(ratio - target_ratio)
                        print(f"      {w}x{h_dim} ratio={ratio:.3f} score={score:.3f}")

                        if score < best_score and score <= tolerance:
                            # Clean up previous best if it exists
                            if best_path and best_path.exists():
                                best_path.unlink(missing_ok=True)
                            best_score = score
                            best_match = url
                            best_path = tmp_path
                        else:
                            tmp_path.unlink(missing_ok=True)

            if best_path and best_path.exists():
                dest = output_dir / f"slide_{slide_num:02d}_{role.lower().replace(' ', '_')}.jpg"
                # Convert to jpg if needed
                try:
                    from PIL import Image as PILImage
                    with PILImage.open(best_path) as img:
                        rgb_img = img.convert("RGB")
                        rgb_img.save(dest, "JPEG", quality=92)
                except Exception:
                    shutil.copy(best_path, dest)
                best_path.unlink(missing_ok=True)
                print(f"  => Saved: {dest.name}")
            else:
                print(f"  => NO SUITABLE IMAGE FOUND for slide {slide_num}")

    finally:
        # Cleanup temp dir
        shutil.rmtree(tmp_dir, ignore_errors=True)

    print("\n" + "=" * 50)
    print("Image sourcing complete.")
    print(f"Check: {output_dir.resolve()}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python source_images.py <path/to/image_preset.json>")
        sys.exit(1)
    run_preset(sys.argv[1])

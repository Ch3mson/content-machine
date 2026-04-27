import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "browser-harness"))

from admin import ensure_daemon
from helpers import new_tab, wait_for_load, wait, js

ensure_daemon()

# Test slide 1 query
query = "lebron james young akron childhood"
url = f"https://duckduckgo.com/?q={query.replace(' ', '%20')}&iax=images&ia=images"
print("Navigating to:", url)
new_tab(url)
wait_for_load()
wait(3)

for i in range(3):
    js("window.scrollBy(0, 900)")
    wait(1)

script = """
[...new Set(
    [...document.querySelectorAll('img')]
    .map(i => i.src || i.getAttribute('data-src'))
    .filter(u => u && u.startsWith('http'))
)]
"""
urls = js(script)
print(f"Found {len(urls)} URLs")

# Test download first candidate
import urllib.request
if urls:
    dest = Path("test_image.jpg")
    req = urllib.request.Request(urls[0], headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as r:
        dest.write_bytes(r.read())
    print(f"Downloaded {dest} ({dest.stat().st_size} bytes)")

    from PIL import Image
    with Image.open(dest) as img:
        w, h = img.size
        ratio = w / h
        print(f"Dimensions: {w}x{h}, ratio: {ratio:.4f} (target 0.5625)")
    dest.unlink()

print("Test passed!")

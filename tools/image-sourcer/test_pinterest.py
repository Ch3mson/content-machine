import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "browser-harness"))

from admin import ensure_daemon
from helpers import new_tab, wait_for_load, wait, js

ensure_daemon()

query = "lebron james young"
url = f"https://www.pinterest.com/search/pins/?q={query.replace(' ', '%20')}"
print("Navigating to:", url)
new_tab(url)
wait_for_load()
wait(3)

for i in range(5):
    js("window.scrollBy(0, 1000)")
    wait(1.5)

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

print(f"Found {len(urls)} Pinterest image URLs")
for u in urls[:10]:
    print(u[:90])

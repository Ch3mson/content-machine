import sys
sys.path.insert(0, 'tools/browser-harness')
from admin import ensure_daemon
from helpers import new_tab, wait_for_load, wait, js

ensure_daemon()
new_tab('https://www.pinterest.com/search/pins/?q=lebron+james+portrait+4k')
wait_for_load()
wait(3)
for i in range(3):
    js('window.scrollBy(0, 1000)')
    wait(1)

urls = js("""
(function(){
    const out = [];
    document.querySelectorAll('img').forEach(function(i) {
        if (i.src) out.push(i.src);
    });
    return [...new Set(out.filter(function(u) {
        return u && u.includes('pinimg.com') && !u.includes('/60x60/');
    }))];
})()
""")

print('Found', len(urls), 'URLs')

import urllib.request
from PIL import Image
import os

for u in urls[:8]:
    u = u.replace('/236x/', '/736x/').replace('/474x/', '/736x/')
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            data = r.read()
            with open('tmp.jpg', 'wb') as f:
                f.write(data)
        with Image.open('tmp.jpg') as img:
            w, h = img.size
            print(f'{w}x{h} ratio={w/h:.3f} | {u[:60]}')
        os.remove('tmp.jpg')
    except Exception as e:
        print('fail:', str(e)[:60])

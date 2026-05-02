import sys
import urllib.parse
sys.path.insert(0, '.')

from admin import ensure_daemon
from helpers import new_tab, wait_for_load, wait, js

ensure_daemon()

q = 'lebron james young'
url = f'https://duckduckgo.com/?q={urllib.parse.quote(q)}&iax=images&ia=images'
new_tab(url)
wait_for_load()
wait(3)

for i in range(3):
    js('window.scrollBy(0, 900)')
    wait(1)

script = """
[...new Set(
    [...document.querySelectorAll('img')]
    .map(i => i.src || i.getAttribute('data-src'))
    .filter(u => u && u.startsWith('http'))
)]
"""
urls = js(script)
print('Found', len(urls), 'image URLs')
for u in (urls or [])[:5]:
    print(u[:80])

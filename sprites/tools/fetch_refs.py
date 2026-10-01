"""Search DeviantArt for pixel-art references of a character, download original PNGs (og:image with the resize
step stripped), and record sources. usage: python3 fetch_refs.py <key> "<search name>" <slug-token>[,<token>...]"""
import os, re, sys, json, subprocess, html
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36'
def get(url, binary=False):
    r = subprocess.run(['curl', '-sL', '-m', '25', '-A', UA, url], capture_output=True)
    return r.stdout if binary else r.stdout.decode('utf8', 'ignore')
key, name, tokens = sys.argv[1], sys.argv[2], sys.argv[3].lower().split(',')
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'refs', 'candidates', key); os.makedirs(out, exist_ok=True)
links = []
for q in (f'{name} pixel art', f'{name} sprite', f'{name} chibi pixel', f'{name} 8 bit'):
    page = get('https://www.deviantart.com/search?q=' + q.replace(' ', '+'))
    for u in re.findall(r'https://www\.deviantart\.com/[a-z0-9_-]+/art/[A-Za-z0-9-]+-\d{6,}', page):
        slug = u.split('/art/')[1].lower()
        if any(t in slug for t in tokens) and u not in links: links.append(u)
links = links[:14]
src = {}
for i, u in enumerate(links):
    m = re.search(r'property="og:image" content="([^"]+)"', get(u))
    if not m: continue
    img = re.sub(r'/v1/[^?]*', '', html.unescape(m.group(1)))
    data = get(img, binary=True)
    if len(data) < 200: continue
    fn = f'{i:02d}.img'; open(os.path.join(out, fn), 'wb').write(data); src[fn] = u
json.dump(src, open(os.path.join(out, 'sources.json'), 'w'), indent=1)
print(key, len(links), 'links,', len(src), 'images')

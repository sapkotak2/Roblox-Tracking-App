"""All 31 characters fitted to Luffy's proportions (tools/fit_luffy.py) from their raw JUS-style frames.
Output: out/fit/<name>.png"""
import os, sys, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
from fit_luffy import fit, LUFFY
from clean_palette import clean
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
src = open(f'{R}/tools/build_roster31.py').read()
base = {'F': f'{R}/refs/jus_fan', 'C': f'{R}/refs/candidates', 'J': f'{R}/refs/jus'}
PICKS = {n: f'{base[k]}/{p}' for n, k, p in re.findall(r"'(\w+)': f'\{(\w)\}/([^']+)'", src)}
OVR = {'toji': dict(head_s=1.0)}          # per-character fit overrides, e.g. {'asta': dict(max_w=40)}
os.makedirs(f'{R}/out/fit', exist_ok=True); os.makedirs(f'{R}/refs/jus_picks', exist_ok=True)
sizes = {}
for name, path in PICKS.items():
    raw = Image.open(path).convert('RGBA'); raw.save(f'{R}/refs/jus_picks/{name}.png')
    out = fit(raw, **OVR.get(name, {}))
    if name == 'megumi':
        p = out.load()
        for y in range(out.height // 2):
            for x in range(out.width):
                if p[x, y][:3] == (165, 82, 68): p[x, y] = (226, 157, 123, 255)
    out.save(f'{R}/out/fit/{name}.png')
    if len(out.getcolors(1 << 20)) > 70: out = clean(f'{R}/out/fit/{name}.png', f'{R}/out/fit/{name}.png', 22)
    sizes[name] = out.size
print(json.dumps(sizes))

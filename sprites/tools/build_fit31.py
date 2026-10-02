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
NECK = {'aizen': 14, 'byakuya': 14, 'gaara': 14, 'geto': 16, 'grimmjow': 14, 'hinata': 13, 'itachi': 14, 'kakashi': 13, 'madara': 15, 'megumi': 14, 'neji': 15, 'obito': 16, 'renji': 21, 'toji': 18, 'urahara': 17, 'yhwach': 18}   # chin line read from the ruler sheets (auto-detection cut faces)
OVR = {n: dict(neck=v) for n, v in NECK.items()}
OVR['ishida'] = dict(neck=14, head_s=1.45, head_w=18)
FACE_FIX = {}   # Bleach: Dark Souls sprite: realistic proportions, tiny head          # per-character fit overrides, e.g. {'asta': dict(max_w=40)}
os.makedirs(f'{R}/out/fit', exist_ok=True); os.makedirs(f'{R}/refs/jus_picks', exist_ok=True)
sizes = {}
for name, path in PICKS.items():
    raw = Image.open(path).convert('RGBA'); raw.save(f'{R}/refs/jus_picks/{name}.png')
    out = fit(raw, **OVR.get(name, {}))
    for src_c, dst_c in FACE_FIX.get(name, {}).items():
        p = out.load()
        for y in range(out.height // 2):
            for x in range(out.width):
                if p[x, y][:3] == src_c: p[x, y] = dst_c + (255,)
    if name == 'megumi':
        p = out.load()
        for y in range(out.height // 2):
            for x in range(out.width):
                if p[x, y][:3] == (165, 82, 68): p[x, y] = (226, 157, 123, 255)
    out.save(f'{R}/out/fit/{name}.png')
    if len(out.getcolors(1 << 20)) > 70: out = clean(f'{R}/out/fit/{name}.png', f'{R}/out/fit/{name}.png', 22)
    sizes[name] = out.size
# Ishida: keep the exact earlier version the user preferred over later attempts
_ish = Image.open(f'{R}/refs/jus_picks/ishida_final.png').convert('RGBA')
from seamscale import grow
def _thicken(im, neck=19, split=12, extra=6):     # widen only the robe (right of the bow arm); head untouched
    head = im.crop((0, 0, im.width, neck)); left = im.crop((0, neck, split, im.height)); right = im.crop((split, neck, im.width, im.height))
    nr = grow(right.transpose(Image.TRANSPOSE), right.width + extra).transpose(Image.TRANSPOSE)
    out = Image.new('RGBA', (im.width + extra, im.height), (0, 0, 0, 0))
    out.alpha_composite(left, (0, neck)); out.alpha_composite(nr, (split, neck)); out.alpha_composite(head, (extra // 2, 0))
    return out.crop(out.getbbox())
_thicken(_ish).save(f'{R}/out/fit/ishida.png')
print(json.dumps(sizes))

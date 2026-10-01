"""Android 17 (mrinsnj) + Hit (aosorto88): exact pixels from the artists' original PNGs (refs/candidates/),
background flood-removed, then grown to roster height with the head rows protected."""
import os, sys
from collections import deque
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
from seamscale import grow
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
def cut(im, tol=24):
    im = im.convert('RGBA'); p = im.load(); w, h = im.size; bg = p[0, 0][:3]
    seen = set(); q = deque([(x, y) for x in range(w) for y in (0, h-1)] + [(x, y) for y in range(h) for x in (0, w-1)])
    while q:
        x, y = q.popleft()
        if (x, y) in seen or not (0 <= x < w and 0 <= y < h): continue
        seen.add((x, y))
        if p[x, y][3] == 0 or sum(abs(a - b) for a, b in zip(p[x, y][:3], bg)) > tol: continue
        p[x, y] = (0, 0, 0, 0); q.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])
    return im.crop(im.getbbox())
a17 = Image.open(f'{R}/refs/candidates/android17_opt3.png').convert('RGBA')          # already cut from the original
hit = cut(Image.open(f'{R}/refs/candidates/hit_1_orig'))
a17.save(f'{R}/refs/android17_native.png'); hit.save(f'{R}/refs/hit_native.png')
print('native', a17.size, hit.size)
grow(a17, 51, round(a17.width * 51 / a17.height), protect_rows=((0, 15),)).save(f'{R}/out/android17.png')
grow(hit, 54, round(hit.width * 54 / hit.height), protect_rows=((0, 12),)).save(f'{R}/out/hit.png')
for n in ('android17', 'hit'): print(n, Image.open(f'{R}/out/{n}.png').size)

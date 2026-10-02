"""Rank every standing frame we have for a character by face visibility: skin pixels in the head area, relative
to sprite height (bigger, clearer faces score higher). Writes refs/faces/<key>/top_<i>.png"""
import os, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
from sheet_frames import frames
from face_clarity import is_skin
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
S = '/tmp/claude-0/-home-user-Roblox-Tracking-App/faeb5496-bf1f-56ac-b86c-68b66f0a1600/scratchpad/fs.png'
def score(f):
    f = f.convert('RGBA'); h = f.height; p = f.load()
    top = int(h * 0.42); skin = sum(1 for y in range(top) for x in range(f.width) if p[x, y][3] and is_skin(p[x, y][:3]))
    return skin / (h * h) * 1000
def screen(key, extra_dirs):
    cands = []
    for d in [f'{R}/refs/{x}/{key}' for x in ('faces', 'jus_fan', 'candidates', 'batch3')] + extra_dirs:
        for fn in glob.glob(f'{d}/*.img') + glob.glob(f'{d}/*.png'):
            try:
                im = Image.open(fn); im.load()
                if im.width * im.height > 6_000_000: continue
                im.convert('RGBA').save(S); fs = frames(S)
            except Exception: continue
            for fr in fs:
                if 34 <= fr.height <= 110 and fr.height >= 1.15 * fr.width: cands.append((score(fr), fr, fn))
    cands.sort(key=lambda c: -c[0]); out = []; seen = set()
    for s, fr, fn in cands:
        sig = (fr.size, fn)
        if sig in seen: continue
        seen.add(sig); out.append((s, fr, fn))
        if len(out) == 6: break
    os.makedirs(f'{R}/refs/faces/{key}', exist_ok=True)
    for i, (s, fr, fn) in enumerate(out): fr.save(f'{R}/refs/faces/{key}/top_{i}.png')
    return [(round(s, 1), fr.size, os.path.relpath(fn, R)) for s, fr, fn in out]
if __name__ == '__main__':
    for k in sys.argv[1:]: print(k, screen(k, []))

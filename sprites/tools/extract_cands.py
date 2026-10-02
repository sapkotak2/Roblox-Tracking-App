"""For one character dir: every downloaded image -> (if upscaled pixel art) recover native grid -> cut frames ->
keep standing figures 32-120 px tall -> cand_<n>.png (max 10, varied sources). usage: extract_cands.py <dir>"""
import os, sys, glob, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
from sheet_frames import frames
import recover_grid
d = sys.argv[1]; tmp = os.path.join(d, '_t.png')
for f in glob.glob(f'{d}/cand_*.png'): os.remove(f)
out = []
for fn in sorted(glob.glob(f'{d}/*.img')):
    try:
        im = Image.open(fn); im.load()
        if im.width * im.height > 6_000_000: continue
        im.convert('RGBA').save(tmp)
        srcs = [tmp]
        if max(im.size) > 160 and im.width * im.height < 2_500_000:
            try:
                import io, contextlib
                with contextlib.redirect_stdout(io.StringIO()):
                    recover_grid.recover(tmp, tmp + '.n.png')
                n = Image.open(tmp + '.n.png')
                if 30 <= n.height <= 400 and n.width * 1.0 < im.width / 1.5: srcs.append(tmp + '.n.png')
            except Exception: pass
        got = 0
        for s in srcs:
            for fr in frames(s):
                if 32 <= fr.height <= 120 and fr.height >= 1.1 * fr.width and fr.width >= 12:
                    out.append((fn, fr)); got += 1
                    if got >= 3: break
            if got: break
    except Exception: continue
for f in glob.glob(f'{d}/_t.png*'): os.remove(f)
for i, (fn, fr) in enumerate(out[:10]): fr.save(f'{d}/cand_{i}.png')
json.dump({f'cand_{i}.png': os.path.basename(fn) for i, (fn, fr) in enumerate(out[:10])}, open(f'{d}/cands.json', 'w'))
print(os.path.basename(d), min(len(out), 10))

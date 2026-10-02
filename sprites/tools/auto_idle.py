"""For every downloaded sheet of a character, cut frames and keep the first 'standing' one (roster-ish size,
taller than wide). Writes refs/<subdir>/<key>/idle_<NN>.png. usage: auto_idle.py <subdir> <key>"""
import os, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
from sheet_frames import frames
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sub, key = sys.argv[1], sys.argv[2]
d = f'{R}/refs/{sub}/{key}'
for f in sorted(glob.glob(f'{d}/*.img')):
    try:
        im = Image.open(f); im.load()
        if im.width * im.height > 5_000_000: continue
        im.convert('RGBA').save(f + '.png')
        fs = frames(f + '.png')
    except Exception as e:
        continue
    pick = next((fr for fr in fs if 38 <= fr.height <= 90 and fr.height >= 1.25 * fr.width), None)
    if pick: pick.save(f'{d}/idle_{os.path.basename(f)[:2]}.png')
    os.remove(f + '.png')
print(key, len(glob.glob(f'{d}/idle_*.png')))

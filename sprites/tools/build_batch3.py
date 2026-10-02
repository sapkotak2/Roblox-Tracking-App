"""Batch 3: chosen frame per character -> fit to Luffy -> out/b3/<name>.png"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
from fit_luffy import fit
from clean_palette import clean
from face_simplify import simplify_head
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
B = f'{R}/refs/batch3'
PICK = dict(aizawa=3, akaza=1, allmight=0, armin=0, asuna=6, baki=5, bakugo=3, chrollo=1, daki=0, deku=3, edward=4,
            endeavor=0, eren=0, erza=8, escanor=3, gabimaru=0, gintoki=0, giyu=0, guts=0, hisoka=4, jinwoo=0, kirito=4,
            kurapika=0, lelouch=8, levi=0, makima=0, meliodas=1, mikasa=0, mob=9, muichiro=0, muzan=0, natsu=0,
            nezuko=3, okarun=0, overhaul=0, rengoku=0, senku=1, shinichi=0, shinra=0, subaru=0, thorfinn=2,
            todoroki=3, tomura=4, zenitsu=0)
SRC = {k: f'{B}/{k}/cand_{v}.png' for k, v in PICK.items()}
SRC.update(rengoku=f'{R}/refs/b3_extra/rengoku.png', senku=f'{R}/refs/b3_extra/senku.png', gon=f'{R}/refs/jus/gon_stand0.png', jotaro=f'{R}/refs/jus/jotaro_stand0.png')
OVR = {'armin': dict(head_s=0.85, head_w=20), 'escanor': dict(max_w=32)}
os.makedirs(f'{R}/out/b3', exist_ok=True); os.makedirs(f'{R}/refs/b3_picks', exist_ok=True)
sizes = {}
for n, p in sorted(SRC.items()):
    raw = Image.open(p).convert('RGBA'); raw.save(f'{R}/refs/b3_picks/{n}.png')
    o = simplify_head(fit(raw, **OVR.get(n, {})), 19, 45)   # fewer face colours = easier to read
    o.save(f'{R}/out/b3/{n}.png')
    if len(o.getcolors(1 << 20) or []) > 70: o = clean(f'{R}/out/b3/{n}.png', f'{R}/out/b3/{n}.png', 22)
    sizes[n] = o.size
print(len(sizes), json.dumps(sizes))

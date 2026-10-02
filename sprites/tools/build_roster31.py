"""Build the 31-character batch: one JUS-style standing frame per character -> chibify with the same rules
(head x1.5, body x1.3, body height x0.78) -> out/jus/<name>.png. Per-character overrides in OVR."""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
from chibify import chibify
from seamscale import shrink_rows
from clean_palette import clean
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
F, C, J = f'{R}/refs/jus_fan', f'{R}/refs/candidates', f'{R}/refs/jus'
PICKS = {
 # official Jump Ultimate Stars
 'sasuke': f'{J}/sasuke_idle.png', 'frieza': f'{J}/frieza_idle.png', 'kakashi': f'{J}/kakashi_stand4.png',
 'hitsugaya': f'{J}/hitsugaya_standB.png', 'renji': f'{J}/renji_standA.png',
 # fan JUS-style
 'hinata': f'{F}/hinata/idle_00.png', 'boruto': f'{F}/boruto/idle_00.png', 'itachi': f'{F}/itachi/idle_00.png',
 'obito': f'{F}/obito/idle_04.png', 'madara': f'{F}/madara/idle_13.png', 'jiraiya': f'{F}/jiraiya/idle_02.png',
 'neji': f'{F}/neji/idle_00.png', 'gaara': f'{F}/gaara/frame_07_0.png', 'ishida': f'{J}/ishida_bds_51.png',
 'aizen': f'{F}/aizen/idle_11.png', 'yhwach': f'{C}/yhwach/idle_00.png', 'orihime': f'{F}/orihime/idle_01.png',
 'byakuya': f'{F}/byakuya/idle_04.png', 'kenpachi': f'{F}/kenpachi/idle_08.png', 'urahara': f'{F}/urahara/idle_03.png',
 'grimmjow': f'{F}/grimmjow/idle_01.png', 'ulquiorra': f'{F}/ulquiorra/idle_06.png', 'itadori': f'{F}/sukuna/idle_03.png',
 'sukuna': f'{F}/sukuna/idle_00.png', 'toji': f'{C}/toji/idle_toji_half.png', 'megumi': f'{F}/megumi/idle_01.png',
 'mahito': f'{C}/mahito/idle_03.png', 'geto': f'{C}/geto/idle_04.png', 'okkotsu': f'{C}/okkotsu/idle_04.png',
 'asta': f'{F}/asta/frame_00_25.png', 'yuno': f'{F}/yuno/idle_05.png',
}
OVR = {   # (head_scale, body_widen, body_squash, neck)
 'frieza': dict(body_widen=1.55),
 'toji': dict(head_scale=1.15, body_widen=1.15, body_squash=0.9),
 'geto': dict(head_scale=1.05, body_widen=1.1, body_squash=0.7),
 'neji': dict(body_widen=1.1),
 'ishida': dict(head_scale=1.35, body_widen=1.25, body_squash=0.6),
 'megumi': dict(head_scale=1.75),
 'mahito': dict(head_scale=1.35, body_widen=1.0),
 'asta': dict(body_widen=1.45),
}
os.makedirs(f'{R}/out/jus', exist_ok=True)
sizes = {}
for name, path in PICKS.items():
    im = Image.open(path).convert('RGBA'); im = im.crop(im.getbbox())
    kw = dict(head_scale=1.5, body_widen=1.3, body_squash=0.78); kw.update(OVR.get(name, {}))
    out = chibify(im, kw['head_scale'], kw['body_widen'], body_squash=kw['body_squash'], neck=kw.get('neck'))
    if name == 'megumi':   # face readability: muddy dark face shade -> mid skin shade
        p = out.load()
        for y in range(out.height // 2):
            for x in range(out.width):
                if p[x, y][:3] == (165, 82, 68): p[x, y] = (226, 157, 123, 255)
    out.save(f'{R}/out/jus/{name}.png')
    if len(out.getcolors(1 << 20)) > 70:   # compression noise from the source -> merge near-identical shades
        out = clean(f'{R}/out/jus/{name}.png', f'{R}/out/jus/{name}.png', 22)
    sizes[name] = out.size
print(json.dumps(sizes))

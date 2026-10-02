"""Regenerate export/dbz_sprites.js (self-contained Node PNG writer) from the final sprites in out/ and out/jus/."""
import os, json, re
from PIL import Image
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
KEYS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#$%&*+-=?@!^~<>:;_|/[](){}'
DBZ = ['vegeta', 'piccolo', 'krillin', 'beerus', 'whis', 'trunks', 'jiren', 'android17', 'hit']
JUS = sorted(f[:-4] for f in os.listdir(f'{R}/out/jus') if f.endswith('.png'))
src = open(f'{R}/export/dbz_sprites.js').read()
head_end, tail_start = src.index('const SPRITES = {'), src.index('function crc32')
parts, sizes = [], []
for n, path in [(n, f'{R}/out/{n}.png') for n in DBZ] + [(n, f'{R}/out/jus/{n}.png') for n in JUS]:
    im = Image.open(path).convert('RGBA'); w, h = im.size; px = im.load(); pal = {}; rows = []
    for y in range(h):
        r = ''
        for x in range(w):
            c = px[x, y]
            if c[3] == 0: r += '.'; continue
            k = '%02x%02x%02x' % c[:3]
            if k not in pal:
                if len(pal) >= len(KEYS): raise SystemExit(f'{n}: too many colours')
                pal[k] = KEYS[len(pal)]
            r += pal[k]
        rows.append(r)
    sizes.append(f'{n} ({w}x{h})')
    parts.append(f"  {n}: {{\n    palette: {json.dumps({v: k for k, v in pal.items()})},\n    rows: [\n" + ',\n'.join('      ' + json.dumps(r) for r in rows) + "\n    ]\n  }")
header = re.sub(r'// StickFight (DBZ )?sprites[^\n]*\n', f'// StickFight sprites ({len(sizes)}): ' + ', '.join(sizes) + '. All face right.\n', src[:head_end])
header = header.replace('// StickFight sprites', '// StickFight DBZ sprites', 0)
open(f'{R}/export/dbz_sprites.js', 'w').write(header + 'const SPRITES = {\n' + ',\n'.join(parts) + '\n};\n\n' + src[tail_start:])
print(len(sizes), 'sprites')

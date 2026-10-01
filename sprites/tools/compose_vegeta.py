"""Full Vegeta sprite = profile head (chars/vegeta_head.txt) + armour body (chars/vegeta_body.txt)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
from grid import load
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
head = load(f'{R}/chars/vegeta_head.txt'); body = load(f'{R}/chars/vegeta_body.txt')
out = Image.new('RGBA', (28, 56), (0, 0, 0, 0))
out.alpha_composite(head, (3, 1))     # head 1 px lower = shorter neck
out.alpha_composite(body, (4, 30))   # body drawn over the neck stub
out.save(f'{R}/out/vegeta.png')
bg = (213, 225, 237)
tiles = [Image.open(f'{R}/refs/game/{n}_native.png') for n in ('tanjiro', 'robin', 'luffy')] + [out, Image.open(f'{R}/refs/game/zoro_native.png')]
Hh = max(t.height for t in tiles); W = sum(t.width + 4 for t in tiles)
for name, b in (('light', bg), ('dark', (10, 14, 26))):
    sh = Image.new('RGBA', (W, Hh), b + (255,)); x = 2
    for t in tiles: sh.alpha_composite(t, (x, Hh - t.height)); x += t.width + 4
    sh.resize((W * 8, Hh * 8), Image.NEAREST).save(f'{R}/out/vegeta_compare_{name}.png')

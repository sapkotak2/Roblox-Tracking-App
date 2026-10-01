"""Piccolo - exact pixels recovered from the user's reference (refs/piccolo_ref.png, 8.86 px grid; see refs/piccolo_native_raw.png),
cleaned (stray sticker-border greys removed, colours quantized) and mirrored to face right."""
import os
from PIL import Image
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
im = Image.open(f'{R}/refs/piccolo_native_raw.png').convert('RGBA'); p = im.load(); W, H = im.size
for y in range(H):
    for x in range(W):
        r, g, b, a = p[x, y]
        if not a: continue
        grey = max(r, g, b) - min(r, g, b) < 18 and r > 150
        alone = not any(0 <= x+dx < W and 0 <= y+dy < H and p[x+dx, y+dy][3] for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)))
        if grey or alone: p[x, y] = (0, 0, 0, 0)
alpha = im.getchannel('A')
q = im.convert('RGB').quantize(colors=20, method=Image.MEDIANCUT, dither=Image.NONE).convert('RGB')
out = Image.new('RGBA', im.size, (0,0,0,0)); out.paste(q, (0, 0), alpha)
out = out.crop(out.getbbox()).transpose(Image.FLIP_LEFT_RIGHT)
out.save(f'{R}/out/piccolo.png')
b = Image.new('RGBA', out.size, (255,255,255,255)); b.alpha_composite(out)
b.resize((out.width*16, out.height*16), Image.NEAREST).save(f'{R}/out/piccolo_20x.png')
print(out.size)

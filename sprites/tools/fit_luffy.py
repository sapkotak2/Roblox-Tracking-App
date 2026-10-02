"""Normalise every sprite to the game's Luffy: same head height/width, same body height, same core body width.
Resizing is crisp: rows/columns are duplicated (grow) or the most redundant ones removed (shrink); no resampling."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
from seamscale import grow, shrink_rows
from chibify import neck_row
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

def spans(im):
    a = im.getchannel('A'); out = []
    for y in range(im.height):
        xs = [x for x in range(im.width) if a.getpixel((x, y))]
        out.append((min(xs), max(xs)) if xs else None)
    return out

def core_width(im):
    """median row width over the middle 60% of the rows - ignores weapon tips / feet / hair spikes"""
    s = [b - a + 1 for a, b in (r for r in spans(im)[int(im.height * .2):int(im.height * .8)] if r)]
    s.sort(); return s[len(s) // 2] if s else im.width

def resize(im, w, h, protect_rows=()):
    im = im.crop(im.getbbox())
    if h > im.height: im = grow(im, h, protect_rows=protect_rows)
    elif h < im.height: im = shrink_rows(im, im.height - h, protect=protect_rows)
    t = im.transpose(Image.TRANSPOSE)
    if w > im.width: t = grow(t, w)
    elif w < im.width: t = shrink_rows(t, im.width - w)
    return t.transpose(Image.TRANSPOSE)

def metrics(im):
    im = im.crop(im.getbbox()); n = neck_row(im)
    head = im.crop((0, 0, im.width, n)); head = head.crop(head.getbbox())
    body = im.crop((0, n, im.width, im.height)); body = body.crop(body.getbbox())
    return dict(neck=n, head_w=head.width, head_h=head.height, body_h=body.height, core=core_width(body), W=im.width, H=im.height)

LUFFY = metrics(Image.open(f'{R}/refs/game/luffy_native.png'))

def fit(im, T=LUFFY, head_w=None, neck=None, max_w=None, head_s=None):
    im = im.convert('RGBA'); im = im.crop(im.getbbox())
    n = neck if neck is not None else neck_row(im)
    head = im.crop((0, 0, im.width, n)); hb = head.getbbox(); head = head.crop(hb)
    body = im.crop((0, n, im.width, im.height)); bb = body.getbbox(); body = body.crop(bb)
    # head: Luffy's head height; width follows the character's own head shape, kept within +-15% of Luffy's
    # scale capped so a head is never more than ~1.6x grown (blocky) or 0.85x shrunk (squashed)
    s = head_s or max(.85, min(1.6, T['head_h'] / head.height))
    hh = round(head.height * s)
    hw = head_w or round(head.width * s)
    if not head_w: hw = max(round(T['head_w'] * .8), min(round(T['head_w'] * 1.2), hw))
    nh = resize(head, hw, hh)
    # body: Luffy's body height, and scaled so the core (torso/legs) width equals Luffy's
    sx = T['core'] / core_width(body)
    bw = round(body.width * sx)
    if max_w: bw = min(bw, max_w)
    nb = resize(body, bw, T['body_h'] + (T['head_h'] - hh))   # total height stays Luffy's
    cx = ((hb[0] + hb[2]) / 2 - bb[0]) * nb.width / body.width
    left = round(cx - nh.width / 2); x0 = min(0, left); W = max(nb.width, left + nh.width) - x0
    out = Image.new('RGBA', (W, nh.height + nb.height), (0, 0, 0, 0))
    out.alpha_composite(nb, (-x0, nh.height)); out.alpha_composite(nh, (left - x0, 0))
    return out.crop(out.getbbox())

if __name__ == '__main__':
    print('LUFFY', LUFFY)

"""Convert a slim fighting-game sprite (e.g. Jump Ultimate Stars) into the roster's chibi proportions, crisply:
the head (rows above the neck) is grown by duplicating its flattest rows/columns, the body is widened the same way,
then the head is re-seated over the neck. No resampling - every pixel is an original pixel."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image
from seamscale import grow, shrink_rows

def opaque_cols(im, y):
    a = im.getchannel('A'); return [x for x in range(im.width) if a.getpixel((x, y))]

def neck_row(im, lo=0.18, hi=0.40):
    best = None
    for y in range(int(im.height * lo), int(im.height * hi)):
        xs = opaque_cols(im, y)
        if xs:
            wdt = max(xs) - min(xs) + 1
            if best is None or wdt < best[0]: best = (wdt, y)
    return best[1]

def chibify(im, head_scale=1.45, body_widen=1.25, target_h=None, neck=None, body_squash=0.8):
    im = im.convert('RGBA'); y = neck if neck is not None else neck_row(im)
    head = im.crop((0, 0, im.width, y)); body = im.crop((0, y, im.width, im.height))
    hb = head.getbbox(); head = head.crop(hb)
    hx_center = (hb[0] + hb[2]) / 2
    nh = grow(head, round(head.height * head_scale), round(head.width * head_scale))
    bb = body.getbbox(); body = body.crop((bb[0], 0, bb[2], body.height))
    nb = grow(body.transpose(Image.TRANSPOSE), round(body.width * body_widen)).transpose(Image.TRANSPOSE)
    if body_squash < 1: nb = shrink_rows(nb, round(nb.height * (1 - body_squash)), protect=((0, 2),))   # shorter chibi body/legs
    # where the neck centre lands in the widened body
    cx = (hx_center - bb[0]) * nb.width / body.width
    left = round(cx - nh.width / 2)
    x0 = min(0, left); W = max(nb.width, left + nh.width) - x0
    out = Image.new('RGBA', (W, nh.height + nb.height - 1), (0, 0, 0, 0))
    out.alpha_composite(nb, (-x0, nh.height - 1))
    out.alpha_composite(nh, (left - x0, 0))
    out = out.crop(out.getbbox())
    if target_h and out.height < target_h: out = grow(out, target_h, protect_rows=((0, nh.height),))
    return out

if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    chibify(Image.open(src), *(float(a) for a in sys.argv[3:5])).save(dst)

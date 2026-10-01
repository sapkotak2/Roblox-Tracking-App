"""Reference -> pixel art: cut out the background, shrink, quantize to a small palette, outline."""
from PIL import Image, ImageFilter
from collections import deque
OUT = (22, 16, 34)

def cutout(im, tol=38):
    """flood-fill near-white/edge-colour background from the borders -> transparent."""
    im = im.convert('RGBA'); w, h = im.size; px = im.load()
    corners = [px[0,0], px[w-1,0], px[0,h-1], px[w-1,h-1]]
    bg = tuple(sum(c[i] for c in corners)//4 for i in range(3))
    def near(p): return sum(abs(p[i]-bg[i]) for i in range(3)) < tol*3
    seen = set(); q = deque()
    for x in range(w):
        for y in (0, h-1): q.append((x, y))
    for y in range(h):
        for x in (0, w-1): q.append((x, y))
    while q:
        x, y = q.popleft()
        if (x, y) in seen or not (0 <= x < w and 0 <= y < h): continue
        seen.add((x, y))
        if not near(px[x, y]): continue
        px[x, y] = (0, 0, 0, 0)
        q.extend(((x+1,y),(x-1,y),(x,y+1),(x,y-1)))
    return im

def bbox_crop(im):
    return im.crop(im.getchannel('A').point(lambda a: 255 if a > 10 else 0).getbbox())

def pixelize(im, width=None, height=None, colors=14, mirror=False, outline=True, sharpen=True):
    im = bbox_crop(im)
    if mirror: im = im.transpose(Image.FLIP_LEFT_RIGHT)
    w, h = im.size
    if width and not height: height = round(h * width / w)
    if height and not width: width = round(w * height / h)
    big = im.resize((width * 4, height * 4), Image.LANCZOS)
    small = big.resize((width, height), Image.BOX)
    a = small.getchannel('A').point(lambda v: 255 if v >= 128 else 0)
    rgb = small.convert('RGB')
    q = rgb.quantize(colors=colors, method=Image.MEDIANCUT, dither=Image.NONE).convert('RGB')
    out = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    out.paste(q, (0, 0), a)
    if outline:
        o = out.load(); res = out.copy(); r = res.load()
        for y in range(height):
            for x in range(width):
                if o[x, y][3] == 0: continue
        pad = Image.new('RGBA', (width + 2, height + 2), (0, 0, 0, 0)); pad.paste(out, (1, 1))
        po = pad.load(); pr = pad.copy(); prr = pr.load()
        for y in range(height + 2):
            for x in range(width + 2):
                if po[x, y][3]: continue
                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < width+2 and 0 <= ny < height+2 and po[nx, ny][3]:
                        prr[x, y] = OUT + (255,); break
        out = pr
    return out

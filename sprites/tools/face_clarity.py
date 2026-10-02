"""Face readability pass (head rows only): skin shades are remapped onto Luffy-style light skin tones by
brightness rank, so faces read as a clear light patch like the game's own sprites."""
from PIL import Image
LUFFY_SKIN = [(250, 220, 188), (240, 196, 160), (214, 156, 120)]     # light, mid, shadow
def is_skin(c):
    r, g, b = c
    if r < 110 or not (r >= g >= b) or r - b < 35: return False
    if g / r > 0.86 and b / r < 0.45: return False                    # yellow hair / gold trim
    if b / r < 0.18: return False                                     # saturated orange/red cloth
    return True
def clarify(im, head_rows, keep=()):
    im = im.convert('RGBA'); p = im.load()
    cols = {}
    for y in range(min(head_rows, im.height)):
        for x in range(im.width):
            c = p[x, y]
            if c[3] and is_skin(c[:3]) and c[:3] not in keep: cols[c[:3]] = cols.get(c[:3], 0) + 1
    if not cols: return im
    ranked = sorted(cols, key=lambda c: -(0.3 * c[0] + 0.59 * c[1] + 0.11 * c[2]))
    n = len(ranked); mapping = {}
    for i, c in enumerate(ranked):
        mapping[c] = LUFFY_SKIN[0] if i < max(1, n // 3) else (LUFFY_SKIN[1] if i < max(2, 2 * n // 3) else LUFFY_SKIN[2])
    for y in range(min(head_rows, im.height)):
        for x in range(im.width):
            c = p[x, y]
            if c[3] and c[:3] in mapping: p[x, y] = mapping[c[:3]] + (255,)
    return im

def sharpen_eyes(im, rect):
    """inside the face rect, push near-black/dark non-skin pixels (eyes, brows) to crisp black so they pop on light skin"""
    im = im.convert('RGBA'); p = im.load(); x0, y0, x1, y1 = rect
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if 0 <= x < im.width and 0 <= y < im.height:
                r, g, b, a = p[x, y]
                if a and not is_skin((r, g, b)) and (r + g + b) < 300 and max(r, g, b) - min(r, g, b) < 90:
                    p[x, y] = (max(0, r - 60), max(0, g - 60), max(0, b - 60), 255)
    return im

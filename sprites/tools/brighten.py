"""Slight, even brightening for the whole roster: mid-tones lifted (gamma), a touch more saturation, outlines
(near-black) kept dark so sprites stay crisp. Applied as a final pass on copies; sources untouched."""
import colorsys
from PIL import Image
def bright_px(c, gamma=0.85, sat=1.12, keep_dark=42):
    r, g, b = c[:3]
    if max(r, g, b) < keep_dark: return c                      # outline / deepest black stays
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    l = l ** gamma; s = min(1.0, s * sat)
    r2, g2, b2 = colorsys.hls_to_rgb(h, l, s)
    return (round(r2 * 255), round(g2 * 255), round(b2 * 255)) + tuple(c[3:])
def brighten(im, **kw):
    im = im.convert('RGBA'); p = im.load(); cache = {}
    for y in range(im.height):
        for x in range(im.width):
            c = p[x, y]
            if c[3]:
                if c not in cache: cache[c] = bright_px(c, **kw)
                p[x, y] = cache[c]
    return im

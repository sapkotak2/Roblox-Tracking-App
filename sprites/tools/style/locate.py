"""Find where a native template appears in the style sheet at integer scales (masked SSE via FFT).
usage: python3 tools/style/locate.py luffy tanjiro ...   -> prints (rms, scale, x, y) best hit per scale
Searches only the two sprite bands of the light panel (4x row y 1000-1300, 2x roster row y 1840-2000, x < 830)."""
import sys
import numpy as np
from PIL import Image

SHEET = 'refs/game/style_sheet.webp'
BANDS = [(1000, 1300), (1840, 2000)]


def _corr(a, k):
    """'valid' cross-correlation of 2-D array a with kernel k via FFT"""
    H, W = a.shape; h, w = k.shape
    fh, fw = H + h, W + w
    r = np.fft.irfft2(np.fft.rfft2(a, (fh, fw)) * np.conj(np.fft.rfft2(k, (fh, fw))), (fh, fw))
    return r[:H - h + 1, :W - w + 1]


def find_in(sheet, nat, scales=(2, 4)):
    h, w = nat.shape[:2]
    m = (nat[..., 3] > 0).astype(np.float64); n = m.sum()
    best = {}
    for s in scales:
        for py in range(s):
            for px in range(s):
                sub = sheet[py:, px:]
                gh, gw = sub.shape[0] // s, sub.shape[1] // s
                if gh < h or gw < w:
                    continue
                g = sub[:gh * s, :gw * s].reshape(gh, s, gw, s, 3).mean((1, 3))
                sse = np.zeros((gh - h + 1, gw - w + 1))
                for ch in range(3):
                    c = nat[..., ch] * m
                    sse += _corr(g[..., ch] ** 2, m) - 2 * _corr(g[..., ch], c) + (c ** 2).sum()
                rms = np.sqrt(np.maximum(sse, 0) / n / 3)
                yy, xx = np.unravel_index(np.argmin(rms), rms.shape)
                hit = (float(rms[yy, xx]), s, px + xx * s, py + yy * s)
                if s not in best or hit < best[s]:
                    best[s] = hit
    return sorted(best.values())


def find(name, scales=(2, 4)):
    sheet = np.asarray(Image.open(SHEET).convert('RGB'), np.float64)
    nat = np.asarray(Image.open(f'refs/game/{name}_native.png').convert('RGBA'), np.float64)
    hits = []
    for y0, y1 in BANDS:
        for r, s, x, y in find_in(sheet[y0:y1, :830], nat, scales):
            hits.append((round(r, 1), s, int(x), int(y + y0)))
    return sorted(hits)


if __name__ == '__main__':
    for nm in sys.argv[1:]:
        print(nm, find(nm))

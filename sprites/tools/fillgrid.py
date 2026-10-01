"""Fill-only sprite authoring: draw shapes with fill letters (no outlines), then add the game's 1px dark outline
automatically around the silhouette and along chosen colour borders (e.g. hair/skin)."""
from PIL import Image
OUT = (29, 28, 33)

class Grid:
    def __init__(self, w, h): self.w, self.h = w, h; self.g = [['.'] * w for _ in range(h)]
    def sp(self, y, c, a, b):
        for x in range(a, b + 1):
            if 0 <= x < self.w and 0 <= y < self.h: self.g[y][x] = c
    def px(self, pts, c):
        for x, y in pts:
            if 0 <= x < self.w and 0 <= y < self.h: self.g[y][x] = c
    def rows(self, y0, spans):            # spans: {row: [(c,a,b),...]}
        for y, lst in spans.items():
            for c, a, b in lst: self.sp(y0 + y, c, a, b)
    def recolor(self, pts, frm, to):
        for x, y in pts:
            if 0 <= x < self.w and 0 <= y < self.h and self.g[y][x] == frm: self.g[y][x] = to

def render(grid, pal, edge_pairs=(), pad=1):
    """pal: letter -> rgb. edge_pairs: (setA, setB) - pixels of setA touching setB become outline."""
    W, H = grid.w + 2 * pad, grid.h + 2 * pad
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); p = im.load()
    L = [['.'] * W for _ in range(H)]
    for y in range(grid.h):
        for x in range(grid.w):
            c = grid.g[y][x]
            if c != '.': L[y + pad][x + pad] = c; p[x + pad, y + pad] = pal[c] + (255,)
    for y in range(H):
        for x in range(W):
            nb = [(x+dx, y+dy) for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)) if 0 <= x+dx < W and 0 <= y+dy < H]
            c = L[y][x]
            if c == '.':
                if any(L[ny][nx] != '.' for nx, ny in nb): p[x, y] = OUT + (255,)
            else:
                for A, B in edge_pairs:
                    if c in A and any(L[ny][nx] in B for nx, ny in nb): p[x, y] = OUT + (255,); break
    return im.crop(im.getbbox())

"""Split a sprite sheet (flat background colour) into frames: connected components (8-way) of non-background
pixels, merged when their boxes overlap/touch, returned in reading order. usage: sheet_frames.py sheet.png [n]"""
import sys
from PIL import Image
from collections import deque
def frames(path, tol=12, min_px=60):
    im = Image.open(path).convert('RGBA'); p = im.load(); w, h = im.size; bg = p[0, 0][:3]
    fg = [[p[x, y][3] and sum(abs(a - b) for a, b in zip(p[x, y][:3], bg)) > tol for x in range(w)] for y in range(h)]
    seen = [[False] * w for _ in range(h)]; boxes = []
    for y in range(h):
        for x in range(w):
            if fg[y][x] and not seen[y][x]:
                q = deque([(x, y)]); seen[y][x] = True; x0 = x1 = x; y0 = y1 = y; n = 0
                while q:
                    a, b = q.popleft(); n += 1
                    x0, x1, y0, y1 = min(x0, a), max(x1, a), min(y0, b), max(y1, b)
                    for dx in (-1, 0, 1):
                        for dy in (-1, 0, 1):
                            c, d = a + dx, b + dy
                            if 0 <= c < w and 0 <= d < h and fg[d][c] and not seen[d][c]: seen[d][c] = True; q.append((c, d))
                if n >= min_px: boxes.append([x0, y0, x1, y1])
    merged = True
    while merged:                                   # merge boxes that overlap or nearly touch (detached bits of one frame)
        merged = False
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                A, B = boxes[i], boxes[j]
                if A[0] - 2 <= B[2] and B[0] - 2 <= A[2] and A[1] - 2 <= B[3] and B[1] - 2 <= A[3]:
                    boxes[i] = [min(A[0], B[0]), min(A[1], B[1]), max(A[2], B[2]), max(A[3], B[3])]; boxes.pop(j); merged = True; break
            if merged: break
    boxes.sort(key=lambda b: (b[1] // 40, b[0]))
    out = []
    for x0, y0, x1, y1 in boxes:
        f = im.crop((x0, y0, x1 + 1, y1 + 1)); fp = f.load()
        for yy in range(f.height):
            for xx in range(f.width):
                if sum(abs(a - b) for a, b in zip(fp[xx, yy][:3], bg)) <= tol: fp[xx, yy] = (0, 0, 0, 0)
        out.append(f)
    return out
if __name__ == '__main__':
    fs = frames(sys.argv[1]); n = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    for i, f in enumerate(fs[:n]): print(i, f.size)

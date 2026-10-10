"""Kyojuro Rengoku (Demon Slayer) - chibi redraw (see tools/chibi.py for the style guide).
Matched to refs/redraw/rengoku (01 coloured body, face crop, tsuba), checklist in refs/redraw/rengoku/NOTES.md."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(34, 14, 16),                                   # outline
    y=(255, 206, 54), Y=(234, 142, 32), r=(204, 36, 36),   # hair base / shade / red tips (red also = flames, guard)
    s=(252, 212, 172), S=(222, 160, 122),             # skin
    e=(255, 252, 242), g=(250, 178, 30), k=(36, 16, 18), m=(150, 40, 32),   # eye white, gold iris, dark, mouth
    b=(62, 48, 50), B=(36, 26, 30),                   # brown-black uniform
    w=(246, 242, 232), W=(196, 192, 188),             # haori / belt / leg wraps
    f=(250, 132, 32),                                 # flame orange
    x=(222, 104, 92),                                 # red-tinted nichirin blade
)
sp = Sprite('rengoku', W=44, H=52, palette=PAL)


def stroke(L, core, k_core, k_out='o'):
    """line of core pixels with a 1-px 4-neighbour outline (blades, handles)."""
    cs = set(core)
    L.put(k_out, *[(x + dx, y + dy) for x, y in core for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
                   if (x + dx, y + dy) not in cs])
    L.put(k_core, *core)
    return L


def spike(L, apex, b1, b2, tip=0.5, base='y', tipk='r'):
    """flame lock: base-colour triangle with a red tip."""
    L.poly(base, [b1, apex, b2])
    ax, ay = apex
    L.poly(tipk, [apex, (ax + (b1[0] - ax) * tip, ay + (b1[1] - ay) * tip), (ax + (b2[0] - ax) * tip, ay + (b2[1] - ay) * tip)])
    return L


def flames(L, x0, x1, ybot, h, n):
    """flame hem: n crimson tongues rising from ybot, orange-yellow cores near the bottom (haori pattern)."""
    wd = (x1 - x0) / n
    pts = [(x0, ybot)]
    for i in range(n):
        pts += [(x0 + wd * i + wd * 0.1, ybot - h * 0.4), (x0 + wd * i + wd * 0.65, ybot - h)]
    pts += [(x1, ybot - h * 0.45), (x1, ybot)]
    L.poly('r', pts)
    for i in range(n):
        cx = x0 + wd * i + wd * 0.5
        L.poly('f', [(cx - wd * 0.3, ybot - 1), (cx + wd * 0.1, ybot - h * 0.55), (cx + wd * 0.3, ybot - 1)])
    return L


# ---------------- haori, back panel (hangs behind, to the left) ----------------
haori_b = sp.layer()
haori_b.poly('w', [(11, 20), (19, 20), (17, 41), (1, 43), (5, 28)])
haori_b.poly('W', [(9, 22), (11, 22), (5, 42), (2, 42), (5, 30)])
flames(haori_b, 1, 17, 43, 12, 3)

# ---------------- legs: slim, clear gap, white leg wraps, dark shoes ----------------
leg_b = sp.layer()
leg_b.poly('b', [(13, 32), (20, 32), (19, 38), (17, 42), (9, 42), (10, 37)]).v('B', 11, 36, 41).v('B', 12, 35, 41)
leg_b.rect('r', 10, 41, 16, 47).poly('y', [(10, 47), (11, 45), (12, 46), (14, 44), (15, 46), (16, 45), (16, 47)])   # flame leg wrap
leg_b.poly('w', [(9, 48), (16, 48), (17, 50), (8, 50)]).h('k', 8, 17, 50)          # white tabi + dark sandal
leg_f = sp.layer()
leg_f.poly('b', [(21, 32), (27, 32), (30, 37), (31, 42), (23, 42), (22, 37)]).v('B', 24, 38, 41).v('B', 23, 36, 41)
leg_f.rect('r', 24, 41, 30, 47).poly('y', [(24, 47), (25, 45), (26, 46), (28, 44), (29, 46), (30, 45), (30, 47)])
leg_f.poly('w', [(24, 48), (31, 48), (33, 50), (24, 50)]).h('k', 24, 33, 50)

# ---------------- torso: black uniform, white belt, waist narrower than chest ----------------
torso = sp.layer()
torso.poly('b', [(13, 21), (26, 21), (27, 25), (25, 33), (14, 33), (12, 25)])
torso.poly('B', [(13, 22), (16, 22), (16, 33), (14, 33), (13, 26)])
torso.h('w', 13, 26, 30).h('W', 13, 26, 31)
torso.px('g', (21, 24), (21, 27)).v('B', 20, 23, 29)
torso.rect('s', 17, 18, 21, 22).v('S', 17, 18, 22).h('S', 17, 21, 19)          # neck
torso.px('w', (17, 22), (18, 22), (20, 22), (21, 22))                           # white collar points

# ---------------- haori, front panel over the near shoulder ----------------
haori_f = sp.layer()
haori_f.poly('w', [(22, 20), (27, 21), (29, 26), (32, 42), (25, 42), (24, 27)])
haori_f.v('W', 25, 28, 37)
flames(haori_f, 25, 32, 42, 9, 2)

# ---------------- back arm: haori sleeve + black forearm reaching to the lower grip ----------------
arm_b = sp.layer()
arm_b.poly('b', [(13, 26), (28, 27), (28, 30), (14, 30)]).h('B', 14, 28, 30)
arm_b.ell('s', 27, 26, 31, 30).px('S', (27, 29), (28, 30))
sleeve_b = sp.layer()
sleeve_b.poly('w', [(10, 21), (15, 21), (17, 28), (11, 29), (9, 25)])
sleeve_b.v('W', 10, 23, 27).v('W', 11, 24, 28)
sleeve_b.poly('r', [(11, 29), (17, 29), (17, 26), (15, 27), (14, 24), (12, 27)]).px('f', (14, 27), (13, 28), (14, 28), (15, 28))

# ---------------- head ----------------
head = sp.layer()
# big golden mane: flame locks rising and sweeping back, red streaks/tips, long locks down past the shoulders
head.ell('y', 9, 3, 31, 19)
head.poly('y', [(9, 12), (14, 16), (13, 24), (8, 25), (5, 20)])                    # long back locks
for t1, t2, b1, b2 in (((7, 0), (9, 0), (5, 8), (15, 4)), ((16, 0), (18, 0), (13, 5), (23, 4)),
                       ((26, 0), (28, 0), (21, 4), (31, 7)), ((35, 2), (35, 4), (28, 4), (31, 11)),
                       ((2, 3), (2, 5), (10, 3), (9, 11)), ((1, 11), (1, 13), (10, 9), (10, 17)),
                       ((3, 23), (5, 24), (8, 16), (12, 22))):
    head.poly('y', [t1, t2, b2, b1])
    f = 0.42
    head.poly('r', [t1, t2, (t2[0] + (b2[0] - t2[0]) * f, t2[1] + (b2[1] - t2[1]) * f),
                    (t1[0] + (b1[0] - t1[0]) * f, t1[1] + (b1[1] - t1[1]) * f)])
head.poly('r', [(18, 3), (20, 2), (22, 7), (20, 7)])                              # red streak in the crown
head.h('Y', 5, 10, 12).h('Y', 7, 11, 16).v('Y', 12, 4, 7).v('Y', 25, 3, 6).v('Y', 10, 19, 22)
# face + fringe: bangs part in the middle, side locks frame the face
head.poly('s', [(14, 8), (29, 8), (30, 12), (29, 16), (26, 19), (17, 19), (14, 15)])
for pts in ([(13, 5), (21, 5), (16, 8)], [(20, 5), (27, 5), (24, 8)], [(25, 5), (31, 6), (29, 9)],
            [(12, 6), (15, 6), (14, 17)], [(28, 7), (31, 7), (30, 13)]):
    head.poly('y', pts)
head.v('S', 15, 10, 15)                                                           # face shade (back side)
# THICK BLACK FORKED BROWS angled up and out
head.px('k', (16, 10), (17, 10), (18, 10), (19, 10), (20, 10), (16, 9), (15, 9), (17, 9))
head.px('k', (23, 10), (24, 10), (25, 10), (26, 10), (27, 10), (26, 9), (27, 9), (28, 9), (28, 8))
# big round staring eyes: white all round, gold iris with a red centre
head.h('o', 18, 20, 11).px('e', (18, 12), (18, 13)).rect('g', 19, 12, 20, 13).px('r', (20, 13))
head.h('o', 23, 26, 11).px('e', (23, 12), (26, 12), (23, 13), (26, 13), (24, 14), (25, 14))
head.rect('g', 24, 12, 25, 13).px('r', (25, 13))
head.px('S', (28, 13), (28, 14))                                                  # nose
head.h('m', 23, 26, 16).px('m', (27, 15))                              # wide confident smile

# ---------------- sword: flame guard, blade up and forward ----------------
sword = sp.layer()
blade = []
for i in range(18):
    x, y = 35 + round(i * 5 / 17), 21 - i
    blade += [(x, y)] + ([(x + 1, y)] if i < 16 else [])
stroke(sword, blade, 'x')
sword.put('e', *[(x + 1, y) for x, y in blade[8:24:2]])                     # edge shine
stroke(sword, [(30, 28), (31, 27), (32, 26), (33, 25), (31, 28), (32, 27), (33, 26)], 'w')   # white-wrapped hilt
sword.put('W', (31, 27), (33, 25))
guard = [(x, y) for y in (21, 22, 23) for x in range(33, 38)] + [(32, 22), (38, 22), (35, 20), (35, 24)]
stroke(sword, guard, 'r')                                                         # round flame tsuba
sword.put('f', (34, 21), (36, 21), (33, 22), (37, 22), (34, 23), (36, 23), (35, 20)).put('y', (35, 22))

# ---------------- front arm: sleeve, forearm, upper grip under the guard ----------------
arm_f = sp.layer()
arm_f.poly('b', [(28, 24), (32, 24), (32, 27), (28, 27)]).h('B', 28, 31, 27)
arm_f.ell('s', 31, 23, 35, 27).px('S', (31, 27), (32, 27))
sleeve_f = sp.layer()
sleeve_f.poly('w', [(23, 20), (27, 20), (29, 22), (30, 28), (24, 28), (23, 24)])
sleeve_f.v('W', 24, 23, 27)
sleeve_f.poly('r', [(24, 28), (30, 28), (30, 24), (28, 26), (26, 23), (24, 26)]).px('f', (26, 26), (26, 27), (27, 27), (29, 27))

for L in (haori_b, leg_b, leg_f, torso, haori_f, arm_b, sleeve_b, head):
    sp.add(L)
sp.add(sword, outlined=False)
sp.add(arm_f)
sp.add(sleeve_f)
sp.save()

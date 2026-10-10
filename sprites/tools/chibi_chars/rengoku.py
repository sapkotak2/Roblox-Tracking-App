"""Kyojuro Rengoku (Demon Slayer) - chibi redraw (see tools/chibi.py for the style guide)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(34, 14, 16),                                   # outline
    y=(255, 206, 54), Y=(234, 142, 32), r=(212, 48, 30),   # hair base / shade / red tips (red also = flames, guard)
    s=(252, 212, 172), S=(222, 160, 122),             # skin
    e=(255, 252, 242), g=(250, 178, 30), k=(36, 16, 18), m=(150, 40, 32),   # eye white, gold iris, dark, mouth
    b=(60, 58, 76), B=(34, 32, 46),                   # black uniform
    w=(246, 242, 232), W=(196, 192, 188),             # haori / belt / leg wraps
    f=(250, 132, 32),                                 # flame orange
    x=(196, 206, 222),                                # blade
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
    """flame hem: n orange tongues rising from ybot, red lower core."""
    wd = (x1 - x0) / n
    pts = [(x0, ybot)]
    for i in range(n):
        pts += [(x0 + wd * i + wd * 0.15, ybot - h * 0.45), (x0 + wd * i + wd * 0.6, ybot - h)]
    pts += [(x1, ybot - h * 0.4), (x1, ybot)]
    L.poly('f', pts)
    rp = [(x0, ybot)]
    for i in range(n):
        rp += [(x0 + wd * i + wd * 0.2, ybot - h * 0.15), (x0 + wd * i + wd * 0.6, ybot - h * 0.55)]
    rp += [(x1, ybot - h * 0.2), (x1, ybot)]
    L.poly('r', rp)
    return L


# ---------------- haori, back panel (hangs behind, to the left) ----------------
haori_b = sp.layer()
haori_b.poly('w', [(11, 20), (19, 20), (17, 42), (2, 42), (6, 28)])
haori_b.poly('W', [(9, 22), (11, 22), (6, 42), (3, 42), (6, 30)])
flames(haori_b, 2, 17, 42, 9, 3)

# ---------------- legs: slim, clear gap, white leg wraps, dark shoes ----------------
leg_b = sp.layer()
leg_b.poly('b', [(14, 32), (20, 32), (18, 40), (16, 44), (10, 44), (12, 39)]).v('B', 12, 40, 44).v('B', 13, 38, 44)
leg_b.rect('w', 10, 43, 16, 47).h('W', 10, 16, 47).v('W', 11, 43, 46)
leg_b.poly('k', [(9, 48), (16, 48), (18, 50), (7, 50)]).h('B', 9, 16, 49)
leg_f = sp.layer()
leg_f.poly('b', [(21, 32), (26, 32), (29, 39), (30, 44), (24, 44), (23, 39)]).v('B', 24, 39, 44).v('B', 25, 41, 44)
leg_f.rect('w', 24, 43, 30, 47).h('W', 24, 30, 47).v('W', 25, 43, 46)
leg_f.poly('k', [(24, 48), (31, 48), (33, 50), (24, 50)]).h('B', 25, 31, 49)

# ---------------- torso: black uniform, white belt, waist narrower than chest ----------------
torso = sp.layer()
torso.poly('b', [(13, 21), (26, 21), (27, 25), (25, 33), (14, 33), (12, 25)])
torso.poly('B', [(13, 22), (16, 22), (16, 33), (14, 33), (13, 26)])
torso.h('w', 13, 26, 30).h('W', 13, 26, 31)
torso.px('g', (21, 25), (21, 28)).v('B', 20, 23, 30)
torso.rect('s', 17, 18, 21, 22).v('S', 17, 18, 22).h('S', 17, 21, 19)          # neck
torso.px('w', (17, 22), (18, 22), (20, 22), (21, 22))                           # white collar points

# ---------------- haori, front panel over the near shoulder ----------------
haori_f = sp.layer()
haori_f.poly('w', [(22, 20), (27, 21), (29, 26), (31, 42), (25, 42), (24, 27)])
haori_f.v('W', 25, 28, 37)
flames(haori_f, 25, 31, 42, 7, 2)

# ---------------- back arm: haori sleeve + black forearm reaching to the lower grip ----------------
arm_b = sp.layer()
arm_b.poly('b', [(13, 26), (28, 27), (28, 30), (14, 30)]).h('B', 14, 28, 30)
arm_b.ell('s', 27, 26, 31, 30).px('S', (27, 29), (28, 30))
sleeve_b = sp.layer()
sleeve_b.poly('w', [(10, 21), (15, 21), (17, 28), (11, 29), (9, 25)])
sleeve_b.v('W', 10, 23, 27).v('W', 11, 24, 28)
sleeve_b.poly('f', [(11, 29), (17, 29), (17, 26), (15, 27), (14, 25), (12, 27)]).h('r', 11, 17, 29)

# ---------------- head ----------------
head = sp.layer()
# one big flame-shaped mane: broad locks with blunt tips rising up and sweeping back, red tips
head.ell('y', 9, 3, 31, 19)
for t1, t2, b1, b2 in (((7, 0), (9, 0), (5, 8), (15, 4)), ((16, 0), (18, 0), (13, 5), (23, 4)),
                       ((26, 0), (28, 0), (21, 4), (31, 7)), ((35, 2), (35, 4), (28, 4), (31, 11)),
                       ((2, 3), (2, 5), (10, 3), (9, 11)), ((1, 11), (1, 13), (10, 9), (10, 17)),
                       ((3, 20), (5, 21), (9, 14), (14, 19))):
    head.poly('y', [t1, t2, b2, b1])
    f = 0.42
    head.poly('r', [t1, t2, (t2[0] + (b2[0] - t2[0]) * f, t2[1] + (b2[1] - t2[1]) * f),
                    (t1[0] + (b1[0] - t1[0]) * f, t1[1] + (b1[1] - t1[1]) * f)])
# back of the mane in shade + two strand lines
head.h('Y', 5, 10, 12).h('Y', 7, 11, 16).v('Y', 12, 4, 7).v('Y', 21, 4, 6).v('Y', 27, 4, 6)
# face
head.poly('s', [(14, 8), (29, 8), (30, 12), (29, 16), (26, 19), (17, 19), (14, 15)])
# fringe flames on the forehead + side lock
for pts in ([(13, 6), (20, 6), (16, 9)], [(19, 6), (25, 6), (22, 9)], [(24, 6), (31, 7), (28, 9)],
            [(12, 7), (15, 7), (14, 16)]):
    head.poly('y', pts)
head.h('S', 15, 29, 10).v('S', 15, 11, 15)                                       # face shade under the fringe
# thick brows, wide bright eyes (far eye left, near eye right)
head.h('k', 17, 20, 10).h('k', 23, 27, 10)                                        # thick brows
head.h('o', 18, 20, 11).px('e', (18, 12), (18, 13)).rect('g', 19, 12, 20, 13).px('r', (20, 13))
head.h('o', 23, 27, 11).px('e', (23, 12), (24, 12), (27, 12), (23, 13), (24, 13), (27, 13))
head.rect('g', 25, 12, 26, 13).px('r', (26, 13))
head.px('S', (28, 13), (28, 14))                                                  # nose
head.h('m', 23, 26, 16).px('e', (24, 16), (25, 16))                              # big grin

# ---------------- sword: flame guard, blade up and forward ----------------
sword = sp.layer()
blade = []
for i in range(18):
    x, y = 35 + round(i * 5 / 17), 21 - i
    blade += [(x, y)] + ([(x + 1, y)] if i < 16 else [])
stroke(sword, blade, 'x')
sword.put('e', *[(x + 1, y) for x, y in blade[8:24:2]])                     # edge shine
stroke(sword, [(30, 28), (31, 27), (32, 26), (33, 25), (31, 28), (32, 27), (33, 26)], 'm')   # handle
guard = [(x, y) for y in (22, 23) for x in range(32, 39)] + [(33, 21), (35, 20), (37, 21), (34, 24), (36, 24)]
stroke(sword, guard, 'r')
sword.put('f', (33, 21), (35, 20), (37, 21), (34, 22), (35, 22), (36, 22))

# ---------------- front arm: sleeve, forearm, upper grip under the guard ----------------
arm_f = sp.layer()
arm_f.poly('b', [(28, 24), (32, 24), (32, 27), (28, 27)]).h('B', 28, 31, 27)
arm_f.ell('s', 31, 23, 35, 27).px('S', (31, 27), (32, 27))
sleeve_f = sp.layer()
sleeve_f.poly('w', [(23, 20), (27, 20), (29, 22), (30, 28), (24, 28), (23, 24)])
sleeve_f.v('W', 24, 23, 27)
sleeve_f.poly('f', [(24, 28), (30, 28), (30, 24), (28, 26), (26, 24), (24, 26)]).h('r', 24, 30, 28)

for L in (haori_b, leg_b, leg_f, torso, haori_f, arm_b, sleeve_b, head):
    sp.add(L)
sp.add(sword, outlined=False)
sp.add(arm_f)
sp.add(sleeve_f)
sp.save()

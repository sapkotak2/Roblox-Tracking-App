"""Escanor 'The One' (Seven Deadly Sins) - chibi redraw (see tools/chibi.py for the style guide).
Matched to refs/redraw/escanor (04 Season 3 design + face crop), checklist in refs/redraw/escanor/NOTES.md."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(48, 24, 16),                                   # outline
    h=(218, 122, 52), H=(152, 76, 32),                # ginger hair + handlebar mustache
    s=(246, 198, 150), S=(210, 144, 100),             # skin
    e=(255, 252, 244), b=(70, 132, 206), k=(40, 22, 16), m=(156, 62, 50),   # eye white, BLUE iris/grip, dark, mouth
    g=(90, 112, 60), G=(60, 78, 42),                  # olive-green trousers
    n=(134, 84, 44), N=(94, 58, 30),                  # brown belt / boots
    y=(242, 188, 62), Y=(188, 122, 34), x=(228, 232, 238),   # Rhitta: gold / gold shade / silver edge
)
sp = Sprite('escanor', W=48, H=52, palette=PAL)


def ringed(L, pts, k, k_out='o', k_low=None, open_top=()):
    """paint a pixel set with a 1-px 4-neighbour outline (for small shapes that must keep their colour);
    columns in open_top get no outline above them"""
    ps = set(pts)
    L.put(k_out, *[(x + dx, y + dy) for x, y in ps for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
                   if (x + dx, y + dy) not in ps and not (dy == -1 and x in open_top)])
    L.put(k, *ps)
    if k_low: L.put(k_low, *[(x, y) for x, y in ps if (x, y + 1) not in ps])
    return L


# ---------------- legs: olive trousers, brown boots ----------------
leg_b = sp.layer()
leg_b.poly('g', [(12, 33), (21, 33), (19, 40), (17, 46), (10, 46), (11, 40)]).v('G', 11, 38, 45).v('G', 12, 37, 45)
leg_b.poly('n', [(9, 45), (17, 45), (18, 48), (19, 50), (6, 50), (8, 47)]).h('N', 6, 19, 50).v('N', 9, 46, 49)
leg_f = sp.layer()
leg_f.poly('g', [(23, 33), (31, 33), (33, 40), (33, 46), (25, 46), (24, 40)]).v('G', 25, 40, 45).v('G', 26, 42, 45)
leg_f.poly('n', [(25, 45), (33, 45), (34, 48), (37, 49), (37, 50), (25, 50)]).h('N', 25, 37, 50).v('N', 26, 46, 49)

# ---------------- torso: giant V, shirtless, 6-pack ----------------
torso = sp.layer()
torso.poly('s', [(7, 19), (33, 19), (38, 23), (36, 28), (31, 34), (13, 34), (8, 28), (5, 23)])
torso.poly('S', [(6, 22), (9, 21), (11, 28), (13, 34), (12, 34), (8, 28)])         # back side in shade
torso.h('S', 12, 19, 26).h('S', 23, 32, 26).px('S', (20, 25), (22, 25), (33, 25))  # pec lines
torso.v('S', 21, 22, 33)                                                          # centre line
torso.h('S', 16, 19, 29).h('S', 23, 27, 29).h('S', 16, 19, 31).h('S', 23, 27, 31)  # abs
torso.v('S', 12, 20, 24)                                                          # deltoid line
torso.rect('n', 11, 32, 32, 34).h('N', 11, 32, 34).rect('y', 21, 32, 22, 33)      # belt + gold buckle
torso.rect('s', 19, 15, 27, 20).v('S', 19, 15, 20).h('S', 19, 26, 17)             # thick neck

# ---------------- Rhitta's handle: from the raised hand, behind the neck, over the near shoulder ----------------
handle = sp.layer().poly('y', [(4, 8), (41, 18), (41, 23), (4, 12)])
handle.poly('b', [(4, 8), (13, 10), (13, 15), (4, 12)])                            # blue grip
handle.ell('y', 0, 6, 5, 12).px('Y', (2, 9), (2, 10))                             # gold ring end
handle.line('Y', [(14, 14), (40, 21)])                                            # shade under the shaft

# ---------------- head ----------------
head = sp.layer()
head.ell('h', 14, 0, 32, 13).rect('h', 14, 6, 19, 14)                            # neat rounded cap + nape
head.poly('s', [(19, 6), (31, 5), (33, 9), (33, 14), (30, 18), (22, 18), (19, 14)])   # face, square jaw
head.poly('h', [(17, 3), (29, 1), (33, 4), (34, 9), (31, 6), (24, 7), (19, 9)])    # side-parted fringe swept forward
head.h('H', 21, 28, 4).v('H', 16, 5, 12).px('H', (32, 7), (33, 8))               # strands / back shade
head.rect('s', 19, 10, 20, 12).px('S', (19, 11), (19, 12))                        # ear
head.v('S', 21, 13, 16).h('S', 22, 24, 17)                                        # jaw shade (back side)
# calm, slightly droopy blue eyes under thin raised brows
head.h('H', 22, 24, 8).h('H', 27, 30, 8).px('H', (30, 7))
head.h('o', 22, 24, 9).px('e', (22, 10)).px('b', (23, 10), (24, 10))
head.h('o', 27, 30, 9).px('e', (27, 10), (30, 10)).px('b', (28, 10), (29, 10))
head.px('S', (31, 11), (32, 11), (32, 12))                                        # long nose
head.h('m', 27, 30, 16).px('m', (31, 15))                                         # confident smile
must = sp.layer()   # big ginger handlebar mustache, ends curling up past the cheeks
ringed(must, [(x, 13) for x in range(24, 34)] + [(x, 14) for x in range(22, 27)] + [(x, 14) for x in range(30, 36)]
       + [(21, 13), (21, 12), (36, 13), (36, 12)], 'h', open_top=range(25, 33))
must.px('H', (27, 13), (28, 13), (29, 13))                                         # centre parting under the nose

# ---------------- back arm: raised, gripping the handle beside the head ----------------
arm_b = sp.layer()
arm_b.poly('s', [(5, 19), (12, 19), (12, 25), (4, 26), (1, 22)]).h('S', 3, 11, 25).v('S', 2, 22, 24)
fore_b = sp.layer().poly('s', [(1, 23), (6, 25), (9, 13), (3, 12)]).v('S', 2, 14, 22).v('S', 3, 15, 21)
hand_b = sp.layer().ell('s', 3, 7, 10, 14).h('S', 4, 9, 13).px('S', (3, 11), (3, 12))

# ---------------- front arm: hand on the hip ----------------
arm_f = sp.layer()
arm_f.poly('s', [(31, 20), (37, 20), (43, 27), (40, 31), (34, 26)]).h('S', 35, 40, 27).v('S', 34, 22, 25)
fore_f = sp.layer().poly('s', [(39, 31), (43, 27), (37, 33), (32, 34), (31, 31)]).h('S', 33, 38, 33)

# ---------------- Rhitta's head: gold crescent blade with a silver edge, disc ornament, spear point ----------------
axe = sp.layer()
axe.poly('y', [(33, 1), (34, 9), (37, 13), (41, 15), (45, 13), (47, 9), (47, 0), (45, 5), (42, 8), (39, 8), (36, 5)])
axe.poly('x', [(34, 2), (36, 6), (39, 9), (42, 9), (45, 6), (47, 1), (47, 4), (45, 8), (42, 11), (39, 11), (36, 8), (34, 5)])   # silver edge band
axe.rect('y', 39, 13, 42, 21).v('Y', 39, 14, 21)                                  # stem down to the handle
axe.poly('y', [(42, 18), (47, 21), (47, 24), (42, 21)]).px('Y', (44, 21))         # spear point
axe.rect('Y', 39, 16, 42, 17)                                                     # collar ring

for L in (leg_b, leg_f, torso, handle, head):
    sp.add(L)
sp.add(must, outlined=False)
for L in (arm_b, fore_b, hand_b, arm_f, fore_f, axe):
    sp.add(L)
sp.save()

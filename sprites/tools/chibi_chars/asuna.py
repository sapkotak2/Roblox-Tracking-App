"""Asuna (Sword Art Online) - chibi redraw (see tools/chibi.py for the style guide).
Matched to refs/redraw/asuna (SAO avatar full body + face), checklist in refs/redraw/asuna/NOTES.md:
big round amber eyes, thin light brows, soft smile, rounder face; very long light chestnut hair with a side-swept
fringe, long side locks and a side braid; KoB uniform: sleeveless white top with red-trimmed high collar, grey chest
plate, red trim lines, detached white sleeves with red/gold bands, red pleated skirt with a white crossed tabard,
long white coat tails behind, white thigh-highs with a red cross; slim fencer stance with the rapier thrust forward."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(56, 26, 24),                                    # outline
    h=(228, 150, 92), H=(170, 92, 52),                 # light chestnut hair / shade (also the thin brows)
    s=(255, 222, 198), S=(236, 168, 140),              # skin
    e=(255, 255, 255), k=(70, 32, 26), z=(196, 112, 44), m=(220, 110, 110),  # eye white, lash, amber iris, smile
    w=(246, 246, 250), W=(178, 180, 202),              # white uniform / cool grey (shade + chest plate)
    r=(214, 36, 46), R=(140, 18, 30),                  # red trim / skirt
    g=(236, 184, 60),                                  # gold band on the sleeves
)
sp = Sprite('asuna', W=50, H=52, palette=PAL)
L = sp.layer

# ---------------- very long hair down the back (to the thighs) ----------------
back_hair = L()
back_hair.poly('h', [(13, 5), (18, 12), (18, 30), (16, 40), (12, 43), (9, 41), (8, 32), (8, 16), (10, 9)])
back_hair.poly('H', [(8, 18), (10, 18), (10, 41), (9, 41), (8, 32)])
back_hair.v('H', 14, 26, 41)
back_hair.poly('h', [(27, 10), (33, 9), (34, 20), (32, 27), (29, 27), (29, 20)]).v('H', 31, 20, 26)   # long lock on the near side

# ---------------- long white coat tails behind the legs (red trim) ----------------
tails = L()
tails.poly('w', [(13, 30), (19, 30), (18, 45), (10, 45)]).v('W', 12, 33, 44).v('W', 13, 31, 44).h('r', 11, 18, 44)

# ---------------- back arm: bare shoulder, detached sleeve, hand on the hip ----------------
back_arm = L()
back_arm.rect('s', 13, 21, 17, 24).v('S', 13, 22, 24)
back_arm.rect('w', 12, 24, 16, 32).v('W', 12, 24, 32).v('W', 13, 24, 32)
back_arm.rect('s', 12, 32, 16, 35).h('S', 12, 16, 34)

# ---------------- legs: white thigh-highs with a red cross, white boots, fencer stance ----------------
leg_b = L()
leg_b.poly('s', [(16, 36), (21, 36), (20, 39), (16, 39)])
leg_b.poly('w', [(15, 39), (21, 39), (19, 47), (15, 47)]).h('r', 15, 21, 39)
leg_b.poly('w', [(11, 47), (19, 47), (19, 50), (11, 50)])
leg_b.v('W', 16, 40, 47).v('W', 17, 40, 47).h('W', 12, 18, 50)
leg_f = L()
leg_f.poly('s', [(23, 36), (28, 36), (29, 39), (24, 39)])
leg_f.poly('w', [(24, 39), (30, 39), (31, 47), (26, 47)]).h('r', 24, 30, 39)
leg_f.v('r', 28, 41, 44).h('r', 27, 29, 42)                                          # red cross on the thigh-high
leg_f.poly('w', [(26, 47), (34, 47), (35, 50), (26, 50)])
leg_f.poly('W', [(24, 40), (25, 40), (27, 47), (26, 47)]).h('W', 27, 34, 50)

# ---------------- red pleated skirt with the white crossed tabard ----------------
skirt = L()
skirt.poly('r', [(18, 29), (28, 29), (31, 37), (14, 37)])
skirt.poly('R', [(18, 29), (20, 29), (18, 37), (14, 37)])
skirt.v('R', 21, 33, 37).v('R', 29, 33, 37)
tabard = L().poly('w', [(22, 29), (27, 29), (27, 36), (24, 38), (22, 36)]).v('r', 24, 31, 35).h('r', 23, 25, 32)

# ---------------- torso: slim, bare shoulders, white top, red-trimmed high collar, grey chest plate ----------------
torso = L()
torso.rect('s', 20, 17, 24, 21).v('S', 20, 17, 21)                                    # neck
torso.poly('w', [(18, 21), (27, 21), (28, 24), (27, 29), (19, 29), (18, 24)])
torso.v('W', 18, 21, 29).v('W', 19, 22, 29)
torso.v('r', 21, 25, 28).v('r', 26, 25, 28)                                          # red trim lines down the front
torso.h('W', 19, 27, 29)                                                             # white belt (grey shade line)
torso.rect('w', 20, 18, 24, 21).h('r', 20, 24, 18).px('r', (22, 20))                 # high collar, red trim + clasp
torso.h('W', 20, 27, 23).h('W', 20, 27, 24)                                         # grey chest plate

# ---------------- head ----------------
head = L()
head.ell('h', 10, 0, 33, 18)
head.poly('s', [(16, 7), (30, 7), (31, 11), (31, 14), (29, 17), (26, 19), (21, 19), (18, 17), (16, 13)])  # rounder face
# side-swept fringe parted on the far side, sweeping toward the front; long side locks
head.poly('h', [(13, 2), (20, 2), (19, 7), (17, 9)])
head.poly('h', [(18, 2), (31, 3), (30, 6), (25, 7), (21, 8)])
head.poly('h', [(28, 3), (33, 6), (33, 12), (32, 16), (30, 9)])
head.poly('h', [(11, 6), (18, 8), (18, 24), (17, 30), (15, 30), (13, 22), (12, 15)])   # long lock in front of the far shoulder
head.v('H', 16, 11, 28).px('H', (20, 4), (21, 5), (22, 6), (27, 4), (28, 5))
# braid running from the temple back along the side of the head
head.px('h', (20, 7)).h('H', 11, 18, 6).h('H', 11, 18, 8).px('H', (12, 7), (14, 7), (16, 7), (18, 7))   # side braid: rope band above the ear
# thin light brows, big round amber eyes (3 rows), soft smile
head.h('H', 19, 21, 8).h('H', 25, 27, 8)
head.h('k', 19, 22, 10).px('e', (20, 11), (20, 12), (20, 13)).px('z', (21, 11), (21, 12), (21, 13))
head.h('k', 24, 28, 10)
head.px('e', (24, 11), (24, 12), (24, 13), (27, 11), (27, 12), (27, 13))
head.px('k', (25, 11), (26, 11)).px('z', (25, 12), (26, 12), (25, 13), (26, 13))
head.px('S', (30, 14))
head.px('m', (25, 16), (26, 16))
head.px('S', (21, 17), (22, 18))

# ---------------- rapier thrust forward at chest height ----------------
rapier = L().poly('W', [(37, 24), (48, 24), (49, 25), (48, 26), (37, 26)]).h('e', 38, 47, 25)

# ---------------- front arm: bare shoulder, detached sleeve with red/gold band, straight out ----------------
front = L()
front.poly('s', [(25, 21), (28, 21), (29, 28), (25, 27)]).v('S', 25, 22, 26)
front.poly('w', [(28, 23), (34, 23), (34, 28), (28, 28)]).h('W', 28, 34, 27).h('W', 28, 34, 28)
front.v('r', 28, 23, 28).v('g', 29, 23, 28)
fist = L().rect('s', 34, 23, 38, 28).h('S', 34, 38, 27).h('S', 34, 38, 28)
guard = L().rect('W', 37, 22, 39, 29).v('e', 38, 23, 28)

for lay in (back_hair, tails, back_arm, leg_b, leg_f, skirt, tabard, torso, head, rapier, front, fist, guard):
    sp.add(lay)
sp.save()

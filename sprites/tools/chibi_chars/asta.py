"""Asta (Black Clover) - chibi redraw (see tools/chibi.py for the style guide).
Matched to refs/redraw/asta (01 anime profile, face crop, Demon-Slayer sword), checklist in refs/redraw/asta/NOTES.md."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from chibi import Sprite

PAL = dict(
    o=(24, 20, 26),                                   # outline (also brows, pupils)
    a=(218, 218, 210), A=(146, 148, 148),             # ash-silver hair / grey shade (A also = sword edge, shirt shade)
    s=(248, 206, 166), S=(214, 150, 112),             # skin
    e=(255, 255, 250), g=(120, 156, 70), m=(132, 50, 44),   # eye white, olive-green iris, mouth
    b=(48, 46, 56), B=(28, 26, 34),                   # black robe / headband / boots / sword
    n=(54, 76, 126), N=(34, 50, 88),                  # navy jacket sleeves + cropped trousers
    w=(242, 240, 232),                                # white shirt, boot toe caps
    r=(156, 100, 54), R=(106, 66, 34),                # brown belt + pouch
    y=(238, 192, 62),                                 # gold Black Bulls emblem / buckle
)
sp = Sprite('asta', W=48, H=52, palette=PAL)

# ---------------- back arm: navy sleeve + fist, below the cape on the far side ----------------
arm_b = sp.layer()
arm_b.poly('n', [(11, 24), (15, 24), (14, 31), (10, 31)]).v('N', 11, 25, 30)
arm_b.ell('s', 8, 29, 13, 34).px('S', (9, 33), (10, 33), (8, 31))

# ---------------- legs: navy cropped trousers, black boots with white toe caps ----------------
leg_b = sp.layer()   # back leg angled back
leg_b.poly('n', [(13, 32), (20, 32), (17, 39), (14, 44), (8, 44), (11, 38)])
leg_b.poly('N', [(9, 43), (12, 37), (14, 34), (14, 37), (12, 43)])
leg_b.px('s', (9, 44), (10, 44), (11, 44), (12, 44)).put('s', (13, 44))           # bit of calf under the slit hem
leg_b.poly('b', [(8, 44), (13, 44), (13, 47), (15, 50), (4, 50), (6, 47)]).v('B', 9, 45, 48)
leg_b.poly('w', [(4, 48), (7, 48), (7, 50), (4, 50)])
leg_f = sp.layer()   # front leg bent forward
leg_f.poly('n', [(21, 32), (27, 32), (31, 37), (31, 44), (25, 44), (24, 38)]).v('N', 25, 38, 43).v('N', 26, 40, 43)
leg_f.poly('b', [(25, 44), (31, 44), (32, 47), (35, 48), (35, 50), (25, 50)]).v('B', 26, 45, 48)
leg_f.poly('w', [(32, 47), (35, 48), (35, 50), (32, 50)])

# ---------------- torso: white shirt at the belly, brown belt + pouch ----------------
torso = sp.layer()
torso.poly('w', [(13, 22), (27, 22), (27, 26), (25, 33), (15, 33), (13, 26)])     # white tunic
torso.poly('A', [(13, 24), (16, 24), (17, 33), (15, 33), (13, 27)])               # back side in shade
torso.h('R', 14, 26, 30).h('r', 14, 26, 31).rect('y', 20, 30, 21, 31)            # belt + gold buckle
torso.rect('r', 23, 31, 26, 35).h('R', 23, 26, 35).px('y', (24, 32))              # pouch on the hip
torso.rect('s', 17, 17, 21, 21).h('S', 17, 21, 18).v('S', 17, 17, 21)             # neck

# ---------------- front arm: navy sleeve, fist on the hilt ----------------
arm_f = sp.layer()
arm_f.poly('n', [(26, 24), (30, 24), (33, 28), (30, 31), (27, 28)]).v('N', 27, 25, 27).px('N', (28, 28), (29, 29))

# ---------------- Black Bulls robe: short black hooded cape over both shoulders, gold bull emblem ----------------
cape = sp.layer()
cape.poly('b', [(12, 19), (27, 19), (31, 23), (30, 26), (24, 25), (17, 25), (9, 27), (9, 23)])
cape.poly('B', [(10, 22), (13, 21), (14, 25), (9, 27)])                            # far side in shade
cape.poly('b', [(10, 17), (16, 17), (16, 21), (11, 22)]).h('B', 11, 15, 21)        # hood bunched behind the neck
cape.v('B', 21, 21, 24)                                                           # front opening
cape.rect('y', 24, 22, 26, 24).px('b', (25, 23))                                 # gold bull emblem
cape.rect('y', 20, 20, 21, 20)                                                    # clasp at the throat

# ---------------- the ahoge: one long strand curling up out of the top of the hair ----------------
ahoge = sp.layer()
core = [(19, 6), (19, 5), (19, 4), (20, 3), (20, 2), (21, 1), (22, 1), (23, 1), (24, 2)]
ahoge.put('o', *[(x + dx, y + dy) for x, y in core for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)) if (x + dx, y + dy) not in core])
ahoge.put('a', *core)

# ---------------- head ----------------
head = sp.layer()
head.ell('a', 9, 4, 30, 19)
# messy spikes fanning up and out (blunt tips keep their colour)
for t1, t2, b1, b2 in (((5, 3), (7, 2), (10, 9), (15, 5)), ((12, 1), (14, 1), (13, 6), (19, 5)),
                       ((25, 1), (27, 2), (22, 5), (29, 6)), ((32, 4), (33, 5), (27, 6), (30, 10)),
                       ((2, 9), (2, 11), (11, 7), (10, 13)), ((3, 16), (4, 18), (10, 13), (12, 18)),
                       ((33, 10), (33, 12), (29, 9), (30, 14))):
    head.poly('a', [t1, t2, b2, b1])
head.poly('s', [(14, 10), (29, 10), (30, 13), (29, 16), (26, 19), (17, 19), (14, 16)])   # face
head.poly('a', [(12, 9), (15, 9), (15, 17), (12, 15)])                            # side lock
head.poly('a', [(26, 9), (30, 9), (30, 12)])                                       # front lock over the temple
# black headband across the forehead, gold Black Bulls emblem on the side
head.poly('b', [(9, 8), (31, 7), (31, 9), (9, 10)]).rect('y', 12, 8, 13, 9)
head.h('A', 11, 15, 6).h('A', 24, 28, 5).h('A', 4, 10, 11).h('A', 6, 11, 15)
head.v('S', 15, 10, 16)                                                           # face shade under the hair
# big olive-green eyes, thin brows angled down to the nose, confident smirk
head.px('o', (16, 11), (17, 11), (18, 11)).px('o', (25, 11), (26, 11), (27, 11), (28, 11))
head.h('o', 18, 20, 12).px('e', (18, 13), (18, 14)).rect('g', 19, 13, 20, 14).px('o', (20, 13))
head.h('o', 23, 27, 12).px('e', (23, 13), (26, 13), (23, 14), (26, 14)).rect('g', 24, 13, 25, 14).px('o', (25, 13))
head.px('S', (28, 15))                                                            # nose
head.h('m', 22, 24, 17)                                                           # small confident smirk

# ---------------- Demon-Slayer Sword: huge broad black blade, long crossguard, held low and forward ----------------
sword = sp.layer()
sword.poly('b', [(32, 34), (36, 30), (46, 40), (46, 43), (42, 47), (39, 46)])     # blade with a slanted tip
sword.line('A', [(37, 31), (45, 39)])                                             # worn light edge
sword.poly('B', [(36, 37), (38, 35), (40, 38), (38, 40)]).px('B', (42, 42), (43, 42), (41, 44))   # chipped patches
guard = sp.layer().line('A', [(29, 37), (39, 27)], width=3)                       # long thin crossguard
hilt = sp.layer().line('R', [(29, 28), (33, 32)], width=3)                       # handle
fist = sp.layer().ell('s', 29, 27, 34, 32).px('S', (30, 31), (31, 32), (29, 30)).px('S', (32, 32))

for L in (arm_b, leg_b, leg_f, torso, cape):
    sp.add(L)
sp.add(ahoge, outlined=False)
for L in (head, hilt, sword, guard, arm_f, fist):
    sp.add(L)
sp.save()

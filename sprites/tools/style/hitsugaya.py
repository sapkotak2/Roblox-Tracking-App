"""Toshiro Hitsugaya (Bleach) built by sprite edits on the clean TANJIRO template (out/style/tanjiro_clean.png).

Why Tanjiro and not Ichigo: Ichigo only exists in the sheet's 2x roster row (1.7 sheet px per sprite pixel),
too small to recover cleanly; Tanjiro already has the sword pose, robes over hakama and the head geometry.

Kept from Tanjiro: head mass and face block (eye boxes, lash row, nose, mouth, jaw, ear), hands, katana line,
torso outline, the baggy hakama (recoloured black: a shinigami hakama), stance, feet and the outline colour.
Changed:
  hair    WHITE spiky hair: Tanjiro's hair mass plus big swept spikes up and to the back (SPIKES), a front
          side lock, forehead locks with one lock falling between the eyes; auto-outlined, base/shade/deep
          shade with strand lines along each spike
  face    teal-green eyes built like Tanjiro's (lash, white, 2x3 iris + highlight), short flat brows pulled
          down, flat mouth. Three options in FACES (see out/style/hitsugaya_faces.png)
  outfit  black shihakusho with white under-collar, sleeveless white captain's haori (back panel to the
          calves, front edge), green sash diagonally across the chest with a round clasp, holding the
          scabbard on his back; white obi; white tabi and straw sandals
  sword   Hyorinmaru drawn in Tanjiro's pose: teal-tinted blade, four-point star tsuba, blue-grey hilt;
          the empty scabbard rides diagonally on his back on the sash

usage: python3 tools/style/hitsugaya.py
  -> out/style/hitsugaya.png, out/style/hitsugaya_check.png (Tanjiro | Hitsugaya, 10x),
     out/style/hitsugaya_faces.png (3 face options, 12x)
"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(__file__))
import spriteedit as se
from PIL import Image, ImageDraw, ImageFont

T = 'out/style/tanjiro_clean.png'
OUT = 'out/style/hitsugaya.png'
OX, OY = 8, 8       # padding left (back spikes, sheath) and top (tall hair)
CHOSEN = 'cool-serious'
# hair tracing (tools/style/trace_hair.py): landmarks in ref 00 (3/4 view, already facing right) and in the
# sprite's face block (template coords; eye centres, chin bottom)
REF = 'refs/redraw/hitsugaya/00_Ep363HitsugayaProfile.png'
REF_MIRROR = True     # his hair sweeps to his left in ref 00; mirrored it sweeps UP and BACK on our sprite
REF_HEAD_BOX = (57, 0, 532, 455)   # (in mirrored coords)
REF_EYES, REF_CHIN = ((233, 336), (343, 336)), (281, 492)   # mirrored coords
SPR_EYES, SPR_CHIN = ((9.5, 16.5), (17.5, 16.5)), (16.5, 24.0)   # x shifted 4 px back: 3/4 head
SPR_BOX = (-8, -12, 30, 24)
TRACE_THRESH = 0.3
# hand clean-up of the traced silhouette: a few large dominant spikes rising and curving up and BACK,
# long side locks over the ear down to the jaw, and the front kept tight to the face (3/4 view)
BIG_SPIKES = [((1, 3), (8, 0), (-5, -7)),       # back spike, curving up and back
              ((7, 0), (13, -3), (3, -8)),      # tallest, up and back
              ((12, -2), (17, -2), (12, -8)),   # crown
              ((17, -1), (22, 1), (19, -6)),    # front of the crown, up
              ((0, 7), (2, 13), (-6, 6)),       # back, flaring out at temple level
              ((2, 11), (5, 15), (-3, 15))]     # lower back lock, pointing down and back
SIDE_LOCKS = [((4, 13), (9, 13), (6, 22)),      # back side lock over the ear, pointed at the jaw
              ((7, 14), (11, 14), (10, 21))]


def HAIR_ADD_MASK(tx, ty):
    m = np.zeros(tx.shape, bool)
    for a, b, c in BIG_SPIKES + SIDE_LOCKS:
        tri(m, a, b, c, OX, OY)
    m |= (tx == 24) & (ty >= 8) & (ty <= 17)                    # front lock framing the face
    return m


def HAIR_CUT_MASK(tx, ty):
    return ((tx >= 26) & (ty >= 6)) | ((tx >= 27) & (ty >= 3))  # nothing in front of the face


STRANDS = [((10, 4), (3, -7), 'U'), ((14, 3), (12, -7), 'U'), ((19, 3), (19, -5), 'U'), ((6, 7), (-4, 6), 'U'),
           ((12, 7), (9, 2), 'S')]                              # (from, to, colour key) along the big spikes
POSE = 'composed'    # 'composed' (v3: arms crossed, sword sheathed on the back) or 'tanjiro' (v2)

K = {
    '#': (26, 21, 33),
    # white hair
    'W': (246, 246, 252), 'S': (208, 208, 230), 'U': (168, 168, 204), 'V': (128, 128, 170),   # Killua/Gojo-style
    # skin
    'c': (248, 212, 173), 'l': (226, 175, 140), 'u': (183, 124, 102),
    # eyes
    'w': (244, 240, 240), 's': (206, 200, 206),
    'P': (16, 70, 74), 'I': (34, 160, 150), 'J': (110, 214, 196), 'x': (250, 255, 255),
    'b': (98, 104, 140),                                  # brow (silver-grey, reads as white brows)
    'o': (196, 128, 118), 'O': (142, 80, 84),
    # black shihakusho
    'K': (46, 46, 60), 'L': (72, 74, 94), 'Z': (32, 31, 44),
    # white haori / obi / tabi
    'H': (240, 242, 248), 'h': (198, 206, 224), 'j': (146, 156, 184),
    # green sash + clasp
    'G': (70, 150, 112), 'g': (44, 104, 80), 'q': (110, 186, 144), 'C': (30, 40, 40),
    # sword: teal blade, star tsuba, hilt
    'B': (150, 206, 214), 'X': (226, 250, 252), 'A': (84, 140, 160),
    'Y': (214, 176, 84), 'y': (140, 108, 52), 'n': (70, 86, 130),
    # scabbard
    'N': (40, 44, 70), 'M': (70, 78, 116),
    # sandals
    'R': (170, 130, 84), 'r': (120, 88, 56),
}
SKIN = [(248, 212, 173), (246, 210, 182), (226, 175, 140), (183, 124, 102)]

# big swept spikes: (base point a, base point b, tip) in template coordinates (y may be negative)
# Hair v4: many THIN flame-like spikes. Each spike = (root x, root y, angle in degrees (0 = right,
# -90 = up), length, base width); the tip is 1 px. The mass sweeps up and slightly back like a flame, side
# spikes flare out almost horizontally at temple/ear level, short tufts at the nape and behind the ear.
import math
FLAMES = [
    # crown: tall tapered flames, up and leaning back toward the back of the head; wide roots, 1-px tips,
    # so the notches between them stay open V shapes instead of black channels
    (4, 4, -145, 8, 5), (8, 2, -125, 10, 5), (12, 1, -112, 10, 5), (16, 1, -102, 10, 5), (20, 3, -94, 8, 4),
    (23, 6, -78, 5, 3),
    # back, rising
    (1, 9, -164, 7, 5),
    # side flares (wings): back side at ear level, front side at the temple
    (1, 15, 172, 5, 4), (2, 19, 150, 4, 3), (25, 9, -10, 3, 3),
    # nape tuft
    (5, 21, 115, 3, 3),
]


def _flame(x, y, ang, ln, wd):
    d = (math.cos(math.radians(ang)), math.sin(math.radians(ang))); n = (-d[1], d[0])
    a = (round(x + n[0] * wd / 2), round(y + n[1] * wd / 2)); b = (round(x - n[0] * wd / 2), round(y - n[1] * wd / 2))
    return a, b, (round(x + d[0] * ln), round(y + d[1] * ln))


SPIKES = [_flame(*f) for f in FLAMES]
CLUMPS = [((13, 7), (10, 3)), ((17, 7), (17, 3)), ((9, 9), (5, 6)), ((6, 12), (2, 11)), ((21, 7), (21, 5))]

# face skin rows: everything else in the head is hair. The signature lock falls from the parting over the
# brow on the inner side of the near (front) eye, x 18-19, down to cheek level (tip at row 20, x 19); two
# shorter jagged fringe points at x 11-12 and x 22-23; front lock framing the face at x 24.
_LOCK = {9: (17, 19), 10: (17, 19), 11: (17, 19), 12: (17, 19), 13: (18, 19), 14: (18, 20), 15: (19, 20),
         16: (19, 20), 17: (20, 20), 18: (20, 20)}          # curves toward the near eye, tip at (20, 19)
_FRINGE = {11: [(11, 12), (22, 23)], 12: [(11, 11), (23, 23)]}
FACE = {}
for _y in range(11, 22):
    _keep = set(range(11 if _y > 11 else 12, (23 if _y < 21 else 22) + 1))
    if _y in _LOCK:
        _keep -= set(range(_LOCK[_y][0], _LOCK[_y][1] + 1))
    for _a, _b in _FRINGE.get(_y, []):
        _keep -= set(range(_a, _b + 1))
    _r, _run = [], None
    for _x in sorted(_keep):
        if _run and _x == _run[1] + 1:
            _run[1] = _x
        else:
            if _run: _r.append(tuple(_run))
            _run = [_x, _x]
    _r.append(tuple(_run)); FACE[_y] = _r
EAR = {18: [(7, 9)], 19: [(6, 9)], 20: [(6, 9)], 21: [(7, 9)]}

# face options: (x, y, rows) in template coords; '?' keeps. Eyes built like Tanjiro's: brow row 14,
# lash row 15, eye rows 16-18 (2-px white + 2x3 teal iris), mouth row 21.
FACES = {
    'cool-serious': [   # big turquoise eyes, sharp lids slanting down to the nose, thick brows scowling inward
        (11, 12, ['?bb???', '??bbbb', '?####?', '?wPP#?', '?wIx??', '?wJJ??']),
        (19, 12, ['???bb?', '?bbb??', '?####?', '?#PPw?', '?wIxw?', '?wJJw?']),
        (17, 21, ['?oO']),
    ],
    'irritated': [      # brows in a firm V, lid lowered over the iris, short hard mouth
        (11, 13, ['?bb???', '???bb?', '?####?', '?ssPP?', '?wwIx?', '??wJJ?']),
        (19, 13, ['???bb?', '?bb???', '?####?', '?ssPP?', '?wwIx?', '?wwJJ?']),
        (17, 21, ['OOO']),
    ],
    'cold-stare': [     # straight heavy lids, small iris with white around it, flat brows, tiny mouth
        (11, 13, ['??????', '?bbbb?', '?####?', '?wsPw?', '?wwIw?', '??wJ??']),
        (19, 13, ['??????', '?bbbb?', '?####?', '?sPws?', '?wIww?', '?wJw??']),
        (18, 21, ['O']),
    ],
}


BODY = [  # x 0-29, rows 22-50 in template coords ('?' keeps the template: chin, hands, hilt, blade, hakama)
    '......#HHh' + '?' * 20,                                  # 22 haori collar behind the jaw
    '......#HHhKKK' + '?' * 6 + 'wKK#' + '?' * 7,             # 23 black collar, white under-collar
    '......#HHHHHHHhKKKwKKK#' + '?' * 7,                     # 24 haori over the shoulder
    '......#HHHHGGHhKKwKKKKKKK#' + '?' * 4,                   # 25 sash over the haori shoulder
    '......#HHHHHGGh#wKK#KKKKL#????',                         # 26 arm hole, black sleeve
    '......#HHHHh#GGwKKK#KKKKL#????',                         # 27
    '......#HHHh#KKCqKKK#KKKKL#????',                         # 28 round sash clasp
    '......#HHHh#KKCCGKK#KKKLL#????',                         # 29
    '......#HHHh#KKKKGGK#KKLLL#????',                         # 30
    '......#HhHh#KKKKKGG#KKK' + '?' * 7,                      # 31
    '......#HhHh#KKKKKKGG####' + '?' * 6,                     # 32 forearm underside
    '......#HhHh#KKKKKKKGG' + '?' * 9,                        # 33
    '......#HhHh#KKKKKKKKG' + '?' * 9,                        # 34
    '......#HhHh#KKKKKK' + '?' * 12,                          # 35
    '......#HHHh#KKKKKK???GGK#?????',                         # 36
    '......#HHHh#KKKKKKKKKKGGK#????',                         # 37
    '......#HHHh#hHHHHHHHHHHHh#????',                         # 38 white obi
    '......#HHHh#hhhhhhhhhhhhh#????',                         # 39
    '......#HHHHHHHHh#ZKK' + '?' * 10,                        # 40 haori flares over the hakama
    '......#HHHHhHHHHh#KK' + '?' * 10,                        # 41
    '.....#HHHHhHHHHHh#KK' + '?' * 10,                        # 42
    '.....#HHHhHHHHHHh#ZK' + '?' * 10,                        # 43
    '.....#HHHhHHHHHHhh#K' + '?' * 10,                        # 44
    '....#HHHhhHHHHHhh#ZK' + '?' * 10,                        # 45
    '....#HHHhHHHHHHhhh#K' + '?' * 10,                        # 46
    '....#HHhHHHHHHHhhh#K' + '?' * 10,                        # 47
    '...#jHHhHHHHHHhhhh#K' + '?' * 10,                        # 48
    '...#jjhhhhhhhhhjjj#K' + '?' * 10,                        # 49
    '...################K' + '?' * 10,                        # 50 haori hem
]

SCABBARD = (-1, 17, [   # Hyorinmaru's empty scabbard on his back (drawn under the body)
    '.....###', '....#MN#', '....#MN#', '....#MN#', '...#MN#.', '...#MN#.', '...#MN#.', '...#MN#.',
    '..#MN#..', '..#MN#..', '..#MN#..', '..#MN#..', '..#MN#..', '.#MN#...', '.#MN#...', '.#MN#...',
    '.#MN#...', '.#MN#...', '#MN#....', '#MN#....', '#MN#....', '#MN#....', '.##.....'])

STAR = (24, 26, [   # four-point star tsuba at the base of the blade
    '???y???', '???Y???', '??yYy??', 'yYYYYYy', '??yYy??', '???Y???', '???y???'])


# v3 pose: small and composed, upright with arms crossed (near forearm on top, hands tucked), Hyorinmaru
# sheathed on his back: hilt + gold star guard over the shoulder, sash across the chest holding it.
# Straight legs, feet slightly apart, hakama falling straight (no bent knees); feet end at row 52. Absolute template rows, (x, 'pixels') segments.
COMPOSED = {
    22: [(6, '#HHh')],
    23: [(6, '#HHhKKK'), (19, 'wKK#')],
    24: [(5, '#HHHHHHHhKKKwKKK#')],
    25: [(4, '#HHHHqGHhKKwKK#KKKL#')],
    26: [(4, '#HHHHHqGgKwKKK#KKKL#')],
    27: [(4, '#HHHHh#qGgKKKK#KKKL#')],
    28: [(4, '#HHHh#KKqCgKKK#KKLL#')],
    29: [(4, '#HHh###########KKLL#')],
    30: [(4, '#HhH#ccKKKKKKKKKKKKL#')],
    31: [(4, '#HhH#lcKKKKKKKKKKKLL#')],
    32: [(4, '#HhH#K###########cc#')],
    33: [(4, '#HhH#KKKKKKKKKKKKlc#')],
    34: [(4, '#HHh#ZKKK#####KKLL#')],
    35: [(4, '#HHh#ZKK#KKKqG#KKL#')],
    36: [(4, '#HHh##Z#KKKKKqG#L#')],
    37: [(4, '#HHh#hHHHHHHHHHHhh#')],
    38: [(4, '#HHh#hhhhhhhhhhhhh#')],
    39: [(4, '#HHHh#ZKKKKLZKKKKL#')],                        # straight legs, hakama falling straight
    40: [(4, '#HHHh#ZKKKKLZKKKKL#')],
    41: [(4, '#HHhH#ZKKKKL#ZKKKL#')],
    42: [(4, '#HHhH#ZKKKKL#ZKKKL#')],
    43: [(4, '#HhHH#ZKKKKL#ZKKKL#')],
    44: [(4, '#HhHH#ZKKKKL#ZKKKL#')],
    45: [(4, '#HHhH#ZKKKKL#ZKKKL#')],
    46: [(4, '#jhhj#ZKKKKL#ZKKKL#')],
    47: [(4, '######ZKKKKL#ZKKKL#')],
    48: [(9, '#ZKKKKL#ZKKKL#')],
    49: [(10, '#HHh#'), (16, '#HHh#')],
    50: [(9, '#HHHHh#'), (16, '#HHHHh#')],
    51: [(8, '#RRRRRr#'), (16, '#RRRRRRr#')],
    52: [(8, '#' * 8), (16, '#' * 9)],
}
HILT = (-1, 14, [   # hilt (blue-grey wrap with diamond marks) up and back over the shoulder, gold star guard
    '##.......',
    '#nn#.....',
    '#nXn#....',
    '.#nXn#...',
    '..#nXn#..',
    '...#nXn#.',
    '...yYy##.',
    '..yYYYy..',
    '...yYy...',
    '....y....'])
SHEATH = (-2, 23, [  # sheath under everything, from the guard down the back, tip below the haori
    '......##', '.....#NM', '.....#NM', '....#NM#', '....#NM#', '...#NM#.', '...#NM#.', '...#NM#.',
    '..#NM#..', '..#NM#..', '..#NM#..', '.#NM#...', '.#NM#...', '.#NM#...', '#NM#....', '#NM#....',
    '#NM#....', '#NM#....', '#NM#....', '.##.....'])


def check():
    for i, r in enumerate(BODY):
        assert len(r) == 30, ('BODY', i + 22, len(r))


def tri(mask, a, b, c, ox, oy):
    h, w = mask.shape
    (x0, y0), (x1, y1), (x2, y2) = a, b, c
    d = (y1 - y2) * (x0 - x2) + (x2 - x1) * (y0 - y2)
    for y in range(min(y0, y1, y2), max(y0, y1, y2) + 1):
        for x in range(min(x0, x1, x2), max(x0, x1, x2) + 1):
            l1 = ((y1 - y2) * (x - x2) + (x2 - x1) * (y - y2)) / d
            l2 = ((y2 - y0) * (x - x2) + (x0 - x2) * (y - y2)) / d
            if l1 >= -0.02 and l2 >= -0.02 and 1 - l1 - l2 >= -0.02 and 0 <= y + oy < h and 0 <= x + ox < w:
                mask[y + oy, x + ox] = True


def line(a, b):
    (x0, y0), (x1, y1) = a, b
    n = max(abs(x1 - x0), abs(y1 - y0))
    return [(round(x0 + (x1 - x0) * t / n), round(y0 + (y1 - y0) * t / n)) for t in range(n + 1)] if n else [a]


def ranges_mask(shape, rows, ox, oy):
    m = np.zeros(shape, bool)
    for y, rs in rows.items():
        for a, b in rs:
            m[y + oy, a + ox:b + ox + 1] = True
    return m


def paint(img, m, key):
    img[m, :3] = K[key]; img[m, 3] = 255


def build_head(img, hair_mode='trace'):
    h, w = img.shape[:2]
    tpl = img.copy()
    rgb = tpl[..., :3].astype(int)
    opaque = tpl[..., 3] > 0
    is_outline = np.all(rgb == K['#'], -1)
    is_skin = np.zeros((h, w), bool)
    for c in SKIN:
        is_skin |= np.all(rgb == c, -1)
    yy, xx = np.mgrid[0:h, 0:w]
    ty, tx = yy - OY, xx - OX                          # template coords
    head_box = (ty <= 21) & (tx <= 25)
    face = ranges_mask((h, w), FACE, OX, OY)
    ear = ranges_mask((h, w), EAR, OX, OY)
    if hair_mode == 'flames':
        # previous round (kept for the check image and for spiky characters): template mass + thin FLAMES
        hair = opaque & head_box & ~is_outline & ~is_skin & ~face & ~ear
        hair &= ~((tx >= 24) & (ty >= 19)) & ~((tx <= 8) & (ty >= 21))
        hair |= head_box & (ty >= 8) & (ty <= 17) & (tx == 24)
        for a, b, c in SPIKES:
            tri(hair, a, b, c, OX, OY)
        hair &= ~face & ~ear
        img[(ty <= 21) & (tx <= 27)] = 0
        paint(img, hair, 'W')
        for a, b, c in SPIKES:
            mid = np.array([(a[0] + b[0]) / 2, (a[1] + b[1]) / 2]); ax = np.array(c) - mid
            n = np.array([-ax[1], ax[0]]); n = -n if n @ np.array([-1.0, 1.0]) < 0 else n
            m = np.zeros_like(hair); tri(m, a, b, c, OX, OY)
            paint(img, m & hair & (((tx - mid[0]) * n[0] + (ty - mid[1]) * n[1]) > 0.5), 'S')
            for x, y in line((round(mid[0]), round(mid[1])), c)[:-2]:
                if hair[y + OY, x + OX]:
                    img[y + OY, x + OX, :3] = K['U']
        return finish_head(img, tpl, hair, face, ear, tx, ty)
    # hair silhouette TRACED from ref 00 (tools/style/trace_hair.py), aligned on the eyes and chin
    import trace_hair as th
    rm = th.ref_mask(REF, th.white_hair, REF_HEAD_BOX, mirror=REF_MIRROR)
    tm, _ = th.to_sprite(rm, REF_EYES, REF_CHIN, SPR_EYES, SPR_CHIN, SPR_BOX, thresh=TRACE_THRESH)
    hair = np.zeros((h, w), bool)
    x0, y0 = SPR_BOX[0] + OX, SPR_BOX[1] + OY
    hh, ww = tm.shape
    ys0, xs0 = max(0, -y0), max(0, -x0)
    hair[y0 + ys0:y0 + hh, x0 + xs0:x0 + ww] = tm[ys0:, xs0:][:h - y0 - ys0, :w - x0 - xs0]
    hair = (hair | HAIR_ADD_MASK(tx, ty)) & ~HAIR_CUT_MASK(tx, ty)
    ear &= ~hair                                               # side locks cover the ear
    hair &= ~face & ~ear & (ty <= 22)
    # fill enclosed gaps between spikes (anything transparent not reachable from the canvas edge)
    free = ~hair & ~face & ~ear
    reach = np.zeros_like(free); reach[0, :] = free[0, :]; reach[:, 0] |= free[:, 0]; reach[:, -1] |= free[:, -1]
    while True:
        grown = reach.copy()
        grown[1:] |= reach[:-1]; grown[:-1] |= reach[1:]; grown[:, 1:] |= reach[:, :-1]; grown[:, :-1] |= reach[:, 1:]
        grown &= free
        if (grown == reach).all():
            break
        reach = grown
    hair |= free & ~reach & (ty <= 21) & (tx <= 27)
    for _ in range(2):                                        # fill pinholes between spikes (read as noise)
        n4 = sum(np.roll(hair, d, ax) for d in (-1, 1) for ax in (0, 1))
        hair |= ~hair & (n4 >= 3) & ~face & ~ear & (ty <= 21)
    nb = sum(np.roll(np.roll(hair, dy, 0), dx, 1) for dy in (-1, 0, 1) for dx in (-1, 0, 1)) - hair
    hair &= ~(hair & (nb == 0))                               # drop isolated specks only (1-px tips stay)
    # clear the old head and repaint
    img[(ty <= 21) & (tx <= 27)] = 0
    paint(img, hair, 'W')
    # shading: mostly flat white; soft blue-grey only in the lower and back part of the mass + strand lines
    sh = hair & ((ty >= 13) & (tx <= 10) | (ty >= 18) | (tx - ty <= -4) & (ty >= 4))   # lower + back part
    sh[:-1] |= hair[:-1] & ~hair[1:] & (ty[:-1] >= 4)          # under-edge of every lock
    paint(img, sh, 'S')
    paint(img, hair & (ty >= 17) & (tx <= 8), 'U')
    for a, b, col in STRANDS:
        for x, y in line(a, b):
            if hair[y + OY, x + OX]:
                img[y + OY, x + OX, :3] = K[col]
    return finish_head(img, tpl, hair, face, ear, tx, ty)


def finish_head(img, tpl, hair, face, ear, tx, ty):
    # face and ear
    paint(img, face, 'c')
    paint(img, face & (tx == 11), 'l')
    paint(img, ear, 'l')
    for (x, y) in [(7, 19), (7, 20), (8, 20)]:
        img[y + OY, x + OX, :3] = K['u']
    # outline: around everything, and where hair meets skin
    body = hair | face | ear
    ring = np.zeros_like(body)
    ring[1:] |= body[:-1]; ring[:-1] |= body[1:]; ring[:, 1:] |= body[:, :-1]; ring[:, :-1] |= body[:, 1:]
    ring &= ~body & (ty <= 22)
    paint(img, ring, '#')
    edge = hair & ((np.roll(face, 1, 0)) | (np.roll(face, -1, 0)) | np.roll(face, 1, 1) | np.roll(face, -1, 1))
    lock = np.zeros_like(hair)
    for y, (a, b) in _LOCK.items():
        lock[y + OY, a + OX:b + OX + 1] = True
    paint(img, edge & ~lock, '#')
    # nose bump + jaw/chin from the template
    img[19 + OY, 19 + OX, :3] = K['l']
    for y in (22, 23):
        row = tpl[y + OY].copy()
        keep = (tx[y + OY] >= 10) & (tx[y + OY] <= 23)
        img[y + OY][keep] = row[keep]
        img[y + OY][(tx[y + OY] >= 24) & (tx[y + OY] <= 27)] = 0          # Tanjiro's earring
    return img


def paint_lock(img):
    """the signature fringe lock, drawn last so it lies over the brow and the eye's inner corner"""
    for y, (a, b) in _LOCK.items():
        for x in range(a, b + 1):
            img[y + OY, x + OX, :3] = K['W' if x == a else 'S']; img[y + OY, x + OX, 3] = 255
        for x in (a - 1, b + 1):                       # thin outline where it lies on skin
            if tuple(img[y + OY, x + OX, :3]) in [K['c'], K['l']]:
                img[y + OY, x + OX, :3] = K['#']
    img[19 + OY, 20 + OX, :3] = K['#']; img[19 + OY, 20 + OX, 3] = 255


def recolour_t(img, mapping, box):
    x0, y0, x1, y1 = box
    se.recolour(img, mapping, (x0 + OX, y0 + OY, x1 + OX, y1 + OY))


def build(face=CHOSEN, pose=POSE, hair_mode='trace'):
    check()
    img = se.pad(se.load(T), left=OX, top=OY, bottom=1)
    if pose == 'composed':
        chin = img[22 + OY:24 + OY, 10 + OX:24 + OX].copy()
        img[22 + OY:] = 0; img[14 + OY:22 + OY, 26 + OX:] = 0          # drop Tanjiro's body and sword
        img[22 + OY:24 + OY, 10 + OX:24 + OX] = chin
        img = build_head(img, hair_mode)
        for x, y, rows in FACES[face]:
            se.patch(img, x + OX, y + OY, rows, K)
        paint_lock(img)
        spec = {y + OY: [(x + OX, t) for x, t in v] for y, v in COMPOSED.items()}
        se.patch(img, 0, 24 + OY, se.seg_rows(img.shape[1], {y - 24 - OY: v for y, v in spec.items() if y >= 24 + OY}), K)
        se.patch(img, 0, 22 + OY, se.seg_rows(img.shape[1], {y - 22 - OY: v for y, v in spec.items() if y < 24 + OY}, fill='?'), K)
        se.patch(img, HILT[0] + OX, HILT[1] + OY, HILT[2], K)
        se.patch_under(img, SHEATH[0] + OX, SHEATH[1] + OY, SHEATH[2], K)
        a = img[..., 3] > 0                                            # drop stray single pixels
        n4 = sum(np.roll(a, d, ax) for d in (-1, 1) for ax in (0, 1))
        img[a & (n4 == 0)] = 0
        return se.crop_to_content(img)
    # sword: teal-tinted blade, blue-grey hilt and pommel
    recolour_t(img, {(46, 46, 54): K['B'], (196, 190, 201): K['X'], (200, 205, 216): K['X'],
                     (87, 89, 102): K['A']}, (23, 14, 45, 31))
    recolour_t(img, {(42, 15, 26): K['n'], (196, 190, 201): K['n']}, (14, 29, 25, 38))
    # Tanjiro's hakama -> black; haori front strip (checker) -> white; leg wraps -> black + white tabi
    recolour_t(img, {(62, 34, 44): K['Z'], (90, 49, 56): K['K'], (118, 70, 78): K['L'], (46, 46, 54): K['Z'],
                     (42, 15, 26): K['Z'], (48, 14, 23): K['Z']}, (10, 38, 31, 56))
    recolour_t(img, {(22, 42, 44): K['h'], (78, 157, 135): K['h'], (98, 195, 163): K['H'],
                     (110, 186, 163): K['H']}, (19, 36, 26, 47))
    recolour_t(img, {(196, 190, 201): K['K'], (244, 235, 236): K['L']}, (8, 50, 31, 54))
    recolour_t(img, {(196, 190, 201): K['h'], (244, 235, 236): K['H']}, (6, 54, 31, 56))
    recolour_t(img, {(42, 15, 26): K['r'], (142, 63, 69): K['R'], (118, 70, 78): K['R'],
                     (62, 34, 44): K['r'], (48, 14, 23): K['r']}, (5, 55, 31, 59))
    img = build_head(img)
    se.patch(img, OX, 22 + OY, BODY, K)
    se.patch(img, STAR[0] + OX, STAR[1] + OY, STAR[2], K)
    se.patch_under(img, SCABBARD[0] + OX, SCABBARD[1] + OY, SCABBARD[2], K)
    for x, y, rows in FACES[face]:
        se.patch(img, x + OX, y + OY, rows, K)
    return img


def faces_sheet(path, z=12):
    f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 22)
    heads = [(n, build(n, pose='tanjiro')[0:OY + 26, 0:OX + 30]) for n in FACES]
    W = sum(h.shape[1] * z + 40 for _, h in heads) + 40
    H = heads[0][1].shape[0] * z + 70
    c = Image.new('RGBA', (W, H), (213, 225, 237, 255)); d = ImageDraw.Draw(c); x = 40
    for n, h in heads:
        im = Image.fromarray(h, 'RGBA')
        c.alpha_composite(im.resize((im.width * z, im.height * z), Image.NEAREST), (x, 20))
        d.text((x, H - 40), n + ('  (used)' if n == CHOSEN else ''),
               fill=(40, 120, 60) if n == CHOSEN else (30, 30, 40), font=f)
        x += h.shape[1] * z + 40
    c.convert('RGB').save(path)


def hair_vs_ref(path, z=12):
    """head at 12x next to crops of the face refs 00 (3/4) and 01 (front), scaled to the same height"""
    head = se.crop_to_content(build())[0:OY + 24 - 1]
    hd = Image.fromarray(head, 'RGBA'); hd = hd.resize((hd.width * z, hd.height * z), Image.NEAREST)
    H = hd.height
    refs = []
    for fn, box in (('00_Ep363HitsugayaProfile.png', (60, 0, 560, 470)), ('01_Ep257HitsugayaProfile.png', (0, 0, 762, 700))):
        r = Image.open(f'refs/redraw/hitsugaya/{fn}').convert('RGBA').crop(box)
        refs.append(r.resize((round(r.width * H / r.height), H), Image.LANCZOS))
    W = hd.width + sum(r.width for r in refs) + 80
    c = Image.new('RGBA', (W, H + 40), (213, 225, 237, 255)); x = 20
    for im in [hd] + refs:
        c.alpha_composite(im, (x, 20)); x += im.width + 20
    c.convert('RGB').save(path)


if __name__ == '__main__':
    img = build()
    se.save(img, OUT)
    # check: previous version | new. PREV defaults to the v2 Tanjiro-pose build; pass a saved sprite path as
    # argv[1] to compare against a specific earlier version instead.
    prev = se.load(sys.argv[1]) if len(sys.argv) > 1 else build(hair_mode='flames')   # previous round's hair
    se.zoom([prev, img], 'out/style/hitsugaya_check.png', z=10)
    faces_sheet('out/style/hitsugaya_faces.png')
    hair_vs_ref('out/style/hitsugaya_hair_vs_ref.png')


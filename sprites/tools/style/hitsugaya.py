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
OX, OY = 4, 4       # padding left (scabbard + back spikes) and top (hair spikes)
CHOSEN = 'cool-serious'

K = {
    '#': (26, 21, 33),
    # white hair
    'W': (240, 244, 250), 'S': (200, 210, 228), 'U': (150, 164, 194), 'V': (112, 124, 156),
    # skin
    'c': (248, 212, 173), 'l': (226, 175, 140), 'u': (183, 124, 102),
    # eyes
    'w': (244, 240, 240), 's': (206, 200, 206),
    'P': (16, 70, 74), 'I': (34, 160, 150), 'J': (110, 214, 196), 'x': (250, 255, 255),
    'b': (124, 134, 164),                                  # brow (silver-grey, reads as white brows)
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
SPIKES = [
    ((8, 3), (16, 2), (11, -4)),     # crown, straight up
    ((3, 6), (10, 2), (0, -3)),      # up and back
    ((1, 5), (3, 12), (-4, 4)),      # back, high
    ((1, 9), (3, 15), (-3, 13)),     # back, low
    ((14, 2), (22, 4), (21, -3)),    # front, up
    ((20, 4), (25, 10), (27, 1)),    # front, over the brow
]
CLUMPS = [((11, 6), (5, 11)), ((8, 12), (4, 17))]   # two soft clump lines in the dome   # strand lines in the dome

# face skin rows (template coords): list of inclusive x ranges. Everything else in the head is hair.
FACE = {11: [(12, 13), (20, 21)], 12: [(11, 15), (19, 23)], 13: [(11, 15), (19, 23)],
        14: [(11, 16), (18, 23)], 15: [(11, 23)], 16: [(11, 23)], 17: [(11, 23)], 18: [(11, 23)],
        19: [(11, 23)], 20: [(11, 23)], 21: [(11, 22)]}
EAR = {18: [(7, 9)], 19: [(6, 9)], 20: [(6, 9)], 21: [(7, 9)]}

# face options: (x, y, rows) in template coords; '?' keeps. Eyes built like Tanjiro's: brow row 14,
# lash row 15, eye rows 16-18 (2-px white + 2x3 teal iris), mouth row 21.
FACES = {
    'cool-serious': [   # level lash, short flat brows with the outer end up (inner end pulled down), flat mouth
        (11, 13, ['?b????', '??bbb?', '?####?', '?wwPP?', '?wwIx?', '??wJJ?']),
        (19, 13, ['????b?', '?bbb??', '?####?', '?wwPP?', '?wwIx?', '?wwJJ?']),
        (18, 21, ['oO']),
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


def build_head(img):
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
    # Tanjiro's hair mass (inner pixels only, not his outline), minus the new face
    hair = opaque & head_box & ~is_outline & ~is_skin & ~face & ~ear
    hair &= ~((tx >= 24) & (ty >= 19)) & ~((tx <= 8) & (ty >= 21))         # earrings
    hair |= head_box & (ty >= 8) & (ty <= 17) & (tx == 24)                  # front side lock
    for a, b, c in SPIKES:
        tri(hair, a, b, c, OX, OY)
    hair &= ~face & ~ear
    hair &= ~((ty >= 17) & (tx <= 4)) & ~((ty >= 19) & (tx <= 5))          # short nape
    for _ in range(2):                                        # fill pinholes between spikes (read as noise)
        n4 = sum(np.roll(hair, d, ax) for d in (-1, 1) for ax in (0, 1))
        hair |= ~hair & (n4 >= 3) & ~face & ~ear & (ty <= 21)
    for _ in range(2):                                        # drop 1-px whiskers at spike tips
        nb = sum(np.roll(np.roll(hair, dy, 0), dx, 1) for dy in (-1, 0, 1) for dx in (-1, 0, 1)) - hair
        hair &= ~(hair & (nb <= 1))
    # clear the old head and repaint
    img[(ty <= 21) & (tx <= 27)] = 0
    paint(img, hair, 'W')
    # shading: light from the top-front; shade the lower/back edge of every clump
    sh = np.zeros_like(hair)
    sh[:, 1:] |= hair[:, 1:] & ~hair[:, :-1]                 # back edge
    sh[:-1] |= hair[:-1] & ~hair[1:]                          # lower edge
    sh |= hair & (tx <= 5) & (ty >= 15)                       # under the back spikes, above the ear
    paint(img, sh, 'S')
    deep = hair & (tx <= 6) & (ty >= 17)
    paint(img, deep, 'U')
    for a, b, c in SPIKES:                                    # shade the lower-back half of each spike
        mid = np.array([(a[0] + b[0]) / 2, (a[1] + b[1]) / 2]); ax = np.array(c) - mid
        n = np.array([-ax[1], ax[0]])
        if n @ np.array([-1.0, 1.0]) < 0:
            n = -n
        m = np.zeros_like(hair); tri(m, a, b, c, OX, OY)
        side = ((tx - mid[0]) * n[0] + (ty - mid[1]) * n[1]) > 0.5
        paint(img, m & hair & side, 'S')
    for a, b, c in SPIKES:                                    # strand line along each spike
        mid = ((a[0] + b[0]) // 2, (a[1] + b[1]) // 2)
        pts = line(mid, c); pts = pts[len(pts) // 3:-2]
        for x, y in pts:
            if hair[y + OY, x + OX]:
                img[y + OY, x + OX, :3] = K['U']
    for a, b in CLUMPS:
        for x, y in line(a, b):
            if hair[y + OY, x + OX]:
                img[y + OY, x + OX, :3] = K['S']
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
    paint(img, edge, '#')
    # nose bump + jaw/chin from the template
    img[19 + OY, 19 + OX, :3] = K['l']
    for y in (22, 23):
        row = tpl[y + OY].copy()
        keep = (tx[y + OY] >= 10) & (tx[y + OY] <= 23)
        img[y + OY][keep] = row[keep]
        img[y + OY][(tx[y + OY] >= 24) & (tx[y + OY] <= 27)] = 0          # Tanjiro's earring
    return img


def recolour_t(img, mapping, box):
    x0, y0, x1, y1 = box
    se.recolour(img, mapping, (x0 + OX, y0 + OY, x1 + OX, y1 + OY))


def build(face=CHOSEN):
    check()
    img = se.pad(se.load(T), left=OX, top=OY, bottom=1)
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
    heads = [(n, build(n)[0:OY + 26, 0:OX + 30]) for n in FACES]
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


if __name__ == '__main__':
    img = build()
    se.save(img, OUT)
    se.zoom([se.load(T), img], 'out/style/hitsugaya_check.png', z=10)
    faces_sheet('out/style/hitsugaya_faces.png')

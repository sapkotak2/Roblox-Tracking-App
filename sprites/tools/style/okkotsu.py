"""Yuta Okkotsu (Jujutsu Kaisen) built by sprite edits on the clean TANJIRO template (out/style/tanjiro_clean.png).

Kept from Tanjiro: head size and outline position, face block (eye boxes, nose, mouth, jaw, ear), the hands,
the katana blade line, the body silhouette, stance and feet positions, the outline colour and the skin ramp.
Changed: hair (rounded teal-black, soft locks over the forehead), eyes (big round, small pupil, dark circles),
thin soft brows, flat mouth, earrings removed, white Jujutsu High jacket (tall collar, off-centre closure,
gold buttons), black slim trousers, white sneakers, silver katana with a small dark guard and dark hilt,
navy sword bag on the back with a grey strap across the chest.

usage: python3 tools/style/okkotsu.py   -> out/style/okkotsu.png (+ out/style/okkotsu_check.png at 10x)
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import spriteedit as se

T = 'out/style/tanjiro_clean.png'
OUT = 'out/style/okkotsu.png'
PADL = 3            # extra columns on the left for the sword bag

K = {
    '#': (26, 21, 33),                                    # template outline
    # hair: teal-black ramp
    'D': (24, 32, 42), 'M': (42, 58, 70), 'T': (60, 86, 98), 'H': (98, 132, 138),
    # skin (template ramp)
    'c': (248, 212, 173), 'l': (226, 175, 140), 'u': (183, 124, 102),
    # eyes / face
    'w': (244, 235, 236), 'P': (26, 21, 33), 'I': (60, 66, 90),
    'Q': (214, 166, 160), 'R': (168, 118, 128), 'o': (150, 88, 90),
    # white jacket (cool shades)
    'W': (240, 242, 248), 'S': (200, 207, 224), 'U': (146, 155, 182),
    'Y': (226, 178, 72), 'y': (150, 104, 40),             # gold button
    # strap and sword bag
    'G': (92, 98, 118), 'g': (128, 136, 158),
    'N': (52, 60, 96), 'B': (34, 38, 66), 'V': (86, 98, 140),
    # trousers
    'K': (52, 53, 68), 'L': (78, 82, 102), 'Z': (37, 36, 50),
    # sneakers
    'E': (172, 178, 198),
    # katana
    'b': (178, 186, 204), 'x': (240, 244, 250), 's': (128, 136, 156), 'z': (40, 38, 58),
}

HEAD = [  # x 0-27, rows 0-23: rounded teal-black hair, soft locks, Tanjiro's face block (eyes come from FACE)
    '............................',  # 0
    '..........#....#............',  # 1
    '........###M###M###.........',  # 2
    '......##MMMMMMMMMMMMM##.....',  # 3
    '.....#MMMTTTTHHTTTMMMMM#....',  # 4
    '....#MMTTHHHHHHHTTMMMMMM#...',  # 5
    '...#MMTTTHHDHHTTTDMMMMMMM#..',  # 6
    '..#DMMMTTDMMMTTMMMDMMMMMM#..',  # 7
    '.#DMMMMMDMMMMMMMMMMDMMMMM#..',  # 8
    '#DMMMMMDMMMMMMDMMMMMDMMMM#..',  # 9
    '.#DMMMMDMMMMMMDMMMMMDMMMM#..',  # 10
    '##' 'D' 'MMMMMM' 'D' 'MMMM' 'D' 'cc' 'MMM' 'D' 'cc' 'D' 'M' '#..',  # 11
    '.#' 'D' 'MMMMM' 'D' 'MM' 'D' 'cccc' 'MM' 'D' 'cccc' 'D' 'M' '#..',  # 12
    '.#' 'D' 'MMMM' 'D' 'MM' 'D' 'l' 'cccc' 'MD' 'c' 'ccccc' 'M' '#..',  # 13
    '..#' 'D' 'MMMM' 'D' 'M' 'D' 'l' 'ccccc' 'D' 'cccccc' 'M' '#..',  # 14
    '..#' 'D' 'MMMM' 'D' 'M' 'D' 'l' + 'c' * 12 + 'M' '#..',  # 15
    '...#' 'D' 'MMM' 'D' 'M' 'D' 'l' + 'c' * 12 + 'D' '#..',  # 16
    '...#' 'D' 'MM' 'DD' 'M' 'D' 'l' + 'c' * 13 + '#..',  # 17
    '...#' 'D' 'M' '#' 'll' 'DD' 'l' + 'c' * 13 + '#..',  # 18
    '....#' 'D' '#' 'lull' 'l' + 'c' * 13 + '#..',  # 19
    '.....#' 'luul' 'l' + 'c' * 13 + '#...',  # 20
    '.....#' 'lull' 'l' 'ccccccc' 'ou' 'ccc' '##...',  # 21
    '......##..###' 'ccccccccc' '#.....',  # 22
    '.............######ccc#.....',  # 23
]

FACE = [  # big round tired eyes with small pupils, dark circles, thin worried brows ('?' keeps HEAD)
    (11, 13, ['???D??', '??D???', '??###?', '?#wII?', '?wwIP?', '?RwwR?', '??RR??']),   # back eye
    (19, 13, ['DD????', '??D???', '?###??', '#wIIw?', 'wwIPw?', 'RwwR??', '?RR???']),   # front eye
]

BODY = [  # x 0-29, rows 22-44 ('?' keeps the template: chin, hands, hilt, blade, legs)
    '......#WWS' + '?' * 20,                              # 22 collar back
    '......#WWSWWS' '??????' 'SWW#' '???????',              # 23 tall collar
    '......#WWSWWWWWSSSSWWYWW#' '?????',                    # 24 collar + gold button
    '......#UUUUUUUUUUUUUUUUUU#' '????',                    # 25 collar seam
    '.......#SSWGGWWWWW#WWWWWW#' '????',                    # 26 shoulders, strap, sleeve top
    '........#SWWGGWWWW#WWWWWS#' '????',                    # 27
    '........#SWWWGGWWW#WWWWSS#' '????',                    # 28
    '........#SWWWWGGWWW#WWWSS#' '????',                    # 29
    '........#SWWWWWGGWW#WSSSU#' '????',                    # 30 cuff folds
    '........#SWWWWWWGGS#SUS' '???????',                    # 31
    '........#SWWWWWWWSU####' '???????',                    # 32 forearm underside
    '........#SSWWWWWSS#WWSS' '???????',                    # 33 back forearm
    '........#SSWWWWWWS#SUS#' '???????',                    # 34
    '........#SSWWWWWWWS####' '???????',                    # 35
    '........#SSWWWWWWUWWGG##' '??????',                    # 36 closure + strap
    '........#SSWWWWWWUWWWGG#NB#' '???',                    # 37 bag bottom at the front hip
    '........#SSSWWWWWYWWWWGGNNB#' '??',                    # 38 gold button
    '........#SSSWWWWWUWWWWWS#NVB#' '?',                    # 39
    '........#USSSSSWWUWWSSSS#NVB#' '?',                    # 40
    '........#UUSUUSSSUSSUUUU#BNB#' '.',                    # 41 hem folds
    '........################.##...',                      # 42
    '.........#ZZKKKK' + '?' * 14,                           # 43 (haori tail -> trousers)
    '..........#ZKKKK' + '?' * 14,                          # 44
]

DETAILS = [  # small finishing touches (x, y, rows)
    (19, 42, ['W', 'S', '?']),          # trouser drawstring peeking under the hem
    (21, 42, ['?', 'W', 'S']),
    (19, 2, ['.#']),                    # one more soft tuft on the crown
]

FEET = [  # x 0-29, rows 55-58: chunky white sneakers
    '.......#' 'WWWW' '#.......#' 'WWWW' '#....',          # 55
    '......#' 'WWWWWWS' '#.....#' 'WWWWWWS' '#.',          # 56
    '......#' 'EEEEEEEE' '#....#' 'EEEEEEEE' '#',          # 57
    '......' + '#' * 10 + '....' + '#' * 10,               # 58
]

BAG = [  # drawn UNDER everything: navy katana bag, tied top behind the head, running down the back
    (-3, 13, ['..###....',
              '.#VNN#...',
              '#VNNNB#..',
              '#VNNNB#..',
              '#gggggg#.',
              '.#VNNB#..',
              '.#VNNB#..',
              '..#VNB#..',
              '..#VNNB#.',
              '...#VNB#.',
              '...#VNNB#',
              '....#VNB#',
              '....#VNNB#',
              '.....#VNB#',
              '.....#VNNB#',
              '......#VNB#']),
]


def check():
    for i, r in enumerate(HEAD):
        assert len(r) == 28, ('HEAD', i, len(r))
    for i, r in enumerate(BODY):
        assert len(r) == 30, ('BODY', i + 22, len(r))
    for i, r in enumerate(FEET):
        assert len(r) == 30, ('FEET', i + 55, len(r))


def build():
    check()
    img = se.pad(se.load(T), bottom=1)                 # one extra row for the sneaker soles' outline
    # legs: Tanjiro's hakama + leg wraps -> black trousers (keeps his leg shapes and stance)
    se.recolour(img, {(62, 34, 44): K['Z'], (90, 49, 56): K['K'], (118, 70, 78): K['L'],
                      (196, 190, 201): K['K'], (244, 235, 236): K['L'], (46, 46, 54): K['Z']}, (8, 42, 30, 56))
    se.patch(img, 0, 0, HEAD, K)
    for x, y, rows in FACE:
        se.patch(img, x, y, rows, K)
    se.patch(img, 0, 22, BODY, K)
    se.patch(img, 0, 55, FEET, K)
    for x, y, rows in DETAILS:
        se.patch(img, x, y, rows, K)
    img = se.pad(img, left=PADL)
    for x, y, rows in BAG:
        se.patch_under(img, x + PADL, y, rows, K)
    # katana: black nichirin blade -> silver (blade only lives right of x 25, rows 14-31)
    se.recolour(img, {(46, 46, 54): K['b'], (196, 190, 201): K['x'], (200, 205, 216): K['x'],
                      (87, 89, 102): K['s']}, (26, 14, 45, 31))
    # hilt (Tanjiro's dark wrap) -> dark navy wrap, pommel -> steel
    se.recolour(img, {(42, 15, 26): K['z'], (196, 190, 201): K['s']}, (17, 29, 28, 38))
    return img


if __name__ == '__main__':
    img = build()
    se.save(img, OUT)
    tj = se.load(T)
    se.zoom([tj, img], 'out/style/okkotsu_check.png', z=10)
    print(se.dump(img, K)[0])

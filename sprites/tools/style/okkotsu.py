"""Yuta Okkotsu (Jujutsu Kaisen) v2, built by sprite edits on the clean TANJIRO template (out/style/tanjiro_clean.png).

Kept from Tanjiro: head size and outline, face block (eye boxes, lash line, brow row, nose, mouth, jaw, ear),
the hands, the katana line, the torso silhouette, stance and feet positions, the outline colour and skin ramp.
Changed:
  hair    black with a subtle blue-grey shine, drawn with Tanjiro's technique (clumps, strand lines, broken
          outline): parted messy fringe with locks between the eyes, side locks and nape pieces
  face    Tanjiro-built eyes (lash line, 2-px white, 2x3 dark grey-blue iris with a 1-px highlight), heavy lid,
          soft tired shade under the eye only, thin brows raised at the inner end, tiny soft mouth.
          Three expressions in FACES (tired-gentle is used; see out/style/okkotsu_faces.png)
  outfit  white Jujutsu High jacket (tall stand-up collar framing the neck, gold buttons, off-centre closure,
          wide folded sleeves, fuller hem flaring at the hips), slim straight black trousers, white sneakers
          with a dark sole line
  props   silver katana with dark hilt; navy sword bag on the back with a grey strap across the chest

usage: python3 tools/style/okkotsu.py
  -> out/style/okkotsu.png, out/style/okkotsu_check.png (Tanjiro | Okkotsu, 10x),
     out/style/okkotsu_faces.png (3 face variants, 12x)
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import spriteedit as se
from PIL import Image, ImageDraw, ImageFont

T = 'out/style/tanjiro_clean.png'
OUT = 'out/style/okkotsu.png'
PADL = 3            # extra columns on the left for the sword bag
CHOSEN = 'deadpan'

K = {
    '#': (26, 21, 33),                                    # template outline
    # hair: black with a subtle blue-grey shine
    'D': (22, 22, 31), 'M': (40, 42, 54), 'T': (58, 62, 78), 'H': (92, 100, 122),
    # skin (template ramp)
    'c': (248, 212, 173), 'l': (226, 175, 140), 'u': (183, 124, 102),
    # eyes / face
    'w': (244, 235, 236), 's': (206, 196, 204),           # eye white, white under the lid's shadow
    'P': (30, 30, 44), 'I': (58, 66, 92), 'J': (96, 108, 140), 'x': (250, 250, 255),   # iris ramp + highlight
    'd': (52, 30, 40),                                    # lash taper (Tanjiro's lash end colour, cooled)
    'b': (112, 92, 98),                                    # thin soft brow
    'r': (226, 186, 168),                                 # tired shade under the eye (soft, skin-toned)
    'o': (204, 138, 126), 'O': (142, 80, 84), 'q': (196, 136, 124),              # tiny mouth
    # white jacket (cool shades)
    'W': (240, 242, 248), 'S': (200, 207, 224), 'U': (146, 155, 182),
    'Y': (226, 178, 72),                                  # gold button
    # strap and sword bag
    'G': (92, 98, 118), 'g': (128, 136, 158),
    'N': (52, 60, 96), 'B': (34, 38, 66), 'V': (86, 98, 140),
    # trousers
    'K': (50, 51, 66), 'L': (76, 80, 100), 'Z': (36, 35, 48),
    # sneakers
    'E': (196, 202, 218), 'Q': (72, 74, 92),
    # katana
    'k': (178, 186, 204), 'X': (240, 244, 250), 'm': (128, 136, 156), 'z': (40, 38, 58),
}

HEAD = [  # x 0-27, rows 0-23. Eyes/brows/mouth come from FACES.
    '............................',                                  # 0
    '.............##.............',                                  # 1
    '.........####MD####.........',                                  # 2
    '.......##MMMMTMMDMMMM##.....',                                  # 3
    '......#DMMTTHHTMDMMTMMMD#...',                                  # 4
    '.....#DMTTHHHTMDMMTTHTMM#...',                                  # 5
    '....#DMTTHHTMDMMMTTHTMMMM#..',                                  # 6
    '...#DMMTTTMDMMMMTTMMDMMMM#..',                                  # 7
    '..#DMMMMMDMMMMDMMMMMDMMMM#..',                                  # 8
    '.#DMMMMDMMMMMDMMMMDMMMDMM#..',                                  # 9
    '#DMMMMDMMMMDMMMMDMMMMDDMM#..',                                  # 10
    '.#' 'DMMMMDMMMMDccDMMMDccDMM' '#..',                            # 11 fringe locks
    '.#' 'DMMMMDMMDlccccDMDccccDM' '#..',                            # 12
    '..#' 'DMMMDMDlcccccDMDcccccM' '#..',                            # 13 centre lock between the eyes
    '..#' 'DMMMDMDl' 'cccccc' 'D' 'cccccc' 'M' '#..',                 # 14
    '..#' 'DMMMDMDl' 'cccccc' 'D' 'cccccc' 'M' '#..',                 # 15
    '...#' 'DMMDMDl' + 'c' * 13 + 'D' '#..',                         # 16
    '...#' 'DMDMMDl' + 'c' * 14 + '#..',                             # 17
    '...#' 'DM#llMDl' + 'c' * 13 + '#..',                            # 18
    '...#' 'D#lulDll' 'ccccccc' 'l' 'ccccc' '#..',                   # 19 (nose bump at x 19)
    '...#' 'D#luull' + 'c' * 13 + '#...',                            # 20
    '....##' 'lulll' 'ccccccc' 'cc' 'ccc' '##...',                   # 21 (mouth from FACES)
    '......##..###' 'ccccccccc' '#.....',                            # 22
    '.............######ccc#.....',                                  # 23
]

# Face variants: list of (x, y, rows) patches over HEAD; '?' keeps HEAD. Built like Tanjiro's eyes:
# brow row 13-14, lash row 15 (+ taper), eye rows 16-18 = 2-px white + 2x3 iris, shade row 19, mouth row 21.
FACES = {
    'deadpan': [        # flat lowered lid over the top of the iris, level gaze, flat low brows, flat mouth
        (11, 12, ['??????', '?bbb??', '?llll?', '?####?', '?ssPP?', '?wwIx?', '??wJJ?', '??????']),
        (19, 12, ['??????', '?bbb??', '?llll?', '?####?', '?ssPP?', '?wwIx?', '??wJJ?', '??????']),
        (18, 21, ['qO']),
    ],
    'side-glance': [    # same half-lid, iris pushed to the front edge of the eye (looking past you)
        (11, 12, ['??????', '?bbb??', '?lllll', '?#####', '?sssPP', '?wwwIx', '??wwJJ', '??????']),
        (19, 12, ['??????', '?bbb??', '?lllll', '?#####', '?sssPP', '?wwwIx', '??wwJJ', '??????']),
        (18, 21, ['OO']),
    ],
    'smug': [           # lids a row lower still, iris half hidden, tiny lopsided mouth (front corner up)
        (11, 12, ['??????', '?bbb??', '??????', '?llll?', '?####?', '?wsPP?', '?wwIx?', '??????']),
        (19, 12, ['??????', '?bbb??', '??????', '?llll?', '?####?', '?wsPP?', '?wwIx?', '??????']),
        (17, 20, ['???q', 'qOO?']),
    ],
}

BODY = [  # x 0-29, rows 22-54 ('?' keeps the template: chin, hands, hilt, blade)
    '......#SWS' + '?' * 20,                                # 22 stand-up collar behind the jaw
    '......#SWWSWWS' '?????' 'SWW#' '???????',              # 23 collar framing the neck
    '......#SWWSWWWWSSSSSWYWW#' '?????',                    # 24 gold collar button
    '......#UWWSWWWWWWWWSWWWU#' '?????',                    # 25 collar
    '......#UUUUUUUUUUUUUUUUUU#' '????',                    # 26 collar seam / shoulders
    '.......#SSWGGWWWWW#WWWWWWW#' '???',                    # 27 sleeve top
    '........#SWWGGWWWW#WWWWUWS#' '???',                    # 28 sleeve folds
    '........#SWWWGGWWWS#WWWUWS#' '???',                    # 29
    '........#SWWWWGGWWS#WWUWSSU#' '??',                    # 30 wide cuff
    '........#SWWWWWGGWS#SSUSSU#' '???',                    # 31
    '........#SWWWWWWGGS#USSU#' '?????',                    # 32
    '........#SWWWWWWWSU#####' '??????',                    # 33 forearm underside
    '........#SSWSWWWSS#WWSS' '???????',                    # 34 back forearm
    '........#SSWWSWWWS#SUS#' '???????',                    # 35
    '........#SSWWWSWWWS####' '???????',                    # 36
    '........#SSWWWWSWUWWGG##' '??????',                    # 37 closure + strap
    '.......#SSSWWWWWSUWWWGG#NB#' '???',                    # 38 bag bottom at the front hip
    '.......#SSSWSSWWWYWWWWGGNNB#' '??',                    # 39 gold button
    '......#SSSSWWSWWWUWWWWWWS#NVB#',                        # 40 hem flares
    '......#USSSSSWWWUWWWSSSSS#NVB#',                        # 41
    '.....#UUSUUSSSSUSSSUUSUUUU#BB#',                        # 42 hem folds
    '.....######################...',                       # 43
    '.........#' 'ZKKKKKKLZKKKKKL' '#....',                  # 44 slim straight trousers
    '.........#' 'ZKKKKL' '#' 'ZKKKKKL' '#.....',             # 45
    '.........#' 'ZKKKKL' '#' 'ZKKKKKL' '#.....',             # 46
    '.........#' 'ZKKKKL' '##' 'ZKKKKL' '#.....',             # 47
    '........#' 'ZKKKKL' '#.#' 'ZKKKKL' '#.....',             # 48
    '........#' 'ZKKKKL' '#..#' 'ZKKKL' '#.....',             # 49
    '........#' 'ZKKKL' '#...#' 'ZKKKL' '#.....',             # 50
    '.......#' 'ZKKKL' '#....#' 'ZKKKL' '#.....',             # 51
    '.......#' 'ZKKKL' '#.....#' 'ZKKL' '#.....',             # 52
    '.......#' 'ZKKL' '#......#' 'ZKKKL' '#....',             # 53
    '.......#' 'ZKKL' '#.......#' 'ZKKL' '#....',             # 54
]

FEET = [  # x 0-29, rows 55-58: white sneakers with a dark sole line
    '.......#' 'WWWW' '#.......#' 'WWWW' '#....',          # 55
    '......#' 'WWWWWWS' '#.....#' 'WWWWWWS' '#.',          # 56
    '......#' 'EQQQQQQQ' '#....#' 'EQQQQQQQ' '#',          # 57
    '......' + '#' * 10 + '....' + '#' * 10,               # 58
]

DETAILS = [  # small finishing touches (x, y, rows)
    (19, 44, ['W', 'S']),               # trouser drawstring peeking under the hem
    (21, 44, ['W']),
    (18, 1, ['..#', '#D#']),            # soft tuft on the crown
    (0, 12, ['#?', '#D', '.#']),        # messy piece at the back of the head
    (3, 20, ['#D#', '#D#', '.#?']),     # longer nape piece
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


def build(face=CHOSEN):
    check()
    img = se.pad(se.load(T), bottom=1)                 # one extra row for the sneaker soles' outline
    # katana: black nichirin blade -> silver; hilt wrap -> dark navy; pommel -> steel
    se.recolour(img, {(46, 46, 54): K['k'], (196, 190, 201): K['X'], (200, 205, 216): K['X'],
                      (87, 89, 102): K['m']}, (23, 14, 45, 31))
    se.recolour(img, {(42, 15, 26): K['z'], (196, 190, 201): K['m']}, (14, 29, 25, 38))
    # Tanjiro's hakama, leg wraps and sandals are replaced, not recoloured
    img[43:, :31] = 0
    se.patch(img, 0, 0, HEAD, K)
    for x, y, rows in FACES[face]:
        se.patch(img, x, y, rows, K)
    se.patch(img, 0, 22, BODY, K)
    se.patch(img, 0, 55, FEET, K)
    for x, y, rows in DETAILS:
        se.patch(img, x, y, rows, K)
    img = se.pad(img, left=PADL)
    for x, y, rows in BAG:
        se.patch_under(img, x + PADL, y, rows, K)
    return img


def faces_sheet(path, z=12):
    f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 22)
    heads = [(n, build(n)[0:26, 0:PADL + 28]) for n in FACES]
    W = sum(h.shape[1] * z + 40 for _, h in heads) + 40
    H = 26 * z + 70
    c = Image.new('RGBA', (W, H), (213, 225, 237, 255)); d = ImageDraw.Draw(c); x = 40
    for n, h in heads:
        im = Image.fromarray(h, 'RGBA')
        c.alpha_composite(im.resize((im.width * z, im.height * z), Image.NEAREST), (x, 20))
        d.text((x, 26 * z + 30), n + ('  (used)' if n == CHOSEN else ''),
               fill=(40, 120, 60) if n == CHOSEN else (30, 30, 40), font=f)
        x += h.shape[1] * z + 40
    c.convert('RGB').save(path)


if __name__ == '__main__':
    img = build()
    se.save(img, OUT)
    se.zoom([se.load(T), img], 'out/style/okkotsu_check.png', z=10)
    faces_sheet('out/style/okkotsu_faces.png')
    print(se.dump(img, K)[0])

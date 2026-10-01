"""Chibi characters, facing right. Logical coords: head top y=0, feet ~y=63."""
from pix import Canvas, hx, shade

WHITE = hx('f4f2f8'); DARK = hx('1c1626')

def head(c, skin):
    c.ellipse(11, 0, 36, 23, skin)
    c.px(37, 16, skin); c.px(37, 17, skin)            # nose bump
    c.rect(23, 22, 28, 26, skin)                      # neck
    c.ellipse(13, 11, 17, 16, skin); c.px(15, 13, shade(skin, .72))  # ear

def face(c, eye=hx('2a1a30'), brow=DARK, white=WHITE, mouth=hx('7a3a3a'), slit=False):
    c.px(31, 13, white, False); c.px(31, 14, white, False)
    c.px(32, 13, eye, False); c.px(32, 14, eye, False)
    c.px(33, 13, DARK, False); c.px(33, 14, DARK, False)
    if slit: c.px(33, 13, DARK, False); c.px(32, 13, eye, False)
    c.line(30, 11, 34, 10, brow)
    c.px(33, 20, mouth, False); c.px(34, 20, mouth, False)

def legs(c, pants, boot, y0=41, y1=58, boot_h=4, toe=True, pants2=None):
    pants2 = pants2 or pants
    c.rect(19, y0, 23, y1, pants); c.rect(26, y0, 30, y1, pants2)
    c.rect(18, y1 + 1, 24, y1 + boot_h, boot)
    c.rect(25, y1 + 1, 32 if toe else 30, y1 + boot_h, boot)

def torso(c, top, y0=25, y1=40, x0=18, x1=30):
    c.rect(x0, y0, x1, y1, top)

def arm_back(c, sleeve, skin, y1=36):
    c.rect(14, 27, 17, y1, sleeve); c.rect(14, y1 + 1, 17, y1 + 4, skin)

def arm_front(c, sleeve, skin, y1=34):
    c.rect(31, 27, 34, y1, sleeve); c.rect(31, y1 + 1, 35, y1 + 4, skin)

def blade(c, x0, y0, x1, y1, col=hx('c9d1e0'), guard=hx('d8b040')):
    c.line(x0, y0, x1, y1, col, 2)
    c.rect(x0 - 1, y0 - 1, x0 + 1, y0 + 1, guard)

# ---------------------------------------------------------------- SASUKE
def sasuke():
    c = Canvas(); skin = hx('f2c9a4'); hair = hx('24284a'); hl = hx('3a4a82')
    white = hx('e8e6f2'); purple = hx('6b4aa0'); pants = hx('2a2a44')
    # back hair spikes
    c.poly([(11,6),(2,9),(8,12),(1,16),(9,17),(2,21),(11,21)], hair)
    arm_back(c, white, skin)
    legs(c, pants, hx('2c3e78'), y1=57, boot_h=5)
    c.rect(19, 51, 23, 57, WHITE); c.rect(26, 51, 30, 57, WHITE)   # leg wraps
    torso(c, white)
    c.poly([(22,25),(26,25),(24,31)], skin)                         # open collar V
    c.rect(18, 36, 30, 39, purple); c.poly([(18,37),(12,41),(15,43),(18,40)], purple)  # rope belt+bow
    head(c, skin)
    # hair cap + bangs
    c.poly([(10,13),(9,7),(13,2),(20,-1),(28,0),(35,3),(37,9),(36,12),(34,8),(30,7),(25,8),(20,9),(17,13),(14,17)], hair)
    c.poly([(13,3),(10,-3),(19,0)], hair); c.poly([(22,0),(26,-4),(30,1)], hair)
    c.poly([(26,8),(30,8),(29,19),(27,22),(25,13)], hair)           # side lock past cheek
    c.poly([(31,7),(37,9),(36,12),(32,11)], hair)                   # forehead lock
    c.rect(17, 2, 21, 3, hl); c.rect(27, 1, 30, 2, hl)
    face(c, eye=hx('c01828'), brow=hair)
    c.px(31,16,hx('c01828'),False)
    arm_front(c, white, skin, y1=36)
    blade(c, 34, 40, 46, 50, hx('b8c6e0'), hx('7a5a30'))
    return c.finish()

# ---------------------------------------------------------------- ITACHI
def itachi():
    c = Canvas(); skin = hx('efc6a2'); hair = hx('1e1e2e'); cloak = hx('1b1a26'); red = hx('c8202e')
    # ponytail
    c.poly([(11,6),(5,10),(3,22),(5,36),(8,34),(9,20),(12,14)], hair)
    c.rect(8, 11, 12, 13, hx('4a3a6a'))                             # hair tie
    # cloak body (flared) behind head
    c.poly([(16,26),(32,26),(35,62),(13,62)], cloak)
    # clouds
    for (x, y) in ((17, 40), (26, 46), (20, 54), (30, 34)):
        c.ellipse(x, y, x + 4, y + 3, WHITE); c.ellipse(x + 1, y + 1, x + 3, y + 2, red)
    c.rect(14, 27, 17, 44, cloak); c.rect(31, 27, 35, 44, cloak)    # sleeves
    c.rect(14, 45, 17, 48, skin)
    c.rect(18, 61, 24, 65, hx('2c3e78')); c.rect(26, 61, 33, 65, hx('2c3e78'))  # sandals
    head(c, skin)
    # high collar (red inside)
    c.poly([(16,22),(34,22),(35,28),(15,28)], cloak); c.rect(21, 22, 29, 27, red)
    c.poly([(21,24),(28,24),(25,30)], skin)
    c.poly([(10,13),(9,6),(14,1),(22,-1),(30,0),(36,4),(37,10),(36,13),(10,13)], hair)
    # forehead protector + scratch
    c.rect(10, 6, 36, 10, hx('2c3358'))
    c.rect(26, 5, 36, 11, hx('c4ccdc')); c.line(26, 9, 36, 6, hx('3a3a52'))
    face(c, eye=hx('c01828'), brow=hair)
    c.line(32, 16, 33, 19, shade(skin, .78)); c.line(29, 16, 29, 19, shade(skin, .78))  # tear troughs
    c.rect(31, 27, 35, 34, cloak); c.rect(31, 35, 35, 38, skin)
    return c.finish()

# ---------------------------------------------------------------- PICCOLO
def piccolo():
    c = Canvas(); skin = hx('6aa84f'); purple = hx('6a2e92'); capew = hx('f0eef4')
    c.poly([(17,25),(31,25),(37,58),(8,58)], capew)                 # cape
    arm_back(c, purple, skin, y1=35)
    legs(c, purple, hx('b87a38'), y1=58, boot_h=5)
    torso(c, purple); c.rect(18, 36, 30, 39, hx('3a2a8a'))          # sash
    head(c, skin)
    c.poly([(13,10),(5,3),(14,15)], skin)                           # long pointed ear
    c.px(7,5,shade(skin,.7),False)
    c.rect(14, 24, 20, 28, capew); c.rect(28, 24, 34, 28, capew)    # shoulder pads
    c.rect(12, 21, 35, 25, capew)                                   # high collar
    c.ellipse(11, -2, 35, 8, capew)                                 # turban
    c.rect(11, 5, 35, 6, hx('d8d4e0'))
    c.line(20, -3, 18, -6, hx('4a8a38')); c.line(27, -3, 29, -6, hx('4a8a38'))   # antennae
    face(c, eye=hx('b03030'), brow=hx('3a2a6a'))
    c.rect(29, 9, 35, 10, hx('3a2a6a'))                              # heavy brow
    arm_front(c, purple, skin, y1=34)
    return c.finish()

# ---------------------------------------------------------------- GOHAN
def gohan():
    c = Canvas(); skin = hx('f0c49c'); hair = hx('1e1a2e'); purple = hx('6a3a98')
    c.poly([(11,6),(3,8),(9,12),(3,15),(11,17)], hair)
    arm_back(c, purple, skin)
    legs(c, purple, hx('a8683a'), y1=58, boot_h=5)
    torso(c, purple); c.poly([(22,25),(27,25),(24,30)], hx('2f4ca8'))   # blue undershirt
    c.rect(18, 36, 30, 39, hx('3a2a8a'))
    head(c, skin)
    c.poly([(10,13),(9,6),(13,1),(20,-2),(28,-1),(35,3),(37,9),(36,12),(33,8),(28,7),(22,8),(17,12),(14,16)], hair)
    c.poly([(14,2),(12,-4),(20,-1)], hair); c.poly([(23,-1),(28,-5),(31,1)], hair)
    c.poly([(30,6),(34,6),(32,16),(30,12)], hair)                    # long front bang
    c.poly([(31,6),(38,8),(36,11),(32,10)], hair)
    face(c, eye=hx('3a2a30'), brow=hair)
    arm_front(c, purple, skin, y1=34)
    return c.finish()

# ---------------------------------------------------------------- VEGETA
def vegeta():
    c = Canvas(); skin = hx('f0c09a'); hair = hx('1a1626'); blue = hx('2a4fc0'); gold = hx('f0c830'); armor = hx('eae8f0')
    arm_back(c, blue, skin, y1=33); c.rect(14, 34, 17, 38, WHITE)
    legs(c, blue, WHITE, y1=57, boot_h=5); c.rect(18, 59, 24, 60, gold); c.rect(25, 59, 32, 60, gold)
    torso(c, blue)
    c.rect(18, 25, 30, 36, armor); c.rect(18, 37, 30, 40, blue)
    c.rect(18, 33, 30, 34, shade(armor, .85))
    c.rect(19, 41, 24, 44, armor); c.rect(26, 41, 31, 44, armor)    # armor skirt
    head(c, skin)
    c.rect(13, 24, 20, 28, gold); c.rect(28, 24, 35, 28, gold)      # shoulder guards
    c.poly([(10,13),(9,6),(12,1),(15,-4),(18,0),(21,-5),(24,0),(28,-4),(31,1),(35,-1),(36,5),(37,10),(36,12),(32,8),(28,6),(22,8),(17,12),(14,16)], hair)
    c.poly([(25,8),(29,8),(27,12)], hair)                            # widow's peak
    face(c, eye=hx('2a2a40'), brow=hair)
    c.line(29, 10, 35, 12, hair, 1)                                  # angry brow
    c.rect(31, 27, 35, 33, blue); c.rect(31, 34, 36, 38, WHITE)
    return c.finish()

# ---------------------------------------------------------------- KRILLIN
def krillin():
    c = Canvas(); skin = hx('f2c8a0'); orange = hx('ee8420'); blue = hx('2c46b4')
    arm_back(c, orange, skin, y1=36); c.rect(14, 36, 17, 38, blue)
    legs(c, orange, blue, y1=57, boot_h=5)
    torso(c, orange); c.rect(18, 36, 30, 39, blue)
    c.poly([(21,25),(28,25),(24,32)], blue)
    head(c, skin)
    for (x, y) in ((25,4),(29,4),(33,5),(27,7),(31,8),(35,8)):       # six burn dots (front)
        c.px(x, y, hx('8a4a3a'), False)
    c.line(31, 11, 35, 10, hx('3a2a2a'))
    face(c, eye=hx('2a2230'), brow=hx('3a2a2a'))
    arm_front(c, orange, skin, y1=34); c.rect(31, 36, 35, 38, blue)
    return c.finish()

# ---------------------------------------------------------------- BEERUS
def beerus():
    c = Canvas(); skin = hx('a98cc0'); dk = hx('3e2a58'); gold = hx('f0c040'); sash = hx('b02a50')
    arm_back(c, skin, skin, y1=34); c.rect(14, 29, 17, 31, gold)
    legs(c, skin, gold, y1=57, boot_h=5)
    c.poly([(16,40),(32,40),(35,56),(13,56)], dk); c.rect(13, 54, 35, 56, gold)   # skirt
    torso(c, dk); c.rect(18, 36, 30, 39, sash); c.rect(22, 36, 25, 39, gold)
    head(c, skin)
    c.poly([(13,6),(9,-4),(21,2)], skin); c.poly([(12,5),(10,-1),(17,3)], dk)       # big ears
    c.poly([(25,2),(30,-4),(33,5)], skin); c.poly([(27,1),(30,-2),(31,3)], dk)
    c.poly([(14,25),(34,25),(32,32),(16,32)], gold)                  # wide collar
    c.rect(19, 26, 29, 28, hx('3a7ac0'))
    face(c, eye=hx('e0c030'), brow=dk, slit=True, mouth=hx('3a2050'))
    c.px(33, 13, DARK, False); c.px(33, 14, DARK, False)
    for dy in (-1, 1): c.line(34, 18, 40, 18 + dy * 2, dk)           # whiskers
    c.px(37, 16, dk, False)
    arm_front(c, skin, skin, y1=34); c.rect(31, 29, 34, 31, gold)
    return c.finish()

# ---------------------------------------------------------------- WHIS
def whis():
    c = Canvas(); skin = hx('9cc4e4'); robe = hx('3a78c8'); hair = hx('eef2fa')
    arm_back(c, robe, skin, y1=36)
    c.poly([(15,26),(33,26),(36,62),(12,62)], robe)                  # long robe
    c.rect(12, 58, 36, 62, WHITE); c.rect(18, 36, 30, 39, hx('222a44'))
    c.rect(18, 61, 24, 65, hx('d8b040')); c.rect(26, 61, 33, 65, hx('d8b040'))
    c.rect(14, 27, 17, 40, robe); c.rect(14, 41, 17, 44, skin)
    head(c, skin)
    c.poly([(12,22),(36,22),(34,29),(14,29)], WHITE)                 # white high collar
    c.poly([(11,10),(9,2),(14,-4),(22,-9),(28,-5),(35,0),(37,7),(36,11),(33,7),(26,6),(18,9),(14,14)], hair)
    c.poly([(16,0),(14,-6),(24,-2)], hair)
    face(c, eye=hx('3a2a4a'), brow=hx('b8c8dc'), mouth=hx('5a4a7a'))
    arm_front(c, robe, skin, y1=34)
    c.line(38, 34, 40, 62, hx('d8b040'), 2)                          # staff
    c.ellipse(36, 28, 42, 34, hx('6ae8f0'))
    return c.finish()

ALL = [('Sasuke', sasuke), ('Itachi', itachi), ('Piccolo', piccolo), ('Gohan', gohan),
       ('Vegeta', vegeta), ('Krillin', krillin), ('Beerus', beerus), ('Whis', whis)]

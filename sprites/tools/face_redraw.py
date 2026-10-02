"""Hand-specified face redraw for readability (like the game's Trunks/Android 17): a clean light skin patch,
two clear eyes with brows, and a mouth. Only pixels that are already opaque are painted (silhouette unchanged).
spec: rect=(x0,y0,x1,y1) face area, eyes=[(x,y),...] top-left of each 2x2 eye (white col then pupil col),
pupil=rgb, mouth=[(x,y),...], extra={(x,y): rgb} optional marks."""
SKIN, SKIN_M, SKIN_D = (250, 218, 186), (238, 190, 154), (206, 146, 112)
BROW, MOUTH, WHITE = (24, 22, 30), (168, 72, 72), (252, 252, 252)
SPECS = {
 'urahara':   dict(rect=(10,11,17,17), eyes=[(11,13),(15,13)], pupil=(40,40,48), mouth=[(14,16)]),
 'renji':     dict(rect=(10,14,19,19), eyes=[(12,15),(16,15)], pupil=(120,30,30), mouth=[(15,18)]),
 'obito':     dict(rect=(10,13,18,19), eyes=[(11,15),(15,15)], pupil=(30,30,40), mouth=[(14,18)]),
 'madara':    dict(rect=(13,12,19,18), eyes=[(14,14),(17,14)], pupil=(40,30,40), mouth=[(17,17)]),
 'kenpachi':  dict(rect=(12,11,19,18), eyes=[(13,13),(17,13)], pupil=(40,30,30), mouth=[(15,17),(16,17)]),
 'byakuya':   dict(rect=(10,9,17,16), eyes=[(11,12),(15,12)], pupil=(60,60,80), mouth=[(14,15)]),
 'yhwach':    dict(rect=(10,9,17,16), eyes=[(11,11),(15,11)], pupil=(140,30,30), mouth=[(12,14),(13,14),(14,14),(15,14)]),
 'toji':      dict(rect=(12,13,20,19), eyes=[(14,15),(18,15)], pupil=(30,40,40), mouth=[(17,18)]),
 'okkotsu':   dict(rect=(13,10,21,17), eyes=[(14,13),(18,13)], pupil=(30,30,40), mouth=[(17,16)]),
 'megumi':    dict(rect=(9,14,16,19), eyes=[(10,15),(14,15)], pupil=(0,90,90), mouth=[(13,18)]),
 'itachi':    dict(rect=(9,12,16,18), eyes=[(10,14),(14,14)], pupil=(200,20,30), mouth=[(13,17)]),
 'geto':      dict(rect=(9,11,18,18), eyes=[(11,13),(15,13)], pupil=(40,30,30), mouth=[(14,17)]),
 'gaara':     dict(rect=(8,11,14,17), eyes=[(8,13),(12,13)], pupil=(40,150,150), mouth=[(11,16)]),
 'jiraiya':   dict(rect=(11,15,18,20), eyes=[(12,16),(16,16)], pupil=(40,30,30), mouth=[(15,19)]),
 'neji':      dict(rect=(19,11,23,17), eyes=[(20,13)], pupil=(190,180,230), mouth=[(22,16)]),
 'sukuna':    dict(rect=(10,12,18,19), eyes=[(12,14),(16,14)], pupil=(200,20,30), mouth=[(15,18)],
                   extra={(11,16): (40,20,20), (17,16): (40,20,20)}),
 'hitsugaya': dict(rect=(12,15,19,20), eyes=[(13,16),(17,16)], pupil=(0,140,140), mouth=[(16,19)]),
 'grimmjow':  dict(rect=(14,11,19,17), eyes=[(15,12),(18,12)], pupil=(30,110,200), mouth=[(18,16)]),
 'asta':      dict(rect=(19,11,26,18), eyes=[(20,13),(24,13)], pupil=(40,140,60), mouth=[(23,17)]),
 'aizen':     dict(rect=(8,9,17,17), eyes=[(10,12),(14,12)], pupil=(110,60,30), mouth=[(14,16)]),
 'hinata':    dict(rect=(13,10,21,17), eyes=[(15,13),(19,13)], pupil=(200,190,235), mouth=[(18,16)],
                   extra={(14,15): (255,150,190), (21,15): (255,150,190)}),
 'itadori':   dict(rect=(12,12,19,19), eyes=[(13,14),(17,14)], pupil=(110,50,40), mouth=[(16,18)]),
}
def redraw(im, spec):
    im = im.convert('RGBA'); p = im.load()
    x0, y0, x1, y1 = spec['rect']
    def put(x, y, c):
        if 0 <= x < im.width and 0 <= y < im.height and p[x, y][3]: p[x, y] = c + (255,)
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            put(x, y, SKIN_M if x == x0 or y == y1 else SKIN)
    for x in range(x0 + 1, x1): put(x, y1, SKIN_D)
    for ex, ey in spec['eyes']:
        for dy in (0, 1): put(ex, ey + dy, WHITE); put(ex + 1, ey + dy, spec['pupil'])
        put(ex + 1, ey + 1, tuple(max(0, v - 60) for v in spec['pupil']))
        for dx in (-1, 0, 1): put(ex + dx, ey - 1, BROW)
    for m in spec['mouth']: put(*m, MOUTH)
    for (x, y), c in spec.get('extra', {}).items(): put(x, y, c)
    return im

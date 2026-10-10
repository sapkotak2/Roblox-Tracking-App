"""Download official character reference art from the character's fandom wiki (MediaWiki API), for the chibi redraws.
For each character: the infobox image + up to N more images from the page whose file names look like character art
(anime/manga/infobox/face/portrait/full). Saved to refs/redraw/<key>/NN_<file>.png with sources.json.
usage: python3 tools/fetch_wiki_refs.py            (all characters in CHARS)
       python3 tools/fetch_wiki_refs.py rengoku    (one)"""
import os, re, sys, json, subprocess, urllib.parse
from PIL import Image
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36'
CHARS = {  # key: (wiki subdomain, page title)
    'baki': ('baki', 'Baki Hanma'), 'jinwoo': ('solo-leveling', 'Sung Jinwoo'), 'kizaru': ('onepiece', 'Borsalino'),
    'escanor': ('nanatsu-no-taizai', 'Escanor'), 'akainu': ('onepiece', 'Sakazuki'), 'okkotsu': ('jujutsu-kaisen', 'Yuta Okkotsu'),
    'bigmom': ('onepiece', 'Charlotte Linlin'), 'rengoku': ('kimetsu-no-yaiba', 'Kyojuro Rengoku'),
    'katakuri': ('onepiece', 'Charlotte Katakuri'), 'asta': ('blackclover', 'Asta'), 'overhaul': ('bokunoheroacademia', 'Kai Chisaki'),
    'chrollo': ('hunterxhunter', 'Chrollo Lucilfer'), 'deku': ('bokunoheroacademia', 'Izuku Midoriya'),
    'makima': ('chainsaw-man', 'Makima'), 'erza': ('fairytail', 'Erza Scarlet'), 'ishida': ('bleach', 'Uryū Ishida'),
    'daki': ('kimetsu-no-yaiba', 'Daki'), 'armin': ('attackontitan', 'Armin Arlert'),
    'lelouch': ('codegeass', 'Lelouch vi Britannia'), 'asuna': ('swordartonline', 'Asuna'),
}
GOOD = re.compile(r'anime|infobox|portrait|face|full|body|profile|design|appearance|manga|color|colour', re.I)
BAD = re.compile(r'logo|icon|symbol|title|volume|chapter_\d|episode_\d|cover|flag|map|signature|\.svg|\.gif|kanji', re.I)
EXTRA = 5


def get(url, binary=False):
    r = subprocess.run(['curl', '-sL', '-m', '40', '-A', UA, url], capture_output=True)
    return r.stdout if binary else r.stdout.decode('utf8', 'ignore')


def api(sub, **q):
    q.update(format='json', redirects=1)
    return json.loads(get(f'https://{sub}.fandom.com/api.php?' + urllib.parse.urlencode(q)) or '{}')


def fetch(key):
    sub, title = CHARS[key]
    out = f'{R}/refs/redraw/{key}'; os.makedirs(out, exist_ok=True)
    urls = []
    pages = api(sub, action='query', titles=title, prop='pageimages', piprop='original').get('query', {}).get('pages', {})
    for p in pages.values():
        if 'original' in p: urls.append(p['original']['source'])
    files = []
    for p in api(sub, action='query', titles=title, prop='images', imlimit=200).get('query', {}).get('pages', {}).values():
        files += [i['title'] for i in p.get('images', [])]
    files = [f for f in files if GOOD.search(f) and not BAD.search(f)][:EXTRA * 3]
    for i in range(0, len(files), 20):
        info = api(sub, action='query', titles='|'.join(files[i:i + 20]), prop='imageinfo', iiprop='url|size')
        for p in info.get('query', {}).get('pages', {}).values():
            ii = (p.get('imageinfo') or [{}])[0]
            if ii.get('url') and ii.get('width', 0) >= 200 and ii['url'] not in urls: urls.append(ii['url'])
    src, n = {}, 0
    for u in urls[:1 + EXTRA]:
        data = get(u, binary=True)
        if len(data) < 2000: continue
        name = re.sub(r'[^A-Za-z0-9_.-]', '_', urllib.parse.unquote(u.split('/revision')[0].split('/')[-1]))[:60]
        tmp = f'{out}/_dl'
        open(tmp, 'wb').write(data)
        try:
            im = Image.open(tmp); im.load()
            im = im.convert('RGBA')
            if max(im.size) > 900: im.thumbnail((900, 900))
            fn = f'{n:02d}_{os.path.splitext(name)[0]}.png'; im.save(f'{out}/{fn}'); src[fn] = u; n += 1
        except Exception:
            pass
        finally:
            os.remove(tmp)
    json.dump(src, open(f'{out}/sources.json', 'w'), indent=1)
    print(f'{key}: {n} images ({sub} / {title})')


if __name__ == '__main__':
    for k in (sys.argv[1:] or CHARS):
        fetch(k)

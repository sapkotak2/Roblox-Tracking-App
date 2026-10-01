#!/usr/bin/env node
// StickFight DBZ sprites: Vegeta (26x56), Piccolo (25x56), Krillin (33x45). All face right.
// Each sprite = palette (letter -> hex colour) + rows of letters ('.' = transparent).
// Usage:  node dbz_sprites.js [outDir]      -> writes vegeta.png, piccolo.png, krillin.png
//         node dbz_sprites.js [outDir] --scale 8   -> also writes 8x previews
// No dependencies (uses Node's built-in zlib to write PNGs).
const fs = require('fs'), path = require('path'), zlib = require('zlib');

const SPRITES = {
  vegeta: {
    palette: {"a": "333333", "b": "000000", "c": "fdd5a8", "d": "a88b6a", "e": "d9b48a", "f": "b8b8b8", "g": "ffffff", "h": "e0e0e0", "i": "040430", "j": "000048", "k": "000080", "l": "ffff00", "m": "ffe600", "n": "c4aa00"},
    rows: [
      "...a......................",
      "...aaaa...................",
      "...aaaa...................",
      "...baaaaaaaa...a..........",
      "...bbbbaaaaaaa.ba.........",
      "...bbbbaaaaaaa.ba.........",
      "...bbbbbbbbbaaabba........",
      "...bbbbbbbbbbbaabbaa......",
      "...bbbbbbbbbbbaabbaa......",
      "a..bbbbbbbbbbbbbabbba.....",
      "aaabbbbbbbbbbbbbbbbba.....",
      "aaabbbbbbbbbbbbbbbbba.....",
      "baaabbbbbbbbbbbbbbbbba....",
      "bbbbabbbbbbbbbbbbbbbbb....",
      "bbbbabbbbbbbbbbbbbbbbb....",
      ".bbbbaabbbbbbbbbbbbbbbb...",
      ".bbbbbbbbbbbcdbbbbbbbbb...",
      "...bbbbbbbbdcccdbbbbbdb...",
      "aaaabbbbbbbdccccdbbbbdb...",
      ".bbbabbbbbbecccccebbceb...",
      "...bbbbbbbbcccccccccccb...",
      "....bbbbddbcbbbccccccbb...",
      ".......bccecbfgbccccbhb...",
      ".......bccccchgbbcbbbgb...",
      "........bbbdcccccccccdb...",
      ".......bbbibeccbbbcceb....",
      ".....bbjkkkkbbdececcb.....",
      "....bjjbkkkjbgbbbbbbfb....",
      "....bkkbkkkbggghbhggghb...",
      "...bibbkkkbhgggggbggggb...",
      "...bkkkkjjbbghfbbbbbhb....",
      "...bbkkkbbbfbbblllllbb....",
      ".bbkkkkbggbhgbbbbbbbbib...",
      ".bbikjjbgggbgbmmmmmmbkb...",
      "bbbbbbbggggbhgbbbbbbbbb...",
      "bffghbbggggbbbbbbbbbbfgb..",
      "bffghbbggggbbbbbbbbbbfgb..",
      "bhhgbbbbgggbfhggggffbgbb..",
      "bgggghhbggbbbbbbbbbbbgbhbb",
      "bggggbbgbbikiiikkiiibhbgbb",
      "bhhbgbbgbbkkkkkkkbkkibgfbb",
      ".bbbfbbbiikbkibikbkkibbb..",
      "....bbbbiikbib.bikbbkb....",
      ".....bbbkkbkib.bikbbkb....",
      ".....bbbkkbkib.bikbbkb....",
      ".....bbkbbkkkb.bkkkkib....",
      "....biikkkkib..bikkkib....",
      "....bbbbkkkib..bbbbbbb....",
      "....bbbbkkkib..bbbbbbb....",
      "....bhhgbbbb...bhghhfb....",
      "...bfgggggfb...bggggfb....",
      "...bfgggggfb...bggggfb....",
      "...bbbbhggb....bfgggbbb...",
      ".bbnlnnbffb.....bhbbnlnb..",
      ".bbbbbbbbbb.....bbbbbbbb..",
      ".bbbbbbbbbb.....bbbbbbbb.."
    ]
  },
  piccolo: {
    palette: {"a": "010101", "b": "000002", "c": "010301", "d": "87dd1e", "e": "040003", "f": "000000", "g": "3b9122", "h": "388341", "i": "010002", "j": "3e504b", "k": "77d131", "l": "722e97", "m": "732e98", "n": "a0d347", "o": "a03273", "p": "391b5e", "q": "a1644c", "r": "892d84", "s": "291744", "t": "451f6a"},
    rows: [
      ".........abbbc...........",
      ".......ccdddddcc.........",
      "......edddddddddc........",
      ".....fdggdcadddddbffff...",
      ".....fgggcddcddddcddddf..",
      "ef.bbggggghfdfddgdfbbbdff",
      "idciiggggghcdcdddjc.aadff",
      ".edccgggjdddccddddf...aff",
      ".bgddcggjdddddgggdde.....",
      "..bggdfghjjddddgdddc.....",
      "..egggdggg.jkddgdde......",
      "...aadgggg..jjgjji.......",
      ".....figgdd.j.gjb........",
      "......cjgdddddgga........",
      ".....ijgjddddddc.........",
      "..ieelggjhkddde..........",
      "eimmmmmhjghjccmii........",
      "cllllmlmghgghglmmee......",
      "cnooolllldddgddmmmlb.....",
      "fonnnofcccdddgdmmpna.....",
      "eoooonncddcedgfffpogcc...",
      ".fdddoonfeeaeedddbnoaa...",
      ".fgdddooennoooddeeeoaa...",
      "..bgggggqoodroacoonnooa..",
      "...eecgddddgcbggddqooof..",
      "......ifddoappbbcgddddc..",
      ".......fbefmjjjc.faiff...",
      ".......fjljlmmmc.........",
      ".......epmmmpslme........",
      "......blpmmmpslme........",
      "......blpmmmpslme........",
      "......flplmmpslme........",
      "......illmmmpslme........",
      "......illmmmpslme........",
      ".....fplmmmmpslmme.......",
      ".....iplmmmmsspmme.......",
      ".....iplmmmmsspmme.......",
      "...fflplmmlpbppmme.......",
      "...bblplmmpleplple.......",
      "..fpplpmmtmbmpmmlpf......",
      "..ipplpppmlblplllpc......",
      ".fmpplppllpepmpllpc......",
      ".fmpplmmmpbppplppla......",
      ".fmpppmmppbppppmmma......",
      ".bppppppplfpplpplpi......",
      ".bpppppple.fpplppf.......",
      "..bpppmli..apppppi.......",
      "..fssssi....fsssb........",
      ".iepppf......appi........",
      "bqqggrfb....firgbb.......",
      "eqqqqqqa....cqqqqa.......",
      ".fqqqqc......fqqa........",
      ".fqqqc.......fqqqaa......",
      ".fqqqc.......fqqqaa......",
      ".aqqqf.......fjqqqqb.....",
      "eqqqqf..................."
    ]
  },
  krillin: {
    palette: {"a": "000000", "b": "d28660", "c": "fadab4", "d": "f0f0f4", "e": "fa6e14", "f": "be2824", "g": "4854dc", "h": "9b483e", "i": "242878", "j": "96a0b4", "k": "242c3e", "l": "506070", "m": "e2be5a"},
    rows: [
      "..............aaaaa..............",
      "............aabccccaa............",
      "...........abcccccccca...........",
      "...........accccccbcbca..........",
      "..........abbbbccccccca..........",
      "..........abbbbccccbcba..........",
      "..........abbbbccccccca..........",
      "..........abbbbccccbcba..........",
      "..........acbbbaaccccca..........",
      "..........acabbccacccba....aaaaa.",
      "..........acbbcccaacaaba..accccca",
      "...........abbbccdacdaca..abbccca",
      "...........abbbccdacdaa...accbbba",
      "........aaefabbccccccaggaacaaccca",
      ".......aeeefbhhhhcaaeggeaaacccbba",
      ".......aiiefccccceeefaicccdaaggga",
      "..aaaaaiiifggggggeeffacccccaaggga",
      "..aaaaaiiifggggggeeffacccccaaggga",
      ".acccaaiiifiiiiiefffeaccbbbcccaa.",
      "accccaaaaaeeiigeeedjfaaaaabbba...",
      "accccaaaaaeeiigeeedjfaaaaabbba...",
      "acccbccabbbaeeeeejdffa..aaaaa....",
      ".cccbgggbbbafeeeefffa............",
      ".cccbgggbbbafeeeefffa............",
      "..aaaaaaaaaaiifeefaa.............",
      "...........aaiiggiga.............",
      "...........aaiiggiga.............",
      ".......aaaeeeegiieeeaa...........",
      ".....aaeeeeeggefggeeeaa..........",
      ".....aaeeeeeggefggeeeaa..........",
      "....aeeeeeffggffggfeeeefaa.......",
      "....feeeffffggffggaeeeefeea......",
      "....feeeffffggffggaeeeefeea......",
      "....effeffffaaaaaaafeeffeea......",
      "....eeeefffa......affffeeefaa....",
      ".....aaaaaaa.......affffeefaa....",
      ".....aaaaaaa.......affffeefaa....",
      ".....aakkka.........aaaa..lkka...",
      ".....aakkka............allllla...",
      ".....aammma.............aallla...",
      ".....aammma.............aallla...",
      "....kkkkkka.............aammma...",
      "..aaaaaaaa................alllaa.",
      "..........................aaaaaa.",
      "..........................aaaaaa."
    ]
  }
};

function crc32(buf) {
  let c, crc = 0xffffffff;
  for (let n = 0; n < buf.length; n++) {
    c = (crc ^ buf[n]) & 0xff;
    for (let k = 0; k < 8; k++) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
    crc = (crc >>> 8) ^ c;
  }
  return (crc ^ 0xffffffff) >>> 0;
}
function chunk(type, data) {
  const len = Buffer.alloc(4); len.writeUInt32BE(data.length);
  const td = Buffer.concat([Buffer.from(type), data]);
  const crc = Buffer.alloc(4); crc.writeUInt32BE(crc32(td));
  return Buffer.concat([len, td, crc]);
}
function encodePNG(w, h, rgba) {
  const raw = Buffer.alloc((w * 4 + 1) * h);
  for (let y = 0; y < h; y++) { raw[y * (w * 4 + 1)] = 0; rgba.copy(raw, y * (w * 4 + 1) + 1, y * w * 4, (y + 1) * w * 4); }
  const ihdr = Buffer.alloc(13);
  ihdr.writeUInt32BE(w, 0); ihdr.writeUInt32BE(h, 4); ihdr[8] = 8; ihdr[9] = 6; ihdr[10] = 0; ihdr[11] = 0; ihdr[12] = 0;
  return Buffer.concat([Buffer.from([137,80,78,71,13,10,26,10]), chunk('IHDR', ihdr), chunk('IDAT', zlib.deflateSync(raw)), chunk('IEND', Buffer.alloc(0))]);
}
function toRGBA(sprite, scale = 1) {
  const h = sprite.rows.length, w = sprite.rows[0].length, W = w * scale, H = h * scale;
  const buf = Buffer.alloc(W * H * 4);
  for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) {
    const k = sprite.rows[y][x]; if (k === '.') continue;
    const hex = sprite.palette[k], r = parseInt(hex.slice(0,2),16), g = parseInt(hex.slice(2,4),16), b = parseInt(hex.slice(4,6),16);
    for (let dy = 0; dy < scale; dy++) for (let dx = 0; dx < scale; dx++) {
      const i = ((y * scale + dy) * W + (x * scale + dx)) * 4; buf[i] = r; buf[i+1] = g; buf[i+2] = b; buf[i+3] = 255;
    }
  }
  return { W, H, buf };
}

if (require.main === module) {
  const args = process.argv.slice(2);
  const si = args.indexOf('--scale'); const scale = si >= 0 ? parseInt(args[si + 1], 10) : 0;
  const outDir = args.find((a, i) => !a.startsWith('--') && args[i - 1] !== '--scale') || '.';
  fs.mkdirSync(outDir, { recursive: true });
  for (const [name, s] of Object.entries(SPRITES)) {
    const a = toRGBA(s, 1); fs.writeFileSync(path.join(outDir, name + '.png'), encodePNG(a.W, a.H, a.buf));
    if (scale > 1) { const b = toRGBA(s, scale); fs.writeFileSync(path.join(outDir, `${name}_${scale}x.png`), encodePNG(b.W, b.H, b.buf)); }
    console.log(`${name}: ${s.rows[0].length}x${s.rows.length} -> ${path.join(outDir, name + '.png')}`);
  }
}
module.exports = { SPRITES, encodePNG, toRGBA };

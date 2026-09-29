"""Generate print-and-play sheets (HTML → PDF via headless Chrome) for Last Deck Standing.

Usage: python3 pnp_sheets.py            # writes ../pnp/last-deck-standing-pnp.html and .pdf
Quantities follow components-sheet.md (full 5-player box).
"""
import html
import os
import subprocess

OUT = os.path.join(os.path.dirname(__file__), "..", "pnp")
# Player colours are chosen to never match the rarity colours (gray / blue / purple) or gold.
PLAYERS = [("Red", "#c62828"), ("Orange", "#ef6c00"), ("Teal", "#00897b"), ("Pink", "#d81b60"), ("Black", "#212121")]
RARITY = {1: ("#8a8f9c", "Common"), 2: ("#2f6fd0", "Rare"), 3: ("#7b3fc4", "Epic")}
ICON = {"A": "&#9876;", "M": "&#10140;", "H": "&#10010;", "D": "&#9760;"}  # crossed swords, arrow, cross, skull
TYPE = {"A": "Attack", "M": "Move", "H": "Heal"}
TEXT = {
    "A": "+{v} Attack this turn.",
    "M": "+{v} Move this turn.",
    "H": "Choose one:<br><b>Heal</b> &ndash; return up to {v} Dead card{s} from your hand to the supply, then remove this card from the game.<br><b>Shield</b> &ndash; +{v} Shield (max 4). Stays until damage uses it.",
}


def card(kind, v, name=None, stripe=None, gold=False, owner=None):
    color, tier = RARITY[v]
    if gold:
        color, tier = "#b8860b", "Gold"
    title = name or f"{TYPE[kind]} {v}"
    body = TEXT[kind].format(v=v, s="" if v == 1 else "s")
    stripe_html = f'<div class="stripe" style="background:{stripe}"></div>' if stripe else ""
    return (f'<div class="card" style="--c:{color}">{stripe_html}'
            f'<div class="top"><span class="val">{v}</span><span class="icon">{ICON[kind]}</span></div>'
            f'<div class="name">{html.escape(title)}</div><div class="tier">{(owner + " starting deck") if owner else tier} &middot; {TYPE[kind]}</div>'
            f'<div class="text">{body}</div></div>')


def dead_card():
    return ('<div class="card dead"><div class="top"><span class="icon big">&#9760;</span></div>'
            '<div class="name">DEAD</div><div class="text">Can\'t be played. Stays in your hand until healed. '
            'End your turn with 3+ Dead cards in hand and you are eliminated.</div>'
            '<div class="tier">Print on a different back</div></div>')


def pages(items, per_page, cls):
    out = []
    for i in range(0, len(items), per_page):
        out.append(f'<section class="page {cls}">' + "".join(items[i:i + per_page]) + "</section>")
    return out


TILE_SET = [[], [], [], [], ["M"], ["A"], ["H"], ["H"], ["M", "A"], ["A", "H"], ["H", "M"], ["M", "M"],
            ["M", "A", "H"], ["A", "A", "H"], ["M", "A", "H"]]
CUBE = {"M": "#1e88e5", "A": "#e53935", "H": "#43a047"}


def tile(icons, letter):
    dots = "".join(f'<span class="loot" style="background:{CUBE[k]}">{ICON[k]}</span>' for k in icons)
    return f'<div class="hex"><div class="hexin">{dots}</div><span class="set">{letter}</span></div>'


def main():
    os.makedirs(OUT, exist_ok=True)
    cards = []
    for pname, col in PLAYERS:
        cards += ([card("A", 1, "Strike", col, owner=pname)] * 4 + [card("M", 1, "Dash", col, owner=pname)] * 3
                  + [card("H", 1, "Patch Up", col, owner=pname)] * 3)
    for k in "AMH":
        for v, n in ((1, 9), (2, 6), (3, 3)):
            cards += [card(k, v)] * n
    for k in "AMH":
        cards += [card(k, 2, gold=True)] * 2 + [card(k, 3, gold=True)] * 2
    dead = [dead_card()] * 60
    tiles = []
    for letter in "ABCDE":
        tiles.append([tile(t, letter) for t in TILE_SET])
    ref = open(os.path.join(os.path.dirname(__file__), "..", "rulebook-draft.md")).read()
    qr = ref.split("## Quick Reference")[1].split("---")[0].strip().splitlines()
    import re
    qr_html = "".join("<p>" + re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", html.escape(l)) + "</p>" for l in qr if l.strip())
    tracker = ('<div class="tracker"><h3>Player: ________</h3>' + "".join(
        f'<div class="track"><b>Base {s}</b>' + "".join(f"<span>{i}</span>" for i in range(5)) + "</div>"
        for s in ("Move", "Attack", "Shield")) +
        '<div class="track"><b>Shield now</b>' + "".join(f"<span>{i}</span>" for i in range(5)) + "</div></div>")
    rounds = "".join(
        f'<span class="rnd{" hot" if r == 7 else ""}{" drop" if r in (3, 5, 7, 9, 11) else ""}">{r}'
        f'{"<small>storm fast</small>" if r == 7 else ""}{"<small>drop</small>" if r in (3, 5, 7, 9, 11) else ""}</span>'
        for r in range(1, 26))
    storm = "".join('<div class="mini"></div>' for _ in range(50))

    body = []
    body += pages(cards, 9, "cards")
    body += pages(dead, 9, "cards")
    body += [f'<section class="page tiles"><h2>Loot tiles &mdash; set {"ABCDE"[i]}</h2><div class="hexgrid">' + "".join(t) + "</div></section>"
             for i, t in enumerate(tiles)]
    body.append('<section class="page misc"><h2>Stat trackers</h2>' + tracker * 5 + "</section>")
    body.append(f'<section class="page misc"><h2>Round track</h2><div class="rounds">{rounds}</div>'
                f'<h2>Storm markers (cut out, or use glass beads)</h2><div class="minis">{storm}</div></section>')
    body.append('<section class="page misc"><h2>Reference cards</h2>' + ('<div class="ref">' + qr_html + "</div>") * 2 + "</section>")

    css = """
@page { size: letter; margin: 0.2in 0.25in; }
* { box-sizing: border-box; }
body { margin: 0; font-family: Helvetica, Arial, sans-serif; color: #1b1f2a; }
.page { page-break-after: always; }
.cards { display: grid; grid-template-columns: repeat(3, 2.5in); grid-auto-rows: 3.5in; gap: 0 0.05in; justify-content: center; }
.card { position: relative; border: 1px dashed #999; padding: 0.14in; overflow: hidden; border-top: 0.16in solid var(--c); }
.card .stripe { position: absolute; left: 0; top: 0; bottom: 0; width: 0.12in; }
.card .top { display: flex; justify-content: space-between; align-items: center; }
.card .val { font-size: 34pt; font-weight: 700; color: var(--c); }
.card .icon { font-size: 28pt; }
.card .icon.big { font-size: 60pt; margin: 0 auto; }
.card .name { font-size: 15pt; font-weight: 700; margin-top: 0.05in; }
.card .tier { font-size: 8pt; text-transform: uppercase; letter-spacing: .08em; color: #555; }
.card .text { font-size: 9.5pt; line-height: 1.35; margin-top: 0.1in; }
.card.dead { border-top-color: #111; background: #f3f3f3; text-align: center; }
.card.dead .name { font-size: 26pt; }
h2 { font-size: 14pt; margin: 0 0 0.1in; }
.hexgrid { display: grid; grid-template-columns: repeat(4, 1.9in); gap: 0.06in 0.06in; justify-content: center; }
.hex { position: relative; width: 1.9in; height: 2.19in; clip-path: polygon(50% 0, 100% 25%, 100% 75%, 50% 100%, 0 75%, 0 25%);
       background: #e9e6dc; display: flex; align-items: center; justify-content: center; }
.hexin { display: flex; gap: 0.08in; flex-wrap: wrap; justify-content: center; width: 1.3in; }
.loot { width: 0.42in; height: 0.42in; border-radius: 50%; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 14pt; }
.set { position: absolute; bottom: 0.32in; font-size: 9pt; font-weight: 700; color: #777; }
.tracker { border: 1px solid #999; padding: 0.08in 0.12in; margin-bottom: 0.1in; }
.tracker h3 { margin: 0 0 0.05in; font-size: 11pt; }
.track { display: flex; align-items: center; gap: 0.05in; margin: 0.03in 0; font-size: 10pt; }
.track b { width: 1.1in; }
.track span { width: 0.35in; height: 0.3in; border: 1px solid #999; display: flex; align-items: center; justify-content: center; }
.rounds { display: grid; grid-template-columns: repeat(9, 0.8in); gap: 0.04in; margin-bottom: 0.3in; }
.rnd { height: 0.8in; border: 1px solid #999; display: flex; flex-direction: column; align-items: center; justify-content: center; font-size: 18pt; font-weight: 700; }
.rnd small { font-size: 7pt; font-weight: 400; text-transform: uppercase; }
.rnd.drop { background: #fff4d6; }
.rnd.hot { background: #ede1ff; }
.minis { display: grid; grid-template-columns: repeat(10, 0.7in); gap: 0.05in; }
.mini { width: 0.7in; height: 0.8in; clip-path: polygon(50% 0, 100% 25%, 100% 75%, 50% 100%, 0 75%, 0 25%); background: #7b3fc4; opacity: .55; }
.ref { border: 1px solid #999; padding: 0.15in; margin-bottom: 0.2in; font-size: 10pt; }
.ref p { margin: 0.04in 0; }
"""
    doc = f'<!doctype html><html><head><meta charset="utf-8"><title>Last Deck Standing PnP</title><style>{css}</style></head><body>{"".join(body)}</body></html>'
    html_path = os.path.abspath(os.path.join(OUT, "last-deck-standing-pnp.html"))
    open(html_path, "w").write(doc)
    pdf_path = html_path.replace(".html", ".pdf")
    chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    if os.path.exists(chrome):
        subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={pdf_path}", "file://" + html_path],
                       check=True, capture_output=True)
    print(f"cards: {len(cards)} + {len(dead)} dead · tiles: {sum(map(len, tiles))} · wrote {html_path}")


if __name__ == "__main__":
    main()

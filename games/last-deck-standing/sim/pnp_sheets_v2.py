"""Print-and-play sheets for Last Deck Standing v2 (realtime), HTML -> PDF via headless Chrome.

Usage: python3 pnp_sheets_v2.py
  writes ../pnp/v2/last-deck-standing-v2-cards-11x17.{html,pdf}    card sheets, 4x4 cards (2.5 x 3.5 in) per 11 x 17 page
         ../pnp/v2/last-deck-standing-v2-pieces-11.5x17.{html,pdf} Market mat, reference sheets, blank hex tiles, storm markers on 11.5 x 17

Contents follow rulebook-v2-draft.md: 10 base decks (up to 10 players), three loot decks, the Market deck (21),
the Gold deck (24), 60 Dead cards (plain backs: every card back is the same). Style and icons are reused from
pnp_sheets.py (comic frames, Material Symbols Sharp, rarity colours), so nothing here is hand-drawn artwork.
"""
import html
import random
import os
import subprocess

from pnp_sheets import COMIC_CSS, MSYM, RARITY, TYPE, TYPE_COLOR, comic, tile_color

OUT = os.path.join(os.path.dirname(__file__), "..", "pnp", "v2")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
GOLD = ("#c98a00", "Legendary")

TEXT = {
    "A": "<b>+{v} Attack</b> this turn.<br>Damage = your Attack &minus; 2 per tile of range.",
    "M": "<b>+{v} Move</b> this turn.<br>One tile per point, on top of your Base Move 1.",
    "H": '<i>One-time.</i><br><b class="hl">Heal:</b> remove up to <b>{v}</b> Dead cards from your hand. Then remove this card from the game.',
}


def card(kind, v, source, owner=None, gold=False):
    color, tier = GOLD if gold else RARITY[v]
    tag = f"{source} &middot; {TYPE[kind]}"
    text = TEXT[kind].format(v=v)
    if source == "Market":
        pay = next(p for n, p, k, val in COSTS if k == kind and val == v)
        text += f'<br><b>Cost:</b> {pay}'
    c = comic(TYPE[kind].upper(), TYPE_COLOR[kind], MSYM[kind], text, color, f"+{v}", tag, owner, cls="rar")
    return c.replace('style="--type:', f'style="--rar:{color}; --type:', 1)


def dead():
    return comic("DEAD", "#2a2a33", "skull", "Can't be played or discarded. Stays in your hand until healed.<br><b>3 in hand at the end of your turn = OUT.</b>",
                 tag="Dead", cls="dead")


def sheets(items, per_page, cls):
    return ["<section class='page %s'>%s</section>" % (cls, "".join(items[i:i + per_page])) for i in range(0, len(items), per_page)]


def decks():
    base, loot, market, gold = [], [], [], []
    for n in range(1, 11):
        o = f"Player {n}"
        base += [card("M", 1, "Starting", o)] * 4 + [card("A", 1, "Starting", o)] * 4 + [card("H", 1, "Starting", o)] * 2
    for k, size in (("M", 14), ("A", 26), ("H", 10)):  # loot is 1s and 2s only; 3s come from the Market, kills or drops
        loot += [card(k, 1, "Loot")] * (size // 2) + [card(k, 2, "Loot")] * (size - size // 2)
    for k, v, n in (("A", 2, 6), ("M", 2, 4), ("H", 2, 4), ("A", 3, 3), ("M", 3, 2), ("H", 3, 2)):
        market += [card(k, v, "Market")] * n
    for k in "MAH":
        gold += [card(k, 3, "Gold", gold=True)] * 4 + [card(k, 4, "Gold", gold=True)] * 4
    return base, loot, market, gold


COSTS = [("Attack 2", "2 Attack + 1 Move", "A", 2), ("Move 2", "2 Move + 1 Heal", "M", 2), ("Heal 2", "1 Heal + 1 Attack + 1 Move", "H", 2),
         ("Attack 3", "3 Attack + 1 Move", "A", 3), ("Move 3", "3 Move + 1 Heal", "M", 3), ("Heal 3", "2 Heal + 1 Attack + 1 Move", "H", 3)]


MARKET_COUNTS = {("A", 2): 6, ("M", 2): 4, ("H", 2): 4, ("A", 3): 3, ("M", 3): 2, ("H", 3): 2}  # the 21-card Market deck


def market_mat():
    rows = "".join(
        f'<tr><td><span class="pill" style="background:{TYPE_COLOR[k]}">{n}</span></td><td>{pay}</td><td class="cp">{MARKET_COUNTS[(k, v)]} of 21</td></tr>'
        for n, pay, k, v in COSTS)
    slots = "".join('<div class="slot"><span>FACE UP</span></div>' for _ in range(3))
    return ("<section class='page mat'><h1>MARKET</h1>"
            f"<div class='slots'>{slots}<div class='slot deck'><span>DECK<br>21 cards</span></div></div>"
            "<div class='mrules'><b>How to buy</b><ul>"
            "<li>Any time on your turn, pay the cards below <b>from your hand</b>. Costs count <b>cards, not value</b>, so pay with 1s. Never Dead cards. The cost is also printed on each Market card.</li>"
            "<li>Paid cards <b>leave the game</b>. The bought card goes into your <b>hand</b>.</li>"
            "<li>Refill the face-up row from the deck after each buy.</li></ul></div>"
            f"<table class='costs'><tr><th>Buy</th><th>Pay</th><th>In the deck</th></tr>{rows}</table></section>")


QUICK = [
    ("Your turn", ["Draw up to 5 cards. Say <b>critical</b> if 3+ Dead are in hand.",
                   "Play cards, move, loot, buy, attack, in any order.",
                   "End: 3+ Dead in hand = <b>out</b>. Otherwise discard down to 3 cards (Dead stay, not counted) and go again. Your turn also ends at the next Storm or Drop alarm."]),
    ("Move and loot", ["Base Move 1 + Move cards played. One adjacent tile per point.",
                       "Moving <b>into</b> a tile with a cube takes it: draw the top card of that loot deck into your hand. Hand cap 5; extra loot goes to your discard pile.",
                       "Gold cubes on your own tile can be taken without moving."]),
    ("Attack", ["Say <b>Attack</b>; the table pauses. Damage = Attack total &minus; 2 per tile of range (Base Attack 1 + cards).",
                "Put that many Dead cards in the target's <b>discard pile</b>. Then resume."]),
    ("Timers", ["<b>Storm (every 4 min):</b> pause, mark the whole outer ring. Moving into a storm tile = 1 Dead; ending your turn on one = 1 more.",
                "<b>Drop (every 2 min):</b> first player (rotates) places it. Then the others move it in turn order: 2p one player 3 tiles; 3p each 2 tiles; 4+ each 1 tile. Table puts one gold cube per player on it."]),
    ("Market", ["Any time on your turn, pay the cost printed on a <b>face-up</b> Market card with cards from your hand (never Dead).",
                "Paid cards <b>leave the game</b>. The bought card goes into your <b>hand</b> (hand cap 5)."]),

]


def reference():
    blocks = "".join(f"<div class='qr'><h3>{t}</h3><ul>" + "".join(f"<li>{x}</li>" for x in xs) + "</ul></div>" for t, xs in QUICK)
    copy = f"<div class='refcopy'><h1>QUICK REFERENCE</h1><div class='qrs'>{blocks}</div></div>"
    return f"<section class='page ref'>{copy}<div class='cutline'>cut here</div>{copy}</section>"


def tiles():
    # 50 of 100 tiles get a printed cube spot in a loot colour (14 Move, 26 Attack, 10 Heal ~ 6/11/4 per 21): put that colour cube on it
    rng = random.Random(7)
    cols = ["M"] * 14 + ["A"] * 26 + ["H"] * 10
    rng.shuffle(cols)
    flat = []
    for i, letter in enumerate("ABCDE"):
        spots = 10
        for n in range(20):
            t = tile_color([], letter)
            if n < spots:
                k = cols.pop()
                t = t.replace('<div class="hloots"></div>',
                              f'<div class="hloots"><span class="cspot" style="--type:{TYPE_COLOR[k]}"><span class="msym">{MSYM[k]}</span></span></div>')
            flat.append(t)
    return sheets(flat, 35, "tiles")


def minis():
    return ["<section class='page minis'>" + "<div class='mini'></div>" * 54 + "</section>"]


PAGE_CSS = """
* { box-sizing: border-box; margin: 0; }
body { font-family: Helvetica, Arial, sans-serif; color: #1b1f2a; }
.page { page-break-after: always; display: flex; flex-wrap: wrap; align-content: flex-start; justify-content: center; }
.cardsheet .page { width: 10in; margin: 0 auto; }
.cardsheet .page > .cc { margin: 0; outline: 1px dashed #aaa; }
.piecesheet .page { width: 10.4in; margin: 0 auto; }
.piecesheet .page.tiles { gap: 0.03in; }
h1 { font: 44pt "Bangers", Impact, sans-serif; letter-spacing: 3px; width: 100%; text-align: center; margin: 0.2in 0 0.15in; }
.cspot { width: 0.7in; height: 0.7in; border-radius: 50%; border: 4px dashed var(--type); background: rgba(255,255,255,.6);
         display: flex; align-items: center; justify-content: center; }
.cspot .msym { font-family: "Material Symbols Sharp"; font-size: 24pt; line-height: 1; color: var(--type);
               font-variation-settings: "FILL" 1, "wght" 700, "GRAD" 0, "opsz" 48; }
.slots { display: flex; gap: 0.2in; width: 100%; justify-content: center; margin: 0.1in 0 0.3in; }
.slot { width: 2.3in; height: 3.3in; border: 3px dashed #777; border-radius: 0.12in; display: flex; align-items: center; justify-content: center;
        font: 18pt "Bangers", Impact, sans-serif; letter-spacing: 2px; color: #777; text-align: center; }
.slot.deck { background: #e7e3da; }
.mrules { width: 100%; border: 1px solid #999; padding: 0.15in 0.25in; font-size: 13pt; margin-bottom: 0.3in; }
.mrules ul { padding-left: 0.25in; margin-top: 0.08in; } .mrules li { margin: 0.05in 0; }
.costs { width: 100%; border-collapse: collapse; font-size: 17pt; }
.costs th { text-align: left; padding: 0.1in 0.15in; border-bottom: 3px solid #1b1f2a; font: 16pt "Bangers", Impact, sans-serif; letter-spacing: 1px; }
.costs td { padding: 0.17in 0.15in; border-bottom: 1px solid #bbb; }
.costs td.cp { color: #666; font-size: 12pt; }
.pill { display: inline-block; color: #fff; font: 20pt "Bangers", Impact, sans-serif; letter-spacing: 1px; padding: 0.04in 0.18in; border-radius: 0.1in; border: 3px solid #15121c; }
.refcopy { width: 100%; height: 7.9in; }
.refcopy h1 { font-size: 34pt; margin: 0.05in 0 0.1in; }
.cutline { width: 100%; border-top: 2px dashed #888; text-align: center; font: 10pt Helvetica, Arial, sans-serif; color: #888; margin: 0.15in 0; }
.qrs { display: grid; grid-template-columns: 1fr 1fr; gap: 0.2in; width: 100%; margin-top: 0.1in; }
.qr { border: 2px solid #1b1f2a; border-radius: 0.1in; padding: 0.12in 0.18in; font-size: 11pt; break-inside: avoid; }
.qr h3 { font: 17pt "Bangers", Impact, sans-serif; letter-spacing: 1px; margin-bottom: 0.05in; }
.qr ul { padding-left: 0.2in; } .qr li { margin: 0.04in 0; line-height: 1.3; }
.minis { gap: 0.06in; }
.mini { width: 0.85in; height: 0.98in; clip-path: polygon(50% 0, 100% 25%, 100% 75%, 50% 100%, 0 75%, 0 25%); background: #7b3fc4; opacity: .6; }
"""


def build(name, size, body_pages, cls, extra_css=""):
    fonts = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bangers&family=Nunito:wght@700;900&display=block">'
             '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Sharp:opsz,wght,FILL,GRAD@48,700,1,0&display=block">')
    css = f"@page {{ size: {size}; margin: 0.25in 0; }}\n" + COMIC_CSS + PAGE_CSS + extra_css
    doc = (f'<!doctype html><html><head><meta charset="utf-8"><title>{name}</title>{fonts}<style>{css}</style></head>'
           f'<body class="{cls}">{"".join(body_pages)}</body></html>')
    html_path = os.path.abspath(os.path.join(OUT, name + ".html"))
    open(html_path, "w").write(doc)
    pdf_path = html_path.replace(".html", ".pdf")
    if os.path.exists(CHROME):
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=20000",
                        f"--print-to-pdf={pdf_path}", "file://" + html_path], check=True, capture_output=True)
    print("wrote", html_path)


def main():
    os.makedirs(OUT, exist_ok=True)
    base, loot, market, gold = decks()
    deads = [dead()] * 60
    cards = sheets(base, 16, "") + sheets(loot, 16, "") + sheets(market, 16, "") + sheets(gold, 16, "") + sheets(deads, 16, "")
    print(f"cards: base {len(base)} loot {len(loot)} market {len(market)} gold {len(gold)} dead {len(deads)} on {len(cards)} pages")
    build("last-deck-standing-v2-cards-11x17", "11in 17in", cards, "cardsheet")
    pieces = [market_mat(), reference()] + tiles() + minis()
    build("last-deck-standing-v2-pieces-11.5x17", "11.5in 17in", pieces, "piecesheet")


if __name__ == "__main__":
    main()

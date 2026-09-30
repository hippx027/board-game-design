"""Generate print-and-play sheets (HTML → PDF via headless Chrome) for Last Deck Standing.

Usage: python3 pnp_sheets.py
  writes ../pnp/last-deck-standing-pnp.{html,pdf}        (ink-saver: plain cards)
     and ../pnp/last-deck-standing-pnp-color.{html,pdf}  (full-colour comic style, see style-mockup-kaiju.html)
Quantities follow components-sheet.md (full 5-player box).
"""
import html
import os
import subprocess

OUT = os.path.join(os.path.dirname(__file__), "..", "pnp")
# Rarity follows Fortnite: Common gray, Rare blue, Epic purple, Legendary gold.
# Starting cards use the normal rarity colour (gray, common); the character is shown by name + symbol in the top bar.
PLAYERS = [(f"Player {i}", f"{i}") for i in range(1, 6)]  # characters now come from ability cards
RARITY = {1: ("#8a8f9c", "Common"), 2: ("#2f6fd0", "Rare"), 3: ("#7b3fc4", "Epic"), 4: ("#c98a00", "Legendary")}
ICON = {"A": "&#9876;", "M": "&#10140;", "H": "&#10010;", "D": "&#9760;"}  # crossed swords, arrow, cross, skull
TYPE = {"A": "Attack", "M": "Move", "H": "Heal"}
TEXT = {
    "A": "+{v} Attack this turn.",
    "M": "+{v} Move this turn.",
    "H": "Choose one:<br><b>Heal</b> &ndash; return up to {v} Dead card{s} from your hand to the supply, then remove this card from the game.<br><b>Shield</b> &ndash; +{v} Shield (max 4). Stays until damage uses it.",
}


def card_plain(kind, v, name=None, stripe=None, legendary=False, owner=None):
    color, tier = RARITY[v]
    if legendary:
        color, tier = "#c98a00", "Legendary"
    title = name or f"{TYPE[kind]} {v}"
    body = TEXT[kind].format(v=v, s="" if v == 1 else "s")
    band = f'<div class="band">{html.escape(owner.upper())}</div>' if owner else ""
    return (f'<div class="card{" owned" if owner else ""}" style="--c:{color}">{band}'
            f'<div class="top"><span class="val">{v}</span><span class="icon">{ICON[kind]}</span></div>'
            f'<div class="name">{html.escape(title)}</div><div class="tier">{"Starting deck" if owner else tier} &middot; {TYPE[kind]}</div>'
            f'<div class="text">{body}</div></div>')


# --- full-colour comic style -------------------------------------------------------
TYPE_COLOR = {"A": "#ff3b30", "M": "#9b4dff", "H": "#20c060"}
MSYM = {"A": "swords", "M": "sprint", "H": "medical_services", "D": "skull"}
COMIC_TEXT = {
    "A": "<b>+{v} Attack</b> this turn.",
    "M": "<b>+{v} Move</b> this turn.",
    "H": 'Choose one:<br><b class="hl">Heal:</b> remove up to {v} Dead from your hand, then remove this card.<br><b class="sh">Shield:</b> +{v} (max 4), stays until used.',
}


def comic(title, typ, icon, text, rarity_color=None, value=None, tag="", owner=None, cls=""):
    badge = f'<div class="badge" style="background:{rarity_color}">{value}</div>' if value is not None else ""
    own = f'<div class="owner">{html.escape(owner.upper())}</div>' if owner else ""
    tagc = rarity_color or "#15121c"
    return (f'<div class="cc {cls}" style="--type:{typ}">{badge}{own}<div class="frame">'
            f'<div class="title{" long" if len(title) > 11 else ""}">{html.escape(title)}</div>'
            f'<div class="art"><div class="plate"><span class="msym">{icon}</span></div></div>'
            f'<div class="text"><div>{text}</div></div></div><div class="tag" style="background:{tagc}">{tag}</div></div>')


def card_color(kind, v, name=None, stripe=None, legendary=False, owner=None):
    color, tier = RARITY[4] if legendary else RARITY[v]
    title = name or f"{TYPE[kind]} {v}"
    tag = "Starting deck" if owner else f"{tier} &middot; {TYPE[kind]}"
    return comic(title, TYPE_COLOR[kind], MSYM[kind], COMIC_TEXT[kind].format(v=v), color, v, tag, owner)


def dead_card_color():
    return comic("DEAD", "#2a2a33", "skull", "Can't be played. Stays in your hand.<br><b>3 in hand at end of turn = OUT.</b>",
                 tag="Dead &middot; different back", cls="dead")


# name: (title colour, burst colour 1, burst colour 2, epithet, pattern)
CHAR_THEME = {
    "Blaze":   ("#ff4d1a", "#ffb347", "#ff6a1a", "The Brawler", "burst"),
    "Shade":   ("#3d2c8d", "#2a2250", "#4b3fa0", "The Sniper", "night"),
    "Ember":   ("#d98e00", "#ffe066", "#f5b400", "The Scavenger", "burst"),
    "Tide":    ("#0097a7", "#4dd0e1", "#00a0b4", "The Runner", "waves"),
    "Nova":    ("#e91e63", "#ffc1dc", "#ff6fa5", "The Medic", "burst"),
    "Gale":    ("#546e7a", "#cfe0e8", "#90a4ae", "The Storm Chaser", "swirl"),
    "Vex":     ("#2e7d32", "#c6ff00", "#64dd17", "The Leech", "burst"),
    "Bastion": ("#455a64", "#b0bec5", "#78909c", "The Tank", "bricks"),
    "Brute":   ("#b71c1c", "#ff8a80", "#e53935", "The Heavy", "burst"),
    "Rig":     ("#f9a825", "#15121c", "#fdd835", "The Mechanic", "hazard"),
}


def char_card_color(icon, name, ability, text):
    col, b1, b2, epithet, pat = CHAR_THEME[name]
    card = comic(name, col, icon, f'<i class="epi">{epithet}</i><br><b>{ability}</b><br>{text}', tag=name.upper(), cls=f"char pat-{pat}")
    return card.replace('style="--type:', f'style="--b1:{b1}; --b2:{b2}; --type:', 1)


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


TILE_SET = [[], [], [], [], ["M"], ["A"], ["A"], ["H"], ["M", "A"], ["A", "A"], ["A", "H"], ["M", "M"],
            ["M", "A", "H"], ["A", "A", "H"], ["M", "A", "A"]]  # 6 Move / 11 Attack / 4 Heal
CUBE = {"M": "#8e44ec", "A": "#e53935", "H": "#43a047"}


def tile_color(icons, letter):
    loot = "".join(f'<span class="hloot" style="--type:{TYPE_COLOR[k]}"><span class="msym">{MSYM[k]}</span></span>' for k in icons)
    return (f'<div class="hexc"><div class="hin"><div class="hloots">{loot}</div>'
            f'<span class="hset">{letter}</span></div></div>')


def tile(icons, letter):
    dots = "".join(f'<span class="loot" style="background:{CUBE[k]}">{ICON[k]}</span>' for k in icons)
    return f'<div class="hex"><div class="hexin">{dots}</div><span class="set">{letter}</span></div>'


CHAR_ICON = {"Blaze": "local_fire_department", "Shade": "dark_mode", "Ember": "diamond", "Tide": "waves", "Nova": "star",
             "Gale": "cyclone", "Vex": "bolt", "Bastion": "fort", "Brute": "sports_mma", "Rig": "build"}


def main(style="plain"):
    os.makedirs(OUT, exist_ok=True)
    color = style == "color"
    card = card_color if color else card_plain
    cards = []
    for pname, sym in PLAYERS:
        cards += ([card("A", 1, "Strike", sym, owner=pname)] * 4 + [card("M", 1, "Dash", sym, owner=pname)] * 3
                  + [card("H", 1, "Patch Up", sym, owner=pname)] * 3)
    for k in "AMH":
        for v, n in (((1, 12), (2, 8), (3, 4)) if k == "A" else ((1, 9), (2, 6), (3, 3))):
            cards += [card(k, v)] * n
    for k in "AMH":
        cards += [card(k, 3, legendary=True)] * 2 + [card(k, 4, legendary=True)] * 2
    dead = [dead_card_color() if color else dead_card()] * 60
    tiles = []
    for letter in "ABCDE":
        tiles.append([(tile_color if color else tile)(t, letter) for t in TILE_SET])
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

    chars = [("&#9650;", "Blaze", "Point blank", "When you attack a player on your own tile, add 1 damage (before their Shield)."),
             ("&#9790;", "Shade", "Long shot", "When you attack an in-range player who isn't on your tile, add 1 damage (before their Shield)."),
             ("&#9670;", "Ember", "Scavenge", "After your normal loot, you may take 1 more cube from the same tile."),
             ("&#8776;", "Tide", "Runner", "Your Base Move starts at 2."),
             ("&#9733;", "Nova", "Field medic", "Your Base Move starts at 2. Each Heal card you use to heal removes up to 2 extra Dead cards from your hand."),
             ("&#9729;&#xFE0E;", "Gale", "Storm runner", "You take 1 less storm damage (none in rounds 1&ndash;6)."),
             ("&#9889;&#xFE0E;", "Vex", "Siphon", "When your attack puts 2+ Dead cards on a player after their Shield, return 1 Dead card from your hand to the supply."),
             ("&#9632;", "Bastion", "Armored", "You start the game with 1 Shield point. Your Base Shield is still 0."),
             ("&#9679;", "Brute", "Heavy hitter", "Your Base Attack starts at 2."),
             ("&#9881;", "Rig", "Tinkerer", "Your first upgrade of the game costs 3 instead of 4.")]
    char_cards = [char_card_color(CHAR_ICON[nm], nm, ab, tx) for sym, nm, ab, tx in chars] if color else \
                 [f'<div class="card char"><div class="sym">{sym}</div><div class="name">{nm}</div>'
                  f'<div class="tier">Character</div><div class="ab">{ab}</div><div class="text">{tx}</div></div>'
                  for sym, nm, ab, tx in chars]
    body = []
    body += pages(char_cards, 9, "cards")
    body += pages(cards, 9, "cards")
    body += pages(dead, 9, "cards")
    body += [f'<section class="page tiles"><h2>Loot tiles &mdash; set {"ABCDE"[i]}</h2><div class="hexgrid">' + "".join(t) + "</div></section>"
             for i, t in enumerate(tiles)]
    body.append('<section class="page misc"><h2>Stat trackers</h2>' + tracker * 5 + "</section>")
    howto = ('<div class="howto"><b>How to use the round track</b><ul>'
             '<li><b>Start:</b> put the marker on 1.</li>'
             '<li><b>Advance:</b> move the marker up 1 at the start of each of the start player\'s turns after the first '
             '(if the start player is out, move it when play reaches their seat).</li>'
             '<li><b>Storm, rounds 1&ndash;6:</b> at the end of your turn place <b>1</b> storm marker. '
             'End your turn on a storm tile: <b>1</b> Dead card to your discard pile.</li>'
             '<li><b>Storm, round 7+ (STORM FAST):</b> place <b>2</b> markers per turn; storm damage is <b>2</b>. '
             'Storm damage ignores Shield.</li>'
             '<li><b>DROP rounds (3, 5, 7, 9, 11):</b> before the start player\'s upkeep, a supply drop lands &mdash; '
             'one drop per starting player (2 players: rounds 3 and 5; 3 players: 3, 5, 7; and so on).</li>'
             '<li><b>Endgame:</b> once every tile is marked, everyone takes storm damage every turn. There is no round limit.</li>'
             '</ul></div>')
    body.append(f'<section class="page misc"><h2>Round track</h2><div class="rounds">{rounds}</div>{howto}'
                f'<h2>Storm markers (cut out, or use glass beads)</h2><div class="minis">{storm}</div></section>')
    body.append('<section class="page misc"><h2>Reference cards</h2>' + ('<div class="ref">' + qr_html + "</div>") * 2 + "</section>")

    css = """
@page { size: letter; margin: 0.2in 0.25in; }
* { box-sizing: border-box; }
body { margin: 0; font-family: Helvetica, Arial, sans-serif; color: #1b1f2a; }
.page { page-break-after: always; }
.cards { display: grid; grid-template-columns: repeat(3, 2.5in); grid-auto-rows: 3.5in; gap: 0 0.05in; justify-content: center; }
.card { position: relative; border: 1px dashed #999; padding: 0.14in; overflow: hidden; border-top: 0.16in solid var(--c); }
.card.owned { border-top: 0; padding-top: 0; }
.card .band { background: var(--c); color: #fff; font-weight: 700; font-size: 10pt; letter-spacing: .12em; text-align: center;
              margin: 0 -0.14in 0.06in; padding: 0.04in 0; }
.card .top { display: flex; justify-content: space-between; align-items: center; }
.card .val { font-size: 34pt; font-weight: 700; color: var(--c); }
.card .icon { font-size: 28pt; }
.card .icon.big { font-size: 60pt; margin: 0 auto; }
.card .name { font-size: 15pt; font-weight: 700; margin-top: 0.05in; }
.card .tier { font-size: 8pt; text-transform: uppercase; letter-spacing: .08em; color: #555; }
.card .text { font-size: 9.5pt; line-height: 1.35; margin-top: 0.1in; }
.card.char { border-top: 0.16in solid #1b1f2a; text-align: center; }
.card.char .sym { font-size: 54pt; margin-top: 0.15in; }
.card.char .name { font-size: 20pt; }
.card.char .ab { font-size: 12pt; font-weight: 700; margin-top: 0.12in; }
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
.howto { border: 1px solid #999; padding: 0.1in 0.15in; margin: -0.15in 0 0.25in; font-size: 10pt; }
.howto ul { margin: 0.05in 0 0; padding-left: 0.2in; } .howto li { margin: 0.03in 0; }
.ref { border: 1px solid #999; padding: 0.15in; margin-bottom: 0.2in; font-size: 10pt; }
.ref p { margin: 0.04in 0; }
"""
    fonts = ""
    if color:
        css += COMIC_CSS
        fonts = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bangers&family=Nunito:wght@700;900&display=block">'
                 '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Sharp:opsz,wght,FILL,GRAD@48,700,1,0&display=block">')
    doc = (f'<!doctype html><html><head><meta charset="utf-8"><title>Last Deck Standing PnP</title>{fonts}'
           f'<style>{css}</style></head><body>{"".join(body)}</body></html>')
    html_path = os.path.abspath(os.path.join(OUT, "last-deck-standing-pnp" + ("-color" if color else "") + ".html"))
    open(html_path, "w").write(doc)
    pdf_path = html_path.replace(".html", ".pdf")
    chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    if os.path.exists(chrome):
        subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=15000",
                        f"--print-to-pdf={pdf_path}", "file://" + html_path],
                       check=True, capture_output=True)
    print(f"{style}: cards {len(cards)} + {len(dead)} dead · tiles {sum(map(len, tiles))} · wrote {html_path}")


COMIC_CSS = """
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.cc { --ink:#15121c; position: relative; width: 2.5in; height: 3.5in; background: #3b3550; padding: 0.09in;
      outline: 1px dashed #aaa; outline-offset: -1px; display: flex; flex-direction: column; font-family: "Nunito", sans-serif; }
.cc .frame { flex: 1; background: #fff8ea; border: 3px solid var(--ink); border-radius: 0.1in; display: flex; flex-direction: column; overflow: hidden; }
.cc .title { font: 19pt/1 "Bangers", Impact, sans-serif; letter-spacing: 1px; color: #fff; text-align: center; background: var(--type);
             border-bottom: 3px solid var(--ink); padding: 0.06in 0.08in 0.05in 0.42in; white-space: nowrap;
             -webkit-text-stroke: 1px var(--ink); text-shadow: 2px 2px 0 var(--ink); }
.cc .title.long { font-size: 15pt; }
.cc .art { flex: 1; min-height: 1.2in; border-bottom: 3px solid var(--ink); display: flex; align-items: center; justify-content: center;
           background: repeating-conic-gradient(from 0deg at 50% 50%, var(--type) 0 10deg, color-mix(in srgb, var(--type) 72%, #fff) 10deg 20deg); }
.cc .plate { width: 70%; height: 72%; background: #fff; border: 3px solid var(--ink); border-radius: 0.1in; box-shadow: 3px 3px 0 var(--ink);
             display: flex; align-items: center; justify-content: center; transform: rotate(-2deg); }
.cc .msym { font-family: "Material Symbols Sharp"; font-size: 50pt; line-height: 1; color: var(--type);
            font-variation-settings: "FILL" 1, "wght" 700, "GRAD" 0, "opsz" 48;
            text-shadow: 2px 0 var(--ink), -2px 0 var(--ink), 0 2px var(--ink), 0 -2px var(--ink),
                         1.4px 1.4px var(--ink), -1.4px 1.4px var(--ink), 1.4px -1.4px var(--ink), -1.4px -1.4px var(--ink); }
.cc .text { padding: 0.06in 0.08in 0.2in; font: 700 8.5pt/1.3 "Nunito", sans-serif; color: var(--ink); text-align: center; min-height: 0.75in;
            display: flex; flex-direction: column; justify-content: center; }
.cc .text b { font-weight: 900; } .cc .text .hl { color: #129a4a; } .cc .text .sh { color: #1e6fe0; }
.cc .badge { position: absolute; top: 0.03in; left: 0.03in; width: 0.5in; height: 0.5in; border-radius: 50%; border: 3px solid var(--ink);
             color: #fff; font: 22pt/1 "Bangers", Impact, sans-serif; display: flex; align-items: center; justify-content: center;
             -webkit-text-stroke: 1px var(--ink); box-shadow: 2px 2px 0 var(--ink); z-index: 2; }
.cc .owner { position: absolute; top: 0.47in; right: 0.14in; background: var(--ink); color: #fff; font: 9pt "Bangers", Impact, sans-serif;
             letter-spacing: 1px; padding: 1px 6px; border-radius: 4px; z-index: 2; }
.cc .tag { position: absolute; bottom: 0.13in; left: 50%; transform: translateX(-50%) rotate(-2deg); color: #fff; border: 2.5px solid var(--ink);
           border-radius: 5px; padding: 1px 9px; font: 10pt "Bangers", Impact, sans-serif; letter-spacing: 1px; white-space: nowrap;
           -webkit-text-stroke: .5px var(--ink); box-shadow: 2px 2px 0 var(--ink); }
.cc.dead .frame { background: #3a3a46; } .cc.dead .text { color: #f3f3f3; }
.cc.dead .art { background: repeating-linear-gradient(135deg, #2a2a33 0 12px, #34343f 12px 24px); }
.cc.dead .plate { background: #e8e8f0; } .cc.dead .msym { color: #2a2a33; text-shadow: none; }
.cc.dead .title { padding-left: 0.08in; }
.cc.char .art { background: repeating-conic-gradient(from 0deg at 50% 50%, var(--b1) 0 10deg, var(--b2) 10deg 20deg); }
.cc.char .msym { color: var(--type); }
.cc.char .tag { background: var(--type) !important; }
.cc.char .epi { font-style: normal; font: 11pt "Bangers", Impact, sans-serif; letter-spacing: 1px; color: var(--type); }
.cc.pat-night .art { background: radial-gradient(circle at 20% 25%, #fff 0 1.5px, transparent 2px) 0 0 / 22px 22px,
                                 radial-gradient(circle at 70% 60%, #d9d2ff 0 1px, transparent 1.5px) 0 0 / 17px 17px,
                                 linear-gradient(160deg, var(--b1), var(--b2)); }
.cc.pat-night .msym { color: #b9a8ff; }
.cc.pat-waves .art { background: radial-gradient(circle at 50% 0, transparent 9px, var(--b2) 10px 13px, transparent 14px) 0 0 / 28px 16px,
                                 linear-gradient(180deg, var(--b1), var(--type)); }
.cc.pat-swirl .art { background: repeating-radial-gradient(circle at 50% 50%, var(--b1) 0 8px, var(--b2) 8px 16px); }
.cc.pat-bricks .art { background: linear-gradient(0deg, #37474f 2px, transparent 2px) 0 0 / 100% 18px,
                                  linear-gradient(90deg, #37474f 2px, transparent 2px) 0 0 / 36px 36px,
                                  linear-gradient(90deg, #37474f 2px, transparent 2px) 18px 18px / 36px 36px, var(--b1); }
.cc.pat-hazard .art { background: repeating-linear-gradient(135deg, var(--b1) 0 14px, var(--b2) 14px 28px); }
.cc.char .title { padding-left: 0.08in; }
h2 { font: 20pt "Bangers", Impact, sans-serif; letter-spacing: 1px; }
.hexc { --ink:#15121c; position: relative; width: 1.9in; height: 2.19in; background: var(--ink);
        clip-path: polygon(50% 0, 100% 25%, 100% 75%, 50% 100%, 0 75%, 0 25%); }
.hexc .hin { position: absolute; inset: 5px; clip-path: polygon(50% 0, 100% 25%, 100% 75%, 50% 100%, 0 75%, 0 25%);
             background: radial-gradient(circle at 50% 50%, rgba(21,18,28,.12) 1px, transparent 1.3px) 0 0 / 8px 8px,
                         repeating-conic-gradient(from 0deg at 50% 50%, #f3e2b3 0 10deg, #ead29a 10deg 20deg);
             display: flex; align-items: center; justify-content: center; }
.hloots { display: flex; flex-wrap: wrap; gap: 0.06in; justify-content: center; width: 1.35in; }
.hloot { width: 0.5in; height: 0.5in; border-radius: 50%; background: #fff; border: 3px solid var(--ink); box-shadow: 2px 2px 0 var(--ink);
         display: flex; align-items: center; justify-content: center; }
.hloot .msym { font-family: "Material Symbols Sharp"; font-size: 21pt; line-height: 1; color: var(--type);
               font-variation-settings: "FILL" 1, "wght" 700, "GRAD" 0, "opsz" 48;
               text-shadow: 1.2px 0 var(--ink), -1.2px 0 var(--ink), 0 1.2px var(--ink), 0 -1.2px var(--ink); }
.hset { position: absolute; bottom: 0.16in; font: 12pt "Bangers", Impact, sans-serif; letter-spacing: 1px; color: var(--ink); }
"""


if __name__ == "__main__":
    main("plain")
    main("color")

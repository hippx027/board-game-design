"""Last Deck Standing — seeded Monte Carlo simulator for Playtest Rules v1.

System evidence only: bots measure length, seat balance, stalls and economy.
They do not measure fun or rule clarity.

Usage:
  python3 lds_sim.py --players 3 5 8 10 --runs 500 --seed 42 --out results.json
  python3 lds_sim.py --players 8 --tiles-total 70      # fixed board size variant
"""
import argparse
import json
import random
from collections import Counter, deque
from statistics import mean, median

RULES_VERSION = "v1 (2026-09-29)"
SIM_VERSION = "lds-sim 0.1"

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)]
GROUP = {"A": "A", "M": "M", "H": "H", "S": "H"}  # Heal and Shield both upgrade Shield
STAT = {"A": "atk", "M": "mov", "H": "shd"}
BASE = {"atk": 1, "mov": 1, "shd": 0}
MAX_ROUNDS = 150


def hexdist(a, b):
    dq, dr = a[0] - b[0], a[1] - b[1]
    return (abs(dq) + abs(dr) + abs(dq + dr)) // 2


def nbrs(h):
    return [(h[0] + d[0], h[1] + d[1]) for d in DIRS]


# Bot profiles: weights for scoring a candidate turn.
PROFILES = {
    "random": None,
    "aggressive": dict(att=3.0, loot=1.0, danger=0.5, heal=1.5, shield=0.5, up={"A": 3, "M": 1, "H": 1}),
    "balanced": dict(att=2.0, loot=1.5, danger=1.0, heal=2.0, shield=1.0, up={"A": 2, "M": 1, "H": 2}),
    "brawler": dict(att=3.0, loot=0.5, danger=0.0, heal=1.5, shield=0.5, up={"A": 3, "M": 1, "H": 1}, retreat=False),
    "skirmisher": dict(att=3.0, loot=1.0, danger=1.5, heal=1.5, shield=0.5, up={"A": 3, "M": 2, "H": 1}),
    "cautious": dict(att=1.5, loot=1.2, danger=2.0, heal=2.5, shield=1.5, up={"A": 1, "M": 1, "H": 3}),
}


def supply_deck(kind, rng, size=12, values=None):
    if values:  # counts of value-1, value-2, value-3 cards
        vals = [v + 1 for v, c in enumerate(values) for _ in range(c)]
    else:
        vals = [1] * (size // 2) + [2] * (size // 3) + [3] * (size - size // 2 - size // 3)
    if kind == "H":  # alternate Heal / Shield within each value
        cards = [("H" if i % 2 == 0 else "S", v) for i, v in enumerate(vals)]
    else:
        cards = [(kind, v) for v in vals]
    rng.shuffle(cards)
    return cards


class Player:
    def __init__(self, seat, profile, rng):
        self.seat, self.profile = seat, profile
        self.stats = dict(BASE)
        self.shield = 0
        self.draw = [("A", 1)] * 4 + [("M", 1)] * 3 + [("H", 1)] * 3
        rng.shuffle(self.draw)
        self.discard, self.hand = [], []
        self.pos = None
        self.alive = True
        self.upgrades = Counter()

    def draw_to(self, n, rng):
        while len(self.hand) < n:
            if not self.draw:
                if not self.discard:
                    return
                self.draw, self.discard = self.discard, []
                rng.shuffle(self.draw)
            self.hand.append(self.draw.pop())


class Game:
    def __init__(self, n, profiles, rng, tiles_per_player=15, tiles_total=None, deck_size=12, storm="choose", upgrade_pay="remove", upgrade_cost=4, push=None,
                 values=None, place_reverse=False, storm_per_turn=1, loot="d4-1", drop_rounds=(), elim_loot=0, retreat=True, kill_upgrade=False, pile=0, pile_move_cost=0, bundle_cap=99, heal_discard=False, elim_timing="upkeep",
                 play_all=False, sticky_dead=False, merged_heal=False, heal_keep=False,
                 min_start=0, hold=0, grace=0, storm_sched=None, dmg_sched=None, heal_no_attack=False, heal_no_move=False, hold_no_heal=False,
                 heal_values=None):
        self.hold_no_heal = hold_no_heal
        self.heal_no_attack, self.heal_no_move = heal_no_attack, heal_no_move
        self.storm_sched = storm_sched or {1: 1}
        self.dmg_sched = dmg_sched or {1: 1}
        self.grace = grace
        self.min_start, self.hold = min_start, hold
        self.storm_tiles = set()
        self.play_all, self.sticky_dead, self.merged_heal, self.heal_keep = play_all, sticky_dead, merged_heal, heal_keep
        self.elim_timing = elim_timing
        self.heal_discard = heal_discard
        self.bundle_cap = bundle_cap
        self.pile, self.pile_move_cost = pile, pile_move_cost
        self.piles = {}
        self.retreat, self.kill_upgrade = retreat, kill_upgrade
        self.loot = loot
        self.drop_rounds, self.elim_loot = set(drop_rounds), elim_loot
        self.drops = {}
        self.drop_count = 0
        self.gold = [(rng.choice("AMHS"), v) for v in [2] * 6 + [3] * 6]
        rng.shuffle(self.gold)
        self.storm_per_turn = storm_per_turn
        self.storm, self.upgrade_pay, self.upgrade_cost, self.push = storm, upgrade_pay, upgrade_cost, push
        self.round = 0
        self.rng = rng
        self.n = n
        total = tiles_total or tiles_per_player * n
        self.tiles = {}
        self.build_board(total)
        self.decks = {k: supply_deck(k, rng, deck_size, values) for k in "AMH"}
        if heal_values:
            self.decks["H"] = supply_deck("H", rng, values=heal_values)
        if merged_heal:
            self.decks["H"] = [("H", v) for _, v in self.decks["H"]]
        self.display = {k: self.decks[k].pop() for k in "AMH"}
        self.players = [Player(i, profiles[i], rng) for i in range(n)]
        for p in (reversed(self.players) if place_reverse else self.players):
            p.pos = self.place_pawn(p)
            p.draw_to(5, rng)
        self.m = Counter()
        self.first_attack_round = None
        self.supply_out_round = {}

    # --- setup -----------------------------------------------------------
    def build_board(self, total):
        rng = self.rng
        self.tiles[(0, 0)] = self.roll_loot()
        while len(self.tiles) < total:
            frontier = list({nb for h in self.tiles for nb in nbrs(h) if nb not in self.tiles})
            h = rng.choice(frontier)
            self.tiles[h] = self.roll_loot()

    def roll_loot(self):
        rng = self.rng
        if self.loot == "tiles":
            if not getattr(self, "tile_pool", None):
                self.tile_pool = [[], [], [], [], ["M"], ["A"], ["H"], ["H"], ["M", "A"], ["A", "H"], ["H", "M"],
                                  ["M", "M"], ["M", "A", "H"], ["A", "A", "H"], ["M", "A", "H"]]
                rng.shuffle(self.tile_pool)
            return list(self.tile_pool.pop())
        n = {"d4-1": lambda: rng.randrange(4),
             "coin": lambda: rng.randrange(2),
             "d6": lambda: [0, 0, 0, 1, 1, 2][rng.randrange(6)],
             "d4-2": lambda: max(0, rng.randrange(1, 5) - 2)}[self.loot]()
        return [["M", "M", "A", "A", "H", "H"][rng.randrange(6)] for _ in range(n)]

    def place_pawn(self, p):
        # Spread out: pick the loot-richest hex among those farthest from placed pawns.
        placed = [q.pos for q in self.players if q.pos is not None]
        cands = list(self.tiles)
        if placed and self.min_start:
            cands = [h for h in cands if min(hexdist(h, x) for x in placed) >= self.min_start] or cands
        if placed and p.profile in ("aggressive", "brawler"):
            near = min(min(hexdist(h, x) for x in placed) for h in cands)
            return self.rng.choice([h for h in cands if min(hexdist(h, x) for x in placed) == near])
        if placed:
            best = max(min(hexdist(h, x) for x in placed) for h in cands)
            cands = [h for h in cands if min(hexdist(h, x) for x in placed) >= best - 1]
        top = max(len(self.tiles[h]) for h in cands)
        return self.rng.choice([h for h in cands if len(self.tiles[h]) == top])

    # --- helpers ---------------------------------------------------------
    def alive(self):
        return [p for p in self.players if p.alive]

    def path_len(self, a, b):
        seen, q = {a: 0}, deque([a])
        while q:
            h = q.popleft()
            if h == b:
                return seen[h]
            for nb in nbrs(h):
                if nb in self.tiles and nb not in seen:
                    seen[nb] = seen[h] + 1
                    q.append(nb)
        return 0

    def reachable(self, start, steps):
        seen = {start: 0}
        q = deque([start])
        while q:
            h = q.popleft()
            if seen[h] == steps:
                continue
            for nb in nbrs(h):
                if nb in self.tiles and nb not in seen:
                    seen[nb] = seen[h] + 1
                    q.append(nb)
        return list(seen)

    def connected_without(self, h):
        rest = [t for t in self.tiles if t != h]
        if not rest:
            return False
        seen, q = {rest[0]}, deque([rest[0]])
        while q:
            for nb in nbrs(q.popleft()):
                if nb in self.tiles and nb != h and nb not in seen:
                    seen.add(nb)
                    q.append(nb)
        return len(seen) == len(rest)

    def edge_tiles(self, allow_pawns=False):
        pawns = {p.pos for p in self.alive()}
        out = [h for h in self.tiles if (allow_pawns or h not in pawns) and h not in self.drops
               and any(nb not in self.tiles for nb in nbrs(h))]
        if self.storm in ("connected", "center"):
            out = [h for h in out if self.connected_without(h)]
        return out

    def push_active(self):
        if self.push is None:
            return False
        if self.push == "auto":
            return not self.edge_tiles()
        return self.round >= int(self.push)

    # --- turn ------------------------------------------------------------
    def play_turn(self, p, rnd):
        rng = self.rng
        p.shield = p.stats["shd"]
        p.draw_to(5, rng)
        if sum(1 for c in p.hand if c[0] == "D") >= 3:
            if self.elim_timing == "upkeep":
                self.eliminate(p, rnd)
                return
            self.m["last_chance_turns"] += 1
        self.m["turns"] += 1
        self.current = p

        self.do_upgrades(p)
        plan = self.choose_plan(p)
        plays, dest, target, loot_kind = plan

        played = [c for grp in plays for c in grp]
        for c in played:
            p.hand.remove(("H", c[1]) if c[0] == "X" else c)
        mov = p.stats["mov"] + sum(v for k, v in played if k == "M")
        atk = p.stats["atk"] + sum(v for k, v in played if k == "A")
        heal = sum(v for k, v in played if k == "H")
        p.shield += sum(v for k, v in played if k in "SX")
        self.m["cards_played"] += len(played)
        self.m["plays_used"] += len(plays)
        self.m["play_slots"] += 2

        healed = 0
        for _ in range(heal):
            if ("D", 0) in p.hand:
                p.hand.remove(("D", 0))
                healed += 1
            elif self.heal_discard and ("D", 0) in p.discard:
                p.discard.remove(("D", 0))
                healed += 1
        self.m["dead_healed"] += healed
        if heal and not healed:
            self.m["wasted_heals"] += 1

        p_start = p.pos
        p.pos = dest
        if target is not None and self.round <= self.grace:
            target = None
        if self.heal_no_attack and any(c[0] == "H" for c in played):
            target = None
        if target is not None:
            dmg = atk - hexdist(dest, target.pos)
            if dmg > 0:
                absorbed = min(target.shield, dmg)
                target.shield -= absorbed
                dealt = dmg - absorbed
                target.discard += [("D", 0)] * dealt
                if dealt:
                    target.last_hit_by = p
                self.m["attacks"] += 1
                self.m["dead_dealt"] += dealt
                self.m["dead_absorbed"] += absorbed
                if dealt and self.first_attack_round is None:
                    self.first_attack_round = rnd
        if loot_kind == "P":
            pool = self.piles.pop(dest)
            self.rng.shuffle(pool)
            got = [c for c in pool if c[0] != "D"][:self.pile]  # Dead cards are redrawn
            p.discard += got
            self.m["pile_loots"] += 1
            self.m["pile_cards"] += len(got)
        elif loot_kind == "G":
            cards = self.drops[dest]
            p.discard.append(cards.pop(max(range(len(cards)), key=lambda i: cards[i][1])))
            self.m["drop_loots"] += 1
            if not cards:
                del self.drops[dest]
        elif loot_kind is not None:
            self.tiles[dest].remove(loot_kind)
            self.take_loot(p, loot_kind, rnd)

        if self.retreat and PROFILES[p.profile] is not None and PROFILES[p.profile].get("retreat", True):
            left = mov - self.path_len(p_start, dest) - (self.pile_move_cost if loot_kind == "P" else 0)
            if left > 0:
                foes = [q for q in self.alive() if q is not p]
                p.pos = min(self.reachable(dest, left), key=lambda h: sum(
                    max(0, q.stats["atk"] + 2 - hexdist(h, q.pos) - p.shield) for q in foes) + self.rng.random() * 0.01)
                self.m["retreats"] += p.pos != dest

        if self.elim_timing == "end" and sum(1 for c in p.hand if c[0] == "D") >= 3:
            self.eliminate(p, rnd)  # hand (with its Dead cards) goes into the loot pile / supply
            p.hand = []
            return

        spent = [("H", c[1]) if c[0] == "X" else c for c in played
                 if c[0] != "H" or self.heal_keep]
        if self.sticky_dead:
            live = sorted((c for c in p.hand if c[0] != "D"), key=lambda c: (c[0] == "H", c[1]), reverse=True)
            if self.hold_no_heal:
                live = [c for c in live if c[0] != "H"] + [c for c in live if c[0] == "H"]
                kept = [c for c in live if c[0] != "H"][:self.hold]
            else:
                kept = live[:self.hold]
            p.discard += spent + [c for c in live if c not in kept or live.count(c) > kept.count(c)][:len(live) - len(kept)]
            p.hand = [c for c in p.hand if c[0] == "D"] + kept
            self.m["held"] += len(kept)
        else:
            p.discard += spent + p.hand
            p.hand = []

        sched = lambda d: d[max(r for r in d if r <= self.round)]
        n_storm = sched(self.storm_sched) if self.storm == "flip" else self.storm_per_turn
        for _ in range(n_storm):
            self.storm_step()
        if self.storm == "flip" and p.pos in self.storm_tiles:
            dmg = sched(self.dmg_sched)
            p.discard += [("D", 0)] * dmg
            self.m["storm_hits"] += dmg

    def storm_step(self):
        p = self.current
        if self.storm == "flip":
            outer = [h for h in self.tiles if h not in self.storm_tiles and
                     any(nb not in self.tiles or nb in self.storm_tiles for nb in nbrs(h))]
            if outer:
                self.storm_tiles.add(self.pick_storm_tile(p, outer))
            else:
                self.m["storm_skipped"] += 1
            return
        push = self.push_active()
        edges = self.edge_tiles(allow_pawns=push)
        if edges:
            h = self.pick_storm_tile(p, edges)
            self.tiles.pop(h)
            self.piles.pop(h, None)
            for q in self.alive():
                if q.pos == h:  # pushed pawn moves to an adjacent tile of its owner's choosing
                    self.m["pushes"] += 1
                    opts = [nb for nb in nbrs(h) if nb in self.tiles]
                    foes = [x.pos for x in self.alive() if x is not q]
                    q.pos = max(opts, key=lambda t: min((hexdist(t, f) for f in foes), default=0) + self.rng.random() * 0.01)
        else:
            self.m["storm_skipped"] += 1

    def take_loot(self, p, kind, rnd):
        self.m["loots"] += 1
        if self.display[kind] is not None:
            card = self.display[kind]
            self.display[kind] = self.decks[kind].pop() if self.decks[kind] else None
        else:
            card = None
        if card is None:
            self.m["loot_empty"] += 1
            self.supply_out_round.setdefault(kind, rnd)
            return
        p.discard.append(card)

    def supply_drop(self):
        alive = self.alive()
        placer = alive[self.drop_count % len(alive)]
        self.drop_count += 1
        far = [h for h in self.tiles if h not in self.drops and hexdist(h, placer.pos) >= 3] or \
              [h for h in self.tiles if h not in self.drops]
        if not far:
            return
        spot = min(far, key=lambda h: hexdist(h, placer.pos) + self.rng.random() * 0.01)
        i = alive.index(placer)
        for q in alive[i + 1:] + alive[:i]:  # clockwise nudges: move 1 hex toward yourself or pass
            opts = [nb for nb in nbrs(spot) if nb in self.tiles and nb not in self.drops]
            best = min(opts, key=lambda h: hexdist(h, q.pos), default=None)
            if best is not None and hexdist(best, q.pos) < hexdist(spot, q.pos):
                spot = best
        self.drops[spot] = [self.gold.pop() for _ in range(2) if self.gold]
        self.m["drops"] += 1

    def eliminate(self, p, rnd):
        p.alive = False
        killer = getattr(p, "last_hit_by", None)
        if self.elim_loot and killer is not None and killer.alive:
            pool = [c for c in p.draw + p.discard + p.hand if c[0] != "D"]
            self.rng.shuffle(pool)
            killer.discard += pool[:self.elim_loot]
            self.m["elim_loot_cards"] += len(pool[:self.elim_loot])
        if self.kill_upgrade and killer is not None and killer.alive:
            for st in ("atk", "shd", "mov"):  # +1 to a stat of the killer's choice
                if killer.stats[st] < 4:
                    killer.stats[st] += 1
                    self.m["kill_upgrades"] += 1
                    break
        self.m["eliminations"] += 1
        if self.pile:
            if p.pos in self.tiles:
                self.piles.setdefault(p.pos, []).extend(p.draw + p.discard + p.hand)
        elif p.pos in self.tiles:
            self.tiles[p.pos] += ["M", "A", "H"]

    # --- bot decisions ---------------------------------------------------
    def do_upgrades(self, p):
        w = PROFILES[p.profile]
        for g in sorted("AMH", key=lambda g: -(w["up"][g] if w else self.rng.random())):
            stat = STAT[g]
            while p.stats[stat] < 4:
                cards = sorted([c for c in p.hand if c[0] != "D" and GROUP[c[0]] == g], key=lambda c: c[1])
                if sum(v for _, v in cards) < self.upgrade_cost:
                    break
                if w is None and self.rng.random() < 0.5:
                    break
                pay, tot = [], 0
                for c in sorted(cards, key=lambda c: -c[1]):  # fewest cards that reach 4
                    pay.append(c)
                    tot += c[1]
                    if tot >= self.upgrade_cost:
                        break
                for c in pay:
                    p.hand.remove(c)
                    if self.upgrade_pay == "discard":
                        p.discard.append(c)
                self.m["overpay"] += tot - self.upgrade_cost
                p.stats[stat] += 1
                p.upgrades[g] += 1
                self.m[f"upgrade_{g}"] += 1

    def play_options(self, p):
        if self.play_all:
            opts = {()}
            for c in p.hand:
                if c[0] == "D":
                    continue
                alts = [(c,)]
                if self.merged_heal and c[0] == "H":
                    alts.append((("X", c[1]),))  # Heal card spent as Shield
                opts |= {tuple(sorted(o + a)) for o in opts for a in alts}
            from collections import Counter as _C
            have = _C(c for c in p.hand if c[0] != "D")
            def ok(o):
                need = _C(("H", v) if k == "X" else (k, v) for k, v in o)
                return all(have[x] >= n for x, n in need.items())
            opts = {o for o in opts if ok(o)}
            return [tuple((c,) for c in o) for o in opts]
        return self.play_options_limited(p)

    def play_options_limited(self, p):
        """All legal sets of up to 2 plays. Upgraded groups play as one bundle."""
        units = []
        bundled = set()
        for c in p.hand:
            if c[0] == "D":
                continue
            g = GROUP[c[0]]
            if p.stats[STAT[g]] > BASE[STAT[g]]:
                if g not in bundled:
                    bundled.add(g)
                    grp = sorted((x for x in p.hand if x[0] != "D" and GROUP[x[0]] == g), key=lambda c: -c[1])
                    units.append(tuple(grp[:self.bundle_cap]))
                    units += [(x,) for x in grp[self.bundle_cap:]]
            else:
                units.append((c,))
        opts = [()]
        for i in range(len(units)):
            opts.append((units[i],))
            for j in range(i + 1, len(units)):
                opts.append((units[i], units[j]))
        return opts

    def choose_plan(self, p):
        rng = self.rng
        foes = [q for q in self.alive() if q is not p]
        opts = self.play_options(p)
        w = PROFILES[p.profile]
        if w is None:
            plays = rng.choice(opts)
            flat = [c for g in plays for c in g]
            mov = p.stats["mov"] + sum(v for k, v in flat if k == "M")
            atk = p.stats["atk"] + sum(v for k, v in flat if k == "A")
            dest = rng.choice(self.reachable(p.pos, mov))
            inr = [q for q in foes if atk - hexdist(dest, q.pos) > 0]
            tgt = rng.choice(inr) if inr else None
            loot = "P" if dest in self.piles else "G" if dest in self.drops else (rng.choice(self.tiles[dest]) if self.tiles[dest] else None)
            return plays, dest, tgt, loot

        dead_in_hand = sum(1 for c in p.hand if c[0] == "D")
        if self.heal_discard:
            dead_in_hand += sum(1 for c in p.discard if c[0] == "D")
        best, best_s = None, -1e9
        reach_cache = {}
        for plays in opts:
            flat = [c for g in plays for c in g]
            mov = p.stats["mov"] + sum(v for k, v in flat if k == "M")
            atk = p.stats["atk"] + sum(v for k, v in flat if k == "A")
            heal = sum(v for k, v in flat if k == "H")
            if self.heal_no_move and heal:
                mov = 0
            shd = p.shield + sum(v for k, v in flat if k in "SX")
            if mov not in reach_cache:
                reach_cache[mov] = self.reachable(p.pos, mov)
            base_s = w["heal"] * min(heal, dead_in_hand)
            if self.elim_timing == "end" and dead_in_hand >= 3 and dead_in_hand - heal < 3:
                base_s += 100  # survive the end-of-turn elimination check + w["shield"] * (shd - p.shield) * 0.5
            for dest in reach_cache[mov]:
                s = base_s
                tgt, tdmg = None, 0
                for q in foes:
                    if self.heal_no_attack and heal:
                        break
                    d = atk - hexdist(dest, q.pos) - q.shield
                    # prefer targets already close to elimination
                    val = d + 0.3 * sum(1 for c in q.discard + q.draw if c[0] == "D") / 5
                    if d > 0 and val > tdmg:
                        tgt, tdmg = q, val
                s += w["att"] * tdmg
                loot = None
                if dest in self.piles and (self.pile_move_cost == 0 or
                                           dest in self.reachable(p.pos, max(0, mov - self.pile_move_cost))):
                    loot = "P"
                    s += w["loot"] * (1 + self.pile * 0.8)
                elif dest in self.drops:
                    loot = "G"
                    s += w["loot"] * 3.5
                elif self.tiles[dest]:
                    loot = max(self.tiles[dest], key=lambda k: (self.display[k] or ("x", 0))[1])
                    s += w["loot"] * (1 + (self.display[loot] or ("x", 0))[1] * 0.5)
                danger = sum(max(0, q.stats["atk"] + 2 - hexdist(dest, q.pos) - shd) for q in foes)
                if dest in self.storm_tiles:
                    danger += 1.5
                if self.hold and not self.hold_no_heal:  # value of Heal cards left in hand to keep for later
                    s += w["heal"] * 0.5 * max(0, sum(1 for c in p.hand if c[0] == "H")
                                                   - sum(1 for c in flat if c[0] in "HX"))
                s -= w["danger"] * danger
                s += rng.random() * 0.01
                if s > best_s:
                    best_s, best = s, (plays, dest, tgt, loot)
        return best

    def pick_storm_tile(self, p, edges):
        if self.storm == "center":  # closing circle: remove the edge tile farthest from the board's centre
            cq = sum(h[0] for h in self.tiles) / len(self.tiles)
            cr = sum(h[1] for h in self.tiles) / len(self.tiles)
            far = lambda h: (abs(h[0] - cq) + abs(h[1] - cr) + abs(h[0] - cq + h[1] - cr)) / 2
            return max(edges, key=lambda h: far(h) + self.rng.random() * 0.01)
        w = PROFILES[p.profile]
        if w is None:
            return self.rng.choice(edges)
        foes = [q for q in self.alive() if q is not p]
        # Remove tiles far from me and near foes, preferring loot-rich ones (deny loot).
        def score(h):
            me = hexdist(h, p.pos)
            near_foe = min((hexdist(h, q.pos) for q in foes), default=0)
            return me - near_foe + len(self.tiles[h]) * 0.5 + self.rng.random() * 0.01
        return max(edges, key=score)

    # --- run -------------------------------------------------------------
    def run(self):
        rnd = 0
        while len(self.alive()) > 1 and rnd < MAX_ROUNDS:
            rnd += 1
            self.round = rnd
            if rnd in self.drop_rounds and self.gold:
                self.supply_drop()
            for p in self.players:
                if p.alive and len(self.alive()) > 1:
                    self.play_turn(p, rnd)
        winner = self.alive()[0] if len(self.alive()) == 1 else None
        return dict(
            rounds=rnd,
            stalled=winner is None,
            winner_seat=winner.seat if winner else None,
            winner_profile=winner.profile if winner else None,
            first_attack_round=self.first_attack_round,
            tiles_left=len(self.tiles),
            supply_out_round=self.supply_out_round,
            **self.m,
        )


def campaign(n, runs, seed, population, **kw):
    rng = random.Random(seed)
    results = []
    for i in range(runs):
        if population == "mixed":
            prof = [rng.choice(["aggressive", "balanced", "cautious"]) for _ in range(n)]
        else:
            prof = [population] * n
        results.append(Game(n, prof, random.Random(rng.random()), **kw).run())
    done = [r for r in results if not r["stalled"]]
    seat = Counter(r["winner_seat"] for r in done)
    tot = lambda k: sum(r.get(k, 0) for r in results)
    rounds = [r["rounds"] for r in done]
    out = dict(
        players=n, runs=runs, seed=seed, population=population, config=kw,
        stall_rate=round(1 - len(done) / runs, 3),
        rounds_mean=round(mean(rounds), 1) if rounds else None,
        rounds_median=median(rounds) if rounds else None,
        rounds_p10_p90=[sorted(rounds)[len(rounds) // 10], sorted(rounds)[len(rounds) * 9 // 10]] if rounds else None,
        turns_mean=round(tot("turns") / runs, 1),
        first_attack_round_median=median([r["first_attack_round"] for r in results if r["first_attack_round"]] or [0]),
        seat_win_rate={s: round(seat[s] / max(1, len(done)), 3) for s in range(n)},
        fair_share=round(1 / n, 3),
        profile_wins=dict(Counter(r["winner_profile"] for r in done)),
        upgrades_per_game={g: round(tot(f"upgrade_{g}") / runs, 2) for g in "AMH"},
        attacks_per_turn=round(tot("attacks") / max(1, tot("turns")), 2),
        dead_dealt_per_game=round(tot("dead_dealt") / runs, 1),
        shield_absorb_share=round(tot("dead_absorbed") / max(1, tot("dead_absorbed") + tot("dead_dealt")), 2),
        play_slot_use=round(tot("plays_used") / max(1, tot("play_slots")), 2),
        loot_empty_rate=round(tot("loot_empty") / max(1, tot("loots")), 2),
        supply_runs_out_pct={k: round(sum(1 for r in results if k in r["supply_out_round"]) / runs, 2) for k in "AMH"},
        drops_per_game=round(tot("drops") / runs, 1),
        drop_loots_per_game=round(tot("drop_loots") / runs, 1),
        last_chance_turns_per_game=round(tot("last_chance_turns") / runs, 1),
        dead_healed_per_game=round(tot("dead_healed") / runs, 1),
        storm_hits_per_game=round(tot("storm_hits") / runs, 1),
        pushes_per_game=round(tot("pushes") / runs, 1),
        storm_skipped_per_game=round(tot("storm_skipped") / runs, 1),
        tiles_left_at_end_mean=round(mean(r["tiles_left"] for r in results), 1),
    )
    return out


def parse_sched(x):
    return {int(r): int(v) for r, v in (kv.split(":") for kv in x.split(","))} if x else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--players", type=int, nargs="+", default=[3, 5, 8, 10])
    ap.add_argument("--runs", type=int, default=500)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--population", default="mixed", choices=["mixed", *PROFILES])
    ap.add_argument("--tiles-per-player", type=int, default=15)
    ap.add_argument("--tiles-total", type=int, default=None)
    ap.add_argument("--deck-size", type=int, default=12)
    ap.add_argument("--storm", default="choose", choices=["choose", "center", "connected", "flip"])
    ap.add_argument("--upgrade-cost", type=int, default=4)
    ap.add_argument("--push", default=None, help="auto | round number")
    ap.add_argument("--upgrade-pay", default="remove", choices=["remove", "discard"])
    ap.add_argument("--values", type=lambda x: [int(v) for v in x.split(",")], default=None, help="e.g. 6,4,2")
    ap.add_argument("--place-reverse", action="store_true")
    ap.add_argument("--storm-per-turn", type=int, default=1)
    ap.add_argument("--loot", default="d4-1", choices=["d4-1", "coin", "d6", "d4-2", "tiles"])
    ap.add_argument("--drop-rounds", type=lambda x: [int(v) for v in x.split(",")], default=[])
    ap.add_argument("--elim-loot", type=int, default=0)
    ap.add_argument("--pile", type=int, default=0, help="loot-pile first pick size (0 = kill cache)")
    ap.add_argument("--bundle-cap", type=int, default=99)
    ap.add_argument("--heal-discard", action="store_true")
    ap.add_argument("--kill-upgrade", action="store_true")
    ap.add_argument("--elim-timing", default="upkeep", choices=["upkeep", "end"])
    ap.add_argument("--play-all", action="store_true")
    ap.add_argument("--sticky-dead", action="store_true")
    ap.add_argument("--merged-heal", action="store_true")
    ap.add_argument("--heal-keep", action="store_true", help="Heal cards used to heal are discarded, not removed")
    ap.add_argument("--min-start", type=int, default=0)
    ap.add_argument("--hold", type=int, default=0)
    ap.add_argument("--grace", type=int, default=0, help="no attacks in rounds 1..N")
    ap.add_argument("--storm-sched", default=None, help="round:markers per turn, e.g. 1:0,5:1,9:2")
    ap.add_argument("--dmg-sched", default=None, help="round:storm damage, e.g. 1:1,9:2")
    ap.add_argument("--heal-no-attack", action="store_true")
    ap.add_argument("--heal-no-move", action="store_true")
    ap.add_argument("--hold-no-heal", action="store_true")
    ap.add_argument("--heal-values", type=lambda x: [int(v) for v in x.split(",")], default=None, help="Heal deck counts of value 1,2,3")
    ap.add_argument("--out")
    a = ap.parse_args()
    kw = dict(tiles_per_player=a.tiles_per_player, tiles_total=a.tiles_total, deck_size=a.deck_size,
              storm=a.storm, upgrade_pay=a.upgrade_pay,
              upgrade_cost=a.upgrade_cost, push=a.push,
              values=a.values, place_reverse=a.place_reverse, storm_per_turn=a.storm_per_turn, loot=a.loot,
              drop_rounds=a.drop_rounds, elim_loot=a.elim_loot,
              pile=a.pile, bundle_cap=a.bundle_cap, heal_discard=a.heal_discard, kill_upgrade=a.kill_upgrade,
              elim_timing=a.elim_timing, play_all=a.play_all, sticky_dead=a.sticky_dead,
              merged_heal=a.merged_heal, heal_keep=a.heal_keep,
              min_start=a.min_start, hold=a.hold, grace=a.grace,
              storm_sched=parse_sched(a.storm_sched), dmg_sched=parse_sched(a.dmg_sched),
              heal_no_attack=a.heal_no_attack, heal_no_move=a.heal_no_move, hold_no_heal=a.hold_no_heal, heal_values=a.heal_values)
    res = dict(rules_version=RULES_VERSION, simulation_version=SIM_VERSION,
               campaigns=[campaign(n, a.runs, a.seed, a.population, **kw) for n in a.players])
    s = json.dumps(res, indent=1)
    if a.out:
        open(a.out, "w").write(s)
    print(s)


if __name__ == "__main__":
    main()

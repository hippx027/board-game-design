"""Last Deck Standing — realtime (v2) Monte Carlo simulator.

Models rulebook-v2-draft.md: no rounds, everyone plays turns at once at their own
pace, a table timer drives storm rings and gold drops. System evidence only: bots
can't say whether realtime is fun, only whether it ends, who it favours, and how
the economy (loot, Market, deck thinning) behaves.

Time model: all events run on a "play clock" in seconds. Pauses (attacks, storm, drops)
freeze the play clock, so they only add to wall-clock length. A turn has three events:
  start  draw, market, heal, move (loot cubes on every tile passed, into the hand)
  attack half way through the turn's duration (resolution depends on --attack-opt)
  end    discard, elimination check, storm damage, next turn starts

Attack options:  none  resolves instantly, no pause (baseline)
                 A     table pauses for --pause-attack seconds, resolves with fresh state
                 B     no pause; the target may respond by playing a Move card to dodge
                 C     simultaneous: attack resolves --delay-attack seconds later, range
                       rechecked (a target who moved away in the window is missed)

Usage:
  python3 lds_rt.py --players 2 3 4 5 --runs 200 --attack-opt A
"""
import argparse
import heapq
import json
import random
from collections import Counter, deque
from statistics import mean, median

DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)]
KINDS = "MAH"


def hexdist(a, b):
    dq, dr = a[0] - b[0], a[1] - b[1]
    return (abs(dq) + abs(dr) + abs(dq + dr)) // 2


def nbrs(h):
    return [(h[0] + d[0], h[1] + d[1]) for d in DIRS]


PROFILES = {  # att: want hits, loot: want cubes, danger: avoid enemies, heal: heal at this many Dead
    "aggressive": dict(att=3.0, loot=1.0, danger=0.3, heal_at=2, buy="AMH"),
    "balanced": dict(att=2.0, loot=1.5, danger=1.0, heal_at=2, buy="AHM"),
    "cautious": dict(att=1.2, loot=1.5, danger=2.0, heal_at=1, buy="HAM"),
}

# Market costs: bought card -> cards paid (counted by number, any value)
COSTS = {
    ("A", 2): "AAM", ("M", 2): "MMH", ("H", 2): "HAM",
    ("A", 3): "AAAM", ("M", 3): "MMMH", ("H", 3): "HHAM",
}


CHEAP_COSTS = {  # one card cheaper than COSTS
    ("A", 2): "AA", ("M", 2): "MH", ("H", 2): "HA",
    ("A", 3): "AAM", ("M", 3): "MMH", ("H", 3): "HHA",
}


def loot_deck(kind, rng, ones, weak=False):
    size, threes = {"M": (12, 4), "A": (16, 6), "H": (10, 4)}[kind]
    vals = [3] * threes + [2] * (size - threes)
    if weak:  # weaker loot: no 3s, half the cards are 1s
        vals, ones = [2] * size, True
    if ones:  # playtest variant: half the 2s become 1s
        twos = [i for i, v in enumerate(vals) if v == 2]
        for i in twos[: len(twos) // 2]:
            vals[i] = 1
    d = [(kind, v) for v in vals]
    rng.shuffle(d)
    return d


def market_deck(rng):
    d = ([("A", 2)] * 6 + [("M", 2)] * 4 + [("H", 2)] * 4 +
         [("A", 3)] * 3 + [("M", 3)] * 2 + [("H", 3)] * 2)
    rng.shuffle(d)
    return d


class Player:
    def __init__(self, seat, profile, speed, team, rng):
        self.seat, self.profile, self.speed, self.team = seat, profile, speed, team
        self.draw = [("A", 1)] * 4 + [("M", 1)] * 4 + [("H", 1)] * 2
        rng.shuffle(self.draw)
        self.discard, self.hand = [], []
        self.pos = None
        self.alive = True
        self.plan = None
        self.turns = 0

    def dead(self):
        return sum(1 for c in self.hand if c[0] == "D")

    def draw_to(self, n, rng):
        while len(self.hand) < n:
            if not self.draw:
                if not self.discard:
                    return
                self.draw, self.discard = self.discard, []
                rng.shuffle(self.draw)
            self.hand.append(self.draw.pop())


class Game:
    def __init__(self, n, rng, a):
        self.a, self.rng, self.n = a, rng, n
        self.t = 0.0           # play clock
        self.pause = 0.0       # total paused seconds
        self.m = Counter()
        self.heap, self.seq = [], 0
        tpp = 15 if n <= 3 else (12 if n == 4 else 10)
        self.tiles = {(0, 0)}
        while len(self.tiles) < tpp * n:
            fr = list({nb for h in self.tiles for nb in nbrs(h) if nb not in self.tiles})
            top = max(sum(1 for x in nbrs(h) if x in self.tiles) for h in fr)  # compact, roundish board (the rules ask for one)
            self.tiles.add(rng.choice([h for h in fr if sum(1 for x in nbrs(h) if x in self.tiles) >= top - (1 if rng.random() < 0.25 else 0)]))
        self.rings = self.compute_rings()
        self.storm, self.rings_marked = set(), 0
        # cubes: tile -> list of kinds ("M","A","H","G")
        self.cubes = {}
        tl = sorted(self.tiles)
        for h in rng.sample(tl, int(len(tl) * a.start_cubes)):
            self.cubes[h] = [rng.choices(KINDS, weights=[6, 11, 4])[0]]
        self.decks = {k: loot_deck(k, rng, a.loot_ones, a.loot_weak) for k in KINDS}
        self.gold = [(k, v, "g") for k in KINDS for v in (3, 3, 3, 3, 4, 4, 4, 4)]  # 24 cards, tagged gold
        self.piles = {}  # tile -> gold cards left by eliminated players, looted first
        rng.shuffle(self.gold)
        self.market_deck = market_deck(rng)
        self.market = [self.market_deck.pop() for _ in range(a.market_slots)]
        names = list(PROFILES)
        self.teams = a.teams if n >= 2 * a.teams else 0
        self.players = []
        for i in range(n):
            team = (i % self.teams) if self.teams else i
            self.players.append(Player(i, names[i % 3] if a.mix else a.profile, rng.uniform(0.7, 1.3), team, rng))
        zone = tl
        if a.bus:  # battle bus: a spinner on the centre tile picks a line; pawns start on it (2-3p) or within 1 tile of it (4+)
            d = rng.choice(DIRS[::2])
            line = {(d[0] * k, d[1] * k) for k in range(-40, 41)}
            slack = 0 if n <= 3 else 1
            zone = [h for h in tl if min(hexdist(h, x) for x in line) <= slack] or tl
        for p in self.players:
            placed = [q.pos for q in self.players if q.pos]
            c = [h for h in zone if not placed or min(hexdist(h, x) for x in placed) >= max(a.start_gap, 1)] or [h for h in zone if h not in placed] or tl
            p.pos = rng.choice(c)
            p.draw_to(5, rng)
        self.next_drop, self.next_storm = a.drop_interval, a.storm_interval
        self.drop_placer = 0
        self.stream = {}       # team -> members rotation (mode A)
        self.rot = Counter()

    # --- board ---
    def compute_rings(self):
        ring, k = {}, 1
        cur = {h for h in self.tiles if any(nb not in self.tiles for nb in nbrs(h))}
        while cur:
            for h in cur:
                ring[h] = k
            k += 1
            cur = {nb for h in cur for nb in nbrs(h) if nb in self.tiles and nb not in ring}
        return ring

    def reach(self, start, steps):
        dist, par, q = {start: 0}, {start: None}, deque([start])
        while q:
            h = q.popleft()
            if dist[h] == steps:
                continue
            for nb in nbrs(h):
                if nb in self.tiles and nb not in dist:
                    dist[nb], par[nb] = dist[h] + 1, h
                    q.append(nb)
        return dist

    def alive(self):
        return [p for p in self.players if p.alive]

    def enemies(self, p):
        return [q for q in self.alive() if q.team != p.team]

    # --- events ---
    def push(self, t, kind, p=None):
        self.seq += 1
        heapq.heappush(self.heap, (t, self.seq, kind, p))

    def wall(self):
        return self.t + self.pause

    def run(self):
        a = self.a
        if a.team_mode == "A" and self.teams:
            for tm in range(self.teams):
                mem = [p for p in self.players if p.team == tm]
                self.push(0.0, "start", mem[0])
        else:
            for p in self.players:
                self.push(p.speed * 3, "start", p)
        self.push(a.drop_interval, "drop")
        self.push(a.storm_interval, "storm")
        while self.heap:
            t, _, kind, p = heapq.heappop(self.heap)
            if t + self.pause > a.max_time:
                self.m["stalled"] = 1
                if a.debug_stall:
                    import sys
                    print("STALL", [(q.seat, q.team, q.alive, q.pos in self.storm, sum(1 for c in q.hand if c[0] == "D"), len(q.hand), len(q.draw), len(q.discard)) for q in self.players], "rings", self.rings_marked, "tiles", len(self.tiles), file=sys.stderr)
                break
            self.t = t
            if p is not None and not p.alive:
                if kind in ("start", "attack", "end") and self.teams and a.team_mode == "A":
                    self.advance_team(p)
                continue
            getattr(self, "ev_" + kind)(p)
            if len({q.team for q in self.alive()}) <= 1:
                break
        w = {q.team for q in self.alive()}
        winner = None
        if len(w) == 1:
            winner = next(q for q in self.alive())
        return winner

    def advance_team(self, p):
        mem = [q for q in self.players if q.team == p.team and q.alive]
        if mem:
            self.rot[p.team] += 1
            self.push(self.t, "start", mem[self.rot[p.team] % len(mem)])

    # --- storm and drop ---
    def ev_storm(self, _):
        a = self.a
        self.pause += a.storm_pause
        self.rings_marked += 1
        self.storm |= {h for h, r in self.rings.items() if r == self.rings_marked}
        self.m["storm_rings"] += 1
        if self.rings_marked < max(self.rings.values()):
            self.push(self.t + a.storm_interval, "storm")

    def ev_drop(self, _):
        a = self.a
        self.pause += a.drop_pause
        al = self.alive()
        if not al or not self.gold:
            return
        first = al[self.drop_placer % len(al)]
        self.drop_placer += 1
        ok = [h for h in self.tiles if h not in self.storm and self.rings[h] > 1] or list(self.tiles)
        spot = min(ok, key=lambda h: (hexdist(h, first.pos), self.rng.random()))
        if a.drop_moves == "scaled":  # 2p: one mover, 3 tiles; 3p: two movers, 2 tiles each; 4+: every other player, 1 tile
            movers, steps = (1, 3) if self.n <= 2 else (2, 2) if self.n == 3 else (self.n - 1, 1)
        else:
            movers, steps = 1, 3
        for k in range(movers):  # movers follow the placer in turn order; the next drop's placer is the first mover, as before
            mv = al[(self.drop_placer + k) % len(al)]
            if mv is not first or len(al) == 1:
                spot = min(self.reach(spot, steps), key=lambda h: (hexdist(h, mv.pos), self.rng.random()))
        k = min(self.n, self.gold_left())
        if k > 0:
            self.cubes.setdefault(spot, []).extend(["G"] * k)
        for _ in range(a.cube_refresh):
            self.cubes.setdefault(self.rng.choice(sorted(self.tiles)), []).append(
                self.rng.choices(KINDS, weights=[6, 11, 4])[0])
        self.m["drops"] += 1
        self.push(self.t + a.drop_interval, "drop")

    # --- bot turn ---
    def gold_left(self):
        return len(self.gold) + sum(len(v) for v in self.piles.values()) - sum(c.count("G") for c in self.cubes.values())

    def take(self, p, kind, pos=None):
        if kind == "G":
            if self.piles.get(pos):
                c = self.piles[pos].pop()
            elif self.gold:
                c = self.gold.pop()
            else:
                return False
        else:
            if not self.decks[kind]:
                self.m["loot_empty_" + kind] += 1
                return False
            c = self.decks[kind].pop()
            self.m["drawn_" + kind] += 1
        cap = self.a.loot_cap
        if cap and len(p.hand) >= cap:
            p.discard.append(c)  # hand full: overflow goes to the discard pile
            self.m["loot_overflow"] += 1
        else:
            p.hand.append(c)
        self.m["loots"] += 1
        return True

    def buy(self, p):
        a, prof = self.a, PROFILES[p.profile]
        bought = 0
        while True:
            opts = []
            for i, c in enumerate(self.market):
                need = Counter(COSTS[c])
                if a.pay_any:  # wildcard payment: the same number of cards, any type (Heals stay home while hurt)
                    pool = [x for x in p.hand if x[0] != "D" and not (x[0] == "H" and p.dead() >= prof["heal_at"])]
                    if len(pool) >= sum(need.values()):
                        opts.append((c[1], -prof["buy"].index(c[0]), i))
                    continue
                if p.dead() >= prof["heal_at"] and need["H"]:
                    continue
                have = Counter(x[0] for x in p.hand if x[0] != "D")
                if all(have[k] >= n for k, n in need.items()):
                    opts.append((c[1], -prof["buy"].index(c[0]), i))
            if not opts:
                break
            _, _, i = max(opts)
            card = self.market[i]
            pays = []
            if a.pay_any:
                pool = [x for x in p.hand if x[0] != "D" and not (x[0] == "H" and p.dead() >= prof["heal_at"])]
                pays = sorted(pool, key=lambda x: (x[1], x[0] == card[0]))[: len(COSTS[card])]
            else:
                for k, n in Counter(COSTS[card]).items():
                    pays += sorted((x for x in p.hand if x[0] == k), key=lambda x: x[1])[:n]
            if True:
                for x in pays:
                    p.hand.remove(x)  # paid cards leave the game (or go to the discard pile with --buy-pays discard)
                    if a.buy_pays == "discard":
                        p.discard.append(x)
            (p.hand if a.buy_to == "hand" else p.discard).append(card)
            self.market[i] = self.market_deck.pop() if self.market_deck else None
            self.market = [c for c in self.market if c]
            self.m["buys"] += 1
            bought += 1
            if not self.market:
                break
        return bought

    def heal(self, p):
        prof = PROFILES[p.profile]
        used = 0
        while p.dead() >= prof["heal_at"]:
            h = sorted((c for c in p.hand if c[0] == "H"), key=lambda c: -c[1])
            if not h:
                break
            c = h[0]
            p.hand.remove(c)
            for _ in range(min(c[1], p.dead())):
                p.hand.remove(("D", 0))
            self.m["heals"] += 1
            used += 1
        return used

    def ev_start(self, p):
        a, rng = self.a, self.rng
        prof = PROFILES[p.profile]
        p.turns += 1
        self.m["turns"] += 1
        p.draw_to(5, rng)
        if p.dead() >= a.elim:
            self.m["critical"] += 1
        acts = (self.buy(p) if a.buy_timing == "start" else 0) + self.heal(p)
        # movement planning: free base move 1 if --base-one, plus Move cards in hand
        mcards = sorted((c for c in p.hand if c[0] == "M"), key=lambda c: c[1])
        bm = 1 if a.base_one else 0
        reach = self.reach(p.pos, bm + sum(c[1] for c in mcards))
        atk = (1 if a.base_one else 0) + sum(c[1] for c in p.hand if c[0] == "A")
        foes = self.enemies(p)
        # best loot along shortest paths: DP on BFS layers
        best = {p.pos: (2 * self.cubes.get(p.pos, []).count("G"), None)}
        for h in sorted(reach, key=lambda x: reach[x]):
            if h == p.pos:
                continue
            c = [(best[g][0], g) for g in nbrs(h) if g in reach and reach[g] == reach[h] - 1 and g in best]
            v, g = max(c)
            best[h] = (v + sum(2 if k == "G" else 1 for k in self.cubes.get(h, [])), g)
        stormy = p.dead() >= 2
        scores = []
        for h, d in reach.items():
            s = prof["loot"] * best[h][0]
            hit = 0
            for q in foes:
                dm = atk - self.a.range_cost * hexdist(h, q.pos)
                if dm > 0:
                    hit = max(hit, dm + (1.5 if q.dead() >= 2 else 0))
            s += prof["att"] * hit
            near = sum(1 for q in foes if hexdist(h, q.pos) <= 2)
            s -= prof["danger"] * near
            if a.storm_mode in ("enter", "both"):
                n_st, g = 0, h
                while g is not None and g != p.pos:
                    n_st += g in self.storm
                    g = best[g][1]
                s -= (3 if stormy else 1.2) * n_st
            if a.storm_mode in ("end", "both") and h in self.storm:
                s -= 6 if stormy else 2.5
            if not hit and foes and prof["att"] >= 2:  # approach
                s -= 0.3 * min(hexdist(h, q.pos) for q in foes)
            if not self.storm and self.rings_marked == 0:
                pass
            s -= 0.05 * d
            scores.append((s + rng.random() * 0.01, h))
        dest = max(scores)[1]
        dist = reach[dest]
        path = []
        g = dest
        while g is not None:
            path.append(g)
            g = best[g][1]
        path.reverse()
        # play Move cards covering the distance
        need, used = max(0, dist - bm), 0
        for c in mcards:
            if used >= need:
                break
            p.hand.remove(c)
            p.discard.append(c)
            used += c[1]
            acts += 1
        for h in path:
            for k in list(self.cubes.get(h, [])):
                if h == p.pos and k != "G":
                    continue  # regular cubes are only looted by moving into a tile; a drop under you is picked up
                if self.take(p, k, h):
                    self.cubes[h].remove(k)
            if a.storm_mode in ("enter", "both") and h != path[0] and h in self.storm:
                p.discard.append(("D", 0))  # 1 Dead per storm tile you move into
                self.m["storm_dead"] += 1
        p.pos = dest
        self.m["moved"] += dist
        dur = a.turn_base + a.sec_per_act * (acts + dist) + a.sec_per_act * len(path)
        dur *= p.speed * rng.uniform(0.8, 1.25)
        dur = max(dur, a.turn_floor)  # a turn can't end before the floor (sand timer)
        p.dur = dur
        self.push(self.t + dur * 0.5, "attack", p)

    def pick_target(self, p):
        a = self.a
        atk = (1 if a.base_one else 0) + sum(c[1] for c in p.hand if c[0] == "A")
        best = None
        for q in self.enemies(p):
            dm = atk - a.range_cost * hexdist(p.pos, q.pos)
            if dm > 0:
                sc = dm + (3 if q.dead() + dm >= 3 else 0) + (1 if q.dead() else 0)
                if not best or sc > best[0]:
                    best = (sc, q)
        return best[1] if best else None

    def ev_attack(self, p):
        a = self.a
        q = self.pick_target(p)
        if q is not None:
            if a.attack_opt == "A":
                self.pause += a.pause_attack
            if a.attack_opt == "C":
                p.plan = ("c", q.seat, self.snapshot_atk(p))
                self.push(self.t + a.delay_attack, "resolve", p)
            else:
                self.resolve(p, q)
        self.push(self.t + p.dur * 0.5, "end", p)

    def snapshot_atk(self, p):
        cards = [c for c in p.hand if c[0] == "A"]
        for c in cards:
            p.hand.remove(c)
            p.discard.append(c)
        return (1 if self.a.base_one else 0) + sum(c[1] for c in cards)

    def ev_resolve(self, p):
        kind, seat, atk = p.plan
        q = self.players[seat]
        if q.alive and p.alive:
            self.deal(p, q, atk)
        # (turn end event already queued)

    def resolve(self, p, q):
        a = self.a
        atk_cards = [c for c in p.hand if c[0] == "A"]
        atk = (1 if a.base_one else 0) + sum(c[1] for c in atk_cards)
        self.m["atk_total"] += atk
        self.m["atk_n"] += 1
        if a.attack_opt == "B":  # target's response: dodge with a Move card
            mv = sorted((c for c in q.hand if c[0] == "M"), key=lambda c: c[1])
            if mv and q.dead() >= 1:
                c = mv[-1]
                dist = self.reach(q.pos, c[1])
                outs = [h for h in dist if atk - a.range_cost * hexdist(p.pos, h) <= 0]
                if outs:
                    q.hand.remove(c)
                    q.discard.append(c)
                    q.pos = min(outs, key=lambda h: dist[h])
                    self.m["dodges"] += 1
                    if a.range_cost * hexdist(p.pos, q.pos) >= atk:
                        return
        for c in atk_cards:
            p.hand.remove(c)
            p.discard.append(c)
        self.deal(p, q, atk)

    def deal(self, p, q, atk):
        dm = atk - self.a.range_cost * hexdist(p.pos, q.pos)
        if dm <= 0:
            self.m["whiffs"] += 1
            return
        q.discard.extend([("D", 0)] * dm)
        self.m["attacks"] += 1
        self.m["dead_dealt"] += dm

    def ev_end(self, p):
        a = self.a
        if p.dead() >= a.elim:
            p.alive = False
            mine = [c for c in p.hand + p.draw + p.discard if len(c) == 3]  # their gold cards populate the pool first
            if mine:
                self.piles.setdefault(p.pos, []).extend(mine)
            k = min(max(self.a.elim_drop, len(mine)), self.gold_left() + len(mine))
            if k > 0:
                self.cubes.setdefault(p.pos, []).extend(["G"] * k)  # loot drop where the player fell
            self.m["elim_attack" if p.pos not in self.storm else "elim_storm"] += 1
            if "first_elim" not in self.m:
                self.m["first_elim"] = self.wall()
            if self.teams and a.team_mode == "A":
                self.advance_team(p)
            return
        if a.storm_mode in ("end", "both") and p.pos in self.storm:
            dmg = 1 + (self.rings_marked >= a.storm_double)
            p.discard.extend([("D", 0)] * dmg)
            self.m["storm_dead"] += dmg
        if a.buy_timing == "end":  # spend the cards you were about to discard
            self.buy(p)
        keep = sorted((c for c in p.hand if c[0] != "D"), key=lambda c: (c[0] != "H", c[1]))[: a.keep]
        keepset = Counter(keep)
        for c in list(p.hand):
            if c[0] == "D":
                continue
            if keepset[c] > 0:
                keepset[c] -= 1
            else:
                p.hand.remove(c)
                p.discard.append(c)
        if self.teams and a.team_mode == "A":
            self.advance_team(p)
        else:
            self.push(self.t + 0.5, "start", p)


def run_game(n, seed, a):
    rng = random.Random(seed)
    g = Game(n, rng, a)
    w = g.run()
    r = dict(n=n, wall=g.wall(), play=g.t, stalled=bool(g.m["stalled"]),
             winner_seat=w.seat if w else None, winner_profile=w.profile if w else None,
             winner_team=w.team if w else None, teams=g.teams, m=dict(g.m),
             speeds=[p.speed for p in g.players], turns=[p.turns for p in g.players],
             winner_speed_rank=None)
    if w:
        order = sorted(range(n), key=lambda i: g.players[i].speed)
        r["winner_speed_rank"] = order.index(w.seat)  # 0 = fastest
    return r


def summarize(rs):
    n = rs[0]["n"]
    done = [r for r in rs if not r["stalled"] and r["winner_seat"] is not None]
    w = sorted(r["wall"] for r in done)
    pct = lambda q: round(w[int(q * (len(w) - 1))] / 60, 1) if w else None
    out = dict(players=n, runs=len(rs), stalled=round(100 * sum(r["stalled"] for r in rs) / len(rs), 1),
               wall_min_p10_med_p90=(pct(0.1), pct(0.5), pct(0.9)),
               pause_pct=round(100 * mean((r["wall"] - r["play"]) / r["wall"] for r in done), 1) if done else None)
    if any(r.get("teams") for r in rs):
        out["teams"] = rs[0]["teams"]
        tw = Counter(r["winner_team"] for r in done)
        out["team_win%"] = [round(100 * tw.get(t, 0) / len(done), 1) for t in range(rs[0]["teams"])] if done else None
    out["seat_win%"] = [round(100 * sum(1 for r in done if r["winner_seat"] == s) / len(done), 1) for s in range(n)] if done else None
    pc = Counter(r["winner_profile"] for r in done)
    out["profile_win%"] = {k: round(100 * v / len(done), 1) for k, v in pc.items()}
    out["fastest_player_win%"] = round(100 * sum(1 for r in done if r["winner_speed_rank"] == 0) / len(done), 1) if done else None
    out["slowest_player_win%"] = round(100 * sum(1 for r in done if r["winner_speed_rank"] == n - 1) / len(done), 1) if done else None
    keys = ["turns", "attacks", "whiffs", "dodges", "loots", "buys", "heals", "drops", "storm_rings", "elim_attack", "elim_storm", "loot_overflow", "atk_total", "atk_n", "drawn_M", "drawn_A", "drawn_H", "loot_empty_M", "loot_empty_A", "loot_empty_H"]
    out["per_game"] = {k: round(mean(r["m"].get(k, 0) for r in rs), 1) for k in keys}
    fe = [r["m"]["first_elim"] / 60 for r in done if "first_elim" in r["m"]]
    out["first_elim_min_med"] = round(median(fe), 1) if fe else None
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--players", type=int, nargs="+", default=[3])
    ap.add_argument("--runs", type=int, default=200)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--attack-opt", default="A", choices=["none", "A", "B", "C"])
    ap.add_argument("--pause-attack", type=float, default=8)
    ap.add_argument("--delay-attack", type=float, default=5)
    ap.add_argument("--storm-interval", type=float, default=120)
    ap.add_argument("--storm-pause", type=float, default=15)
    ap.add_argument("--storm-double", type=int, default=3, help="storm damage becomes 2 once this many rings are marked")
    ap.add_argument("--drop-interval", type=float, default=120)
    ap.add_argument("--drop-moves", default="classic", choices=["classic", "scaled"], help="classic: one player moves the drop 3 tiles; scaled: by player count (2p 1x3, 3p 2x2, 4+ each other player x1)")
    ap.add_argument("--bus", action="store_true", help="spinner line: pawns start on a random line through the centre (2-3p) or within 1 tile of it (4+)")
    ap.add_argument("--start-gap", type=int, default=0, help="minimum tiles between starting pawns (0 = any free tile)")
    ap.add_argument("--market-slots", type=int, default=3, help="face-up Market cards")
    ap.add_argument("--buy-pays", default="leave", choices=["leave", "discard"], help="paid Market cards leave the game, or go to the discard pile")
    ap.add_argument("--buy-timing", default="start", choices=["start", "end"], help="bots buy at the start of their turn (before acting) or at the end with leftover cards")
    ap.add_argument("--buy-to", default="discard", choices=["discard", "hand"], help="where a bought Market card goes")
    ap.add_argument("--pay-any", action="store_true", help="Market costs are the same number of cards but any type")
    ap.add_argument("--drop-pause", type=float, default=10)
    ap.add_argument("--cube-refresh", type=int, default=0, help="regular cubes the table adds per drop (variant)")
    ap.add_argument("--start-cubes", type=float, default=0.5, help="cubes per tile at setup")
    ap.add_argument("--base-one", action="store_true", default=True, help="Base Move 1 and Base Attack 1 (designer locked this in)")
    ap.add_argument("--loot-ones", action="store_true", help="half the loot 2s become 1s")
    ap.add_argument("--elim", type=int, default=3, help="Dead cards in hand at end of turn that eliminate you")
    ap.add_argument("--storm-mode", default="both", choices=["enter", "end", "both"], help="enter: 1 Dead per storm tile you move into; end: ending your turn on one")
    ap.add_argument("--debug-stall", action="store_true")
    ap.add_argument("--loot-cap", type=int, default=5, help="hand size cap for looting; extra loot goes to the discard pile (0 = no cap)")
    ap.add_argument("--loot-weak", action="store_true", help="loot values 1 and 2 only (half 1s, half 2s)")
    ap.add_argument("--cheap-market", nargs="?", const="all", choices=["all", "two"], help="every Market cost is one card smaller (all), or only the value-2 cards (two)")
    ap.add_argument("--keep", type=int, default=3, help="cards a bot keeps at end of turn")
    ap.add_argument("--range-cost", type=int, default=2, help="damage lost per tile of range (v1: 1, now 2)")
    ap.add_argument("--elim-drop", type=int, default=2, help="gold cubes dropped where a player is eliminated")
    ap.add_argument("--turn-floor", type=float, default=0, help="minimum seconds per turn")
    ap.add_argument("--turn-base", type=float, default=20)
    ap.add_argument("--sec-per-act", type=float, default=5)
    ap.add_argument("--max-time", type=float, default=5400)
    ap.add_argument("--teams", type=int, default=0, help="number of teams (players split evenly)")
    ap.add_argument("--team-mode", default="A", choices=["A", "C"], help="A: members rotate one stream; C: all members play at once")
    ap.add_argument("--profile", default="balanced")
    ap.add_argument("--mix", action="store_true", help="mix aggressive/balanced/cautious across seats")
    ap.add_argument("--out")
    a = ap.parse_args()
    if a.cheap_market:
        COSTS.update({k: v for k, v in CHEAP_COSTS.items() if a.cheap_market == "all" or k[1] == 2})
    res = {}
    for n in a.players:
        rs = [run_game(n, a.seed * 1000 + i, a) for i in range(a.runs)]
        res[n] = summarize(rs)
        print(json.dumps(res[n]))
    if a.out:
        json.dump(res, open(a.out, "w"), indent=1)


if __name__ == "__main__":
    main()

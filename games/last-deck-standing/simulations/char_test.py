"""SIM-018: character stats + abilities. Run from sim/: python3 ../simulations/char_test.py"""
import sys, random, json
from collections import Counter
sys.path.insert(0, ".")
import lds_sim as L
BASE = dict(upgrade_pay="discard", upgrade_cost=4, loot="tiles", pile=5, play_all=True, sticky_dead=True, elim_timing="end",
            merged_heal=True, hold=5, storm="flip", storm_sched={1: 1, 7: 2}, dmg_sched={1: 1, 7: 2}, min_start=3,
            min_draw=2, drop_rule="inner", display_n=2, shield_persist=True, shield_cap=4, tile_mix="armory",
            deck_sizes=[24, 18, 18])
NAMES = list(L.CHARACTERS)
out = {}
for n in (2, 3, 4, 5):
    rng = random.Random(100 + n); wins = Counter(); seen = Counter(); rounds = []
    runs = 1500
    for _ in range(runs):
        chars = rng.sample(NAMES, n)
        prof = [rng.choice(["aggressive", "balanced", "cautious"]) for _ in range(n)]
        tp = {4: 12, 5: 10}.get(n, 15)
        g = L.Game(n, prof, random.Random(rng.random()), tiles_per_player=tp,
                   drop_rounds=tuple(3 + 2 * i for i in range(n)), characters=chars, **BASE)
        r = g.run(); rounds.append(r["rounds"])
        seen.update(chars)
        if r["winner_char"]: wins[r["winner_char"]] += 1
    rate = {c: round(wins[c] / seen[c], 3) for c in NAMES}
    out[n] = rate
    print(f"{n}p (fair {1/n:.2f}) median rounds={sorted(rounds)[runs//2]}: " + "  ".join(f"{c}={rate[c]:.2f}" for c in NAMES), flush=True)
json.dump(out, open("../simulations/char_results.json", "w"), indent=1)

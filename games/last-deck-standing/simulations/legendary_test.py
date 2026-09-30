"""SIM-022: Legendary (supply drop) card values. Run from sim/."""
import sys, random
from collections import Counter
sys.path.insert(0, ".")
import lds_sim as L
BASE = dict(upgrade_pay="discard", upgrade_cost=4, loot="tiles", pile=5, play_all=True, sticky_dead=True, elim_timing="end",
            merged_heal=True, hold=5, storm="flip", storm_sched={1: 1, 7: 2}, dmg_sched={1: 1, 7: 2}, min_start=3,
            drop_rule="inner", display_n=2, shield_persist=True, shield_cap=4, tile_mix="armory", deck_sizes=[24, 18, 18], end_limit=3)
VARIANTS = {"values 2,2,3,3 (current)": [2, 2, 3, 3], "values 3,3,3,3": [3, 3, 3, 3],
            "values 3,3,4,4": [3, 3, 4, 4], "values 4,4,4,4": [4, 4, 4, 4]}
for name, vals in VARIANTS.items():
    print("==", name, flush=True)
    for n in (2, 3, 4, 5):
        rng = random.Random(60 + n); runs = 500; wins = Counter(); seats = Counter(); rounds = []; turns = dl = 0; upg = 0; drop_winner = 0
        for _ in range(runs):
            prof = [rng.choice(["aggressive", "balanced", "cautious"]) for _ in range(n)]
            g = L.Game(n, prof, random.Random(rng.random()), tiles_per_player={4: 12, 5: 10}.get(n, 15),
                       drop_rounds=tuple(3 + 2 * i for i in range(n)), legendary_values=vals, **BASE)
            r = g.run(); rounds.append(r["rounds"]); wins[r["winner_profile"]] += 1; seats[r["winner_seat"]] += 1
            turns += r.get("turns", 0); dl += r.get("drop_loots", 0); upg += sum(r.get(f"upgrade_{k}", 0) for k in "AMH")
        T = sum(v for k, v in wins.items() if k)
        print(f"  {n}p rounds={sorted(rounds)[runs//2]} turns={turns/runs:.0f} dropLoots={dl/runs:.1f} upg={upg/runs:.1f} "
              f"seats={[round(seats[i]/runs,2) for i in range(n)]} " + " ".join(f"{k[:4]}={wins[k]/T:.2f}" for k in ["aggressive", "balanced", "cautious"]), flush=True)

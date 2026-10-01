"""SIM-027: storm reworks. Usage: python3 storm_test.py <players>"""
import os, random, sys
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sim"))
import lds_sim as L
CORE = dict(upgrade_pay="discard", upgrade_cost=4, loot="tiles", pile=5, play_all=True, sticky_dead=True, elim_timing="end",
            merged_heal=True, hold=5, min_start=3, drop_rule="inner", display_n=2, shield_persist=True, shield_cap=4,
            tile_mix="armory", deck_sizes=[24, 18, 18], end_limit=3, no_refill=True, base_shd_max=3, split_attack=True)
FLIP = dict(storm="flip", storm_sched={1: 1, 7: 2}, dmg_sched={1: 1, 7: 2})
VARIANTS = {
    "current: markers, edge or touching": dict(FLIP, storm_mode="any"),
    "A: remove edge tiles (no damage, push-off r8)": dict(storm="connected", push="8"),
    "B: mark, then remove marked edges": dict(FLIP, storm_mode="markremove"),
    "C: ring by ring": dict(FLIP, storm_mode="rings"),
}
n = int(sys.argv[1])
for name, kw in VARIANTS.items():
    rng = random.Random(2700 + n); runs = 400
    wins, seats = Counter(), Counter(); rounds = []; turns = storm = dealt = pushes = removed = 0
    for _ in range(runs):
        prof = [rng.choice(["aggressive", "balanced", "cautious"]) for _ in range(n)]
        r = L.Game(n, prof, random.Random(rng.random()), tiles_per_player={4: 12, 5: 10}.get(n, 15),
                   drop_rounds=tuple(3 + 2 * i for i in range(n)), **CORE, **kw).run()
        rounds.append(r["rounds"]); wins[r["winner_profile"]] += 1; seats[r["winner_seat"]] += 1
        turns += r.get("turns", 0); storm += r.get("storm_hits", 0); dealt += r.get("dead_dealt", 0)
        pushes += r.get("pushes", 0); removed += r.get("tiles_removed", 0)
    T = sum(v for k, v in wins.items() if k)
    print(f"{n}p | {name:46s} | stall={sum(1 for x in rounds if x >= 150)/runs:.2f} rounds={sorted(rounds)[runs//2]} "
          f"p90={sorted(rounds)[int(runs*.9)]} turns={turns/runs:.0f} stormDead={storm/runs:.0f} attackDead={dealt/runs:.0f} "
          f"pushes={pushes/runs:.1f} removed={removed/runs:.0f} seats={[round(seats[i]/runs,2) for i in range(n)]} "
          + " ".join(f"{k[:4]}={wins[k]/T:.2f}" for k in ["aggressive", "balanced", "cautious"]), flush=True)

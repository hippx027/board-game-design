"""SIM-019: ability-card pool. Each player is dealt one random ability card. Run from sim/."""
import sys, random, json
from collections import Counter
sys.path.insert(0, ".")
import lds_sim as L
BASE = dict(upgrade_pay="discard", upgrade_cost=4, loot="tiles", pile=5, play_all=True, sticky_dead=True, elim_timing="end",
            merged_heal=True, hold=5, storm="flip", storm_sched={1: 1, 7: 2}, dmg_sched={1: 1, 7: 2}, min_start=3,
            drop_rule="inner", display_n=2, shield_persist=True, shield_cap=4, tile_mix="armory", deck_sizes=[24, 18, 18], end_limit=3)
POOL = {
    "Point blank (+1 dmg on your tile)": ({}, "point_blank"),
    "Long shot (+1 dmg off your tile)": ({}, "long_shot"),
    "Scavenge (loot twice)": ({}, "scavenge"),
    "Runner (Base Move 2)": ({"mov": 2}, None),
    "Field medic (Heal cards heal +2, Base Move 2)": ({"mov": 2}, "field_medic"),
    "Storm runner (storm dmg -1)": ({}, "storm_runner"),
    "Siphon (hit 2+: heal 1)": ({}, "siphon"),
    "Armored (start with 1 Shield, no refill)": ({"start_shield": 1}, None),
    "Heavy hitter (Base Attack 2)": ({"atk": 2}, None),
    "Deep pockets (keep 4 at end of turn)": ({}, "keep4"),
    "Tinkerer (first upgrade costs 3)": ({}, "tinkerer"),
}
L.CHARACTERS.clear(); L.CHARACTERS.update(POOL); L.LONG_SHOT_MIN = 1; L.PB_BONUS = 1; L.MEDIC_BONUS = 2
names = list(POOL); res = {}
for n in (2, 3, 4, 5):
    rng = random.Random(500 + n); wins = Counter(); seen = Counter(); runs = int(sys.argv[1]) if len(sys.argv) > 1 else 2500
    for _ in range(runs):
        cs = rng.sample(names, n); prof = [rng.choice(["aggressive", "balanced", "cautious"]) for _ in range(n)]
        r = L.Game(n, prof, random.Random(rng.random()), tiles_per_player={4: 12, 5: 10}.get(n, 15),
                   drop_rounds=tuple(3 + 2 * i for i in range(n)), characters=cs, **BASE).run()
        seen.update(cs); wins[r["winner_char"]] += 1
    res[n] = {c: wins[c] / seen[c] * n for c in names}  # 1.00 = fair share
    print(f"{n}p done", flush=True)
print(f"{'ability':36s}" + "".join(f"{n}p".rjust(7) for n in (2, 3, 4, 5)) + "   (1.00 = fair share)")
for c in sorted(names, key=lambda c: -sum(res[n][c] for n in res)):
    print(f"{c:36s}" + "".join(f"{res[n][c]:7.2f}" for n in (2, 3, 4, 5)))
json.dump(res, open("../simulations/ability_results3.json", "w"), indent=1)

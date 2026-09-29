"""Try character tuning versions quickly. Run from sim/."""
import sys, random
from collections import Counter
sys.path.insert(0, ".")
import lds_sim as L
BASE = dict(upgrade_pay="discard", upgrade_cost=4, loot="tiles", pile=5, play_all=True, sticky_dead=True, elim_timing="end",
            merged_heal=True, hold=5, storm="flip", storm_sched={1: 1, 7: 2}, dmg_sched={1: 1, 7: 2}, min_start=3,
            min_draw=2, drop_rule="inner", display_n=2, shield_persist=True, shield_cap=4, tile_mix="armory", deck_sizes=[24, 18, 18])
VERSIONS = {
 "v8": ({"Blaze": ({}, "point_blank"), "Ember": ({}, "scavenge"), "Tide": ({"mov": 2}, "storm_runner"),
         "Nova": ({}, "field_medic"), "Shade": ({}, "long_shot")}, 1, 1),
 "v9": ({"Blaze": ({}, "point_blank"), "Ember": ({"mov": 2}, "scavenge"), "Tide": ({}, "storm_runner"),
         "Nova": ({"shd": 1}, "field_medic"), "Shade": ({}, "long_shot")}, 1, 1),
 "v10": ({"Blaze": ({}, "point_blank"), "Ember": ({"mov": 2}, "scavenge"), "Tide": ({"mov": 2}, "storm_runner"),
         "Nova": ({"shd": 1}, None), "Shade": ({}, "long_shot")}, 1, 1),
}
for vname, (chars, lsmin, pb) in VERSIONS.items():
    L.CHARACTERS.clear(); L.CHARACTERS.update(chars); L.LONG_SHOT_MIN = lsmin; L.PB_BONUS = pb
    names = list(chars); line = []
    for n in (2, 3, 4, 5):
        rng = random.Random(7 + n); wins = Counter(); seen = Counter(); runs = 1200
        for _ in range(runs):
            cs = rng.sample(names, n); prof = [rng.choice(["aggressive", "balanced", "cautious"]) for _ in range(n)]
            r = L.Game(n, prof, random.Random(rng.random()), tiles_per_player={4: 12, 5: 10}.get(n, 15),
                       drop_rounds=tuple(3 + 2 * i for i in range(n)), characters=cs, **BASE).run()
            seen.update(cs); wins[r["winner_char"]] += 1
        line.append(f"{n}p: " + " ".join(f"{c}={wins[c]/seen[c]:.2f}" for c in names))
    print(vname, " | ".join(line), flush=True)

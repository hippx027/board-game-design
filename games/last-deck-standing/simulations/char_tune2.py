"""Character tuning round 2 (SIM-018). Run from sim/."""
import sys, random
from collections import Counter
sys.path.insert(0, ".")
import lds_sim as L
BASE = dict(upgrade_pay="discard", upgrade_cost=4, loot="tiles", pile=5, play_all=True, sticky_dead=True, elim_timing="end",
            merged_heal=True, hold=5, storm="flip", storm_sched={1: 1, 7: 2}, dmg_sched={1: 1, 7: 2}, min_start=3,
            min_draw=2, drop_rule="inner", display_n=2, shield_persist=True, shield_cap=4, tile_mix="armory", deck_sizes=[24, 18, 18])
B, E, S = ({}, "point_blank"), ({}, "scavenge"), ({}, "long_shot")
VERSIONS = {
 "v8 (baseline)": dict(chars={"Blaze": B, "Ember": E, "Tide": ({"mov": 2}, "storm_runner"), "Nova": ({}, "field_medic"), "Shade": S}),
 "v11 Tide Move2 only; Nova medic + 1 starting Shield": dict(chars={"Blaze": B, "Ember": E, "Tide": ({"mov": 2}, None), "Nova": ({"start_shield": 1}, "field_medic"), "Shade": S}),
 "v12 Nova medic +2": dict(chars={"Blaze": B, "Ember": E, "Tide": ({"mov": 2}, "storm_runner"), "Nova": ({}, "field_medic"), "Shade": S}, medic=2),
 "v13 Tide Move2 only; Nova medic +2": dict(chars={"Blaze": B, "Ember": E, "Tide": ({"mov": 2}, None), "Nova": ({}, "field_medic"), "Shade": S}, medic=2),
 "v14 Tide storm runner + 1 starting Shield; Nova medic + 1 starting Shield": dict(chars={"Blaze": B, "Ember": E, "Tide": ({"start_shield": 1}, "storm_runner"), "Nova": ({"start_shield": 1}, "field_medic"), "Shade": S}),
}
for vname, cfg in VERSIONS.items():
    L.CHARACTERS.clear(); L.CHARACTERS.update(cfg["chars"]); L.LONG_SHOT_MIN = 1; L.PB_BONUS = 1; L.MEDIC_BONUS = cfg.get("medic", 1)
    names = list(cfg["chars"]); line = []; worst = 0
    for n in (2, 3, 4, 5):
        rng = random.Random(11 + n); wins = Counter(); seen = Counter(); runs = 1200
        for _ in range(runs):
            cs = rng.sample(names, n); prof = [rng.choice(["aggressive", "balanced", "cautious"]) for _ in range(n)]
            r = L.Game(n, prof, random.Random(rng.random()), tiles_per_player={4: 12, 5: 10}.get(n, 15),
                       drop_rounds=tuple(3 + 2 * i for i in range(n)), characters=cs, **BASE).run()
            seen.update(cs); wins[r["winner_char"]] += 1
        rates = {c: wins[c] / seen[c] for c in names}
        worst = max(worst, max(abs(v - 1 / n) * n for v in rates.values()))  # relative deviation from fair share
        line.append(f"{n}p " + " ".join(f"{c[0]}{rates[c]:.2f}" for c in names))
    print(f"{vname}\n   " + " | ".join(line) + f"\n   worst relative deviation from fair: {worst:.0%}", flush=True)

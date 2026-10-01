"""SIM-023: character tweaks (Rig all upgrades cost 3, Tank Base Shield 1, Medic variants). Run from sim/."""
import sys, random
from collections import Counter
sys.path.insert(0, ".")
import lds_sim as L
BASE = dict(upgrade_pay="discard", upgrade_cost=4, loot="tiles", pile=5, play_all=True, sticky_dead=True, elim_timing="end",
            merged_heal=True, hold=5, storm="flip", storm_sched={1: 1, 7: 2}, dmg_sched={1: 1, 7: 2}, min_start=3,
            drop_rule="inner", display_n=2, shield_persist=True, shield_cap=4, tile_mix="armory", deck_sizes=[24, 18, 18], end_limit=3)
COMMON = {
    "Brawler": ({}, "point_blank"), "Sniper": ({}, "long_shot"), "Scavenger": ({}, "scavenge"), "Runner": ({"mov": 2}, None),
    "Storm Chaser": ({}, "storm_runner"), "Leech": ({}, "siphon"), "Heavy": ({"atk": 2}, None),
    "Mechanic (all upgrades cost 3)": ({}, "tinkerer_all"),
    "Medic (heal +2, Heal cards discarded)": ({}, "field_medic_keep"),
}
MEDICS = {"Tank T1: Base Shield 1, Base Attack 0": ({"shd": 1, "atk": 0}, None),
          "Tank T2: Base Shield 1, upgrades cost 5": ({"shd": 1}, "tank_slow")}
L.LONG_SHOT_MIN = 1; L.PB_BONUS = 1; L.MEDIC_BONUS = 2
for mname, mdef in MEDICS.items():
    pool = dict(COMMON); pool[mname] = mdef
    L.CHARACTERS.clear(); L.CHARACTERS.update(pool); names = list(pool); res = {}
    for n in (2, 3, 4, 5):
        rng = random.Random(900 + n); wins = Counter(); seen = Counter(); runs = 1200
        for _ in range(runs):
            cs = rng.sample(names, n); prof = [rng.choice(["aggressive", "balanced", "cautious"]) for _ in range(n)]
            r = L.Game(n, prof, random.Random(rng.random()), tiles_per_player={4: 12, 5: 10}.get(n, 15),
                       drop_rounds=tuple(3 + 2 * i for i in range(n)), characters=cs, **BASE).run()
            seen.update(cs); wins[r["winner_char"]] += 1
        res[n] = {c: wins[c] / seen[c] * n for c in names}
    print(f"== pool with {mname}", flush=True)
    for c in sorted(names, key=lambda c: -sum(res[n][c] for n in res)):
        print(f"  {c:52s}" + "".join(f"{res[n][c]:7.2f}" for n in (2, 3, 4, 5)), flush=True)

"""SIM-025: Medic loop and Mechanic fixes. Usage: python3 ability_test8.py <players>  (any working directory)"""
import os
import random
import sys
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sim"))
import lds_sim as L

BASE = dict(upgrade_pay="discard", upgrade_cost=4, loot="tiles", pile=5, play_all=True, sticky_dead=True, elim_timing="end",
            merged_heal=True, hold=5, storm="flip", storm_sched={1: 1, 7: 2}, dmg_sched={1: 1, 7: 2}, min_start=3,
            drop_rule="inner", display_n=2, shield_persist=True, shield_cap=4, tile_mix="armory", deck_sizes=[24, 18, 18], end_limit=3)
POOL = {"Brawler": ({}, "point_blank"), "Sniper": ({}, "long_shot"), "Scavenger": ({}, "scavenge"), "Runner": ({"mov": 2}, None),
        "Storm Chaser": ({}, "storm_runner"), "Leech": ({}, "siphon"), "Heavy": ({"atk": 2}, None),
        "Tank": ({"shd": 1}, "tank_slow"),
        "Medic now (+2, recycles)": ({}, "field_medic_keep"),
        "Medic M1 (+2, recycles, can't keep Heals)": ({}, "medic_nohold"),
        "Medic M2 (+1, recycles)": ({}, "medic_plus1"),
        "Mechanic now (all cost 3)": ({}, "tinkerer_all"),
        "Mechanic C1 (cost 3 once per turn)": ({}, "tinkerer_once"),
        "Mechanic C2 (first upgrade of each stat costs 3)": ({}, "tinkerer_perstat")}
L.CHARACTERS.clear(); L.CHARACTERS.update(POOL); L.LONG_SHOT_MIN = 1; L.PB_BONUS = 1; L.MEDIC_BONUS = 2
names = list(POOL)
n = int(sys.argv[1])
rng = random.Random(1700 + n)
wins, seen = Counter(), Counter()
for _ in range(1400):
    cs = rng.sample(names, n)
    prof = [rng.choice(["aggressive", "balanced", "cautious"]) for _ in range(n)]
    r = L.Game(n, prof, random.Random(rng.random()), tiles_per_player={4: 12, 5: 10}.get(n, 15),
               drop_rounds=tuple(3 + 2 * i for i in range(n)), characters=cs, **BASE).run()
    seen.update(cs)
    wins[r["winner_char"]] += 1
for c in names:
    print(f"{n}p\t{c}\t{wins[c] / seen[c] * n:.2f}")

"""SIM-029: split one-time Heal cards (base game) and new character abilities. Usage: heal_split_chars_test.py <players> <base|chars>"""
import os, random, sys
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sim"))
import lds_sim as L
CORE = dict(upgrade_pay="discard", upgrade_cost=4, loot="tiles", pile=5, play_all=True, sticky_dead=True, elim_timing="end",
            merged_heal=True, hold=5, min_start=3, drop_rule="inner", display_n=2, shield_persist=True, shield_cap=4,
            tile_mix="armory", deck_sizes=[24, 18, 18], end_limit=3, no_refill=True, split_attack=True, base_shd_max=0,
            storm="flip", storm_sched={1: 1, 7: 2}, dmg_sched={1: 1, 7: 2}, storm_mode="rings", shield_card_remove=True)
n, mode = int(sys.argv[1]), sys.argv[2]
if mode == "base":
    for name, kw in {"one-time, pick heal OR shield": {}, "one-time, SPLIT heal + shield": dict(heal_split=True)}.items():
        rng = random.Random(2900 + n); runs = 400; wins = Counter(); seats = Counter(); rounds = []; turns = healed = absorbed = dealt = storm = 0
        for _ in range(runs):
            prof = [rng.choice(["aggressive", "balanced", "cautious"]) for _ in range(n)]
            r = L.Game(n, prof, random.Random(rng.random()), tiles_per_player={4: 12, 5: 10}.get(n, 15),
                       drop_rounds=tuple(3 + 2 * i for i in range(n)), **CORE, **kw).run()
            rounds.append(r["rounds"]); wins[r["winner_profile"]] += 1; seats[r["winner_seat"]] += 1
            turns += r["turns"]; healed += r.get("dead_healed", 0); absorbed += r.get("dead_absorbed", 0); dealt += r.get("dead_dealt", 0); storm += r.get("storm_hits", 0)
        T = sum(v for k, v in wins.items() if k)
        print(f"{n}p | {name:32s} | stall={sum(1 for x in rounds if x >= 150)/runs:.2f} rounds={sorted(rounds)[runs//2]} turns={turns/runs:.0f} "
              f"healed={healed/runs:.1f} shieldShare={absorbed/max(1,absorbed+dealt):.2f} storm={storm/runs:.0f} "
              f"seats={[round(seats[i]/runs,2) for i in range(n)]} " + " ".join(f"{k[:4]}={wins[k]/T:.2f}" for k in ["aggressive", "balanced", "cautious"]), flush=True)
else:
    POOL = {"Brawler (+1 dmg on your tile)": ({}, "point_blank"), "Sniper (+1 dmg off your tile)": ({}, "long_shot"),
            "Scavenger (2nd cube)": ({}, "scavenge"), "Runner (Move 2)": ({"mov": 2}, None),
            "Storm Chaser (storm -1)": ({}, "storm_runner"), "Leech (siphon)": ({}, "siphon"), "Heavy (Attack 2)": ({"atk": 2}, None),
            "Tank v2 (start 1 Shield, upgrades 5)": ({"start_shield": 1}, "tank_slow"),
            "Mechanic v2 (all upgrades cost 3)": ({}, "tinkerer_all"),
            "Medic v2 (once per turn, a Heal heals 1 extra)": ({}, "medic_once"),
            "Berserker v2 (+2 Attack per Dead in hand)": ({}, "berserker2"),
            "Hoarder v2 (keep 5 at end of turn)": ({}, "keep5")}
    L.CHARACTERS.clear(); L.CHARACTERS.update(POOL); L.LONG_SHOT_MIN = 1; L.PB_BONUS = 1
    names = list(POOL); rng = random.Random(3000 + n); wins = Counter(); seen = Counter()
    for _ in range(1200):
        cs = rng.sample(names, n); prof = [rng.choice(["aggressive", "balanced", "cautious"]) for _ in range(n)]
        r = L.Game(n, prof, random.Random(rng.random()), tiles_per_player={4: 12, 5: 10}.get(n, 15),
                   drop_rounds=tuple(3 + 2 * i for i in range(n)), characters=cs, heal_split=True, **CORE).run()
        seen.update(cs); wins[r["winner_char"]] += 1
    for c in names:
        print(f"{n}p\t{c}\t{wins[c] / seen[c] * n:.2f}", flush=True)

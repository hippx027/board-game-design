"""SIM-028: no Heal upgrade; Heal cards always go to the discard pile (heal or shield). Usage: python3 heal_discard_test.py <players>"""
import os, random, sys
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sim"))
import lds_sim as L
CORE = dict(upgrade_pay="discard", upgrade_cost=4, loot="tiles", pile=5, play_all=True, sticky_dead=True, elim_timing="end",
            merged_heal=True, hold=5, min_start=3, drop_rule="inner", display_n=2, shield_persist=True, shield_cap=4,
            tile_mix="armory", deck_sizes=[24, 18, 18], end_limit=3, no_refill=True, split_attack=True,
            storm="flip", storm_sched={1: 1, 7: 2}, dmg_sched={1: 1, 7: 2}, storm_mode="rings")
VARIANTS = {
    "no Heal upgrade; shield REUSE, heal one-time": dict(base_shd_max=0),
    "no Heal upgrade; ONE-TIME for heal and shield": dict(base_shd_max=0, shield_card_remove=True),
}
n = int(sys.argv[1])
for name, kw in VARIANTS.items():
    rng = random.Random(2800 + n); runs = 400
    wins, seats = Counter(), Counter(); rounds = []; turns = healed = dealt = absorbed = storm = 0; upg = Counter()
    for _ in range(runs):
        prof = [rng.choice(["aggressive", "balanced", "cautious"]) for _ in range(n)]
        r = L.Game(n, prof, random.Random(rng.random()), tiles_per_player={4: 12, 5: 10}.get(n, 15),
                   drop_rounds=tuple(3 + 2 * i for i in range(n)), **CORE, **kw).run()
        rounds.append(r["rounds"]); wins[r["winner_profile"]] += 1; seats[r["winner_seat"]] += 1
        turns += r.get("turns", 0); healed += r.get("dead_healed", 0); dealt += r.get("dead_dealt", 0)
        absorbed += r.get("dead_absorbed", 0); storm += r.get("storm_hits", 0)
        for k in "AMH": upg[k] += r.get(f"upgrade_{k}", 0)
    T = sum(v for k, v in wins.items() if k)
    print(f"{n}p | {name:50s} | stall={sum(1 for x in rounds if x >= 150)/runs:.2f} rounds={sorted(rounds)[runs//2]} "
          f"p90={sorted(rounds)[int(runs*.9)]} turns={turns/runs:.0f} healed={healed/runs:.1f} dealt={dealt/runs:.0f} "
          f"storm={storm/runs:.0f} absorbed={absorbed/max(1,absorbed+dealt):.2f} upg A/M/H={upg['A']/runs:.1f}/{upg['M']/runs:.1f}/{upg['H']/runs:.1f} "
          f"seats={[round(seats[i]/runs,2) for i in range(n)]} " + " ".join(f"{k[:4]}={wins[k]/T:.2f}" for k in ["aggressive", "balanced", "cautious"]), flush=True)

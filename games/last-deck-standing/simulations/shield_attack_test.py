"""SIM-026: no upkeep Shield refill (Heal upgrade = +1 per Heal card) and split attacks.
Usage: python3 shield_attack_test.py <players>"""
import os
import random
import sys
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sim"))
import lds_sim as L

BASE = dict(upgrade_pay="discard", upgrade_cost=4, loot="tiles", pile=5, play_all=True, sticky_dead=True, elim_timing="end",
            merged_heal=True, hold=5, storm="flip", storm_sched={1: 1, 7: 2}, dmg_sched={1: 1, 7: 2}, min_start=3,
            drop_rule="inner", display_n=2, shield_persist=True, shield_cap=4, tile_mix="armory", deck_sizes=[24, 18, 18], end_limit=3)
VARIANTS = {
    "current": {},
    "no refill + Heal upgrade +1/card": dict(no_refill=True, base_shd_max=3),
    "split attacks": dict(split_attack=True),
    "both": dict(no_refill=True, base_shd_max=3, split_attack=True),
}
n = int(sys.argv[1])
for name, kw in VARIANTS.items():
    rng = random.Random(2600 + n); runs = 500
    wins, seats = Counter(), Counter(); rounds = []; turns = atk = dealt = absorbed = healed = upgH = 0
    for _ in range(runs):
        prof = [rng.choice(["aggressive", "balanced", "cautious"]) for _ in range(n)]
        r = L.Game(n, prof, random.Random(rng.random()), tiles_per_player={4: 12, 5: 10}.get(n, 15),
                   drop_rounds=tuple(3 + 2 * i for i in range(n)), **BASE, **kw).run()
        rounds.append(r["rounds"]); wins[r["winner_profile"]] += 1; seats[r["winner_seat"]] += 1
        turns += r.get("turns", 0); atk += r.get("attacks", 0); dealt += r.get("dead_dealt", 0)
        absorbed += r.get("dead_absorbed", 0); healed += r.get("dead_healed", 0); upgH += r.get("upgrade_H", 0)
    T = sum(v for k, v in wins.items() if k)
    print(f"{n}p | {name:34s} | stall={sum(1 for x in rounds if x >= 150)/runs:.2f} rounds={sorted(rounds)[runs//2]} "
          f"turns={turns/runs:.0f} attacks/turn={atk/max(1,turns):.2f} dealt={dealt/runs:.0f} absorbed={absorbed/max(1,absorbed+dealt):.2f} "
          f"healed={healed/runs:.1f} healUpg={upgH/runs:.1f} seats={[round(seats[i]/runs,2) for i in range(n)]} "
          + " ".join(f"{k[:4]}={wins[k]/T:.2f}" for k in ["aggressive", "balanced", "cautious"]), flush=True)

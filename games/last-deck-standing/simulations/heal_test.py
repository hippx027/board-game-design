"""SIM-006: Heal from discard pile. Run from sim/."""
import sys, random
sys.path.insert(0, ".")
import lds_sim as L
BASE = dict(storm="connected", push="8", upgrade_pay="discard", upgrade_cost=5, place_reverse=True,
            deck_size=18, drop_rounds=(4, 8, 12), pile=5, loot="tiles", bundle_cap=3)
for hd in (False, True):
    for n in (3, 5):
        rng = random.Random(1); rs = []; wins = {}; healed = wasted = turns = 0
        for _ in range(300):
            prof = [rng.choice(["aggressive", "balanced", "cautious"]) for _ in range(n)]
            g = L.Game(n, prof, random.Random(rng.random()), heal_discard=hd, **BASE)
            r = g.run(); rs.append(r["rounds"])
            if r["winner_profile"]: wins[r["winner_profile"]] = wins.get(r["winner_profile"], 0) + 1
            healed += r.get("dead_healed", 0); wasted += r.get("wasted_heals", 0); turns += r.get("turns", 0)
        rs.sort(); t = sum(wins.values())
        print(f"heal_discard={hd!s:5} {n}p median rounds={rs[150]} p90={rs[270]} dead healed/game={healed/300:.1f} "
              f"wasted heals/game={wasted/300:.1f} wins: " + " ".join(f"{k[:4]}={v/t:.2f}" for k, v in sorted(wins.items())), flush=True)

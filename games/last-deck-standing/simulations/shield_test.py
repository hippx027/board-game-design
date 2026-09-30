"""SIM-021: Shield turtle fixes. Run from sim/."""
import sys, random
from collections import Counter
sys.path.insert(0, ".")
import lds_sim as L
BASE = dict(upgrade_pay="discard", upgrade_cost=4, loot="tiles", pile=5, play_all=True, sticky_dead=True, elim_timing="end",
            merged_heal=True, hold=5, storm="flip", storm_sched={1: 1, 7: 2}, dmg_sched={1: 1, 7: 2}, min_start=3,
            drop_rule="inner", display_n=2, shield_persist=True, tile_mix="armory", deck_sizes=[24, 18, 18], end_limit=3)
VARIANTS = {
    "current: max 4, Base Shield max 4": dict(shield_cap=4),
    "Shield max 3": dict(shield_cap=3),
    "Shield decays 1 per upkeep": dict(shield_cap=4, shield_decay=True),
    "Base Shield max 2": dict(shield_cap=4, base_shd_max=2),
    "Heal used as Shield leaves game": dict(shield_cap=4, shield_card_remove=True),
    "decay + Base Shield max 2": dict(shield_cap=4, shield_decay=True, base_shd_max=2),
}
for name, kw in VARIANTS.items():
    print("==", name, flush=True)
    for n in (2, 3, 4, 5):
        rng = random.Random(40 + n); runs = 500; wins = Counter(); seats = Counter(); rounds = []; absorbed = dealt = turns = 0; upg = Counter()
        for _ in range(runs):
            prof = [rng.choice(["aggressive", "balanced", "cautious"]) for _ in range(n)]
            g = L.Game(n, prof, random.Random(rng.random()), tiles_per_player={4: 12, 5: 10}.get(n, 15),
                       drop_rounds=tuple(3 + 2 * i for i in range(n)), **BASE, **kw)
            r = g.run(); rounds.append(r["rounds"]); wins[r["winner_profile"]] += 1; seats[r["winner_seat"]] += 1
            absorbed += r.get("dead_absorbed", 0); dealt += r.get("dead_dealt", 0); turns += r.get("turns", 0)
            for k in "AMH": upg[k] += r.get(f"upgrade_{k}", 0)
        T = sum(v for k, v in wins.items() if k)
        print(f"  {n}p rounds={sorted(rounds)[runs//2]} turns={turns/runs:.0f} absorbed={absorbed/max(1,absorbed+dealt):.2f} "
              f"shieldUpg={upg['H']/runs:.1f} seats={[round(seats[i]/runs,2) for i in range(n)]} "
              + " ".join(f"{k[:4]}={wins[k]/T:.2f}" for k in ["aggressive", "balanced", "cautious"]), flush=True)

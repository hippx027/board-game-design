"""SIM-005: bundle cap + why fight. Run from sim/: python3 ../simulations/fight_test.py"""
import sys, random
sys.path.insert(0, ".")
import lds_sim as L
BASE = dict(storm="connected", push="8", upgrade_pay="discard", upgrade_cost=5, place_reverse=True,
            deck_size=18, drop_rounds=(4, 8, 12), pile=5, loot="tiles")

def seat_win(test, n, runs, field, **kw):
    rng = random.Random(1); w = 0; rounds = []; maxhit = 0
    for _ in range(runs):
        prof = [test] + [rng.choice(field) for _ in range(n - 1)]; rng.shuffle(prof)
        idx = prof.index(test)
        r = L.Game(n, prof, random.Random(rng.random()), **{**BASE, **kw}).run()
        w += r["winner_seat"] == idx; rounds.append(r["rounds"])
    return w / runs, sorted(rounds)[runs // 2]

print("A) bundle cap, 5p, win rate of one bot among mixed field (fair 0.20)")
for cap in (99, 3, 2):
    row = []
    for t in ("aggressive", "balanced", "cautious"):
        wr, med = seat_win(t, 5, 200, ["aggressive", "balanced", "cautious"], bundle_cap=cap)
        row.append(f"{t[:4]}={wr:.2f}")
    print(f"  cap={'none' if cap == 99 else cap:4}", " ".join(row), f"median rounds={med}", flush=True)

print("B) 2p duels, 300 games each: row player's win rate")
styles = ["brawler", "skirmisher", "cautious"]
for a in styles:
    row = []
    for b in styles:
        if a == b: row.append("  -  "); continue
        wr, _ = seat_win(a, 2, 300, [b], bundle_cap=3)
        row.append(f"{wr:.2f}")
    print(f"  {a:10s} vs {styles}: {row}", flush=True)

print("C) 5p, one bot among a mixed field of all three styles (fair 0.20)")
for t in styles:
    wr, med = seat_win(t, 5, 200, styles, bundle_cap=3)
    print(f"  {t:10s} {wr:.2f}  median rounds={med}", flush=True)

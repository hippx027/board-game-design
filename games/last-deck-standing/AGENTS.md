# Last Deck Standing — Agent Notes

Context for any AI agent (Claude Code, Codex, Cursor) picking up this project. Read this, then `design-state.md`, before proposing changes.

## What this is
A battle royale deck builder by Brandon and Chris. Players flood rivals' decks with Dead cards while a storm shrinks a hex board built by the players. It's in a first-paper-playtest stage (2026-09-29).

## Files
| File | Purpose |
|---|---|
| `rulebook-draft.md` | **Source of truth** for the rules (v1). Main rules above `---`; Designer Notes (Ideas for Later, Playtest Questions) below |
| `rulebook.html` | Published playtester page, pre-rendered from the Markdown by `sim/build_html.js`. Live at https://claude.ai/artifact/Vxqh1KqNT3K8XXwGD8Ub2y |
| `design-state.md` | Locked / Rejected / Open decisions, evidence table, risks, next experiment |
| `components-sheet.md`, `pnp-checklist.md` | Paper prototype build |
| `playtest-log-001.md`, `feedback-sheet.md` | First human session kit |
| `sim/lds_sim.py` | Seeded Monte Carlo simulator (heuristic bots; system evidence only) |
| `simulations/SIM-00N.md`, `READTHROUGH-001.md` | Test write-ups; raw JSON in `simulations/data*/` |

To rebuild after editing the rules: `node sim/build_html.js rulebook-draft.md rulebook.html` (pre-renders static, ASCII-safe HTML; needs `npm install marked@12`) and `node sim/md2docx.js rulebook-draft.md "Last Deck Standing Rules v1.docx"` (needs `npm install docx`). The Claude artifact page is no longer updated; the local files are the source of truth.

## Running the simulator
```bash
cd sim
python3 lds_sim.py --players 3 4 5 --runs 300 --seed 42 \
  --tiles-per-player 12 --upgrade-pay discard --upgrade-cost 4 --deck-size 18 --loot tiles --pile 5 \
  --play-all --sticky-dead --elim-timing end --merged-heal --hold 5 \
  --storm flip --storm-sched 1:1,7:2 --dmg-sched 1:1,7:2 --min-start 3 \
  --min-draw 2 --drop-rule inner --display 2 --shield-persist --shield-cap 4 --tile-mix armory --deck-sizes 24,18,18 --drop-rounds 3,5,7,9  # one drop per player: 3,5 at 2p; 3,5,7 at 3p; ...
```
The flags above match the current rules (use `--tiles-per-player` 15 for 2–3p, 12 for 4p, 10 for 5p). Other levers: `--tiles-per-player`, `--drop-rounds 4,8,12` (gold supply drops), `--elim-loot`, `--storm-per-turn`, `--values 6,4,2`. Bot styles are in `PROFILES` (random, aggressive, balanced, cautious, brawler, skirmisher). Also: `--heal-discard`, `--kill-upgrade` (rejected variants, kept for regression).

## How the designer works (preferences)
- **The designer makes the rules calls.** Surface contradictions as clear options with a recommendation; don't silently decide. Defaults you choose must be flagged in the rules or notes.
- **Ideas the designer likes but hasn't committed to go in Designer Notes → Ideas for Later**, not the main rules.
- **Test before adopting** when a change affects balance: one variable per run, report stalls, median rounds, turns, and seat and play-style win rates. Never auto-fix rules from sim anomalies; propose and let the designer decide.
- The rules are **v1**; don't track changes against the original Google Doc.
- Plain rulebook language for new playtesters: short numbered steps, tables for card data, a quick reference card.

## Key findings to remember
- The original storm stranded players on islands, and 69% of 5-player games never ended. That was fixed by the no-island rule (SIM-001/002).
- Turtling (cautious play winning) was only fixed by letting players play every card, together with sticky Dead cards, end-of-turn elimination and the merged Heal/Shield card (SIM-007). Kill rewards, loot piles, supply drops and retreat moves did not help (SIM-004/005).
- 8–10 players is too long solo (~115 turns). It's tabled as a team variant.
- Bots see all information, so they can't measure what hidden or open information does to players. Marked Dead-card backs need human testing.

- With holding (Heal cards included, the designer's call: holding heals is a Fortnite-style strategy), cautious play wins ~52% at 5p in bots. Watch it in human tests; don't "fix" it by banning heal holding (SIM-009).

## Open questions
Supply-drop placement (rotating, in notes) · upgrade cost 4 vs 5 · whether turtling is fun or dull · real seconds per turn (target 30–60 min).

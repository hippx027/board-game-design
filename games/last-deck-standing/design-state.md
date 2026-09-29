# Design State — Last Deck Standing

Updated 2026-09-29 · Designers: Brandon and Chris · Milestone: 1 → 3 (paper MVP ready for first external playtest)

## Project Status
| Field | Value |
|---|---|
| Pitch | A battle royale deck builder: flood rivals' decks with Dead cards while the storm shrinks the board |
| Fun sentence | Go all in for the kill, then get out before someone hits you back |
| Players / time | 2–5 / 30–60 min (8–10 player team variant needs testing) |
| Rules | `rulebook-draft.md` (v1) |
| Prototype | P1 simulation (`sim/lds_sim.py`) · P4 PnP ready (`pnp-checklist.md`) |

## Locked
- Elimination: 3+ Dead cards in hand at the **end** of your turn; announce "critical" at upkeep; Dead cards stay in hand (sticky) and have marked backs
- Damage = Attack − range, no minimum; same-hex fights allowed by design
- Play any number of cards; one attack per turn
- Heal card is Heal or Shield (chosen when played); used to heal → removed from game
- Loot: pre-made tiles (21 icons per 15-tile set); cube → card into your discard pile
- Upgrades: pay 4+ value of one type, paid cards to discard, max 4
- Storm: no islands; Phase 2 push-off from round 8; the active player chooses the tile
- Reverse pawn placement order
- Elimination loot pile: 5 / 3 / 1 picks
- Supply decks of 18 cards; 60 Dead cards
- Heal affects your hand only
- Tiles per player scale down: 15 (2–3p), 12 (4p), 10 (5p)

## Rejected
- Resource cubes and buying cards
- Storm tokens / storm damage in the base game (moved to Ideas)
- Minimum-1 damage
- Upgrade payments leaving the game (thinned decks and caused stalls, SIM-001)
- Heal from the discard pile (tested SIM-005; designer kept hand-only)
- 2-play limit and bundled plays (replaced by play-all, SIM-007)
- Separate Shield cards (merged into Heal)
- A 2-movement cost to loot a pile (no effect, SIM-004)

## Open / Ideas
Supply drops (gold deck, rotating placement) · teams and knockdowns for 8–10 players · Self-Revive special card · walls · chests · named locations · battle bus drop · levels · upgrade cost 4 option

## Evidence
| ID | Type | Finding |
|---|---|---|
| SIM-001 | P1 | v1 stalled 69% at 5p (islands, thinned decks) |
| SIM-002 | P1 | No-island storm plus push-off: 0% stalls |
| SIM-003 | P1 | Reverse placement fixes seat balance; 10p is too long (about 115 turns) |
| SIM-004 | P1 | 18-card supplies; kill rewards don't change the cautious edge |
| SIM-005 | P1 | Bundle cap 3 is neutral; fighting wins 1v1 (72%) but loses in a crowd |
| SIM-006 | P1 | Fewer tiles at 4–5p: 5p goes from 64 to 53 turns; seat balance holds, 0% stalls |
| SIM-007 | P1 | Play-all + sticky Dead + end-of-turn elimination + merged Heal: first fix for turtling (5p cautious 48% → 30%); 13 rounds / 48 turns; cost 4 triples upgrades with no length or balance change |
| READTHROUGH-001 | P2 (agent) | Wording gaps fixed; same-hex duels; upgrades rare in fast games |

System evidence only. Fun, clarity with humans, setup time and table handling are unproven (physical_dependency).

## Risks (≤5)
1. Longer human turns with unlimited plays
2. 2-player games favour aggression strongly (bots: 48% aggressive vs 14% cautious)
3. Setup time (now 50 tiles at 5p)
4. Hidden-deck reshuffle swings (mitigated by marked backs)
5. The storm may feel fiddly (connectivity checks)

## Next Experiment
Paper session 001: Good/Bad/Meh plus triage (`playtest-log-001.md`). Then run the kill-criteria gate after 3 sessions.

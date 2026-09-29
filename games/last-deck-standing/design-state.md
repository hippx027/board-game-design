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
- Storm: markers placed from the outside in (tiles stay); 1 per turn, then 2 per turn from round 7; ending a turn on a storm tile = 1 Dead (2 from round 7) to discard; Shield doesn't block it
- Normal pawn placement order; pawns start ≥3 tiles apart
- Supply drops: gold deck, one per player at rounds 3, 5, 7, 9, 11; placement rotates from the start player; placed on a tile that's not storm or edge; nudge 1 tile each (SIM-011/013)
- Holding: keep any unplayed cards (Heal cards included); at upkeep draw to 5 and always at least 2, then discard down to 5 (not Dead cards)
- Elimination loot pile: 5 / 3 / 1 picks
- Supply decks of 18 cards; 60 Dead cards
- Heal affects your hand only
- Tiles per player scale down: 15 (2–3p), 12 (4p), 10 (5p)

## Rejected
- Resource cubes and buying cards
- Removing tiles for the storm, no-islands rule and push-off (replaced by storm markers, SIM-008)
- Reverse placement order (SIM-008)
- Minimum-1 damage
- Upgrade payments leaving the game (thinned decks and caused stalls, SIM-001)
- Heal from the discard pile (tested SIM-005; designer kept hand-only)
- 2-play limit and bundled plays (replaced by play-all, SIM-007)
- Separate Shield cards (merged into Heal)
- A 2-movement cost to loot a pile (no effect, SIM-004)

## Open / Ideas
Next fix to test if cautious play dominates with humans: siphon · teams and knockdowns for 8–10 players · Self-Revive special card · walls · chests · named locations · battle bus drop · levels · upgrade cost 4 option

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
| SIM-008 | P1 | Storm markers work; reverse placement hurts once players can place near each other; normal order + ≥3 apart fixes seats |
| SIM-009 | P1 | Hold all + "close fast" storm: 13 rounds / 50 turns at 5p, 2p seats 50/50; cautious ~52% (holding Heals); Heal holding kept by designer as a real strategy |
| SIM-010 | P1 | Thinner Heal values barely change healing (-10%); kept 9/6/3 |
| SIM-011 | P1 | Supply drops: one per player at rounds 3/5/7/9/11; ~4.7 drops at 5p; no balance change; placer choice doesn't affect balance |
| SIM-012 | P1 | Loot piles don't reward fighters (aggressive claims 23%; final hitter claims 34%) |
| SIM-013 | P1 | Draw-at-least-2 upkeep (fixes the hold-5 immortality exploit) and non-storm/non-edge drops: no stalls, same length, +1 upgrade/game |
| READTHROUGH-003 | P2 (agent) | Found hold-5 immortality, spiteful drop placement, no round-25 end |
| READTHROUGH-001 | P2 (agent) | Wording gaps fixed; same-hex duels; upgrades rare in fast games |

System evidence only. Fun, clarity with humans, setup time and table handling are unproven (physical_dependency).

## Risks (≤5)
1. Cautious Heal-hoarding may dominate (sim ~52% at 5p); check with humans
2. Longer human turns with unlimited plays
3. Setup time (now 50 tiles at 5p)
4. Hidden-deck reshuffle swings (mitigated by marked backs)
5. Storm-marker placement speed at the table

## Next Experiment
Paper session 001: Good/Bad/Meh plus triage (`playtest-log-001.md`). Then run the kill-criteria gate after 3 sessions.

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
- Play any number of cards
- Heal cards are one-time: split the value between removing Dead cards from hand and adding Shield, then the card leaves the game (SIM-028/029)
- Shield persists until damage uses it (max 4) and never refills on its own; it only comes from Heal cards. There is no Heal upgrade; only Move and Attack upgrade, and Heal cards can't pay (SIM-028)
- Attacks can be split among several players (at most one attack per player per turn); each attack subtracts its own range (SIM-026)
- Loot: pre-made tiles (21 icons per 15-tile set: 6 Move / 11 Attack / 4 Heal); cube → card into your discard pile
- Upgrades: pay 4+ value of one type, paid cards to discard, max 4
- Storm: markers placed ring by ring from the outside in (finish the outer ring before the next; SIM-027) (tiles stay); 1 per turn, then 2 per turn from round 7; ending a turn on a storm tile = 1 Dead (2 from round 7) to discard; Shield doesn't block it
- Normal pawn placement order; pawns start ≥3 tiles apart
- Supply drops: Legendary deck (values 3/3/4/4 per type, SIM-022), one per player at rounds 3, 5, 7, 9, 11; placement rotates from the start player; placed on a tile that's not storm or edge; nudge 1 tile each (SIM-011/013)
- Holding: at end of turn discard down to 3 cards (Dead cards stay and count); at upkeep draw to 5, so you always draw at least 2 (SIM-020)
- Elimination loot pile: 5 / 3 / 1 picks
- First Game (learning rules) box: no drops, loot piles, upgrades, loot display, critical call or characters; plays the same length with no stalls (SIM-024)
- Characters (optional variant until human playtests): 10 character (ability) cards, deal 2 keep 1; starting decks labelled Player 1–5 (SIM-019)
- Supply decks: Attack 24, Move 18, Heal 18 (same 1/2 : 1/3 : 1/6 value spread), 2 face up per deck (6-card loot display); 60 Dead cards
- Heal affects your hand only
- Tiles per player scale down: 15 (2–3p), 12 (4p), 10 (5p)

## Art direction (chosen)
- Comic "kaiju" style study: `pnp/style-mockup-kaiju.html`
- Type colours: Attack red, Move purple, Heal green, Shield blue
- Rarity (Fortnite naming): Common gray, Rare blue, Epic purple, Legendary gold, shown Slay-the-Spire style: the title bar (reading ATTACK / MOVE / HEAL) and a tinted frame are the rarity colour, plus the badge and tag (`pnp/rarity-mocks.html`, first row). The value badge reads "+1", "+2", …
- Characters each have their own palette, art pattern and epithet (Blaze the Brawler, Shade the Sniper, Ember the Scavenger, Tide the Runner, Nova the Medic, Gale the Storm Chaser, Vex the Leech, Bastion the Tank, Brute the Heavy, Rig the Mechanic)
- Hex tiles: ink-outlined hexes, sand sunburst, loot as white sticker discs in type colours; loot cubes: purple Move, red Attack, green Heal
- Icons: Material Symbols **Sharp**, filled, with an ink outline, in a tilted white rectangle plate

## Rejected
- A round-25 end rule: designer says kill or be killed; the storm plus draw-at-least-2 always forces an end (0% stalls in SIM-013/014)
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
| SIM-019 | P1 | 11 ability cards tested over 3 rounds; 10 within about ±25% of fair (most ±15%); Deep pockets too weak and left out |
| SIM-020 | P1 | End-of-turn discard to 3 replaces draw-at-least-2: same balance, ~2 fewer turns at 5p |
| SIM-016 | P1 | Attack-heavy tiles: more attacks, less healing, shorter games; no change to who wins; heavy mixes empty the Attack deck; first adopted 7/9/5, then 6/11/4 with a 24-card Attack deck |
| SIM-015 | P1 | Persistent Shield (max 4; 4 and 8 equivalent): absorbs 21% of damage (was 13%); +2 rounds at 5p; balance unchanged |
| SIM-014 | P1 | 2–3 face-up cards per supply deck (2 adopted): +13–15% upgrades, no balance or length change |
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

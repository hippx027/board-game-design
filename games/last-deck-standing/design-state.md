# Design State — Last Deck Standing

Updated 2026-10-12 · Designers: Brandon and Chris · Milestone: v2 (realtime) drafted from playtest 001; first v2 paper session next

**Two rulesets live here.** v2 (realtime) is current: `rulebook-v2-draft.md`. The v1 (turn-based) record is kept below under "Archived v1" for reference; where they disagree, v2 wins.

## v2 Project Status
| Field | Value |
|---|---|
| Rules | `rulebook-v2-draft.md` (v2, realtime) · `rulebook-draft.md` (v1 baseline) |
| Source | `playtest-notes-001.md` (first human session) and the designer's answers, 2026-10-12 |
| Prototype | Realtime sim `sim/lds_rt.py` (SIM-030, addenda 1–13) · print sheets `pnp/v2/last-deck-standing-v2-*.pdf` from `sim/pnp_sheets_v2.py` |
| Players / time | 2–5 solo, or teams (equal sizes) up to 10 players · no time target for now (sim: about 8–12 min at 37 s turns) |

## v2 Locked (designer's calls)
- Realtime: no rounds; everyone plays their own turns at their own pace, no turn timer; a table timer drives drops (every 2 min) and the storm (every 4 min); pausing freezes the play clock
- Attacks: declare "Attack", pause the table, resolve, resume (option A). B (dodge with a Move card) and C (resolves 5 s later) are for later
- Damage = Attack − **2 per tile of range**; Dead cards go into the target's discard pile, placed by the attacker
- Base deck 4 Move 1 / 4 Attack 1 / 2 Heal 1; Base Move 1 and Base Attack 1, fixed; no stat tracker and no Shield
- Heal is one-time: removes Dead cards from your hand, then leaves the game
- Hand: draw up to 5; at end of turn discard down to 3 non-Dead cards (Dead stay, not counted; SIM-030 add. 15 modelled this as keep 3)
- Elimination: 3+ Dead cards in hand at the end of your own turn; Dead cards have plain backs; announce "critical" at 3 in hand; no hand limit on Dead cards but you can't discard them
- Loot: cubes on half the tiles, on printed cube spots in a loot colour (50 of 100 tiles: 14 Move, 26 Attack, 10 Heal; 2026-10-13); you loot by moving *into* a tile (start tile excluded); loot goes into your hand; **hand cap 5** with overflow going to the discard pile (SIM-030 addendum 10)
- Loot decks Move 14 / Attack 26 / Heal 10 (50, one per cube spot; 100 tiles, 50 spots), values 1 and 2, half each (designer's call, 2026-10-13: 3s only from the Market, kills or drops; SIM-030 add. 19)
- Market: no tiers for now, one 21-card deck (values 2 and 3), 3 face up; Splendor-style specific costs printed on each card (designer's call 2026-10-13; pay-any was tried and rejected as a feel, SIM-030 add. 20), paid cards leave the game, bought card goes to hand
- Hand cap 5 always (overflow loot to discard; buying only shrinks hand); empty draw pile reshuffles discard incl. Dead; healed Dead return to the Dead supply; Base Attack once per turn; bought/paid Heal leaves the game. Print: tiles on Letter sticker sheets (hex 1.75 in across flats, 20 per sheet), cards on 11x17.
- Legendary deck 48 (3s and 4s; 72 at 8+ players, SIM-030 add. 23); drops every 2 min (1st player places, then each other player moves it in turn order: 2p one mover x3 tiles, 3p two movers x2 tiles, 4+ every other player x1 tile, legendary cubes = player count, on the tile); elimination drop (2 legendary cubes where a player fell, their legendary cards first)
- Storm: whole outer ring marked each alarm; 1 Dead card per storm tile you move into, plus 1 more if you end your turn on one
- Teams: any equal-size layout, rotation (each member goes after the previous teammate), no attacking teammates
- Turn floor: none for the first session
- First Game box in the v2 draft: solo, drops in, attack option A, no teams

## v2 Open / Ideas
Hand lock (2 Dead + 3 junk is unkillable): left as is; the Storm and loot-and-upgrade incentives are meant to punish campers, watch in playtests · starting-tile cubes stuck: accepted · Market as a board location (several instances) · giving cards to a player on your tile · market tiers · cube refresh with each drop · attack options B and C · hand cap lower or higher than 5 · teams in simultaneous mode · Market costs (cheaper costs stall the sim, so unresolved) · characters from v1 are not carried into v2

## v2 Evidence (SIM-030, `simulations/SIM-030.md`)
| Addendum | Finding |
|---|---|
| Headline | Realtime games run about 7–11 min at 37 s turns (3/5 players); attack options A/B/C don't change win rates, A adds time |
| 2–5 | Turn floor is a roughly linear pace dial; range cost 2 lengthens games 10–50%; a free base Attack 1 is weak at range 2 |
| 6 | Looting on entering a tile and 2-minute storm play about the same; the enter charge adds some 5p stalls |
| 6b | Enter + end-of-turn storm charge: 0–1% stalls |
| 7 | Starting cubes are a weak length dial (about +2.5 min from 20% to 100% of tiles); Market buys barely move |
| 8 | Teams: rotation stalls with big teams (5v5 24%); simultaneous is fine up to 10 players |
| 9 | Slower storm trims rotation stalls a little; the enter charge is what stalls them (likely a bot artifact, unverified) |
| 10 | Hand cap 5 costs almost nothing |
| 11 | First Game config: 8.4 min (3p), 9.9 min (4p), stalls 0.3% / 3.7% |
| 12–13 | Weaker loot does nothing; cheaper Market costs raise buys about 50% but cause 15–32% stalls |

System evidence only. Fun, how pauses feel, whether deck upgrading happens (sim: about 3 buys per player) and table handling are unproven; human sessions decide those.

## v2 Risks (≤5)
1. The Market may barely get used (sim: about 3 buys per player per game); loot out-competes it
2. Attack pauses are 33–50% of table time in the sim, which may not feel realtime
3. Rotation teams of 4+ may stall in play (sim 14–24%)
4. Bots can't judge fun or table handling; several rules are my defaults (marked "default" in the draft)
5. Games are short (about 8 min), so the deck-building idea may not get room

## v2 Next Experiment
Paper session 002: First Game, 3–4 players, rulebook-v2-draft.md. Count Market buys per player, real game length, pause share and hoarding; then decide the Market costs.

---

# Archived v1 (turn-based)


Updated 2026-09-29 · Designers: Brandon and Chris · Milestone: 1 → 3 (paper MVP ready for first external playtest)

## v1 Project Status
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
- Battle bus spinner on the centre tile: pawns start on its line (2–3p) or within 1 tile of it (4+), no minimum distance between pawns (each on its own tile), normal placement order (SIM-030 add. 17)
- Supply drops: Legendary deck (values 3/3/4/4 per type, SIM-022), one per player at rounds 3, 5, 7, 9, 11; placement rotates from the start player; placed on a tile that's not storm or edge; nudge 1 tile each (SIM-011/013)
- Holding: at end of turn discard down to 3 cards (Dead cards stay and count); at upkeep draw to 5, so you always draw at least 2 (SIM-020)
- Elimination loot pile: 5 / 3 / 1 picks
- First Game (learning rules) box: no drops, loot piles, upgrades, loot display, critical call or characters; plays the same length with no stalls (SIM-024)
- Characters (optional variant until human playtests): 10 character (ability) cards, deal 2 keep 1; starting decks labelled Player 1–5 (SIM-019)
- Supply decks: Attack 24, Move 18, Heal 18 (same 1/2 : 1/3 : 1/6 value spread), 2 face up per deck (6-card loot display); 60 Dead cards
- Heal affects your hand only
- Tiles per player scale down: 15 (2–3p), 12 (4p), 10 (5p)

## Art direction (chosen)
- Comic "kaiju" style study: `pnp/v1/style-mockup-kaiju.html`
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

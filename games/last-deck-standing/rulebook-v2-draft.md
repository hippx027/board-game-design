# Last Deck Standing — Realtime Rules v2 (DRAFT)

Designers: Brandon and Chris. Drafted 2026-10-12 from playtest 001 notes (`playtest-notes-001.md`) and the designer's answers. `rulebook-draft.md` (v1) stays as the turn-based baseline.

**Turn floor: none for the first session (designer's call).** Starting cubes: ⚑ half the tiles (sim default; not yet answered).

**Every number in [brackets] is a placeholder to be tuned. Every line marked ⚑ is my assumption, awaiting the designer's call.** Updated with the designer's answers (round 2).

## Overview
- **Players:** 2–5 solo, or 2 teams · **Time:** no target for now (designer's call, 2026-10-12). Sim says about 7–11 min at 37 s turns; see SIM-030
- **Goal:** Be the last player (or team) standing. You knock opponents out by putting Dead cards in their decks.
- **You are eliminated** if you end a turn with 3 or more Dead cards in your hand.
- **Realtime:** there are no rounds. Everyone plays their own turns at the same time and at their own pace. There is no turn timer. The storm and loot drops run on a table timer.

## What changed from v1
| v1 | v2 |
|---|---|
| Players take turns around the table | Everyone plays at once, each at their own pace; the table pauses for attacks |
| Rounds drive the storm and drops | A table timer drives both |
| Base Move / Base Attack / Shield stats and a stat tracker | **Base Move 1 and Base Attack 1, fixed** (designer's call): nothing upgrades them, so there is no tracker and no Shield. Everything above 1 comes from cards |
| Upgrade stats | Upgrade your **deck** by trading cards for better cards at the Market |
| Loot tiles with fixed loot icons; take a card to your discard pile | Loot cubes marking available loot; take the top card of that type's deck **into your hand** (to test) |
| Face-up loot display | Gone. You take the top card, unseen. (A face-up Market replaces it) |
| Dead cards have marked backs | Plain backs. You announce when 3 are in your hand |
| Discard down to 3 at end of turn | Discard as many as you like (never Dead cards) |
| Range costs 1 damage per tile | Range costs **2** damage per tile |
| Cards 1–4 value | Starting cards are 1; everything you gain at the Market is 2 or higher |

## Components
| Item | Qty | Notes |
|---|---|---|
| Base deck | 10 per player | **4 Move 1, 4 Attack 1, 2 Heal 1** |
| Loot decks | 3, one per type | Move 12, Attack 16, Heal 10 ⚑, each shuffled face down. Values 2 and 3 only (no 1s). Playtest variant: replace half the 2s with 1s, since looting is faster now |
| Gold deck | 24 | Value 3 and 4 cards (4 each of Move 3/4, Attack 3/4, Heal 3/4); taken from gold cubes in drops and elimination drops |
| Market deck | 20 | Value 2 and 3 cards; 3 face up; see Market |
| Dead cards | 60 | Plain backs |
| Loot cubes | [per board] | One colour per type (purple Move, red Attack, green Heal); mark available loot on the board |
| Gold cubes | 1 per player per drop | Mark drops; taking one gives the top card of the Gold deck |
| Board tiles | per player count | Same hex tiles as v1, but without printed loot icons ⚑ |
| Pawn | 1 per player | |
| Table timer | 1 | A phone with two repeating alarms: **Drop** and **Storm** |
| Storm markers | enough for the edge | One per tile |
| Cards print | 11×17 paper | Card sheets (replaces the old size) |

## Setup
1. Build the board as in v1 (players alternate placing tiles, each touching the last), but with no loot icons.
2. Place loot cubes on [N] tiles ⚑ (see Looting).
3. Place pawns at least 3 tiles apart, in the order players choose.
4. Shuffle your 10-card base deck and draw 5.
5. Lay out the Market.
6. Start the timer: the 2-minute Drop clock starts with the game. Everyone starts together.

## Your Turn (played at your own speed)
1. **Draw** up to 5 cards. If you have 3 or more Dead cards in your hand, say **"critical"** out loud ⚑.
2. **Act** in any order: play cards, move, attack, loot, trade at the Market.
3. **End:** if you have 3 or more Dead cards in hand, you are eliminated. Otherwise put your played cards in your discard pile, discard any unplayed cards you don't want (never Dead cards), and start your next turn right away.

Nobody waits for you. If you take a long turn, the others take several.

## Cards
| Card | When played |
|---|---|
| **Move N** | Move N extra tiles this turn (on top of your Base Move 1) |
| **Attack N** | Add N to your attack this turn (on top of your Base Attack 1) |
| **Heal N** | One-time use. Remove up to N Dead cards from your hand. The card leaves the game. There is no Shield |

Starting cards are value 1. Cards gained from the Market are value 2 or higher.

## Moving
Play Move cards. Move up to 1 (your Base Move) plus the total value of Move cards played this turn, one adjacent tile per point. You can't cross a gap. Any number of pawns may share a tile. You always have **Base Move 1**, so you can move 1 tile with no Move cards. Base Move and Base Attack never change.

## Looting
- Cubes on the board mark **available loot**.
- **Loot a cube by moving into its tile** (designer's call): each cube on a tile you move into, passing through or stopping, is removed from the board and you take the **top card of the matching loot deck** (purple Move, red Attack, green Heal) **into your hand**. You can loot as many tiles as you can reach in a turn. The tile you start on doesn't count, so you can't loot a cube you are standing on. **Exception:** gold cubes from a drop or an elimination drop that are on your tile are picked up without moving ⚑ (when: any time on your turn).
- Looted cards in hand can be played right away, and that is the point: a Heal you loot is a Heal you can use. Played cards (other than Heals) go to your discard pile and become part of your deck.
- There is no hand limit. At end of turn you discard any unplayed cards you don't want to keep, but never Dead cards. Played cards go to your discard pile.
- Cubes are returned to the supply. New cubes appear with each **Drop**.

## Market
You may trade cards from your hand to buy a Market card, any time during your turn.

- **No tiers for now** (designer's call; tiers return later). The Market deck is one shuffled deck; **3 cards are face up** and are replaced from the deck as they're bought.
- Market cards are **value 2 or 3**, never 1. ⚑ Deck: 6× Attack 2, 4× Move 2, 4× Heal 2, 3× Attack 3, 2× Move 3, 2× Heal 3.
- **Cost is a combo of cards, counted by number, not value.** So paying value 1s is the efficient trade, and paying a 3 is a waste. ⚑ Proposed costs (first version to test):

| Buy | Pay |
|---|---|
| Attack 2 | 2 Attack + 1 Move |
| Move 2 | 2 Move + 1 Heal |
| Heal 2 | 1 Heal + 1 Attack + 1 Move |
| Attack 3 | 3 Attack + 1 Move |
| Move 3 | 3 Move + 1 Heal |
| Heal 3 | 2 Heal + 1 Attack + 1 Move |

- Paid cards **leave the game** ⚑ (this thins your deck, which is the aim: fewer junk cards, stronger draws; v1's rejection of leaving the game was about stat upgrades stalling, so watch for it). Cards come from your hand.
- The bought card goes into your **discard pile** and joins your deck at the next reshuffle.

The game inside the game: **collect the right cards to turn many low cards into a few strong ones.**

## Attacking (realtime)
To attack, you declare **"Attack"** and **pause the table** (Captain Sonar style; designer's pick for the first session):
1. Everyone freezes, including the timers.
2. You name the target(s), count the range, and resolve the attack with the **damage = your Attack total − 2 × Range** (each tile of distance costs 2, changed from v1's 1); 0 or less can't hit. Example: Attack 4 does 4 at range 0, 2 at range 1, and can't reach range 2.
3. You put the Dead cards into the target's **discard pile**, yourself. They show up when that deck reshuffles, as in v1.
4. Everyone resumes.

You can split your Attack among several players, as in v1 (one attack per player). **Locked for the first paper session: option A (pause).** Options B (the target may dodge with a Move card) and C (resolves 5 s later) are listed below to try in later sessions. In the sim none of them changes who wins; only A costs time.

## Dead Cards
- Dead cards have plain backs, like all other cards (marked backs would stop people shuffling them to the top).
- If you hold 3 or more, you **announce "critical"** when you draw or receive them. Everyone knows you're one hit from being out.
- Dead cards can't be played or discarded, and stay in your hand until you heal them.
- **Elimination:** you still take turns, just in realtime. If you end your turn with 3 or more Dead cards in hand, you're out. Nothing else eliminates you.

## Elimination Drop
When a player is eliminated:
1. Remove their pawn and return all their Dead cards to the Dead supply. Their other cards leave the game, **except any gold (Legendary) cards they own** (hand, deck or discard): those stay on the tile as the first cards of the loot pool.
2. **Loot drop:** place **2 gold cubes** on the tile where they fell ⚑. It's a drop with no pause and no nudging. Whoever moves through or onto the tile takes them like any gold cube: the fallen player's gold cards come first, then the top of the Gold deck. If they left more than 2 gold cards, add one cube per extra card.
3. Gold cubes only come out while the Gold deck has cards left.


## The Storm (timer)
- The storm alarm sounds **every 2 minutes** (designer's call).
- On the alarm, **pause the table**, place storm markers on **every tile of the current outer ring** at once, then resume.
- **1 Dead card for each storm tile you move into** (designer's call), and **1 more if you end your turn on a storm tile**. Dead cards go in your discard pile. Standing in the storm and not moving still costs the end-of-turn card. Later rings [2] ⚑.
- Once every tile is marked, every move costs a Dead card, plus one more at the end of your turn.

## Drops (timer)
- The 2-minute Drop clock starts with the game and repeats.
- On the alarm, pause the table:
  1. The first player picks a tile and places the drop marker there. The first player rotates each drop ⚑.
  2. The next player moves the drop up to **3 tiles**.
  3. The table places **gold cubes**: one per player in the game (2 players: 2 cubes; 3 players: 3 cubes) ⚑. Place them all on the drop's tile or its neighbours ⚑ (my test: on the tile, so a drop is a fight magnet).
- Looting a gold cube works like any cube: move into its tile, remove it and take the top card of the Gold deck into your hand. If a drop lands on your tile, you pick it up without moving.
- Regular cubes are **not** refreshed by drops. They are only the starting cubes. Playtest variant: a cube refresh (for example, the table adds [N] regular cubes with each drop).

## Teams (variant)
- 2 teams of 2–3.
- Teammates take **turns one at a time**: member 1 takes a full turn, then member 2, then member 3.
- The teams play against each other **in realtime**: both teams are running at once.
- A team is eliminated when all its members are.
- Teammates can help: a teammate on your tile can play a Heal on you ⚑.

## Playtest options still to run
**#2 — Attack timing:**
- **A (drafted above):** pause the table, resolve.
- **B:** the attack goes in an **action queue** and a target gets 5 seconds to respond with a card (a Shield-like block).
- **C:** attacks are **simultaneous**: you each name a target, then reveal.

**#3 — Team rotation:**
- **A:** members take turns one at a time, as drafted.
- **B:** a team has a **single shared hand**.
- **C:** members play simultaneously, with no rotation (solo rules, shared win).

**Storm:** interval is 2 minutes; test 3 / 4 as variants. Both charges are in (enter + end of turn).

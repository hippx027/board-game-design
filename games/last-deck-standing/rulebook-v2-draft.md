# Last Deck Standing — Realtime Rules v2 (DRAFT)

Designers: Brandon and Chris. Drafted 2026-10-12 from playtest 001 notes (`playtest-notes-001.md`) and the designer's answers. `rulebook-draft.md` (v1) stays as the turn-based baseline.

**Turn floor: none for the first session (designer's call), but see the Realtime table rules (every turn must do something).** Starting cubes: 43 cubes on 38 of the 61 hexes (about 7 in 10, raised from half on 2026-10-22, because you now have to move into a hex to loot it; SIM-030 addendum 28).

**Lines marked "default" are my calls where the designer hadn't decided; they were adopted on 2026-10-12 so the first paper session can start ("do them all"), and the designer can change any of them.** Numbers in [brackets] are still placeholders.

**Δ marks what is new or changed from v1** (turn-based, `rulebook-draft.md`): a Δ on a heading means the whole section differs; on a bullet, table row or step, just that line. Unmarked text plays as in v1. Dropped from v1: stat tracker and Shield, round track, loot display, loot piles, characters, marked Dead backs, supply-drop marker. The print file `last-deck-standing-v2-diff-*.pdf` holds only the Δ components.

## Overview
- Δ **Players:** 2–6 on the fixed board (solo or equal-size teams; 7–10 wait for the bigger hex-group boards, see Ideas for Later) · **Time:** no target for now (designer's call, 2026-10-12). Sim says about 4–6 min with no pauses and discard-all (bots; humans slower); see SIM-030 addendum 29
- Δ **Goal:** Be the last player (or team) standing. You knock opponents out by putting Dead cards in their decks. **The game ends the moment only one player or team is left,** and they win (designer's call, 2026-10-13); they don't have to finish their turn.
- **You are eliminated** if you end a turn with 3 or more Dead cards in your hand.
- Δ **Realtime:** there are no rounds. Everyone plays their own turns at the same time and at their own pace, with no turn timer (designer's call, 2026-10-22). The storm and loot drops run on a table timer.

## Δ First Game (learning rules, 3–4 players, no teams)
For your first paper session, play it like this. Everything else plays exactly as written.

| Leave out | Instead |
|---|---|
| Teams | Everyone plays for themselves |
| The "critical" call | Just check for 3+ Dead cards at the end of your turn |
| Other attack options | Declare "Attack", resolve it at once, no pause |

**Drops stay in** (designer's call: they matter at every player count): the 2-minute drop timer, legendary cubes, the Legendary deck and the elimination drop.

Keep: the 4-minute storm timer, the Market (3 face up, no tiers, specific costs printed on each card), the hand cap of 5, and Range cost 2 per tile. Cubes go on the 43 printed cube spots.

What to watch for (these are the questions this session answers):
1. **Does the Market get used?** Sim: about 3 buys per player per game (9 at 3p, 11 at 4p). Count yours.
2. **Do attacks feel fair without a pause?** Note any argument about positions or who declared first (the sim has no data on this). Rule of thumb already in the rules: positions are fixed the moment someone says "Attack".
3. **How long does a game take?** Sim with the current rules (no pauses, discard-all, fixed board): about 4 minutes at 2–3 players to about 6 minutes at 6 players. Humans will be slower than bots. Write down the real number.
4. **Hoarding:** does the hand cap of 5 change what you loot or hold?
5. **Storm:** does it push people together or just kill them? Sim: at 4 minutes the storm marks fewer than 1 ring per game, so it barely matters (see the Storm note under Playtest options).

Simulated games under the current rules (SIM-030, addendum 29) end in about 4–6 minutes with 0% stalls (bots; humans slower).

## What changed from v1
| v1 | v2 |
|---|---|
| Players take turns around the table | Everyone plays at once, each at their own pace; attacks resolve on the spot, no pause |
| Rounds drive the storm and drops | A table timer drives both |
| Base Move / Base Attack / Shield stats and a stat tracker | **Base Move 1 and Base Attack 1, fixed** (designer's call): nothing upgrades them, so there is no tracker and no Shield. Everything above 1 comes from cards |
| Upgrade stats | Upgrade your **deck** by trading cards for better cards at the Market |
| Loot tiles with fixed loot icons; take a card to your discard pile | Loot cubes marking available loot; take the top card of that type's deck **into your hand** (to test) |
| Face-up loot display | Gone. You take the top card, unseen. (A face-up Market replaces it) |
| Dead cards have marked backs | Plain backs. You announce when 3 are in your hand |
| Discard down to 3 at end of turn | **Discard every non-Dead card** (designer's call, 2026-10-22): only Dead cards stay in your hand, so you redraw to 5 each turn. Hand cap of 5; looted cards over the cap go to your discard pile |
| Range costs 1 damage per tile | Range costs **2** damage per tile |
| Cards 1–4 value | Starting cards are 1; everything you gain at the Market is 2 or higher |

## Components
| Item | Qty | Notes |
|---|---|---|
| Δ Base deck | 10 per player | **4 Move 1, 4 Attack 1, 2 Heal 1** |
| Δ Loot decks | 3, one per type | Move 12, Attack 23, Heal 8 (43 cards, one per cube spot on the fixed board), each shuffled face down. **Values 1 and 2 only, half each** (designer's call: no 3s in loot; Move 6×1 + 6×2, Attack 11×1 + 12×2, Heal 4×1 + 4×2; the half-and-half split is my default). To get 3s you must use the Market, kill someone (elimination drop) or reach a drop. Old loot (2s and 3s) is kept as a variant |
| Δ Legendary deck | 48 | Value 3 and 4 cards (8 each of Move 3/4, Attack 3/4, Heal 3/4 in the 48; the second 24 for 8-10 players is shelved with those player counts). Bots at 6 players draw about 15 per game. Sized by SIM-030 addendum 23; taken from legendary cubes in drops and elimination drops |
| Δ Market deck | 21 | Value 2 and 3 cards; 3 face up; see Market |
| Δ Dead cards | 70 | Plain backs. Trimmed from 100 to **70** (default, 2026-10-25) now that the game is 2-6 players: the sim's average peak is 46 out at once at 6 players (SIM-030 addendum 29), so 70 leaves headroom for bad games; raise it again if 7-10 players return. If the supply ever runs out, play on: no more Dead can be dealt until some are healed or an eliminated player returns theirs |
| Δ Loot cubes | 43 | One colour per type (purple Move 12, red Attack 23, green Heal 8); one on every printed cube spot of the board |
| Legendary cubes | 1 per player per drop | Mark drops; taking one gives the top card of the Legendary deck |
| Δ Table timer | 1 | A phone with two repeating alarms, **Storm** and **Drop**, and one pause button. The timer app in `timer/index.html` does this (it has no per-player turn timers; ATTACK! only logs) |
| Δ Game board | 1 | **One fixed board** (designer's call, 2026-10-22): a hexagon of 61 hexes (radius 4), 38 have a printed loot spot (5 of them **double-loot hexes** with two spots, one per hex group A to E) for 43 spots in all, the rest blank. The centre hex is a regular hex (it can hold loot); hexes are shaded in 5 groups A to E for later group play. Print: `last-deck-standing-v2-board-17x11.5.pdf`, one landscape page. Individual hex tiles are gone for now |
| Pawn | 1 per player | |
| Δ Spinner | 1 | Battle bus: sits on the centre tile; its line sets where pawns may start (a paper arrow on a pin, or a pencil, works) |
| Δ Storm markers | 61 | One per hex |
| Δ Cards print | 11×17 paper | Card sheets (replaces the old size) |

## Setup
1. Δ **Lay out the board.** Use the fixed 61-hex board for any player count from 2 to 6 (default: the sim runs fine at 2–6 players; 2 players on 61 hexes is roomy but the storm still closes it). No building: the old player-built boards and per-player tile counts are gone for now.
2. Δ Put a loot cube of the **matching colour** on every printed cube spot (43 spots on 38 of the 61 hexes, 5 of them double-loot hexes; designer's call 2026-10-22, tested in SIM-030 addendum 28). The mix is 12 purple Move, 23 red Attack, 8 green Heal (about 6/11/4 per 21), matching the loot decks card for card. When a cube is looted the spot stays empty; no new loot cubes appear (only legendary cubes, from Drops).
3. Δ **Battle bus:** put a spinner on the centre hex (a regular hex, not marked) and spin it. Its line runs across the board through the centre. In a **2 or 3 player** game, pawns start **on the line**. With **4 or more players**, they start **on the line or 1 tile away from it**. No minimum distance between pawns (designer's call), but each pawn starts on its own tile; players place in the order they choose. (Designer confirmed 2026-10-13: the line sets starting positions.)
4. Δ Shuffle your 10-card base deck and draw 5. **When your draw pile is empty, shuffle your discard pile (Dead cards included) to make a new one** (designer's call, 2026-10-13).
5. Lay out the Market.
6. Δ **Seat order:** go around the table clockwise from the player who spun the spinner (the youngest player spins; default). This is the "turn order" for Drops (designer's call, 2026-10-13).
7. Δ Start the timer: the 2-minute Drop clock starts with the game. Everyone starts together.

## Δ Your Turn (played at your own speed)
1. **Draw** up to 5 cards. If you have 3 or more Dead cards in your hand, say **"critical"** out loud (default).
2. **Act** in any order: play cards, move, attack, loot, trade at the Market.
3. **End:** if you have 3 or more Dead cards in hand, you are eliminated. Otherwise put your played cards in your discard pile, **discard every card in your hand that isn't Dead** (designer's call, 2026-10-22; replaces "keep up to 3"), and start your next turn right away. Dead cards stay, so you draw back up to 5 (3 or more cards if you hold 2 Dead). Use it or lose it: a Heal or Move you don't play goes to your discard pile, not back to your hand (it comes around again when you reshuffle), so spend what you want before you End.

**No turn timer (designer's call, 2026-10-22; replaces the 1-minute sand timer).** Timers run only the table events: the Storm and the Drops. Turns have no limit, so a slow player simply takes fewer turns than a fast one. You can End early; your next turn starts right away.

Nobody waits for you. If you take a long turn, the others take several.

## Δ Cards
| Card | When played |
|---|---|
| **Move N** | Move N extra tiles this turn (on top of your Base Move 1) |
| **Attack N** | Add N to your attack this turn (on top of your Base Attack 1, which you get **once per turn**, not once per declared Attack) |
| **Heal N** | One-time use. Remove up to N Dead cards from your hand. The card leaves the game. There is no Shield |

Starting cards are value 1. Cards gained from the Market are value 2 or higher.

## Δ Moving
Play Move cards. Move up to 1 (your Base Move) plus the total value of Move cards played this turn, one adjacent tile per point.  Any number of pawns may share a tile. You always have **Base Move 1**, so you can move 1 tile with no Move cards. Base Move and Base Attack never change.

## Δ Looting
- Cubes on the board mark **available loot**.
- **Loot a cube by moving into its tile** (designer's call): each cube on a tile you move into, passing through or stopping, is removed from the board and you take the **top card of the matching loot deck** (purple Move, red Attack, green Heal) **into your hand**. You can loot as many tiles as you can reach in a turn. The tile you start on doesn't count, so you can't loot a cube you are standing on. **Exception:** legendary cubes from a drop or an elimination drop that are on your tile are picked up without moving, as soon as they land (default).
- Looted cards in hand can be played right away, and that is the point: a Heal you loot is a Heal you can use. Played cards (other than Heals) go to your discard pile and become part of your deck.
- **Your hand never goes over 5 cards, ever** (designer's call: always follow the hand cap). Dead cards in your hand count toward it. If your hand is full when you loot, the looted card goes **straight to your discard pile** instead of your hand (default overflow rule; you are never forced to discard to loot). At end of turn you discard every non-Dead card (see Your Turn). Played cards go to your discard pile.
- Cubes are returned to the supply. The only new cubes are **legendary cubes** from Drops.

## Δ Market
You may trade cards from your hand to buy a Market card, any time during your turn.

- **No tiers for now** (designer's call; tiers return later). The Market deck is one shuffled deck; **3 cards are face up** and are replaced from the deck as they're bought.
- Market cards are **value 2 or 3**, never 1. Deck (21 cards, default): 6× Attack 2, 4× Move 2, 4× Heal 2, 3× Attack 3, 2× Move 3, 2× Heal 3.
- **Each Market card has its own cost: a combo of specific cards from your hand, counted by number, not value** (Splendor-style; designer's call, 2026-10-13, replacing "pay any cards"). So paying value 1s is the efficient trade, and paying a 3 is a waste. The cost is printed on the card. Never Dead cards. **You may pay with Legendary cards too** (designer's call, 2026-10-13). Costs (default; cheaper costs stalled the sim, SIM-030 addendum 12-13):

| Buy | Pay |
|---|---|
| Attack 2 | 2 Attack + 1 Move |
| Move 2 | 2 Move + 1 Heal |
| Heal 2 | 1 Heal + 1 Attack + 1 Move |
| Attack 3 | 3 Attack + 1 Move |
| Move 3 | 3 Move + 1 Heal |
| Heal 3 | 2 Heal + 1 Attack + 1 Move |

- Paid cards **leave the game** (this thins your deck: fewer junk cards, stronger draws).
- The bought card goes **into your hand**, so you can play it this turn. Buying always shrinks your hand (you pay 3 or 4 cards and get 1), so the hand cap never blocks a buy. (Sim: about 3 buys per player whether the bought card goes to your hand or your discard pile.)
- **A Heal you buy is like any Heal:** it leaves the game when you play it, and a Heal you pay as part of a cost leaves the game too.
- **If the Market deck runs out,** face-up cards that are bought are not replaced (default; the 21-card deck is rarely emptied at 2-4 players).

The game inside the game: **collect the right cards to turn many low cards into a few strong ones.**

## Δ Attacking (realtime)
To attack, you declare **"Attack"** out loud and resolve it on the spot. **The table does not pause** (designer's call, 2026-10-22; the Captain Sonar-style pause is kept as an option below). Positions are fixed the moment you say "Attack": nobody may move until it resolves.
1. You name the target(s), count the range, and resolve the attack with the **damage = your Attack total − 2 × Range** (each tile of distance costs 2, changed from v1's 1); 0 or less can't hit. Example: Attack 4 does 4 at range 0, 2 at range 1, and can't reach range 2.
2. You put the Dead cards into the target's **discard pile**, yourself (designer's call, 2026-10-22: stays in the discard pile; "reshuffle on hit" is in Ideas for Later). They show up when that deck reshuffles, usually within a turn or two. The target takes no forced turn and loses no cards.

You can split your Attack among several players, as in v1 (one attack per player). **The range cost is paid per target** (designer's call, 2026-10-13): each target takes your Attack total (pool) minus 2 per tile of its own range, and you choose how to divide the Attack among them. **Locked for the first paper session: no pause (option 0).** Options A (pause the table, resolve, resume), B (the target may dodge with a Move card) and C (resolves 5 s later) are listed below to try in later sessions. In the sim none of them changes who wins; only A costs time.

**No-pause edge cases (defaults, 2026-10-25, untested):**
- **Two attacks at once:** whoever said "Attack" first resolves first; if you can't agree, the older player decides. Positions freeze for both until both are done.
- **Mid-move:** a pawn you have started to move is where your hand left it when "Attack" is said; no taking it back.
- **Target out of range after a card is played:** an attacker is committed to the Attack cards already played; a target may not play a Move card to escape after "Attack" is said.
- **A target in the middle of their own turn** keeps their hand; the Dead cards go to their discard pile, so their hand is unaffected.
- **Lost cards or disputes:** the table timer's Attack button is for the log only; it does not pause.

## Δ Dead Cards
- **Healed Dead cards go back to the Dead supply** (the stack), not to a discard pile (designer's call, 2026-10-13).
- Dead cards have plain backs, like all other cards (marked backs would stop people shuffling them to the top).
- If you hold 3 or more, you **announce "critical"** when you draw them. Everyone knows you're one hit from being out.
- Dead cards can't be played or discarded, and stay in your hand until you heal them.
- **Elimination:** if you end your turn with 3 or more Dead cards in hand, you're out. Nothing else eliminates you.

## Δ Elimination Drop
When a player is eliminated:
1. Remove their pawn and return all their Dead cards to the Dead supply. Their other cards leave the game, **except any Legendary cards they own** (hand, deck or discard): those stay on the tile as the first cards of the loot pool.
2. **Loot drop:** place **2 legendary cubes** on the tile where they fell (default). It's a drop with no pause and no nudging. Whoever moves through or onto the tile takes them like any legendary cube: the fallen player's legendary cards come first, then the top of the Legendary deck. If they left more than 2 legendary cards, add one cube per extra card.
3. The fallen player's own Legendary cards always drop. Extra cubes taken from the Legendary deck only come out while that deck has cards left (designer's call, 2026-10-13).


## Δ The Storm (timer)
- The storm alarm sounds **every 4 minutes** (designer's call; first alarm at 4:00).
- On the alarm, **pause the table**, place storm markers on **every tile of the current outer ring** at once, then resume.
- **1 Dead card for each storm tile you move into** (designer's call), and **1 more if you end your turn on a storm tile**. Dead cards go in your discard pile. Standing in the storm and not moving still costs the end-of-turn card.
- Once every tile is marked, every move costs a Dead card, plus one more at the end of your turn.

## Δ Drops (timer)
- The 2-minute Drop clock starts with the game and repeats.
- On the alarm, pause the table:
  1. One player (the **placer**) picks a tile and places the drop marker there. The placer rotates each drop, one seat clockwise (default).
  2. Then the players after them, in seat order, each move the drop (designer's call), up to:
     - **2 players:** the other player moves it **3 tiles**.
     - **3 players:** each of the other two moves it up to **2 tiles**.
     - **4 or more players:** each other player moves it up to **1 tile**, in turn order.
  3. The table places **legendary cubes**: one per player in the game (2 players: 2 cubes; 3 players: 3 cubes) (default). Place them all **on the drop's tile** (default; a drop is a fight magnet).
- Looting a legendary cube works like any cube: move into its tile, remove it and take the top card of the Legendary deck into your hand. If a drop lands on your tile, you pick it up without moving.
- Regular cubes are **not** refreshed by drops. They are only the starting cubes. Playtest variant: a cube refresh (for example, the table adds [N] regular cubes with each drop).

## Δ Teams (variant)
- **Any team shape from 2 to 6 players**: 2 teams of 2–3 (2v2, 3v3) or 3 teams of 2 (2v2v2). Bigger teams (up to 5v5) wait for the 7–10 player boards in Ideas for Later. **Teams are equal in size** for the first sessions (designer's call).
- Every player has their own deck, hand and pawn.
- **Rotation (designer's call):** each team takes turns one player at a time. Member 1 takes a full turn, then member 2, and so on, then back to member 1. Each player goes after the previous teammate has finished. Different teams run in realtime against each other, so every team has one player acting at a time.
- **No turn timer, so rotation is manual (default, 2026-10-25):** when you End, say "next" and your teammate starts. If a teammate is stuck, the rest of the team may say "skip" and the rotation moves on. At 2–6 players teams are 2 teams of 2–3 or 3 teams of 2; the rotation only matters at 3 on a team.
- A team is eliminated when all its members are. When a member is eliminated, the rotation skips them.
- **You can't attack a teammate** (designer's call), with Attack cards or anything else.
- Teammates can help: a teammate on your tile can play a Heal on you (default).
- The board is the same fixed 61 hexes for every team layout, so teams stop at 6 players for now; the table timer is the same for every team size.
- **Known risk, SIM-030 addendum 8:** rotation gets slow with big teams. Your next turn only comes after every teammate has gone, so the storm kills players who haven't acted yet, and 5v5 stalls in about a quarter of sim games. Fine at 2v2 and 3v3. Playtest the big layouts and see; options to test if needed are listed below.

## Realtime table rules (defaults from the blind read-through, 2026-10-25; untested)
Fixes for gaps a blind read-through found once the turn timer and the attack pause were removed. All are my defaults, flagged for the designer:
- **Every turn must do something.** You can't End until you have moved, looted, bought, played a card or attacked at least once. This stops instant End-and-redraw cycling and free micro-turns (a free Base Move/Attack is still allowed, but once per turn like everything else).
- **Alarms end every turn.** When the Storm or Drop alarm sounds, everyone stops touching cards and pawns and every turn ends where it stands (elimination and the storm's end-of-turn Dead card are checked). Half-finished moves stay as they are; play resumes from that state. A player can't sit in a turn forever to dodge elimination or the storm. This is what "pause the table" means for the Storm and the Drop.
- **Attack cards are spent.** Played Attack cards and the Base Attack are used up when an Attack resolves, so you can't re-declare with the same cards. **Damage = Dead cards:** you put that many Dead cards into the target's discard pile.
- **First hand wins.** If two players reach for the same cube or face-up Market card, the first hand to touch it takes it; a tie goes to the older player. Cubes are collected when you enter a tile, so a pawn frozen mid-path by "Attack" keeps what it has already picked up.
- **Last two out together:** if both survivors would be eliminated at the same End (alarm), the one with fewer Dead cards wins, then the older player.
- **Start of game:** no actions until someone says "Go"; no Attacks in the first 10 seconds.
- **Drops:** the drop lands on a tile with no storm marker; cubes = living players; with no Legendary cards left, no cubes are placed. If the Dead supply is empty, storm charges and hits deal no card (default).
- **The Drop marker** is any spare token (a coin); it isn't a component.

## Playtest options still to run

**Note: pacing without a turn timer (2026-10-22).** Nothing caps a turn now, so a very slow player gets few turns and a fast one many; ending instantly still gives a free Base Move 1 and Base Attack 1. **Playtest options if pace is a problem:** the 1-minute sand timer back; a minimum turn length; a limit of one declared Attack per turn. **Watch for:** rushing micro-turns to farm moves, and one slow player stalling nobody but themselves.

**Attack timing (one list; the rules above use 0):**
- **0 (locked):** no pause, positions fixed when "Attack" is said.
- **A:** pause the table, resolve, resume.
- **B:** the attack goes in an **action queue** and a target gets 5 seconds to respond with a card (for example by playing a Move card to step out of range).
- **C:** attacks are **simultaneous**: you each name a target, then reveal.

**Team rotation:**
- **A (locked, designer's call):** members take turns one at a time, as drafted.
- **B:** a team has a **single shared hand**.
- **C:** members play simultaneously, with no rotation (solo rules, shared win); the sim says this scales to 10 players with few stalls.
- **Big-team fixes to test if rotation stalls:** a slower storm for teams of 4+ (for example 3 min), or damage only on entering a storm tile.

**Storm:** interval is 4 minutes (designer's call; sim: SIM-030 add. 14). Both charges are in (enter + end of turn). **Flag (SIM-030 addendum 29):** with no pauses, discard-all and the 61-hex board, games last 4–6 minutes in the sim, so a 4-minute storm marks only 0.3–0.9 rings per game and barely matters. At 2 minutes it marks 1.2–2.1 rings; at 90 s, 2.1–2.7. Keep 4 minutes for the first human playtest and time real games, then decide. The timer app lets you pick 2–5 minutes.

**Loot overflow (flag):** bots lose 2 (2 players) to 16 (6 players) looted cards per game to a full hand, because everything is discarded each turn and loot lands in a hand that is often already full. Default: leave it (the overflow card goes to your discard pile, not lost). If playtesters feel robbed, option: a looted card over the cap is played or kept face-up beside your hand until your next draw.

**Room to deck-build (flag):** the sim's games make about 5 Market buys at 2 players to 14 at 6 players, but each player only takes 4–5 turns in a 4-minute game at 3–4 players, so bought cards rarely reshuffle in. Watch whether the Market feels worth it; option if not: cheaper costs or buying straight to the draw pile.

## Ideas for Later (not rules)
- **Give cards to a player on your tile:** put non-Dead cards from your hand into another player's discard pile if you share a tile. Designer's idea (2026-10-12), kept for later. The 5-card hand cap applies, though it can't matter because cards go to their discard pile. Open questions: teammates only, or anyone? Is it an action? A limit per turn? (Market costs count cards, so gifting helps the receiver; see SIM-030 notes.)
- **Hand lock (gone since 2026-10-22):** with everything discarded each turn, 2 Dead + 3 kept cards can't happen. History:  the first draft of this rule had Dead not counting toward the 3 you keep, so 2 Dead + 3 kept cards filled the hand and a player never drew again, immune to every Dead card. The designer's rule is that Dead always count toward the 3, which means you always draw at least 2 cards. Starting-tile cubes that can't be looted by moving in are accepted as is.
- **Hex groups instead of one fixed board (designer's idea, 2026-10-22):** after the fixed board, play with groups of hexes joined in different shapes, so every game has a new map. Brings back 7-10 player games by using more groups.
  - **Plan (designer, 2026-10-22):** the box holds **10 groups**; the first game uses the default map (5 groups A to E of 12 hexes around the centre hex, as printed on the board PDF). After the first game, **each player places one group on the map as they like.**
  - **Not for the first session:** a 3-player map of 37 hexes needs fewer loot cubes (the 43-card loot decks assume the full 61), so use the full board until the loot per group is sorted out.
  - **Placement defaults (my picks, 2026-10-25, not tested):** the centre hex always goes down first. Players place one group each in seat order, then the youngest spins for the first placer. A group must touch the centre hex or a group already placed (edges meet along whole hex sides), and no holes inside the map. With 3 players the map is 37 hexes (centre plus 3 groups), with 5 players it is 61.
  - **Open:** the shapes of groups F to J (different outlines and loot layouts so maps vary), the number of groups per player count, and how Storm rings work on an irregular map (default: the storm marks the hexes farthest from the centre first, a whole ring at a time).
- **A few super-good hexes (designer's idea, 2026-10-22):** special hexes in the mix with a rich cube spot or a bonus, once shaped boards exist.
- **The map opens up (designer's idea, 2026-10-22):** mid-game a new hex or group is added to the board and comes with a high-loot hex, which pulls players toward it like a drop does. Open: where it attaches (outer edge only, so it can't outrun the storm?), who places it, and whether it replaces or adds to Drops.
- **Reshuffle on hit (designer's idea, 2026-10-22):** when you are hit, the Dead go to your discard pile and your whole discard pile is shuffled into your draw pile at once. Dead reach your hand about as fast as shuffling them in (model: 1.0-1.2 own turns vs 1.7-2.1 with Dead in the discard), and you also get your earlier good cards back, so a hit is not purely a loss. Not adopted; the rule stays "into the discard pile". Other Dead delivery options modelled: shuffle into the draw pile, on top of the draw pile. A forced end-of-turn on hit was rejected as feeling bad.
- **Market tiers** return later (the designer said "not later").
- **Cube refresh** with each drop, as a playtest variant.
- **Market as a location:** instead of buying anywhere, the Market is a board tile you have to be on to buy. **Multiple Market tiles** (several instances, so there's no single crowd). Designer's idea (2026-10-12), kept for later. Design notes: buying becomes rarer (the sim already shows only about 3 buys per player per game), a central tile would be stormed last, and 10-player games need several tiles. If tried, buy only while standing on a tile and let the first to declare take a face-up card. Not simulated yet.

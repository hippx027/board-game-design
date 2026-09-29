# Last Deck Standing — Playtest Rules v1

Designers: Brandon and Chris.

## Overview
- **Players:** 2–5 · **Time:** 30–60 min
- **Goal:** Be the last player standing. You knock opponents out by flooding their decks with Dead cards.
- **You are eliminated** if you end your turn with 3 or more Dead cards in your hand. Dead cards stay in your hand until you heal them, so every hit also slows you down.

## Components
| Item | Qty | Notes |
|---|---|---|
| Loot tiles | 15 per player (one tile set each) | Hex tiles printed with 0–3 loot icons; see Loot Tile Set |
| Base deck cards | 10 per player | 4 Strike (Attack 1), 3 Dash (Move 1), 3 Patch Up (Heal 1) |
| Attack supply deck | 18 | 9× value 1, 6× value 2, 3× value 3 |
| Movement supply deck | 18 | 9× value 1, 6× value 2, 3× value 3 |
| Heal supply deck | 18 | 9× value 1, 6× value 2, 3× value 3 (each Heal card can heal or shield) |
| Dead cards | 60 | Marked on the back, so everyone can see Dead cards in hands and decks. If they run out, use any marked substitute |
| Loot cubes | 7 per color per player (Move, Attack, Heal) | Mark unlooted loot on the tiles |
| Player pawn | 1 per player | |
| Stat tracker | 1 per player | Tracks Base Move, Base Attack and Base Shield (each 0–4) and current Shield points |
| Round track and marker | 1 | 25 spaces; tracks the global round for the storm phases |

Each card has a value from 1 to 3, which is its strength. Rarity color: value 1 gray, 2 blue, 3 purple.

## Setup
1. Randomly choose a starting player.
2. **Build the board.** Each player takes one 15-tile set, shuffles it face down and keeps the top tiles for their player count: **15** tiles with 2–3 players, **12** with 4, **10** with 5. Return the rest to the box unseen. Starting with the start player and going clockwise, take your top tile, turn it face up and place it. Each new tile must touch at least one tile already placed.
3. **Loot.** Put a matching loot cube on every loot icon on the board.
4. In **reverse** turn order (the last player first, the start player last), each player places their pawn on any hex. Players may share a hex.
5. Place the round marker on round 1 of the round track.
6. Shuffle the three supply decks separately and place them face down. Turn the top card of each face up. Those three cards are the **loot display**.
7. Each player sets their stats to Base Move 1, Base Attack 1, Base Shield 0.
8. Each player shuffles their 10-card base deck and draws 5 cards.
9. The start player takes the first turn. Each time play passes the start player's seat, advance the round marker. Keep doing this even after the start player is eliminated.

## Your Turn
Play goes clockwise. Each turn has three phases.

### Phase 1: Upkeep
1. Set your Shield points equal to your Base Shield. Any points left over from last turn are lost.
2. Draw until you have 5 cards in hand. Dead cards still in your hand count toward the 5. If your draw pile runs out, shuffle your discard pile to make a new one and keep drawing.
3. **Critical:** if 3 or more cards in your hand are Dead cards, announce "critical" to the table. You have this turn to heal, or you'll be eliminated at the end of it.

### Phase 2: Actions
You may do the following in any order, and you may mix them:

- **Play any number of cards** from your hand, including none. Dead cards can't be played.
- **Move** up to your total Move: Base Move plus the Move cards you played this turn. You may move some before playing cards and the rest after.
- **Attack once** (see Attacking). You may attack even if you played no Attack cards, since your Base Attack still counts.
- **Loot once** (see Looting).
- **Upgrade** any number of times (see Upgrading).

### Phase 3: End of Turn
1. **Elimination check:** if 3 or more cards in your hand are Dead cards, you are eliminated (see Elimination) and your turn ends; skip the storm.
2. Put your played and unplayed cards in your discard pile. **Dead cards stay in your hand.** Heal cards used to heal are removed from the game instead.
3. **Storm:** you remove one tile from the board (see The Storm).
4. The next player clockwise begins their turn.

## Cards
| Card | When played |
|---|---|
| **Move** (Dash, Movement deck) | Add its value to your Move this turn. |
| **Attack** (Strike, Attack deck) | Add its value to your Attack this turn. |
| **Heal** (Patch Up, Heal deck) | Choose one when you play it: **Heal:** return up to that many Dead cards **from your hand** to the Dead supply, then remove this card from the game. **Shield:** gain that many Shield points (they can go above your Base Shield and protect you until your next upkeep); the card is discarded normally. |

## Attacking
1. Total Attack = Base Attack + Attack cards played this turn.
2. Pick a target. **Range** is the straight-line hex distance from your hex to theirs, counting any removed hexes in between. The same hex is range 0, and an adjacent hex is range 1.
3. **Damage = Total Attack − Range.** If that is 0 or less, the target is out of range and you can't attack them.
   - Example: Attack 4 hits range 0 for 4, range 2 for 2, range 3 for 1, and can't reach range 4.
4. Each of the target's Shield points cancels 1 damage and is then spent.
5. The target puts the remaining damage as Dead cards from the supply **into their discard pile**. They show up when the deck reshuffles.

You only get one attack, so play your Attack cards before you attack.

## Looting
Once per turn, you may take either 1 cube from the hex you're on or one pick from a loot pile there (see Elimination), never both. Return the cube to the general supply and gain a card of that type (Move cube → Movement deck, Attack → Attack deck, Heal → Heal deck). Choose either:
- the **face-up card** of that type in the loot display (then turn the next card of that deck face up), or
- the **top card** of that deck, unseen.

The card goes into your **discard pile**. Cubes taken from tiles never come back. If a deck and its display slot are both empty, you can't loot that type.

## Upgrading
At any time on your turn, pay cards from your hand of one type with a total value of **4** or more to raise that stat by 1:
- Attack cards → Base Attack
- Move cards → Base Move
- Heal cards → Base Shield

Example: a value-3 Move card plus a value-1 Move card raises Base Move by 1. So do two value-2s, or four value-1s.

Paid cards go to your discard pile, not out of the game; they come back when you reshuffle. Cards you pay with can't also be played this turn. You may overpay, but extra value above 4 is lost. Each stat maxes out at 4.

## The Storm
At the end of your turn, you choose and remove one **edge tile** from the board: a tile with at least one side not touching another tile. Any loot cubes on it go back to the supply.

**The board must stay in one piece.** You can't remove a tile if that would split the board into separate islands. Never remove the last tile. If no tile qualifies, skip this step.

The storm moves in two phases, set by the round marker:

| Phase | Rounds | Which tiles the storm can remove |
|---|---|---|
| 1: Closing | 1–7 | Edge tiles with no pawn on them |
| 2: Collapse | 8+ | Any edge tile, even one with pawns on it |

**Push-off (Phase 2):** if you remove a tile with pawns on it, each of those pawns' owners chooses a remaining tile adjacent to the removed one and moves their pawn there. A pawn can be pushed more than once in a game.

Removed tiles are gone. Pawns can't move onto or across the gap, and range is still counted in hexes across the gap.

## Elimination
The elimination check happens only at the end of your own turn. If you are eliminated:
1. Remove your pawn.
2. Put your Dead cards back in the Dead supply. Gather the rest of your hand, deck and discard pile into a face-down **loot pile** on your hex.
3. The loot pile is looted with the normal loot action, but players look through it and choose cards:
    - The first player to loot it keeps up to **5** cards of their choice.
    - The second keeps up to **3**.
    - The third keeps **1**. Then the rest of the pile is removed from the game.
    - If the pile runs out sooner, it is gone.
4. Looted cards go to your discard pile. If the storm removes the tile, the pile is lost.

## Winning
The last player not eliminated wins. There are no ties: players are only eliminated at the end of their own turn, one at a time.

## Loot Tile Set
Each player's set has 15 tiles and 21 loot icons, 7 of each type:

| Tiles | Loot icons on each tile |
|---|---|
| 4 | none |
| 4 | 1 each: Move · Attack · Heal · Heal |
| 4 | 2 each: Move+Attack · Attack+Heal · Heal+Move · Move+Move |
| 3 | 3 each: Move+Attack+Heal · Attack+Attack+Heal · Move+Attack+Heal |

## Quick Reference
**Upkeep:** reset Shield → draw up to 5 (Dead cards in hand count) → 3+ Dead: announce "critical"
**Actions (any order):** play any cards · move · 1 attack · 1 loot (cube or pile pick) · upgrade
**Eliminated:** Dead cards to supply; your other cards become a loot pile (first looter picks 5, then 3, then 1)
**End:** eliminated if 3+ Dead in hand → discard all but Dead cards (Heal cards used to heal leave the game) → storm removes 1 edge tile (never splits the board)
**Damage:** Attack − Range; 0 or less can't hit; Shield absorbs; Dead cards go to the target's discard pile
**Upgrade:** pay 4+ value of one type from hand → +1 stat (max 4); paid cards go to discard

---

## Designer Notes

### Ideas for Later (not in these rules)
- **Design intent: same-hex fights.** Sharing a hex is allowed on purpose. You can go all in for maximum damage, but if you don't get away afterward, they hit you back.
- **Storm damage:** storm tiles that deal Dead cards to anyone who ends a turn on them, possibly escalating to 2 later in the game.
- **Battle bus drop:** players deploy along a straight-line bus path instead of placing anywhere.
- **One-shot weapons:** Attack cards like a Shotgun that leave the game after use.
- **Supply drops (gold deck):** a separate 12-card gold deck of value-2 and value-3 cards of mixed types, shuffled.
    - At the start of rounds 4, 8 and 12, a drop of 2 gold cards lands. The placer puts it on any tile at least 3 hexes from their own pawn. Then each other player, clockwise, may nudge it 1 hex or pass. It can never be nudged off the board or into a gap.
    - Placement rotates: the start player places the round 4 drop, the next player clockwise places round 8, and so on.
    - Looting the drop uses your loot action: take 1 of its cards into your discard pile. The other card stays for the next looter.
    - The storm can't remove a tile with an unlooted drop on it.
    - Simulation: about 3 drops per game, and players grab nearly all of them.
- **8–10 player team variant (needs testing):** duos or squads that share a win. Teammates can revive a knocked-down partner (see Knocked down). Simulation: 10 solo players take about 115 turns, far past 45 minutes, so high player counts need teams or simultaneous turns.
- **Knocked down (team play only):** if you end your turn with 3 or more Dead cards, you're knocked down instead of eliminated. You can be knocked down only once per game; a second time eliminates you.
    - While knocked down, you move at most 1 hex, can't attack or loot, and can only play Heal cards.
    - Get your hand below 3 Dead cards by the end of your next turn to stand back up. Otherwise you're eliminated at the end of that turn.
    - Any hit that lands on you while you're knocked down eliminates you immediately.
    - A teammate on your hex can spend a Heal card on you to revive you. You stand up with that many fewer Dead cards.
- **Special cards:** rare cards with unique effects, such as a **Self-Revive** that lets a solo player survive one end-of-turn elimination check.
- **Walls:** spend a card to place a wall on a hex edge. Walls block movement, and attacks through a wall cost +1 range.
- **Chests:** some tiles are chests. Looting one lets you take the display card and the top card of the deck.
- **Named locations:** each player places one named tile during setup, such as a factory or a village, with richer loot.

### Playtest Questions
- With unlimited plays, how long does a turn take? Time a few.
- Is upgrading worth giving up a turn's cards? Which stat do people upgrade first?
- Heal or Shield: which do players choose, and when? Is a critical turn ever survivable in practice?
- Does removing 1 tile per turn shrink the board at the right pace for 2 players vs 5?
- Do players pick the face-up loot card or gamble on the deck?

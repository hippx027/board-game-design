# Readthrough 5 — 2p, Characters variant, seed 1515
Deal (random): A gets Leech/Heavy -> keeps Heavy (Base Atk 2). B gets Mechanic/Brawler -> keeps Mechanic (upgrades cost 3). Start player: B.
No Medic or Tank dealt; they are tested as thought experiments at the end.
Decks A: A1 M1 A1 H1 A1 | A1 H1 H1 M1 M1   B: H1 M1 H1 A1 A1 | A1 M1 H1 A1 M1
Legendary order: H3 M3 | H4 H4 (drop 1 = H3+M3, drop 2 = H4+H4)
Board: 30 tiles, roughly round, radius ~3. Pawns placed 4 apart.

R1 B: hand H1 M1 H1 A1 A1. Holds H1 H1 (pays nothing; needs 3 Heal). Moves 1, loots Attack (A2 face-up). Discards to 3: keeps H1 H1 A1. Storm 1 marker (edge).
R1 A: A1 M1 A1 H1 A1. Plays M1, moves 2 toward centre, loots A2. Keeps A1 A1 A1 (holding to spike). Storm.
R2 B: draws A1 M1 -> H1 H1 A1 A1 M1. No 3rd Heal. Loots Heal (H2). Keeps H1 H1 A1.
R2 A: A1A1A1 + H1 H1. Hold-to-spike: A1x3 + Base 2 = 5 atk, range 4 -> 1 dmg to B (B Shield 0). Keeps H1 H1 + nothing else useful... keeps H1 H1.
R3 DROP (B places, A nudges toward self): H3, M3.
R3 B: draws H1 M1 A1 -> hand H1 H1 H1 M1 A1. **Mechanic pays H1x3 = 3 -> Base Shield 1.** Also moves 1. Keeps A1 M1. Shield refills to 1 next upkeep every turn (Tank ability for free).
R3 A: loots drop H3. Keeps H1 H1.
R4 B: reshuffle; hand incl. M1 M1 A1 A2 D. Pays A1+A2 = 3 -> Base Atk 2. Dead card (from A's hit) sits in hand.
R4 A: A2 A1 A1 + base 2 = 6 atk, range 3 -> 3, B shield 1 -> 2 Dead into B discard.
R5 DROP: H4 H4 (A places it adjacent to self; B nudges 1 away).
R5 B: heals D with H1 (removed). Pays M1 M1 M1 (one looted) -> Base Move 2. Loots drop H4.
R5 A: loots drop H4 -> A shields 4 on next turn.
R6 B: H4 alone pays 3 (overpay) -> Base Shield 2. Paid card goes to discard, comes back = reusable upgrade currency.
R6 A: plays H4 shield -> 4. Attacks 5 at range 2 -> 3 dmg, B shield 2 -> 1 Dead.
R7 (storm fast, 2 markers each, 2 dmg): B at Base Move 2/Atk 2/Shield 2. Upgrades Atk to 3 with A2+A1.
R7-R8: A's H4 is still in A's deck; A's shield persists at 4 until used, B's attacks (3-5) mostly absorbed. B's Shield 2 refills every upkeep, so A's hits land 1-2 Dead.
R8 B: Base Atk 4 (pays A3 looted). Base 4 alone = 4 dmg range 0/ 2 at range 2 every turn with no cards.
R9: storm covers ~all but 3 tiles. A: 3 Dead in hand at upkeep ("critical"), heals 2 with H1+H2, survives with 1.
R10 B: same tile as A, Atk 4 + A1 A1 = 6 vs A shield 1 -> 5 Dead. Storm 2 more.
R10 A: draws into 3 Dead + 2 more, no Heal in hand -> eliminated end of turn. **B (Mechanic) wins, round 10.**

## Exploit notes
- Mechanic: base deck's 3 Move 1 / 3 Heal 1 exactly pay an upgrade; holding 3 cards at discard-to-3 makes it reliable. Paid cards recycle, so B upgraded 5 times by R8. Strong.
- Mechanic "cost 3" vs core "total value of 4 or more ... extra value above 4 is lost" — core text hard-codes 4.
- Medic (thought test): holds 1 Heal card each turn; H1 removes 3 Dead, back to discard, reshuffles. With H4 (drop) it removes 6 Dead and recycles: near-immunity. Holding + discard-to-3 means always keep a Heal. Strong / near game-breaking in 2p.
- Tank (thought test): Base Shield 1 refills each upkeep; in 2p one attack per turn cycle so every attack -1. Cost 5 means H4 alone can't upgrade; paying Heal to raise Base Shield costs 5. Tank still gets Base Shield upgrades from Heal - Mechanic got the same Shield 1 for 3 Heal 1s on turn 3, which makes Tank strictly worse-looking.

# Readthrough 4, 3p, seed 1101

Board 45 tiles; edge tiles=26, interior=19
Agg pawn (-2, 0)
Cau pawn (3, -1)
Loot pawn (2, 2)
R1 Agg @(-2, 0) sh0 bm1ba1bs0 hand[M1 M1 M1 A1 H1] deck5 disc0
  move (-2, 0)->(2, -1) (move 4)
  ATTACK Cau atk2 rng1 dmg1 shield-0 => 1 Dead to discard
  loot M cube -> ('M', 3) (display M now [('M', 2), ('M', 2)])
  storm now 1/45
R1 Cau @(3, -1) sh0 bm1ba1bs0 hand[A1 M1 A1 H1 H1] deck5 disc1
  shield ('H', 1): 0->1
  move (3, -1)->(1, 1) (move 2)
  ATTACK Agg atk3 rng2 dmg1 shield-0 => 1 Dead to discard
  loot M cube -> ('M', 2) (display M now [('M', 2), ('M', 1)])
  storm now 2/45
R1 Loot @(2, 2) sh0 bm1ba1bs0 hand[A1 A1 A1 H1 M1] deck5 disc0
  ATTACK Agg atk4 rng3 dmg1 shield-0 => 1 Dead to discard
  loot A cube -> ('A', 2) (display A now [('A', 1), ('A', 2)])
  storm now 3/45
R2 Agg @(2, -1) sh0 bm1ba1bs0 hand[H1 H1 A1 H1 A1] deck1 disc7
  move (2, -1)->(1, 0) (move 1)
  ATTACK Cau atk3 rng1 dmg2 shield-1 => 1 Dead to discard
  loot A cube -> ('A', 2) (display A now [('A', 1), ('A', 3)])
  storm now 4/45
R2 Cau @(1, 1) sh0 bm1ba1bs0 hand[H1 H1 A1 M1 A1] deck1 disc7
  shield ('H', 1): 0->1
  move (1, 1)->(-1, 2) (move 2)
  ATTACK Agg atk3 rng2 dmg1 shield-0 => 1 Dead to discard
  loot A cube -> ('A', 3) (display A now [('A', 1), ('A', 3)])
  storm now 5/45
R2 Loot @(2, 2) sh0 bm1ba1bs0 hand[H1 M1 M1 A1 H1] deck1 disc5
  move (2, 2)->(2, 3) (move 3)
  loot A cube -> ('A', 3) (display A now [('A', 1), ('A', 2)])
  storm now 6/45
R3 SUPPLY DROP by Agg: [('A', 3), ('H', 3)] at (1, 0)
  Cau nudges drop to (0, 1)
  Loot nudges drop to (1, 1)
   reshuffle
R3 Agg @(1, 0) sh0 bm1ba1bs0 hand[H1 H1 H1 A1 X] deck10 disc0
  heal ('H', 1) removes 1 Dead (card out of game)
  move (1, 0)->(0, 1) (move 1)
  ATTACK Cau atk2 rng1 dmg1 shield-1 => 0 Dead to discard
  loot H cube -> ('H', 2) (display H now [('H', 1), ('H', 2)])
  storm now 7/45
   reshuffle
R3 Cau @(-1, 2) sh0 bm1ba1bs0 hand[H1 M1 X X A1] deck9 disc0
  heal ('H', 1) removes 1 Dead (card out of game)
  move (-1, 2)->(-3, 2) (move 2)
  loot M cube -> ('M', 2) (display M now [('M', 1), ('M', 1)])
  storm now 8/45
   reshuffle
R3 Loot @(2, 3) sh0 bm1ba1bs0 hand[A1 H1 H1 H1 A3] deck7 disc0
  UPGRADE ba->2 paying [('A', 3), ('A', 1)]
  loot M cube -> ('M', 1) (display M now [('M', 1), ('M', 1)])
  storm now 9/45
  STORM damage 1
R4 Agg @(0, 1) sh0 bm1ba1bs0 hand[H1 H1 M1 A2 M1] deck7 disc2
  move (0, 1)->(-3, 2) (move 3)
  ATTACK Cau atk3 rng0 dmg3 shield-0 => 3 Dead to discard
  loot H cube -> ('H', 2) (display H now [('H', 1), ('H', 1)])
  storm now 10/45
  STORM damage 1
R4 Cau @(-3, 2) sh0 bm1ba1bs0 hand[X A1 A1 H1 M1] deck6 disc5
  heal ('H', 1) removes 1 Dead (card out of game)
  move (-3, 2)->(-1, 2) (move 2)
  ATTACK Agg atk3 rng2 dmg1 shield-0 => 1 Dead to discard
  loot H cube -> ('H', 1) (display H now [('H', 1), ('H', 3)])
  storm now 11/45
R4 Loot @(2, 3) sh0 bm1ba2bs0 hand[H1 H1 H1 M1 M1] deck5 disc4
  move (2, 3)->(1, 1) (move 3)
  loot DROP card ('A', 3)
  storm now 12/45
  old drop leftovers removed: [('H', 3)]
R5 SUPPLY DROP by Cau: [('H', 3), ('A', 2)] at (-1, 2)
  Agg nudges drop to (-2, 2)
  Loot nudges drop to (-1, 2)
R5 Agg @(-3, 2) sh0 bm1ba1bs0 hand[H1 H1 X M3 X] deck4 disc8
  heal ('H', 1) removes 1 Dead (card out of game)
  heal ('H', 1) removes 1 Dead (card out of game)
  move (-3, 2)->(-1, 2) (move 4)
  ATTACK Cau atk1 rng0 dmg1 shield-0 => 1 Dead to discard
  loot DROP card ('H', 3)
  storm now 13/45
R5 Cau @(-1, 2) sh0 bm1ba1bs0 hand[A3 H1 M1 M2 A1] deck1 disc10
  UPGRADE ba->2 paying [('A', 3), ('A', 1)]
  move (-1, 2)->(0, -2) (move 4)
  loot M cube -> ('M', 1) (display M now [('M', 1), ('M', 1)])
  storm now 14/45
R5 Loot @(1, 1) sh0 bm1ba2bs0 hand[H1 H1 H1 A2 A1] deck3 disc7
  move (1, 1)->(1, 2) (move 1)
  ATTACK Agg atk5 rng2 dmg3 shield-0 => 3 Dead to discard
  loot M cube -> ('M', 1) (display M now [('M', 1), ('M', 2)])
  storm now 15/45
   reshuffle
R6 Agg @(-1, 2) sh0 bm1ba1bs0 hand[A1 M1 A1 A1 A1] deck12 disc0
  UPGRADE ba->2 paying [('A', 1), ('A', 1), ('A', 1), ('A', 1)]
  move (-1, 2)->(1, 2) (move 2)
  ATTACK Loot atk2 rng0 dmg2 shield-0 => 2 Dead to discard
  loot A cube -> ('A', 2) (display A now [('A', 1), ('A', 1)])
  storm now 16/45
   reshuffle
R6 Cau @(0, -2) sh0 bm1ba2bs0 hand[H1 A1 A1 A1 M1] deck12 disc0
  move (0, -2)->(-1, -2) (move 2)
  loot A cube -> ('A', 1) (display A now [('A', 1), ('A', 1)])
  discard to 3: tossed A1, keep [H1 A1 A1]
  storm now 17/45
R6 Loot @(1, 2) sh0 bm1ba2bs0 hand[H1 H1 H1 M1 A1] deck1 disc12
  move (1, 2)->(-1, 2) (move 2)
  ATTACK Agg atk3 rng2 dmg1 shield-0 => 1 Dead to discard
  loot DROP card ('A', 2)
  drop emptied, marker removed
  storm now 18/45
R7 SUPPLY DROP by Loot: [('M', 3), ('M', 3)] at (-1, 2)
  Agg nudges drop to (0, 2)
  Cau nudges drop to (-1, 2)
R7 Agg @(1, 2) sh0 bm1ba2bs0 hand[X H2 X X M3] deck7 disc7 CRITICAL
  heal ('H', 2) removes 2 Dead (card out of game)
  move (1, 2)->(-1, 2) (move 4)
  ATTACK Loot atk2 rng0 dmg2 shield-0 => 2 Dead to discard
  loot DROP card ('M', 3)
  storm now 20/45
R7 Cau @(-1, -2) sh0 bm1ba2bs0 hand[H1 A1 A1 M1 M1] deck10 disc3
  move (-1, -2)->(0, -1) (move 3)
  ATTACK Agg atk4 rng3 dmg1 shield-0 => 1 Dead to discard
  loot M cube -> ('M', 2) (display M now [('M', 1), ('M', 1)])
  storm now 22/45
   reshuffle
R7 Loot @(-1, 2) sh0 bm1ba2bs0 hand[H1 H1 H1 A1 M1] deck16 disc0
  ATTACK Agg atk3 rng0 dmg3 shield-0 => 3 Dead to discard
  loot DROP card ('M', 3)
  drop emptied, marker removed
  storm now 24/45
R8 Agg @(-1, 2) sh0 bm1ba2bs0 hand[X X H2 H3 M1] deck3 disc13
  heal ('H', 3) removes 2 Dead (card out of game)
  ATTACK Loot atk2 rng0 dmg2 shield-0 => 2 Dead to discard
  loot A cube -> ('A', 1) (display A now [('A', 1), ('A', 3)])
  storm now 26/45
R8 Cau @(0, -1) sh0 bm1ba2bs0 hand[H1 X X X H1] deck6 disc8 CRITICAL
  heal ('H', 1) removes 1 Dead (card out of game)
  heal ('H', 1) removes 1 Dead (card out of game)
  move (0, -1)->(0, 0) (move 1)
  loot A cube -> ('A', 3) (display A now [('A', 1), ('A', 2)])
  storm now 28/45
R8 Loot @(-1, 2) sh0 bm1ba2bs0 hand[H1 H1 H1 X A1] deck14 disc5
  heal ('H', 1) removes 1 Dead (card out of game)
  move (-1, 2)->(0, 1) (move 1)
  ATTACK Agg atk3 rng1 dmg2 shield-0 => 2 Dead to discard
  loot A cube -> ('A', 2) (display A now [('A', 1), ('A', 2)])
  storm now 30/45
   reshuffle
R9 Agg @(-1, 2) sh0 bm1ba2bs0 hand[H2 X M1 A2 X] deck16 disc0
  heal ('H', 2) removes 2 Dead (card out of game)
  move (-1, 2)->(0, 1) (move 2)
  ATTACK Loot atk4 rng0 dmg4 shield-0 => 4 Dead to discard
  storm now 32/45
R9 Cau @(0, 0) sh0 bm1ba2bs0 hand[X A1 X M2 M2] deck2 disc9
  UPGRADE bm->2 paying [('M', 2), ('M', 2)]
  move (0, 0)->(-2, 1) (move 2)
  ATTACK Agg atk3 rng2 dmg1 shield-0 => 1 Dead to discard
  loot A cube -> ('A', 2) (display A now [('A', 1), ('A', 2)])
  storm now 34/45
R9 Loot @(0, 1) sh0 bm1ba2bs0 hand[H1 H1 X A1 A1] deck11 disc11
  heal ('H', 1) removes 1 Dead (card out of game)
  move (0, 1)->(-1, 1) (move 1)
  ATTACK Agg atk4 rng1 dmg3 shield-0 => 3 Dead to discard
  storm now 36/45
R10 Agg @(0, 1) sh0 bm1ba2bs0 hand[M1 A1 A1 X A1] deck11 disc6
  move (0, 1)->(-1, 1) (move 2)
  ATTACK Loot atk5 rng0 dmg5 shield-0 => 5 Dead to discard
  storm now 38/45
  STORM damage 2
   reshuffle
R10 Cau @(-2, 1) sh0 bm2ba2bs0 hand[X X M1 A3 M1] deck12 disc0
  move (-2, 1)->(0, 3) (move 4)
  ATTACK Agg atk5 rng3 dmg2 shield-0 => 2 Dead to discard
  loot A cube -> ('A', 2) (display A now [('A', 1), ('A', 1)])
  storm now 40/45
R10 Loot @(-1, 1) sh0 bm1ba2bs0 hand[H1 M1 X M1 A2] deck7 disc18
  heal ('H', 1) removes 1 Dead (card out of game)
  move (-1, 1)->(2, 1) (move 3)
  ATTACK Cau atk4 rng2 dmg2 shield-0 => 2 Dead to discard
  loot H cube -> ('H', 3) (display H now [('H', 1), ('H', 2)])
  storm now 42/45
R11 Agg @(-1, 1) sh0 bm1ba2bs0 hand[X X A1 X X] deck7 disc14 CRITICAL
  move (-1, 1)->(0, 1) (move 1)
  ATTACK Cau atk3 rng2 dmg1 shield-0 => 1 Dead to discard
  ELIMINATED with 4 Dead in hand
R11 Cau @(0, 3) sh0 bm2ba2bs0 hand[X X M2 A1 A1] deck9 disc7
  move (0, 3)->(-2, 4) (move 4)
  loot A cube -> ('A', 1) (display A now [('A', 1), ('A', 1)])
  discard to 3: tossed A1, keep [X X A1]
  storm now 44/45
R11 Loot @(2, 1) sh0 bm1ba2bs0 hand[A3 A3 X M1 X] deck2 disc22
  UPGRADE ba->3 paying [('A', 3), ('A', 3)]
  move (2, 1)->(1, 1) (move 2)
  loot A cube -> ('A', 1) (display A now [('A', 1), ('A', 2)])
  storm now 45/45
  STORM damage 2
R12 Cau @(-2, 4) sh0 bm2ba2bs0 hand[X X A1 M1 A1] deck7 disc10
  move (-2, 4)->(-4, 3) (move 3)
  loot H cube -> ('H', 2) (display H now [('H', 1), ('H', 1)])
  discard to 3: tossed A1, keep [X X A1]
  storm now 45/45
  STORM damage 2
   reshuffle
R12 Loot @(1, 1) sh0 bm1ba3bs0 hand[X X M1 A2 X] deck27 disc0 CRITICAL
  move (1, 1)->(0, 1) (move 2)
  ATTACK Cau atk5 rng4 dmg1 shield-0 => 1 Dead to discard
  claim pile #1 takes [('M', 3), ('M', 3), ('A', 2), ('A', 2), ('A', 1)]
  ELIMINATED with 3 Dead in hand
END round 12: alive ['Cau']
Agg dealt22 took20 storm3 loots8 ups1 healed9
Cau dealt7 took10 storm2 loots12 ups2 healed4
Loot dealt16 took15 storm3 loots11 ups2 healed3
issues flagged: {'healwaste'}

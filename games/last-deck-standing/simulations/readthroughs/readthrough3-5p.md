# Readthrough 3, 5p, seed 808 (script g.py, heuristic choices; movement abstracted as hex distance)

Start player P0
Board 50 tiles, cubes M21 A23 H24
P0 pawn (2, -3)
P1 pawn (3, 0)
P2 pawn (0, -4)
P3 pawn (-5, 2)
P4 pawn (5, -3)
R1 P0 @(2, -3) hand H1A1A1M1A1 mv2->(1, -4) ATK P2 att4 dmg3(shield0) LOOT ('H', 1) | held 0 storm1/50 dead_supply57 stats M1A1S0
R1 P1 @(3, 0) hand A1M1A1A1H1 mv2->(5, -2) ATK P4 att4 dmg3(shield0) LOOT ('H', 1) | held 0 storm2/50 dead_supply54 stats M1A1S0
R1 P2 @(0, -4) hand M1A1A1H1A1 mv2->(1, -4) ATK P0 att4 dmg3(shield1) LOOT ('A', 1) | held 0 storm3/50 dead_supply51 stats M1A1S0
R1 P3 @(-5, 2) hand M1A1M1H1H1 mv3->(-2, 0) | held 2 storm4/50 dead_supply51 stats M1A1S0
R1 P4 @(5, -3) hand H1M1H1A1H1 mv2->(5, -2) ATK P1 att2 dmg1(shield1) LOOT ('A', 1) | held 1 storm5/50 dead_supply50 stats M1A1S0
R2 P0 @(1, -4) hand A1M1H1H1M1 mv3->(-1, -1) ATK P3 att2 dmg1(shield0) LOOT ('M', 3) | held 1 storm6/50 dead_supply49 stats M1A1S0
R2 P1 @(5, -2) hand H1A1M1H1M1 mv3->(5, -2) ATK P4 att2 dmg0(shield2) LOOT ('M', 1) | held 1 storm7/50 dead_supply49 stats M1A1S0
R2 P2 @(1, -4) hand M1A1M1H1H1 mv3->(-1, -1) ATK P0 att2 dmg1(shield1) | held 1 storm8/50 dead_supply48 stats M1A1S0
R2 P3 @(-2, 0) hand H1H1A1H1M1 mv2->(-1, -1) ATK P2 att2 dmg1(shield1) | held 2 storm9/50 dead_supply47 stats M1A1S0
R2 P4 @(5, -2) hand H1A1A1M1A1 mv2->(4, -1) ATK P1 att4 dmg2(shield1) LOOT ('A', 2) | held 1 storm10/50 dead_supply45 stats M1A1S0
R3 SUPPLY DROP placed by P0 at (5, -3) [('M', 2), ('M', 2)]
  P3 nudges to (4, -3)
R3 P0 @(-1, -1) hand H1DA1A1M1 heal1(-1D) mv2->(-1, -1) ATK P3 att3 dmg2(shield1) | held 0 storm11/50 dead_supply44 stats M1A1S0
R3 P1 @(5, -2) hand H1M1H1A1D heal1(-1D) mv2->(4, -3) DROP ('M', 2) | held 0 storm12/50 dead_supply45 stats M1A1S0
R3 P2 @(-1, -1) hand H1M1A1H1D heal1(-1D) mv2->(-1, -1) ATK P3 att2 dmg2(shield0) | held 0 storm13/50 dead_supply44 stats M1A1S0
R3 P3 @(-1, -1) hand H1H1A1A1D heal1(-1D) mv1->(-1, -1) ATK P2 att3 dmg2(shield1) | held 0 storm14/50 dead_supply43 stats M1A1S0
R3 P4 @(4, -1) hand H1M1M1A1D heal1(-1D) mv3->(4, -3) ATK P1 att2 dmg1(shield1) DROP ('M', 2) | held 0 storm15/50 dead_supply43 stats M1A1S0
R4 P0 @(-1, -1) hand M3DH1M1H1 heal1(-1D) mv5->(4, -3) ATK P4 att1 dmg1(shield0) LOOT ('H', 1) | held 0 storm16/50 dead_supply43 stats M1A1S0
R4 P1 @(4, -3) hand A1M1DM1A1 mv3->(3, -2) ATK P4 att3 dmg2(shield0) LOOT ('M', 2) | held 0 storm17/50 dead_supply41 stats M1A1S0
R4 P2 @(-1, -1) hand DM1A1DM1 mv3->(2, -2) ATK P1 att2 dmg1(shield0) LOOT ('A', 2) | held 0 storm18/50 dead_supply40 stats M1A1S0
R4 P3 @(-1, -1) hand DDDA1M1 CRITICAL mv2->(1, -1) ATK P2 att2 dmg1(shield0) LOOT ('H', 2) ELIMINATED
R4 P4 @(4, -3) hand M1A2A1A1D mv2->(3, -2) ATK P1 att5 dmg5(shield0) LOOT ('M', 3) | held 0 storm19/50 dead_supply38 stats M1A1S0
R5 SUPPLY DROP placed by P1 at (1, 5) [('M', 3), ('M', 2)]
  P0 nudges to (1, 4)
R5 P0 @(4, -3) hand A1H1A1DM1 heal1(-1D) mv2->(2, -2) ATK P2 att3 dmg3(shield0) LOOT ('H', 3) | held 0 storm20/50 dead_supply36 stats M1A1S0
R5 P1 @(3, -2) hand DH1A1M1D heal1(-1D) mv2->(1, -1) ATK P2 att2 dmg1(shield0) CLAIM#1 pile 5c | held 0 storm21/50 dead_supply36 stats M1A1S0
R5 P2 @(2, -2) hand DDA1A1H1 heal1(-1D) mv1->(1, -1) ATK P1 att3 dmg3(shield0) CLAIM#2 pile 3c | held 0 storm22/50 dead_supply34 stats M1A1S0
R5 P4 @(3, -2) hand DH1H1A1A1 heal1(-1D) mv1->(2, -2) ATK P0 att3 dmg3(shield0) | held 1 storm23/50 dead_supply32 stats M1A1S0
R6 P0 @(2, -2) hand DA1A1H1H1 heal1(-1D) mv1->(1, -1) ATK P2 att3 dmg3(shield0) CLAIM#3 pile 1c (pile gone) | held 0 storm24/50 dead_supply30 stats M1A1S0
R6 P1 @(1, -1) hand DH1DDD CRITICAL heal1(-1D) mv1->(1, -1) ATK P2 att1 dmg1(shield0) ELIMINATED
R6 P2 @(1, -1) hand DDA1A1D CRITICAL mv1->(1, -1) ATK P0 att3 dmg2(shield1) CLAIM#1 pile 5c ELIMINATED
R6 P4 @(2, -2) hand H1DM2M3A2 heal1(-1D) mv6->(1, -1) ATK P0 att3 dmg3(shield0) CLAIM#1 pile 5c | held 0 storm25/50 dead_supply49 stats M1A1S0
R7 SUPPLY DROP placed by P4 at (4, -2) [('A', 3), ('M', 3)]
R7 P0 @(1, -1) hand H3DA1M1M1 heal3(-1D) mv3->(1, -1) ATK P4 att2 dmg2(shield0) CLAIM#2 pile 3c | held 0 storm27/50 dead_supply48 stats M1A1S0
R7 P4 @(1, -1) hand A1M1M1DA1 mv3->(1, -1) ATK P0 att3 dmg3(shield0) CLAIM#3 pile 1c (pile gone) | held 0 storm29/50 dead_supply45 stats M1A1S0
R8 P0 @(1, -1) hand A1M3DDM1 mv5->(4, -2) DROP ('M', 3) | held 0 storm31/50 dead_supply45 stats M1A1S0
R8 P4 @(1, -1) hand DA1DM1A1 mv2->(3, -2) ATK P0 att3 dmg2(shield0) | held 0 storm33/50 dead_supply43 stats M1A1S0
R9 SUPPLY DROP placed by P4 at (1, -4) [('H', 3), ('M', 2)]
  P0 nudges to (2, -4)
R9 P0 @(4, -2) hand DDDDH1 CRITICAL heal1(-1D) mv1->(3, -2) ATK P4 att1 dmg1(shield0) ELIMINATED
WINNER P4 round 9

## Rules snags hit in play
- R5 drop still on board (unlooted) when R7 drop arrives; only 1 drop marker. Script replaced it.
- R6: P1 and P2 eliminated on same tile (1,-1): two loot piles on one tile, only one 'claim on a loot pile there'; which pile? Script overwrote (bug-equivalent of rule gap).
- R9: 5 drops at 5p though 2 alive; placer rotation after eliminations put P4 twice (R7, R9).
- R4 P3 held DDD from draw; no Heal in hand -> dead on arrival, turn still fully played (attack/loot) before elimination.
- Storm never reached all 50 tiles; game ended R9.

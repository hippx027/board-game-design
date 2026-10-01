# Readthrough 5 - 4p blind game (seed 1414)

```
Start player: P2
Board: 48 tiles, cubes 68
P2 pawn at (-3, -1)
P3 pawn at (3, -3)
P4 pawn at (-2, 1)
P1 pawn at (4, -1)
Display: {'A': [('A', 3), ('A', 3)], 'M': [('M', 1), ('M', 3)], 'H': [('H', 1), ('H', 3)]}
[R1] P2 @(-3, -1) hand H1A1M1A1H1 B(M1A1S0) sh0
   moves (-3, -1)->(-2, 0) (2)
   ATTACKS P4 A3 rng1 shield-0 => 2 Dead
   loots M cube -> ('M', 3)
[R1] P3 @(3, -3) hand M1M1A1H1H1 B(M1A1S0) sh0
   moves (3, -3)->(3, 0) (3)
   ATTACKS P1 A2 rng1 shield-0 => 1 Dead
   loots A cube -> ('A', 3)
[R1] P4 @(-2, 1) hand H1M1A1A1A1 B(M1A1S0) sh0
   moves (-2, 1)->(-2, 0) (1)
   ATTACKS P2 A4 rng0 shield-0 => 4 Dead
[R1] P1 @(4, -1) hand H1M1M1A1M1 B(M1A1S0) sh0
   moves (4, -1)->(3, 0) (1)
   ATTACKS P3 A2 rng0 shield-0 => 2 Dead
   loots H cube -> ('H', 3)
   shields +1 -> 1
   ends on storm: +1 Dead

=== ROUND 2 ===
[R2] P2 @(-2, 0) hand H1H1A1M1M1 B(M1A1S0) sh0
   moves (-2, 0)->(-1, 0) (1)
   ATTACKS P4 A2 rng1 shield-0 => 1 Dead
   loots A cube -> ('A', 3)
   shields +1 -> 1
[R2] P3 @(3, 0) hand H1H1M1A1H1 B(M1A1S0) sh0
   ATTACKS P1 A2 rng0 shield-1 => 1 Dead
   loots M cube -> ('M', 1)
   shields +1 -> 1
   ends on storm: +1 Dead
[R2] P4 @(-2, 0) hand H1M1M1A1M1 B(M1A1S0) sh0
   moves (-2, 0)->(2, 0) (4)
   ATTACKS P1 A2 rng1 shield-0 => 1 Dead
   loots A cube -> ('A', 2)
[R2] P1 @(3, 0) hand M1M1M1H1H1 B(M1A1S0) sh0
   moves (3, 0)->(2, 0) (1)
   ATTACKS P4 A1 rng0 shield-0 => 1 Dead
   shields +1 -> 1
   ends on storm: +1 Dead

=== ROUND 3 ===
  SUPPLY DROP by P2: [('H', 3), ('M', 4)] at (0, 0)
   P3 nudges to (1, 0)
   P4 nudges to (2, 0)
[R3] P2 @(-1, 0) hand H1M1M1H1A1 B(M1A1S0) sh1
   moves (-1, 0)->(2, 0) (3)
   ATTACKS P4 A2 rng0 shield-0 => 2 Dead
   loots DROP ('H', 3)
   ends on storm: +1 Dead
[R3] P3 @(3, 0) hand H1H1M1A1A1 B(M1A1S0) sh1
   moves (3, 0)->(2, 0) (1)
   ATTACKS P4 A3 rng0 shield-0 => 3 Dead
   loots DROP ('M', 4)
   ends on storm: +1 Dead
[R3] P4 @(2, 0) hand H1H1H1D0A1 B(M1A1S0) sh0
   heals 1 with H1 (card removed)
   moves (2, 0)->(2, 1) (1)
   ATTACKS P3 A2 rng1 shield-1 => 0 Dead
   loots A cube -> ('A', 2)
[R3] P1 @(2, 0) hand H1M1M1A1A1 B(M1A1S0) sh1
   moves (2, 0)->(2, 1) (1)
   ATTACKS P4 A3 rng0 shield-0 => 3 Dead
   ends on storm: +1 Dead

=== ROUND 4 ===
[R4] P2 @(2, 0) hand H1H1D0M1M1 B(M1A1S0) sh1
   heals 1 with H1 (card removed)
   moves (2, 0)->(1, 1) (1)
   loots A cube -> ('A', 2)
[R4] P3 @(2, 0) hand H1H1M1A1A1 B(M1A1S0) sh0
   moves (2, 0)->(1, 2) (2)
   ATTACKS P4 A3 rng1 shield-0 => 2 Dead
   loots A cube -> ('A', 2)
[R4] P4 @(2, 1) hand H1H1M1D0A1 B(M1A1S0) sh0
   heals 1 with H1 (card removed)
   moves (2, 1)->(1, 2) (1)
   ATTACKS P3 A2 rng0 shield-0 => 2 Dead
   loots A cube -> ('A', 1)
   ends on storm: +1 Dead
[R4] P1 @(2, 1) hand H1M1M1A1A1 B(M1A1S0) sh1
   moves (2, 1)->(1, 2) (1)
   ATTACKS P4 A3 rng0 shield-0 => 3 Dead
   loots M cube -> ('M', 2)
   ends on storm: +1 Dead

=== ROUND 5 ===
  SUPPLY DROP by P3: [('M', 3), ('A', 4)] at (0, 2)
   P2 nudges to (1, 1)
   P4 nudges to (1, 2)
[R5] P2 @(1, 1) hand H1M1M1A1A1 B(M1A1S0) sh1
   moves (1, 1)->(1, 2) (1)
   ATTACKS P4 A3 rng0 shield-0 => 3 Dead
   loots DROP ('M', 3)
   ends on storm: +1 Dead
[R5] P3 @(1, 2) hand H1H1M1D0A3 B(M1A1S0) sh0
   heals 1 with H1 (card removed)
   ATTACKS P4 A4 rng0 shield-0 => 4 Dead
   loots DROP ('A', 4)
   ends on storm: +1 Dead
[R5] P4 @(1, 2) hand H1M1D0D0A1 B(M1A1S0) sh0
   heals 1 with H1 (card removed)
   moves (1, 2)->(1, 3) (1)
   ATTACKS P3 A2 rng1 shield-0 => 1 Dead
   loots A cube -> ('A', 1)
[R5] P1 @(1, 2) hand H1M1M1D0M1 B(M1A1S0) sh1
   heals 1 with H1 (card removed)
   moves (1, 2)->(1, 3) (1)
   ATTACKS P4 A1 rng0 shield-0 => 1 Dead
   loots H cube -> ('H', 3)
   ends on storm: +1 Dead

=== ROUND 6 ===
[R6] P2 @(1, 2) hand H1M1M1D0A1 B(M1A1S0) sh1
   heals 1 with H1 (card removed)
   ATTACKS P3 A2 rng0 shield-0 => 2 Dead
   ends on storm: +1 Dead
[R6] P3 @(1, 2) hand H1M1D0D0M1 B(M1A1S0) sh0
   heals 1 with H1 (card removed)
   moves (1, 2)->(-1, 1) (3)
   loots A cube -> ('A', 1)
[R6] P4 @(1, 3) hand D0M1D0M1D0 B(M1A1S0) sh0 CRITICAL
   moves (1, 3)->(-2, 3) (3)
   loots A cube -> ('A', 1)
   *** P4 ELIMINATED with 3 Dead in hand ***
[R6] P1 @(1, 3) hand M1M1M1A1D0 B(M1A1S0) sh1
   moves (1, 3)->(-1, 1) (4)
   ATTACKS P3 A2 rng0 shield-0 => 2 Dead
   ends on storm: +1 Dead

=== ROUND 7 ===
  SUPPLY DROP by P1: [('H', 4), ('A', 3)] at (0, 0)
   P2 nudges to (1, 0)
   P3 nudges to (0, 0)
[R7] P2 @(1, 2) hand M1M1A3D0A1 B(M1A1S0) sh1
   moves (1, 2)->(0, 0) (3)
   ATTACKS P3 A5 rng1 shield-0 => 4 Dead
   loots DROP ('H', 4)
   ends on storm: +2 Dead
[R7] P3 @(-1, 1) hand D0H1A1A1D0 B(M1A1S0) sh0
   heals 1 with H1 (card removed)
   moves (-1, 1)->(0, 0) (1)
   ATTACKS P2 A3 rng0 shield-1 => 2 Dead
   loots DROP ('A', 3)
   ends on storm: +2 Dead
[R7] P1 @(-1, 1) hand D0D0D0A1H3 B(M1A1S0) sh1 CRITICAL
   heals 3 with H3 (card removed)
   moves (-1, 1)->(0, 0) (1)
   ATTACKS P3 A2 rng0 shield-0 => 2 Dead
   ends on storm: +2 Dead

=== ROUND 8 ===
[R8] P2 @(0, 0) hand D0M1D0H1H3 B(M1A1S0) sh0
   heals 2 with H3 (card removed)
   moves (0, 0)->(2, -2) (2)
   loots H cube -> ('H', 1)
   ends on storm: +2 Dead
[R8] P3 @(0, 0) hand D0M4M1D0D0 B(M1A1S0) sh0 CRITICAL
   UPGRADE bm -> 2 paying [('M', 1), ('M', 4)]
   moves (0, 0)->(2, -2) (2)
   ATTACKS P2 A1 rng0 shield-0 => 1 Dead
   *** P3 ELIMINATED with 3 Dead in hand ***
[R8] P1 @(0, 0) hand H1D0H1D0D0 B(M1A1S0) sh1 CRITICAL
   heals 1 with H1 (card removed)
   heals 1 with H1 (card removed)
   moves (0, 0)->(1, 0) (1)
   loots M cube -> ('M', 2)
   ends on storm: +2 Dead

=== ROUND 9 ===
  SUPPLY DROP by P1: [('M', 4), ('H', 3)] at (3, -2)
   P2 nudges to (2, -2)
[R9] P2 @(2, -2) hand H1M3D0A3M1 B(M1A1S0) sh0
   heals 1 with H1 (card removed)
   UPGRADE bm -> 2 paying [('M', 1), ('M', 3)]
   ATTACKS P1 A4 rng2 shield-1 => 1 Dead
   claims pile #1: [('A', 4), ('M', 4), ('A', 3), ('A', 3), ('A', 2)]
   ends on storm: +2 Dead
[R9] P1 @(1, 0) hand D0A1D0A1M1 B(M1A1S0) sh0
   moves (1, 0)->(2, -2) (2)
   ATTACKS P2 A3 rng0 shield-0 => 3 Dead
   claims pile #2: [('A', 1), ('A', 1), ('M', 1)]
   ends on storm: +2 Dead

=== ROUND 10 ===
[R10] P2 @(2, -2) hand D0A1H1D0D0 B(M2A1S0) sh0 CRITICAL
   heals 1 with H1 (card removed)
   ATTACKS P1 A2 rng0 shield-0 => 2 Dead
   claims pile #3: [('A', 1)]
   ends on storm: +2 Dead
[R10] P1 @(2, -2) hand D0D0D0H3A1 B(M1A1S0) sh0 CRITICAL
   heals 3 with H3 (card removed)
   ATTACKS P2 A2 rng0 shield-0 => 2 Dead
   loots DROP ('M', 4)
   ends on storm: +2 Dead

=== ROUND 11 ===
[R11] P2 @(2, -2) hand D0D0A1D0M1 B(M2A1S0) sh0 CRITICAL
   ATTACKS P1 A2 rng0 shield-0 => 2 Dead
   loots DROP ('H', 3)
   *** P2 ELIMINATED with 3 Dead in hand ***

WINNER: ['P1'] round 11, turns 35, Dead supply left 47
```

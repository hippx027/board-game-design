# Readthrough 2 - 5p, seed 505 (scripted literal play, g.py)

Assumptions: Dead cards in deck/discard of eliminated player also return to supply (not into pile); tiles placed round-robin until all 50 placed; round advances when turn passes back to seat 0; loot display taken if value>=2 else top.
```
Board 50 tiles, cubes M22 A24 H22
P4 pawn (-3, 0)
P3 pawn (-1, 4)
P2 pawn (-1, 0)
P1 pawn (-3, 0)
P0 pawn (0, -2)
R1 P0@(0, -2) hand=A1A1H1M1H1 B(M1A1S0) shield+2 move->(-1, 0) atk3->P2 r0 dmg3 sh-0 =>3X storm1 -(-2, 5) |tiles49
R1 P1@(-3, 0) hand=A1H1M1H1M1 B(M1A1S0) shield+2 atk2->P4 r0 dmg2 sh-0 =>2X lootA:A1(top) storm1 -(3, -2) |tiles48
R1 P2@(-1, 0) hand=H1M1A1A1H1 B(M1A1S0) shield+2 move->(-3, 0) atk3->P1 r0 dmg3 sh-2 =>1X lootM:M2(disp) storm1 -(3, -3) |tiles47
R1 P3@(-1, 4) hand=A1A1A1A1M1 B(M1A1S0) upgA->2 move->(-1, 3) lootM:M3(top) storm1 -(-2, -2) |tiles46
R1 P4@(-3, 0) hand=M1A1A1A1H1 B(M1A1S0) shield+1 atk4->P1 r0 dmg4 sh-0 =>4X lootH:H2(disp) storm1 -(2, 1) |tiles45
R2 P0@(-1, 0) hand=M1A1H1A1M1 B(M1A1S0) shield+1 move->(-3, 0) atk3->P1 r0 dmg3 sh-0 =>3X storm1 -(0, 3) |tiles44
R2 P1@(-3, 0) hand=A1H1A1M1A1 B(M1A1S0) shield+1 atk4->P0 r0 dmg4 sh-1 =>3X storm1 -(1, 2) |tiles43
R2 P2@(-3, 0) hand=M1H1A1M1A1 B(M1A1S0) shield+1 atk3->P0 r0 dmg3 sh-0 =>3X storm1 -(-1, 4) |tiles42
R2 P3@(-1, 3) hand=M1H1M1H1H1 B(M1A2S0) shield+3 move->(0, 2) lootM:M3(top) storm1 -(-3, -1) |tiles41
R2 P4@(-3, 0) hand=H1A1H1M1M1 B(M1A1S0) shield+2 atk2->P0 r0 dmg2 sh-0 =>2X storm1 -(3, -1) |tiles40
R3 P0@(-3, 0) hand=XXA1H1M1 B(M1A1S0) heal1(-1X) atk2->P1 r0 dmg2 sh-1 =>1X storm1 -(3, 0) |tiles39
R3 P1@(-3, 0) hand=XXA1H1H1 B(M1A1S0) heal1(-1X) heal1(-1X) atk2->P0 r0 dmg2 sh-0 =>2X storm1 -(2, 0) |tiles38
R3 P2@(-3, 0) hand=A1XXXH1 B(M1A1S0) CRITICAL heal1(-1X) atk2->P0 r0 dmg2 sh-0 =>2X storm1 -(-3, 5) |tiles37
R3 P3@(0, 2) hand=M3A1A1M1H1 B(M1A2S0) shield+1 move->(-3, 0) atk4->P0 r0 dmg4 sh-0 =>4X storm1 -(2, -3) |tiles36
R3 P4@(-3, 0) hand=A1H1M1H1H1 B(M1A1S0) shield+3 atk2->P0 r0 dmg2 sh-0 =>2X storm1 -(2, -2) |tiles35
R4 P0@(-3, 0) hand=XA1XXA1 B(M1A1S0) CRITICAL atk3->P1 r0 dmg3 sh-0 =>3X ELIMINATED (3X in hand; 14X in deck/disc) pile 9 cards |tiles35
R4 P1@(-3, 0) hand=M1M1A1M1X B(M1A1S0) atk2->P2 r0 dmg2 sh-0 =>2X lootpile 5:[('H', 1), ('M', 1), ('M', 1), ('A', 1), ('H', 1)] storm1 -(2, -1) |tiles34
R4 P2@(-3, 0) hand=XXH1M1A1 B(M1A1S0) heal1(-1X) atk2->P1 r0 dmg2 sh-0 =>2X lootpile 3:[('A', 1), ('M', 1), ('A', 1)] storm1 -(1, 1) |tiles33
R4 P3@(-3, 0) hand=M1A1A1M3H1 B(M1A2S0) shield+1 upgM->2 atk4->P1 r0 dmg4 sh-0 =>4X lootpile 1:[('A', 1)] storm1 -(0, 2) |tiles32
R4 P4@(-3, 0) hand=A1H2XXA1 B(M1A1S0) heal2(-2X) atk3->P1 r0 dmg3 sh-0 =>3X storm1 -(-4, 5) |tiles31
R5 P1@(-3, 0) hand=XXA1XX B(M1A1S0) CRITICAL atk2->P2 r0 dmg2 sh-0 =>2X ELIMINATED (4X in hand; 15X in deck/disc) pile 14 cards |tiles31
R5 P2@(-3, 0) hand=XH1M1M1M2 B(M1A1S0) heal1(-1X) atk1->P3 r0 dmg1 sh-1 =>0X lootpile 5:[('A', 1), ('A', 1), ('H', 1), ('A', 1), ('H', 1)] storm1 -(-1, 3) |tiles30
R5 P3@(-3, 0) hand=H1M1M1A1A1 B(M2A2S0) shield+1 atk4->P2 r0 dmg4 sh-0 =>4X lootpile 3:[('M', 1), ('M', 1), ('A', 1)] storm1 -(-2, 4) |tiles29
R5 P4@(-3, 0) hand=A1M1M1H1A1 B(M1A1S0) shield+1 atk3->P2 r0 dmg3 sh-0 =>3X lootpile 1:[('H', 1)] storm1 -(1, -2) |tiles28
R6 P2@(-3, 0) hand=A1A1XXX B(M1A1S0) CRITICAL atk3->P3 r0 dmg3 sh-1 =>2X ELIMINATED (3X in hand; 8X in deck/disc) pile 16 cards |tiles28
R6 P3@(-3, 0) hand=M3H1A1H1M1 B(M2A2S0) shield+2 upgM->3 atk3->P4 r0 dmg3 sh-1 =>2X lootpile 5:[('M', 2), ('H', 1), ('A', 1), ('A', 1), ('H', 1)] storm1 -(1, -3) |tiles27
R6 P4@(-3, 0) hand=M1H1A1H1A1 B(M1A1S0) shield+2 atk3->P3 r0 dmg3 sh-2 =>1X lootpile 3:[('A', 1), ('A', 1), ('M', 1)] storm1 -(-3, 4) |tiles26
R7 P3@(-3, 0) hand=M3A1A1A1M1 B(M3A2S0) upgM->4 atk5->P4 r0 dmg5 sh-2 =>3X lootpile 1:[('M', 1)] storm1 -(1, 0) |tiles25
R7 P4@(-3, 0) hand=A1H1A1XM1 B(M1A1S0) heal1(-1X) atk3->P3 r0 dmg3 sh-0 =>3X storm1 -(1, -1) |tiles24
R8 P3@(-3, 0) hand=M1XA1A1H1 B(M4A2S0) heal1(-1X) atk4->P4 r0 dmg4 sh-0 =>4X storm2 -(-3, 0) push P3->(-2, 0) push P4->(-3, 1) |tiles23
R8 P4@(-3, 1) hand=XA1XXA1 B(M1A1S0) CRITICAL move->(-2, 0) atk3->P3 r0 dmg3 sh-0 =>3X lootA:A3(top) ELIMINATED (3X in hand; 5X in deck/disc) pile 14 cards |tiles23
END round 9 turns 31 alive [3]```

# Readthrough 4, 5p, seed 1202 (scripted literal play)

Board: 50 tiles, icons M22 A38 H14
R1 P1 hand['A1', 'M1', 'H1', 'H1', 'M1'] shield->1 shield->2 mv3->(3, 2) atk2 hit P3 2(sh-0) loot('M', 3) | stats M1A1S0 sh2 dead(deck+disc)0 storm1/50
R1 P2 hand['M1', 'M1', 'H1', 'A1', 'A1'] shield->1 mv3->(1, -1) atk3 hit P4 3(sh-0) loot('A', 3) | stats M1A1S0 sh1 dead(deck+disc)0 storm2/50
R1 P3 hand['H1', 'M1', 'A1', 'A1', 'H1'] shield->1 shield->2 mv2->(3, 2) atk3 hit P1 1(sh-2) | stats M1A1S0 sh2 dead(deck+disc)2 storm3/50
R1 P4 hand['A1', 'H1', 'H1', 'M1', 'H1'] shield->1 shield->2 shield->3 mv2->(1, -1) atk2 hit P2 1(sh-1) | stats M1A1S0 sh3 dead(deck+disc)3 storm4/50
R1 P5 hand['A1', 'H1', 'A1', 'A1', 'A1'] shield->1 mv1->(-2, 2) atk5 hit P2 2(sh-0) loot('A', 2) | stats M1A1S0 sh1 dead(deck+disc)0 storm5/50
R2 P1 hand['A1', 'H1', 'M1', 'A1', 'A1'] shield->1 mv2->(3, 1) atk4 hit P3 1(sh-2) loot('H', 2) | stats M1A1S0 sh1 dead(deck+disc)1 storm6/50
R2 P2 hand['H1', 'M1', 'A1', 'A1', 'H1'] shield->1 shield->2 mv2->(1, -1) atk3 hit P4 0(sh-3) | stats M1A1S0 sh2 dead(deck+disc)3 storm7/50
R2 P3 hand['H1', 'A1', 'M1', 'A1', 'M1'] shield->1 mv3->(3, 1) atk3 hit P1 2(sh-1) | stats M1A1S0 sh1 dead(deck+disc)3 storm8/50
R2 P4 hand['A1', 'A1', 'A1', 'M1', 'M1'] mv3->(1, -1) atk4 hit P2 2(sh-2) | stats M1A1S0 sh0 dead(deck+disc)3 storm9/50
R2 P5 hand['H1', 'M1', 'H1', 'M1', 'M1'] shield->2 shield->3 mv4->(1, -1) atk1 hit P2 1(sh-0) | stats M1A1S0 sh3 dead(deck+disc)0 storm10/50
R3 drop by P1 at (3, 0) [('H', 3), ('H', 3)]
R3 P1 hand['M1', 'D', 'H2', 'A1', 'H1'] heal1 shield->1 mv2->(3, 0) atk2 hit P3 0(sh-1) lootDrop('H', 3) | stats M1A1S0 sh1 dead(deck+disc)2 storm11/50
R3 P2 hand['M1', 'A1', 'A3', 'D', 'D'] UPG ba->2 mv2->(1, -1) atk2 hit P4 2(sh-0) | stats M1A2S0 sh0 dead(deck+disc)4 storm12/50
R3 P3 hand['H1', 'D', 'A1', 'A1', 'H1'] heal1 shield->1 mv1->(3, 0) atk3 hit P1 2(sh-1) lootDrop('H', 3) | stats M1A1S0 sh1 dead(deck+disc)2 storm13/50
R3 P4 hand['M1', 'H1', 'D', 'A1', 'D'] heal1 mv2->(1, -1) atk2 hit P2 2(sh-0) | stats M1A1S0 sh0 dead(deck+disc)3 storm14/50
R3 P5 hand['A1', 'A2', 'M1', 'H1', 'A1'] shield->4 mv2->(1, -1) atk5 hit P2 5(sh-0) | stats M1A1S0 sh4 dead(deck+disc)0 storm15/50
R4 P1 hand['A1', 'D', 'H1', 'H1', 'M1'] heal1 shield->1 mv2->(3, 0) atk2 hit P3 1(sh-1) | stats M1A1S0 sh1 dead(deck+disc)3 storm16/50
R4 P2 hand['D', 'D', 'A1', 'M1', 'D'] CRITICAL mv2->(1, -1) atk3 hit P4 3(sh-0) ELIMINATED
R4 P3 hand['D', 'A1', 'M1', 'D', 'M1'] mv3->(3, 0) atk2 hit P1 1(sh-1) | stats M1A1S0 sh0 dead(deck+disc)1 storm17/50
R4 P4 hand['D', 'D', 'M1', 'H1', 'H1'] heal1 heal1 mv2->(1, -1) atk1 hit P5 0(sh-1) pileclaim5 | stats M1A1S0 sh0 dead(deck+disc)5 storm18/50
R4 P5 hand['A1', 'A1', 'M1', 'M1', 'H1'] shield->4 mv3->(1, -1) atk3 hit P4 3(sh-0) pileclaim3 | stats M1A1S0 sh4 dead(deck+disc)0 storm19/50
R5 drop by P3 at (1, -1) [('A', 2), ('H', 2)]
R5 P1 hand['M1', 'D', 'A1', 'A1', 'M3'] mv5->(3, 0) atk3 hit P3 3(sh-0) | stats M1A1S0 sh0 dead(deck+disc)3 storm20/50
R5 P3 hand['D', 'D', 'M1', 'H1', 'A1'] heal1 mv2->(3, 0) atk2 hit P1 2(sh-0) | stats M1A1S0 sh0 dead(deck+disc)4 storm21/50
R5 P4 hand['D', 'A1', 'D', 'M1', 'A1'] mv2->(1, -1) atk3 hit P5 0(sh-3) lootDrop('H', 2) | stats M1A1S0 sh0 dead(deck+disc)6 storm22/50
R5 P5 hand['H1', 'A1', 'A1', 'M1', 'H1'] shield->2 shield->3 mv2->(1, -1) atk3 hit P4 3(sh-0) lootDrop('A', 2) | stats M1A1S0 sh3 dead(deck+disc)0 storm23/50
R6 P1 hand['D', 'M1', 'A1', 'D', 'M1'] mv3->(3, 0) atk2 hit P3 2(sh-0) | stats M1A1S0 sh0 dead(deck+disc)4 storm24/50
R6 P3 hand['D', 'D', 'A1', 'D', 'M1'] CRITICAL mv2->(3, 0) atk2 hit P1 2(sh-0) ELIMINATED
R6 P4 hand['D', 'D', 'A1', 'D', 'H1'] CRITICAL heal1 mv1->(1, -1) atk2 hit P5 0(sh-2) pileclaim1 | stats M1A1S0 sh0 dead(deck+disc)8 storm25/50
R6 P5 hand['A1', 'M1', 'H1', 'M1', 'H1'] shield->2 shield->3 mv3->(1, -1) atk2 hit P4 2(sh-0) | stats M1A1S0 sh3 dead(deck+disc)0 storm26/50
R7 drop by P4 at (1, 0) [('M', 2), ('A', 2)]
R7 P1 hand['D', 'D', 'M3', 'D', 'D'] CRITICAL mv4->(1, 0) atk1 lootDrop('A', 2) ELIMINATED
R7 P4 hand['D', 'D', 'A1', 'M1', 'A3'] mv2->(1, 0) atk5 hit P5 1(sh-3) lootDrop('M', 2) | stats M1A1S0 sh0 dead(deck+disc)10 storm28/50
R7 P5 hand['A2', 'M1', 'A1', 'A1', 'M1'] UPG ba->2 mv3->(1, 0) atk2 hit P4 2(sh-0) pileclaim5 | stats M1A2S0 sh0 dead(deck+disc)1 storm30/50
R8 P4 hand['D', 'D', 'D', 'M1', 'D'] CRITICAL mv2->(1, 0) atk1 hit P5 1(sh-0) pileclaim3 ELIMINATED
END: alive [5] winner 5

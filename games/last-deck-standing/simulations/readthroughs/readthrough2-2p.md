# Readthrough 2 - 2p exploit game (seed 606)
Setup: A start player. B places pawn first (reverse order); A places LAST on B's hex (AAH tile) = same-hex brawl. Both stay at range 0 all game; Move cards dumped. Storm (rounds 1-7) removes far edge tiles only; no pawn tiles removable.
```
  attack A atk3 range2 shield-0 => 1 Dead to discard
  storm removes (-3, 3)
R19 T41 A hand XXM2H1H1 pos(-1, 1) stats M1A1S0 deck8 disc14
  Heal1: heals 1 Dead (card removed from game)
  Heal1 as shield -> sh 1
  move (-1, 1)->(0, -1) (2/3)
  loot H cube -> ('H', 1) (top)
  attack B atk1 range0 shield-0 => 1 Dead to discard
  storm removes (-2, 3)
R19 T42 B hand XM1A3M1A1 pos(0, -1) stats M4A1S0 deck0 disc24
  upgrade ba paying [('A', 3), ('A', 1)] -> 2
  move (0, -1)->(-1, 2) (3/6)
  storm removes (-1, -1)
R20 T43 A hand XH3M1M1M1 pos(0, -1) stats M1A1S0 deck4 disc17
  Heal3 as shield -> sh 3
  move (0, -1)->(-1, 2) (3/4)
  attack B atk1 range0 shield-0 => 1 Dead to discard
  storm removes (0, -1)
R20 T44 B hand XM2XH1H1 pos(-1, 2) stats M4A2S0 deck25 disc0
  Heal1: heals 1 Dead (card removed from game)
  Heal1: heals 1 Dead (card removed from game)
  move (-1, 2)->(0, 0) (2/6)
  storm removes (-1, 2)
  push-off: A -> (-1, 1)
R21 T45 A hand XA1H1M1A1 pos(-1, 1) stats M1A1S0 deck0 disc21
  Heal1 as shield -> sh 1
  move (-1, 1)->(0, 0) (1/2)
  attack B atk3 range0 shield-0 => 3 Dead to discard
  storm removes (-1, 1)
R21 T46 B hand M2XH1XA2 pos(0, 0) stats M4A2S0 deck20 disc4
  Heal1: heals 1 Dead (card removed from game)
  attack A atk4 range0 shield-1 => 3 Dead to discard
  storm: no legal tile, skip
R22 T47 A hand XA1A1M2A1 pos(0, 0) stats M1A1S0 deck24 disc0
  attack B atk4 range0 shield-0 => 4 Dead to discard
  storm: no legal tile, skip
R22 T48 B hand XM1M2XX pos(0, 0) stats M4A2S0 deck16 disc10 CRITICAL
  attack A atk2 range0 shield-0 => 2 Dead to discard
  ELIMINATED B with 3 Dead; loot pile of 20 at (0, 0)
END round 22; alive ['A']; tiles left 1; critical survivals []
```
Winner: B (round 4). A drew 3 Dead + no Heal at upkeep: critical with zero outs.

# Components Sheet — Last Deck Standing (Rules v1)

Data before art. Quantities are for a full 5-player box. Source of truth for rules: `rulebook-draft.md`.

## Cards
| id | type | name | qty | effect | tags | notes |
|---|---|---|---|---|---|---|
| BASE-A1 | card | Strike | 20 (4 per player) | +1 Attack | base, attack, gray | Player-colour stripe and character name: Blaze (red), Ember (orange), Tide (teal), Nova (pink), Shade (black) |
| BASE-M1 | card | Dash | 15 (3 per player) | +1 Move | base, move, gray | |
| BASE-H1 | card | Patch Up | 15 (3 per player) | Choose: heal 1 Dead from hand (then remove from game) or +1 Shield | base, heal, gray | |
| ATK-1 | card | Attack 1 | 9 | +1 Attack | supply, attack, gray | |
| ATK-2 | card | Attack 2 | 6 | +2 Attack | supply, attack, blue | |
| ATK-3 | card | Attack 3 | 3 | +3 Attack | supply, attack, purple | |
| MOV-1 | card | Move 1 | 9 | +1 Move | supply, move, gray | |
| MOV-2 | card | Move 2 | 6 | +2 Move | supply, move, blue | |
| MOV-3 | card | Move 3 | 3 | +3 Move | supply, move, purple | |
| HEL-1 | card | Heal 1 | 9 | Choose: heal 1 Dead from hand (then remove from game) or +1 Shield | supply, heal, gray | Heal deck |
| HEL-2 | card | Heal 2 | 6 | Choose: heal up to 2 Dead or +2 Shield | supply, heal, blue | Heal deck |
| HEL-3 | card | Heal 3 | 3 | Choose: heal up to 3 Dead or +3 Shield | supply, heal, purple | Heal deck |
| DEAD | card | Dead | 60 | No effect; can't be played | dead | **Distinct marked back** so Dead cards are visible in hands and decks |
| GOLD-* | card | Gold drop cards | 12 | Mixed Attack / Move / Heal, value 2 or 3 (e.g. 2 of each type at value 2 and at value 3) | gold | Supply drops |
| DROP | token | Supply drop marker | 1 | Marks the current drop | | |

Totals: base 50 · supply 54 (3 × 18) · Dead 60 · gold 12.

## Loot Tiles
Per player set (×5 sets = 75 tiles). Mark each tile's set letter (A–E) on its back.

| id | type | loot icons | qty per set |
|---|---|---|---|
| TILE-0 | hex tile | none | 4 |
| TILE-M | hex tile | Move | 1 |
| TILE-A | hex tile | Attack | 2 |
| TILE-H | hex tile | Heal | 1 |
| TILE-MA | hex tile | Move + Attack | 1 |
| TILE-AH | hex tile | Attack + Heal | 1 |
| TILE-HM | hex tile | Heal + Move | 1 |
| TILE-MM | hex tile | Move + Move | 1 |
| TILE-MAH | hex tile | Move + Attack + Heal | 1 |
| TILE-MAA | hex tile | Move + Attack + Attack | 1 |
| TILE-AAH | hex tile | Attack + Attack + Heal | 1 |

Per set: 15 tiles, 21 icons (7 Move, 9 Attack, 5 Heal).

## Tokens / Other
| id | name | qty | purpose | notes |
|---|---|---|---|---|
| CUBE-M/A/H | Loot cubes | 35 Move, 45 Attack, 25 Heal | One per loot icon at setup | Use colour **and** icon shape for colour-blind play |
| PAWN | Player pawns | 5 | Position | |
| STAT | Stat tracker | 5 | Base Move / Attack / Shield (0–4) and current Shield | Paper sheet with 3 tracks and a Shield counter |
| ROUND | Round track + marker | 1 | Rounds 1–25; round 7 marked "Storm closes fast" | Also marks supply-drop rounds when testing |
| STORM | Storm markers | 50 | Mark storm tiles | Translucent hex overlays or discs, so loot icons stay visible |
| PILE | Loot pile marker | 4 | Marks an eliminated player's pile | Optional |
| REF | Reference card | 5 | Quick Reference from the rulebook | |

## Counts Check
- [x] Every id appears in the rulebook (gold cards: Ideas for Later)
- [x] 2 players: 30 tiles, 20 base cards; 5 players: 75 tiles, 50 base cards
- [x] Dead-card backs are the only back that differs
- [ ] Art: placeholders only

## Tools
Cards → CSV → `../../tools/nanDECK-guide.md` (`tools/export-pipeline.md`). Digital table after paper works: `tools/TTS-guide.md`.

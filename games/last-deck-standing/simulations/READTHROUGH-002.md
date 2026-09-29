# READTHROUGH-002 — Blind read-throughs of the play-all rules (2p, 3p, 5p)

Date 2026-09-29 · three Claude (Opus) agents, main rules only · logs in `readthroughs/readthrough2-*.md`

| Game | Tester | Result |
|---|---|---|
| 2p | Rules lawyer | Won in round 4; start player placed on the opponent's hex and they brawled at range 0 |
| 3p | Three styles | Aggressive won in round 22; ended with a range-0 brawl on the last tile |
| 5p | First-timer | Won in round 8; all 5 pawns converged on one hex from round 1 |

Critical turns: 0 of 3+ survived in these games.

## Design issues (for the designer)
1. Same-hex brawls dominate every game; movement barely matters; the start player can place on an opponent's hex
2. Critical is near-certain death with 4+ Dead cards or no Heal card in hand
3. No endgame rule: the storm stops at the last tile, and round 25 has no defined outcome
4. Upgrades are nearly free, because unplayed cards are discarded anyway
5. Nothing makes players spread out early

## Wording fixes applied
Tile placement repeats until all tiles are placed · pawns go on tiles · round marker timing · empty-deck draw · "critical" is a warning only · no plays in Phase 3 · Heal: one mode for its whole value; Shield points go on the tracker · range first, then Shield · range across gaps · a loot action is one claim, and claims count in order · paid cards add nothing · edge tiles include sides facing inner gaps; loot piles don't protect tiles · push-off moves every pawn, owners choose in turn order · every Dead card you own returns to the supply on elimination · Quick Reference adds the Heal choice and storm phases · components: tile-set back colours, loot pile markers

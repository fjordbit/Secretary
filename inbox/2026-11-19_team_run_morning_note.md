# Team run on the groove findings — morning note, 19 Nov (Kai)

All calculated, not measured. Nothing is merged. Nothing is changed in the specification or on the pages.
Six falsifiers (A–F) and one re-run in a larger model (G). Details per part: `log/2026-11-19.md`.

## The short conclusion

The principle held. Most of the numbers moved. Three new problems are large enough to need you.

**Held (not broken):**
- A groove all round the outside of the yoke, at the sensors, sets where the standing axial field is zero.
- The zero sits at the same place in 3D, with the yoke split in two halves, and next to the split.
- The zero is robust to a groove off the sensor plane, unequal magnet rings and the yoke steel grade.
- An axial sensor at the zero reads a long loss several times stronger than without a groove.
- The local-fault signal rises with the field in the rope.

**Corrected numbers, 52 mm head:**

| | Said on 18 Nov | Now |
|---|---|---|
| Groove depth for the zero at 13 / 16 / 19 mm | 6.1 / 5.4 / 4.6 mm | 5.0 / 4.25 / 3.5 mm |
| Gain in LMA reading at 16 mm | 4–6 times | 3.8 times |
| Magnets 1 % weaker read as | well under 1 % | 0.1–0.3 % of metal |
| Best field in the rope for LMA | 1.92–2.07 T | 1.90–2.03 T (about 1.94–1.96 T) |
| Magnet needed for that | 1.3 times | 1.06–1.15 times |

Cause: the model box was too small (300 mm). A second solver agrees with the new depths.
All the groove notes of 18 Nov carry old-box numbers.

## Three new problems

1. **Steel near the head changes the reading.** A steel structure 200 mm away reads as about 4 % of metal;
   at 500 mm about 1 %. A second head 300 mm along the rope: about 8 %. A mild-steel housing 10 mm outside
   the yoke: 6.5 %, and it cuts the reading by 37 %. A calibration after installation removes the offset, but
   not if the surroundings change later (a vessel, a platform moving). The model overstates one-sided objects.
   The head with a groove is 1–3.4 times as sensitive to this as the head without.
2. **Temperature changes the scale of the loss reading.** From −20 to +45 °C: −6 to +11 % with N48SH,
   −5 to +8 % with N52. This is the magnet's strength changing with temperature. It needs a temperature
   correction or a reference.
3. **N52 in a warm, open, empty head loses strength for good.** 57–88 % of the magnet goes past its limit
   at +45 °C with no rope inside. With a rope inside it is safe. N48SH is safe in every case.

## Smaller, but they change the design

- **The zero must be adjustable.** Cut to the model depth and not adjusted, the sensor can go outside its
  ±20 mT range. About 0.4 mm of zero per 0.1 mm of groove depth.
- **No working point above about 2.0 T.** A thicker magnet pushes the yoke away and the groove cannot hold the
  zero at 16 mm.
- **"Lean towards LMA because local faults have margin" is not safe.** A broken wire inside the rope gives
  only 0.6 / 1.2 / 1.5 times the noise limit at 1.88 / 1.99 / 2.09 T. An outer wire has 6–7 times.
  The noise limit itself is derived, not measured.
- **The axial sensor part (TMR2584):** its data sheet gives a zero drift with temperature that can be read two
  ways. One way it is harmless; the other way it is 7–16 % of metal per degree. Must be asked or measured.
- **A sensor moving 0.5 mm after calibration** reads as 2.5 % of metal.
- **The thin yoke** does work on the 52 mm head, but needs 1.6–1.7 times the magnet. The groove still wins.
- **The groove costs** 4–14 % of the local-fault signal at equal magnet.

## Five things in the specification that would change (your decision, none made)

1. Magnet sizing: about 24 mm N52 for 2.00 T against 15.8 mm now in the specification.
2. The line that says the cut-out is not adopted would be reversed.
3. The range rule for the axial part (±94–150 mT) would no longer apply.
4. One shared head for 40 and 52 mm rope cannot hold the zero for both.
5. The ±0.5 % LMA limit in the factory test is not reachable with this reading alone.

## Not done

- No measurement. A field measurement on the prototype would test the model directly.
- No one-sided steel object in 3D; no real housing.
- The level along a long loss needs processing with the head's response. Tested that it can work; not built.
- Measured rope steel curve, measured noise, magnet temperature data per grade.

## Where things are

- Branches, all unmerged: u95 → u96 → u97 → u98 → u100, u99 (plots), u101a–f (team run), u102 (re-run).
- Notes: `C:/Users/stian/Prosjekter-u102/max/sws/3d/falsify/` (a and g) and `Prosjekter-u101b … f` (b–f).

— Kai

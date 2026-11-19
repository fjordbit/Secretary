# GitHub issue — fjordbit/max — for the head designer (assign `hmssyncro`). Replaces the draft of 8 Nov. No personal names in the body.

Title: SWS magnets: supplier data for N52 and N48SH (and alternatives) before ordering

Body:

**Where we stand.** The magnet grade is decided by price once the supplier data is in. Until then every result is shown for both N52 and N48SH. Other magnet types are noted if they fit, with their drawbacks (larger, weaker, more brittle, price). Envelope for service, storage and transport: −40 / +50 °C.

**Two things the model shows (calculated, catalogue values assumed, not measured):**

1. **An open, empty, warm head.** With no rope and no keeper inside, N52 at +45 °C has 57–88 % of the magnet volume past the point where it loses strength for good. With a rope inside it is safe (0.05–0.08 %, corners only). N48SH is safe in every case run.
2. **Temperature changes the scale of the loss-of-metal reading.** From −20 to +45 °C the reading for the same loss changes by −6 to +11 % with N48SH and −5 to +8 % with N52. The cause is the magnet's strength changing with temperature. The project holds only one temperature coefficient (−0.12 %/K, from an N40SH table) for all grades, so these numbers need the real coefficients.

**Task.** Obtain from the magnet supplier, for the one-piece radially magnetised half-ring (R 32.0 inside, R 48.7–51.0 outside, 40 mm long, 178.2° arc; `sws/3d/p52/design.md` §3), and for a radial thickness 10–15 % larger:

1. For N52 and N48SH: Br, Hcj and the demagnetisation curves J(H) and B(H) at −40, 20, 50 and 80 °C, for this arc and not the block table.
2. The reversible temperature coefficients of Br and Hcj for each grade over −40 to +50 °C.
3. Whether the highest-Br grade with Hcj ≥ 1.2 MA/m at 20 °C exists for this shape (an N52 that is safe in the empty head).
4. One alternative with a smaller temperature coefficient (for example samarium-cobalt): Br, size needed for the same flux, price, and handling limits.
5. Full one-piece radial magnetisation at this size confirmed; the largest one-piece size.
6. Tolerances on thickness and end faces, and the spread of Br between pieces of one batch.
7. Price and lead time for 4 pieces + 2 spares, per grade.
8. The supplier's recommendation for a keeper for an open half in transport and storage.

**Done when** the supplier's sheets are in `sws/data/` as a source and the price per grade is written in this issue.

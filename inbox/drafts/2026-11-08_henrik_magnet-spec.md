# Draft — Stian sends. To: Henrik. Subject: SWS magnets — what we need from the supplier before ordering

Henrik,

Short version: the temperature envelope for the SWS head is now settled at −40 / +50 °C for service, storage and
transport (the 49 °C record day rounded up; the magnets, not the electronics, set the transport limit). The
magnets we order must show no irreversible loss after a +50 °C excursion with the half open and empty, i.e. no
rope in the head and no keeper. Before any more FE runs I want the supplier's data for the actual one-piece
radial half-rings, not the block-grade table.

What the model says today (2D, our own knee model, assumed catalogue values; all in the repo under
sws/fem-2d and tasks/reports/U36.md):

- N48SH (Hcj ≥ 1.59 MA/m at 20 °C): no loss at any excursion up to +80 °C, empty or with rope.
- N52 at the catalogue Hcj (0.88 MA/m): an empty half loses rope field after any excursion above +45 °C
  (−32 mT at +50, −60 mT at +80). The 1 % / 1 mT criterion fails.
- N52 would need Hcj ≥ about 1.19 MA/m at 20 °C to stay under 1 mT loss at +50 °C empty. That is above
  what plain N52 is sold at, so the supplier has to tell us which grade meets it.

Ask the supplier (per half-ring: one piece, sintered NdFeB, radially magnetised, R 32.0 / R 48.7–51.0 mm,
40 mm axial, 178.2° arc, 4 pieces per head plus spares; details in sws/3d/p52/design.md §3):

1. Intrinsic demagnetisation curves J(H) and B(H) at 20, 50, 60 and 80 °C for the one-piece radial arc of this
   size, for N48SH and for the highest-Br grade that gives Hcj ≥ 1.2 MA/m at 20 °C. Grade table values are not
   enough; radially oriented one-piece arcs can come in lower than the block grade.
2. Br, Hcj and their temperature coefficients, and the knee position at 50 and 80 °C.
3. Confirmation that the half-ring can be fully magnetised in one piece at this size, and the maximum one-piece
   size they can make.
4. Tolerances on thickness (we assume ±0.1 mm) and on the arc end set-back.
5. Price and lead time for 4 + 2 spares in N48SH and in the Hcj ≥ 1.2 grade. If N52 pieces are still free, one
   pair of those as well: we bake it empty at +50 °C in the lab and close the N52 question with a measurement.
6. Whether they recommend a keeper for the open half in transport, and if so what.

If you have the supplier contact to hand, send it to me and I take it from there tomorrow; otherwise ask them
directly and copy me. Ramin is in the loop.

Stian

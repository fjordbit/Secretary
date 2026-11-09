# Draft — Stian sends. To: Henrik. Subject: SWS magnets — what we need from the supplier before ordering

Henrik,

Could you take this to the magnet supplier? I would like their numbers for the actual half-rings before we run any more FE. Happy to write to them myself if you send me the contact.

I am setting the range for the head to −40 / +50 °C, for service, storage and transport. +50 °C is the 49 °C record day rounded up, and I mean the magnet itself, including a half that is open and empty in a crate. The electronics can live with a wider range; +50 °C is the cap I want the magnets qualified to.

What we need from the parts we order: no permanent loss of rope field after a +50 °C soak with the half open and empty (no rope in the head, no keeper). When the head is closed again, rope induction before and after should stay within 1 %, which is the FAT rule we already have.

The figures below are our own 2D knee model (`tasks/reports/U36.md`), run on published block-grade minima. We do not have a data sheet from the supplier for this arc. The mail of 9 October confirms that each half-ring is one sintered piece, magnetised radially. Br and Hcj in the model are the Goudsmit catalogue (register R4): N48SH at least 1.59 MA/m, plain N52 about 0.88 MA/m, both at 20 °C.

- N48SH at that catalogue Hcj keeps the rope field after an empty-half excursion from +45 °C through +80 °C, and with the 40 mm rope in the head as well.
- Plain N52 at 0.88 MA/m loses about 29 mT of rope field after an empty soak at +45 °C, about 32 mT at +50 °C and about 60 mT at +80 °C. The virgin rope field on that head is 1.92 T, so 32 mT is outside the 1 % FAT rule.
- To keep that permanent loss under 1 mT after an empty +50 °C soak, the model needs Hcj of about 1.19 MA/m at 20 °C. That sits above plain N52. It is a screen for which grade to quote: we still want the curve, because the design will follow the curve.

The part, per half-ring (one piece, sintered NdFeB, radial magnetisation; drawing notes in `sws/3d/p52/design.md` §3):

- Inner radius 32.0 mm. That is the Ø64 seat: 60 mm free bore plus the 2 mm guard.
- Outer radius follows the thickness: about 48.7 mm for N52 at 16.73 mm, 49.5 mm for N48SH at 17.45 mm, 51.0 mm for N40SH at 19.02 mm.
- Axial length 40 mm. Arc 178.2°: a half-ring with 0.5 mm set-back from the split at each end, measured at the bore.
- Four per head (two poles, two halves), plus spares.

Please ask them for:

1. Intrinsic curves J(H) and B(H) at 20, 50, 60 and 80 °C, for this one-piece radial arc, for N48SH and for the highest-Br grade they can offer with Hcj at least 1.2 MA/m at 20 °C. A block-grade catalogue does not answer this; a radial arc in one piece can land below the block grade.
2. Br, Hcj, both temperature coefficients, and the knee position at 50 and 80 °C.
3. Confirmation that a half-ring of this size can be fully magnetised in one piece, and the largest one-piece size they will make.
4. Tolerances on thickness (we have assumed ±0.1 mm) and on the set-back of the arc ends.
5. Price and lead time for 4 + 2 spares in N48SH and in the Hcj ≥ 1.2 grade. If N52 is still the grade they offer at no extra cost, one pair of those as well would let us bake an empty half at +50 °C in the lab and settle that question with a measurement.
6. Whether they recommend a keeper for the open half in transport, and what they would use.

If you have the contact to hand, send it and I will take it from there. Otherwise please ask them and copy me. Ramin is in the loop.

Thank you,
Stian

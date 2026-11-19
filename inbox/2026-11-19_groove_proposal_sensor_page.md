# PROPOSAL — not in the specification, not on the pages

**Where it would sit.** Sensor page, section "Where the sensor can sit" (`docs/sws/sensor.html`, id `s-where`),
directly after the paragraph that begins "An open point that belongs to it: the yoke cut-out." and before the
paragraph that begins "The search order for the sensor". Nothing on the page is edited by this proposal.

---

**The groove and the zero (calculated, not measured).** In the model a groove all round the outside of the
yoke at the sensors moves the zero of the axial field (where the field along the rope is zero) nearer to the rope.
On the head for the 52 mm rope the zero is 24.5 mm from the rope surface without one; a groove 4.98, 4.25 or
3.53 mm deep puts it at 13, 16 or 19 mm. With the zero at 16 mm, an axial sensor reads about 3.8 times more
per 1 % of metal lost than without a groove. Open: the sensor's distance from the rope is not picked; each 0.1 mm
of depth moves the zero about 0.4 mm, so the zero must be adjustable on a built head; steel or a second head nearby
moved it by up to about 2 mm in the cases calculated.

![The groove moves the zero](fig_a_zero.png)

*Figure A. The axial field against distance from the rope, without and with the groove; where a curve crosses
zero, an axial sensor starts from zero.*

![Groove depth against the zero](fig_b_depth.png)

*Figure B. How deep a groove must be for each zero; N48SH and N52 magnets need depths within 0.14 mm of
these.*

[Detail](README.md#figures): what the groove buys in signal (C), the prototype head as drawn (D), a field map
of the head (E).

*Links and figure paths are relative to `max/sws/3d/groove_plots/`; on the page they would point there or to
copies beside the page. The prototype head as drawn has its zero at 16.7 mm, calculated (figure D).*

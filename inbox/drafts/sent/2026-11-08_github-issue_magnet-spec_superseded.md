# GitHub issue draft — fjordbit/max — for the head designer (assign by login). No personal names in the body.

Title: SWS magnets: supplier data and procurement spec before ordering (envelope −40 / +50 °C)

Body:

**Ruling (owner, 2026-11-08 evening).** Service, storage and transport envelope −40 / +50 °C. The 49 °C record
day rounds up to 50. The magnets set the transport limit, not the electronics. Magnets are ordered against a
requirement: no irreversible loss after a +50 °C excursion with the half open and empty (no rope, no keeper),
measured as rope induction before and after the soak within 1 % (spec FAT, result 8).

**Record.** `sws/spec/rendered/SWS_HW_Design_Input_Specification_rev130.md` l.367 / l.429 (storage and soak
written "owner to set"; to become +50); `sws/data/sws_data_sources.md` 8 Nov rows (envelope ruling, operating
range, storage, soak); `tasks/reports/U36.md` table (2D knee-history loss vs excursion temperature);
`sws/3d/p52/design.md` §3 (half-ring geometry and the open supplier questions); register [R29].

**What the model gives (2D, knee model status A, catalogue values assumed):**

| Grade, Hcj20 | Empty half, +50 °C | Empty half, +80 °C | 40 mm rope in head, +50 °C |
|---|---|---|---|
| N48SH, 1.59 MA/m | 0 mT | 0 mT | 0 mT |
| N52, 0.88 MA/m | −32 mT | −60 mT | ≈ −3 mT |
| N52, 1.19 MA/m | −0.2 mT | −17 mT | 0 mT |

Virgin B_rope is 1.920 T at the N52 2D size, so any empty-half loss puts N52 under the floor.

**Task.** Obtain from the magnet supplier, for the one-piece radially magnetised half-ring (R 32.0 / R 48.7–51.0,
40 mm, 178.2° arc, design.md §3):

1. J(H) and B(H) at 20, 50, 60, 80 °C for N48SH and for the highest-Br grade with Hcj ≥ 1.2 MA/m at 20 °C, for
   this arc, not the block table.
2. Br, Hcj, temperature coefficients, knee at 50 and 80 °C.
3. Full one-piece magnetisation at this size confirmed; maximum one-piece size.
4. Thickness and end-face tolerances.
5. Price and lead time, 4 + 2 spares, both grades; one N52 pair for the +50 °C empty-half lab test if free.
6. Keeper recommendation for the open half in transport.

**Done when** the supplier sheet is in `sws/data/` as a source, register rows l.153 and l.181 move from U/A to
S, and the +50 °C value is written into rev130 l.367 / l.429 (owner's Word master updated). No new FE runs until
then (owner, 2026-11-08).

Labels: sws, needs-supplier. Assignee: the head designer's GitHub login.

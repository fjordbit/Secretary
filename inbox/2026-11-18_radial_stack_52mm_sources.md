# Sources: radial stack, 52 mm rope (figure 2026-11-18_radial_stack_52mm.png)

All paths relative to `C:/Users/stian/Prosjekter-u05/max/`. Spec = `sws/spec/rendered/SWS_HW_Design_Input_Specification_rev130.md`.
Read-only; nothing in the repo was changed.

## Numbers on the figure

| Size | Value | Source (file:line) | Conflict |
|---|---|---|---|
| Rope radius | 26 (52 mm rope) | sws/3d/p52/design.md:20 | – |
| Rope new at +4 % | 54.08 mm, r 27.04 | sws/3d/design_inputs.md:34; sws/data/sws_data_sources.md:99 (+0 to +4 %, maker); Spec:503 | +5 % in sws/due-diligence/briefs/sws_standoff_brief.md:19 (status U) and Spec:532 (rev history, "from memory, flagged U") → 54.6 mm, r 27.3. **Documents differ** |
| Free bore Ø60 = guard inner face, r 30 | 60 | design.md:172; design_inputs.md:21, :33, :38–39; Spec:494 ("free passage inside the magnet guard") | Spec:459 and the result 9 addendum read it as drilled bore (design_inputs.md:41–42; sws/3d/rope_range.md:95); corrected 2026-10-29 |
| Free gap, centred new rope | 4.0 | design.md:172 (r 30 − 26) | sws/fem-2d/sws_guard_findings.md:13 (SUPERSEDED, :119): "4 mm radial gap incl. ~2 mm wear liner" → liner inside Ø60. **Documents differ** |
| Clearance at +4 % | 2.96 | design_inputs.md:42–43; Spec:494 | – |
| Guard thickness | 2.0 | design.md:173; design_inputs.md:32; Spec:173 | 1.5–2 in Spec:395, sws_data_sources.md:89, :171, sws_guard_findings.md:66, :110; 0.5–1 ("guard/liner over the sensor face") in sws_standoff_brief.md:21, sws_data_sources.md:219, sws_standoff_findings.md:43; 1 in the floor stack Spec:285 |
| Magnet seat / inner face | Ø64, r 32 | design.md:174; design_inputs.md:39 (drilled bore 64) | – |
| Magnet thickness | 15.8–20.5 | Spec:179 (100 mm: N52 15.8 / N48SH 16.6 / N40SH 18.2, +80 °C 19.1; "No grade or thickness is selected" :173); design.md:175 (drawn 20.5; 16.73 N52 / 17.45 N48SH / 19.02 N40SH at +45 °C); Spec:254 (19.1) | **Documents differ** (per-grade values differ by ~0.8–0.9 mm between Spec:179 and design.md:175) |
| Magnet axial position / length | z 50–90, 40 | design.md:177, :179 | – |
| Yoke wall | 12.0 | design.md:180; Spec:254 | 12.1 in Spec:179 (N40SH, +45 °C) |
| Yoke bore between the poles | Ø105 (r 52.5), no shoulder | design.md:183 | sensor_placement.md:22 uses yoke inner radius 51.1 (lm 19.1) |
| Sensor carrier envelope | r 30–52.5, \|z\| < 50 | design.md:197 | – |
| Sensing element (TMR die) radius | r 31 (5 mm) / r 29 (3 mm) | design.md:193, :205–206; Spec:13 ("5 mm design stand-off with a 3 mm floor") | – |
| Axial sensor radius | r 36.5 | design.md:194, :206–207 ([UNVERIFIED] in the document) | – |
| Radial sensor at z ±4 | ±4 | design.md:203–205 | – |
| Stand-off "geometry stack" | liner 1.5 + recess 2.5 + die 1.0 = 5 (status A) | sws/hw-selection/sws_sensor_placement.md:15, :35; sws_data_sources.md:312; sws/3d/geometry_study.md:255 | vs floor stack below. **Documents differ**; sws/3d/reconciliation.md:69 "Open: needs a decision" |
| Stand-off "floor stack" | movement 3 + guard 1 + die 0.7 = 4.7 | Spec:285; sws/hw-selection/sws_standoff_findings.md:28; sws_sensor_placement.md:36–37 | as above |
| Liner face position (geometry stack) | at the nominal rope surface; rope at +4 % reaches 1.04 into it | sws_sensor_placement.md:38–39 | – |
| Rope-contact liner | ~2 mm, UHMW-PE / PA6 / PEEK, sacrificial | Spec:397; sws_guard_findings.md:68 | 1.5 in the geometry stack (above); location not stated in Spec:397; Spec:228 "liner: not yet designed" |
| Liner location | on the carrier between the poles, part of the stand-off | sws_data_sources.md:312 | sws_guard_findings.md:13 (superseded) puts it inside the Ø60 at the pole |
| Sensor positions | 16 at 22.5°, first 11.25° from the split, 8 per half | design.md:195, :202–203; Spec:285, :292 | – |
| Radial + axial channel per position | one radial and one axial TMR (or one 2-axis) per spoke | Spec:283, :285; design.md:203–205 | – |
| Rope movement in service | 2–3 | sws_data_sources.md:105 ([R18] via [R3]); Spec:389 | – |
| Centring target | ≤ 0.5 | Spec:33, :218 | – |
| Grease, dirt | no size | Spec:383 ("wipeable"), :512 | **no allowance in the documents** |
| Ice | no size | Spec:504 (open: scraper, larger gap or heated bore) | **no allowance in the documents** |
| Broken wire end | touches the guard at a pole; wire 2.5 (A) | Spec:391; sws_guard_findings.md:50; sws_standoff_findings.md:39 | no protrusion allowance |
| Guard groove (worst) | 0.7 | Spec:391, :395 | groove is into the guard, not into the gap |
| Liner wear depth | – | – | **not in the documents** |

Gap arithmetic (figure panel E): 4.0 − 1.04 = 2.96; 4.0 − 1.30 = 2.70; minus 0.5 → 2.46 / 2.20; minus 2–3 → 0.96 … −0.04 (at +4 %) and −0.30 (+5 %, 3 mm).

## Where the clearance question has been discussed

- Spec:13 (summary) — 5 mm design stand-off, 3 mm floor; stated, not derived in detail.
- Spec:33 (§1 preconditions) — rope centring by the installation, residual eccentricity target ≤ 0.5 mm, value to be stated by mechanical design.
- Spec:198 (result 1/2) — bore gap barely matters magnetically; rope size changes sensor lift-off.
- Spec:205, :212 (result 2) — carrier bands ±4 mm; stand-off adjustable in 2 mm steps (shims or spoke positions).
- Spec:216 (result 5) — sacrificial 316L/PEEK liner over bore and sensor faces against protruding wires; no thickness.
- Spec:256 — "wide 35–57, clearance bore" Ø70 row, withdrawn 2026-10-29 (clearance had subtracted the guard twice).
- Spec:285 (§6) — stand-off = sum of floors (movement, diameter tolerance, guard, die depth) + margin; floors 4.7; target 4–5 ±0.5; open.
- Spec:391, :395, :397 (§9) — guard 1.5–2 mm, liner ~2 mm sacrificial; loose wire touches guard.
- Spec:475–476, :494, :502–504, :512 (open items) — stand-off and tolerance open; rope play envelope open; Ø60 stands (2.96 mm at +4 %); rope movement to be measured; delivered diameter +0 to +4 %; ice and lubricant open.
- Spec:532 (rev history) — rope +5 % tolerance vs bore added as item (EN 12385 from memory, U).
- sws/3d/design_inputs.md:21–44 (§1) — definitions D_b / t_g / D_f / c / s; Ø60 is free bore; 2.96 mm.
- sws/3d/rope_range.md:79–103 — bore and guard; decided 2026-10-30: keep modelled heads, drilled bores 4 mm larger.
- sws/3d/p52/design.md:223–227 — die at R 29 lies inside the Ø60 free bore; carrier liner bore must be smaller than pole bore; left to carrier design (U9/U11).
- sws/3d/geometry_study.md:255–269 — liner 1.5 + recess 2.5 + die 1.0; 3 mm floor needs liner + recess ≤ 2.0.
- sws/3d/reconciliation.md:46 — bore read as drilled vs free; resolved to free bore. :69 — two stand-off stacks; open, needs a decision.
- sws/hw-selection/sws_standoff_findings.md:16–29 — signal vs stand-off; floors 4.7 > 3 mm minimum; 3 mm holds only with guidance.
- sws/hw-selection/sws_sensor_placement.md:13–41 — geometry stack vs floor stack; record does not say which the carrier follows.
- sws/due-diligence/briefs/sws_standoff_brief.md:18–24, :36–38 — floors listed (movement 2–3, +5 % tolerance, guard/liner 0.5–1, die 0.3–0.7); guidance to ≤ 0.5 mm is what lets the stand-off come down.
- sws/fem-2d/sws_guard_findings.md:13, :66–72 (superseded) — 4 mm gap incl. ~2 mm liner; guard 1.5–2; liner separate; entry funnel.
- sws/fem-2d/sws_review_2026-10-23_findings.md:35, :95 — bore 65 → 70 for liner/recess/movement; withdrawn 2026-10-29 (guard subtracted twice).
- sws/data/sws_data_sources.md:141, :144 (superseded bore sweeps), :156 (sensor guard/liner counts against stand-off), :203 (5/3 mm, A), :219, :290 (bore decision, Ø70 withdrawn), :312 (magnet guard vs rope liner, geometry stack).
- sws/housing/rounds/2026-11-11/synthesis.md:19, :33 — models split on sensors behind a thinned wall/film (3) vs behind the liner (2); liner and rope grease asked back; not a decision (README).
- sws/hw-selection/rounds/2026-11-10, 2026-11-12-sensor, 2026-11-16-sensor — use the 5 mm stand-off as an input; no clearance conclusion found (only README/brief/synthesis grepped).

## Not checked

Model answer files inside the rounds (only README, briefs, syntheses); housing/carrier drawings; `sws_geometry_stack.py` itself; the older spec revisions beyond the Ø70 row.

# Fault signals in mT, 52 mm rope: sources

Figure: `2026-11-18_fault_signals_mT_52mm.png` (script `2026-11-18_fault_signals_mT_52mm.py`, same folder).
Repo: `C:/Users/stian/Prosjekter-u05/max` (read only). All values are model values (3D FE), placeholder materials,
status A (p52/design.md l.430–432; spec rev130 l.15). Not measured.

## Case plotted

The base case of `sws/figures/decided/u32_faults_3d.png` (make_u32_figures.py l.91, l.101–102): P52 one-piece head,
N52* lm 16.73 mm (run point), hard wire, +45 °C, half-space L_h 25, box 300, level 1.5, worst angle
(sws/3d/p52/design.md l.342–344). N52* label: "virgin recoil law, knee violated in storage and on the 40 mm rope,
Hcj 0.88 MA/m status A; not usable as a margin" (design.md l.433–434).
Values read from `sws/3d/results/p52/u32_summary.json` → `faults` → case `P52lm16.73N52_d52_hard_+45C`, files
`…_Lh25_h1.5_acc` / `_rest` / `_gaps`; keys `Br5_worst`, `Br3_worst`, `Bz3_worst`, `Bz365_worst`, `lma_percent`.

Other grades: N48SH within 0.6 % of N52* (design.md l.360–364); N40SH within 0.9 % of N48SH (l.407–409).

## Plotted numbers (mT, worst angle)

| Fault (figure label) | LMA % | B_r 5 mm | B_r 3 mm | B_z 3 mm | B_z R 36.5 | Document line |
|---|---|---|---|---|---|---|
| 1 wire deep in the rope | 0.30 | 0.17 | 0.25 | 0.35 | 0.08 | design.md l.352 (B_z R 36.5: JSON only) |
| 1 hidden wire (king) | 0.32 | 1.27 | 2.13 | 3.09 | 0.43 | l.350 |
| 1 hidden wire (bottom) | 0.31 | 1.27 | 2.10 | 2.96 | 0.44 | l.351 |
| 1 visible crown wire | 0.31 | 1.46 | 2.42 | 3.61 | 0.50 | l.353 |
| 2 hidden wires (flank), gap 1 mm | 0.62 | 1.89 | 3.16 | 4.57 | 0.65 | l.399–400 (B_r); B_z: JSON only |
| 2 hidden wires (flank), gap 2 mm (headline) | 0.62 | 2.70 | 4.43 | 6.29 | 0.94 | l.348 |
| 2 hidden wires (flank), gap 4 mm | 0.62 | 3.74 | 5.97 | 8.10 | 1.34 | l.399–400 (B_r); B_z: JSON only |
| 2 hidden wires (flank), gap 10 mm | 0.62 | 5.29 | 7.77 | 8.41 | 2.00 | l.399–400 (B_r); B_z: JSON only |
| 2 hidden wires (king + bottom) | 0.63 | 2.82 | 4.62 | 6.60 | 0.99 | l.349 |
| 3 wires missing over 20 mm | 0.94 | 9.87 | 13.78 | 9.49 | 3.29 | l.354 |
| 6-wire cluster (one strand) | 1.87 | 9.39 | 14.68 | 21.16 | 3.50 | l.355 |
| Inner-rope strand broken | 5.17 | 4.25 | 5.66 | 7.81 | 2.20 | l.356 |

B_z at R 36.5 for P52 is in the JSON (`Bz365_worst`) but not in the design.md tables; the H52 (U16) equivalents are in
sws/3d/verification.md l.905–915 (e.g. headline 0.95 mT). B_z for the gap series is in the JSON only (verification.md
l.969–975 gives it for H52).

Other figure numbers:
- Pass line 0.22 mT = 2 × 0.11 mT p-p: spec rev130 l.325 ("zero-peak signal ≥ 2 × peak-peak noise"), l.327 ("0.11 at
  52 mm"); margin = S / (2 N_pp), THEORY.md l.172–174.
- No mT limit for LMA; FAT asks "LMA reading within ±0.5 % of the machined value": spec rev130 l.435.
- Standing axial field −39.22 mT at R 29 (3 mm) and −26.56 mT at R 36.5: p52/design.md l.209–217 (stranded rope, hard
  +80 °C, lm 20.5, box 1200: a different run point from the bars; the base-case JSON at box 300 gives −39.4 / −24.6 mT,
  and box 300 reads 12–16 % high, l.221). Ratios on the figure: 3.09 / 39.22 = 8 %, 0.43 / 26.56 = 1.6 %.
- LMA signal falls with radius (H52): 11.9 mT at 27 mm, 0.95 at 36.5, 0.03 at 50; factor 6.6 against 3 mm:
  verification.md l.921–925. R 36.5 is the head designer's value, [UNVERIFIED] (design.md l.194).
- Pole spacing 100 mm (design.md l.178); yoke / head length 180 mm (l.182).

## Do we measure LMA correctly for faults longer than the sensor / head?

**The documents do not answer it. Nothing longer than 20 mm has been calculated.**

What is calculated:
- Short faults only. Longest: 3 crown-side wires missing over 20 mm (run_3dd.py l.77; design.md l.354). The fault
  model's segment boundaries allow break gaps of 1–20 mm only (THEORY.md l.154–155), and the passage read-out is valid
  while the head field is uniform over the signature, about ±20 mm (THEORY.md l.163–165).
- The 2D ring defect in the geometry study is 8 mm long (geometry_study.md l.7–8): 0.3 % gives −0.119 mT, 30 % gives
  −14.2 mT on the axial channel at 3 mm (l.47–50).
- Each B_z value is one sensor at the worst angle (verification.md l.901–903), not a summed or main-flux figure.

What is not calculated:
- Any fault longer than the pole spacing (100 mm) or the head (180 mm): not calculated.
- A long, uniform loss of metallic area (an LMA step): not calculated. design_inputs.md l.138–139: "LMA steps such as a
  broken strand give larger signals that are not in the register: [INPUT: largest LMA signal]."
- The sum of the 16 axial channels around the rope: no such calculation found in sws/3d.

What is assumed (specification):
- spec rev130 l.271: the axial channels, "summed around the circumference they also track the main-flux change that
  follows loss of metallic area (LMA)". Whether 16 axial TMRs are enough, or a dedicated main-flux sensor (Hall probe in
  the pole gap, or a search coil) is needed, "is an open question for the prototype". Discard criteria (EN 12927,
  ISO 4309) are in % LMA, so a calibrated LMA channel is a requirement (l.271; ISO 4309 row l.64).
- Open item, spec rev130 l.464: "Is a dedicated main-flux (LMA) sensor needed, or do the 16 axial TMRs give a usable
  LMA figure?"
- Planned characterisation: removed-wire LMA steps of 1 % and 5 % on the reference rope (l.445); FAT ±0.5 % (l.435).
  A spare ADC channel is kept for "a future LMA sensor" (l.321).

Related: the deep inner-rope wire on the axial channel (0.24 mm movement-equivalent) is not separable from rope
movement (verification.md l.933–934); B_z changes 1.41 mT per mm of lateral offset at 3 mm (l.929).

## What would have to be calculated or tested to answer it

1. A long uniform LMA step (e.g. 1 % and 5 %, lengths 20 → 100 → 180 mm and longer than the head) in the 3D model,
   with the fault passing through the whole head, not the ±20 mm passage shortcut: needs a longer section than L_h 25/60.
2. The 16 axial channels summed around the rope for those cases, against the same for the short faults.
3. A main-flux reading in the same runs (flux through the rope / Hall in the pole gap / search coil) to compare with the
   summed axial TMRs.
4. Rope lateral movement and template drift on the summed axial channel over a long fault (DC-like signal).
5. Test: the 1 % and 5 % removed-wire LMA steps on the reference rope (spec l.445), made longer than the head, read
   against the ±0.5 % FAT criterion (l.435).

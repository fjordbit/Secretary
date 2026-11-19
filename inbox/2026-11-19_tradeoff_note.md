# The trade-off: groove depth against rope induction, axial gain against radial cost

Calculated, not measured. 2D axisymmetric model, homogenised rope (middle rope curve), placeholder yoke steel, 25 °C,
model box r 2400 × z ±2400 mm. H52 head (52 mm rope), outer groove 20 mm wide at the mid-plane. A stronger magnet
here is a thicker magnet of a real grade (N52 or N48SH), with the yoke moved out with it. Lift-off is from the rope
surface. Nothing is selected. Terms: [terms.md](terms.md); sources: [source.md](source.md).

**In plain words.**
1. With a real magnet made thicker, a stronger magnet needs a deeper groove to keep the zero at 16 mm: from about
   2 mm at 1.94 T to about 9 mm at 2.03 T, because the thicker magnet pushes the yoke away from the rope.
2. The zero can be held at 16 mm only up to about 2.04 T in this head (N52 about 31 mm thick, 1.3 mm of yoke steel
   left over the groove); the rope reaches 2.2 T with a magnet about 2.1 times today's and 2.3 T with about 2.8
   times, but then the zero lies about 26 mm or more out, past anything a groove can pull in.
3. The groove costs the radial element at the same magnet: at the modelled magnet the groove for 16 mm takes 9 %
   off the short-fault signal at 3 mm (9.56 to 8.73 mT), and deeper grooves take more (about 15 % for 13 mm).
4. Along the 16 mm line the stronger magnet pays this back and more: the radial signal at 3 mm rises from 7.9 to
   11.6 mT between 1.94 and 2.03 T, and the axial level from 0.35 to about 0.95 mT per 1 %, flat above about 2.00 T.
5. Moving the radial element from 3 to 5 mm halves its short-fault signal, and to 8 mm leaves about 28 %, with or
   without the groove.
6. On the axial element, the groove's larger level makes every element error smaller in % of metal (about 3.6
   times); the Hall parts read here keep range everywhere, but four of five drift 1–7 mT in offset over temperature
   (the fifth, a 5 V programmable part, 0.08 mT), against 0.1–0.9 mT for the TMR parts whose sheets state it (or 9 mT for one TMR
   part, depending on how its sheet is read).

**Results** (N52 on the 16 mm zero line unless said; level and drift at the zero; short-fault signal = largest
|ΔB_r| at the radial element)

| Magnet (thickness) | Groove depth (mm) | Rope, mid-plane / peak (T) | Level per 1 % (mT) | Magnets 1 % weaker read as | Short-fault signal at 3 / 5 / 8 mm (mT) |
|---|---|---|---|---|---|
| modelled N40SH (19.1 mm), no groove (zero 24.3 mm; level at 16 mm) | 0 | 1.972 / 2.087 | −0.200 | −1.44 %* | 9.56 / 5.10 / 2.70 |
| modelled N40SH (19.1 mm) | 3.92 | 1.953 / 2.084 | −0.714 | +0.08 % | 8.73 / 4.70 / 2.52 |
| N52 × 0.75 (14.3 mm) | 2.13 | 1.936 / 2.085 | −0.352 | +0.17 % | 7.91 / 4.34 / 2.41 |
| N52 × 0.95 (18.1 mm) | 3.58 | 1.971 / 2.140 | −0.774 | −0.02 % | 9.51 / 5.07 / 2.68 |
| N52 × 1.15 (22.0 mm) | 5.06 | 1.998 / 2.185 | −0.949 | −0.20 % | 10.54 / 5.50 / 2.83 |
| N52 × 1.35 (25.8 mm) | 6.84 | 2.019 / 2.221 | −0.974 | −0.42 % | 11.20 / 5.75 / 2.92 |
| N52 × 1.55 (29.6 mm) | 9.22 | 2.033 / 2.248 | −0.943 | −0.71 % | 11.58 / 5.90 / 2.96 |
| N52 × 1.65 (31.5 mm), standing only | 10.65 (1.3 mm steel left) | 2.039 | — | — | — |
| N48SH × 0.85 (16.2 mm) | 2.93 | 1.946 / 2.091 | −0.537 | +0.15 % | 8.40 / 4.56 / 2.48 |
| N48SH × 1.00 (19.1 mm) | 3.92 | 1.970 / 2.128 | −0.802 | −0.03 % | 9.47 / 5.05 / 2.67 |
| N48SH × 1.15 (22.0 mm) | 4.98 | 1.990 / 2.160 | −0.924 | −0.16 % | 10.25 / 5.38 / 2.79 |
| N48SH × 1.30 (24.8 mm) | 6.25 | 2.005 / 2.186 | −0.964 | −0.33 % | 10.78 / 5.59 / 2.86 |
| N52, no groove: × 1.7 / 2.2 / 2.8 / 3.5 | 0 (zero 38 / 48 / 59 / 72 mm) | 2.132 / 2.216 / 2.303 / 2.387 | — | — | — |

*At 16 mm, no groove: +0.288 mT ÷ −0.200 mT. N48SH × 0.70 (zero landed at 15.24 mm) is in `results/lines.json` and
not in the table. Old-box comparison: not used.

![Figure F](fig_f_map.png)

*Figure F ([interactive](fig_f_map.html), [slide](fig_f_map_slide.png)). Groove depth against rope induction, N52
made thicker. Black: where the zero falls (13 / 16 / 19 mm). Colour: loss-of-metal level per 1 % at 16 mm. Dotted:
radial short-fault signal at 3 mm. Hatched: zero 13–19 mm at 1.90 T or more (the fine net covers it from about 1.93 T). Rings on the 16 mm
line: N52 magnet thickness.*

![Figure G](fig_g_cost.png)

*Figure G ([interactive](fig_g_cost.html), [slide](fig_g_cost_slide.png)). At the modelled magnet: what the groove
gains on the axial side and costs on the radial side, as % of the value without a groove.*

Also: Figure H ([interactive](fig_h_line16.html), [png](fig_h_line16.png)) along the 16 mm line, and Figure I
([interactive](fig_i_radial.html), [png](fig_i_radial.png)) the radial signal against lift-off.

---

## Dense part

### 1. Model and what was solved

Same solver, mesh rules (refine 0.25, pole lines), Newton tolerance (1e-11) and read-outs as `../falsify/g_lib.py`;
the large box of `../falsify/g_large_box.md` (r 2400 × z ±2400 mm, A = 0). Rope: the middle curve of the rope-curve
bracket (`../demo/h52_groove.py`, Bs 1.97 T, Ha 1700 A/m, fill as modelled). Magnet: register minimum remanence at
25 °C (N52 1.42 T, N48SH 1.36 T; the modelled N40SH 1.25 T), thickness 19.1 mm × f, the yoke (11.96 mm) moved out
with it, as `../falsify/f_magnet_mech.py`. The remanence knob of the earlier notes (geometry fixed, remanence
scaled) was not used for the net: above about 1.14 × the modelled remanence (N52) it is not a magnet that exists.
Per point: standing field and zero; level per 1 % (300 mm, 10 % lost, centred on the head, z_d 0 only; at the
reference point of `g_large_box.md` the z_d 0 level is 0.7 % larger than the mean over ±30 mm, −0.680 against −0.675 mT, its Tables 2 and 1); magnets 1 % weaker on
the same mesh; the short ring (4 mm, 30 % of the outer 2 mm) with |ΔB_r| read at 0–14 mm along the rope and the
largest kept. Results: `results/cal.json`, `coarse.json`, `model.json`, `fine_grid.json`, `lines.json`; read-outs
`results/summary.json`. All 540 solves converged (9–12 Newton steps, 183–231 k nodes).

**Checks.** Short ring read with the ring fixed and the read point moved, against the ring moved past a fixed read
point (N52 × 1.0, groove 4 mm): 9.77 against 9.71 mT at 3 mm (+0.7 %), 5.18 against 5.06 mT at 5 mm (+2.5 %), 2.72
against 2.70 mT at 8 mm (+0.9 %). Zero on the plain mesh against the loss mesh: 15.710 / 15.714 mm and 19.497 /
19.501 mm (0.004 mm). Mesh scatter on the fine grid (largest residual of the zero from a quadratic through five
neighbouring depths 0.25 mm apart): 0.04–0.16 mm of zero, rope induction about 0.00005 T or less; nothing smoothed. The
line points are solved at the depth read off that grid: N52 zeros landed within 0.17 mm of 13 / 16 / 19 mm, N48SH
within 0.08 mm of 16 mm except the × 0.70 point (15.24 mm, left out of the table and of Figure H).

**Coarse net.** N52: f 0.6, 0.8, 1.0, 1.3 × depth 0–7 mm in 1 mm steps with all read-outs, standing field also at
9 mm; f 1.7, 2.2, 2.8 × depth 0, 2, 4, 6, 7, 9, 11 mm (standing); f 3.5, no groove. N48SH: f 0.6, 0.8, 1.0, 1.3,
1.7 × depth 0, 2, 4, 6, 7, 9 mm (standing); f 3.5, no groove. **Fine net** (the area where the zero falls 12–20 mm,
which holds the 13–19 mm, ≥ 1.90 T area): N52, f 0.75–1.65 in steps of 0.10 (0.006–0.02 T apart), depth in 0.25 mm
steps: 152 standing solves. Then all read-outs on the lines of constant zero 13 / 16 / 19 mm at f 0.75, 0.95, 1.15,
1.35, 1.55 (N52) and on the 16 mm line for N48SH at f 0.7, 0.85, 1.0, 1.15, 1.3.

### 2. How far the rope induction goes, and what stops it

| N52 thickness × | 0.6 | 0.8 | 1.0 | 1.3 | 1.7 | 2.2 | 2.8 | 3.5 |
|---|---|---|---|---|---|---|---|---|
| Rope, mid-plane, no groove (T) | 1.903 | 1.955 | 2.000 | 2.059 | 2.132 | 2.216 | 2.303 | 2.387 |
| Zero, no groove (mm) | 16.2 | 20.3 | 24.4 | 30.4 | 38.1 | 47.7 | 59.1 | 72.3 |
| Zero with the deepest groove solved (mm; depth) | — | — | 3.2 (9) | 9.8 (9) | 16.5 (11) | 28.2 (11) | 40.3 (11) | — |

(N48SH: 1.896 / 1.946 / 1.991 / 2.049 / 2.119 / 2.363 T at × 0.6 / 0.8 / 1.0 / 1.3 / 1.7 / 3.5.) The rope reaches 2.2 T
at about N52 × 2.1 (40 mm of magnet) and 2.3 T at about × 2.8 (53 mm), with no groove. What stops the head is not the
rope but the zero: the thicker magnet moves the yoke face out (lift-off of the face 25.1 mm at × 1, 37.5 mm at × 1.65,
48.0 mm at × 2.2), and the standing B_z at 16 mm grows (−19 mT at × 1, −84 mT at × 1.7 without a groove). The groove
pulls the zero to 16 mm up to × 1.65 (2.039 T, groove 10.65 mm, 1.3 mm of steel left); at × 1.7 a groove leaving
0.96 mm of steel gives 16.5 mm; at × 2.2 / 2.8 the zero stays at 28 / 40 mm. Above 2.0 T the rope is past its knee
(middle curve Bs 1.97 T): each further 0.1 T costs about 0.55–0.7 × today's magnet thickness again. The reach found in
`f_magnet_mech.md` (hard wire, old box: about 2.00 T) is a little higher here (2.04 T) on the middle curve in the
large box.

### 3. Along constant zero: less groove or more

Along each line of constant zero the depth rises with the magnet (Figure F, table above): for 16 mm, N52 2.13 →
3.58 → 5.06 → 6.84 → 9.22 → 10.65 mm from 1.936 to 2.039 T; N48SH 2.93 → 6.25 mm from 1.946 to 2.005 T; for 13 mm
2.96 → 10.89 mm (1.926 → 2.011 T), for 19 mm 0.33 → 7.75 mm (1.942 → 2.052 T). **A stronger magnet wants more groove**,
roughly 1 mm per 0.025 T at first and 1 mm per 0.004 T near the end. At equal induction a thinner magnet of a
stronger grade needs less groove (1.95 T: N52 × 0.85 about 2.9 mm, N48SH × 0.85 2.93 mm, modelled N40SH × 1.0
3.92 mm), because its yoke face sits nearer the rope.

What each side gains or loses along the 16 mm line (N52, 1.936 → 2.033 T):
- **Axial:** level per 1 % −0.352 → −0.774 → −0.949 → −0.974 → −0.943 mT: it grows 2.7 × up to about 2.00 T, then is
  flat and falls slightly. Magnets 1 % weaker read as +0.17 → −0.71 % of metal: the magnet null (read as 0) lies at
  about 1.968 T for N52 and about 1.966 T for N48SH; above it the magnet error grows by about 0.11 points per 0.01 T.
  Steel left over the groove 9.8 → 2.7 mm.
- **Radial:** the short-fault signal at 3 mm 7.91 → 11.58 mT (+46 %), at 5 mm 4.34 → 5.90, at 8 mm 2.41 → 2.96; it
  follows the rope induction, and the deeper groove along the line does not stop it rising. The standing B_z across
  the radial element at 3 mm grows with it: −27.0 → −60.7 mT.
- **Inner-wire margin (stand-in).** The repo's method is 3D (`../falsify/c_third_dimension.md` §2, old box: one
  wire inside the inner rope, 5 mm, margin 0.56 / 1.16 / 1.51 at its 3D rope induction 1.881 / 1.989 / 2.093 T,
  margin 1 near 1.96 T; those runs were set up at the old-box 2D steps 1.90 / 2.00 / 2.10 T). It cannot be carried
  to a 2D net, so the rope induction stands in. Read across linearly against the 2D steps, margin 1 falls at about
  1.97 T (1.96 T against the 3D induction): the 16 mm line crosses it at N52 about × 0.95 (18 mm), N48SH about
  × 1.0. Read the line as ±0.02 T.
- **Demagnetisation (N52, warm, head empty).** `../falsify/f_magnet_mech.md` §2 (old box; a quantity inside the
  magnet): N52 at +45 °C with the head empty has 57–88 % of its volume past the knee at every thickness tried
  (× 0.8–1.49 with the groove) and 11–24 % at × 1.75–2.0 without; N48SH 0.00–0.01 %. So every N52 point of the 16 mm
  line here sits where N52 in the warm empty head is past its knee. Not re-run here.
- **The remanence knob, for comparison** (`../falsify/g_results/wp.json`, large box, middle curve, geometry fixed):
  depth for 16 mm 4.38 / 3.92 / 4.02 / 4.33 mm at 1.911 / 1.953 / 2.004 / 2.043 T. With the geometry held, the depth
  barely moves; the real magnet's growth in depth comes from its thickness.

### 4. What the groove costs the radial side, and the radial element's lift-off

At the modelled magnet (`results/model.json`, Figure G): with depth 0 / 3 / 3.92 / 5 / 7 mm the zero falls at 24.3 /
19.7 / 16.0 / 11.7 / 5.8 mm, the rope at 1.972 / 1.964 / 1.953 / 1.934 / 1.884 T; the level at 16 mm is 1.0 / 2.4 /
3.6 / 4.3 / 4.4 × its no-groove value (−0.200 mT); the radial signal at 3 mm 100 / 96 / 91 / 82 / 58 %, at 8 mm 100 /
97 / 93 / 86 / 63 %. The cost on the radial side is the rope induction the groove takes away at equal magnet (−0.019
T for 16 mm), as in `c_third_dimension.md` (3D, old box: −3 % outer-strand wire, −17 % inner-rope wire at equal magnet).

Radial signal against lift-off (Figure I): no groove 9.56 / 5.10 / 2.70 mT at 3 / 5 / 8 mm; groove for 16 mm 8.73 /
4.70 / 2.52; N52 at 2.033 T 11.58 / 5.90 / 2.96; N48SH at 2.005 T 10.78 / 5.59 / 2.86. Moving the element from 3 to 5
mm costs 46–49 % of the signal, to 8 mm 71–74 %, the same with and without the groove. The stronger magnet buys back
less at 8 mm (+18 % from the modelled magnet to N52 at 2.03 T) than at 3 mm (+33 %). The standing field across the
radial element falls with lift-off (modelled magnet, no groove: B_z −39.6 mT at 3 mm, −35.2 at 5, −30.5 at 8; with the
16 mm groove −31.7 / −26.4 / −20.3 mT); B_r on the mid-plane is zero by symmetry (read-out below 0.1 mT).

### 5. Hall beside TMR for the axial element (data sheets; arithmetic in `t_hall.py`, `results/hall.json`)

Sheet figures: the TMR rows from `../../hw-selection/sws_sensor_candidates.md` (CT100 and TMR215x re-read on the
sheet; TMR2584, TMR2185, TMR2083S as that note records them); the Hall rows read on the makers' current sheets.
"n/s": not on the sheet. Derived values marked (d). Noise p-p over 0.1–100 Hz is white noise only (density × 10 ×
6.6, d); no sheet states 1/f noise, and the months-long change the loss-of-metal channel reads lies below every band.
(`sws_sensor_candidates.md` derives 0.011–0.016 mT p-p for the same parts over 0–125 Hz; the band is the
difference. For the MLX91377 it records 3.4 mV rms at a ±80 mT span, about 0.11 mT rms; the 2.5 mV rms at ±40 mT
used here is the sheet's other figure.)

| Part | Type, senses | Linear range | Sensitivity | Noise: density; p-p 0.1–100 Hz | Zero offset; drift with temperature; over life | Sensitivity drift | Hysteresis | Supply; current | Package | Price class |
|---|---|---|---|---|---|---|---|---|---|---|
| TMR2584 | TMR, out of the package plane | specified ±20 mT; saturates ±30 mT | 5 mV/V/mT | n/s | ±10 mV/V (≈ ±2 mT, d); "0.5 mV max", unit ambiguous (total or per K); life n/s | −290 ppm/K | ≤ 0.2 mT | 1–7 V; ≈ 1.1 mA at 3.3 V (d) | SOT23-5 and others | n/s |
| TMR2185 | TMR, in plane | specified ±20 mT; saturates ±100 mT | 3.4 mV/V/mT | n/s | ±10 mV/V (≈ ±2.9 mT, d); drift n/s; life n/s | −770 ppm/K | 0.03 mT typ | 0.5–7 V; ≈ 77 µA (d) | SOP8, LGA4L | n/s |
| CT100 | TMR, in plane | ±20 mT linear (±50 mT operating) | 4.5 mV/V/mT | 0.7 µV/√Hz at 10 Hz, 1 V (0.16 µT/√Hz, d); ≈ 0.010 mT p-p (d) | ±5 mV/V (≈ ±1.1 mT, d); ±4 µV/V/K max (≈ 0.9 µT/K, d); life n/s | −250 typ, −350 max ppm/K | 0.05 % at ±20 mT | 1.0–5.5 V; 0.3 mW at 3 V | SOT23-6, DFN6 | n/s |
| TMR2083S | TMR, in plane | ±50 mT (0.5 %FS) | 1.8 mV/V/mT | n/s | ±10 mV/V (≈ ±5.6 mT, d); 2 µV/V/K (≈ 1.1 µT/K, d); life n/s | −1000 ppm/K | 0.15 mT | 0.5–7 V; 10 kΩ | SOT23-5 | n/s |
| TMR2152S | TMR, in plane | ±50 mT (1 %FS) | 2.0 mV/V/mT | n/s | ±10 mV/V (≈ ±5 mT, d); 10 µV/V/K max (≈ 5 µT/K, d); life n/s | −500 ppm/K | ≤ 0.5 mT | 0.5–7 V; 7 kΩ | SOT23-5 | n/s |
| TMR2151S | TMR, in plane | ±100 mT (1 %FS) | 1.0 mV/V/mT | n/s | ±10 mV/V (≈ ±10 mT, d); 10 µV/V/K max (≈ 10 µT/K, d); life n/s | −500 ppm/K | ≤ 0.5 mT | 0.5–7 V; 7 kΩ | SOT23-5 | n/s |
| DRV5055A3 / A4 (Z3 / Z4) | Hall, out of the package plane | ±88 / ±176 mT at 3.3 V | 15 / 7.5 mV/mT | 215 nT/√Hz; ≈ 0.014 mT p-p (d) | ±60 mV at 25 °C (≈ ±4 / ±8 mT, d); ±1 % of supply over −40…125 °C (≈ ±2.2 / ±4.4 mT, d); life: < 0.5 typ after 1000 h, unit unreadable on the sheet | A: +0.12 %/K typ; Z: 0 typ | n/s | 3–3.63 V; ≈ 2 mA | SOT-23, TO-92 | ≈ 0.4–1 USD (listings) |
| TMAG5253BA4 | Hall, out of the package plane | ±160 mT | 7.5 mV/mT | 220 nT/√Hz; ≈ 0.015 mT p-p (d) | ±40 mV (≈ ±5.3 mT, d); ±50 mV over −40…125 °C (≈ ±6.7 mT, d), ±5 mV over 0…50 °C (≈ ±0.67 mT, d); life 10 mV typ after 1000 h (≈ 1.3 mT, d) | +0.12 %/K typ | n/s | 1.65–3.6 V; 2.6 mA typ | X2SON-4 | n/s |
| A1304-T | Hall, direction on a figure only | ±37.5 mT typ | 40 mV/mT | 0.23 µT/√Hz; ≈ 0.015 mT p-p (d) | ±25 mV (≈ ±0.6 mT, d); ±40 mV typ 25→85 °C (≈ ±1 mT, d); life: sensitivity ±3 % typ | +0.12 %/K typ | n/s | 3–3.6 V; 7.7 mA typ | SOT23-W, −40…85 °C | ≈ 0.4–1 USD (listings) |
| MLX91377 | Hall, programmable, out of the package plane | span 10–100 mT, offset placeable | programmed | density n/s; 2.5 mV rms at ±40 mT span, band n/s (≈ 0.26 mT p-p, d, assumed gain) | 10 LSB at ±25 mT span (≈ 0.12 mT, d); 3.9 LSB over the full range at ±40 mT span (≈ 0.08 mT, d); life inside "total drift" | ±1.5 % | n/s | 4.5–5.5 V; 11 mA typ | TSSOP-16 | n/s; status not confirmed |

**What each part resolves here** (`t_hall.py`; modelled magnet, middle curve). Smallest long loss = (offset change
over −40…+50 °C + noise p-p + hysteresis) ÷ level per 1 %, one element, no temperature correction, no long-term
drift (on no sheet). Level per 1 %: at the zero with the groove −0.773 / −0.713 / −0.509 mT (zero 13 / 16 / 19 mm);
without a groove at 13 / 16 / 19 mm −0.268 / −0.200 / −0.138 mT. In range: |standing B_z| + a 10 % loss passing
(10 × level) within the stated linear range; with the groove the standing field at the zero is taken as 0 (build
tolerances are not added; `../falsify/d_measurement_chain.md` §3, old box, puts the worst-case sum with a 10 % loss
passing at 12.8–21.8 mT at 1.92–2.00 T).

| Part | Offset change used (mT) | Groove, zero 16 mm | No groove, 16 mm | In range: groove 13 / 16 / 19 mm | In range: no groove 13 / 16 / 19 mm (needs 22.7 / 17.3 / 11.4 mT) |
|---|---|---|---|---|---|
| TMR2584, offset tempco read as a total | 0.10 | 0.42 % | 1.50 % | yes / yes / yes | no / yes / yes (±20 mT) |
| TMR2584, read per kelvin | 9.0 | 12.9 % | 45.9 % | yes | no / yes / yes |
| TMR2185 | n/s | cannot be told | cannot be told | yes | no / yes / yes |
| CT100 | 0.08 | 0.14 % | 0.50 % | yes | no / yes / yes |
| TMR2083S | 0.10 | 0.35 % | 1.24 % | yes | yes |
| TMR2152S | 0.45 | 1.33 % | 4.74 % | yes | yes |
| TMR2151S | 0.90 | 1.96 % | 6.99 % | yes | yes |
| DRV5055A3 | 2.2 | 3.10 % | 11.1 % | yes | yes |
| DRV5055A4 | 4.4 | 6.19 % | 22.0 % | yes | yes |
| TMAG5253BA4 | 6.7 (0.67 over 0…50 °C) | 9.41 % | 33.5 % | yes | yes |
| A1304-T | 1.0 (25→85 °C only) | 1.42 % | 5.07 % | yes | yes (±37.5 mT) |
| MLX91377, ±40 mT span | 0.08 | 0.48 % | 1.70 % | yes | yes |

At 2.00 T the level at the zero is about 0.95 mT per 1 % (table above), so every figure in the groove column falls
by about a quarter. Sixteen elements summed divide the noise and independent offsets by about 4, not the common
temperature drift (`d_measurement_chain.md` §5).

**What a Hall element gains and loses here.** Gains: range (±37.5–176 mT) and no saturation in any standing field
of the net, so the axial element would not need the zero to sit on it, and a tolerance or a passing 20 % loss
cannot push it out of range; a noise density is on three of the four Hall sheets (0.014–0.015 mT p-p, d), a noise figure without a
band on the fourth; lifetime drift is stated on
three sheets where no TMR sheet states any. Loses: the zero-field offset drift is 1–7 mT over temperature on the
four 3.3 V parts, 1.4–9.4 % of metal with the groove and 5–34 % without, so a per-part temperature table would
be needed to come under 1 %; 2–11 mA per element against µA to about 1 mA for the bridges; most options carry +0.12 %/K
sensitivity drift by design (the DRV5055 Z options 0 typical). With the groove, the TMR parts whose sheets give an
offset drift resolve 0.1–2 % of metal on one element (TMR2584 0.4 % or 13 %, depending on how its sheet is read).

**Direction, both ways (the board arrangement is not confirmed).** The Hall parts read here, and the Z-axis TMR2584,
sense out of the package plane; the other TMR parts sense in the plane. On a thin board across the rope (the
working prototype's arrangement as recorded), the axial field is perpendicular to the board: an out-of-plane part
reads it flat on the board, so a Hall part or the TMR2584 fits and the in-plane TMR parts would need edge mounting.
On boards along the rope (spokes, the specification's layout), the axial field lies in the board's plane: the
in-plane TMR parts read it flat, and a Hall part would need edge or leaded mounting.

Compared, not picked: with the groove, the Hall parts trade a few % of metal of uncorrected offset drift for range;
without the groove the same drift is 3.6 times larger in % of metal.

**Source table** (sheets read for this note; PDFs not copied).

| Part | Sheet | Revision | Address |
|---|---|---|---|
| TMR2584, TMR2185 | MultiDimension data sheets | v2.1 / v2.1.2, copies on file, via `sws_sensor_candidates.md` | maker's site, dowaytech.com |
| CT100 | Allegro CT100 1D Linear Sensor | CT100-DS Rev. 8 | https://www.allegromicro.com/-/media/files/datasheets/ct100-datasheet.pdf |
| TMR2151S, TMR2152S | MultiDimension TMR215x TMR Linear Magnetic Sensor | v1.2.2 | https://www.dowaytech.com/en/index.php?c=download&id=3419 |
| TMR2083S | MultiDimension TMR2083 data sheet | v1.0.1, via `sws_sensor_candidates.md` | https://www.dowaytech.com/en/index.php?c=download&id=2823 |
| DRV5055 | TI DRV5055 Ratiometric Linear Hall-Effect Sensor | SBAS640C | https://www.ti.com/lit/ds/symlink/drv5055.pdf |
| TMAG5253 | TI TMAG5253 Low-Power Linear Hall Effect Sensor With EN Pin | SBASAI5E | https://www.ti.com/lit/ds/symlink/tmag5253.pdf |
| A1304 | Allegro A1304 Linear Hall-Effect Sensor IC with Analog Output | A1304-DS Rev. 4 | https://www.allegromicro.com/-/media/files/datasheets/a1304-datasheet.pdf |
| MLX91377 | Melexis MLX91377 High Performance Linear Hall Effect Sensor IC | Revision 001 | https://www.melexis.com/-/media/files/documents/datasheets/mlx91377-datasheet-melexis.pdf |

Prices: order of magnitude from distributor search listings (not opened). A1367 left out: its higher-sensitivity
options are last-time-buy on its sheet (`sws_sensor_candidates.md`).

### 6. Not calculated

The rope curves other than the middle one; temperature (all at 25 °C; N52's knee from `f_magnet_mech.md`, old box,
not re-run); the level along the rope (only the loss centred on the head, z_d 0); the short ring's ΔB_z peak search
(only ΔB_r); the inner-wire margin itself (3D; read across); 3D, the split, real surroundings (the large box is
empty); forces, stray field and weight at the new thicknesses (`f_magnet_mech.md` gives them for × 0.8–1.9 in the old
box); the N48SH fine net (only its 16 mm line); build tolerances on the axial element's range; long-term drift of any
element (on no sheet); any measurement.

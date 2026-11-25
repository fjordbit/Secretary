# Temperature in the twin

Calculated with a lumped estimate over four assumed days; nothing here is measured, and no site data are used.
The climate is described only by its type: hot, humid, subtropical, coastal, with the head at the waterline.

## In plain words

1. Each half gets two digital temperature sensors, one at the upper and one at the lower end of its board,
   because the head stands upright and such parts are cheap. The twin now has them.
2. A small model of one head (five lumped masses: the housing's upper and lower half, the yoke with the magnets,
   and the board's upper and lower end) works out the temperatures over a day from air, sun, wind and the water.
3. Covered, the head follows the air with a lag of an hour or two; the magnets' peak stays within 2 K of the
   air's peak on every day tried.
4. Uncovered (sun on the housing, as during maintenance), the magnets' peak lies 5 K above the air's on the
   hot, clear, still day, and 11.5 K above it on the cold, clear day (the low winter sun falls on the sides).
5. The 45 °C maximum is passed only on the worst-case summer day with the head uncovered: the magnets are above
   it for 5.6 hours (light grey housing), 3.1 hours if the head is uncovered only from 9 to 15 h.
6. The two end sensors read within 0.4 K of each other in this model, less than one 0.5 °C step of the part
   the specification names; the model ties the board closely to the yoke, so a real gradient may be larger.
7. Over one day, temperature changes the size of the loss-of-metal reading by about 1–3 % with the head
   covered and 1.5–5.6 % uncovered, and makes a clean rope read as up to 0.85 % of metal lost or gained
   (N52 and N48SH shown side by side).
8. One figure of the axial sensing element's data sheet is printed without a clear unit; read per kelvin it
   would make a clean rope read as up to 4.8 % of metal (swing up to 2.6 % in a day), read as a total it
   changes the result by under 0.02 %. It is not resolved here.
9. The second sensor travels in the frame's second temperature field, which is already there: the frame is
   unchanged in size and layout.
10. All of it is off unless `thermal.enabled` is set; with it off the twin gives the same bytes as before.

The owner's direction for the line, stated as such: no powerful machine at each winch; the root box does simple
things that limit what is sent; heavier analysis sits after it; everything settable in the root box and in the
twin. Here that means: the half only reads and sends its two temperatures; the correction is done after the box.

## What is assumed

| What | Value | Status |
|---|---|---|
| The four days | profiles in `thermal_days/` (below), from the climate type | ASSUMED until site data are given |
| Head size | Ø 126 × 180 mm | the record (sun study, decided shared head) |
| Masses | housing 5 kg, yoke and magnets 9.0 kg, two boards 0.30 kg | housing 4–6 kg in the register (status A there); magnetics 8.7–9.3 kg on record; boards ASSUMED |
| Heat capacities | housing 500, magnets 470, boards 1 100 J/kg K | 470 from the sun study; 500 (stainless) and 1 100 (FR-4 with parts and gel) ASSUMED |
| Heat inside | 0.6 W (0.3 W per half), half to each board end | record: 0.2–0.4 W per half (sun study heat budget) |
| Finish | light grey: solar absorptance 0.50, emittance 0.90; white, dark and bare stainless as alternatives | the sun study's table |
| Conductances between masses | below, with their arithmetic | ASSUMED |
| Water below | reflects 7 % of the sun; the lower end sees the water surface at the day's water temperature | ASSUMED |
| Covered | no sun, and everything the housing sees is at air temperature, except that the lower end still sees the water | ASSUMED (the sun study's "shielded" case, plus the water) |
| Both halves | the same temperatures (the sun-facing half is not told apart) | ASSUMED |

## What a measurement would replace

- Site data (hourly air, sun, wind, water) for the four days: replaces every day profile.
- A logged day with the head covered and one uncovered (the two end sensors and one on the yoke): replaces the
  conductances and the heat capacities, and shows the real gradient between the ends.
- The housing material, its finish and its mass from the drawing: replaces the housing figures.
- A climate test of a half (each sensing element's zero and gain against temperature): replaces the data-sheet
  terms, and settles the unit of the axial part's offset figure.
- The magnet supplier's remanence against temperature per grade: replaces the single coefficient (−0.12 %/K)
  that the register holds for every grade.

## The four days

Step 10 minutes; the model interpolates to its own 30 s step. The step: the board's time constant is about
4 minutes (below), the sun's elevation changes about 2.5° in 10 minutes, and climate data come hourly at best.
Air follows the ASHRAE design-day shape (Fundamentals 2009, ch. 14) between the stated minimum and maximum; the
sun is the ASHRAE 2009 clear-sky model at latitude 30° N (a subtropical latitude, ASSUMED), as the repository's
sun study uses it, with a cloud factor (beam × (1 − c), diffuse × (1 + c/2), ASSUMED).

| Day | Air min–max (°C) | Dew point (°C) | Peak sun, global / beam (W/m²) | Cloud | Wind (m/s) | Water (°C) |
|---|---|---|---|---|---|---|
| General summer | 26.0–33.0 | 24 | 713 / 560 | 0.3 | 2 night, 4.5 at 15 h | 30 |
| General winter | 8.0–17.0 | 5 | 456 / 539 | 0.4 | 3 night, 4.5 at 14 h | 15 |
| Worst-case summer | 31.8–42.8 | 22 | 929 / 800 | 0 | 1 all day | 32 |
| Worst-case winter | −15.0 to −8.0 | −20 | 712 / 914 | 0 | 0.5 all day | 6 |

Source types: climate-type descriptions of humid subtropical climates (physical-geography textbooks: summer mean
daily maxima about 30–38 °C, warm humid nights, a small daily range near the coast), and the design and
record-class values the repository's sun study already carries for this climate type (summer 0.4 % design dry
bulb 36.0 °C, record 42.8 °C, range 10–11 K, dew point 22–24 °C; winter record −15 °C, range 7 K, dew point
−20 °C; wind 1 and 0.5 m/s as its low, conservative values). The general days are set inside those bounds; the
worst-case days take the record-class values. Each profile file states its parameters and the reason for each
in its header; `thermal_days/make_days.py` writes them.

## The model of one head

A lumped estimate, not a thermal simulation of the real housing. Five masses, each at one temperature:

| Mass | Heat capacity (J/K) | Arithmetic |
|---|---|---|
| Housing, upper half | 1 250 | 5 kg / 2 × 500 J/kg K |
| Housing, lower half | 1 250 | the same |
| Yoke and magnets | 4 230 | 9.0 kg × 470 J/kg K |
| Board, upper end | 165 | 0.30 kg / 2 × 1 100 J/kg K |
| Board, lower end | 165 | the same |

| Link | W/K | Arithmetic (all ASSUMED) |
|---|---|---|
| Housing upper – lower | 0.62 | stainless shell of 5 kg over 180 mm: section 5 / (8 000 × 0.18) = 3.5 × 10⁻³ m²; 16 W/m K × 3.5 × 10⁻³ / 0.09 m |
| Housing half – yoke | 1.8 each | 0.5 mm air gap: 0.026 / 0.0005 = 52 W/m² K, over half the side π × 0.126 × 0.18 / 2 = 0.0356 m² |
| Yoke – board end | 0.5 each | the board on the yoke by spacers; round figure |
| Housing half – board end | 0.2 each | through gel and air; round figure |
| Board upper – lower | 0.043 | along two boards: 20 W/m K (FR-4 with copper) × 0.06 m × 1.6 mm / 0.09 m = 0.021 per board, × 2 |

Outside, per housing half (side half 0.0356 m², one end 0.0125 m²): convection by the sun study's cross-flow
formula (Hilpert, floor 4 W/m² K; at 1 m/s on Ø 126 mm: Re = 1 × 0.126 / 1.6 × 10⁻⁵ = 7 875, h = 9.1 W/m² K);
long-wave exchange with emittance 0.90: uncovered, the side sees half sky (Berdahl-Martin sky temperature from
the dew point) and half surroundings (air temperature above, water below), the top end the sky, the bottom end
the water; covered, everything at air temperature except the lower end, which still sees the water. Sun,
uncovered only: beam on the projected side D × L/2 per half (× sine of the zenith angle) and on the top end
(× cosine), half the sky's diffuse on each side, all of it on the top end, and 7 % of the global reflected
by the water onto the lower side and the bottom end; times the finish's absorptance.

Checks of size. The whole head: 7 060 J/K against about 1.45 W/K to the outside (0.87 W/K convection at 1 m/s
over 0.096 m², 0.58 W/K long-wave, 4 × 0.9 × 5.67 × 10⁻⁸ × 308³ = 6.0 W/m² K), so a time constant of about
7 060 / 1.45 = 4 900 s, 1.4 hours; the board end 165 / (0.5 + 0.2 + 0.043) = 220 s. At noon on the worst summer
day the sun stands 81.5° high (90 − 30 + 21.5 declination), so the sides get little beam: absorbed about 14 W on
the upper half and 9 W on the lower. The model reproduces air temperature in every node when air, dew point
and water are held at 20 °C with no heat inside (a test).

Against the sun study already on record (same record-class air, 42.8 °C): its unshaded light-grey head on the
record day reaches 55 °C and its shaded one 43 °C; here 47.8 °C and 41.5 °C. The difference is the waterline:
the study's head stands over sunlit ground (19 K above air at full sun, reflectance 0.3), this one over water
at 32 °C (reflectance 0.07).

## Results

Per day and cover; "window" is uncovered from 9 to 15 h only. Light grey. Hours are over the 24 h day.

| Day | Cover | Magnets (°C) | Board at the elements (°C) | Upper / lower sensor max (°C) | Upper − lower, largest (K) | Magnets above 45 °C (h) | A sensor above 45 °C (h) |
|---|---|---|---|---|---|---|---|
| General summer | covered | 26.9–33.0 | 27.3–33.4 | 33.4 / 33.4 | 0.04 | 0 | 0 |
| General summer | uncovered | 25.8–35.9 | 26.2–36.3 | 36.4 / 36.3 | 0.22 | 0 | 0 |
| General summer | window | 26.9–35.9 | 27.3–36.3 | 36.4 / 36.2 | 0.22 | 0 | 0 |
| General winter | covered | 9.0–17.1 | 9.4–17.5 | 17.5 / 17.4 | 0.06 | 0 | 0 |
| General winter | uncovered | 7.2–18.9 | 7.6–19.3 | 19.4 / 19.3 | 0.12 | 0 | 0 |
| General winter | window | 9.0–18.9 | 9.4–19.3 | 19.4 / 19.3 | 0.09 | 0 | 0 |
| Worst-case summer | covered | 32.6–41.5 | 33.0–41.9 | 42.0 / 41.8 | 0.13 | 0 | 0 |
| Worst-case summer | uncovered | 30.8–47.8 | 31.2–48.2 | 48.3 / 48.0 | 0.41 | **5.6** | **6.4** |
| Worst-case summer | window | 32.6–47.4 | 33.0–47.9 | 48.0 / 47.7 | 0.41 | **3.1** | **3.8** |
| Worst-case winter | covered | −11.2 to −6.0 | −10.8 to −5.6 | −5.6 / −5.5 | 0.18 | 0 | 0 |
| Worst-case winter | uncovered | −15.6 to 3.5 | −15.2 to 3.9 | 3.9 / 3.9 | 0.25 | 0 | 0 |
| Worst-case winter | window | −11.2 to 3.4 | −10.8 to 3.8 | 3.7 / 3.8 | 0.18 | 0 | 0 |

Uncovered all day, magnets min–max (°C) and hours above 45 °C, by finish (the sun study's four):

| Finish | General summer | General winter | Worst-case summer | Worst-case winter |
|---|---|---|---|---|
| White | 25.8–34.0 | 7.2–17.1 | 30.8–43.6, 0 h | −15.6 to −3.6 |
| Light grey | 25.8–35.9 | 7.2–18.9 | 30.8–47.8, 5.6 h | −15.6 to 3.5 |
| Dark | 25.8–39.0 | 7.2–21.9 | 30.8–54.3, 9.9 h | −15.5 to 14.6 |
| Bare stainless | 26.5–36.9 | 8.2–20.2 | 32.5–51.8, 8.9 h | −13.9 to 7.8 |

### What it does to the reading, both grades

Against the reading at 20 °C (the simulator's `temperature.reference_C`), over the day: min to max, then the
swing (max − min). Two ways, side by side:

- **The simulator's factor**: 1 + (−0.12 %/K) × (T_magnet − 20) on every magnetic term. The register holds one
  coefficient for every grade (sourced for N40SH), so this way N52 and N48SH come out the same.
- **The record's table**: the axial reading at the zero per grade, from the earlier team run
  (`../3d/falsify/b_tolerances.md` section 2, H52 head, zero at 16 mm): against the same grade at 25 °C,
  N52 offset −0.48 / +0.36 % of metal and level +7.9 / −4.7 % at −20 / +45 °C; N48SH −0.94 / +0.60 % and
  +11.1 / −6.2 %. Taken linearly between −20, 25 and 45 °C and on beyond, relative to 20 °C.

Both add the sensing elements against the board temperature (axial: −290 ppm/K on the gain; offset as below).

Size of a loss reading, change in % (min to max; swing):

| Day | Cover | Simulator's factor (both grades) | N52 by the record | N48SH by the record |
|---|---|---|---|---|
| General summer | covered | −1.94 to −1.04; 0.90 | −3.11 to −1.53; 1.58 | −4.05 to −2.02; 2.03 |
| General summer | uncovered | −2.38 to −0.87; 1.50 | −3.88 to −1.23; 2.64 | −5.02 to −1.64; 3.38 |
| General winter | covered | +0.43 to +1.63; 1.20 | +0.59 to +2.23; 1.64 | +0.79 to +2.99; 2.20 |
| General winter | uncovered | +0.15 to +1.91; 1.76 | +0.21 to +2.60; 2.40 | +0.28 to +3.50; 3.22 |
| Worst-case summer | covered | −3.20 to −1.89; 1.31 | −5.32 to −3.02; 2.30 | −6.87 to −3.92; 2.95 |
| Worst-case summer | uncovered | −4.12 to −1.62; 2.50 | −6.94 to −2.54; 4.39 | −8.94 to −3.32; 5.62 |
| Worst-case winter | covered | +3.88 to +4.67; 0.78 | +5.29 to +6.36; 1.07 | +7.12 to +8.55; 1.44 |
| Worst-case winter | uncovered | +2.46 to +5.33; 2.87 | +3.36 to +7.27; 3.92 | +4.51 to +9.77; 5.26 |

A clean rope read as metal lost (+) or gained (−), in % of metal by the simulator's own scale (the axial
standing reading's change divided by `lma.axial_mT_per_pct`, −0.675 mT per 1 %), axial offset term at zero
(min to max; swing):

| Day | Cover | Simulator's factor (both grades) | N52 by the record | N48SH by the record |
|---|---|---|---|---|
| General summer | covered | +0.08 to +0.14; 0.07 | +0.10 to +0.23; 0.12 | +0.18 to +0.37; 0.20 |
| General summer | uncovered | +0.06 to +0.18; 0.11 | +0.08 to +0.29; 0.20 | +0.14 to +0.47; 0.33 |
| General winter | covered | −0.12 to −0.03; 0.09 | −0.14 to −0.04; 0.10 | −0.25 to −0.07; 0.19 |
| General winter | uncovered | −0.14 to −0.01; 0.13 | −0.16 to −0.01; 0.15 | −0.29 to −0.02; 0.27 |
| Worst-case summer | covered | +0.14 to +0.24; 0.10 | +0.22 to +0.40; 0.18 | +0.36 to +0.65; 0.29 |
| Worst-case summer | uncovered | +0.12 to +0.31; 0.19 | +0.18 to +0.52; 0.34 | +0.30 to +0.85; 0.54 |
| Worst-case winter | covered | −0.35 to −0.29; 0.06 | −0.40 to −0.33; 0.07 | −0.72 to −0.60; 0.12 |
| Worst-case winter | uncovered | −0.39 to −0.18; 0.21 | −0.45 to −0.21; 0.24 | −0.82 to −0.38; 0.44 |

Arithmetic of one cell (simulator's factor, worst-case summer, covered, at the magnets' peak 41.5 °C, board
41.9 °C): factor 1 − 0.0012 × 21.5 = 0.9742; axial gain 1 − 290 × 10⁻⁶ × 21.9 = 0.99365; the standing reading
5 000 µT × (0.9742 × 0.99365 − 1) = −160 µT; −160 / −675 = +0.24 % of metal. The size of a loss reading:
0.9742 × 0.99365 − 1 = −3.20 %.

The axial part's offset figure, the two readings (results file, key `false_loss_pct_metal_min_max_swing`):
read as a total (0.1 mT over −40…125 °C, spread linearly: 0.1 / 165 K = 0.606 µT/K) the swing moves by under
0.02 % of metal; read per kelvin (0.5 mV at 1 V ÷ 5 mV/V/mT = 0.1 mT/K = 100 µT/K) the false loss becomes
−3.9 to −1.5 % (worst-case summer, uncovered) and +2.2 to +4.8 % (worst-case winter, uncovered), swing up to
2.6 % in a day, the same for both grades within 0.3 %. The setting `thermal.axial_offset_uT_per_K` starts at
0 with both readings beside it; this unit does not decide which reading holds.

Ripple size (both grades the same: it follows the simulator's factor and the element gain): radial
−4.7 to −1.9 % (worst-case summer, uncovered) to +2.8 to +6.1 % (worst-case winter, uncovered); axial
−4.1 to −1.6 % and +2.5 to +5.3 %. The whole table is in `thermal_out/results.json`.

The logger's correction (it divides by the simulator's factor at the frame's first temperature field, now the
upper sensor): what it leaves against the true magnet temperature is at most 0.008 % of metal on every day,
because in this model the board ends follow the yoke within about 0.5 K. With a real gradient that is larger,
this residual grows by 0.0089 % of metal per kelvin between sensor and magnets (5 000 µT × 0.0012 / 675 µT).

## How the second sensor travels

| Option | Frame layout | What changes | Each value arrives |
|---|---|---|---|
| **A. The two existing temperature fields** (bytes 18–19 upper end, 20–21 lower end) — built | unchanged, 1 229 bytes | the fields' meaning: the link note calls them "carrier, yoke", the beta filled both with one value | every frame (10 per second) |
| B. The rotating aux slot (byte 22 slot number, 23–24 value) | unchanged | the aux bytes' content: today the beta counts frames in byte 22 and sends 0 in 23–24; slot numbers would be given meanings, on both the Python and the C side | once per rotation, e.g. 8 slots: 1.25 times per second |
| C. A frame change (2 more bytes per extra sensor) | changes: 1 231 bytes or more, a new frame type | half, C half, box, logger, the traffic calculation | every frame |

A is built because it needs neither a layout change nor a new meaning for the aux slot, and the C half's core
already writes the two fields independently (`c_half/test_core.c`, "two different temperatures in their
fields"). With A, a yoke sensor (the specification's "second one on the magnet yoke is cheap") would need B or
C. The C half and the Python half still give the same bytes in every existing test (default settings). What is
left for a byte comparison in the two-field mode: the C host program's input row carries one temperature per
half (`c_half/table_to_bin.py`, `ROW_DT` temps of 2; `c_half/host_main.c` fills `{t, t}`); a row of 2 × 2 and
passing the pair is what is left. The C core itself needs no change.

## Settings

All in `settings.toml`, section `[thermal]` (with `[thermal.finishes]`, `[thermal.G_W_per_K]`,
`[thermal.grade_table]`), each with its unit, source and alternatives; any one reachable by `--set`, e.g.
`run_beta.py --set thermal.enabled=true --set thermal.day_file=thermal_days/summer_worst.csv --set
thermal.cover=uncovered --set thermal.start_hour=13`. `thermal.grade` is empty: it must be named ("N52" or
"N48SH") only with `grade_model = "record_table"`; the runs here show both.

## Files

`linebeta/thermal.py` (the model and the day profiles), `linebeta/thermal_twin.py` (into the signal and the
frame), `thermal_days/` (four profiles and the script that writes them), `thermal_runs.py` (these results),
`thermal_out/` (results.json, summary.csv), `figures/temperature/` (T1–T5), `tests/test_thermal.py` (15 tests).

## Figures

Research type by the plot standard, HTML with hover plus PNG, in `figures/temperature/`:
T1–T4 the four days (air, magnets covered and uncovered, the two end sensors uncovered, the 45 °C line):
[T1](figures/temperature/fig_t1.html) general summer, [T2](figures/temperature/fig_t2.html) general winter,
[T3](figures/temperature/fig_t3.html) worst-case summer, [T4](figures/temperature/fig_t4.html) worst-case winter;
[T5](figures/temperature/fig_t5.html) the false loss over the worst-case summer day, both grades and the
simulator's factor, covered and uncovered.

## Not done

- The sun-facing half against the other half (both halves get the same temperatures); the head's orientation.
- Rain, spray, wetting, condensation, a closed and unventilated cover (the sun study gives +5–10 K for that).
- The converter's own drift with temperature; hysteresis; the radial element in the record's table (radial
  terms use the simulator's factor only).
- `HeadSim.truth_uT` (used by the proof and figures B1/B4) does not include the thermal terms; with the
  temperature on, those comparisons would need it.
- The C host's input row for two temperatures per half (above).
- Sensitivity of the results to the assumed conductances (each ASSUMED; a logged day replaces them).
- The full lift run through the line for each of the 16 cases: the figures above come from the twin's own
  functions; a test checks that the twin's samples follow them and that the two readings reach the logger.

## Terms

- **Head**: the part on the rope, two halves. **Half**: one of them, with its own board.
- **Sensing element**: one field-sensing part (radial or axial). **Channel**: one converter input.
- **Temperature sensor**: here the two cheap digital parts per half, at the upper and the lower end of the board.
- **Covered / uncovered / window**: the head under its cover all day / in the open all day / in the open only
  between two set hours (maintenance).
- **Lumped estimate**: each mass at one temperature, joined by fixed conductances; no shape detail.
- **False loss**: what a clean rope reads as, in % of metal, when only the temperature has changed.
- **% of metal**: the simulator's own scale, the axial reading per 1 % of metallic area lost (−0.675 mT).

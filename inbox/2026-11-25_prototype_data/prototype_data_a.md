# The prototype recording: what the data shows (analysis A)

Measured on the 40 mm prototype head on its rig: two loggers, 12 radial and 12 axial channels, 100 lines per second,
15 recordings (5 at rest, 10 with the head moving). This is a first look at the data. No model is fitted; nothing is
picked or advised. mV/V is what the loggers record; field values in mT or µT rest on the data-sheet sensitivities on record
(radial 3.4, axial 5.0 mV/V per mT) and are shown separately.

## In plain words

1. The recording is clean: all 30 files are complete, with no gaps, no repeated lines, no flat, stuck or clipped
   channel. The two loggers agree to within about 0.05 s once aligned by their
   time stamps, where that can be measured.
2. Standing still, the axial channels read −14 to −51 mV/V (about −3 to −10 mT) and the radial channels −11 to
   +8 mV/V (within about ±3.4 mT). The six elements of a side differ by up to 32 mV/V; that spread is part offsets
   and placement, not something the data can split.
3. At rest the axial channels drift slowly, all the same way: 1 to 7 µT per hour over the 97-minute lunch recording.
4. Noise at rest is low and each channel's own: axial about 0.6 to 1.0 µT rms in 1–10 Hz. Five radial channels
   are as quiet as the axial ones; seven are 5 to 13 times noisier. No channel shares noise with the others on its side.
5. Several channels (radial B2 and A2 most) show short excursions that repeat about every 110 s for long stretches while
   the head stands still. Nothing in the notes explains them.
6. When the head moves, every channel shows the strand ripple: a near-sine wave, one cycle per 0.64 s at the normal
   speed. Radial ripple is about 0.2 to 2.3 mT peak to peak; axial about 0.08 to 0.15 mT. Its size did not change
   between the two speeds used (× 1.29), compared within the afternoon.
7. The ripple repeats very closely pass after pass (radial: 3–10 % left over after aligning), also when the head
   travels the other way. Axial ripple repeats within a session, but changed between morning and afternoon.
8. The level of every channel shifts with the direction of travel: radial by up to 8 mV/V (2.4 mT), axial by up to
   4.6 mV/V (0.9 mT). Two features sit at the same place in every pass: a slow wave once per 8.0 ripple cycles, and
   a stretch of about 30 cycles at the motor-side end where the axial level differs by up to 14 mV/V.
9. A strong magnet near the head moves the readings by up to 11 mT and leaves them changed, by up to 2.5 mT radial
   and 0.64 mT axial: up to 2.9 and 7.5 times the ripple's peak to peak. The axial level does not come back within
   35 s; the radial moves part of the way.
10. Moving the head 1–2 mm off centre changes the axial channels by up to 1.2 mV/V (0.25 mT) in a fixed pattern
   (B1, B2, A3–A6 up; B3–B6, A1, A2 down); the mean of all twelve axial channels moves 5 times less than a single channel. Shaking the rope
   by hand gives movement mostly at 5.9–7.4 Hz that is smaller than the ripple on the radial channels and up to twice it on the
   axial ones.

---

<a id="s1"></a>
## 1. The recording

Two loggers (maker's model GRANITE VOLT 116, 16 differential channels each), one recording the radial elements and
one the axial elements (the notes; logger units 6111 and 7686). Bridge excitation 5000 mV. Channels 1–6 are the B
side, 9–14 the A side; here **B1–B6** and **A1–A6** (element 1–6 of each side). Both loggers use the same channel
names. Table: `tables/inventory.csv` (per file); `tables/inventory.json` adds per-channel minimum and maximum.

| Recording | What (the notes) | Length radial / axial (s) | Lines, radial / axial |
|---|---|---|---|
| steady1 | head at rest, almost at the far side | 581.2 / 581.4 | 58 125 / 58 143 |
| run1–run4 | one pass each, run1 from the motor side, run2 back, 3–4 repeat 1–2 | 104.6–116.8 / 108.8–113.1 | 10 461–11 680 / 10 877–11 308 |
| steady2 | head at rest at the motor side, over lunch | 5798.0 / 5792.8 | 579 800 / 579 278 |
| steady3 | strong magnet near the head (B side twice, A side once) | 151.9 / 152.1 | 15 192 / 15 207 |
| steady4 | head off centre in steps of about 1–2 mm | 173.1 / 166.5 | 17 311 / 16 647 |
| steady5 | rope shaken by hand | 175.9 / 181.5 | 17 587 / 18 147 |
| run5–run6 | repeat of run1–2 (centre may differ after steady4) | 99.9–101.9 / 95.3–96.4 | 9 997–10 193 / 9 530–9 639 |
| run7–run8 | repeat of run1–2, slightly faster | 75.6–82.9 / 77.4–82.3 | 7 564–8 294 / 7 742–8 231 |
| run9 | back and forth at midspan, 4 times | 189.3 / 183.3 | 18 929 / 18 333 |
| run10 | back and forth at midspan, 2 times, with a manual ramp | 136.6 / 131.5 | 13 663 / 13 150 |

- **Rate**: 100.000 lines per second in every file; every time step is 10 ms; record numbers step by 1 throughout:
  no gaps and no repeated record numbers in any of the 30 files. No missing values.
- **Flat, stuck, clipped, dead**: none. No channel has a standard deviation under 0.0001 mV/V; no channel holds the
  same value for 10 lines in a row. Largest |value| anywhere: radial 42.5 mV/V, axial 59.8 mV/V (both in steady3),
  against the edge of the parts' specified range (radial 3.4 × 20 = 68 mV/V; axial 5.0 × 20 = 100 mV/V; data
  sheets) and the logger input range (below).
- **The two loggers' clocks.** The loggers start 2–4.4 s apart in each file, but stamp on the same 10 ms grid, so
  shared stamps can be matched one to one. How well that aligns them: the activity of each logger (sum over its
  channels of the change per line) cross-correlated within ±3 s (`a1b_clock.py`). Where both see the same events
  (all runs, steady3–5; normalised peak 0.48–0.98), the axial logger's stamps lie **+0.013 to +0.030 s** from the
  radial logger's in the morning runs and **−0.024 to −0.053 s** in the afternoon files: within 1 to 5 lines, moving
  by about 0.07 s between morning and afternoon. steady1 and steady2 have no shared event (peak 0.03 and 0.007), so
  no estimate there. Every analysis below aligns by time stamp only; an error of up to 5 lines is not corrected.
- **Logger data sheet** (the maker's public product page, maker and model only): input ranges ±5000, ±1000 and
  ±200 mV; 24-bit converter; accuracy ±(0.04 % of reading + offset) at 0–40 °C; up to 16 channels at 167 Hz. The
  page states no input noise figure and no filter details. Which range and filter were used is not in the
  notes. The axial levels (up to 59.8 mV/V × 5 V = 299 mV) exceed the ±200 mV range, so that logger was not on it.

<a id="s2"></a>
## 2. Standing levels

Median of each channel with the head at rest (`a2_standing.py`, `tables/standing.json`). steady1 whole file (far
side), steady2 whole file (motor side), steady3 / steady4 / steady5 before anything was done (first 8 / 10 / 4 s).

| mV/V | B1 | B2 | B3 | B4 | B5 | B6 | A1 | A2 | A3 | A4 | A5 | A6 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| radial, steady1 | 0.9 | −1.0 | −10.8 | −4.2 | −1.1 | −8.0 | −2.7 | 1.3 | 1.3 | −1.1 | 0.8 | −3.1 |
| radial, steady2 | 1.7 | 5.7 | −1.9 | −0.4 | 0.1 | 2.7 | 0.2 | 2.1 | 7.9 | −0.8 | 6.4 | 4.2 |
| radial, steady4 | 0.5 | −3.8 | −9.4 | −11.1 | −2.2 | −5.9 | −8.7 | −1.0 | −1.8 | −1.3 | −3.2 | −1.8 |
| axial, steady1 | −46.5 | −29.4 | −21.7 | −17.1 | −25.5 | −34.8 | −39.7 | −25.9 | −22.1 | −21.1 | −32.5 | −48.7 |
| axial, steady2 | −47.7 | −33.0 | −27.8 | −25.8 | −37.9 | −50.5 | −48.8 | −31.0 | −23.2 | −18.8 | −29.5 | −46.1 |
| axial, steady4 | −42.1 | −25.5 | −18.1 | −13.8 | −21.6 | −29.7 | −35.4 | −22.5 | −19.7 | −18.7 | −29.2 | −44.5 |

- **In field units** (÷ 3.4 radial, ÷ 5.0 axial; the part's own offset, up to ±10 mV/V = ±2.9 mT radial and ±2 mT
  axial by the data sheets, is inside these numbers and cannot be taken out): axial −2.8 to −10.1 mT, radial
  within ±3.4 mT, over steady1–5.
- **Spread between the six elements of a side**: axial standard deviation 9.5–12.1 mV/V, range 24.7–32.1 mV/V;
  radial standard deviation 2.0–4.6 mV/V, range 4.5–11.7 mV/V. The axial pattern runs smoothly from element 1 to
  element 6 on each side (most negative at B1, B6, A1 and A6).
- **A against B** (mean of A minus mean of B): axial −3.2 to +4.2 mV/V, radial +0.9 to +3.5 mV/V. For the same
  element number, A minus B in the axial channels goes from +5.5…+8.0 (element 1) to −11.8…−14.9 mV/V (element 6)
  in steady1, 3, 4 and 5; steady2 (other end of the rope) differs.
- **steady1 → steady5**: the head stood at different places (far side, motor side, midspan for steady1–3; not
  stated for steady4–5), so this mixes place and time. Axial levels move by up to 21 mV/V between files (B6: −50.5 in steady2,
  −29.7 in steady4).
- **Drift at rest, steady2** (straight-line fit over 1.61 h; figure `f2_drift_steady2`): axial **+0.005 to
  +0.037 mV/V per hour, every channel the same sign** = 1.0 to 7.4 µT/h (÷ 5.0); radial −0.019 to +0.014 mV/V per
  hour = up to 5.7 µT/h (÷ 3.4), either sign. Last 5 min minus first 5 min, axial: +0.001 to +0.059 mV/V. The
  radial fits carry the repeated excursions (section 3).
- **Across the day, same place, same last direction of travel** (rest level after the stop): runs ending at the far
  side, 6 minutes apart in the morning: axial within ±0.29 mV/V, radial within ±0.35 mV/V; afternoon pair within
  ±0.15 / ±1.5 mV/V. Morning against afternoon (about 3 h later; centring and steady3 in between): axial
  −3.9 to +2.8 mV/V, a pattern across the elements (B1, B2, A6 up; B5, B6, A1–A4 down), not one common drift. So no
  day drift in mV/V per hour can be read from it: the change is not one rate on all channels.

Figures: `figures/f2_standing_axial`, `figures/f2_standing_radial`, `figures/f2_drift_steady2` (.html, .png).

<a id="s3"></a>
## 3. Noise at rest (steady2, 97 min, head at rest at the motor side)

`a3_noise.py`, `tables/noise_steady2.json`. Band rms with a 4th-order Butterworth band-pass run forwards and
backwards; the top band stops at 49 Hz (the Nyquist frequency is 50 Hz). "Quiet minutes": minutes in which no
channel of that logger shows a slow excursion (range of its 1-s medians within 3 times its median minute); radial
27 of 96 minutes, axial 35 of 96.

| rms, quiet minutes | 0.01–0.1 Hz | 0.1–1 Hz | 1–10 Hz | 10–49 Hz |
|---|---|---|---|---|
| axial, 12 channels | 0.33–4.8 µT | 0.37–0.72 µT | 0.59–0.96 µT | 1.11–1.40 µT |
| radial B1, B3, B4, A1, A6 | 0.55–39 µT | 0.42–0.61 µT | 0.71–0.85 µT | 1.36–1.47 µT |
| radial B2, B5, B6, A2–A5 | 1.2–97 µT | 1.2–2.8 µT | 3.3–8.8 µT | 7.1–18.8 µT |

(µT = rms in mV/V ÷ 3.4 or ÷ 5.0 × 1000; e.g. axial B1, 1–10 Hz: 0.00293 mV/V ÷ 5.0 × 1000 = 0.59 µT.)

- **Spectrum** (figure `f3_spectrum_steady2`; Welch, 655 s segments): flat above about 1 Hz. Floor (median density
  10–45 Hz): axial 0.18–0.23 µT/√Hz; radial B1, B3, B4, A1, A6 0.22–0.24 µT/√Hz; the other seven radial channels
  1.1–3.0 µT/√Hz. Below 1 Hz it rises; slope of log density against log frequency, 0.01–1 Hz: axial −0.7 to −1.4,
  radial −0.3 to −2.3 (the radial slopes carry the excursions).
- **Repeated excursions.** Radial B2 and A2 (up to 2.7 mV/V), B1, A1, B5, A5, B4, A4 (up to about 1 mV/V) and the
  axial B2, B4, A2, A4 (up to 0.2 mV/V) show short slow excursions in bursts of 10–15, one every **about 110 s**
  (strongest spectral line 0.003–0.05 Hz at a period of 109 s in all 12 radial and 10 of 12 axial channels; the
  Welch resolution is 0.0015 Hz, so 100–120 s). They also appear in steady1 and steady4–5. They are not tied to any
  action in the notes. They set the 0.01–0.1 Hz band over the whole file (radial up to 0.57 mV/V = 169 µT rms).
- **Mains**: a line at 49.95–50.00 Hz, just under the Nyquist frequency, in 10 of 12 radial channels (0.0032–0.0063
  mV/V rms = 0.9–1.9 µT rms; A4 also a second line at 49.95 Hz, 0.00095 mV/V) and in 11 of 12 axial channels (0.0002–0.001 mV/V = 0.03–0.19 µT rms).
  A line at 37.5 Hz in five axial channels (about 0.0002 mV/V). What the logger's filter does at 50 Hz is not known
  (above).
- **Common against own noise**: the share of a channel's variance that the mean of the other five channels of its
  side and logger explains: at most 0.2 % (1–10 Hz) and 1.1 % (0.1–1 Hz), radial and axial. A radial channel against
  the axial channel of the same element: correlation −0.025 to +0.016. The noise is each channel's own.
- **How much is the logger.** The public page gives no noise figure, so this cannot be split. What the data shows:
  referred to the logger input (× 5 V), the white floor is 3.8 µV/√Hz on the quiet radial channels (0.00076 mV/V
  × 5000 mV) and 4.5–5.7 µV/√Hz on the axial ones; two part types with bridges of 43 kΩ and 3 kΩ (data sheets) give
  nearly the same floor, about 140 to 800 times the thermal noise of those resistances (3.8 ÷ 0.027 and 5.7 ÷ 0.007) (√(4kTR) at 20 °C: 27 nV/√Hz at
  43 kΩ, 7 nV/√Hz at 3 kΩ). The seven noisier radial channels are 5–13 times above that floor.
- **Drift over the file**: section 2.

Figures: `figures/f3_spectrum_steady2`, `figures/f3_band_rms`.

<a id="s4"></a>
## 4. The runs

`a4_runs.py`, `tables/runs.json`. Methods in the script header; the main choices:
- A **pass** (or leg) is where the radial channels move in 0.5–10 Hz at more than 10 times their rest level.
- **Position in ripple cycles**: the ripple's own phase (Hilbert phase of the radial channels' main component,
  0.7–1.3 × the ripple frequency), one cycle per ripple wavelength. **Not in mm**: travel length, head speed, rope
  construction and lay length are not on record (the rope is 40 mm; its construction is "type unknown" in the
  record), so a period in mm cannot be derived. If the travel length L were known, the ripple wavelength would be
  L ÷ 136 (cycles per pass, below).
- **Ripple size**: band 0.4–4.5 × the ripple frequency, middle 60 % of a pass; peak to peak = median over cycles of
  (max − min) in each cycle.

**What a pass looks like** (figure `f4_pass_run1`): at the start every channel steps to a new level (section
"direction" below), then rides the ripple; the axial level climbs over the first ~30 cycles from the motor side;
at the stop it steps to a new rest level.

**Strand ripple** (runs 1–6, one pass each):
- **Period**: ripple frequency 1.5509–1.5559 Hz, mean 1.5536 Hz → **0.644 s** (1 ÷ 1.5536); runs 7–8: 2.0056 and
  2.0075 Hz → **0.498 s**. **135.93–137.85 cycles per full pass** (runs 1–8).
- **Size, radial**: peak to peak 0.59 (A4) to 7.91 (A1) mV/V, median 3.2 mV/V; ÷ 3.4 = 0.17 to 2.33 mT, median
  0.93 mT. rms 0.21–2.86 mV/V (0.06–0.84 mT).
- **Size, axial**: peak to peak 0.42–0.77 mV/V, median 0.60; ÷ 5.0 = 0.084–0.154 mT, median 0.12 mT. rms 0.16–0.28
  mV/V (0.032–0.056 mT).
- **Shape**: near-sine. 2nd harmonic 1.0–1.7 %, 3rd 0.2–0.3 % of the fundamental (amplitude, summed over radial
  channels).

**Speed** (runs 7–8 against runs 1–6): ripple frequency 2.0065 ÷ 1.5536 = **1.29 times**; pass duration 88.0 ÷ 68.9
s = 1.28 times (pass flanks ±0.25 s). **Ripple size did not change between the two speeds**: peak to peak runs 7–8 ÷ runs 5–6
(same afternoon) per channel, radial 0.97–1.05, axial 0.96–1.04. Against runs 1–6 (which mixes in the
morning-to-afternoon change of the axial ripple): mean of channels radial 1.00, axial 1.06; per channel rms
ratios 0.91–1.36 axial, 0.97–1.05 radial. Only one speed step (× 1.29) was run. In run10's ramps
(ripple frequency rising from about 1.0 to 1.55 Hz) the radial ripple rms (mean of channels) stays 0.78–1.55 mV/V with no trend against
frequency.

**Repeatability** (residual rms ÷ ripple rms after the best shift on the cycle axis; ripple band, 12 channels):

| Pair | Radial ripple | Axial ripple | Shift (cycles) |
|---|---|---|---|
| run3 vs run1, same session (6 min) | 2.7 % | 14 % | +0.04 |
| run4 vs run2, same session | 4.1 % | 12 % | +0.02 |
| run7 vs run5, afternoon, faster | 3.3 % | 33 % | −0.46 |
| run8 vs run6, afternoon, faster | 4.1 % | 21 % | −0.82 |
| run5 vs run1, morning against afternoon | 7.4 % | 82 % | +0.12 |
| run7 vs run1 / run6 vs run2 / run8 vs run2 | 7.8 / 8.6 / 8.1 % | 81 / 71 / 68 % | −0.34 / +0.30 / −0.52 |
| run2 mirrored vs run1, opposite direction | 9.8 % | 54 % | +0.14 |
| run4 mirrored vs run3 / run6 mirrored vs run5 | 8.0 / 8.9 % | 56 / 52 % | +0.10 / +0.62 |

- The whole axial signal (not only the ripple band; rest level removed) repeats to 1.0–3.4 % within a session.
- The radial ripple retraces itself in the opposite direction (8–10 %); the axial ripple does not (52–56 %).
- Morning against afternoon the axial ripple shape changed (68–82 %); the radial did not (7–9 %).

**Direction**: the level of every channel depends on the direction of travel (figure `f4_run9_direction`). Mean
level travelling from the motor side minus travelling towards it (run9 legs, 4 each way, midspan): radial **+1.1
to +8.1 mV/V** (all channels the same sign; ÷ 3.4 = 0.3–2.4 mT), axial **−0.2 to −4.6 mV/V** (÷ 5.0 = 0.03–0.92 mT).
Run1 against run2 (whole passes) gives +0.5 to +7.8 and −0.04 to −4.3 mV/V. The rest level after a stop also
depends on the last direction.

**run9 (back and forth, 8 legs)**: legs of 29.0–39.7 cycles (17.3–23.7 s) at 1.68 Hz. The radial ripple retraces
itself: residual 7–10 % against the leg before (mirrored), 3–6 % against the leg two before (same direction).
**Ripple counting as a distance**: start of each leg by adding up counted cycles (out +, back −) against the start
found by matching the ripple pattern: they differ by −1.16 to +0.63 cycles over legs 3–8 (−0.70, +0.63, −0.14,
+0.09, +0.17, −1.16). After 8 legs the counted position is 2.86 cycles from the start; the matched one is not
known for the last stop (no leg after it).

**run10 (back and forth with a manual ramp, 4 legs)**: the ripple frequency rises from about 1.0 Hz to 1.50–1.55 Hz
within each leg (figure `f4_run10_ramp`). Counting against matching: +2.67 and −2.63 cycles (legs 3 and 4).

**Features at the same place in every pass, not ripple** (mean of four passes each way; figure
`f4_slow_features`; places in ripple cycles from the motor-side end of the pass, the same in both directions):
- **A slow wave of 8.0 ripple cycles** (7.97–8.09 in every channel, both directions), 35–125 cycles, peak to peak
  radial 0.5–4.9 mV/V, axial 1.4–3.5 mV/V (axial ÷ 5.0 = 0.28–0.69 mT).
- **The motor-side end, 0–30 cycles**: the axial level at 1–6 cycles differs from the middle of the pass by −11.0 to
  +0.7 mV/V (from the motor side) and −2.3 to −14.0 mV/V (towards it), largest on B6 (−11.0 / −14.0 mV/V = −2.2 /
  −2.8 mT); radial +0.8 to +8.1 mV/V. It changes steadily over about 30 cycles in both directions.
- **A short burst at about 28 cycles from the motor-side end**, axial channels, in all eight passes (runs 1–8).
  Measure: |signal| in 6–45 Hz in units of the channel's median, largest over the channels in each half cycle. At
  28–28.5 cycles every one of the eight passes reaches at least 7.5 times (typical value along the pass: 4.5); in
  the six passes whose largest value lies at 26–28.5 cycles, its size is 0.16–0.22 mV/V (÷ 5.0 = 0.03–0.04 mT).
- **Not at one place**: short spikes in radial B1 (also B3, B4) in run5 (cycles 53–115) and run7 (cycles 122–124),
  up to 1.3 and 1.5 mV/V in 6–45 Hz; not in the other passes.

Figures: `figures/f4_pass_run1`, `f4_repeat_B6`, `f4_slow_features`, `f4_run9_direction`, `f4_run10_ramp`.

<a id="s5"></a>
## 5. A strong magnet near the head (steady3)

`a5_steady3.py`, `tables/steady3.json`. Head at rest at about midspan. Event windows read off the activity trace (s
from the first shared stamp): **B side, first** 9.0–24.0; **B side, second** 34.5–41.8; **A side, snapped to the
yoke and pulled off** 53.5–112.2 (snap at 59.3 s). Level before = median of the 3 s ending 0.5 s before the event;
after = median of 1 s centred 1, 5, 20 and 35 s after it (where the next event allows). Shift = after (5 s) −
before. % of ripple = shift ÷ the channel's ripple peak to peak (runs 1–6) × 100.

| | Largest excursion | Shift after 5 s | Shift in % of ripple pp | Change from 5 to 35 s after |
|---|---|---|---|---|
| radial, B side first | −16.5 mV/V (B4; −4.9 mT) | −0.64 to −3.60 mV/V (−0.19 to −1.06 mT) | −38 to −138 % | next event within 11 s |
| axial, B side first | +9.1 mV/V (B1; +1.8 mT) | −0.59 to +1.91 mV/V (−0.12 to +0.38 mT) | −88 to +446 % | next event within 11 s |
| radial, B side second | −20.9 mV/V (B4; −6.2 mT) | −1.46 to +3.06 mV/V (−0.43 to +0.90 mT) | −42 to +211 % | (11.7 s to the next) |
| axial, B side second | +12.7 mV/V (B1; +2.5 mT) | +0.05 to +1.04 mV/V (+0.01 to +0.21 mT) | +7 to +221 % | (11.7 s to the next) |
| radial, A side snapped | −38.9 mV/V (A3; −11.4 mT) | **−1.42 to −8.47 mV/V (−0.42 to −2.49 mT)** | −58 to −291 % | +0.4 to +3.1 mV/V on 8 channels, under 0.2 on 4 |
| axial, A side snapped | +33.3 mV/V (A6; +6.7 mT) | **−0.58 to +3.20 mV/V (−0.12 to +0.64 mT)** | −89 to +746 % | under 0.04 mV/V on all 12 |

- **Does the zero come back?** Not within the time the recording gives. After the A-side event the axial channels
  stay where they landed (change from 5 to 35 s under 0.04 mV/V on every axial channel).
  Radial channels move back part of the way on 8 of 12 channels (+0.4 to +3.1 mV/V over 30 s, against shifts of
  −1.4 to −8.5); the channels that move most (A2, A1, B2) are among those with the repeated slow excursions of section 3, so
  how much of it is a return cannot be told.
- **Over the whole file** (first 3 s against the last 10 s): radial −0.1 to −9.0 mV/V on 11 channels, +0.6 on A2;
  axial +0.04 to +6.1 mV/V, all positive. ÷ 3.4 / ÷ 5.0: radial up to −2.6 mT, axial up to +1.2 mT.
- **Radial and axial separately**: radial excursions are larger (up to 11.4 mT against 6.7 mT) and the radial shift
  is larger in mT (up to 2.5 against 0.64); against each channel's own ripple the axial shift is larger (up to 7.5
  times the axial ripple pp, against up to 2.9 times the radial).
- **Where it sits** (head, elements or rope) cannot be told from steady3 alone. Afterwards, the axial level along
  the whole pass changed between morning and afternoon by a near-constant pattern (section 6), not by a local step
  at midspan where the magnet was applied.

Figure: `figures/f5_steady3`.

<a id="s6"></a>
## 6. Off centre (steady4) and shaking (steady5)

`a6_steady4_5.py`, `tables/steady4_5.json`.

**steady4.** Nine plateaus between pushes (s): 1–11 (start), 15–30, 33–38.5, 43–57, 73–87, 92–102, 106–110.5,
116–126, 157–165. Change = plateau level − start level.
- The axial changes share one pattern (first principal component, 81 % of the variance): **rising B1 (+0.31), B2,
  A3, A4, A5, A6 (+0.42); falling B3–B6 (B6 −0.41), A1 (−0.31), A2 (−0.03)** (unit vector over the 12 channels).
  Along it the plateaus sit at 0, −0.26, −0.57, +0.56, +2.20, +0.78, −0.40, +0.64, +2.90 mV/V.
- Largest change (plateau 9, figure `f6_steady4_axial`): axial B1 +0.99, B6 −1.19, A1 −1.00, A5 +1.15, A6 +1.23
  mV/V; radial up to −1.39 (B2) and −1.10 (A1) mV/V.
- **Per mm**: push sizes are not on record. Reading the notes' "about 1–2 mm" as the distance of plateau 9 from the
  start: axial up to **1.23 mV/V per mm if 1 mm, 0.62 if 2 mm** (÷ 5.0 = 0.25 / 0.12 mT per mm); radial up to 1.39
  / 0.70 mV/V per mm (0.41 / 0.20 mT per mm).
- **Sums**: standard deviation over the plateaus of one axial channel 0.15–0.58 mV/V (median 0.35); of the mean of
  the six B-side channels 0.13, the six A-side 0.18, all twelve **0.07 mV/V**. Radial: single 0.05–0.98 (median
  0.35), side means 0.33 and 0.25, all twelve 0.28: the radial mean is not steadier than a typical channel.
- **Afternoon against morning passes**: the change of the axial pass levels (run5 − run1, run7 − run3) correlates
  0.74–0.75 with this pattern; towards the motor side (run6 − run2, run8 − run4) 0.33–0.37. All twelve also moved
  down by 0.01–1.6 mV/V.

**steady5** (rope shaken by hand; windows 6–22, 98–121 and 127–150 s; figure `f6_steady5`): dominant frequency
**5.9–7.4 Hz** (2.7–2.9 Hz on seven channels, mostly axial, in one or two windows), against a ripple of 1.55 Hz in the runs. In 0.5–20 Hz the
rms is 0.10–0.63 times the ripple rms on the radial channels and **0.29–2.07 times** on the axial ones (largest on
B1, B6, A6); 1-s peak to peak up to 3.7 mV/V radial (A1) and 1.7 mV/V axial (B1).

<a id="s7"></a>
## 7. The simulator assumes / measured / ratio

Settings from `../../line_beta/settings.toml` (52 mm rope, the product's elements and converter); measured here on
the 40 mm prototype with other parts and a logger, so a ratio is a comparison of two different set-ups, not a
correction. `a7_table.py`, `tables/assumed_vs_measured.json`. µT and mT from mV/V by ÷ 3.4 (radial) and ÷ 5.0
(axial), the data-sheet sensitivities.

| Setting | Simulator assumes | Measured (prototype, 40 mm rope) | Ratio measured / assumed |
|---|---|---|---|
| noise per element (density) | 1.5 µT rms white at 4000/s = 1.5 ÷ √(4000/2) = 0.0335 µT/√Hz | axial 0.178–0.227; radial low group 0.223–0.238, other radial 1.15–3.02 µT/√Hz (median density 10–45 Hz, steady2) | axial 5.3–6.8; radial 6.6–90 |
| noise per element (rms) | 1.5 µT rms over 0–2000 Hz | axial 1.6–5.1 µT, radial 1.9–97 µT rms over 0.01–49 Hz (quiet minutes) | not comparable as rms (different bandwidth); see the density row |
| ripple, radial (half peak to peak) | 265 µT | 86–1163 µT, median 465 (= pp mV/V ÷ 2 ÷ 3.4 × 1000; runs 1–6) | 0.33–4.39, median 1.76 |
| ripple, axial (half peak to peak) | 105 µT | 42–77 µT, median 60 (= pp mV/V ÷ 2 ÷ 5.0 × 1000) | 0.40–0.73, median 0.57 |
| ripple harmonics (2nd, 3rd) | 0.20, 0.10 of the fundamental | 0.010–0.017, 0.002–0.003 (amplitude, radial, runs 1–6) | 0.07, 0.03 |
| strand pitch | 40 mm (52 mm rope) | not in mm: 135.93–137.85 ripple cycles per full pass; travel length not on record | cannot be formed |
| standing, radial | 50 mT | \|level\| 0.01–3.36 mT (÷ 3.4; steady1–5), part offset up to ±2.9 mT inside | 0.000–0.067 |
| standing, axial | 5 mT | \|level\| 2.8–10.1 mT, median 5.5 (÷ 5.0), part offset up to ±2 mT inside | 0.55–2.02 |
| drift | 20 µT/h, one rate on all elements | axial 1.0–7.4 µT/h (all one sign), radial 0.03–5.7 µT/h (either sign); fit over 1.6 h at rest | axial 0.05–0.37, radial 0.001–0.29 |
| hum at the mains frequency | 30 µT at 49.9 Hz (amplitude) | at the logger output, after its own filter: amplitude radial 1.3–2.6 µT, axial 0.05–0.27 µT (= rms × √2) | radial 0.04–0.09, axial 0.002–0.009; a lower bound only |
| hum harmonics, 300 Hz drive tone | 2nd 0.3, 3rd 0.5, 5th 0.2; 10 µT at 300 Hz | above the logger's 50 Hz Nyquist frequency: not in this data | cannot be formed |
| long loss, level per 1 % | axial −0.675 mT per % | notes.txt names no loss of metal on the rig's rope | cannot be formed |
| broken wire | radial 1.35, axial 0.156 mT | notes.txt names no broken wire; one short axial feature repeats in every pass (section 4, 0.03–0.04 mT); what it is, is not on record | cannot be formed |
| temperature, magnet coefficient | −0.12 %/K | no temperature in the recording or the notes | cannot be formed |
| speed | 3.2 m/min (52 mm case) | not in m/min; runs 7–8 against 1–6: × 1.29 (ripple frequency), × 1.28 (pass duration) | cannot be formed |

The record holds that the rig's rope carries faults made by hand, with no places on file; notes.txt says nothing
about faults either way, so none is assumed here.

## What this data cannot tell

- Anything in mm, m or m/min: no travel length, head speed, lay length or rope construction is on record. Only
  ratios and ripple cycles.
- Absolute field: each part's offset (up to ±10 mV/V) sits inside every standing level; the sensitivities are data-
  sheet values at 1 V supply and 25 °C, not checked on these parts; which element sits where round the rope (angle)
  is not in the notes.
- Whether the steady3 shift lives in the elements, the head's steel and magnets or the rope.
- How much of the noise is the logger: no noise figure on its public page, range and filter settings not in the
  notes.
- The hum at the elements (the logger's filter at 50 Hz is not known) and anything above 50 Hz.
- Anything about temperature, so neither the cause of the axial drift nor a magnet coefficient.
- Broken-wire or loss-of-metal signal sizes: no known fault or loss with a place.
- What causes the 110 s excursions, the 8-cycle wave, the motor-end stretch, the burst at 28 cycles, the direction
  offset and the B1 spikes in run5 and run7.

## Questions to the test engineer

1. How long is the head's travel, and what speed did the drive run at in runs 1–6 and 7–8 (in m/min)?
2. What is the rope: construction, number of outer strands, lay length?
3. What range, filter or integration setting and 50 Hz rejection were set on the two loggers?
4. Where does each element (B1–B6, A1–A6) sit round the rope, and which side of the cut plane is A?
5. In steady4: how far and which way was each push, and is the start position the centred one? Was the head
   re-centred before run5?
6. In steady3: what magnet, at what times, and was the head at the same place along the rope as the magnet?
7. What is at the motor-side end of the travel (the first part of each pass): steel, the drive, a clamp, a fault?
8. Are there known faults on this rope, and where (in metres from the motor-side end)?
9. Was the temperature noted at any time, and did anything near the rig switch on and off about every 110 s during
   the lunch recording?
10. Was anything touched or changed between the morning runs and steady3 (cable, clamp, head position)?

<a id="terms"></a>
## Terms

- **Head**: the 40 mm prototype head; **half**: one of its two halves (A and B side of the cut plane).
- **Sensing element (radial / axial)**: one element reading the field across / along the rope; on this head a
  TMR2185 (radial) and a TMR2584 (axial) part (record), data-sheet sensitivity 3.4 and 5.0 mV/V per mT.
- **Channel**: one logged signal, B1–B6 and A1–A6 per logger; radial channels on one logger, axial on the other.
- **mV/V**: logger output in mV per V of bridge excitation (5000 mV here).
- **Pass, leg**: one movement of the head from stop to stop.
- **Ripple, ripple cycle**: the near-sine wave the strands make while the head moves; one cycle = one ripple
  wavelength of travel.
- **pp**: peak to peak. **rms**: root mean square.
- **Quiet minutes**: minutes of steady2 with no slow excursion on any channel of that logger.

## How it was made

Scripts in this folder, run in order with Python and numpy, scipy, matplotlib (isolated mode, the raw data folder
and a cache folder outside the repository as arguments): `a1_inventory.py`, `a1b_clock.py`, `a2_standing.py`,
`a3_noise.py`, `a4_runs.py`, `a5_steady3.py`, `a6_steady4_5.py`, `a7_table.py`; `pdlib.py` reads the logger files,
`figs.py` draws through the plot standard (`../../3d/groove_plots/plotstandard.py`, unchanged). The raw files are
not in the repository; `tables/` holds only derived numbers. Figures: `figures/*.html` (interactive) and `.png`.

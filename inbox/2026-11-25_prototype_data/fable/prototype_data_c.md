# Prototype recording: analysis C (Claude Fable 5.2, blind), with an independent check

Analysis C is one outside model's reading of the prototype recording. It was made blind: the model had the
measured data, the test engineer's notes, the file format and the questions, and nothing from the project.
Its full report, scripts and derived tables are in `answers/`. The brief it got is `brief.md`. How it was run
and limited is in `run_record.md`. This note gives what it found and how far its numbers held when they were
recomputed from the raw files by independent scripts (`check/`). It draws no conclusions beyond that check.

## What the model found, in ten plain lines

1. All 30 files are clean: 100 samples per second exactly, no gaps, no repeated records, no flat, clipped or dead channel.
2. The two loggers' clocks drift apart by about 15 ms per hour. They agree within one sample in the morning and are 4 to 5 samples apart in the afternoon.
3. Every channel carries a slow train of pulses, one about every 100 s, that repeats about every 40 minutes. Its timing matches the two loggers' clocks slipping past each other. The model reads it as the loggers disturbing each other, and says itself that this is an inference.
4. With the rope at rest and nothing touched, the levels drift by at most 0.013 mV/V per hour (radial) and 0.036 mV/V per hour (axial).
5. With the rope moving, the radial channels show a near-sine ripple of up to 7.9 mV/V peak to peak. The axial ripple is 0.3-0.6 mV/V. A pass holds 134 ripple periods. No period in mm can be derived from the files.
6. The ripple phase steps by about -120 degrees from each element to the next round the ring. A second line sits at one eighth of the ripple frequency.
7. The same pass repeated minutes later comes back the same. Forward and backward passes differ by a level offset of up to 7.6 mV/V (radial) and a shift of about 0.2 s. Speed (1.29 times) does not change the radial ripple size.
8. The strong magnet left a step in every channel: radial down by up to 9 mV/V and axial up by up to 6 mV/V, which is more than one ripple peak to peak. Nothing of it came back within 28 minutes.
9. Moving the head off centre changes the axial channels by up to about 0.66 mV/V per mm, as one sine round the ring; the mean of all twelve largely cancels this. The per-mm figure rests on an assumed 2 mm, which is good to a factor of two.
10. Hand shaking sits at 5-10 Hz (peak about 7.4 Hz). It is smaller than the ripple in the radial channels and larger in the axial ones.

## The check: headline figures recomputed from the raw files

The figures were recomputed by scripts written for this check, from the model's stated definitions, without
its scripts (`check/c1`-`c8`; outputs in a local folder, not committed). Separately, two of the model's own
scripts (`q1a_inventory.py`, `q5_steady3.py`) were read and then re-run on a separate copy of the data. Both
gave results identical to the byte with the ones the model saved.

| # | claim (report id) | model | this check | verdict |
|---|---|---|---|---|
| 1 | rate, gaps, record steps (H1) | 100.00000 /s; 0; 0 | 100.000 /s in all 30 files; largest step 10 ms; 0 record steps other than +1 | agrees |
| 2 | clock offset, radial minus axial, steady5 (H2) | +42.9 ms | +41.8 ms (2-20 Hz band, sum of 12 channels per logger, cross-correlation peak, parabolic interpolation) | agrees (1.1 ms) |
| 3 | clock offset, steady3 (H2) | +29.5 ms | +23.7 ms (same method) | partly: 5.8 ms apart, about half a sample; method-dependent |
| 4 | quantisation step (H4) | 1.28496e-4 mV/V | 1.284963e-4 mV/V (least-squares divisor of small differences, 146 file-channels) | agrees |
| 5 | slow pulse train (H5) | spacing 98-103 s; 12 per train; repeat about 2380 s; p-p radial A2 5.27, B2 5.19 | median peak spacing 101 s on all large-pulse channels; one pause of about 1270 s between trains; slow p-p A2 5.23, B2 4.93 mV/V | agrees |
| 6 | 0.01-0.1 Hz rms as logged, steady2 (H8) | radial 0.013-0.69; axial 0.0023-0.043 mV/V | radial 0.012-0.62; axial 0.0026-0.039 mV/V (FFT band sum) | agrees |
| 7 | mains tone, radial B3 (H9) | 0.0075 mV/V | 0.0075 mV/V (same demodulation, without floor correction) | agrees |
| 8 | drift, axial B6, steady2 (H10) | 0.036 mV/V per h | 0.0369 (line fit); 0.0370 (last minus first 600 s: 0.0534 mV/V / 1.444 h) | agrees |
| 9 | ripple frequency (H11) | run1 1.5529 Hz; run8 2.0037 Hz; 133.8 periods per pass (f x duration) | run1 1.5553 Hz; run8 2.0050 Hz (FFT peak, middle 60 %); 1.5553 x 86.03 s = 133.8 | agrees (within 0.15 %) |
| 10 | ripple size, run1 radial A1 (H12) | rms 2.845; p-p 7.876 mV/V | rms 2.843; p-p 7.94 mV/V | agrees |
| 11 | speed ratio (H16) | 1.293 | 2.0050 / 1.5553 = 1.289 (run8/run1); 1.293 (run7/run5) | agrees |
| 12 | ripple phase steps round the ring, run1 radial (4.2) | -123 ... -148 degrees, sum -1440; reversed going backward | -121, -125, -132, -114, -109, -99, -108, -112, -130, -120, -120, -151; sum -1440; run2 all positive (sum +1440); run7 the same as run1 | agrees |
| 13 | line at one eighth of the ripple, run1 (4.2) | radial 0.16-1.16; axial 0.36-0.52 mV/V | radial 0.16-1.18; axial 0.37-0.54 mV/V | agrees |
| 14 | run1 against run3, residual as logged (4.3) | per channel 0.067-1.948, median 0.45 mV/V | 0.071-1.912, median 0.44 (shift and stretch on whole samples) | agrees |
| 15 | run1 against run3, axial residual (H14) | median 0.053 (largest 0.072) mV/V | median 0.075 (largest 0.100), alignment to whole samples only | partly: same order, about 40 % higher here |
| 16 | step left by the magnet, axial (H18) | +0.09 ... +6.05 mV/V | +0.09 ... +6.07 mV/V (last 5 s minus first 5 s) | agrees |
| 17 | step left by the magnet, radial (H18) | -0.95 ... -8.97, all negative (pattern-corrected) | as logged -9.00 ... +1.11; A2 +1.11 and A4 +0.05; B4 -8.25 against -8.97 | differs as logged. The model's figure depends on its own pulse-train correction, which was not reproduced here. |
| 18 | recovery after 28 minutes (H19) | B4 +0.04 mV/V (0.4 % of the step) | B4 -0.20 mV/V (2.4 % of 8.25) | agrees in substance: no recovery |
| 19 | shaking: frequency and size (H21; 6.2) | 7.4 Hz; burst rms radial A1 0.660, axial B1 0.321 mV/V; 70 s of bursts | 7.3 Hz; 0.756 and 0.365 mV/V; 53.5 s of bursts by the same rule | partly: about 15 % higher here; the burst threshold sets the size |
| 20 | spikes on radial B1 (H22) | run5 166, run7 34; largest 1.66 and 1.99 mV/V | largest 1.66 and 1.99 mV/V; counts 450 and 88 with a simpler rule (no local-maximum test); run1: 1 | agrees on place and size; the count depends on the rule |

**Summary:** of 20 figures, 15 agree, 4 agree in part, and 1 differs as logged (no. 17). The difference is fully
explained by the model's pulse-train correction. That correction is the one part of the analysis this check
did not reproduce, and every "pattern-corrected" figure in the report rests on it. They are mainly the
pattern-corrected levels, the drift and the repeat residuals of the eight large-pulse radial channels.

## What the model claims beyond what the data shows

- **The pulse train as interference between the two loggers.** This is an inference from timing; the model says so
  itself. The pulse train is in the data (check no. 5). Its cause is not.
- **"The magnet left the head in the state a reversal produces."** This rests on a correlation of 0.973 (radial) and
  0.880 (axial) between the step and the forward/backward offset. That is a comparison, not shown causation.
- **"Eight equal features per turn".** This reading of the -120 degree phase step and the 1/8 line rests on twelve
  evenly spaced elements, which the model assumed. The phases themselves hold (checks no. 12 and 13).
- **The per-mm figures of the off-centre test** rest on the model taking the farthest position as 2.0 mm. The model
  says so and gives a factor of two.
- **"The one clear fault"** is the model's word for the spikes on radial B1 (report section 1.2). The brief asked for
  repeating features to be described without naming a cause. The model also calls the spikes "not a magnetic
  feature", which the data does not show either way.

## What it could not tell (its own list, shortened)

Anything in mm or mm/s; the field in physical units; how much of the noise is the logger's own (no shorted-input
record); proof of where the pulse train comes from; true time; the true mm scale and direction of the off-centre
test; what changed the afternoon trace (the magnet, the off-centre test and the shaking cannot be separated); whether
the 0.2 s shift between the directions belongs to the drive or the signal; what the features along the pass are;
temperature effects and stability from day to day; behaviour outside the tested speeds; where the rope stood in
steady1. Ten questions to the test engineer are at the end of `answers/report.md`.

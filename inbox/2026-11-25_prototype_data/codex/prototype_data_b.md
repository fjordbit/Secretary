# Prototype recording, analysis B: the newest Codex through a script loop

Codex (gpt-5.3-codex-xhigh, through the round tool) never saw the data. It wrote analysis scripts from a blind
brief and the file format; the scripts were read and run here on a copy of the data; their outputs went back,
and it gave its findings. Two rounds. Its answers are in `answers/`, the briefs beside this note. Below: what
it found, how much of it holds against an independent recomputation from the raw files, and what it could
not tell. This note draws no conclusions of its own beyond the check.

## What Codex found, in ten plain lines

1. All 30 files are at 100 records per second, with durations from 75.63 s to 5797.99 s, and no flat, clipped
   or dead channel.
2. It reports about 1 % of records missing in every file (for example 104 in run1); the check shows this is a
   reading error in its own script, not the data (row 1 below).
3. The two loggers' time stamps line up to within one sample (0.01 s).
4. Standing levels differ a lot between the sensing elements: radial means from -10.8 to +1.3 mV/V in steady1,
   axial from -48.7 to -17.1 mV/V; side A minus side B is +3.4 mV/V radial and -2.5 mV/V axial in steady1.
5. From steady1 to steady5 every axial channel rose by +2.3 to +4.4 mV/V; radial channels moved both ways.
6. In the long quiet record (steady2) the radial channels carry 0.03 to 0.83 mV/V rms in total, mostly below
   0.1 Hz; the axial channels 0.012 to 0.056 mV/V; radial channels are more alike (mean |correlation| 0.43
   against 0.28 axial).
7. A periodic ripple runs through every pass at about 0.635 s, and about 0.495 s in the faster runs 7 and 8.
8. It reads the ripple as larger at the higher speed (ratios 1.2 to 2.6); the check does not support that (row 11).
9. In steady3 (strong magnet) it found one radial and two axial events, with radial levels that did not return;
   the check finds three events in both loggers and different after-levels (rows 12, 13).
10. In steady4 it gives -0.2 to +1.3 mV/V per mm radial and -0.6 to +0.6 mV/V per mm axial (assuming 1.5 mm),
    and says sums over a side are not steadier than one channel; the check finds the opposite once the sum is
    scaled to one channel (row 14). steady5 (shaking) sits at about 0.11 to 0.17 Hz.

## The check

Recomputed from the raw files with scripts in `check/` (`load.py` reads the files; `check.py`, `base.py`,
`ripple.py`, `steady3_means.py`; their printed outputs beside them). None of Codex's code or outputs is used.

| # | Codex's figure (answer round 2) | Independent figure | Agrees? |
|---|---|---|---|
| 1 | about 1 % of records missing in every file: run1 radial 104 of 10 461, steady2 radial 5 798 of 579 800 | 0 gaps in the record numbers. The 104 and 5 798 are exactly the records whose time stamp falls on a whole second (written without decimals); its time parser drops them | no |
| 2 | 100 Hz in all files; durations 75.63 s (run8 radial) to 5797.99 s (steady2 radial) | 100.000 Hz; 75.63 s and 5797.99 s | yes |
| 3 | stamps of the two loggers match with offset 0 s, uncertainty 0.01 s | cross-correlating the steady3 event edges of the two loggers: axial 3 samples later, +0.03 s | yes in size; the 0.01 s is too tight |
| 4 | steady means: radial steady1 -10.812 to +1.335 mV/V; axial steady2 -50.535 to -18.783 mV/V | -10.812 to +1.335; -50.535 to -18.783 | yes |
| 5 | A minus B, radial steady1 +3.415 mV/V; axial steady2 +4.211 mV/V | mean B - mean A = -3.41 and -4.21, so A - B = +3.41 and +4.21 | yes |
| 6 | steady5 - steady1: radial brfull4 -6.122 mV/V; axial +2.293 to +4.442 mV/V | brfull4: -10.314 - (-4.193) = -6.121; axial: brfull4 -14.804 - (-17.097) = +2.293, brfull14 -44.278 - (-48.719) = +4.441 | yes |
| 7 | drift over the day, line through the five steady-file means: radial all negative, -3.163 to -0.214 mV/V per hour; axial +1.263 to +3.290 | same line: -3.163 to -0.214 and +1.263 to +3.290. Without steady3 (the file with the magnet events): radial -2.687 to +0.145, axial +0.891 to +2.873 | arithmetic yes; "all radial negative" rests on steady3 |
| 8 | steady2 total rms: radial 0.028 to 0.831 mV/V, axial 0.012 to 0.056 mV/V | standard deviation per channel: radial 0.0281 to 0.831, axial 0.0124 to 0.0557 | yes |
| 9 | tones: axial 37.878 Hz, radial near 48.5 Hz | axial 37.500 Hz; strongest radial line in 30-50 Hz at 49.83 to 49.90 Hz. 37.5 x 100 / 99 = 37.88: its frequencies run 1 % high because of the dropped records (row 1) | no |
| 10 | ripple period about 0.635 s (runs 1-2), 0.493-0.498 s (runs 7-8) | 0.640 s (1.562 Hz) and 0.500 s (2.002 Hz); 1.5625 x 100 / 99 = 1.578 Hz, the same 1 % shift | yes within 1 % |
| 11 | ripple larger at higher speed: run7/run1 1.325-1.558 radial, 1.222-2.607 axial | rms of the ripple line in the spectrum (peak ±0.15 Hz): run7/run1 radial 0.93 to 1.09 (median 0.99), run8/run2 1.00 to 1.13; axial median 0.91 and 0.95 (range 0.69 to 2.21). Its ratio comes from a 1 s smoothing filter that passes more of a faster ripple | no |
| 12 | steady3: 1 radial event, 2 axial events | 2 s means show three excursions in both loggers, at about 11-27 s, 37-45 s and 57-115 s from file start (`check/steady3_means_output.txt`) | no |
| 13 | steady3 after-levels: radial does not return, +2.85 to +35.4 mV/V; axial event 2 -0.40 to +1.77 mV/V | level in the last 20 s minus the first 10 s: radial -8.92 to -0.57 mV/V; axial +0.05 to +6.05 mV/V (largest brfull6 side B: -29.69 - (-35.74) = +6.05) | no |
| 14 | steady4: sums over a side are not steadier than one channel (std ratio 2.1 to 9.7) | its ratio compares a sum of 6 with one channel. Scaled to one channel (side mean): radial B 0.348 against 0.349 median single (ratio 1.00), radial A 0.246 (0.70); axial B 0.149 and A 0.170 against 0.369 (0.40, 0.46); all twelve axial 0.065 (0.18) | no |
| 15 | steady5 dominant frequency about 0.110 to 0.171 Hz | 0.110 to 0.146 Hz (resolution 0.012 Hz) | yes |

Count: 8 agree (2, 3, 4, 5, 6, 8, 10, 15), 1 agrees in arithmetic only (7), 6 differ (1, 9, 11, 12, 13, 14).
Not checked: the repeatability residuals (run1 against run3, run5, run2), the run9 and run10 position-error and
ramp figures, and the steady4 per-mm figures. These rest on its own alignment and splitting methods, which
were not rebuilt here.

What it claims that the data does not support: missing records (row 1); tone frequencies (row 9); ripple
growing with speed (row 11); one or two steady3 events (row 12) and the after-levels built on them (row 13);
sums not steadier (row 14); "all radial channels drift down" without the magnet file (row 7).

## What it could not tell

From its own list: ripple length in mm (no rope speed in the record); the cause of the spread between sensing
elements; any reading on rope damage (no diameter, construction or travel on record); the logger's own share
of the noise (it gave no data-sheet figure); a list of features repeating at the same place in every pass (its
output for that was marked optional and not sent).

## What the loop could not give, compared with a free look at the raw files

The model never saw a trace, so it could not notice what a first plot shows at once: that one record in a
hundred is lost by its parser, that steady3 holds three events and not one, that the last event leaves the
axial levels shifted. Each such slip spreads to every figure downstream (the 1 % shift in every frequency, the
event levels), and the model then reads its own outputs as fact; in round 2 it flagged none of them, although
the brief asked it to say when an output looked wrong. The loop also cut what it could read: its outputs came to
399 279 bytes against the 250 000 asked for, so the steady-mean table (20 686 bytes) did not fit the tool's
400 000-byte input; it worked round that from another table. And it chose to ask for no third round, so no
second look at its methods happened. A free look would have caught the parsing and event-detection errors in
minutes; the loop gave a full set of tables, most of the basic statistics right, and most of the event and
method-dependent figures wrong.

## How it was run

Round 1: brief (`brief.md`) of 14 676 bytes as sent, answered in 489 s with three scripts. The model quoted
the brief's last line back word for word. All three scripts were read before running: no network, no
subprocess, no shell, no deletion, reads only the data argument, writes only the output argument. One change
before running, recorded in `answers/scripts_round1/run_fix.diff`: `np.trapz` renamed to `np.trapezoid`
(removed from numpy 2.5). All three ran without error (4 s, 11 s, 2 s).
Round 2: brief (`brief_round2.md`) plus the round-1 brief, the three scripts, a run log and 27 output files,
398 497 bytes as sent; the two files marked optional were left out, and the tool's 400 000-byte limit left out
`steady_channel_means.csv`. The model quoted both the brief's last line and the last line of the last file,
so the whole input reached it. It asked for no further scripts, so its round-2 findings are final.
Model file: `models.yaml`. Raw data and the Python environment are not in the repository.

# The root box limits what is sent

Simulated throughout: every number below comes from the line beta's simulator and its settings, not from a real
head. Nothing here is selected; the parts are options, side by side, each its own setting, all off by default.

## In short

The owner's direction: no powerful machine at each winch; the root box does simple things that limit what is sent;
heavier analysis sits after it; everything settable in the root box and in the twin. No data is to be lost, and
there may be more noise than converter jitter.

1. The root box can tell when the rope moves from the SWS's own data (the strand ripple), with 5 integer
   operations per channel and sample. In the simulator it found all 36 starts tried, 1.1 s after the ramp began,
   and made no false start in 4.5 hours of distinct rest data (both halves watched), with noise, hum and drift
   raised up to 20 times.
2. On the large installation the machine's movement signal can do the same job, alone or together with the data.
3. A ring memory in the box keeps the last 20 s of frames (about 0.5 MB for 2 halves, 1 MB for 4), so a run is sent
   from a little before the movement starts.
4. At rest the box can send everything (as today), send it through a dead band, or hold it back and send only a
   keep-alive frame every 10 s plus a marker that says "held at rest, nothing sent".
5. A dead band loses data by its nature: what changes less than its width is not sent. Used only at rest, every
   sample of a run still arrives bit for bit (a test proves it).
6. Compression without loss shrinks a frame 1.2 to 1.6 times at the simulator's own noise; the mains hum is what
   keeps it from shrinking more.
7. Large installation, bytes per day: 218 GB today; 49 GB when the rest is held back; 31-42 GB when the rest is
   held back and the runs are compressed (two runs a day assumed).
8. First installation: 12.8 GB today; 2.9 GB held at rest; 1.8-2.5 GB held at rest and compressed.
9. The logger rebuilds the record from what it gets. The marker tells it which frames were held at rest, so that
   gap is never taken for lost data, and the count of lost frames still works (tested with dropped frames and a
   network stop during a run).
10. In the simulator the noise at rest, at the line rate, is almost all mains hum (14 µT rms), not converter noise
    (under 0.5 µT).

## The options side by side

Per day, two runs (5.25 h sent with pre-roll and post-roll) and 18.75 h at rest, noise as in the simulator (1×).
"Large" = 204 halves, "first" = 12 halves. Compression figures for delta_varint / delta_rice / zlib.

| Option | What is sent | What is lost | Work in the box | Large, GB/day | First, GB/day |
|---|---|---|---|---|---|
| Today | every frame | nothing | — | 218.2 | 12.84 |
| Compression only | every frame, coded | nothing | 11 / about 6 + k operations per value; zlib much more | 151.4 / 134.6 / 187.7 | 8.91 / 7.92 / 11.04 |
| Dead band at rest, compression always (the option in the brief) | runs whole; rest through the dead band | at rest, every change smaller than the width (3 × rest noise: 42 µT radial, 46.5 µT axial) | + 4 operations per value | 102.7 / 66.0 / 65.1 | 6.04 / 3.88 / 3.83 |
| Rest held back, keep-alive every 10 s | runs whole; at rest one frame in 100 plus a marker | at rest 99 % of the samples; a run the detector misses | + ring memory 0.5-1 MB | 49.45 | 2.91 |
| Rest held back, runs compressed | the same, coded | the same | both | 34.3 / 30.5 / 42.5 | 2.02 / 1.80 / 2.50 |
| Dead band always | everything through the dead band | every change smaller than the width, in runs too (ripple detail, small wire signals) | + 4 operations per value | not worked out | not worked out |

An option put forward in the brief, shown here as one row among the others and not as a ruling: a dead band only
while the rope stands still, and everything sent, compressed without loss, during a run. It is the third row.

Checked on the whole line (`tables/reduction_pipeline.json`: one 20 m lift at 3.2 m/min after 600 s at rest, in
process): bytes published against today: rest held 0.574; rest held + delta_varint 0.400; rest held + zlib 0.493;
dead band at rest (3×) + delta_varint 0.577; everything sent + delta_varint 0.696; the machine's signal, rest held +
delta_varint 0.395. Ring only (rest sent) 1.000. No frame lost in any of them (box 0, logger 0); 12 294 frames held
at rest (12 473 with the machine's signal). The rest share here is short (600 s), so these are not the day figures.

## The settings

All under `[reduction]` in `settings.toml`; each can be set for one run with `run_beta.py --set reduction.<name>=<value>`.

| Name | Unit | Default | Range or choices | What it does |
|---|---|---|---|---|
| `enabled` | — | false | true / false | master switch; false = every frame sent unchanged, as before |
| `detector` | — | data | off / data / external / either | what says "moving" |
| `detect_mains_Hz` | Hz | 50 | 50, 60 | running sum over one mains period (M = 250 / 50 = 5 samples) |
| `detect_lag_s` | s | 0.1 | 0.02-1 | difference over this lag (D = 25 samples) |
| `detect_window_s` | s | 0.5 | 0.1-2 | activity summed over this window |
| `detect_threshold_uT` | µT | 10 | 1-100 | mean absolute lag difference per channel that counts as moving |
| `detect_combine` | — | median | median / max / mean | over the 16 channels of a half |
| `detect_min_duration_s` | s | 1 | 0.5-5 | above for this long = moving |
| `detect_hold_off_s` | s | 10 | 1-60 | below for this long = stopped |
| `external_delay_s` | s | 0 | 0-5 | delay of the machine's movement signal |
| `pre_roll_s` | s | 20 | 0-120 | ring memory: every frame waits this long in the box |
| `post_roll_s` | s | 10 | 0-120 | sent as running this long after the stop decision |
| `rest` | — | send | send / hold | frames at rest |
| `keepalive_s` | s | 10 | 1-600 | at rest, one frame sent unchanged this often |
| `dead_band` | — | off | off / at_rest / always | per channel |
| `dead_band_counts` | counts | 0 | 0-10 000 | width; the larger of this and the next |
| `dead_band_x_rest_noise` | × rest noise | 0 | 0-10 | width in multiples of `rest_noise_uT` |
| `rest_noise_uT` | µT rms | [14.0, 15.5] | — | rest noise at the line rate [radial, axial]; from the simulator, to be replaced by a measured one |
| `compression` | — | off | off / delta_varint / delta_rice / zlib / delta_varint_zlib | on every frame sent |
| `zlib_level` | — | 6 | 1-9 | for zlib |
| `study_noise_factors` | × | [1, 5, 20] | — | study only: element noise, hum and drift raised by these |
| `day_runs`, `day_rest_h` | —, h | 2, 18.75 | 0-9, 0-24 | study only: runs per day and hours at rest (assumed) |
| `halves_large`, `halves_first` | — | 204, 12 | — | given: 3 × 17 winches × 2 SWS × 2 halves; 6 SWS × 2 halves |

## 1. Movement from the SWS's own data

Per half, on the 250-per-second values the box already receives, integers only, per channel and sample:
running sum over one mains period (M = 250 / 50 = 5 samples: one add, one subtract; it nulls 50 Hz and its
harmonics), difference to the running sum 0.1 s earlier (D = 25 samples: one subtract; it removes the standing level,
drift and slow temperature change and passes the ripple), absolute value and sum (two). That is 5 operations; at the
end of each 0.5 s window one scaling per channel and a median of 16. For a box with 4 halves:
5 × 16 channels × 250 per s × 4 halves = 80 000 operations per second. Memory M + D = 30 values per channel.
The box moves when either of its halves moves (or, by setting, the machine's signal says so). The first frame after
a half boots is skipped: the half's filter settles from zero in it, a step of the whole standing field.

Measured on simulated lifts (20 m travel, 30 min at rest before, out and back, both halves, 3 seeds, 3.2 and 5 m/min;
36 starts per threshold; `tables/reduction_study.json`):

| Noise, hum and drift × | Activity at rest, median / largest (µT) | Activity running, smallest (µT) | False starts at rest (1.5 h distinct) | Missed starts | Delay from the start of the ramp |
|---|---|---|---|---|---|
| 1 | 0.23 / 0.27 | 86 (3.2 m/min), 144 (5 m/min) | 0 | 0 | 1.1 s |
| 5 | 0.93 / 1.10 | 86, 144 | 0 | 0 | 1.1 s |
| 20 | 3.69 / 4.36 | 86, 143 | 0 | 0 | 1.1 s |

Time at rest per factor: 3 seeds × 1 800 s = 1.5 h of distinct data (the two speeds share the same rest, so the
6 cases hold 3 h but only 1.5 h of it differs), both halves watched; 4.5 h over the three factors, which reuse the
same seeds at a larger scale. Thresholds 5, 10 and 20 µT gave the same result (delay 1.1 s); 50 µT gave 1.6 s; none gave a false start
or a missed start. The delay is set by the window (0.5 s) and the minimum duration (1 s), not by the noise. The
largest rest value excludes the first 2 s of data: the very first window after start-up is about 10 times higher
(2.3 µT at 1×, 45-56 µT at 20×) because the history starts from one sample; it lasts one window, below the
minimum duration of two windows, so it made no false start; with `detect_min_duration_s` = 0.5 s it would at 20×.

## 2. The ring memory and the pre-roll

Every frame waits `pre_roll_s` in the box before it leaves. When movement is found, every frame still in the ring
from up to `pre_roll_s` before that moment is sent as part of the run; after the stop decision (hold-off 10 s), frames
for `post_roll_s` more. The cost is the memory and a delay: every frame reaches the logger `pre_roll_s` later.

Memory, bytes = halves × channels × rate × bytes × seconds:

| Halves | Pre-roll | Samples | As frames (1 229 B, 10 per s) |
|---|---|---|---|
| 2 | 20 s | 2 × 16 × 250 × 3 × 20 = 480 000 B | 2 × 1 229 × 10 × 20 = 491 600 B |
| 4 | 20 s | 4 × 16 × 250 × 3 × 20 = 960 000 B | 4 × 1 229 × 10 × 20 = 983 200 B |
| 2 / 4 | 60 s | 1 440 000 / 2 880 000 B | 1 474 800 / 2 949 600 B |

What pre-roll makes a missed first metre impossible: with the measured delay of 1.1 s, any pre-roll above 1.1 s
keeps the start. To keep the first metre even if the detector were a whole metre late:
at 3.2 m/min = 53.33 mm/s, the 1 s ramp covers 53.33 × 1 / 2 = 26.7 mm, the rest of the metre 973.3 / 53.33 =
18.25 s, total 19.25 s; at 5 m/min = 83.33 mm/s, the ramp covers 41.7 mm, the rest 958.3 / 83.33 = 11.50 s, total
12.50 s. The default 20 s covers both.

## 3. Dead band

Per channel: a value within the width of the last value sent on that channel is replaced by that value (held). The
width is `dead_band_counts` or `dead_band_x_rest_noise` × `rest_noise_uT` (in counts: radial 23.07 counts per µT,
axial 230.7), whichever is larger. 4 operations per value. A frame that went through the dead band carries quality
bit 0x08; the box checks the half's CRC on arrival and writes a new one after the dead band.

| Mode | What is sent | What is lost |
|---|---|---|
| off | every value | nothing |
| at_rest | runs unchanged; at rest the held values | at rest, every change smaller than the width |
| always | the held values, also in runs | every change smaller than the width, in runs too |

Test (`test_dead_band_at_rest_only_keeps_every_run_sample_bit_for_bit`): the same lift with and without the dead band
at rest (3 × rest noise) and compression; every frame of the run (over 4 000, both halves) arrives byte for byte the same,
none flagged; at rest every value stays within the width of the original.

At rest in the simulator (30 s at rest, 1×): 1 × rest noise replaces 49 % of the values, 3 × replaces 96 %. The width
in multiples of "rest noise" is in practice a width in multiples of the hum, since the hum is most of it.
A keep-alive frame (unchanged) goes every `keepalive_s` also in this mode, and the dead band starts again from it.

## 4. Compression without loss

Applied to each frame the box sends; every frame decodes on its own (a lost frame never spoils the next). The 25-byte
header and the CRC are kept as they are. Message 0x21 = type, scheme, body, stamp.

- **delta_varint**: per channel the difference to the previous sample (the first against zero), zigzag, 7 bits per
  byte. About 11 integer operations per value.
- **delta_rice**: the same differences, Rice code with one parameter k per channel and frame (from the mean). About
  6 + k operations per value.
- **zlib**: the standard library's deflate on the frame; tens of operations per byte, about 256 kB working memory.
- **delta_varint_zlib**: the two in a row.

Ratio (frame bytes / coded bytes), 30 s each, at noise, hum and drift × 1 / 5 / 20; running and at rest gave the same
figures to within 0.03, because the sample-to-sample change is set by the hum, not by the ripple:

| Scheme | × 1 | × 5 | × 20 | × 1, hum off, running / rest |
|---|---|---|---|---|
| delta_varint | 1.45 | 1.23 | 1.10 | 1.50 / 2.15 |
| delta_rice | 1.63-1.64 | 1.43 | 1.30 | 1.91 / 2.47 |
| zlib | 1.17-1.20 | 1.17 | 1.11 | 1.17 / 1.33 |
| delta_varint_zlib | 1.43 | 1.24 | 1.12 | 1.61 / 2.20 |

After a dead band at rest of 3 × rest noise (× 1): delta_varint 2.48, delta_rice 4.83, zlib 7.50, delta_varint_zlib
7.54 (held values repeat, which suits zlib). Every scheme gave the same bytes back for every frame tried
(tests: random, full-scale jumps and simulated frames). Time on this PC per sample of 16 channels: zlib (C library)
1.8 µs; delta_varint in Python with numpy 2.6 µs (not a measure for a small processor; the operation counts above
are).

## 5. Bytes per day

Message today: 1 229-byte frame + 9 stamp = 1 238 B, 10 per s per half. Compressed message: body + 2 type bytes +
9 stamp = body + 11. Marker: 6 + 8 per range + 9 stamp = 23 B for one range, one per keep-alive interval.
Run time sent: one run at 3.2 m/min is out 4 688.5 s + 30 s at the far end + back 4 688.5 s = 9 407 s, plus pre-roll
20, hold-off 10, post-roll 10 = 9 447 s = 2.624 h; two runs 5.248 h; the rest of the day 18.75 h. Both settable
(`day_runs`, `day_rest_h`).

Large installation (204 halves):
- today: 204 × 1 238 × 10 × 86 400 = 218.2 GB
- rest held: 204 × (5.248 × 3 600 × 1 238 × 10 + 18.75 × 3 600 × 0.1 × (1 238 + 23)) = 49.45 GB
- rest held + delta_varint: 204 × (5.248 × 3 600 × (1 229 / 1.45 + 11) × 10 + 18.75 × 3 600 × 0.1 × (1 229 / 1.45
  + 11 + 23)) = 34.3 GB; + delta_rice (1.63 running, 1.64 at rest) 30.5 GB; + zlib (1.17 running, 1.20 at
  rest) 42.5 GB
- dead band at rest 3× + compression always: 204 × (5.248 × 3 600 × (1 229 / 1.45 + 11) × 10 + 18.75 × 3 600 ×
  (1 229 / 2.48 + 11) × 10) = 102.7 GB (delta_varint); delta_rice 66.0 GB; zlib 65.1 GB
- everything sent, compression only: 151.4 / 134.6 / 187.7 GB

First installation (12 halves): the same lines × 12 / 204: 12.84 GB today; 2.91 held at rest; 2.02 / 1.80 / 2.50
held at rest and compressed; 6.04 / 3.88 / 3.83 with the dead band at rest; 8.91 / 7.92 / 11.04 compression only.
Every line with its arithmetic is in `tables/reduction_study.json` (`per_day`).

## 6. What the logger does with it

- A compressed frame (0x21) is decompressed on arrival and stored exactly as a plain frame is: the run files keep
  the open format and hold the half's own bytes.
- A rest marker (0x23) lists, per half, the half's boot count, the samples per frame and ranges of first-sample
  indices of the frames the box received and held. The logger enters those frames into the half's sample order as
  "held at rest": the gap they leave is not counted as lost, and they are counted on their own
  (`rest_held_frames`, `rest_spans` in `session.json`); a marker delivered twice is counted once. The box counts
  markers apart from frames (`published_markers`).
- A frame the box never received (lost on the serial line at rest) is not in the marker's ranges, so the logger
  counts it as lost, exactly as before. The box counts it too.
- The marker always goes before the next frame the box sends on that half (keep-alive or run), so the logger knows
  within `keepalive_s` whether a gap is "held at rest" or "lost". The marker ends with the stamp, so the box's
  disk buffer and back-fill flag work for it unchanged.
- Rebuilding the full record: the stored frames, plus the rest spans (nothing there but the keep-alive frames, one
  every 10 s), plus for frames flagged 0x08 the knowledge that each value lies within the stated width of the true
  value. The logger's own run finding, position and drift worked on a run sent this way (`run_beta.py`, 20 m, two
  lifts, rest held, delta_varint: position after registration rms 10.6 mm, drift 19.81 of 20 µT/h put in).
- Tested (`test_hold_at_rest_with_drops_and_network_stop_counts_every_loss`): rest held, compression on, three
  frames dropped during the run and one at rest, a 60 s network stop during the run: 4 put in = 4 counted by the box =
  4 by the logger; frames at the logger + held at rest + lost = frames produced; every run frame that was not dropped
  arrives byte for byte.

## What each option loses

- **Ring memory**: nothing; every frame reaches the logger `pre_roll_s` later (20 s by default).
- **Rest held back**: the samples at rest between keep-alive frames (99 % of them at 10 s), so anything that happens
  at rest is seen only at keep-alive resolution; a run the detector misses entirely (none missed in the simulator;
  the machine's signal, where there is one, is a second source).
- **Dead band**: every change smaller than the width, at rest only or always; with "always" this includes run
  detail such as small wire signals under the width.
- **Compression**: nothing; it costs processor work in the box and a decoder at the logger.
- **A false start**: nothing lost, only more sent.

## Open, for the owner

1. On the large installation, can the machine's movement signal be wired to the root box, and how long before the
   rope moves does it come?
2. How many runs a day and how many hours at rest on each installation? The day figures rest on 2 runs and 18.75 h.
3. Is anything at rest of interest beyond one frame every 10 s (temperature, handling during maintenance)?
4. Is a delay of 20 s (the pre-roll) from head to logger acceptable for what is shown live?
5. Must the stored or forwarded format be one a commercial logging system reads, or may the logger decode?
6. A recording at rest on site (hum and noise at the line rate) to replace `rest_noise_uT`.

## Files

`linebeta/reduction.py` (the box's part and the logger's unpacking), `tests/test_reduction.py`, `study_reduction.py`
(all numbers here; `tables/reduction_study.json`, `tables/reduction_pipeline.json`). Hooks: one marked block each in
`linebeta/pipeline.py` (switches the box over when enabled), `linebeta/logger.py` (unpacks compressed frames and
markers), `settings.toml` (`[reduction]`) and `README.md`. `linebeta/root_box.py` is not changed: the reducing box is
a subclass that receives, checks, counts and stamps with the same code.

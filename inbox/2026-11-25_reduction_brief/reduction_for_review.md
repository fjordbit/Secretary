# The root box: how it limits what it sends, for review from the measurement side

Nothing here is selected. Each step is an option with its own settings, all off by default. Numbers marked
"simulated" come from the simulator of the data line; numbers marked "measured" come from the prototype recording
(two loggers, 100 readings per second, 15 files).

## In short

The root box is the small box at each winch. It receives the data from the halves of the SWS heads on that winch
and sends it on to the logger, which stores it. The direction given for its design:

- no powerful machine at each winch: the root box only does simple steps that limit what is sent;
- no data is to be lost; the noise on site may be larger than the converters' own noise (hum, vibration, handling);
- every step is a setting, in the root box and the same in the digital twin.

The three steps, each can be switched on alone or with the others:

1. **Dead band.** A channel's new value that differs from the last value sent by less than a set width is replaced
   by that last value. It removes noise-sized changes, and by its nature it loses them.
2. **Compression without loss.** Each frame is packed smaller before it is sent and unpacked by the logger to the
   very same bytes.
3. **Memory, and sending only around movement.** Every frame waits 20 s in the box. When the rope starts to move,
   the frames from up to 20 s before are still there and go out as part of the run; after the stop, 10 s more. At
   rest the box can send everything as today, send it through the dead band, or hold it back and send one frame
   every 10 s plus a marker that says "held at rest, nothing sent".

One proposal, shown as one option among the others and not ruled: **a dead band only while the rope stands still,
and everything sent, compressed without loss, during a run.**

Runs without an encoder: the box finds movement in the SWS's own data. When the rope moves, the strands make a
regular ripple on every channel, and the box watches for it. On the large installation a movement signal from the
machine is available and may start the logging as well; the data detector runs beside it. The first installation
has no such signal.

**Tried on your recording, settings unchanged** (measured):

- it found all 20 passes in run1-run10, and said "moving" 1.3-2.2 s after the pass began (the pass finder is a
  separate, simple measure of the ripple, section 4a; on the slow manual ramps of run10 the detector was earlier);
- it never started at quiet rest: 106 minutes in steady1 and steady2, plus the still parts of run1-run9;
- it did start when a magnet came near (steady3), on three of the eight pushes off centre (steady4) and when the
  rope was shaken (steady5): that sends more, it loses nothing;
- the 20 s memory is about nine times the largest delay seen (2.2 s).

The plan rests on things only a measurement can tell. **Six questions at the end ask you to confirm or correct it.**

| Option | What is sent | What it can lose | Simulated, large installation, GB per day |
|---|---|---|---|
| Today | every frame | nothing | 218.2 |
| Compression only | every frame, packed | nothing | 134.6-187.7 |
| Dead band at rest, compression always (the proposal) | runs whole; rest through the dead band | at rest, changes under the width | 65.1-102.7 |
| Rest held back, one frame every 10 s | runs whole; at rest 1 frame in 100 and a marker | at rest 99 % of the samples; a run the detector misses | 49.45 |
| Rest held back, runs compressed | the same, packed | the same | 30.5-42.5 |
| Dead band always | everything through the dead band | changes under the width, in runs too | not worked out |

The GB figures assume two runs a day, 18.75 h at rest, the simulator's noise and a dead band 3 x the simulated rest noise wide; a range gives the figure for each compression scheme, not an uncertainty; their arithmetic is in
`root_box_reduction.md` (section 5). Large installation = 3 main stations x 17 winches = 51 winches = 102 SWS = 204
halves.

---

## How to read the step-by-step parts

Each step below is written as numbered plain steps. "If ... then ..." means: do the second part only when the first
part is true. A **channel** is one sensing element's signal. A **frame** is what a half sends every 0.1 s: for each
of its 16 channels (8 radial, 8 axial), 25 values at 250 values per second. A **count** is one step of the converter;
in the product, 1 µT is 23.07 counts on a radial channel and 230.7 counts on an axial channel (simulator settings;
see Terms).

<a id="deadband"></a>
## 1. Dead band

**In one sentence:** a new value that lies within the width of the last value sent on that channel is replaced by
that last value, so noise-sized changes stop changing what is sent.

**Step by step**, for one channel. Names: *value* = the newest reading; *kept value* = the last value sent on this
channel; *width* = the dead band width in counts.

1. If there is no kept value yet, then the first value becomes the kept value.
2. For each new value: if the difference between the value and the kept value, ignoring its sign, is at most the
   width, then send the kept value instead of the value.
3. Otherwise send the value, and it becomes the new kept value.
4. A frame that went through these steps carries a mark saying so; if any value in it changed, the box writes a new check sum for it.
5. When it is used, by the mode: *off* = never; *at_rest* = only on frames the box counts as "at rest", only
   when frames at rest are sent, and never on a keep-alive frame (sent unchanged); *always* = also during runs.
6. During a run (modes off and at_rest) the kept value is forgotten, so the dead band starts again after the run.
   A keep-alive frame (step 3, item 5) sets the kept value to that frame's last values.

Width in counts = the larger of `dead_band_counts` and `dead_band_x_rest_noise` x `rest_noise_uT` x counts per µT,
rounded down.

**Worked example.** Width 3 x rest noise on a radial channel: 3 x 14 µT x 23.07 counts per µT = 968.9, rounded down
to 968 counts (42 µT). Kept value 1000. New values 1300, 600, 2100, 2050, 1200:

| New value | Difference to kept value | Within 968? | Sent | Kept value after |
|---|---|---|---|---|
| 1300 | 300 | yes | 1000 | 1000 |
| 600 | 400 | yes | 1000 | 1000 |
| 2100 | 1100 | no | 2100 | 2100 |
| 2050 | 50 | yes | 2100 | 2100 |
| 1200 | 900 | yes | 2100 | 2100 |

**What it can lose:** every change smaller than the width. The last row shows how much: a drop of 900 counts is
not sent. Used only at rest, every value of a run still arrives bit for bit (a test in the simulator proves it).

**Settings**

| Name | Unit | Default | What it does |
|---|---|---|---|
| `dead_band` | — | off | off / at_rest / always |
| `dead_band_counts` | counts | 0 | width in counts |
| `dead_band_x_rest_noise` | x rest noise | 0 | width in multiples of the rest noise |
| `rest_noise_uT` | µT rms | 14.0 radial, 15.5 axial | rest noise; from the simulator, to be replaced by a measured figure |

<a id="compression"></a>
## 2. Compression without loss

**In one sentence:** instead of each value, the box sends how much it changed since the value before, in as few
bytes as that change needs, and the logger adds the changes up again to get the very same values.

**Step by step** (the scheme `delta_varint`). Names: *difference* = this value minus the value before it on the
same channel; *code number* = the difference turned into a number that is never negative.

1. Keep the frame's header (25 bytes) and its check sum (4 bytes) as they are.
2. Go through the frame one sample time after the other, and within each, channel 1 to 16.
3. Difference = this value minus the previous value of the same channel in this frame. For the first value of each
   channel in the frame there is no previous one: the difference is the value itself. (So each frame can be unpacked on its own,
   and a lost frame never spoils the next.)
4. Code number: if the difference is zero or positive, then twice the difference; if it is negative, then twice its
   size minus one. (0 becomes 0, −1 becomes 1, +1 becomes 2, −2 becomes 3, +2 becomes 4, and so on.)
5. Write the code number 7 bits at a time, smallest part first, one byte for each 7 bits; the eighth bit of a byte is
   1 when another byte of the same number follows, 0 on its last byte.
6. The logger does it backwards: reads the bytes into code numbers, turns them back into differences, adds them up
   channel by channel, and puts header and check sum around them. The result is the frame, byte for byte.

**Worked example.** One channel, four values in counts: 5000, 5003, 4998, 5001.
Differences: 5000 (the first, against zero), +3, −5, +3. Code numbers: 10000, 6, 9, 6.
Bytes: 10000 needs two bytes (14 bits), 6, 9 and 6 one byte each: 5 bytes instead of 4 x 3 = 12.

Other schemes, each a setting: `delta_rice` (the same differences, packed bit by bit with one size parameter per
channel and frame), `zlib` (the general packer of the standard library), `delta_varint_zlib` (the two in a row).

**What it can lose:** nothing. It costs work in the box (about 11 simple operations per value for `delta_varint`) and
an unpacker at the logger. Simulated: frames shrink 1.17 to 1.64 times at the simulator's own noise; the mains hum
in the simulator is what keeps it from shrinking more (`root_box_reduction.md`, section 4).

**Settings**

| Name | Unit | Default | What it does |
|---|---|---|---|
| `compression` | — | off | off / delta_varint / delta_rice / zlib / delta_varint_zlib |
| `zlib_level` | — | 6 | 1-9, for the two zlib schemes |

<a id="memory"></a>
## 3. Memory, and sending only around movement

**In one sentence:** every frame waits a set time in the box, so that when movement is found the frames from just
before it are still there and can be sent as part of the run.

**Step by step**, for each frame that arrives. Names: *pre-roll* = how long a frame waits in the box (20 s); *post-roll*
= how long after the stop frames are still sent as a run (10 s); *moving stretch* = the time from "moving" to
"stopped" as the detector (section 4) or the machine's signal says.

1. The frame is checked, counted and time-stamped as today. It is given to the detector (section 4), then put into
   the memory with its arrival time.
2. A frame leaves the memory when it has waited the pre-roll.
3. When it leaves: if its arrival time lies between (the start of a moving stretch minus the pre-roll) and (the end
   of that stretch plus the post-roll), then it belongs to a run. A stretch that has not ended yet has no end.
   (If the detector is switched off, every frame belongs to a run.)
4. If it belongs to a run: send it (through the dead band only in mode *always*).
5. If it is at rest, and at least `keepalive_s` (10 s) has passed since this half's last keep-alive frame: send it
   unchanged, marked "keep-alive".
6. Otherwise, if frames at rest are held (`rest` = hold): do not send it; write it in this half's list of held
   frames (its restart count, the number of its first sample, how many samples).
7. Otherwise (`rest` = send): send it, through the dead band if the mode is *at_rest* or *always*.
8. Before any frame of a half is sent, if that half's list of held frames is not empty, then a marker goes first:
   "held at rest, nothing sent", with the held frames as ranges of sample numbers. Then the list is emptied, and
   the frame is packed (if compression is on) and sent.

The marker is how the logger tells "at rest, nothing sent" from "data lost": a gap covered by a marker is held, a
gap not covered is lost and is counted as lost, as today (tested in the simulator with dropped frames and a network
stop during a run).

**Worked example.** Pre-roll 20 s, post-roll 10 s; the detector says "stopped" after 10 s below its threshold (the hold-off, section 4). The rope starts at 100.0 s; on your recording the
detector said "moving" at most 2.2 s after the pass finder's start (section 4a), so at 102.2 s. Frames that arrived from 102.2 − 20 = 82.2 s on are sent as
the run: 17.8 s of standing still before the start are included. The rope stops at 400.0 s; the detector says
"stopped" after 10 s below its threshold, at about 410 s; frames up to 410 + 10 = 420 s are sent as the run.

Memory needed in the box, bytes = halves x channels x values per second x bytes per value x seconds:
2 halves x 16 x 250 x 3 x 20 = 480 000 bytes; 4 halves: 960 000 bytes.

**What it can lose:** the memory itself loses nothing; every frame reaches the logger 20 s later. With `rest` = hold:
the values at rest between keep-alive frames (at 10 frames per second and one kept every 10 s, 99 of every 100
frames), and a whole run if the detector and the machine's signal both miss it.

**Settings**

| Name | Unit | Default | What it does |
|---|---|---|---|
| `enabled` | — | false | master switch; false = every frame sent unchanged, as today |
| `pre_roll_s` | s | 20 | how long every frame waits in the box |
| `post_roll_s` | s | 10 | sent as a run this long after "stopped" |
| `rest` | — | send | send / hold: frames at rest |
| `keepalive_s` | s | 10 | at rest, one frame sent unchanged this often |

<a id="noencoder"></a>
## 4. Runs without an encoder

**In one sentence:** the box looks at how much each channel changes over a tenth of a second, after averaging out
the mains hum; when the strands pass, that change is large on every channel, at rest it is small.

**Step by step**, for one half. Names: *M* = the number of values in one mains period (values per second ÷ mains
frequency: 250 ÷ 50 = 5); *D* = the number of values in 0.1 s (25); *W* = the number of values in one window of
0.5 s (125); *activity* = the average change, in µT.

For each channel and each new value:

1. Running sum: add the new value to the sum of the last M values and take away the value that drops out. (A sum
   over exactly one mains period cancels the hum.)
2. Change: this running sum minus the running sum D values ago, ignoring its sign. (The standing level and slow
   drift cancel; the strand ripple does not.)
3. Add the change to the channel's window total.

After every W values (every 0.5 s):

4. Activity of each channel = window total ÷ (W x M) ÷ counts per µT.
5. Activity of the half = the middle value (median) of its channels' activities.
6. If the activity is above the threshold (10 µT): count one more window above, and set the count of windows below
   to zero. If the half is not yet moving and the windows above add up to `detect_min_duration_s` (1 s = 2 windows),
   then the half is moving.
7. Otherwise: count one more window below, and set the count of windows above to zero. If the half is moving and
   the windows below add up to `detect_hold_off_s` (10 s = 20 windows), then the half has stopped.
8. Set the window totals back to zero.

At the very start there is no history yet: the last M values are all taken to be the first value, and the running
sums D values ago all to be the first running sum, so the start itself makes no change.

The box is moving when any of its halves is moving. The first frame after a half restarts is not used (the half's
filter settles in it). Work: 5 simple whole-number operations per channel and value; for a box with 4 halves
5 x 16 x 250 x 4 = 80 000 per second.

**Worked example** (half B, measured on run1, one window every 0.5 s): at rest 1.5, 1.7, 1.3 µT; the pass begins;
then 54.5, 108.1, 90.5 µT. The window of 54.5 is the first above 10 µT; after the next one (2 windows = 1 s above)
the half is moving. At the end of the pass: 70.5, 15.1, 8.8, 7.2, 5.5 µT: from 8.8 on the windows are below; after
20 of them (10 s) the half would be stopped (this file ends 9.3 s after the pass, just before that).

**The machine's movement signal.** On the large installation the machine can give a "moving" signal. Setting
`detector`: *data* (the SWS's own data only; the first installation has no machine signal), *external* (the
machine's signal only), *either* (moving when either says so). With *either*, the machine's signal may start the
logging, and the data detector runs beside it and catches a run the signal misses.

**Settings**

| Name | Unit | Default | What it does |
|---|---|---|---|
| `detector` | — | data | off / data / external / either |
| `detect_mains_Hz` | Hz | 50 | mains frequency; sets M |
| `detect_lag_s` | s | 0.1 | the lag; sets D |
| `detect_window_s` | s | 0.5 | the window; sets W |
| `detect_threshold_uT` | µT | 10 | activity above this counts |
| `detect_combine` | — | median | median / max / mean over the channels |
| `detect_min_duration_s` | s | 1 | above this long = moving |
| `detect_hold_off_s` | s | 10 | below this long = stopped |
| `external_delay_s` | s | 0 | delay of the machine's signal |

<a id="measured"></a>
### 4a. The detector on your recording

The detector was run unchanged on all 15 files, settings at their defaults; only the input was adapted (100
readings per second, mV/V, 12 channels per logger; conversion in the details below). Five ways of grouping the
channels were tried: each half as the product has it (side B: its 6 radial and 6 axial channels; side A the same),
the box (moving when either half is), and each logger on its own (12 radial, 12 axial).

When the rope really moved was taken from the ripple itself, by a separate and simple measure: the radial channels
filtered to 0.5-10 Hz, and "moving" where their combined size is above 10 times its size in the first 2 s of the
file (the pass finder of the recording's own analysis). It finds 20 passes: one each in run1-run8, eight in run9,
four in run10. In the steady files the head does not travel, so every start there counts as a false start.

| Measured, default settings | Half B | Half A | Box | Radial only | Axial only |
|---|---|---|---|---|---|
| Passes found, of 20 | 20 | 20 | 20 | 20 | 20 |
| Said "moving" after the pass began, run1-run9 (s) | 1.28-2.20 | 1.28-2.20 | 1.28-2.20 | 0.84-2.20 | 1.28-2.20 |
| The first window above the threshold began (s) | 0.28-1.20 | 0.28-1.20 | 0.28-1.20 | −0.16-1.20 | 0.28-1.20 |
| run10, slow manual ramp (s; negative = before the pass finder) | −1.87 | −0.37 | −1.87 | −2.42 | −0.37 |
| False starts at quiet rest | 0 | 0 | 0 | 0 | 0 |
| Largest activity at quiet rest (µT) | 3.78 | 5.26 | — | 9.77 | 2.98 |
| Smallest activity in the middle of a pass, run1-run9 (µT) | 43.8 | 32.2 | — | 193.6 | 17.5 |

Quiet rest = steady1 (9.7 min) and steady2 (96.5 min) whole, and run1-run9 outside 3 s around each pass. run10 is
left out of the rest and pass figures: its manual ramps make the stretches between passes neither rest nor run.

- **Stops.** "Stopped" comes 10 s (the hold-off) after the activity falls below the threshold. Where a file goes on
  long enough after the last pass, it came 9.15-10.30 s after the pass ended (5 cases, logger groupings; the 10.30 s is run1 on the axial logger, whose own file runs on past the shared time stamps); in the
  other files the recording ends 2.3-9.8 s after the pass, before the hold-off runs out.
- **Back and forth.** The eight passes of run9 (stops of 0.3-1.2 s between them) and the four of run10 (stops of
  5.1-7.1 s) each make one moving stretch, since every stop is shorter than the hold-off.
- **Handling at rest** (the box): the magnet in steady3 made 5 starts, 98.0 of 149.2 s counted as moving; the pushes
  off centre in steady4 made 3 starts (pushes 4, 5 and 8 of 8), 70.0 of 166.5 s; the shaking in steady5 made 2
  starts, 109.5 of 175.9 s. With the memory, each such start also sends the 20 s before it and 10 s after it.
- **Margin.** A threshold works where it lies above the largest activity at rest and below the smallest activity in
  a pass. For a half: 5.26 to 32.2 µT (32.2 ÷ 5.26 = 6.1 times). For the radial channels alone, 10 µT sits only
  just above the rest value of 9.77 µT: the seven radial channels that are 5-13 times noisier than the others are
  more than half of the twelve, so they set the middle value. For the axial channels alone: 2.98 to 17.5 µT.

**Changed settings, listed** (one change, to show the cost): `detect_threshold_uT` = 20.
Halves and box: still 20 of 20 passes, the same delays in run1-run9, no false start at quiet rest; handling starts
in the box: steady3 4 (70.0 s), steady4 3 (32.0 s), steady5 2 (108.5 s). Radial alone: the margin at rest becomes
20 ÷ 9.77 = 2.0 times. Axial alone: the activity in run10 falls under 20 µT at times (smallest 17.5 µT in
run1-run9); it said "moving" 8.13 s after the first pass of run10 began and twice said "stopped" in the middle of a
pass for 1.5 s and 3.5 s. With a pre-roll of 20 s and a post-roll of 10 s none of this loses a frame (8.13 < 20;
1.5 and 3.5 < 10 + 20), but it shows that 20 µT is too close for the axial channels alone.

**What pre-roll keeps the start on the rig.** The largest delay seen, counted from the pass finder's start, was 2.2 s (8.13 s in the one changed
case). Any pre-roll above that keeps the start. On the rig, 2.2 s is 2.2 x 1.5536 = 3.4 ripple cycles at the
speed of run1-run6, and 2.2 x 2.0065 = 4.4 at the speed of run7-run8 (ripple frequencies from the recording's own
analysis, `prototype_data/analysis_a/prototype_data_a.md`, section 4, "Strand ripple"). If the delay in seconds is the same on the installation (not shown: other head, rope and speed): at
3.2 m/min = 53.33 mm/s, 2.2 s is 117 mm of rope; at 5 m/min = 83.33 mm/s, 183 mm. The 20 s default is 20 ÷ 2.2 =
9.1 times the largest delay seen at default settings.

Figures: `measured_check/figures/fig1_detector_run1` (activity through one pass) and
`measured_check/figures/fig2_detector_rest_steady2` (activity at rest over 97 minutes), each .html and .png.

<a id="confirm"></a>
## What we ask you to confirm

1. **Dead band at rest.** At rest your channels showed short slow excursions about every 110 s and a drift of 1-7 µT
   per hour on the axial channels. Is a dead band at rest of a few times the rest noise acceptable, or is any of
   that worth keeping in full?
2. **Pre-roll.** The detector said "moving" at most 2.2 s after the ripple began. Can the rope creep or ramp up more
   slowly than on the rig (as in run10) so that the first metre passes before the ripple shows, and is 20 s enough?
3. **What else moves the signal at rest.** A magnet near the head, pushing the head off centre and shaking the rope
   all started the detector. What else happens at rest on a winch (handling, tools, cranes, temperature, a
   neighbouring winch) that should, or should not, count as movement?
4. **The noisier radial channels.** Seven radial channels were 5-13 times noisier than the rest. Is that the parts,
   the wiring or the logger setup, and would you expect it in the product?
5. **Start and stop of a real run.** On the installation, how fast does the rope reach speed, and how long are the
   stops inside one run (at the far end, or back and forth)? The hold-off of 10 s joins stops shorter than that.
6. **The proposal.** Would you, from the measurement side, accept "dead band only at rest, everything sent during a
   run", or should something during a run also be thinned, or nothing at rest be held back?

---

## Details

**The adapter for the recording** (`measured_check/detector_on_recording.py`; the detector itself is the
simulator's, unchanged):

- Values to whole counts: count = mV/V x 1 000 000 (1 count = 0.000001 mV/V; the files carry 6-7 digits).
- Counts per µT from the data-sheet sensitivities on record (radial 3.4, axial 5.0 mV/V per mT): radial
  3.4 ÷ 1000 x 1 000 000 = 3 400 counts per µT; axial 5 000.
- The threshold of 10 µT in both units: radial 10 x 3.4 ÷ 1000 = 0.034 mV/V, axial 10 x 5.0 ÷ 1000 = 0.050 mV/V. As a
  window total: product radial 10 x W x M x 23.07 = 10 x 125 x 5 x 23.0687 = 144 179 counts (23.0687 = 23.07 unrounded); recording radial
  10 x 50 x 2 x 3 400 = 3 400 000 counts.
- 100 instead of 250 values per second; every time setting stays in seconds, so M = 100 ÷ 50 = 2 (50 Hz is the highest frequency that 100 readings per second
  can show), D = 0.1 x 100 = 10, W = 0.5 x 100 = 50 (product: 5, 25, 125).
  1 s above = 2 windows, 10 s below = 20 windows, as in the product.
- 12 channels per detector instead of 16 (6 radial + 6 axial per side; 12 of one kind per logger). The combine rule
  (median) is unchanged.
- Frames of 0.1 s = 10 readings, fed in order as the box would receive them. Half B and half A combine the two
  loggers on their shared time stamps (they agree to within about 0.05 s; recording analysis).
- The recording is not the product: other sensing elements, a logger instead of the product's converters and
  filter, a 40 mm rope, a prototype head. The activity figures say how this detector behaves on real noise and a
  real ripple, not what the product will read.

**Files.** `measured_check/detector_on_recording.py` (the run; `--set name=value` for a changed setting, `--tag` for
its name), `measured_check/reader.py` (reads the logger files), `measured_check/figures_detector.py` (the two
figures), `measured_check/tables/detector_measured.json` (every number above, per file and grouping, both passes).
The raw recording is not in the repository. The steps themselves: `linebeta/reduction.py`; the simulated study and
the day figures: `root_box_reduction.md`.

<a id="terms"></a>
## Terms

- **SWS**: the steel wire rope instrument; one **head** on the rope, made of two **halves**.
- **Sensing element (radial / axial)**: one element reading the field across / along the rope.
- **Channel**: one sensing element's signal.
- **Root box**: the box at each winch between the halves and the logger.
- **Logger**: here, where the data is stored after the root box; in "your recording", the two lab loggers.
- **Frame**: what a half sends every 0.1 s (header, 25 values per channel, check sum).
- **Count**: one step of the converter. Product (simulator settings): 23.07 counts per µT radial, 230.7 axial.
- **Strand ripple**: the near-sine wave the strands make on every channel while the rope moves.
- **Pre-roll / post-roll**: frames kept and sent from before the start / after the stop.
- **Keep-alive frame**: one frame sent unchanged at rest every `keepalive_s`, so drift and health stay visible.
- **Marker**: a short message "held at rest, nothing sent" with the held frames' sample numbers.
- **Dead band, width**: see section 1.
- **mV/V**: logger output in mV per V of bridge supply. **µT, mT**: micro- and millitesla. **rms**: root mean square.
- **Median**: the middle value when the values are put in order.

## Sources in the recording's own analysis

(`max/sws/prototype_data/analysis_a/prototype_data_a.md`, on its
own branch): ripple frequencies 1.5536 and 2.0065 Hz (section 4, "Strand ripple"); seven radial channels 5-13 times
noisier than the others (section 3 and "In plain words", item 4); slow excursions about every 110 s and axial drift
1-7 µT per hour (sections 3 and 2); the two loggers agree to within about 0.05 s (section 1).

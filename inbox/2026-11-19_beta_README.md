# The transmitter line as a running beta

## What it is, in five sentences

1. A program that runs the whole line on one PC: the rope and head simulator, the two halves of a head, the serial
   lines, the root box, a real MQTT broker on the PC itself, and the logger.
2. The simulator stands in for the rope and the 32 elements of a head; the half, the root box and the logger are
   written as the real code, and the root box is meant to run later on a small industrial computer.
3. One lift is the rope going out 250 m and back, with a 1 s ramp at each start and stop; it runs about
   67 times faster than real time, so a lift at 3.2 m/min (about 157 simulated minutes with the stops) takes
   about 2.4 (two lifts, the default, about 5) minutes.
4. The logger finds by itself when the rope moves, works out where along the rope each sample was taken from the
   strand ripple and the known length, and lines each later lift up with the first one.
5. Every number the beta starts from is a setting in one file, [settings.toml](settings.toml), with its source
   and the alternatives beside it; nothing is selected, and everything here is simulated, not measured.

## How to start it

From an empty checkout, in PowerShell, in this folder (`max/sws/line_beta`). Python 3.11 or later is needed
(`tomllib`); the path to `python.exe` is whatever Python is on the PC.

```powershell
python.exe -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe run_beta.py
```

The packages (all from pip, nothing installed system-wide, nothing outside the PC): numpy, matplotlib, paho-mqtt
(MQTT client), amqtt (MQTT broker, listens on 127.0.0.1 only), crc32c, pytest.

Other runs, each one line:

```powershell
.venv\Scripts\python.exe run_beta.py --set motion.speed_m_min=5.0       # the fast test case
.venv\Scripts\python.exe run_beta.py --heads 6 --seconds 600             # installation A, 6 heads, 10 minutes
.venv\Scripts\python.exe run_beta.py --heads 102 --seconds 60            # installation B, frames replayed
.venv\Scripts\python.exe run_beta.py --drop 5                            # drop 5 frames on one line
.venv\Scripts\python.exe run_beta.py --corrupt 3                         # corrupt 3 frames on another line
.venv\Scripts\python.exe run_beta.py --break-line 2                      # break a line for 2 s
.venv\Scripts\python.exe run_beta.py --net-stop 60                       # stop the network for an hour
.venv\Scripts\python.exe run_beta.py --restart-half                      # restart one half half-way
.venv\Scripts\python.exe run_beta.py --transport inproc                  # without the broker (faster)
.venv\Scripts\python.exe run_beta.py --table tables\example_table.csv --start 1977.6 --seconds 0.5
.venv\Scripts\python.exe run_beta.py --proof                             # the proof table (about 15 min)
.venv\Scripts\python.exe -m pytest -m "not slow"                         # the tests (about 3 min)
.venv\Scripts\python.exe -m pytest -m slow                               # the 250 m tests (about 6 min)
```

## What you see

A status line that updates every two seconds:

```text
sim   42.8 min  x   85 real time      20 frames/s     24.7 kB/s line  lost 0  buffer    0.0 MB  disk   63.8 MB  network up
```

simulated time, speed against real time, frames per second into the box(es), bytes per second on the serial
lines, frames lost (counted by the box), the box's disk buffer, the logger's disk use, and the network state.
At the end it prints the losses, the traffic against `../transmitter/line_calc.py`, the position error and the
drift, and writes into the output folder (`out/` unless `--out`): `report.json`, `per_second.json`, the run
folders (raw frames plus an index, `results_half0.json`), the logger's session store, and the plots B1–B4 (B1 only when a broken wire lies inside the travel).

## Settings

All in [settings.toml](settings.toml). The not-settled ones, with their starting value and alternatives:

| Setting | Starting value | Alternatives | From |
|---|---|---|---|
| `motion.speed_m_min` (rope speed) | 3.2 m/min | 5.0 (fast test case) | owner |
| `rope.length_m`, `rope.travel_m` | 250 m | — | owner |
| `motion.ramp_s` | 1 s | — | owner |
| `converter.rate_per_s` | 4000 | 1000, 2000 | transmitter-line note |
| `half.line_rate_per_s` | 250 | 80, 100, 125 | owner, transmitter-line note |
| `half.filter` | `three_stage` (three block averages + correction) | `block` (one block average) | transmitter-line note |
| `half.frame_period_s` | 0.1 s | — | owner |
| `line.bit_rate` | 460 800 bit/s | 1 000 000 | transmitter-line note |
| `line.arrangement` | one line per half | shared RS-485 line (not built) | specification / note |
| `box.arrangement` | one box per winch | one per head | transmitter-line note |
| `box.buffer_length_h`, `box.buffer_max_MB` | 24 h, 4096 MB | 1, 72, 720 h | transmitter-line note |
| `mqtt.transport` | real broker on the PC | in-process stand-in | — |
| `mqtt.topic_raw` | `sws/{installation}/{winch}/{head}/{half}/raw` | — | transmitter-line note |
| `mqtt.per_message` | one message per half per frame | one per box per second (not built) | transmitter-line note |
| `rope.strand_pitch_mm` | 40 mm, varying 1 % in a 5 m wave | 30, 60 mm | repository (assumed there) |
| `faults.signal_mm` | 10 mm (two-lobed pulse) | 20, 25, 60 mm | transmitter-line note |
| `hum.mains_Hz` | 49.9 Hz | 50, 60 Hz | assumed |

The disturbances, each with its unit and an `enabled` switch: `standing` (mT), `lma` (mT per % of metal,
head response mm), `faults` (mT per wire, gap factors, widths), `ripple` (µT, harmonics), `noise` (µT rms,
converter noise from the sheet), `drift` (µT per hour), `temperature` (°C, K per hour, % per K), `hum` (µT,
harmonics, drive tone). The fault list (`[[fault]]`) is the 52 mm test-rope list with each zone moved onto the
250 m rope, plus one 2 % stretch over 10 m. The provisional pass figures are under `[proof]`.

## Proof

Provisional figures: **the owner sets them.** A test that fails stays failing. All simulated.

| Test | Figure (provisional) | Result | Pass |
|---|---|---|---|
| A 10 mm fault at 5 m/min arrives with its peak | at least 95 % | 99.9 % (1 348.7 of 1 350 µT, both lobes) | pass |
| A slow drift put in is recovered at the logger | within 2 % | 19.83 against 20 µT/h put in: 0.9 % low | pass |
| 50 Hz hum (49.9 Hz, 30 µT) with 2nd, 3rd, 5th harmonics and a 300 Hz drive tone: change of the one-second level | at most 1 µT (a fifth of the 5 µT level need) | 0.085 µT largest, 0.028 µT mean, any channel | pass |
| Position from the data alone after registration, 250 m out and back | within 10 mm | largest 27.3 mm, rms 10.8 mm | **FAIL** |
| No frame lost silently: losses put in = losses counted | equal | 11 put in (drops, corruptions, two line breaks) = 11 counted by the box = 11 by the logger = 11 missing | pass |
| A restart of a half is seen and its silence counted | 20 frames (2 s) | 1 restart, 20 frames | pass |
| The box rides through a network stop of 10 simulated minutes | no frame lost | 0 lost; 12 001 frames held on disk (15.1 MB) and sent after | pass (also over the real broker) |
| Measured traffic and storage against `line_calc.py` | within 5 % | largest difference 0.6 % (table below) | pass |

Numbers from `run_beta.py --proof` (in-process transport; the network-stop test also runs over the real broker in
`pytest`). The 250 m tests use the default settings (3.2 m/min, two lifts); the fault test uses 5 m/min on a 20 m
travel with one wire, run with and without it, so that the difference is the wire alone.

**Position, before and after registration.** The first lift is the reference; a later lift starts 7 mm further
on (assumed). From the data alone (ripple count, ramps, fixed length): first lift rms 10.8 mm, largest 27.3 mm;
later lift before registration rms 16.4 mm, largest 34.3 mm; after registration to the first lift rms 10.8 mm,
largest 27.3 mm. Registration removes the later lift's own error (it lands on the first lift to within 0.1 mm)
but cannot remove the first lift's: the assumed strand pitch varies 1 % in a 5 m wave, so a ripple count reads up
to about 16 mm short inside each wave, and the fixed length only corrects the total. With a constant pitch (side
figure, same runs otherwise): largest 11.0 mm after registration, rms 4.3 mm, so the figure still fails by a
little; what is left there comes mostly where wires and losses pass the head and distort the ripple for a moment.
The 10 mm figure cannot be met against the true position without a position reference on the rope (marks, or an
encoder); against the first lift it is met.

## Measured traffic and storage against the calculation

One head, 250 per second, 1 229-byte frames every 100 ms per half, measured over two lifts (317.6 simulated
minutes):

| Quantity, per half | Measured in the run | `line_calc.py` | Difference |
|---|---|---|---|
| Serial line, bytes × 10 bits | 123.43 kbit/s | 123.50 kbit/s | −0.1 % (COBS adds 1 byte here; line_calc counts 5) |
| Stored raw frames (frame + 9 box bytes + 4-byte record length) | 44.71 MB per running hour | 44.57 MB | +0.3 % |
| The same with the CSV index | 46.91 MB per hour | 44.57 MB | +5.3 % (the index is 2.2 MB per hour; not in line_calc) |
| MQTT packets of the raw messages | 100.88 kbit/s | 101.52 kbit/s (MQTT part of `traffic.mqtt_message`) | −0.6 % (shorter topic) |
| Box disk buffer during a 10-minute stop, one head | 15.1 MB, i.e. 90.7 MB per hour | 89 MB per hour (installation A) | +1.8 % (topic stored per record) |

Ethernet, IP and TCP bytes, which `line_calc.py` adds on top of MQTT, cannot be measured on one PC (loopback or
in-process); they are not compared. Health messages (once a second per half) add about 2 % MQTT traffic.

## Scale: 6 and 102 heads

| Run | Frames | Lost | Speed | Per half against `line_calc.py` | Logger disk |
|---|---|---|---|---|---|
| 6 heads (installation A), 10 simulated minutes, all generated, real broker | 72 000 | 0 | 11 × real time | serial −0.1 %, storage +0.3 % | 89.4 MB raw in 10 min = 537 MB per running hour (line_calc: 12 halves × 44.6 = 535) |
| 102 heads (installation B, 51 boxes of 4 halves), 60 simulated s, frames of one head replayed with each half's id (tables of frames), in-process | 122 400 | 0 | 6 × real time | serial −0.1 %, storage +0.3 %, MQTT −0.5 % | 14.7 MB in 60 s = 9.1 GB per running hour (line_calc 9.1) |
| The same 102 heads over the pip broker (amqtt) | 122 400 sent | the logger had received 11 841 when it gave up waiting | — | — | — |

At 102 heads the pip broker is the limit, not the box or the logger: 2 040 messages a second from 51 boxes,
pushed six times faster than real time, were more than it could pass on. A broker meant for production (not pip
installable, so not tried here) is needed to test B over MQTT; the in-process transport shows that the box and
logger code keep up.

## What is simulated and what is real code

| Piece | File | Real or simulated |
|---|---|---|
| Rope, head, elements, converter counts | `linebeta/rope_sim.py` | **Simulated** (sizes from the repository, the rest assumed; see settings) |
| Half: decimation filter, frame, CRC-32C, COBS | `linebeta/half.py` | Real logic, in Python, to be carried to C; time is simulated |
| Serial line | `linebeta/line.py` | **Simulated** (bit rate, send buffer, faults put in) |
| Root box: check, count, stamp, disk buffer, forward, health | `linebeta/root_box.py` | Real code; only its byte source and clock are simulated (`run_serial` reads real ports, untested) |
| Transport | `linebeta/transport.py` | Real MQTT to a real broker on the PC (amqtt); in-process stand-in with the same interface |
| Logger: storage, moving, runs, position, registration, drift | `linebeta/logger.py`, `linebeta/analysis.py` | Real code on simulated data |
| One command, report, plots | `run_beta.py`, `linebeta/pipeline.py`, `linebeta/plots.py` | — |

The network stop is a real disconnect of the box's MQTT client from the broker; the network itself is the PC's
loopback. Nothing leaves the PC.

## The half in C later

The half is written as plain functions on integer arrays with explicit state, so it maps to C as follows:

| Python (`half.py`) | In C | One to one? |
|---|---|---|
| `crc32c_ref` | table CRC-32C (or the microcontroller's CRC unit) | yes |
| `cobs_encode`, `cobs_decode` | the usual COBS loop | yes (the Python splits on zeros; same output) |
| `pack24`, `build_frame`, `HEADER_FMT` | byte writes into a 1 229-byte buffer, little-endian | yes |
| `cic3_decimate` | three `uint64_t` integrators per channel per converter result (wrapping), decimate, three combs per output, `(x + n³/2) / n³` | yes in arithmetic; numpy's `cumsum` stands for the per-result loop |
| `correction` | `(-y0 + 10*y1 - y2 + 4) >> 3` | yes |
| `block_average` | sum of n results, `(sum + n/2) / n` | yes |
| `Half.process` framing, counters, boot count, edge latch | main loop; the 1 Hz edge is an interrupt that latches the converter result count | logic yes; the edge list becomes an interrupt |
| temperatures | an I²C/SPI read once a second | not modelled (value given by the simulator) |
| SPI, DRDY, converter set-up, DC block off | driver code | not in the beta |

No high-pass, no offset removal and no scaling anywhere in the half or the box: the tests check that a constant
comes out unchanged to the count and that a ramp keeps its slope.

## Table format

A table replaces the generated signal (settings `sim.mode = "table"`, `sim.table_path`, or `--table`). It is
how a recording from a real head will be replayed through the same half, line, box and logger.

- **File**: `.csv` (plain text, UTF-8) or `.npz` (numpy, the same arrays).
- **Header lines**: `# key: value`, at least `rate_per_s` (converter results per second, must equal
  `converter.rate_per_s`), `elements` (32), `units` (`counts`).
- **Columns**: `sample` (converter result index, consecutive integers), `t_s` (= sample / rate, seconds from the
  start of the simulation or recording), `x_mm` (position along the rope in mm if known, empty if not; not read by
  the line, kept for comparison), `temp_half0_C`, `temp_half1_C` (each half's temperature, °C, 0.01 resolution),
  then `e00` … `e31`.
- **Elements**: `e00`–`e15` are half 0, `e16`–`e31` half 1; within a half, channels 0–7 are the radial elements
  at positions 0–7 round the rope (22.5° apart) and 8–15 the axial elements at the same positions.
- **Units**: signed 24-bit converter counts (±8 388 607), as the converter delivers them; to microtesla with
  `linebeta.settings.counts_per_uT` (radial 1.0 mV/V/mT, gain 1; axial 5.0 mV/V/mT, gain 2; 3.3 V; ±1.2 V).
- **Time**: from `sample` and `rate_per_s` only; a recording must be at the converter rate, without gaps.
- **Example**: [tables/example_table.csv](tables/example_table.csv), 0.5 s (2 000 rows) made by the simulator with
  `run_beta.py --make-table tables/example_table.csv --start 1977.6 --seconds 0.5`, while wire F02 passes the head.
  The test `tests/test_run_beta.py::test_example_table_replays_to_the_same_frames` runs it through the whole line
  and checks that the frames are the same, byte for byte, as those of the generated run over the same span.

## Fitting the simulator to a recording

No fitting tool is built; the settings are kept apart so that each can be read off one feature of a recorded
trace, one at a time, with the others switched off in the simulator for the comparison:

| Setting | Read off | Needs |
|---|---|---|
| `noise.element_uT_rms` | rms of each channel at standstill, after removing the mean and the mains lines | a standstill; the converter part (sheet) taken out in quadrature |
| `hum.mains_Hz`, `hum.uT`, `hum.harmonics`, `hum.drive_*` | the line spectrum at standstill | a recording at the converter rate (above half the line rate the half's filter removes them) |
| `drift.uT_per_h`, `drift.spread` | slope of each channel's level during a long standstill at steady temperature; or out against back at the same rope point (figure B4) | hours |
| `temperature.magnet_pct_per_K` | level against the frames' temperatures over a day at standstill, after the drift | a temperature swing |
| `standing.radial_mT`, `standing.axial_mT` | mean level of each channel on clean rope | — |
| `rope.strand_pitch_mm` | ripple cycles counted over a known travel | the fixed length |
| `ripple.radial_uT`, `ripple.axial_uT`, `ripple.harmonics` | half the peak-to-peak of the band-passed ripple in steady running; its spectrum at 2× and 3× the ripple frequency | steady speed |
| `rope.pitch_variation_*` | the ripple count against an independent position (marks on the rope) | marks; the data alone cannot show it |
| `lma.axial_mT_per_pct`, `lma.head_response_mm` | the level step over a known loss (test rope L2, 1 % × 1 m) and the width of its edges | the test rope |
| `faults.radial_mT_per_wire`, `faults.signal_mm`, `faults.axial_*`, `faults.*_angle_deg` | peak and lobe distance of a known wire (test rope F02), on each position round the rope | the test rope |
| `motion.speed_m_min`, `motion.ramp_s` | ripple frequency over time | — |

## Run files

The logger keeps everything it receives in `<out>/session/` and writes each run it finds into
`<out>/run_w<winch>_h<head>_<n>/`:

- `frames_half<k>.bin`: records of `u32 length` (little-endian) + the message as received: the half's frame
  unchanged (layout below) + 9 bytes from the box (`u64` receive time in µs since the box epoch, `u8` quality:
  1 = frames missing before this one, 2 = first frame after a restart, 4 = held in the box's buffer).
- `index_half<k>.csv`: one row per record: `offset, length, winch, head, half, half_id, boot, first_index, n,
  rx_us, quality, t_first_s` (time of the frame's first sample from the 1 Hz edge latch).
- `run.json`: start and end time, frames and bytes per half. `results_half0.json`: passes, direction, scale,
  registration shift, drift, radial peaks.

Frame (as `../transmitter/transmitter_line.md` section 5; little-endian; 1 229 bytes at 250 per second): byte 0 type
0x11; 1 half id; 2–5 index of the first sample (u32); 6 samples (25); 7 rate and filter code (filter id << 6 |
converter rate code << 3 | line rate code); 8–9 health; 10 boot count; 11 sync edges seen; 12–15 sync latch (line
sample index at the 1 Hz edge); 16–17 sync fraction (/65 536 of a line sample); 18–21 two temperatures (i16,
0.01 °C); 22 aux slot; 23–24 aux value; 25… samples × 16 channels × 3 bytes (channel 0–7 radial, 8–15 axial, signed
24-bit); last 4 CRC-32C. On the serial line each frame is COBS-encoded and ends with a 00h byte.

## Figures

Drawn by `run_beta.py` after the default run (one head, two lifts, 3.2 m/min, real broker), copied to
[figures/](figures/). Simulated: every curve is the beta's own computation, none is a measurement.

### Figure B1

[fig_b1.html](figures/fig_b1.html) · [fig_b1.png](figures/fig_b1.png). One broken wire (F02: one outer wire, 2 mm
gap, at 102 m) on the radial element facing it, standing level removed. Solid: what the simulator put on the
element; dashed: what the logger stored after the half, the line, the box and MQTT, drawn on the logger's own
position. The shape and both peaks arrive whole (about −1 380 and +1 080 µT, with the ripple under them); the
dashed curve sits about 10 mm early because the logger's position from the ripple is 10 mm off at that point of
the rope (figure B2).

### Figure B2

[fig_b2.html](figures/fig_b2.html) · [fig_b2.png](figures/fig_b2.png). Position error along the 250 m rope: the
first lift out and back, a later lift before and after registration, and the provisional ±10 mm band. The 5 m
wave is the assumed pitch variation.

### Figure B3

[fig_b3.html](figures/fig_b3.html) · [fig_b3.png](figures/fig_b3.png). Serial, MQTT and stored rate per half,
one-minute means, against the figures `line_calc.py` gives.

### Figure B4

[fig_b4.html](figures/fig_b4.html) · [fig_b4.png](figures/fig_b4.png). The axial level on the way back minus on
the way out at the same rope point, against the time between the two visits: the drift put in (20 µT per hour)
and what the logger recovered from the stored frames.

## Terms

- **SWS**: the whole product. **Head**: the part on the rope, two halves. **Half**: one of them, with its own
  board. **Element**: one field sensing element (8 radial + 8 axial per half). **Channel**: one converter input.
- **Root box**: the box at the other end of the serial cables (the owner's "transmitter").
- **Converter rate**: results per second from the converter. **Line rate**: values per channel per second after
  the half's averaging.
- **Frame**: what a half sends every 100 ms. **Run**: one lift, out and back, as the logger finds it.
- **Registration**: lining a run's position axis up with the first run's, on the signal itself.
- **MQTT**: a publish/subscribe message protocol over TCP; the box publishes, the logger subscribes, a broker
  passes the messages on. **COBS**: consistent overhead byte stuffing (no 00h inside a frame). **CRC-32C**: the
  Castagnoli 32-bit check.

## Sources

Signal sizes and their sources are named beside each value in [settings.toml](settings.toml): the transmitter-line
note and its `line_calc.py` (`../transmitter/`), `../3d/falsify/g_large_box.md` (level per 1 % of metal),
`../3d/falsify/d_measurement_chain.md` (residual standing field, magnet coefficient), `../3d/falsify/c_third_dimension.md`
(one broken wire at the radial and axial elements), `../3d/results/u19_summary.json` via the transmitter-line note
(strand ripple), the ADS131M08 noise table via `line_calc.py`, and the 52 mm test-rope fault list (branch
`u84-test-rope`). Traffic is compared with `line_calc.py` and `../data-path/traffic.py`, imported unchanged.

## What is not done

- The 10 mm position figure is not met (above); no reference on the rope is simulated.
- The half in C; SPI, DRDY, the converters' set-up, the temperature part's driver.
- The root box on real serial ports: `run_serial` is written for pyserial but not installed or tested; no real
  clock discipline (NTP or PTP) and no 1 Hz edge output: the edge is simulated at whole simulated seconds.
- The shared RS-485 line, and one MQTT message per box per second: settings exist, code does not.
- 102 heads over MQTT with a production broker; 102 heads with every head generated (frames are replayed).
- The logger writes each run's files when the session closes, not live as the run starts and stops; it processes
  half 0 of each head only (not both halves together, not two heads of a winch).
- Registration is on the strand ripple only, within half a pitch; no coarse step on the long-loss trace.
- Direction from the order of the ripple phase round the rope works here because the simulated ripple is a helical
  pattern by construction; the logger takes the passes as out then back and reports whether the phase order agrees.
- Faults: a plain threshold list of radial peaks; no template, no counting against discard criteria.
- Element noise is white (no one-over-f part); the radial element reads no long loss (no number on record); all
  pulse shapes, the ripple shape and the pitch wave are assumptions.
- No format for a commercial logging system; no compression; no retention handling.
- Nothing is measured; no recorded trace has been replayed yet (the table format is ready for one).

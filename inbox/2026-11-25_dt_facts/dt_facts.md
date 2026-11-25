# Fixed facts for the digital twin of the SWS

## In short

- This page lists what a digital twin of the SWS must hold, one fact per line.
- Each line carries one status word, as in the parts table, and the place where it is recorded.
- Where the record holds two values, both are shown and the line says **two values on record**. Nothing is
  settled here that has not been ruled.
- Where older documents say something else, they are listed in [dt_disagreements.md](dt_disagreements.md),
  with the change that would correct them. No existing file is changed.
- Every calculated figure shows its arithmetic.

Status words (from the [parts table README](../parts_table/README.md)): ruled by the owner · on record, one
value · on record, several values · calculated, not measured · proposal, not agreed · open: nothing on record.
"Outside" means the fact is held outside this repository and is not yet in a project document (the parts table
writes such a source `outside: ...`). Parts-table rows are cited by their id in
[parts.yaml](../parts_table/parts.yaml).

## 1. Counts and hierarchy

| # | Fact | Status | Recorded at |
|---|---|---|---|
| F01 | Names: SWS (the whole Safe Wire Sensor), head, half, sensing element (radial / axial), channel, root box. "Sensor" alone is not used. | ruled by the owner | [parts.yaml](../parts_table/parts.yaml) `names` |
| F02 | Hierarchy: shiplift → main station → winch → rope → SWS → half → channel. | ruled by the owner | outside; counts in F03–F07 |
| F03 | Large (52 mm) installation: 3 main stations × 17 winches = 51 winches. | ruled by the owner | parts.yaml I03 (51 winches); the split 3 × 17 is outside |
| F04 | One rope per winch: 51 ropes. Two SWS per rope: 51 × 2 = 102 SWS. Two halves per SWS: 102 × 2 = 204 halves. | ruled by the owner | parts.yaml I03 |
| F05 | First installation: 6 SWS = 6 × 2 = 12 halves; the 40 mm head on 38 mm rope; the record gives it as 6 winches with one head each. | ruled by the owner | parts.yaml I04 |
| F06 | Heads built first: ten 40 mm heads. | ruled by the owner | parts.yaml I05 |
| F07 | Rope diameter: 52 mm on the large installation (design range 35–57 mm); 38 mm on the first installation. | on record, one value | parts.yaml R02; I04 |
| F08 | Sensing elements: 8 radial + 8 axial per half = 16; 16 positions round the rope at 22.5° (8 per half). | on record, one value | parts.yaml D03; [transmitter_line.md](../transmitter/transmitter_line.md) l.66 |
| F09 | Board arrangement: spokes (specification) or one thin board (prototype); not settled. **Two values on record.** | on record, several values | parts.yaml D01 |

## 2. Channels, converters, rates, frame

| # | Fact | Status | Recorded at |
|---|---|---|---|
| F10 | Converters: two 8-channel converters per half (8 radial + 8 axial = 16 channels), digital temperature, ratiometric reference; no converter input for the supply or for temperature. | ruled by the owner | parts.yaml K01; [specification rev131](../spec/rendered/SWS_HW_Design_Input_Specification_rev131.md) l.298 |
| F11 | Converter part: ADS131M08 on record; ADS114S08 / ADS124S08 in one hardware case. **Two values on record.** | on record, several values | parts.yaml K02 |
| F12 | Channels: 16 per half; 16 × 2 = 32 per SWS; 204 × 16 = 3 264 on the large installation; 12 × 16 = 192 on the first. | ruled by the owner | parts.yaml K01, O03 (arithmetic there: 51 winches × 64 = 3 264) |
| F13 | Line rate in the product: 250 values per second per channel. The parts table still carries it as a proposal (V01, which also names 500 as preferred reserve in the specification); listed as disagreement D01. | ruled by the owner | outside (given as fixed); parts.yaml V01 |
| F14 | Converter data rate: 4 000 per second decimated to the line rate (line beta), 500 per second (hardware page), 250–1 000 per second (specification). **Two values on record** (three). | on record, several values | parts.yaml K04 |
| F15 | Values per second: large installation 204 halves × 16 × 250 = 816 000; first installation 12 × 16 × 250 = 48 000. | calculated, not measured | parts.yaml O03 (large); first: arithmetic here |
| F16 | Frame: one every 100 ms per half; 250 × 0.1 s = 25 samples per frame. Header 25 bytes: 25 + 25 × 16 × 3 + 4 (check) = 1 229 bytes, 1 235 on the wire; or header 23 bytes: 23 + 1 200 + 4 = 1 227 bytes. **Two values on record.** | on record, several values | parts.yaml Z02 |
| F17 | Load per half on its line: 1 235 bytes × 10 frames/s × 10 bits = 123.5 kbit/s, 26.8 % of 460.8 kbit/s. | calculated, not measured | parts.yaml Z03 |
| F18 | Temperature: one digital part per half on the carrier (I²C / SPI fits the two-converter board) and a second on the yoke, or 9–10 per half (outside round); resolution 0.5 °C for the part (specification) and a frame field in steps of 0.01 °C (transmitter-line note). **Two values on record.** | on record, several values | parts.yaml T01; specification rev131 l.346; transmitter_line.md l.332 |
| F19 | Microcontroller: none named; one per half, Cortex-M class. | open: nothing on record | parts.yaml U01 |

## 3. Line, root box, network path

| # | Fact | Status | Recorded at |
|---|---|---|---|
| F20 | Line from half to root box: RS-422, one per half (specification) or RS-485 shared by several heads on category 7 cable (newer thought). **Two values on record.** | on record, several values | parts.yaml N01, N02 |
| F21 | Line bit rate: 460.8 kbit/s or 1 Mbit/s, not settled. **Two values on record** (as candidates). | open: nothing on record | parts.yaml Z01 |
| F22 | Cable length: set by the hoist layout; RS-422 good for 100 m at this rate. | on record, one value | parts.yaml N03 |
| F23 | Root box per hoist (winch), up to four halves (specification): 51 on the large installation, 6 on the first; or one per head (transmitter-line note, line beta): 102 on the large installation. **Two values on record.** | on record, several values | specification rev131 l.402; transmitter_line.md l.50, l.364; line_beta README l.78 |
| F24 | Root box kind: 4 × RS-422, 4 × fused 24 V, 1 × Ethernet, PoE (specification) or an industrial mini computer that receives and forwards (newer thought). **Two values on record.** | on record, several values | parts.yaml X01 |
| F25 | Root box buffer for a lost network: 24 h, 4 096 MB (alternatives 1, 72, 720 h). | proposal, not agreed | parts.yaml X02 |
| F26 | PoE class of the root box: 802.3af or 802.3at. | open: nothing on record | parts.yaml X03 |
| F27 | Network path: half → own line → root box → one Ethernet connection on one managed, rate-limited switch port per root box → server / logger. MQTT from the box to the logger is the proposal on record. | on record, one value (port); proposal, not agreed (MQTT) | specification rev131 l.414; transmitter_line.md l.355–357, l.370 |
| F28 | Supply: 24 V from the root box over the same cable; local 3.3 V. | on record, one value | parts.yaml S01 |
| F29 | Firmware: bootloader with remote update through the root box. | on record, one value | specification rev131 l.347, l.415 |
| F30 | Connection to the control system: none on the first installation; on the 52 mm installation possible, added only if the first installation's test runs show it is strictly needed. | ruled by the owner | parts.yaml I04, I06 |

## 4. Rope, travel, speed, position, bending cycles

| # | Fact | Status | Recorded at |
|---|---|---|---|
| F31 | Fixed travel on the 52 mm installation: 250 m (the rope length R18 refers to). Travel on the first installation: not on record. | ruled by the owner | parts.yaml I01 (R18 still lists ≤ 220 m beside it) |
| F32 | Rope speed on the 52 mm installation: 3.2 m/min at the drum (0.4 m/min × 8 = 3.2); 5 m/min the fast test case; 15 m/min is the specification's extreme case. Speed on the first installation: not on record. | ruled by the owner | parts.yaml I02 (R17 still lists 3 / 15 m/min beside it) |
| F33 | One pass at 3.2 m/min: 250 m / 3.2 m/min = 78.1 min; at 5 m/min: 250 / 5 = 50 min. | calculated, not measured | arithmetic here, from F31, F32 |
| F34 | Rope position: proximity sensors at each end of the fixed travel, on both installations; by default the SWS works out movement, speed and position from its own data (strand ripple, with the known ramp, top speed and travel). No encoder (given as ruled for both installations). | ruled by the owner | parts.yaml I01; I04 (no encoder, first installation); "no encoder" for both: outside |
| F35 | Bending cycles: calculated in the control system and written to the same server as the SWS data; the screen shows both. This does not conflict with F30 (two domains, same rope). | ruled by the owner | outside (no parts-table row yet) |

## 5. Time and processing

| # | Fact | Status | Recorded at |
|---|---|---|---|
| F36 | Time alignment of the halves: a 1 Hz edge on its own pair from the root box; each half latches its sample counter; residual 80 µs; at 15 m/min (0.25 m/s) 0.25 m/s × 80 µs = 0.02 mm, at 3.2 m/min (0.053 m/s) 0.004 mm. | on record, one value | parts.yaml Z04 |
| F37 | Without the edge two halves drift apart by up to 80 ppm: 220 m × 80 × 10⁻⁶ = 17.6 mm (on the 250 m travel: 250 m × 80 × 10⁻⁶ = 20 mm). | calculated, not measured | parts.yaml Z05; 250 m line: arithmetic here |
| F38 | Who stamps the time: the half sends a sample index and the latched count, the root box adds its receive time and maps the halves onto one time base (specification, transmitter-line note); or the SWS stamps each block at sampling from SNTP (twin architecture). **Two values on record.** | on record, several values | specification rev131 l.413, l.419; transmitter_line.md l.355, l.457; twin `architecture.html` l.326–327 |
| F39 | Where processing happens: in the root box (position tagging, template correlation, detection: specification) or at the logger, the box only checking, stamping and forwarding (newer thought, the transmitter-line note, the line beta). **Two values on record.** | on record, several values | parts.yaml X01; specification rev131 l.408, l.415; transmitter_line.md l.57 |
| F40 | Storage per half: (1 229 + 9) bytes × 10 frames/s × 3 600 s = 44.6 MB per running hour at 250 per second; large installation all day about 216 GB of raw frames. | calculated, not measured | parts.yaml O02, O04 |
| F41 | What the site's logging system takes: not known. | open: nothing on record | parts.yaml O01 |

## 6. Screens and states

| # | Fact | Status | Recorded at |
|---|---|---|---|
| F42 | Three screens, kept apart: the project's own HMI, which training never changes; a separate trainer HMI where a rope is picked and a fault created; a customer HMI later. | ruled by the owner | outside |
| F43 | The state of a rope with a finding is called "Concern". It is not an alarm. | ruled by the owner | outside |
| F44 | A rope of concern is shown in warning orange, not alarm red. | ruled by the owner | outside |
| F45 | Findings latch: a rope leaves Concern only when the rope is replaced, or when the finding is removed with evidence (a person dismisses it with a recorded reason). | ruled by the owner | outside |
| F46 | The worst value may drop when a finding is dismissed. | ruled by the owner | outside |
| F47 | No statistics over a time window (such as "worst in 6 days"); what counts is the finding and its values while it stands. | ruled by the owner | outside |

## Count by status word

| Status | Facts |
|---|---|
| ruled by the owner | 20 (F01–F06, F10, F12, F13, F30–F32, F34, F35, F42–F47) |
| on record, one value | 7 (F07, F08, F22, F27 port part, F28, F29, F36) |
| on record, several values | 10 (F09, F11, F14, F16, F18, F20, F23, F24, F38, F39) |
| calculated, not measured | 5 (F15, F17, F33, F37, F40) |
| proposal, not agreed | 1 (F25) |
| open: nothing on record | 4 (F19, F21, F26, F41) |

F27 carries two words (the switch port is on record, the MQTT path is a proposal) and is counted under "on
record, one value". F13 is given as fixed and counted as ruled; the parts table still carries it as a proposal
(disagreement D01). 47 facts in all. Eleven lines are marked **two values on record**: F09, F11, F14, F16, F18,
F20, F21, F23, F24, F38, F39. F31 and F32 are ruled; the parts-table rows R18 and R17 still hold the older
values beside the rulings and are listed as disagreements.

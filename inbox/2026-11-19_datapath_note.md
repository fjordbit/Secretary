# Data path from the converters to the logger: blind round, own check, traffic

Calculated, not measured. Nothing here is selected; it is input for the owner's decisions. Words: SWS = the whole
product; head = the part on the rope, two halves; half = one of them, with its own board; element = one field
sensing element (16 per half); channel = one converter input; root box = the box at the other end of the serial
cables, as the specification calls it (the owner also calls it the transmitter). Terms: [terms.md](terms.md).

## In eight sentences

1. All three outside answers propose the same path: each half samples at a fixed rate of about 250 per second,
   sends the raw 24-bit samples in a frame every 100 ms over its own point-to-point serial line, and one root box
   per winch checks and forwards the frames unchanged over Ethernet (MQTT) to the logger, which does all processing.
2. They differ on the line rate (460.8 kbit/s in two answers, 1 Mbit/s in one), on how the 1 Hz timing edge
   travels, on whether a lost frame is resent, and on whether installation A should first run at 1000 per second.
3. A frame every 100 ms is not a sample every 100 ms: one sample per 100 ms puts 25 mm of rope between samples at
   15 m/min and steps over a 10–20 mm fault, while 250 samples per second sent in frames of 25 gives the
   specification's 1 mm, so "sample fast, send every 100 ms" reconciles the two (all three answers agree).
4. The traffic is small: at 250 per second one half sends about 123 kbit/s on its line, and the whole of
   installation B sends about 22 Mbit/s to the logger, about a fifth of a 100 Mbit/s link and about 2 % of 1 Gbit/s.
5. Two heads (four halves) on one shared RS-485 line hold at 250 per second only at 1 Mbit/s, at 50 % load, and the
   assumed rule of thumb for cable length (not checked against its documents) puts 1 Mbit/s at about 100 m; at 460.8 kbit/s one shared line holds two halves up to about
   230 per second.
6. A 1-wire temperature part works but is weak here (slow conversion, tight bit timing next to the converters'
   interrupts, poor accuracy at −40 °C); a digital temperature part on I²C or SPI fits the owner's two-converter
   board, which has no spare converter input for the answers' other choice, a thermistor.
7. All three answers name the logger, not the links, as the likely weak point (answer 1's main finding; the
   numbers here agree): installation B at 250 per second is 816 000 values per second and about 216 GB per day
   as raw frames if recorded all day (317 GB as 4-byte values), and what the site's logging system takes is
   not known.
8. The owner must first answer where rope position comes from and whether it is logged on the same clock, and
   then what the site's logging system can take.

## The record against the owner's newer thought and the three answers

Specification = `max/sws/spec/SWS_HW_Design_Input_Specification_rev123_2026-10-23.md` (section, line); the sampling and
link lines quoted read the same in the rev130 rendering, at other line numbers. Link note = `max/sws/hw-selection/sws_link_and_readout.md` (a proposal, not
the record). Answers = `answers/answer_1.md` … `answer_3.md`; the blind agents saw only the brief.

| Item | Specification says | Owner's newer thought (brief, or later correction) | Three answers say | Agreed? |
|---|---|---|---|---|
| Converters per half | Three ADS131M08: 16 elements + one input for the element supply + two analogue temperatures (§7 l.269, l.288). **Out of date on this point.** | Two 8-channel converters (8 radial + 8 axial = 16 signals), digital temperature, ratiometric reference: no input for the supply, none for temperature. (The blind brief still said three.) | All took three as given and use the spare inputs (A2 sends 8 spare-channel means per frame; A1–A3 put a thermistor on a spare input) | No: specification out of date; answers built on the brief's three |
| Signals per half | 16 (§6 l.235) | 16 | 16 | Yes |
| What sets the sampling | Tied to rope position: encoder-triggered, or fixed rate resampled to position in the root box (§4 l.131); 1 mm pitch (l.117); 250 S/s at 15 m/min (l.118) | A frame every 100 ms, perhaps 50 ms | Fixed time rate, 250 per second; position applied at the logger; A1, A3: a delta-sigma converter should not be started by position | Answers agree with each other and with the specification's second option; they move the resampling from the root box to the logger |
| Frame | Sample index, 16 values, excitation, temperatures, status/check (§10 l.378); link note: one 77-byte frame per sample instant | Every 100 ms (or 50 ms) | Every 100 ms, many samples per frame; header 20–32 bytes, 32-bit check, byte stuffing | Answers agree with the owner; the link note's frame per sample costs 56 % more line at 250 per second (192.5 against 123 kbit/s) |
| Line | RS-422, 4-wire + 24 V, shielded, 460.8 kbit/s or 1 Mbit/s, one per half (§10 l.373, l.377) | RS-485 so that several heads share a line; category 7 cable | One half per line in all three: RS-422 at 460.8 kbit/s (A1), RS-422 at 1 Mbit/s (A2), RS-485 parts wired 4-wire full duplex at 460.8 kbit/s with an addressed protocol for later sharing (A3) | Answers agree with the specification, not with the owner's sharing |
| Load per half, raw, 250 per second | 96 kbit/s payload "plus framing" (§10 l.377) | — | 122.8 / 125.8 / 124.1 kbit/s on the wire | Yes (own check 123.3 kbit/s) |
| Root box | One per hoist, up to four halves; position tagging, template correlation, detection, a full pass buffered, time sync, firmware (§10 l.369, l.373, l.380) | Industrial mini computer: receives, perhaps scales, sends on over Ethernet; all processing at the logger. A remote I/O station with a serial card: thought needlessly complex | One per winch, 4 ports; checks, time-stamps, buffers (hours to 24 h), forwards unchanged; no scaling, filtering or detection; remote I/O rejected by all three | Answers agree with the owner on processing at the logger and disagree with the specification; they advise against scaling in the box |
| Box to logger | One Ethernet port; protocol to be defined (§10 l.379, l.382) | MQTT "or other" | MQTT, acknowledged once, binary payload; UDP counted as the alternative | Yes |
| Time alignment of the halves | 1 Hz edge on its own pair; each half latches its sample counter; 80 µs residual (§10 l.384) | Same | A1, A3: own pair; A2: a sync byte on the box-to-half pair, its start bit as the edge. Across the site: PTP, else NTP | Mostly; A2 differs on the carrier |
| Rope position | No encoder on the SWS; logged hoist speed or position, time-stamped against the root-box clock (§8 l.330) | — | All three ask where position comes from; none assumes a source at the head | Yes, open |
| Temperature | One per half on the element carrier, 0.5 °C resolution, logged with every frame; a second on the yoke (§7 l.313) | Digital; 1-wire part known to the owner | 1-wire workable but weak; first choice a thermistor or RTD on a spare converter input, second a digital I²C/SPI part (±0.1–0.5 °C) | Partly: with two converters only the digital I²C/SPI choice is open; the link note already shows I²C |
| Width of a fault's signal | Set by lift-off, not the wire; about one rope diameter, 25–60 mm; pitch ≤ lift-off/5 (§4 l.125–131) | 10–20 mm fault (brief) | A2, A3: "I do not know how wide the signal is" | The record answers their question; 1 mm is conservative by its own rule |
| Cable length | "RS-422 is good for 100 m at this rate" (§10 l.381) | 5 / 30 / 100 m cases | Rule length × rate ≤ 10⁸ (all three; assumed here, not checked against the documents): 217 m at 460.8 kbit/s, 100 m at 1 Mbit/s (marginal) | Yes, on an assumed rule |
| Power per half | 0.2–0.4 W (§7 l.317) | — | Ethernet in the head rejected on power; A1: an always-on terminated driver 70–120 mW | Yes |
| Redundancy | No system redundancy in revision 1; sensing-element overlap only (§6 l.263) | — | No redundancy proposed | Yes |

## Figure T1 — bit rate on one serial line

![T1](fig_t1.png) — interactive: [fig_t1.html](fig_t1.html); slide: [fig_t1_slide.png](fig_t1_slide.png).

One half on its own line stays inside half of 460.8 kbit/s up to 472 per second. Two halves sharing a line reach
the 460.8 kbit/s margin at 230 per second; four halves (two heads) reach the 1 Mbit/s margin at 250 per second.

## Figure T2 — rope between two samples

![T2](fig_t2.png) — interactive: [fig_t2.html](fig_t2.html).

At 15 m/min, 10 and 20 samples per second put 25 and 12.5 mm between samples, inside or above the 10–20 mm band.
50 per second gives 5 mm; 250 per second gives the specification's 1 mm.

Further figures: T3 traffic from the root boxes to the logger ([fig_t3.html](fig_t3.html), [png](fig_t3.png)), storage per day
([fig_t3b.html](fig_t3b.html), [png](fig_t3b.png)), T4 safe cable length ([fig_t4.html](fig_t4.html),
[png](fig_t4.png)). Sources: [source.md](source.md). Tables: [traffic_tables.md](traffic_tables.md).

---

## Dense part

### The three answers, ten lines each

**Answer 1.** Fixed 250 per second, raw 24-bit, no position-triggered sampling (a restart resets the converter's
filter); position applied at the logger from time-stamped drive or encoder data. Frame every 100 ms, 28 bytes of
overhead, two temperatures, 32-bit check, byte stuffing; information frame every 10 s. RS-422 point to point, one
per half, 460.8 kbit/s; isolated ports and 24 V per port at the box. Box per winch, 4 ports; checks, time-stamps,
buffers hours, forwards unchanged, no scaling. MQTT acknowledged once, binary. Lost frame: marked, not resent.
RS-485 sharing rejected: a babbling half blocks the line; two halves at 250 per second use 54 % of 460.8 k. Ethernet
in the head kept for revision 2. Temperature: digital I²C/SPI on the board, thermistors on spare inputs where it
matters. Main finding: the logger is the bottleneck — but its "13 000 channels, 3.3 million samples per second"
for B is four times too high (see disagreements); its 217 GB per day is consistent with the right count.

**Answer 2.** Fixed 250 per second by default, settable to 500 or 1000; raw 24-bit; frame every 100 ms with a
20-byte header, 8 spare-channel means (24 bytes), two temperatures, 32-bit check. RS-422 point to point at 1 Mbit/s
(460.8 kbit/s beyond 100 m); the 1 Hz edge as a sync byte on the box-to-half pair; isolated transceivers and supplies
in the half. Box per winch: checks, one resend from a 2 s buffer in the half, PTP or NTP, 24 h buffer, MQTT one
message per head per 100 ms. RS-485 multidrop, Ethernet in the half and CAN FD rejected. Proposes running
installation A at 1000 per second and choosing B's rate from A's data. Lossless reductions only: record while the
rope moves; resample to 1 mm at the logger. Temperature: thermistor/RTD on a spare input first, digital I²C/SPI
second. Margin 60 % load.

**Answer 3.** Fixed rate; converters at 1000 per second averaged to 250 in the microcontroller; frame every
100 ms, 32 bytes of overhead including an optional position field; spare and supply values once a second. RS-485
parts wired 4-wire full duplex, one half per line, addressed protocol from the start; 460.8 kbit/s; isolation at
the box. Box per winch, industrial fanless computer, 4 isolated ports; checks, resend from a 2 s buffer, PTP clock,
generates the 1 Hz edge, 24 h flash buffer, forwards unchanged, no scaling. MQTT one message per half. Ethernet in
the half and CAN FD rejected; remote I/O station rejected. Reduction to 16 bits counted but not advised.
Temperature: thermistor/RTD on a spare input plus one accurate digital part. Margin 60 % load.

### Own check against the answers (differences over 10 %)

`traffic.py` (standard library; every assumption one named constant) reproduces the answers' traffic numbers within 10 %
above 50 per second. Where they differ by more than 10 %:

| Number | Own | Answer | Why | Who is right |
|---|---|---|---|---|
| Serial load per half at 10 / 20 per second | 7.7 / 12.5 kbit/s | A2: 10.2 / 15.0 (+32 / +20 %); A3: 8.5 at 10 (+10 %) | Frame overhead: A2 carries 8 spare-channel means (52 bytes overhead), A3 32 bytes + 3 idle characters, own 23 + 4 | Each, on its own assumption. With the owner's two converters there are no spare channels, so A2's 24 bytes fall away |
| MQTT traffic per head at 10 per second | 31.2 kbit/s | A2: 25 (−20 %) | A2 sends one message per head, so the per-message overhead is shared | Both; it matters only at low rates (within 2 % at 250) |
| MQTT per half at 10 per second | 15.6 kbit/s | A3: 17.3 (+11 %) | Larger MQTT header and topic | Both |
| Storage, B, 250 per second, all day | 216 GB raw frames; 317 GB as 4-byte values + time | 217 / 221 / 220 GB | Own second figure assumes a logger format | The answers, for raw frames; the logger's real format is not known |
| Highest rate per line | 50 % load, 1 half, at 115.2 kbit/s / 460.8 kbit/s / 1 Mbit/s: 113 / 472 / 1031 per second | A2, A3 at 60 % load: 130 / 560 / 1230 | Different margin; own figures at 60 %: 137 / 567 / 1239 | Both; the margin is a choice (2 halves at 115.2 kbit/s: A2 50 against own 62 at 60 %, from A2's 52-byte overhead and its rounding to steps of 10) |
| Storage, B, 10 / 50 per second | 13.2 / 47.1 GB per day (raw frames) | A2: 18 / 52 (+36 / +10 %); A3: 17 at 10 (+29 %) | A2 stores its 8 spare-channel means, A3 a 16-byte box header per message; at low rates the per-frame overhead dominates | Each, on its own assumption; own count has no box header (see assumptions) |
| B, channels and values per second | 3 264 channels, 816 000 values/s | A1: "about 13 000 channels, 3.3 million samples per second" | A1 multiplied the brief's 64 channels per winch by 204 (halves), not by 51 (winches) | Own, A2 and A3. A1's storage (217 GB/day) uses the right count |

### Traffic, raw 24-bit, frame every 100 ms (from `traffic.json`)

| Level (halves) | 10 per second: serial / MQTT | 250 per second: serial / MQTT | Storage per day at 250, raw frames |
|---|---|---|---|
| Half (1) | 7.7 / 15.6 kbit/s | 123 / 108 kbit/s | 1.06 GB |
| Head (2) = winch and box in A | 15.4 / 31.2 kbit/s | 247 / 216 kbit/s | 2.12 GB |
| Winch and box in B (4) | 30.8 / 62.4 kbit/s | 493 / 431 kbit/s | 4.24 GB |
| Installation A (12) | 92 / 187 kbit/s | 1.48 / 1.29 Mbit/s | 12.7 GB |
| Installation B (204) | 1.57 / 3.18 Mbit/s | 25.2 / 22.0 Mbit/s | 216 GB |

Serial at the installation level is the sum of the separate lines, not one line. MQTT is lower than serial at
250 per second because the serial line pays 10 bits per byte; at 10 per second the Ethernet overhead dominates.

Line load at 250 per second, raw: one half 27 % of 460.8 kbit/s; two halves on one line 54 % of 460.8 kbit/s, 25 %
of 1 Mbit/s; four halves 108 % of 460.8 kbit/s, 50 % of 1 Mbit/s (2-wire, polled). At 115.2 kbit/s even one half is 107 %.

### Disagreements, for the owner (not resolved here)

1. Line rate: 460.8 kbit/s (A1, A3) or 1 Mbit/s (A2, with 460.8 kbit/s beyond 100 m).
2. Sharing a line: the owner's RS-485 sharing against one half per line (all three). A3 keeps RS-485 parts and an
   addressed protocol so that sharing stays possible later.
3. The 1 Hz edge: own pair (specification, A1, A3) or a sync byte on the downlink pair (A2), which frees a pair.
4. Lost frame: resend from a 2 s buffer in the half (A2, A3) or mark and move on (A1).
5. Installation A at 1000 per second first (A2), or at 250 (A1, A3).
6. Where processing sits: in the root box (specification) or at the logger (owner's newer thought, all three).
7. Scaling in the root box: "perhaps" (owner) against "never; send the factors as data" (all three).
8. Converter rate: native 250 per second (A1) or 1000 averaged to 250 in the microcontroller (A3). Not checked
   here against the data sheet.
9. Margin: 50 % (A1, own) or 60 % (A2, A3) of the line rate.
10. Box buffer: hours (A1) or at least 24 h (A2, A3).
11. One MQTT message per half (A1, A3) or per head (A2).

### Assumptions (all in `traffic.py`)

16 signal channels per half, 3 bytes each; no other converter channel in the frame. Two digital temperatures
per half, read once a second, the latest value repeated in each frame header (2 bytes each). Header 23 bytes as in
the link note (type, half id, sample counter, health, boot count, sync fields, aux slot, temperatures); 4-byte
check; byte stuffing 1 byte per 254 plus a 1-byte delimiter; 10 bits per byte (8N1). Frame every 100 ms. Shared
line: 2-wire, polled, 6-byte poll and two gaps of 3.5 character times per frame. Margin: 50 % of the line rate.
Ethernet: preamble 8, header 14, check 4, gap 12, 64-byte minimum; IPv4 20; TCP 32 (with timestamps); MTU 1500;
MQTT topic 24 bytes, packet id 2, one message per half per 100 ms, no box header or receive time added by the root box
(all three answers add one; A3 counts 16 bytes); reverse acknowledgements counted separately.
UDP alternative: 8-byte UDP header plus an own 8-byte header. Storage: raw frame bodies, or 4-byte values plus an
8-byte time per sample; recording all day (an upper bound). Reduction for comparison: 16 bits per value (assumed,
not proposed). Cable: length × rate ≤ 10⁸ m·bit/s, at most 1 200 m (assumed, from memory). Installation A 12
halves in 6 boxes, B 204 halves in 51 boxes.

### Questions for the owner, in order

1. Where does rope position come from on installations A and B, and is it logged on the same clock as the root
   boxes? (All three answers ask; the specification assumes logged hoist speed or position, §8.)
2. What can the site's logging system take: 816 000 values per second for B at 250 per second, by which protocol,
   recorded all day or only while the rope moves, and kept for how long?
3. One half per line (specification, all three answers), or shared RS-485 lines? Four halves on one line need
   1 Mbit/s at 250 per second and keep cables near 100 m or less.
4. Processing in the root box (specification) or at the logger (newer thought)? And should the box scale at all?
5. Real cable lengths and where the root box sits.
6. What the temperature is for — correcting the elements (it must sit at them) or watching the board — and how
   accurate it must be below −10 °C.
7. Does the head network's switch support PTP?

### What is not known

The site's logging system and its input formats; the real cable lengths and routes; the noise near the winch
drives; whether the 10⁸ rule holds for the category 7 cable chosen; the converters' native lowest rate at the
chosen clock (not checked here); the bit error rate of the line; the winch duty cycle; how well a lossless coding
would compress this signal. The figures are calculated, from assumptions listed above; nothing is measured.

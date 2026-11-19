# The transmitter line: from the converters in a half to the root box and on to the logger

Calculated, not measured. Nothing here is selected; it is a design draft with its alternatives beside it, for the
owner's decisions. Words: SWS = the whole product; head = the part on the rope, two halves; half = one of them, with
its own board (two 8-channel converters, a microcontroller, a line driver); element = one field sensing element
(8 radial + 8 axial per half); channel = one converter input; root box = the box at the other end of the serial
cables, as the specification calls it (also called the transmitter). Converter data rate = results per second
from the converter; line rate = values per channel per second sent after averaging. Terms: [terms.md](terms.md).
Sources of every figure: [source.md](source.md). All numbers: `line_calc.py` → `line_calc.json`.

## In twelve sentences

1. The code on record is pseudocode and arithmetic, not firmware: a half that sends every converter result raw,
   a root box with stub processing, and traffic scripts; **there is no averaging anywhere in it**, only the
   converter's own filter.
2. The sampling theorem says a signal is carried faithfully only if it is sampled more than twice per cycle of its
   fastest part; anything faster that reaches the sampler folds down and looks like a slower signal.
3. A 10 mm fault at 15 m/min has content up to about 28 Hz, so the theorem's least rate is about 57 per second;
   at the normal 5 m/min it is about 19 per second.
4. How far above the least rate depends on one choice: if the samples are used as they fall, about four to five
   times the least rate keeps a 10 mm fault's peak within 1 % (250 per second up to 15 m/min, 125 up to 7.5, 80 up
   to 5; proposed rule 1: 16 per second for each m/min); if the logger interpolates between samples, the filter's
   own loss is all that counts and 100 / 50 / 40 per second do the same with the three-stage average below.
5. Converter noise is small: at the element it is 0.6–1.6 µT rms on a radial channel and 0.1–0.3 µT on an axial
   one over 250–4000 converter results a second, against a broken-wire need of about 15 µT rms, so the converter is
   not what sets the rate.
6. Averaging lowers converter noise only down to a floor the data sheet itself shows, and the element's own noise
   (assumed: about 1.5 µT rms, or about 7 µT on the less sensitive radial part if its voltage noise is what stays
   the same) is larger than the converter's, so more averaging buys little.
7. Averaging must only ever be a low-pass with a gain of exactly one at zero frequency, so drift and the long loss pass
   unchanged; any high-pass, offset removal or the converter's built-in "DC block" in the half or the box would remove
   the long-loss signal along with the drift (proposed rule 2).
8. Mains at 50 Hz folds to zero hertz at 10, 25 or 50 per second and would read as a level change if single samples
   were picked; a proper average in the half removes it before the rate is reduced, so picking samples is not
   proposed here.
9. Without an encoder, the strand ripple works as an encoder in the simulation: about 1 mm of position error per
   cycle count when the pitch is steady, 7–9 mm when the pitch varies 1 % along the rope, before the run is registered
   to the first run (the record's ±4 mm scheme); it fails at stops unless the count is held, and if noise exceeds about
   a fifth of the ripple.
10. The line itself is light: one frame of about 1.2 kB every 100 ms per half at 250 per second, 124 kbit/s,
   27 % of 460.8 kbit/s, which holds the 100 m cable case on the assumed cable rule; 1 Mbit/s is at its 100 m edge.
11. A root box needs 89 MB (installation A) or 178 MB (B) per hour of lost network at 250 per second, 2.1 or 4.3 GB
   for 24 hours.
12. Storage: installation B at 250 per second stores 9 GB per running hour, 3.3 TB a year at one hour a day and
   80 TB at 24; installation A a seventeenth of that; the first run of every rope kept for life is a few hundred MB.

## The line as blocks

```text
 HALF (x2 per head)                          ROOT BOX (one per winch; one per head as the alternative)       LOGGER
 16 elements -> RC filter -> 2 converters    receive (4 ports, RS-422/485 parts)                               MQTT broker
   (8 radial, 8 axial)       at 1-4 k/s      check (CRC-32C, sequence, boot count, half id)                     -> decoder
 microcontroller:                            stamp (box clock, NTP/PTP; 1 Hz edge out on its own pair)         -> run files
   three-stage average -> line rate          buffer (flash ring, >= 24 h)                                      -> moving detector
   frame every 100 ms, CRC-32C, COBS  ====>  forward unchanged as MQTT (QoS 1)  ==== Ethernet ====>             -> first-run archive
   latch 1 Hz edge, temperatures, health     health (ports, temperatures, link errors) 1/s                      -> processing
         <==== 1 Hz edge, commands ====      no scaling, no filtering, no detection
```

## The line in numbers

Line rate 250 per second unless said; how: C calculated, S read on a sheet, R from a repository note, A assumed.

| Item | Value | How |
|---|---|---|
| Elements per half / channels | 16 (8 radial, 8 axial) on two 8-channel converters | owner |
| Converter data rate (ADS131M08, 8.192 MHz) | 250, 500, 1000, 2000, 4000 … per second | S (Table 8-2) |
| Converter noise at the element, radial / axial, 1000 per second | 1.02 / 0.18 µT rms | C from S |
| Broken-wire need | 0.10 mT p-p ≈ 15 µT rms | R (spec §7) |
| Long-loss level need | 5 µT, the brief's figure (1 % of the 0.675 mT a 1 % loss gives is 6.75 µT) | brief; R (g_large_box) |
| Line rate keeping a 10 mm fault within 1 %, samples as they fall | 80 / 125 / 250 per second at 5 / 7.5 / 15 m/min | C (simulated pulse) |
| The same, logger interpolating (filter loss only), three-stage / block | 40 / 50 / 100; 50 / 80 / 160 per second | C (simulated pulse) |
| Frame | 25-byte header + 16 × 3 bytes × 25 samples + 4-byte check = 1 229 bytes, 1 235 on the wire | C (proposal) |
| Frames per half | 10 per second | proposal |
| Serial load per half | 123.5 kbit/s (63.4 at 125 per second) | C |
| Share of 460.8 kbit/s / 1 Mbit/s | 26.8 % / 12.4 % | C |
| Cable length the rule allows, 460.8 kbit/s / 1 Mbit/s | 217 m / 100 m against the 100 m case | A (rule of thumb, unchecked) |
| MQTT messages, A / B | 120 / 2 040 per second (one per half per 100 ms) | C |
| MQTT traffic, A / B | 1.3 / 22.2 Mbit/s | C |
| Box buffer, 1 h / 24 h lost network | A 89 MB / 2.1 GB; B 178 MB / 4.3 GB | C |
| Storage per half per running hour | 44.6 MB (18.6 MB at 100 per second) | C |
| Storage per year, 1 / 4 / 24 running hours a day, A | 0.20 / 0.78 / 4.7 TB | C |
| Storage per year, 1 / 4 / 24 running hours a day, B | 3.3 / 13.3 / 80 TB | C |
| Disk for one year of everything, half full, B, 4 h a day | 27 TB | C, A (50 % fill) |

## Figures

**N1 — converter noise against converter data rate, both parts.** ![N1](fig_n1.png) Interactive:
[fig_n1.html](fig_n1.html); slide: [fig_n1_slide.png](fig_n1_slide.png) (part 1 = ADS131M08, part 2 =
ADS131E08). Every curve stays under a sixth of the broken-wire need; noise rises slowly with the rate. The second
part sits lower partly because of its higher gain and an unconfirmed factor in its noise equation.

**S2 — a fault's peak kept after averaging, against line rate.** ![S2](fig_s2.png) Interactive:
[fig_s2.html](fig_s2.html); slide: [fig_s2_slide.png](fig_s2_slide.png). Below about 80 per second a 10 mm fault
loses its peak; at up to 7.5 m/min the three-stage average keeps it within 1 % from 125 per second, a block average
from 160, and the 20 ms mean stays about 2 % short at any rate.

**D1 — storage per year against running hours per day.** ![D1](fig_d1.png) Interactive: [fig_d1.html](fig_d1.html).

Further figures: N2 noise after averaging ([html](fig_n2.html), [png](fig_n2.png), [slide](fig_n2_slide.png)); S1
where the signals sit in frequency ([html](fig_s1.html), [png](fig_s1.png)); A1 where mains and drive tones land
([html](fig_a1.html), [png](fig_a1.png)); P1 simulated position from the ripple ([html](fig_p1.html),
[png](fig_p1.png)).

---

## Dense part

### 1. What is on record

| What | Where | What it does | What it lacks |
|---|---|---|---|
| Half firmware, pseudocode | `sws/hw-selection/sws_link_and_readout.md` §3; rendered on the software page by `docs/sws/build_software.py` | Two (or three) ADS131M08 at 500 per second (OSR 8192), one DRDY interrupt reads all, checks the SPI CRC, rails and stuck codes; one frame **per sample** with sample counter, health, boot count, 1 Hz sync latch and fraction, two temperatures, an aux slot; CRC-32C; COBS | **No averaging or decimation** (every converter result is sent; the only averaging is the converter's own filter); no line rate below the converter rate; no frame batching; DC block not mentioned (default off) |
| Frame and link budget | same note §4; `sws/hw-selection/sws_link_budget.py` | 77-byte frame per sample; 192.5 kbit/s at 250, 385 at 500 per second | Batching; two-converter frame at 100 ms (added here) |
| Root box, pseudocode | same note §6 | Receive, CRC, unwrap counters, gaps, 1 Hz edge, time base per half, align two halves, position from an encoder or logged hoist speed, one pass buffered; processing steps as stubs | Position without an encoder or logged speed; moving detection; network-loss buffer; forwarding protocol (MQTT not there); the record puts detection in the box, the owner's newer thought at the logger |
| Sync budget | `sws/hw-selection/sws_sync_budget.py`, `sws_sync_findings.md` | 80 µs residual with a 1 Hz edge; position error terms; "register each run to the first run" to ±4 mm | Assumes the hoist's speed or position is logged; the first installation has neither |
| Traffic arithmetic | `sws/data-path/traffic.py` | Batched 100 ms frames, serial, MQTT, storage | Averaging, filtering, position, run files |
| Rate and pitch scripts | `sws/hw-selection/sws_sampling_chart.py`, `sws_pitch_check.py`, `sws_mux_rate.py` | Rate per mm, pitch rule, multiplexer rates | — |
| Specification §4, §7, §8, §10 | rev130 rendering | 1 mm pitch, 250 per second at 15 m/min; tie sampling to position by encoder or resample in the root box; template from pass 2–3; position from logged hoist speed; root box does detection | Out of date on three converters per half; assumes a logged speed |

No firmware source, no root-box code and no logger code is in the repository. **There is no averaging in the code on
record.**

### 2. Noise against data rate

Bridge: radial 1.0 mV/V/mT (wide-range in-plane TMR), axial 5.0 mV/V/mT (Z-axis TMR), from the candidates note;
supply 3.3 V (specification §7, itself an assumption there). Gains taken so the full scale covers the element's
range (radial 217 mT → 0.72 V; axial 30 mT → 0.50 V): ADS131M08 gain 1 / 2 (±1.2 / ±0.6 V); ADS131E08 gain 2 / 4
(±1.2 / ±0.6 V at its 2.4 V reference).

| Converter rate (per s) | M08 µV rms g1 / g2 (S, Table 7-1) | M08 effective bits g1 / g2 (S, Table 7-2) | M08 radial / axial µT (C) | E08 µV radial g2 / axial g4 (C from S Table 1) | E08 radial / axial µT (C) |
|---|---|---|---|---|---|
| 250 | 1.90 / 1.69 | 20.3 / 19.4 | 0.58 / 0.10 | — | — |
| 500 | 2.39 / 2.13 | 19.9 / 19.1 | 0.72 / 0.13 | — (not native at 2.048 MHz) | — |
| 1 000 | 3.38 / 2.99 | 19.4 / 18.6 | 1.02 / 0.18 | 1.23 / 0.80 | 0.37 / 0.05 |
| 2 000 | 4.25 / 3.91 | 19.1 / 18.2 | 1.29 / 0.24 | 1.75 / 1.14 | 0.53 / 0.07 |
| 4 000 | 5.35 / 4.68 | 18.8 / 18.0 | 1.62 / 0.28 | 2.88 / 1.81 | 0.87 / 0.11 |
| 8 000 | 7.56 / 6.62 | 18.3 / 17.5 | 2.29 / 0.40 | 3.62 / 2.33 | 1.10 / 0.14 |
| 32 000 | 21.31 / 15.26 | 16.8 / 16.3 | 6.46 / 0.92 | 28.1 / 14.4 | 8.5 / 0.87 |

E08 dynamic range in dB, gain 1 / 2 / 4 (S, Table 1): 117.7 / 116.8 / 114.5 at 1 kSPS, 111.4 / 109.4 / 107.4 at
4 kSPS. Its µV are derived with Eq. 2 taking the root-two factor as in the M08 sheet (the text copy read does not
show it; if it is a 2, the E08 figures are 0.71 times these).

**Curve N1, three numbers.** ADS131M08, radial channel: 0.58 µT rms at 250 per second, 1.02 at 1 000, 1.62 at 4 000
(axial 0.10 / 0.18 / 0.28). Against the broken-wire need of 15 µT rms these are 4–11 % (radial), and in quadrature
they add less than 1 % to any other noise of that size.

**Curve N2, averaging.** White-noise rule: averaging n results divides by √n. Averaged to a line rate of 250 the
radial channel would be 0.51 µT (from 1 000), 0.41 µT (from 4 000) — but the sheet's own 250 per second value is
0.58 µT, so below about 0.6 µT the rule is optimistic: a fit noise² = a·rate + b to the sheet's rates gives a floor
of 1.76 µV (0.53 µT radial) that no averaging removes (fit within 15 %). The element's own noise is not on any
wide-range sheet; taking the one figure on file (700 nV/√Hz at 10 Hz, 4.5 mV/V/mT) as one-over-f from 0.01 Hz gives
1.4–1.6 µT rms over line rates 100–1 000 (assumed), above the converter everywhere. So averaging helps until the
converter floor (about 0.5–0.6 µT) and is small against the element. Two cautions: the element figure is taken in field
terms; if instead the bridge's voltage noise stays the same, the radial part (1.0 against 4.5 mV/V/mT) is about 4.5
times noisier, about 7 µT rms, half the broken-wire need, so the radial element's own noise is the first thing to
measure. And the three-tap correction raises white noise by about 1.26 times, not included in N2.

**Against the two needs.** Broken wire: the converter's radial noise is below the need by a factor 26 at 250 per
second, 9.3 at 4 000 and 6.6 at 8 000. Long-loss level, 5 µT (the brief's figure): not a per-sample need but a level
compared with a base trace months earlier; white noise averages away over a 312 mm window and 16 elements (below
0.1 µT), one-over-f noise much less so (on the element assumption above, about 2 µT per element and 0.5 µT over 16
between two runs months apart); what does not average away at all is drift. Converter drift at the element (S, §6.5
/ 7.5): ADS131M08 offset 105–215 nV/K → 0.006–0.013 µT/K axial (0.4–0.85 µT over 65 K), 0.03–0.07 µT/K radial
(2.1–4.2 µT over 65 K); gain drift 10–20 ppm/K including the internal reference × a 5 mT standing residual (the
d-note's assumption) → 3.3–6.5 µT over 65 K, comparable with the 5 µT need. ADS131E08: offset drift 0.65 µV/K →
0.04 µT/K axial, 0.20 µT/K radial (12.8 µT over 65 K, above the need); gain drift 3 ppm/K excluding its reference. A
ratiometric reference from the bridge supply (the link note's proposal) or a temperature table is needed for the
level; it is not a rate question.

**The range that holds.** Converter: any native rate from 1 000 to 4 000 per second gives noise far under the needs
and room for a decimation by 4–16 to the line rate; 250 native (no MCU averaging; the lowest native rate in
high-resolution mode) has the weakest filtering against tones (table below). Line rate: from the lowest rate that
keeps a 10 mm fault at the fastest speed served (samples used as they fall: 80 / 125 / 250 at 5 / 7.5 / 15 m/min;
with interpolation at the logger: 40 / 50 / 100) up to 471 per second (one half at half of 460.8 kbit/s). Inside that range noise does not
decide; what decides is the fastest speed to be served at full fault amplitude, where mains and drive tones land, and
storage (linear in the line rate).

### 3. Averaging that keeps drift and does not smear a fault; the sampling theorem

**Where the signals sit (S1).** Fault (two-lobed pulse, lobes the fault length apart; "highest frequency" = 1 % of
the spectrum's top):

| Speed (m/min) | 10 mm: highest Hz | least rate (theorem) | rate keeping 99 % | factor | 20 mm: highest Hz | least rate | rate keeping 99 % | factor |
|---|---|---|---|---|---|---|---|---|
| 1 | 1.9 | 3.8 | 20 | 5.3 | 0.95 | 1.9 | 10 | 5.3 |
| 5 | 9.5 | 18.9 | 80 | 4.2 | 4.7 | 9.5 | 40 | 4.2 |
| 7.5 | 14.2 | 28.4 | 125 | 4.4 | 7.1 | 14.2 | 80 | 5.6 |
| 15 | 28.4 | 56.8 | 250 | 4.4 | 14.2 | 28.4 | 125 | 4.4 |

"Rate keeping 99 %": the lowest line rate (of those dividing 4 000) at which the three-stage average keeps 99 % of the
peak at the worst sample phase, for both pulse shapes (simulated pulse). The factor of 4–5 over the theorem's least
rate pays for the sample falling beside the peak and for the filter's rounding near its band edge. If the logger
interpolates between samples (possible above the theorem's rate), the sample-phase part is recovered and only the
filter's own loss counts: the three-stage average then keeps 99 % from 40 / 50 / 100 per second and a block average
from 50 / 80 / 160 per second at 5 / 7.5 / 15 m/min for a 10 mm fault (`rate_for_99pct_filter_only` in the JSON).
Which of the two readings applies is the owner's question 1. Strand ripple (pitch 30–60 mm,
assumed): 0.28–0.56 Hz at 1 m/min, 1.4–2.8 at 5, 2.1–4.2 at 7.5, 4.2–8.3 at 15. Long loss (300–1 560 mm): 0.01–0.83
Hz. Drift: hours, near 0 Hz.

**Three filters (S2), from 4 000 per second.** Block average (one average of 4 000/L results), 20-ms mean (a running
mean over one 50 Hz period, then decimated), three-stage average (three block averages, then the correction
[−1/8, 5/4, −1/8]). Peak kept, worst phase, at 125 / 250 per second:

| Fault, speed | Block average | 20-ms mean | Three-stage + correction |
|---|---|---|---|
| 10 mm, 5 m/min | 99.5 / 99.9 % | 98.7 / 99.0 % | 99.6 / 99.9 % |
| 10 mm, 7.5 m/min | 98.8 / 99.7 % | 97.3 / 97.8 % | 99.1 / 99.8 % |
| 20 mm, 5 m/min | 99.9 / 100 % | 99.7 / 99.7 % | 99.9 / 100 % |
| 20 mm, 7.5 m/min | 99.7 / 99.9 % | 99.3 / 99.4 % | 99.8 / 99.9 % |
| 10 mm, 15 m/min | 95.5 / 98.9 % | 90.3 / 91.9 % | 96.4 / 99.1 % |

On the fault alone the block average and the three-stage average differ by under 1 %; they differ on what they let
fold (next table). The 20-ms mean cancels 50 Hz but smears a fast fault whatever the line rate.

**Aliasing of the ripple.** Below a line rate of about 17 per second the ripple at 15 m/min (up to 8.3 Hz) is above
half the line rate and folds (at 10 per second 8.3 Hz lands at 1.7 Hz). From 20 per second up, the ripple is carried
as it is.

**Drift.** Every filter above has a gain of exactly 1 at zero frequency (the taps of each sum to 1; the correction
[−1/8, 5/4, −1/8] sums to 1), so a slow drift passes unchanged and stays visible. A high-pass does the opposite: a
1 560 mm loss passing at 5 m/min keeps on average 53 % of its level through a first-order high-pass at 0.01 Hz and
3 % at 0.1 Hz (at 15 m/min: 80 % and 18 %). The ADS131M08 has such a filter built in, the DC block (Table 8-4,
§8.3.8, corners from 9.7 mHz to 181 Hz at 4 kSPS, scaling with the data rate); it is off by default (DCBLOCK = 0h).

**Rule 1 (rate), proposed.** Line rate ≥ 16 per second for each m/min of the fastest rope speed at which a 10 mm
fault must keep its peak within 1 % with the samples used as they fall (250 per second for 15 m/min), or ≥ 7 per
second per m/min (100 for 15 m/min) if the logger interpolates; the half reaches it by averaging, not by keeping every
n-th converter result.

**Rule 2 (no high-pass in the half or the box), proposed.** Between the element and the logger only filters with a gain of
exactly one at zero frequency: the converter's own filter and the decimation average. No high-pass, no offset or
baseline removal, no auto-zero, the converter's DC block off on every channel (DCBLOCK = 0h), no scaling in the
box. Any removal of drift is done at the logger, on stored raw data, where the long-loss trace is kept beside it.

**The sampling theorem applied to interference.** Where a tone lands after sampling at each rate, folded into 0 … rate/2
(Hz). Mains and harmonics from the grid; 300 / 360 Hz rectifier ripple and 4.1 kHz switching of a large winch drive
are assumed (the drives are not on file):

| Tone | 10 | 20 | 50 | 100 | 250 | 500 | 1 000 per second |
|---|---|---|---|---|---|---|---|
| 50 Hz | **0** | 10 | **0** | 50 | 50 | 50 | 50 |
| 100 Hz (2nd) | 0 | 0 | 0 | **0** | 100 | 100 | 100 |
| 150 Hz (3rd) | 0 | 10 | 0 | 50 | 100 | 150 | 150 |
| 250 Hz (5th) | 0 | 10 | 0 | 50 | **0** | 250 | 250 |
| 60 Hz | 0 | 0 | 10 | 40 | 60 | 60 | 60 |
| 180 Hz (3rd of 60) | 0 | 0 | 20 | 20 | 70 | 180 | 180 |
| 300 Hz ripple (A) | 0 | 0 | 0 | 0 | 50 | 200 | 300 |
| 360 Hz ripple (A) | 0 | 0 | 10 | 40 | 110 | 140 | 360 |
| 4.1 kHz switching (A) | 0 | 0 | 0 | 0 | 100 | 100 | 100 |

At 10 per second 50 Hz lands on 0 Hz: a mains pick-up of constant phase reads as a level step, and mains at 49.9 Hz
lands at 0.1 Hz, a slow wave that looks like drift. How much is left before it folds (amplitude, 1 = all), converter
at 4 000 per second:

| Line rate, tone | keep every n-th result | block average (at 250 the same as the converter run at 250 itself) | three-stage average with correction |
|---|---|---|---|
| 10, 49.9 Hz → 0.1 Hz | 0.999 | 0.002 | < 10⁻⁸ |
| 100, 150 Hz → 50 Hz | 0.993 | 0.21 | 0.014 |
| 100, 360 Hz → 40 Hz | 0.961 | 0.082 | 0.0009 |
| 250, 300 Hz → 50 Hz | 0.973 | 0.15 | 0.004 |
| 250, 360 Hz → 110 Hz | 0.961 | 0.21 | 0.015 |
| 250, 50 Hz (stays 50 Hz) | 0.999 | 0.94 | 0.96 |

**Who removes what.** (a) The converter's own filter (sinc3, with sinc1 above OSR 1024; S, §8.3.7) has nulls at every
multiple of its data rate and removes the modulator's high-frequency noise; between half its data rate and its data
rate it attenuates little (a block average, table above), and it repeats at multiples of the modulator frequency
(4.096 MHz in high-resolution mode), where it removes nothing. (b) The simple RC filter in front of each converter
input must remove what lies near the modulator frequency and above: drive switching harmonics and radio frequency,
which the digital filter cannot see. (c) The decimation in the microcontroller must remove everything between half
the line rate and half the converter rate before it reduces the rate: mains harmonics, drive ripple, vibration;
a three-stage average does this to 0.015 or better in the cases above, a block average only to 0.08–0.21. Mains at
50/60 Hz below half the line rate (at 250 per second) is not folded and stays in the data as a 50/60 Hz tone; it is
removed, if needed, at the logger by a notch, which keeps drift (a notch passes zero frequency). Phase-locking the
converter rate to the mains is not possible with a free-running crystal and is not proposed.

### 4. Position without an encoder

No recorded or simulated trace with strand ripple along the rope is in the repository; the stranded 3D model
(`3d/results/u19_summary.json`) gives the ripple's size over rotation angle (straight lay), not along the rope:
0.21 mT p-p axial at 3 mm at the mid-plane (calculated); the radial ripple there is read-out noise, and the 0.53 mT
p-p radial figure is 4 mm off the mid-plane. It is used here only as an order of size. Figure P1 is therefore **simulated**: a sine ripple of pitch 30 or 60 mm plus white noise, 5 m/min
with ramps, position from the unwrapped ripple phase, the count held while the ripple is gone (moving detection),
one scale factor from the known run length.

| Case (simulated) | Noise / ripple 0.01 | 0.1 | 0.2 | 0.3 |
|---|---|---|---|---|
| Pitch 30 mm, constant | 0.7 mm rms | 3.5 | 11 | 26 |
| Pitch 30 mm, varying 1 % (assumed) | 9.0 | 9.9 | 14 | 26 |
| Pitch 60 mm, varying 1 % | 7.1 | 12 | 40 | 72 |
| Pitch 30 mm, stop in the run, count held | 8.2 | 7.8 | 10 | 21 |
| Same, count not held at the stop | 39 | 337 | 489 | 554 |

Expected noise over ripple on this head: about 1.6 µT rms (axial element, assumed, plus converter) over about
105 µT of ripple amplitude (half the axial 0.21 mT p-p), about 0.015. So the ripple counts rope to about a millimetre per cycle; the error left is the pitch
not being constant along the rope (lay length changing with load and wear), which a single fixed length (out and back
between the same stops, the ramps seen in the data) corrects only on average. Registration of each run to the first
run on the signal itself (specification §8: coarse on the long-loss trace, fine on the ripple and fault signatures,
to ±4 mm) removes the rest; the ripple count gives it a start within about 10 mm, inside its ±15–30 mm capture.

What the half must record: every channel at the line rate, unbroken, with the sample index, the 1 Hz latch and the
temperatures (as now). What the box must record: receive time per frame and the edge times, so the logger can rebuild
one time axis per head. Moving, direction and stops are found at the logger from the data (ripple envelope in the
0.2–20 Hz band; direction from the order in which a feature passes the two halves' or two heads' elements, not tested
here).

What breaks it: a stop or very slow ramp counted without holding (hundreds of mm, table); noise or vibration above
about a fifth of the ripple (cycle slips); a lay-length change along the rope or between loads (scale, removed only
on average by the fixed length); a fault, splice or local loss that distorts the ripple for a few cycles; rope
rotation in the head between runs (the ripple's phase shifts); a sine-shaped ripple is assumed here, the real one has
harmonics and wanders. What an encoder adds on the large installation: speed, direction and stops directly and on the
box clock, a position axis independent of the signal, resampling to a fixed pitch at the logger, and a check on the
ripple count; it does not remove rope strain or slip on the drum, so registration to the first run is still needed.

### 5. The line, as a design draft with alternatives (none selected)

**Frame (proposal), little-endian, before COBS, one per 100 ms.**

| Byte | Field | Notes |
|---|---|---|
| 0 | type / version | 0x11 = averaged sample frame |
| 1 | half id | strap |
| 2–5 | index of the first sample, u32 | at the line rate; wraps after 199 days at 250 per second |
| 6 | samples in this frame, u8 | 25 at 250 per second |
| 7 | rate and filter code, u8 | converter rate, averaging factor, filter id: the logger knows what it reads |
| 8–9 | health, u16 | as the link note |
| 10 | boot count | |
| 11 | sync edges seen | |
| 12–15 | sync latch, u32 | sample index at or before the 1 Hz edge |
| 16–17 | sync fraction, u16 | |
| 18–21 | temperatures, 2 × i16 | carrier, yoke; 0.01 °C |
| 22 | aux slot | |
| 23–24 | aux value | |
| 25 … | 25 × 16 × 3 bytes | channel 0–7 radial, 8–15 axial, 24-bit, as averaged |
| last 4 | CRC-32C | |

Alternatives beside it: one frame per sample (the link note's 77 bytes; 192.5 kbit/s at 250 per second, 56 % more
line); 50 ms frames (12–13 samples; 2.3–2.7 % more line); 20-bit packing (16 % less line; the averaged value has more than
20 meaningful bits only below about 0.5 µT radial, so it loses nothing the needs see — not checked against the axial
range); a 16-bit value (6.6 µT per step on the radial range: coarser than the level need; not proposed).

**Serial.** At 250 per second: 1 235 bytes on the wire per frame, 123.5 kbit/s, 26.8 % of 460.8 kbit/s, 12.4 % of
1 Mbit/s (the earlier unit's 23-byte header gave 123.3). At 125: 63.4 kbit/s. The 100 m case: the assumed cable rule
(length × rate ≤ 10⁸) gives 217 m at 460.8 kbit/s and exactly 100 m at 1 Mbit/s. The serial load does not limit any
line rate up to 471 per second at 460.8 kbit/s with the 50 % margin.

**The 1 Hz edge.** As the record: a dedicated pair from the box, latched by each half (80 µs residual between
halves). Alternatives: a 10 Hz edge (8 µs); the edge as a sync byte's start bit on the box-to-half pair, freeing a pair
(one outside answer in the earlier round). With averaging, a sample is the average over 4 ms (at 250); the latch
refers to the converter result index and the averaging is aligned to the same index in both halves, so both halves'
averages cover the same instants.

**The root box in blocks.** Receive (4 ports; isolated; RS-422/485 parts), check (CRC-32C, sequence and boot count,
half id against the port), stamp (box clock NTP- or PTP-disciplined; receive time per frame; edge times), buffer
(flash ring), forward (MQTT, unchanged frame body plus 9 bytes: receive time and a quality byte), health (per port:
frames, CRC errors, gaps, temperatures, supply; once a second). No scaling, filtering or detection (rule 2).

| Buffer for lost network | 1 h | 24 h |
|---|---|---|
| Box, installation A (2 halves), 100 / 250 per second | 37 / 89 MB | 0.9 / 2.1 GB |
| Box, installation B (4 halves), 100 / 250 per second | 75 / 178 MB | 1.8 / 4.3 GB |

**Box per winch, or one box per SWS (alternative, kept beside it).** On installation A one
winch has one head, so the two are the same. On B one box per head doubles the boxes (102 instead of 51), halves each
box's ports, traffic and buffer (2 halves: the A figures above), and a failed box costs one head, not a winch; it costs
more and its 1 Hz edge serves only one head, so aligning the two heads of a winch would rest on the boxes' clocks
(NTP about 1 ms, PTP better) instead of one common edge.

**MQTT.** Topics (proposal): `sws/<installation>/<winch>/<head>/<half>/raw` (QoS 1, binary: the frame body plus the
box's 9 bytes, ten a second); `sws/…/<half>/health` (once a second, small, readable text); `sws/…/<box>/status`
(retained: online, firmware, configuration). Message rate and traffic: A 120 per second, 1.3 Mbit/s; B 2 040 per
second, 22.2 Mbit/s (at 250 per second). Alternative beside it: one message per box per second carrying all its halves'
ten frames (A 6, B 51 messages per second, about 50 kB each on B), fewer messages for the broker at the cost of one
second more delay, which does not matter here (not a safety system).

**Logging.** Stored: every raw frame as received, with the box time and quality byte; nothing processed is the only
copy. Files per run per head: the logger detects "moving" from the data (strand-ripple envelope in 0.2–20 Hz above
half its running amplitude for 2 s; stopped after 10 s below; 30 s kept before and after), opens a file at the start
and closes it at the stop; a stopped rope gives no files except a slow health record. The first full run of each rope
(both directions, after the record's two conditioning passes) is kept for the rope's life: 33 MB per half per 220 m
pass at 5 m/min at 250 per second, so a few hundred MB per rope.

| Storage | Per half per running hour | A per day, 1 / 4 / 24 h | B per day, 1 / 4 / 24 h | A per year | B per year |
|---|---|---|---|---|---|
| 100 per second | 18.6 MB | 0.22 / 0.90 / 5.4 GB | 3.8 / 15 / 91 GB | 0.08 / 0.33 / 2.0 TB | 1.4 / 5.6 / 33 TB |
| 250 per second | 44.6 MB | 0.53 / 2.1 / 12.8 GB | 9.1 / 36 / 218 GB | 0.20 / 0.78 / 4.7 TB | 3.3 / 13.3 / 80 TB |

Disk, planned half full (margin assumed): keep everything one year at 250 per second: A 0.39 / 1.6 / 9.4 TB, B 6.6 /
27 / 159 TB for 1 / 4 / 24 running hours a day; keep 90 days of everything plus the first runs for life: A 0.10 / 0.39
/ 2.3 TB, B 1.6 / 6.5 / 39 TB. No compression counted; how far a lossless compression shrinks these traces is not
known.

**What to ask the supplier of a commercial process data acquisition system.** (1) Can it subscribe to MQTT and decode
a binary payload of our layout, or must the box send its own format; (2) values per second and channels per licence,
and the price at B's 816 000 values per second at 250 per second (326 400 at 100); (3) does it time-stamp from a time
in the payload or only on arrival; (4) can it open and close files on a condition computed from the data (moving);
(5) storage format, compression, and how files are exported to other tools; (6) retention tiers and archiving; (7)
PTP or NTP, and its clock's accuracy; (8) behaviour when the network returns after hours: does it accept back-filled
data in time order.

### 6. The outside answers

Three outside models answered the blind brief (the owner's facts of today, nothing from this repository); saved
unchanged in [answers/](answers/) after a name scan (0 hits). Read after parts 1–5 were written. Called here by model
family: Opus, Grok, Codex. All three quote converter figures from memory; none had the data sheets.

**Opus, in ten lines.** Converter at 4 kSPS, a 136-tap linear-phase FIR to 250 per second in the microcontroller
(flat to 65 Hz, ≥ 90 dB from 185 Hz); 250 per second is "the floor", because at 100 per second 60 Hz folds to 40 Hz.
Never in the half: offset removal, auto-zero, high-pass, adaptive filters, event-only sending. Sample by time; position
afterwards from the ripple phase (Hilbert or phase-locked tracker on 8 elements), scale from the run length,
direction from the order of phase round the circumference (its own derivation, untested), registration by piecewise
correlation; 0.5–1 mm local, ±5–25 mm after registration. Frame 34-byte header, 1 244 bytes per 100 ms, CRC-32,
COBS, 460.8 kbit/s; the 1 Hz edge as a sync byte on the downlink pair. Box: receive time, a 256 GB spool (30 days),
no filtering or scaling. MQTT one message per half per second (12 / 204 per second), 1.2 / 20 Mbit/s payload. Storage
B 13.3 TB a year at 4 h a day; keep raw 3 years, reference runs for life. Main risk: level drift; it believes the
ADS131M08 has no external reference input and concludes that 0.005 mT is 100 ppm of a 50 mT "full level".

**Grok, in ten lines.** Converter at 1 000 per second, block average of 4 to 250 per second, no high-pass. Noise
table from memory (1.0 µV at 250 to 14 µV at 32 000). Frequencies as speed / length (12.5 Hz for 10 mm at 7.5 m/min).
Frame 1 624 bytes per 100 ms with 4-byte values and an 8-byte time from the half; 1 Mbit/s preferred, one line per
half; 1 Hz edge kept. Box: CRC, time, buffer 24 h (5.5 GB per B winch), MQTT per half 16 kB/s, alternative raw TCP
or ZeroMQ. Always stream, also standing still; store 6 h a day or always-on (282 GB a day for B). Position: ripple
phase 1–5 mm if the pitch is stable, plus fixed length and registration. Tests: fault at 5 and 7.5 m/min, drift
≤ 0.005 mT over 1 h after temperature correction, ripple encoder ≤ 1 % of length.

**Codex, in ten lines.** Converter at 1 000 per second, block average of 4 to 250 per second; noise from memory
(1.2 µV at 250, 4.7 at 4 000). Frequencies as speed / length. "Belongs in the half: per-channel gain and offset
trim." Position: ripple phase with pitch estimate, constrained by fixed length; 0.5–2 % of the length travelled
unless constrained. Frame 32-byte header (with an 8-byte time from the half) plus a 4-byte check, 1 236 bytes; 123.6 kbit/s at 250 per
second; one line per half. Box spool 72 h (12.8 GB for a B winch); MQTT per half, ten per second; alternative NATS
JetStream. Storage at 2 h a day, 330 days: A 0.35 TB, B 6.0 TB a year. Fault loss model sinc(f·T) with f = speed /
length: 2.5 % for 10 mm at 7.5 m/min at 100 per second.

**Where they agree, differ, and differ from the numbers here by more than 10 %.**

| Item | Here | Opus | Grok | Codex | Agree? / who is right |
|---|---|---|---|---|---|
| Line rate | 80 / 125 / 250 per second at 5 / 7.5 / 15 m/min (rule 1) | 250 floor | 250 | 250 | All four at 250 for the brief; here the rate follows the speed |
| Converter rate | 1 000–4 000 | 4 000 | 1 000 | 1 000 | Range; not resolved |
| Decimation filter | three-stage average + correction | 136-tap FIR | block of 4 | block of 4 | Differ: a block average lets 8–21 % of 150–360 Hz tones fold at 100–250 per second (tone table); a proper filter 0.06–1 % |
| No high-pass, no offset removal in the half | rule 2 | yes | yes | yes, but "gain and offset trim" in the half | Codex's offset trim breaks rule 2 if it is applied to the data; harmless only if sent as constants |
| M08 noise, 250 per second, gain 1 | 1.90 µV (sheet) | 1.5 (−21 %) | 1.0 (−47 %) | 1.2 (−37 %) | Sheet, Table 7-1; all three low |
| M08 noise, 1 000 | 3.38 (sheet) | 3.0 (−11 %) | 1.8 (−47 %) | 2.4 (−29 %) | Sheet |
| M08 noise, 4 000 | 5.35 (sheet) | 6.0 (+12 %) | 3.6 (−33 %) | 4.7 (−12 %) | Sheet |
| M08 external reference | yes, REFIN 1.1–1.3 V (sheet 8.3.4; link note) | "no external reference pin" | assumes ratiometric is possible | — | Sheet: Opus wrong |
| Fault peak lost, 10 mm, 7.5 m/min, 100 per second | 0.36 % filter only, 1.4 % worst sample phase (Gaussian pulse, block average); 0.5 / 1.9 % two-lobed | 0.36 % | 3 % | 2.5 % | Opus right for the filter alone (identical figure); the extra loss of sample phase is recoverable by interpolation at the logger (Opus's point), so 0.36 % is the filter's share. Codex and Grok treat the pulse as a tone at speed / length: 2–8 × too high |
| Frame per 100 ms, 250 per second | 1 229 bytes body, 1 235 on the wire | 1 244 on the wire | 1 624 (4-byte values) | 1 236 body | Within 10 % except Grok (+32 %, its 4-byte values) |
| Serial, one half, 250 per second | 123.5 kbit/s | 124.4 | 134; 269 "design load" | 123.6 | Within 10 %; Grok's ×2 is its margin, not a load |
| MQTT, B | 22.2 Mbit/s on the wire | 20 payload (−10 %) | 26 (+19 %) | 20.2 payload (−9 %) | Payload against wire: both right; Grok's 4-byte values |
| Box buffer, B, 24 h | 4.3 GB | 4.3 per day | 5.5 (+29 %) | 4.27 per day (12.8 for 72 h) | Same arithmetic; Grok's 4-byte values |
| Box buffer length | 1 h and 24 h computed | 30 days | 24 h | 72 h | Not resolved: a choice |
| Storage B, 250, 4 h a day | 13.3 TB a year | 13.3 | — (6 h: 70 GB a day, +28 % on the same hours) | — (2 h, 330 days: 6.0, same arithmetic) | Agree except Grok's value width |
| Storage B always-on | 218 GB a day | — | 282 (+29 %) | — | Grok's 4-byte values |
| Position without encoder | 0.7 mm (steady pitch) to 9 mm (pitch varying 1 %), simulated; then registration ±4 mm | 0.5–1 mm local; ±5–25 mm registered | 1–5 mm with stable pitch | 0.5–2 % of length | Codex's 0.5–2 % is its unconstrained figure; it forces the end point with the fixed length but gives no constrained number; agree at the local scale |
| 1 Hz edge | own pair (record) | sync byte on the downlink | own pair | own pair | Not resolved |
| Time stamp in the half | sample index + latch | sample index + latch | 8-byte UTC time | 8-byte time | Differ: a clock time in the half needs the half to know the time; the index + latch does not |
| Standing still | send; files only while moving; slow health | send always; 1 per second summary when idle | always on | keep moving windows | Differ on what is stored when idle |
| Level drift | gain drift × residual 3.3–6.5 µT over 65 K; magnet temperature larger | 100 ppm of "50 mT" | ≤ 0.005 mT after correction | — | Opus's conclusion (temperature model, relative level) agrees; its base does not: the element at the zero sees a small standing field, so the converter's gain drift acts on a few mT, not 50 |

**The disagreements, for the owner (not resolved here).**

1. Decimation filter: a plain block average (Grok, Codex) or a proper decimation filter (Opus's FIR, the three-stage
   average here).
2. Converter rate: 1 000 (Grok, Codex) or 4 000 per second (Opus); here anything from 1 000 to 4 000.
3. Line rate fixed at 250 (all three) or set by the fastest speed to be served (rule 1 here).
4. Offset or gain trim in the half (Codex) or nothing that alters the data in the half (Opus, Grok, rule 2).
5. Clock time in the half (Grok, Codex) or sample index and edge latch only (Opus, here, the record).
6. The 1 Hz edge on its own pair or as a byte on the downlink (Opus).
7. Box buffer: 24 h (Grok), 72 h (Codex), 30 days (Opus).
8. Idle data: everything always (Grok), a 1 per second summary (Opus), only moving windows (Codex, here).
9. Direction without an encoder: from the order of phase round the circumference (Opus, untested), from the ripple
   phase slope (Grok), or not addressed (Codex).
10. MQTT one message per half per 100 ms (Grok, Codex, here) or per second (Opus); alternatives: file transfer
    (Opus), raw TCP or ZeroMQ (Grok), NATS JetStream (Codex).

### Assumptions (all in `line_calc.py`)

Bridge sensitivities and ranges from the candidates note; 3.3 V supply; the element noise (one TMR figure on file,
one-over-f); the fault shape (two-lobed or single pulse with the fault length as its width); the 1 % spectrum point as
"highest frequency"; the 99 % aim; strand pitch 30–60 mm; a sine ripple; a 1 % slow pitch variation; 5 s ramps; mains
harmonics and drive tones; the header layout; 9 bytes added by the box; 50 % disk fill; the cable rule from memory;
installation A 12 halves, B 204.

### Questions for the owner, in order

1. What is the fastest rope speed at which a fault must keep its full peak — 5, 7.5 or 15 m/min — and will the logger
   interpolate between samples? Together they set the line rate (80 / 125 / 250 per second used as they fall; 40 / 50 /
   100 with interpolation) and the storage in proportion.
2. How many running hours a day, and how long must everything be kept (beyond the first run of each rope)? It sets the
   disk from under 1 TB to about 160 TB.
3. Should the half average to the line rate (rule 1, a change to the pseudocode on record), and is the three-stage
   average the filter to write, or a plain block average?
4. Which commercial logging system is in place on the first installation, and can it take a binary MQTT payload?
5. One root box per winch or per head on installation B?
6. Can the first installation give a reference length (two marks, or the known travel between the end stops) for the
   ripple count's scale?
7. Is the drive on the first installation known (rectifier and switching frequency), to check the tone table?

### Not done

No measurement of anything; no recorded ripple trace (P1 is simulated); the element noise of the parts; the
ADS131E08 noise equation's factor; the cable rule; lossless compression ratio; direction detection from the data;
the firmware itself; the logger's real formats.

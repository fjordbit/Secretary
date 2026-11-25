# Where older sources disagree with the fixed facts

## In short

- This list compares the older sources with the fact page [dt_facts.md](dt_facts.md) (facts F01–F47).
- 34 rows: 25 are **(a)** out of date, 9 are **(b)** open points that need a ruling.
- Every (a) row has the exact change that would correct it, further down. **None of these changes is
  applied**; no existing file is changed by this unit.
- The (b) rows are not settled here; both sides are shown.

**(a)** = out of date against a ruling, or wrong against the file's own stated source; one correction follows.
**(b)** = two sources disagree and nothing on record settles it; it needs a ruling.

Paths are repository paths under `max/`. "Line" is the line in the file at the base of this branch. A file that
is generated (the chart json, the 3D scene json, the rendered pages) is corrected in its generator and rebuilt;
the generated copy is named so that it is not missed. The specification's master is the .docx; its rows below
cite the rendered Markdown of rev131 and are corrected by a redline or a new revision.

## The list

| # | File and line | What it says | What the fact page says | Kind |
|---|---|---|---|---|
| D01 | `sws/parts_table/parts.yaml` l.1330 (V01); built into `docs/sws/results.html` l.190 | 250 values per second per channel: "proposal, not agreed" | F13: 250 per second per channel in the product, given as fixed | (a) |
| D02 | `sws/parts_table/parts.yaml` l.234–238 (R18) | Rope length "on record, several values" (≤ 220 m and 250 m), no conflict line | F31: 250 m fixed travel, ruled (I01) | (a) |
| D03 | `sws/parts_table/parts.yaml` l.220–224 (R17) | Rope speed "on record, several values" (3 / 15 and 3.2 / 5 m/min), no conflict line | F32: 3.2 m/min, 5 m/min fast test, 15 m/min the specification's extreme, ruled (I02) | (a) |
| D04 | `flow/examples-0.2-draft/make_sws_shiplift.py` l.36–39, l.266–268; generated `sws-shiplift.chart.json` l.6–22 | Scale card: "~250" SWS sensors, "~125" winches, "~42" base stations | F03, F04: 3 main stations, 51 winches, 102 SWS | (a) |
| D05 | `studio/tests/kernel.test.js` l.217 | The test asserts "~250 SWS sensors", "~125 winches", "~42 base stations" | as D04 | (a) |
| D06 | `studio/modules/sws/profile.js` l.83 | "real scale ~250 SWS, estimate" | F04: 102 SWS | (a) |
| D07 | `flow/examples-0.2-draft/make_sws_shiplift.py` l.164, l.179; `studio/modules/sws/profile.js` l.79; `studio/modules/sws/view3d.js` l.23; `studio/modules/sws/szoom.js` l.4; `twin/geometry/shiplift-layout.demo.yaml` l.32; `twin/model/README.md` l.38; generated `studio/modules/sws/scene3d.demo.json` l.279 | Level "base station" with about 3 winches each, "of ~42" | F02, F03: 3 main stations × 17 winches. The chart keeps an open item on whether its base station is the main station (MCC) or something else (`make_sws_shiplift.py` l.232–236); the twin page maps MCC to "Main station" (`flow-line-language.html` l.660). The counts are corrected in D04; the name is not settled here | (b) |
| D08 | `flow/examples-0.2-draft/make_sws_shiplift.py` l.225–227 (open item `sws_per_hoist`) | SWS per winch open: 2 against one per hoist (functional specification) | F04: one rope per winch, two SWS per rope, ruled | (a) |
| D09 | `flow/examples-0.2-draft/make_sws_shiplift.py` l.240–242 (open item `counts`) | Scale open: about 250 SWS, ~125 winches, ~42 base stations; 102 hoists with one SWS each (functional specification); 200 SWS (twin architecture); 200 priced (specification) | F03, F04 | (a) |
| D10 | `flow/examples-0.2-draft/make_sws_shiplift.py` l.98 (and its docstring l.11–13, l.92); generated chart json (480 lines name it) | Each half has an "excitation" channel (an input for the bridge supply) | F10: two converters, no input for the supply. ("3 x" converters is no longer in the script: l.109 reads "2 x ADS131M08 [rev131]".) | (a) |
| D11 | `flow/examples-0.2-draft/make_sws_shiplift.py` l.96–97 | Channel labels "TMR radial, spoke i", "TMR axial, spoke i" | F01: sensing element; F09: spoke layout not settled (D01 in the parts table says nothing is to be built on it) | (a) |
| D12 | `twin/Shiplift-twin-analysis/docs/architecture.html` l.120, l.291, l.315 | "SWS × ~200"; "200 SWS are one type and 200 instances"; worked example 16 channels × 100 Hz × 200 SWS = 320 000 values/s | F04: 102 SWS; F12: 32 channels per SWS; F13: 250 per second; F15: 816 000 values/s. The page calls it a worked example; its 200 may come from the series quantity (D33) | (a) |
| D13 | branch `u10-twin-design`, `max/twin/Shiplift-twin-analysis/docs/architecture.html` l.315 | 24 channels × 100 Hz × 200 SWS = 480 000 values/s (main already reads 16) | as D12 | (a) |
| D14 | `twin/Shiplift-twin-analysis/docs/flow-line-language.html` l.613, l.655 | "reduce 100 Hz → tick"; "Raw 100 Hz is stored in full" | F13: 250 per second | (a) |
| D15 | `twin/Shiplift-twin-analysis/docs/architecture.html` l.568; `decision-log.md` l.200; `flow-line-language.html` l.312, l.445; `twin/DESIGN.md` l.73 | Open: are SWS 1 and SWS 2 the left and right rope of a hoist; drawn as "SWS 1 · L", "SWS 2 · R" | F04: one rope per winch, two SWS on that rope | (a) |
| D16 | `twin/Shiplift-twin-analysis/docs/flow-line-language.html` l.283, l.311, code l.426 and l.480; `decision-log.md` l.199 | 17 hoists per side, two sides, 6 / 6 / 5 per main station (MCC) | F03: 3 main stations × 17 winches = 51 | (a) |
| D17 | `twin/Shiplift-twin-analysis/docs/flow-line-language.html` l.660 | Labels: SWS shown as "Sensor", half as "Sampling unit" | F01: names | (a) |
| D18 | `twin/Shiplift-twin-analysis/docs/architecture.html` l.332 | Rope position from the drum angle via the control system's data, fused in a Kalman filter | F34: proximity sensors at the ends of the travel and the SWS's own data, no encoder; F30: no control-system link on the first installation | (a) |
| D19 | `sws/spec/rendered/…rev131.md` l.149, l.151, l.363, l.413, l.465 | Sampling tied to an encoder or a drum encoder count in the root box; position from logged hoist speed; "the root box adds position (encoder count from the network)"; open item "drum encoder resolution"; l.413 also lists an "excitation" value in the frame | F34: no encoder, position from the proximity sensors and the SWS's own data; F10: no supply input | (a) |
| D20 | `sws/spec/rendered/…rev131.md` l.21, l.122, l.128, l.130, l.133, l.354, l.415, l.454 | Rope length ≤ 220 m; pass time and sample count for 220 m | F31: 250 m | (a) |
| D21 | `sws/spec/rendered/…rev131.md` l.126 | Normal speed ≤ 3 m/min (0.05 m/s) | F32: 3.2 m/min at the drum; 5 m/min fast test case (15 m/min on l.127 stays as the extreme) | (a) |
| D22 | `sws/transmitter/transmitter_line.md` l.19 | "at the normal 5 m/min" | F32: 3.2 m/min normal, 5 m/min the fast test case | (a) |
| D23 | `sws/transmitter/transmitter_line.md` l.381–382 | First run kept for life: "33 MB per half per 220 m pass at 5 m/min" | F31: 250 m | (a) |
| D24 | `sws/data-path/data_path.md` l.30–31, l.50, l.172–173 | Where rope position comes from is open and must be answered first | F34, ruled | (a) |
| D25 | `sws/line_beta/settings.toml` l.130; `sws/line_beta/README.md` l.73; `sws/parts_table/parts.yaml` l.1333 | 125 per second is an alternative line rate | A 100 ms frame holds 125 × 0.1 = 12.5 samples, not a whole number; `sws/line_beta/linebeta/settings.py` l.54–57 raises on it. F16: frame every 100 ms | (a) |
| D26 | `sws/line_beta/settings.toml` l.148–150; `sws/line_beta/README.md` l.79; `sws/parts_table/parts.yaml` l.1708 | Buffer 24 h with a cap of 4 096 MB | The cap holds less than 24 h on a box of four halves: 21.8 h by the code's own count, 22.6 h by the measured rate, 23.0 h by `sws/transmitter/line_calc.py` (arithmetic below). Which count of 24 h the cap should follow is not settled | (b) |
| D27 | `sws/spec/rendered/…rev131.md` l.408, l.415 against `sws/data-path/data_path.md` l.47, `sws/transmitter/transmitter_line.md` l.57, parts.yaml X01 | Processing (position tagging, template, detection) in the root box, against all processing at the logger | F39: two values on record | (b) |
| D28 | `twin/Shiplift-twin-analysis/docs/architecture.html` l.121, l.326–327 against `sws/spec/rendered/…rev131.md` l.413, l.419 and `sws/transmitter/transmitter_line.md` l.355, l.457 | The SWS stamps each block at sampling from SNTP in its firmware, against: the half sends a sample index and a latched count, the root box stamps and maps to one time base | F38: two values on record. The specification adds that the halves are on serial lines, not Ethernet (l.419) | (b) |
| D29 | `flow/examples-0.2-draft/make_sws_shiplift.py` l.184 against `sws/spec/rendered/…rev131.md` l.402 and `sws/transmitter/transmitter_line.md` l.50, l.364 | One SWS data publisher per base station (about 3 winches) against one root box per hoist (winch), or per head as the alternative | F23: one per winch on record, per head named as the alternative; not ruled | (b) |
| D30 | `flow/examples-0.2-draft/make_sws_shiplift.py` l.29–31 | Drawn layout 2 base stations × 3 winches × 2 SWS | F03, F04: 3 × 17 × 2. Whether the chart draws all 51 winches or keeps a smaller drawn layout under a corrected scale card is a choice (the json is about 38 000 lines for 6 winches) | (b) |
| D31 | `sws/spec/rendered/…rev131.md` l.346 and parts.yaml T01 against `sws/transmitter/transmitter_line.md` l.332 and `sws/line_beta/settings.toml` l.102 | Temperature 0.5 °C resolution, against temperatures carried in steps of 0.01 °C | F18: two values on record. They may be different quantities (the part's resolution and the frame field's step); which one the twin uses is not stated | (b) |
| D32 | `sws/line_beta/settings.toml` l.70–72 against `sws/3d/p52/design.md` l.399–401 | Gap factors at 0 / 1 / 2 / 3 / 10 mm = 0.2 / 0.70 / 1.0 / 1.15 / 1.96 (0 and 3 mm assumed); the 3D record gives 1.89 / 2.70 / 3.74 / 5.29 mT at 1 / 2 / 4 / 10 mm for two hidden wires | Ratios from the record: 1.89 / 2.70 = 0.70, 3.74 / 2.70 = 1.385, 5.29 / 2.70 = 1.96. The 4 mm point is on record and not used; its 1.385 sits above the assumed 1.15 at 3 mm (straight line between 2 and 4 mm: (1.0 + 1.385) / 2 = 1.19). The factors are from two hidden wires and are applied to one outer wire (1.35 mT, l.67) | (b) |
| D33 | `docs/sws/build_hardware.py` l.276 (parts.yaml H09) | About 200 heads (400 halves) over the series | F04, F05: 102 + 6 = 108 SWS on the two named installations; possibly the origin of the twin's "~200" (D12) | (b) |
| D34 | `sws/parts_table/parts.yaml` l.1814 (I01 `conflict`) | Names `transmitter_line.md` l.115 as out of date on rope position | On reading, l.115 describes what the older pseudocode lacks ("Position without an encoder or logged speed"); it is not itself out of date. The data-path lines it names are (D24) | (a) |

Counts: 34 rows; (a) 25 — D01–D06, D08–D25, D34; (b) 9 — D07, D26–D33.

## Corrections for the (a) rows (not applied)

Each item: file, line, old text → new text. Where a line holds a name or a date, the old text is given as a
fragment that leaves it out, or the line is named and replaced whole.

**D01** `sws/parts_table/parts.yaml`
- l.1330 `  status: proposal, not agreed` → `  status: ruled by the owner`
- l.1331 `line: Line rate — 250 values per second per channel proposed (R17 speed sets it); 500 preferred in the specification (V01)` → remove the line (a ruled row is not in the summary lists)
- after l.1332 `  values:` add a first value: `    - value: 250 per second per channel in the product` / `      source: "outside: given as fixed, not yet in a project document"`
- then `render.py --check`, `render.py`, and rebuild `docs/sws/results.html` (its l.190 "proposal, not agreed" follows).

**D02** `sws/parts_table/parts.yaml`, after l.238 add:
`  conflict: "Rope length — 250 m fixed travel is ruled (I01); the specification's ≤ 220 m is out of date (R18)"`

**D03** `sws/parts_table/parts.yaml`, after l.224 add:
`  conflict: "Rope speed — 3.2 m/min at the drum, 5 m/min fast test case, 15 m/min the specification's extreme are ruled (I02); the specification's normal ≤ 3 m/min is out of date (R17)"`

**D04** `flow/examples-0.2-draft/make_sws_shiplift.py` (then run it to rebuild the json)
- l.36 `SWS_TOTAL_EST = 250` → `SWS_TOTAL_EST = 102   # ruled: 51 winches x 2 SWS (parts table I03)`
- l.37 `WINCHES_PER_BS = 3` → `WINCHES_PER_BS = 17   # ruled: 17 winches per main station`
- l.38 `# ~125` → `# 51 = 102 / 2`; l.39 `# ~42` → `# 3 = 51 / 17`
- l.266, the whole line from `{"what": "SWS sensors"` to `"open": "counts"},` → `{"what": "SWS", "value": f"{SWS_TOTAL_EST}", "basis": "ruled (parts table I03)"},`
- l.267 `{"what": "winches", "value": f"~{WINCH_EST}", "basis": f"derived: {SWS_PER_WINCH} SWS per winch", "open": "sws_per_hoist"},` → `{"what": "winches", "value": f"{WINCH_EST}", "basis": "ruled: 3 main stations x 17, one rope each"},`
- l.268 `"value": f"~{BS_EST}", "basis": f"derived: ~{WINCHES_PER_BS} winches per base station"` → `"value": f"{BS_EST}", "basis": "ruled: 3 main stations x 17 winches"` (the label "base stations" and the open item `base_station_vs_mcc` stay: whether the chart's base station is the main station is D07)
- l.164 `f"Winch {n} of ~{WINCHES_PER_BS} (hoist)"` → `f"Winch {n} of {WINCHES_PER_BS} (hoist)"`; l.179 `of ~{BS_EST}` → `of {BS_EST}`

**D05** `studio/tests/kernel.test.js` l.217
`!/~250 SWS sensors/.test(txt) || !/~125 winches/.test(txt) || !/~42 base stations/.test(txt)` → `!/102 SWS/.test(txt) || !/51 winches/.test(txt) || !/3 main stations/.test(txt)`

**D06** `studio/modules/sws/profile.js` l.83 `(real scale ~250 SWS, estimate)` → `(real scale 102 SWS on 51 winches)`

**D08** `flow/examples-0.2-draft/make_sws_shiplift.py` l.225–227: delete the open item `sws_per_hoist` (ruled: one rope per winch, two SWS per rope). Its reference on l.267 goes with D04.

**D09** same file l.240–242: delete the open item `counts`. Its reference on l.266 goes with D04.

**D10** same file
- l.98 `chans += [("excitation", "V", "bridge excitation (ratiometric)"), ("temp_carrier", "°C", "temperature, TMR carrier"),` → `chans += [("temp_carrier", "°C", "temperature, carrier (digital part)"),`
- l.92 `16 TMR + excitation + temperatures [rev127]` → `16 sensing elements + digital temperatures [rev131]`
- l.12 `§7 (excitation channel; temperature on the carrier,` → `§7 (temperature on the carrier,`
- rerun the script; the json's 480 "excitation" lines go.

**D11** same file
- l.96 `f"TMR radial, spoke {i}"` → `f"radial sensing element, position {i}"`
- l.97 `f"TMR axial, spoke {i}"` → `f"axial sensing element, position {i}"`

**D12** `twin/Shiplift-twin-analysis/docs/architecture.html`
- l.120 `SWS × ~200` → `SWS × 102`
- l.291 `200 SWS are one type and 200 instances` → `102 SWS are one type and 102 instances`
- l.315 `16 channels × 100 Hz × 200 SWS is 320 000 values/s. One row per value drowns PostgreSQL; one-second blocks give 3 200 rows/s. Continuous i16 storage is about 55 GB per day uncompressed` → `32 channels × 250 per second × 102 SWS is 816 000 values/s. One row per value drowns PostgreSQL; one-second blocks give 3 264 rows/s. Continuous i16 storage is about 141 GB per day uncompressed`
  (arithmetic: 102 × 32 × 250 = 816 000; one block per channel per second: 102 × 32 = 3 264; 816 000 × 2 bytes × 86 400 s = 141.0 × 10⁹ bytes. The page's own check: 320 000 × 2 × 86 400 = 55.3 × 10⁹. As raw 24-bit frames the record gives about 216 GB, parts.yaml O04.)

**D13** branch `u10-twin-design`, `max/twin/Shiplift-twin-analysis/docs/architecture.html` l.315: `24 channels × 100 Hz × 200 SWS is 480 000 values/s. One row per value drowns PostgreSQL; one-second blocks give 4 800 rows/s. Continuous i16 storage is about 83 GB per day uncompressed` → the new text of D12. (Main already carries the 16-channel text; this is a branch copy.)

**D14** `twin/Shiplift-twin-analysis/docs/flow-line-language.html`
- l.613 `reduce 100 Hz → tick` → `reduce 250 per second → tick`
- l.655 `Raw 100 Hz is stored in full.` → `Raw 250 per second is stored in full.`

**D15**
- `architecture.html` l.568 `Hoists per side for each lift, hoist-to-MCC grouping, and whether SWS 1 and 2 are the left and right rope of every hoist.` → `Hoists per side for each lift and hoist-to-MCC grouping. (SWS 1 and 2 sit on the one rope of each winch: ruled.)`
- `decision-log.md` l.200 `- Whether SWS 1 and SWS 2 are the left and right rope of a hoist, and whether every hoist has both.` → delete; add under the decided items: `- **Decided:** One rope per winch; SWS 1 and SWS 2 both sit on it (ruled).`
- `flow-line-language.html` l.312: delete the list item `Are SWS 1 and SWS 2 the left and right rope of a hoist, and does every hoist get both?`
- `flow-line-language.html` l.445 `swsNode('sws1','SWS 1 · L'), swsNode('sws2','SWS 2 · R')` → `swsNode('sws1','SWS 1'), swsNode('sws2','SWS 2')`
- `twin/DESIGN.md` l.73 `` - `[OPEN]` SWS 1/2 per rope.`` → delete.

**D16** `twin/Shiplift-twin-analysis/docs/flow-line-language.html`
- l.283 `Counts use the placeholder layout of 17 hoists per side and 2 SWS per hoist.` → `Counts: 3 main stations × 17 winches, one rope per winch, 2 SWS per rope (ruled).`
- l.311: delete the list item `Hoist count per side for each lift, and which hoists sit on which MCC. This page uses 17 per side and 6 / 6 / 5 per MCC as placeholders.`
- `decision-log.md` l.199 `- The hoist count per side for each lift, and the hoist-to-MCC grouping. The flow line language page uses 17 per side and 6/6/5 as placeholders.` → delete; add `- **Decided:** 3 main stations × 17 winches = 51 on the large installation (ruled).`
- code: l.426 `var HOISTS = 17;` and l.480 `function mccOf(h){ return h <= 6 ? 1 : (h <= 12 ? 2 : 3); }` build two sides of 17 with three main stations each. A tree of 3 main stations × 17 winches is a change to the page's tree builder (l.426–485), not a one-line edit; it belongs to the unit that rebuilds the views.

**D17** `flow-line-language.html` l.660 `sws:'Sensor', unit:'Sampling unit'` → `sws:'SWS', unit:'Half'`

**D18** `architecture.html` l.332 `drum angle (via iba), drum and layer geometry, the sensor's offset along the rope and stretch under load, fused in a Kalman filter.` → `the proximity sensors at each end of the fixed travel and the SWS's own data (strand ripple, with the known ramp, top speed and travel); no encoder, and no control-system link on the first installation.`

**D19** `sws/spec/rendered/SWS_HW_Design_Input_Specification_rev131.md` (via a redline of the .docx)
- l.149 `Sampling should be tied to rope position, not to time: either trigger the ADC from the hoist encoder (one sample per fixed rope increment) or sample at a fixed rate and resample onto a position axis in the root box using the drum encoder count received over the network.` → `Sampling is at a fixed rate. There is no encoder: position comes from proximity sensors at each end of the fixed travel and from the SWS's own data (strand ripple, with the known ramp, top speed and travel), and the samples are placed on a position axis from it.`
- l.151 `the rope's position reference (drum encoder resolution, rope-on-drum slip estimate)` → `the rope's position reference (proximity sensors at each end of the travel; the SWS's own data)`
- l.363 `No encoder is needed on the SWS in revision 1 if the installation's control system logs hoist speed or position with run and direction; time × nominal speed alone is rejected because an unseen stop gives an unbounded error. Position is the integral of logged hoist speed (or logged position), timestamped against the root-box clock, which is NTP-aligned to the logger (1 ms → 0.25 mm at 15 m/min).` → `There is no encoder, and the first installation has no link to the control system. Position comes from proximity sensors at each end of the fixed travel and from the SWS's own data: the strand ripple, with the known ramp time, top speed and travel length used to pick out one complete run.`
- l.413 `Sample index, 16 channel values, excitation, temperatures, status/CRC; the root box adds position (encoder count from the network) and timestamp` → `Sample index, 16 channel values, temperatures, status/CRC; the root box adds a timestamp` (who stamps is D28)
- l.465 `- ☐ Rope position source: drum encoder resolution, how the count reaches the root box, acceptable slip` → delete (ruled).
- l.419 keeps a quadrature counter input on the root box as a hardware hook "even if unused"; that does not contradict F34 and is not changed.

**D20** same file
- l.21 `Each sensor measures a rope section of up to 220 m that is hoisted and lowered repeatedly past the same sensor position.` → `Each SWS measures the rope over the fixed travel of 250 m, which is hoisted and lowered repeatedly past the same SWS.`
- l.122 `the 220 m rope length sets memory and pass duration` → `the 250 m rope length sets memory and pass duration`
- l.128 `| Rope length measured by one sensor | ≤ 220 m | [input] |` → `| Rope length measured by one SWS | 250 m (fixed travel) | [input] |`
- l.130 `| Pass time for 220 m | 14.7 min at 15 m/min, 73 min at 3 m/min | [est.] |` → `| Pass time for 250 m | 16.7 min at 15 m/min, 78.1 min at 3.2 m/min | [est.] |` (250 / 15 = 16.7; 250 / 3.2 = 78.1)
- l.133 `| Samples per 220 m pass per channel | 220 000 at 1 mm pitch | [est.] |` → `| Samples per 250 m pass per channel | 250 000 at 1 mm pitch | [est.] |`
- l.354 `the same 220 m passes the same sensor` → `the same 250 m passes the same SWS`
- l.415 `buffering of at least one full 220 m pass per half` → `buffering of at least one full 250 m pass per half`
- l.454 `then a full 220 m pass at normal speed` → `then a full 250 m pass at normal speed`

**D21** same file l.126 `| Rope speed, normal | ≤ 3 m/min (0.05 m/s) | [input] |` → `| Rope speed, normal | 3.2 m/min at the drum (0.053 m/s); 5 m/min fast test case | [input] |` (3.2 / 60 = 0.053 m/s)

**D22** `sws/transmitter/transmitter_line.md` l.19 `at the normal 5 m/min it is about 19 per second.` → `at the 5 m/min fast test case it is about 19 per second.`

**D23** `sws/transmitter/transmitter_line.md` l.381–382 `33 MB per half per 220 m` / `pass at 5 m/min` → `37 MB per half per 250 m` / `pass at 5 m/min` (250 m / 5 m/min = 50 min; 44.6 MB per hour × 50 / 60 = 37.2 MB; the old figure: 220 / 5 = 44 min, 44.6 × 44 / 60 = 32.7 MB)

**D24** `sws/data-path/data_path.md`
- l.30–31 `8. The owner must first answer where rope position comes from and whether it is logged on the same clock, and` / `then what the site's logging system can take.` → `8. Rope position comes from proximity sensors at each end of the travel and from the SWS's own data (ruled);` / `   what the site's logging system can take is still to be answered.`
- l.50, last cell `Yes, open` → `Answered: no encoder; proximity sensors at each end of the travel and the SWS's own data (ruled)`
- l.172–173 question 1 (`1. Where does rope position come from on installations A and B, …`): delete and renumber 2–7 as 1–6.

**D25**
- `sws/line_beta/settings.toml` l.130 `line_rate_per_s_alternatives = [80, 100, 125, 250]` → `line_rate_per_s_alternatives = [80, 100, 250]`
- `sws/line_beta/README.md` l.73 `| 250 | 80, 100, 125 |` → `| 250 | 80, 100 |`
- `sws/parts_table/parts.yaml` l.1333 `(alternatives 80, 100, 125)` → `(alternatives 80, 100)` (its quote on l.1336 is unchanged)

**D34** `sws/parts_table/parts.yaml` l.1814, in the `conflict` text: ` and the transmitter-line note (branch u109-transmitter-line, transmitter_line.md l.115)` → delete (l.115 describes what the older pseudocode lacks and is not out of date; the data-path lines stay named). On l.1830 `The two notes cited first are out of date` → `The data-path note is out of date`.

## The arithmetic behind D26 (a (b) row; no correction given)

The box caps its spool at min(`buffer_max_MB`, bytes per hour × `buffer_length_h`)
(`sws/line_beta/linebeta/root_box.py` l.136); bytes per hour = halves × (1 229 + 9 + 64) bytes / 0.1 s × 3 600
(l.150–154). For four halves: 4 × 1 302 × 10 × 3 600 = 187.5 MB per hour, so 24 h = 4 500 MB and the cap of
4 096 MB holds 4 096 / 187.5 = 21.8 h. By the measured disk rate (`sws/line_beta/README.md` l.134: 90.7 MB per
hour per head, two heads = 181.4): 4 096 / 181.4 = 22.6 h. By `sws/transmitter/line_calc.py` (178 MB per hour,
4.3 GB for 24 h, `transmitter_line.md` l.80, l.362): 4 096 / 178 = 23.0 h. The code multiplies by 10⁶; if 4 096 was
meant as 4 GiB (4 295 × 10⁶ bytes) it holds 4 295 / 187.5 = 22.9 h. Three counts of 24 h stand side by side (4 500 /
about 4 350 / 4 270 MB); which one the setting follows is not settled here.

## The (b) rows, as headings

1. D07 — Is the chart's "base station" the ruled main station (the chart's own open item `base_station_vs_mcc`)?
2. D26 — The 24 h buffer and its 4 096 MB cap: which count of 24 h the cap follows.
3. D27 — Where processing happens: in the root box or at the logger.
4. D28 — Who stamps the time: the SWS at sampling (SNTP), or the half's sample index with the root box's stamp.
5. D29 — Where the root box sits: per winch, per head, or one SWS publisher per station as the chart draws it.
6. D30 — Whether the chart draws all 51 winches or a smaller layout under a corrected scale card.
7. D31 — Temperature: 0.5 °C part resolution against 0.01 °C frame steps; which the twin uses.
8. D32 — Gap factors of the broken-wire signal: the 4 mm point on record is unused, 0 and 3 mm are assumed, and
   factors from two hidden wires are applied to one outer wire.
9. D33 — The series quantity of about 200 heads against the 108 SWS of the two named installations.

## What was checked and found already right

- "3 x" converters in the chart script: gone; l.109 reads "2 x ADS131M08 [rev131]" (the residue is D10).
- The specification's converter count (rev131 l.298): two per half.
- `twin/Shiplift-twin-analysis/docs/decision-log.md` l.14–15 (SWS data stored with the site's data, time-synchronised
  and tagged with rope position) agrees with F27 and F35.
- `sws/transmitter/transmitter_line.md` §4 ("Position without an encoder") agrees with F34.
- The line beta's settings for rope length, travel, speed and frame period agree with F31, F32 and F16.

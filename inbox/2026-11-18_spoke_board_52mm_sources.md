# Sources: spoke board, 52 mm rope (figure 2026-11-18_spoke_board_52mm.png)

Script: `2026-11-18_spoke_board_52mm.py` (same folder). Paths relative to `C:/Users/stian/Prosjekter-u05/max/sws/`.
Short names: **PL** = hw-selection/sws_sensor_placement.md; **CA** = hw-selection/sws_sensor_candidates.md;
**SY** = hw-selection/rounds/2026-11-16-sensor/synthesis.md; **DC** = same round, datasheet_check.md;
**SP** = spec/rendered/SWS_HW_Design_Input_Specification_rev130.md; **DM** = 3d/p52/design.md;
**RS** = C:/Users/stian/secretary/inbox/2026-11-18_radial_stack_52mm_sources.md. Read-only; nothing in the repo changed.

## (a) Numbers on the figure

| Number | Value | Source | Note |
|---|---|---|---|
| Rope radius | 26.0 | RS:10 | – |
| Stand-off stack (geometry) | liner 1.5 + recess 2.5 + die 1.0 = 5, status A | PL:15, PL:35 | drawn |
| Stand-off stack (floor) | movement 3 + guard 1 + die 0.7 = 4.7 | PL:36–37; SP:285 | **documents differ**; PL:38 "record does not say which" |
| Stand-off = 4.0 + e (e = element depth behind the face nearest the rope) | – | PL:58–59 | so the part face is at r 30.0 |
| Sensor radius at 5 / 3 mm, 52 mm rope | 31.0 / 29.0 | PL:22; DM:193 | – |
| Spoke-to-spoke at the sensor, 5 / 3 mm | 12.17 / 11.39 (2π r / 16, centre to centre) | PL:22, PL:31 | – |
| 16 positions, 8 spokes per half, 22.5° | – | PL:13; SP:285, SP:292 | – |
| Board thickness | **not in the documents** | PL:31–32 | drawn 1.6, "assumed for drawing only" |
| Spoke / carrier axial length | **not in the documents** | PL:44–45 | – |
| Tab size | only "tab width at least the part, 1.10–1.40 (X2SON-4) / 2.10–2.64 (SOT-23)"; thickness and length **not in the documents** | PL:120–121 | drawn 1.8 × 0.8 and 2.8 × 3.0 |
| z of the axial part in B | **not in the documents** ("cannot both sit on the mid-plane") | PL:128–130 | drawn 1.2–2.0 |
| Board-edge keep-out, outline tolerance, solder fillet | **not in the documents** (add to e) | PL:77–79 | – |
| Radial yoke inner radius / spoke length, 52 mm in shared Ø60 | 51.1 / 20.1 (16.8–19.2 at +45 °C sizes) | PL:22, PL:28–30 | not drawn (off panel) |
| A, TMR2185G LGA4L 2.0 × 1.5 (× 0.73), edge to rope | e 0.6–0.85; stand-off 4.60–4.85; kept 104–110 % | PL:65; CA:120 (0.73 height); PL:214–215 (sensing along the 1.5 side; surface 0.16–0.18 below top) | element r 30.60–30.85 (derived: 26 + stand-off) |
| A, TMR2151S SOT23-5, pin-1 end to rope, radial | e 1.00–1.20; 5.00–5.20; 95–100 % | PL:67; DC:62 (body 2.95 × 1.65) | in table only |
| A, TMR2185P SOP8 lead side to rope | 6.20–6.70; 68–76 % | PL:66 | not drawn |
| A: parts back to back, same r and z | "does no harm" | PL:104–106 | layout is the note's own (PL:99–100) |
| A: record names no part; spec says "one radial and one axial TMR bridge" | – | SP:268, SP:285 | drawn TMR2185G both channels (the leadless part PL computes) |
| B, TMAG5253 X2SON-4 on tab, face to rope, radial | e 0.115–0.145; 4.12–4.14; 124–125 % | PL:68 | r 30.12–30.14 |
| B, TMAG5253 on cross tab, edge to rope, axial | e 0.50–0.75; 4.50–4.75; 106–113 % | PL:69 | r 30.50–30.75 |
| TMAG5253 package | X2SON-4 1.40 × 1.10 × 0.4; element 130 ± 15 µm below top | CA:127; PL:232–233; DC:49 | – |
| DRV5055 SOT-23 on a tab | **not computed** (lead span / body length not read; element 650 ± 80 µm above the board plane, not a depth) | PL:85–88 | drawn dashed, no dot |
| SOT-23 (DBZ) size | body 2.80–3.04 × 1.20–1.40, 2.10–2.64 across leads, ≤ 1.12 high | DC:45–46; PL:118–119 | – |
| Models' placement | B 3 of 3 | SY:11 | agreement, not measurement (SY:96) |
| Models' axial part | DRV5055A4 3 of 3 | SY:14 | – |
| Models' radial part | DRV5055A2 2 of 3, DRV5055A4 1 of 3 ("provisionally") | SY:15; SY:100 (still disputed) | – |
| DRV5055A4 range | ±176 mT at 3.3 V, minimum at 25 °C | DC:29 | – |
| DRV5055A2 range | ±44 mT at 3.3 V (±42 is the 5 V figure) | DC:30–31 | correction |
| TMAG5253BA4 range | ±160 mT, already net of tolerance | DC:48 | correction |
| Models' axial demand / radial sums | 131–156 mT / 12.6–20.1 mT | DC:86–87 | – |
| TMR2185 range | specified within ±20 mT, saturation ±100 mT | CA:77, CA:120; DC:65 | – |
| Radial field at r 31.0 | 0.23 mT at mid-plane, 7.53 mT at 4 mm off, ~1.9 mT/mm (inference) | PL:48–49 | 2D, shared head, 52 mm, 25 °C, placeholder materials (PL:47) |
| Axial background at r 31.0 | −36.6 mT, falls 1.86 mT/mm outward, zero at r 50.4; 15 mm stand-off → −17.6 mT, 17 % signal (extrapolation) | PL:48–52 | same limits |
| Radial on mid-plane best; axial loses little off it | inference | PL:128–130 | – |
| Signal law | 0.39 mT at 5 mm, ~21 %/mm, kept 79/129/170 % at 6/4/3 mm, ~2.4 % per 0.1 mm | PL:56–58; SP:285 | radial peak; no axial law (PL:92–93) |
| **Documents differ:** radial read at z ±4 (B_r 0 at z 0), axial at z 0, R 36.5 [UNVERIFIED] | – | DM:194, DM:203–207 | PL puts both at the inner edge (PL:99–130); SP:285 "at the inner edge" |
| Tilt mixing | 0.64 mT per degree at 36.6 mT (A); 3.19 mT at 5° (B tab) | PL:107–110, PL:123–124 | not drawn |

## (b) What the documents judge a sensor part on

1. **Linear range** against background + signal: rule "≥ 2 × (DC background + largest signal)" (SP:331); axial background 31–60 mT design rope, up to ~107 mT (SP:325); record design point ~150 mT (CA:25); radial below ~10 mT, ≥ ~23 mT derived (CA:27, CA:56–57). Models replace the 2× rule by a sum, margin × worst background + signal + tilt leak (SY:19–20); demand 131–156 mT (DC:86).
2. **Noise in the band**: 0.10 mT p-p after template in 0–125 Hz at 57 mm, 0.11 at 52 mm (SP:327); density spec at 1–100 Hz (SP:333); computed as density × 6.6 × √125 (CA:57–60); anti-alias filter before any multiplexer (DC:97–104).
3. **Signal kept by the package / element depth**: ~2.4 % per 0.1 mm (PL:56–61); package ≤ 3 × 3 mm, die close to the spoke edge (SP:337).
4. **Sensing axis vs. board** (in-plane vs out-of-plane): SP:277–283, SP:337; PL:101–102.
5. **Cross-field** (radial part in 31–107 mT across it): on no sheet (CA:140–145; PL:113).
6. **Temperature drift**: sensitivity %/K and offset µV/V/K (SP:334–335, SP:345); TCS × background as uncompensated error (CA:61–64); zero-field drift of Hall parts ±4 mT (CA:79) / ±6.7 mT (CA:86).
7. **Hysteresis**: low (SP:336); minor loop on no sheet (CA:146–148); DRV5055 sheet gives none (DC:40).
8. **Supply**: 3.3 V ratiometric (SP:338); 5 V parts fail (CA:83, CA:88).
9. **Power**: ~1 mW per bridge assumed (CA:35); DRV5055 6.6 mW typical (CA:256; DC:38); whether 1 mW is a hard limit asked by all three models (SY:39–40); power-on time for gating (DC:106–108).
10. **Room between spokes**: 12.17 mm centre to centre at r 31, less board thickness (PL:31–32); tab width (PL:120–121).
11. **Alignment / tilt**: die rotation on no sheet (CA:149–150; PL:107–112, PL:122–125).
12. **Qualification and supply life**: −40…+125 °C, second source or availability statement, 10 years (SP:339); field the part survives, zero after a strong field, long-term drift, part spread (CA:151–162).
13. **Sensitivity**: highest that still meets the range (SP:332).

## (c) What each channel is for

- **Broken wire (local fault):** the radial channel — "Radial channels: local-fault (LF) detection from leakage flux at broken wires and pits" (SP:270). The axial channel gives "a second signature of the same defects with different symmetry" (SP:271).
- **Loss of metallic area over a length:** the axial channels "summed around the circumference ... track the main-flux change that follows loss of metallic area (LMA)" (SP:271); whether 16 axial parts suffice or a dedicated main-flux sensor (Hall probe in the pole gap, or a search coil) is needed is open (SP:271, SP:464); a coil wound round the rope for LMA sits on the carrier, not a spoke (PL:172). The inner rope "is an LMA question, not an LF one" (SP:285).

## (d) Which channel is easier to specify

The documents do not use the word "easier". Their words: "The two channels do not ask for the same part. The axial sensor sits in a static background of tens of mT and ... needs a linear range of the order of 100 mT or more ...; the radial sensor sits below about 10 mT" (CA:40–42); "The radial channel, at its lower background, has several TMR candidates on range; the field across them is the open question" (CA:170–171). So the radial channel is the one the sheets can serve on range; the axial channel's range is what decides the part family (SP:331). But "for the radial channel the record gives no range" (CA:56).

## Not checked

The model answer files themselves (only synthesis and datasheet_check); no data sheet opened; `sws_sensor_placement.py/.json`, `bz_radius_2d.json`; whether TMR2185G may be turned for the axial channel (PL does not say which channel it computes); the minimum SOT-23 height.

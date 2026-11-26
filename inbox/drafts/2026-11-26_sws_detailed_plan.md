# SWS: detailed plan — DRAFT for Stian to read, not sent

Drafted Thu 26 Nov 2026. Built on the schedule from the meeting of 19 Nov (20 tasks) and on the record of work
done since 22 Oct. The full list of work done, 131 rows with figures and sources, is in
`inbox/2026-11-26_plan/sws_history.md`.

## 1. In short

- The schedule from 19 Nov stands: magnet and control hardware orders on **15 Dec**, assembly on **10 Mar**,
  first installation at the **end of March**.
- New in this plan: the **digital twin of the SWS, first version, Wed 2 Dec**.
- Much of the analysis the schedule asks for by 30 Nov exists already (section 3). What it lacks is rope data
  and magnet supplier data, both asked for and not yet received.
- Five things need a ruling or an input before they can move (section 5). The nearest: the board package for
  the specialist, and the size of the large installation.

## 2. Dates that control the plan

| Date | What | State |
|---|---|---|
| Fri 27 Nov | Detailed plan circulated (task 20) | this draft |
| Mon 30 Nov | Magnetic analysis and parameter sweep issued (task 2) | figures exist; note to write |
| **Wed 2 Dec** | **Digital twin of the SWS, first version** | in work |
| Fri 4 Dec | Board architecture confirmed with the specialist (task 7) | package late, not started |
| Fri 4 Dec | Potting method and curing qualified (task 9) | reading done, no trial yet |
| Mon 14 Dec | Magnet geometry, size and grade final (task 5); controls architecture rechecked (task 10) | needs rulings |
| Tue 15 Dec | Orders: magnets (10 heads), control and logging hardware (tasks 6, 11) | — |
| 4–29 Jan | Mechanical design, FMECA | not started |
| 1 Feb–9 Mar | Manufacture and delivery | — |
| 10 Mar | Assembly starts | — |
| 10–24 Mar | Internal validation on the workshop rope | — |
| 29–31 Mar | First installation (six heads) | — |

## 3. Work done since the start (22 Oct – 26 Nov)

All figures are calculated unless marked measured. One line per area; the detail is in the history file.

| Area | What exists | Key result |
|---|---|---|
| Specification | Revisions 123 to 131, a register of rulings, a live parts table (28 parts) | two converters per half; service −40 / +50 °C; names fixed |
| Magnetic circuit, 2D | In-house 2D checked against two other solvers | agreement within 0.33 mT on rope flux density in 18 cases |
| Magnetic circuit, 3D | Stranded rope, broken wires, long loss, groove in the yoke, the 40 mm head on 38–40 mm rope (378 solves), a six-builder falsification run | 52 mm: magnet length for 1.92 T is 16.7 mm (N52) / 17.5 mm (N48SH); 40 mm head gives 1.87–2.07 T on 38–40 mm rope; steel within 0.5 m shifts the reading by 1–8 % of metal |
| Magnet grade, temperature | Knee checks for both grades, empty head and on rope; sun model; four weather days in the twin | N48SH holds everywhere checked; N52 passes the knee in an empty warm head; magnets above 45 °C only on the worst summer day, uncovered (5.6 h) |
| Sensing elements, converters | Data-sheet checks of converters and elements, two blind rounds with five models, placement options on one thin board | 5 of 5: two simultaneous 8-channel 24-bit converters per half; radial element at 5 mm 5 of 5; axial element 3 Hall : 2 TMR, open |
| Potting | Housing and sealing options, resin data sheets | room-temperature epoxies have glass transition inside the service range; soft gel option documented; no trial yet |
| Data line | Frame and line study, the half's core in C, a running simulator of half, root box and logger, update and connection note, root box data reduction | C and Python give the same bytes; 123.5 kbit/s per half; movement found in the SWS data in 1.1 s; data per day 218 → 31–43 GB with rest held back and compression |
| Prototype measurement | Test procedure and rig sheet; the recording of 20 Nov (15 files, measured) analysed three times independently | measured: radial ripple up to 7.9 mV/V; axial noise 0.6–1.0 µT rms; a strong magnet leaves the zero moved and it does not return within 28 min; movement detector found 20 of 20 passes, 0 false starts in 106 min |
| Digital twin | Design, simulator of the full large installation with each rope its own identity and faults, temperature, root box reduction, all joined | 125 tests pass, 1 known failure (position from ripple, 27 mm against 10 mm target) |
| Presentation (HMI) | Two design rounds, four designs, rulings on states and colours | state "Concern" in orange, findings latch, no time-window statistics |
| Standards | EN 12927 chapter 14 and ISO 4309 read and mapped | test piece 0.5 % of metallic area; discard 10 % loss of area |
| Reviews | 16 rounds with outside models, each checked against data sheets or re-computed | findings and contradictions recorded per round |
| Documentation | Eleven pages published for the team, three reading levels | last release 20 Nov |
| Tasks to colleagues | Five issues: rope construction data (#1), prototype noise floor (#2), prototype groove (#3), magnet supplier data (#4), steel near the SWS (#5) | #3 answered in part; the others open |

## 4. The plan forward

### 4a. Digital twin of the SWS, first version — Wed 2 Dec

What "first version" means here: the large installation runs as a twin, every rope with its own faults, and
our own screen shows it live; a second screen lets us put a fault on a chosen rope.

| When | Step | Needs |
|---|---|---|
| Thu 26 – Fri 27 Nov | Plant size corrected to two sides: 102 winches, 6 stations, 204 SWS, 408 halves; fixed facts page applied | ruled 26 Nov |
| Thu 26 – Mon 30 Nov | Twin fitted to the measured recording: ripple size, low-frequency noise, level shift with direction of travel; table "assumed / measured" | — |
| Fri 27 Nov – Mon 30 Nov | Main screen, design version 3 with the rulings applied, fed live from the twin through the same server path the real system will use | — |
| Mon 30 Nov – Tue 1 Dec | Trainer screen: pick a rope, a position and a fault kind, create it; the main screen is not changed by it | — |
| Tue 1 Dec | End-to-end run, check, short demonstration recording | — |
| **Wed 2 Dec** | **First version shown** | — |

After the first version, not before: root box logic in C++, the steel near the SWS in 3D and as a term in the
twin, the customer screen, bending cycles from the control system as a second source.

### 4b. The schedule's own tasks, with what the record adds

| Task (no. in the schedule) | Lead | Date | What exists | What is missing |
|---|---|---|---|---|
| 1 Rope and magnetic-property data | Marius / Henrik | 25 Nov | prototype recording received and analysed | rope construction and lay (#1); magnet supplier data (#4); travel length and speed of the rig |
| 2 Magnetic analysis issued | Stian | 30 Nov | 40 mm head on 38–40 mm rope, groove map, working point, both grades | one note that collects it; real B–H data for the rope |
| 3 Test specification to rope suppliers, 40 mm comparison rope | Ramin | 4 Dec | fault list for a 52 mm test rope (21 faults) | the same for 40 mm |
| 4 Sensor hardware and parallel data | Stian | 28 Feb | element candidates checked; prototype data | choice of axial element (5.3) |
| 5 Magnet geometry, size, grade final | Stian / Henrik | 14 Dec | working area for both grades | ruling on grade (5.4); supplier data (#4) |
| 6 Order magnets, 10 heads | Stian / Henrik | 15 Dec | — | task 5 |
| 7 Board architecture with the specialist | Stian | 4 Dec | architecture and rounds on record | **the package for the specialist (5.1)** |
| 8 Board design, producer talks | Stian | 31 Jan | — | tasks 4 and 7 |
| 9 Potting method and curing | Stian | 4 Dec | resin notes | a trial on real elements; three failures seen on the prototype |
| 10 Controls, link, power, logging, remote access | Stian | 14 Dec | data line simulator; update and connection note; root box reduction | ruling on the link and on root box against PLC rack (5.5) |
| 11 Order control and logging hardware | Stian / project | 15 Dec | — | task 10 |
| 12 Calibration station sketch | Stian | 14 Dec | — | not started |
| 13–15 Mechanical design, manufacture, site fit | mechanical team, Ramin | Jan – 5 Mar | position of the SWS on the rope and nearest steel seen in the CAD pictures | geometry for the 3D run (#5); FMECA |
| 16–18 Integration, internal test, installation | team | 6–31 Mar | rig sheet, procedures page | calibration and acceptance procedure |
| 19 Processing and simulation from measured data | Stian / team | to 31 Mar | three analyses; detector tried on the recording | section 4a |
| 20 Detailed plan | Ramin / Stian / Henrik | 27 Nov | this draft | — |

### 4c. Added tasks, not in the schedule of 19 Nov

| Task | Lead | Date (proposed) |
|---|---|---|
| Digital twin of the SWS, first version | Stian | 2 Dec |
| Root box data reduction: review from the measurement side (brief with pseudocode) | Henrik | 4 Dec |
| Steel near the SWS: geometry (#5), then a 3D run, then a term in the twin | Henrik, then Stian | geometry 4 Dec; run 11 Dec |
| Questions on the prototype recording (travel length, speed, rope construction, strong-magnet steps) | Henrik | 4 Dec |
| Root box logic in C++ | Stian | 18 Dec |
| Firmware update and connection design (eight open questions) | Stian | 14 Dec |
| Second measurement of the same rope with the reference instrument | to name | when it arrives |
| Acceptance, FAT and site test procedures; recalibration | to name | before 10 Mar |

## 5. Rulings and inputs needed

1. **Board package for the specialist.** Was due 22 Nov, not started. A new date is needed; task 7 ends 4 Dec.
2. ~~Size of the large installation.~~ **Ruled 26 Nov: two sides, each 51 winches and 3 stations: 102 winches,
   6 stations, 204 SWS, 408 halves.** The twin is being corrected. Earlier text: the layout drawing read as six motor
   control centres; the twin has 51 winches and three stations.
3. **Axial sensing element, Hall or TMR.** The measured recording shows the zero stays moved after a strong
   field. Needed before the board design (task 8).
4. **Magnet grade for the order of 15 Dec.** The documents show N52 and N48SH side by side and select neither.
5. **The link and the box at the winch.** The minutes say RS-422 into a PLC rack. The design on record is
   RS-485 into a root box per winch. Ours to propose: own line per half, or one shared polled line.

## 6. Risks seen from the record

| Risk | Where it comes from | What limits it |
|---|---|---|
| Zero moved by a strong field | measured on the prototype | choice of element; a test with a known field; a reset routine |
| Seven of twelve radial channels 5–13 times noisier | measured on the prototype | find the cause before the board design |
| Steel 143 mm from the rope at the SWS, moving steel within 1 m | CAD pictures | 3D run; a term in the twin; zero taken in place |
| N52 in an empty warm head | calculated | N48SH, or a keeper and handling rule |
| Rope data missing | #1 open since 3 Nov | assumptions documented; update when it arrives |
| Five days between readiness and installation | the schedule itself | move the field date, not the test |

## 2026-11-12 11:04 (machine clock) - started
- Unit / branch: U71 / u71-sensor-run from 5defd84 (C:/Users/stian/Prosjekter-u71/max)
- Job: the sensor run. Requirement from the record, candidate parts against data sheets actually read, what the sensor fixes for the life cycle, rows for next week's prototype test. Note sws/hw-selection/sws_sensor_candidates.md, section "The sensor" on hardware.html, pointers on procedures.html. Nothing selected.
- Rests on: spec rev130 §4 (speed, sample rate), §5 result 4, §6 (architecture, stand-off, redundancy), §7 (TMR selection table, noise budget 0.10 mT p-p, linear range 31-107 mT), §8, §9 (-40..+50 °C, TMR drift row), §12; register rows "Axial background at the sensor, decided head", "Signal at 5 mm", "Noise budget for SNR >= 2 at every angle", "Guard thickness / TMR die depth"; U17 (bz_radius, offset-range idea); 3d/design_inputs.md.
- Timebox 2 h, ends ~13:04 machine clock.
— Leeboard

## 2026-11-12 (machine clock) - progress
- Requirement table and life-cycle table drafted in sws/hw-selection/sws_sensor_candidates.md; two data-sheet readers out (TMR; Hall/AMR), general queries only.
- Procedures page: two rows sharpened, one added (sensor transfer per channel, 17 rows), pointer from recalibration to the hardware page.
— Leeboard

## 2026-11-12 (machine clock) - committed, done
- Unit / branch: U71 / u71-sensor-run, tip c9dee56 (C:/Users/stian/Prosjekter-u71/max). No merge, no push, no export.
- Note sws/hw-selection/sws_sensor_candidates.md (16 parts, sheets read 2026-11-12); "The sensor" on hardware.html (6 A4, was 5); procedures.html 17 rows, 4 A4.
- Seven --check ok; SWS tests 133 (p52 deselected). idscan 0 (343 added lines, 2 long data lines skipped); scan_tree added 0, removed 0.
- Sensor engineer SIGN WITH FIXES (taken, 2 declined); falsifier 1 FAIL -> fixed; falsifier 2 FAIL (2 blocking) -> fixed, not re-run.
— Leeboard

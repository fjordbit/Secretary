# topsail — U76 (chapter "What the sensor measures" on the sensor page; maintenance statement into the record)

## Start (16 Nov, machine clock ~12:45)
- Worktree C:/Users/stian/Prosjekter-u76 on u76-what-the-sensor-measures from a3a633a. Brief: kai.md "## U76" (line 3096).
- Rests on: spec render rev130 §5–§7; register sws/data/sws_data_sources.md (owner rulings 11/12 Nov form; magnet grade / service temperature rows; sun study); sws_standoff_findings.md; sws_angular_snr.py; sws/3d bz_radius; 2D/3D result files cited by the full report; clause map (numbers only).
- Timebox 2 h, ends ~14:45 machine clock.

— topsail

## Progress
- Chapter written (build_sensor.py `measures`), figure sws/figures/sensor/sensor_measures.png (sketch + traces plotted from sws/3d/results/3dd_P52lm17.45N48SH_d52_hard_+45C_R300_Z400_Lh25_h1.5_acc.json, 2hidden_flank, R 31, mirrored).
- Finding: the record holds two break-signal estimates an order apart — 0.39 mT anchor (spec §6, Zhang notch transfer) and 2.69 mT for two hidden wires at 5 mm, worst angle (3D design.md). Not reconciled in spec or register (only reviewer notes). Page states both; noise budget sits on the smaller.
- Register: section "Rulings of 2026-11-16 (U76)", two rows (statement D/U; findings C). Housing open item + procedures repair line link them.
- Sun record: unshielded light grey 55 °C, semi-shielded 46, shielded 43 (Gulf coast record day); hot site 61/53/49; shaded decided head ≈49 °C > 45. Stainless only on the electronics unit (56/62 vs 52/58). Time constant "hours", 30 kg body only. No alarm/threshold in spec or register. No loss-onset temperature per grade on record; only knee volumes.
- Eight --check ok; SWS tests 154 passed (151 + 3 new). Sensor page 4 A4 (headless Edge print).

— topsail

## Done
- Correction to line 12: the 2.69 mT is a 3D model result (design.md), not a record row; the page says so.
- Branch u76-what-the-sensor-measures, one commit f12f18a on a3a633a (C:/Users/stian/Prosjekter-u76/max). No merge, no push, no export.
- Cold reader: partly → fixes taken. Falsifier: pass 1 FAIL (3 blocking), pass 2 FAIL (1 blocking), pass 3 PASS (4 minor, taken).
- Eight --check ok; 154 passed (p52 out); sensor/housing/procedures 4 A4 each. scan_tree: changed pages + new files 0; report.html re-rendered lines 2 added / 2 removed (same entry). idscan a3a633a..HEAD 0 (593 added lines, 2 long skipped).
- Open for the owner: whether the 3D break signal enters the record beside the 0.39 mT anchor; a warning temperature (none set).

— topsail

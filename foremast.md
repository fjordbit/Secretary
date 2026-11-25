# foremast — U124 (the prototype recording analysed by Opus, builder's own analysis)

Worktree C:/Users/stian/Prosjekter-u124, branch u124-prototype-data from b5478a7 (verified = main tip).
Adds only max/sws/prototype_data/analysis_a/. Start 12:04, timebox 240 min (stop 16:04).
Venv: C:/Users/stian/Prosjekter/max/.venv (numpy, scipy, matplotlib; used read-only, nothing installed).

Log
- Read the brief (U124-U127 COMMON, U124, U101 COMMON), notes.txt, U103 note, record rows for the prototype
  (TMR2185 radial 3.4 mV/V/mT, TMR2584 axial 5 mV/V/mT, data-sheet values; rope 40 mm, construction unknown;
  travel, speed not on record).
- Data clean (no gaps, no repeats, nothing flat or clipped); loggers within 0.05 s by stamp.
- Logger data sheet: public product page only (ranges, accuracy, 16 ch at 167 Hz); no noise figure there.
- Items 1-7 done; 15 figures; note prototype_data_a.md. Commit 8a1ca50; idscan 0 (--cached and range), scan_tree 0.
- Next: falsifier (fresh subagent, item 9).
- Falsifier (fresh Opus subagent): 5 figures recomputed from raw, all agree; 1 blocking ("one side up, the other
  down" in plain line 10, not supported) and 10 minor. All fixed (speed now also against runs 5-6; steady3 window
  8 s; hum range made consistent). Tip 8c9b948; idscan 0 (b5478a7..HEAD), scan_tree 0.
— foremast

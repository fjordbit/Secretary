# ballast — U132 notes to Kai (full-scale twin, every rope its own identity)

- Worktree C:/Users/stian/Prosjekter-u132, branch u132-dt-full-scale from b5478a7 (main tip verified b5478a7 from
  Prosjekter-u05). Venv inside line_beta (.venv, ignored). Measured data not opened.
- New: linebeta/twin.py (plant loader, rope identity, RopeId/TwinSim, on-demand LazySims, ParallelSims workers,
  truth file, exact pass times), linebeta/scenario.py (twin fault scenario), twin_faults.py (CLI), twin_scale.py
  (measurement), plants/plant_large.toml, plants/plant_first.toml, tests/test_twin.py.
- Shared files, one marked block each (U132): settings.toml [plant] appended (enabled=false); pipeline.py one elif
  branch in the sources; run_beta.py six lines after `replay = ...`; README.md section at the end.
- Name scheme proposed (settings): rope S1-W01, SWS S1-W01-A/B, half S1-W01-A.0/.1. Topics unchanged: winch =
  rope index, head = SWS index.
- Places of the two SWS on a rope (0 and 1.0 m) and strand-pitch tolerance (2 %) are ASSUMED placeholders, settings.
- First installation written as 6 ropes x 1 SWS (TL installation A: one head per winch); stations not on record.
- Two-SWS proof: wire at 102.26 m: out A 1977.875 s, B 1996.625 s (+1000/53.333 = 18.75 s); back B 7530.375 s,
  A 7549.125 s. Peaks at those times to the sample, same size; neighbour rope reads 0.
- Scale (shared PC; indicative): 51 ropes single process 0.69x real time (one pass 1.9 h), 12 workers 1.33x (59 min,
  3.5 GB peak all processes). The main process (Python halves, boxes, logger) limits.
- Found on the way: TOML top-level keys after [[station]] fall into the last station; a worker dying left the
  parent waiting forever: now polls and raises.
- Falsifier (fresh agent, files + suite): defaults hold (full suite rerun, same 27.28 mm FAIL), two-SWS arithmetic
  holds (also an lma check), names hold. Fixed after it: scenario faults could drop silently (rope renamed / other
  plant): now raise; table + plant replayed one table: refused in run_beta; workers stayed alive: they now end after
  the last chunk; truth "present" only at the centre: state present/partial/absent added; negative lma refused;
  README scale arithmetic now from 2-decimal walls; dates/role removed from CLI docstring. Left: --make-table and
  --proof ignore the plant; pipeline.run direct with table + plant takes the table; removal = absent for the next run.
- Suite: before 76 passed + 1 failed; after 94 passed + 1 failed (same test, 27.28 mm). Tip 4f341b5. idscan 0,
  scan_tree 0.
- Not done: per_head arrangement numbers the topic winch as the SWS index (pipeline as today); no prefetch in
  workers; logger processes half 0 only.

— ballast

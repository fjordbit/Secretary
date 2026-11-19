# stunsail — U106 groove plots (builder notes for Kai)

- Worktree C:/Users/stian/Prosjekter-u106, branch u106-groove-plots from 02a9486 (verified = tip of u103-prototype-head).
- plotstandard.py copied from model-round 573e59b (blob 9ab386a, identical).
- Standard cannot draw marks (shaded range, band, vertical line, marked points) or a field map: figkit.py adds
  them around the unchanged module (ps.check run first; same text limits on the marks). Field map E by hand.
- Module gap found: only three calculated line styles; a fourth calculated curve repeats the first style
  (colour differs), so grey print does not separate them. Not changed (module is not ours to change here).
- Re-runs (run_missing.py, large box): standing profiles at the three depths; depth sweeps (H52 model, N48SH,
  N52; H40); level at N48SH / N52 for the zero at 16 mm; prototype at N48SH / N52; one field map solve.
- All 72 re-run solves converged (10 Newton steps, 185-225 k nodes). Map re-solved once more on a 1 mm grid
  (first version 4.4 MB, too large).
- Falsifier: 5 blocking (A note "under 0.1 mm" wrong at 19 mm: 0.13; B slide "0.4-0.5" overstated for 52 mm
  head; digit codes H52/N48SH/B_z not linked - module's abbreviation regex misses them; abbreviations on
  slides; README mark-count claim vs D with 7 entries). All fixed: figkit now tests digit codes and counts
  marks; D shows N48SH-N52 as one band. Non-blocking fixed: minus signs, diameter, "in the model", proposal
  steel/second-head wording, link note. Not fixed: C legend overlaps the no-groove curve at 10-13 mm; grey-
  print style repeat (module gap).
- Commit d112319 (adds only max/sws/3d/groove_plots/, 25 files). idscan 0 (02a9486..HEAD), scan_tree 0.
  build.py --check: 1 problem (report.html stale, as base); pytest tests/test_sws_* 185/186 (report, as base).
  run.log (has local paths) kept out of the repo, in the scratchpad.

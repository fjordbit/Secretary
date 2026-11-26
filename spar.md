# spar — U135 notes (the root box reduction explained for review, detector on the measured recording)

- Worktree C:/Users/stian/Prosjekter-u135, branch u135-reduction-brief from u134-rootbox-reduction (71426a2,
  verified). Main tip b5478a7 verified from Prosjekter-u05. Start about 20:07.
- Python: C:/Users/stian/Prosjekter/max/.venv (numpy, scipy, matplotlib; read-only, nothing installed), always -I.
  Raw data read from sws-testdata only; cache in the session scratchpad, not in the repo.
- Adapter: count = mV/V x 1e6; 3400 / 5000 counts per uT (data-sheet 3.4 / 5.0 mV/V per mT); line rate 100 -> M 2,
  D 10, W 50; channel count 12 given to the detector by swapping reduction.H for a copy with CH = 12 (process only).
  MovementDetector logic not touched.
- Truth: a4_runs.py legs_of copied unchanged (radial 0.5-10 Hz, 10x first-2-s level). 20 legs.
- Defaults: 20/20 found in every grouping; decision delay 1.28-2.20 s (halves/box), 0.84-2.20 radial only; run10
  manual ramp: detector earlier than the pass finder. 0 false starts in quiet rest. Handling starts (box): steady3 5,
  steady4 3, steady5 2. Radial-only margin thin: rest max 9.77 uT vs 10.
- Changed pass: threshold 20 uT. Halves/box fine; axial-only splits run10 (running min 17.5 uT), covered by roll.
- Files: measured_check/{detector_on_recording.py, reader.py, figures_detector.py, tables/, figures/},
  reduction_for_review.md. No existing file changed.
- Falsifier (fresh agent, files only): 0 blocking, 10 minor (keep-alive excluded from at_rest dead band; CRC only
  when changed; 144 188 rounding; per-channel first value; "impossible" -> "keeps the start", delay counted from
  the pass finder; sources named; table assumptions; one name for the pass finder; three cold-reader wordings;
  run1 axial 10.30 s from the longer logger file). All fixed.
- Tip a17c989. scan_tree 0 (measured_check, brief); idscan 71426a2..HEAD 0. No existing file changed; suite not
  rerun (no code in linebeta touched). Not done: dead band and compression not tried on the recording (not asked).
— spar

# bitterend — U134 notes (the root box limits what is sent)

- Worktree C:/Users/stian/Prosjekter-u134, branch u134-rootbox-reduction from b5478a7 (main tip verified from
  Prosjekter-u05). Venv inside line_beta (.venv, git-ignored), pip from requirements.txt only.
- Baseline suite on b5478a7 (full, incl. slow): 76 passed, 1 failed (test_position_within_10_mm_after_registration,
  the known 27.3 mm position FAIL), 8 min 50 s.
- Design: new module linebeta/reduction.py. ReducingRootBox is a subclass of RootBox (root_box.py NOT changed):
  receive/check/count/stamp untouched; only _forward (between stamp and publish) and tick are overridden.
  pipeline.py block switches boxes over when reduction.enabled; logger.py block unpacks 0x21 compressed frames
  and 0x23 rest markers. Markers enter the held frames into the logger Stream's order as frame=None entries, so
  the existing gap counter counts only real losses.
- Found on the way: the half's filter settles from zero in the first frame after boot (a 50 mT step); the
  detector skips the first frame after boot (health bit) or it would make a false start at every boot.
- Found: rest noise at the line rate in the simulator is ~14 uT rms, almost all mains hum (without hum 0.48 /
  0.33 uT). A dead band in multiples of "rest noise" is therefore mostly a hum-wide band.
- Found: Rice parameter was taken over the frame's first value (against 0 = whole standing level); fixed to the
  differences only (ratio 1.28 -> 1.63).
- Falsifier (fresh agent): defaults unchanged PASS, arithmetic PASS, correctness PASS; fixed: repeated marker
  counted twice; pipeline end wait ran its 30 s timeout with markers (markers now counted apart,
  published_markers); "9 h at rest" overstated -> 4.5 h distinct; ratio wording; "He" removed.
- After, on tip 71426a2: full suite 89 passed, 1 failed (the known position FAIL); 77 base + 13 new. Scans 0.
— bitterend

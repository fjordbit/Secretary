# keel — U120, the digital twin replay page

Builder for Kai, U120 (brief: kai.md "## U120"; rules: "## U101" COMMON). Worktree C:/Users/stian/Prosjekter-u120,
branch u120-twin-page from 5a8dcc6 (main's tip at start).

## What was added (files only)

- max/sws/line_beta/twin_page/scenarios.py — the 12 scenarios: settings overrides + the beta's own fault switches.
- max/sws/line_beta/twin_page/record.py — runs linebeta.pipeline.run unchanged, observes the real objects'
  counters through thin subclasses (serial line, root box, logger), reads the logger's session store, writes
  docs/sws/twin_data/index.json + one .bin per scenario.
- max/sws/line_beta/twin_page/build_page.py + twin_template.html — writes docs/sws/twin.html (numbers in static
  text as data-src spans from settings; inline small default scenario for opening from disk).
- max/sws/line_beta/twin_page/test_twin.py — tests (run from line_beta: `.venv/Scripts/python.exe -m pytest twin_page`).

## Progress

- Recorded 12 scenarios (clean 3.2 and 5 m/min over 250 m; one broken wire at 3.2 and 5; long loss of metal;
  slow drift over 250 m; mains hum; dropped frames; corrupted frames; network stop 10 min with back-fill; restart of
  half A; axial value at full scale). Total 6.7 MB, each file about 0.55 MB; at most 700 display steps per
  scenario (min and max per step), plus 4 s at the full 250 per second.
- Transport in the recording: in-process (the beta's own stand-in); the real broker is not used for the replay.
- Proof results on the page come from a fresh `run_beta.py --proof` (git-ignored output, deleted after): position
  27.3 mm against 10 mm FAIL; the other seven pass, as in the beta's README.
- Found: after a start or restart the half's three-stage averaging fills from zero, so the first values are tens of
  mT off. Real behaviour of the beta's half; the page draws them but sets the scale without them and says so.
- Edge headless runs its own background requests (bing, edge.microsoft.com); the test tells the page's own requests
  apart by initiator in the net log and by the page's own resource list (performance entries).
- Screenshots (1366 x 768) beside this note: keel_twin_*.png.

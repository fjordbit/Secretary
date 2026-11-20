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

(filled in below as the run goes)

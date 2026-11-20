# topgallant — U117 results page (builder notes for Kai)

Worktree C:/Users/stian/Prosjekter-u117, branch u117-results-page from 5a8dcc6 (checked: tip of main).

## What was built
- `max/docs/sws/build_results.py` writes `results.html` (the ninth menu page, "Results", after the start page) and
  `parts.html` (the full parts table; off the menu, linked from results.html#r-table, like rig_sheet.html).
- The values come from parts.yaml, row by row. Each value links to its own yaml line, and the number test reads that
  line. Display filter `show()`: line references "(… l.NNN)" and attributions ("owner's newer thought",
  "— the owner's position", "; owner statement") move to the hover title, and the part name "Installation facts given
  by the owner" is shown as "Installation facts". Nothing else changes. The record's wording is in the title.
- Figures: PNG embedded, plus the interactive HTML in a `<details>` iframe (srcdoc, `<base>` pointing at the published
  repo folder). This is self-contained, so no relative link leaves docs/sws. Blocks d and e have no interactive
  version (only PNG/SVG exists). Block h has no figure (the Scotchcast note has none).
- Menu: FORMATS in build.py; the tests that pin the menu were updated (easy, hardware, short). There is a link line
  at the top of index.html and easy.html through their builders.
- report.html was rebuilt because its menu changed. The rebuild also pulled in register rows that were already on
  main (it was stale before: base `--check` 8/9, pytest failed on it).

## Environment
- The u41 venv has no PyYAML. The builder therefore carries a small reader for the subset of YAML that parts.yaml
  uses. The test `test_yaml_reader_agrees_with_pyyaml` skips in u41; run under C:/Users/stian/Prosjekter/max/.venv,
  it passes (equal to yaml.safe_load).
- test_sws_p52 fails in the u41 venv only (no yaml); it passes in the solver venv. This was already so at base.

## Terms merge (#r-names), where the files differ (the newer file's wording is kept; merge order u106 < u107 < u108 < u109 < u111)
- SWS / head / half / element / channel / root box: five different wordings across the files (element run 3:
  "steel wire rope sensor"; tradeoff: channel = broken-wire / loss-of-metal channel; data-path / transmitter:
  channel = one converter input). All are replaced by the ruled names block of parts.yaml.
- Level: groove_plots adds "averaged over the loss passing the head"; the shorter element run 3 wording is kept.
- Magnet grades: groove_plots names the N40SH placeholder and N42 for the prototype. Element run 3 (newer) gives
  N52 18.1 mm / N48SH 19.1 mm. The page keeps the remanence only.
- Hall: element run 3's wording, plus the tradeoff clause "wide range, higher noise, larger drift". The cited line
  holds only the first part.
- Groove: groove_plots wording (20 mm on the model heads, 10 × 2 mm on the prototype). The tradeoff note adds the
  wall depth of 11.96 mm.

## Older pages that now disagree with results.html
- software.html: 500 samples per second in its short box and its link section; "the specification has three"
  converters (case C).
- hardware.html: 500 per second preferred; the three-ADS131M08 cases; 4000 SPS figures.
- report.html: small-box groove depths 6.08 / 5.36 / 4.64 mm (h52_groove part); 2.1 T as the middle of the window.
- sensor.html: placements on the spoke board and the old stand-off framing. The board is now one thin board (a
  proposal).
- parts.yaml itself: R40 (40 mm head on 38–40 mm rope) is still "open: nothing on record", while the h40_on_38 note
  (merged as u115) answers it in the model. Not edited, per the brief.

— topgallant

## Cold reader (one pass) and what was done
- Fixed: the working point is now "the page works with about 2.0 T, proposal, not agreed; the model cannot place it
  in tesla until the rope curve is measured; record also holds 2.1 T". Board "not settled" in the ten sentences.
  Status shown on 250/s, groove depths and line rate. Closing sentence no longer says that everything is calculated.
  Liner wording; "64 K rise"; N48SH on potting; 52 mm named. parts.html notes: attributions and "(status D)" moved
  to the hover title.
- Not fixed (outside the brief): the menu labels and descriptions of the other pages use "decided", "chosen",
  "choose", "selection" and "sensor" alone. They show here because the switch is shared.
- Not fixed: Y04 shows 3.92 mm under two magnet descriptions (that is in parts.yaml). The Model box term says
  "1.1 mm too deep", which holds for H52 only (H40 is about 0.5 mm). The record's own "no selection" / "none picked"
  wording is kept in values.

Tip 5c448b3. Checks 10/10 ok; SWS pytest 209 passed, 2 skipped, 1 failed in the u41 venv (p52, no yaml: as at base),
and both of those pass in the solver venv. results.html prints on 8 A4, parts.html on 10.
— topgallant

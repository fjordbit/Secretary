# forefoot — U119 two converters per half everywhere (builder notes for Kai)

Worktree C:/Users/stian/Prosjekter-u119, branch u119-two-converters from 5c448b3 (checked: tip of u117-results-page).

## Grep (the brief's, widened) — hits per class
Widened pattern: the brief's plus "three (devices)", "N_DEV = 3", "19 of 24", "5 spare", "five spare", "fourth ADS",
"three converter", "3 converters", "24 inputs", "three chips", "CHANNELS = (16, 24)", "24 ch". Over max/, pycache excluded.

| Class | Before (lines / files) | After (lines / files) |
|---|---|---|
| A live | 113 / 23 | 49 / 16 — none states three as current: 27 are case D's multiplexed chips ("three chips", "3 × ADS114S08"), a different case kept on purpose; 22 name the old count once as superseded or are marked (report marks, K01 note, data-path row, traffic.py comment, regexes that point at round files, a test docstring) |
| B specification | 10 / 1 (rev130 render) | 17 / 2: rev131 6 (superseded mentions, the 24-position alternative, the first-issue history row) + REDLINE 11 (the rows themselves) |
| C history | 84 / 19 | 94 / 20 (rev130 render now counts as an older revision); none changed |

Before, class A by file: build_hardware 17, hardware.html 15, report.html 12, chart.json 24, link note 8, software.html 5,
test_sws_hardware 5, build_software 4, price md 4, price py 3, price json 2, parts.yaml 2, transmitter_line 2, and 1 each in
parts.html, results.html, make_sws_shiplift.py, data_path.md, traffic.py, sws_link_budget.py, parts_table.html/.md,
test_sws_software, twin architecture.html.
Class C (unchanged): rounds/2026-11-10 (brief, synthesis, five answers), data-path/answers 1–3, due-diligence briefs/
sws_carrier_brief, fem-2d/sws_review_2026-10-23_findings, spec rev123 md and renders rev127–rev130, tasks/reports U58/U60/U61.
Also outside the brief's grep, found by "three near converter": sws_sun_exposure_findings.md (ADS131M08, 3 pcs, 18 mW),
sws_sync_findings.md (2–3 ADS131M08, twice), sws_data_sources.md row "Fixes applied 2026-10-14" (3 ADC / 16 TMR),
sws_scripts_README.md (corrected to 3 and 16), TASKS.md l.93: all spec-phase or dated record → C, not changed; the four
that the full report shows carry a marked correction there (below).

## Recomputed (old → new)
- Link budget (`sws_link_budget.py`, CHANNELS (16, 24) → (16,)): the 24-channel row (101 bytes, 505.0 kbit/s, 110 % at
  460.8 k, 50.5 % at 1 M) is gone; 16-channel rows unchanged (77 bytes; 192.5 / 385.0 / 770.0 kbit/s). Link note §4 table
  and the "24 channels need 1 Mbit/s" sentences removed (link note, hardware and software pages).
- Price and complexity (`sws_price_complexity.py`, case C folded away): C's converters alone 29 / 22 USD (10 / 1000 pcs),
  chain BOM 45–56 / 34–37, assembled 127–280 / 42–63, temperature 0.63 → removed (kept as one line in the note). A, B, D
  unchanged; the overlap stays 45–58 (1000 pcs) and 134–268 (10 pcs); converter share 26–53 % unchanged; index order:
  equal A B D, behaviour A B D, parts B A D (flips). Both figures regenerated (price_complexity.png, price_glance.png).
- Twin worked example (architecture.html, hand arithmetic, no script): 24 → 16 channels: 480 000 → 320 000 values/s,
  4 800 → 3 200 rows/s, about 83 → 55 GB per day. Not corrected: the example multiplies by "200 SWS", while an SWS has two
  halves of 16 channels; it was already loose.
- Spec channel row: "16 TMR + excitation + 2 temperature = 19 of 24" → "16 TMR = 16 of 16".
- Not recomputed: the heat budget's 3 × 6.0 mW = 18 mW (sun findings, spec-phase record, class C) — 2 × 6.0 = 12 mW,
  inside the stated 0.2–0.4 W band; marked in the report only.

## Specification and full report
- New revision by the existing route: rev131 docx = rev130 docx with 11 text replacements and one revision-log row
  (stdlib zip edit, the same route as rev128–rev130; script kept in my scratchpad, not in the repo); `render_spec.py` knows
  rev131 and renders it by default; rev130 re-renders byte-identical. Redline: REDLINE_2026-11-18.md section U119, rows
  13–24 (applied in rev131). spec/README updated. **The owner's Word master still has to follow by hand.**
- rev131 lines: 285 backplane, 287 coverage ("The third ADS131M08 that 16 positions need" — missed by the grep, found on
  the after-pass), 292 channel row, 298 design conclusions + gradiometer sentence, 302 recommendation ("decided" dropped),
  317 option B, 321 schematic note (excitation channel and five spares gone; ratiometric reference named as the owner's
  position; l.317 "internal 1.2 V only" NOT changed — K03 holds both), 327 and 493 the 24-position alternative ("one
  8-channel converter more than the two of rev131"), 419 timing, revision-log row. First-issue log row l.527 kept.
- All builders now cite rev131 (HB.SPEC and build.py "spec" part); line numbers equal to rev130 up to the log.
- Full report: the spec part is rev131. Dated parts that state the old count get a marked correction after the text
  (`COUNT_MARKS` in build.py, italic "[superseded: two converters per half]", hover title): spec l.527 log row, f_sun,
  f_sync ×2, f_review, register row, b_carrier, scripts README. 8 marks; build fails (MISSING) if a phrase is not found.

## Cases
- Case C (third ADS131M08 for the bridge supply and two analogue temperatures) folded away on the hardware page, the
  price note and script, and the link note §8. Judgment: it also differed from A in measuring the bridge supply on a
  channel instead of a ratiometric reference; the owner's position in K01 / data-path covers that too (ratiometric
  reference), so I counted it as "only what the ruling settles". If Kai reads the brief strictly ("more than the
  temperature channel"), C would be kept: say so.
- Case D kept (multiplexed ADS114S08 / ADS124S08, three to four chips for 16 bridges, not a temperature matter).
- Round 2 records (ranking table, "C first or second for all five") kept as the record with one line each saying C's count
  is superseded; the C paragraph of round 2 shortened to a pointer.

## The four small items
1. R40 → "calculated, not measured", values from h40_on_38.md l.11 / l.19 with arithmetic; results.html block c and
   SETTLES updated; parts table, parts.html, results.html rebuilt.
2. K01: value "ruled by the owner: two — …"; refs rev131 l.298, transmitter line, rev130 l.298; note names rev130's three
   ADS131M08 / 24 channels once as superseded.
3. Menu labels and hover descriptions (build.py FORMATS) and hardware page:
   - start page: "what is decided, what is open" → "what is on record, what is open";
   - "Hardware selection" → "Hardware cases" (menu label and the page h1); its hover: "four cases for an outside expert
     to choose from" → "three cases for an outside expert to weigh";
   - sensor: "where it can sit on the spoke board, with suggestions; nothing chosen" → "on the board, with suggestions;
     no part or placement picked" (the spoke board is not confirmed);
   - housing: "for an outside expert to choose from" → "to weigh";
   - hardware lede: "four cases … to choose from … The choice of case is the expert's" → "three cases … to weigh, two
     converters per half being ruled by the owner … Which case is the expert's call"; section title "The four cases" →
     "The cases"; spec rev131 l.302 "layout decided in section 6" dropped.
4. Cold reader's two: Y04 — 3.92 mm now one value, "one depth under two names, modelled N40SH here and N48SH in element
   run 3" with a ref to element_run_3 l.64 and a note; Model box term and block b — "about 1.1 mm on the 52 mm head, about
   0.5 mm on the 40 mm head", cited to g_large_box.md l.183.

## 500 per second on older pages (listed, not changed)
build_hardware.py l.283, 328, 346, 383 (×2), 420, 434, 471, 476, 506; build_software.py l.160, 208 (and the link note's
OSR 8192 = 500 S/s example throughout).

## Checks
- `--check`: 10 of 10 page builders ok; price note ok; parts table 153 rows, 0 problems.
- SWS pytest (u41 venv): 209 passed, 2 skipped, 1 failed (test_sws_p52, no yaml — as at base); p52 + results tests in
  the solver venv: 31 passed. Tests changed to the new truth (none deleted): easy (menu label), software (short box),
  hardware (cases table A B D, ruling named, positions, round 2, data-sheet wording, cable and budget rows, price cells,
  menu label).
- Line-reference drift fixed in parts.yaml (E12, K02, K04, T01 point at build_hardware.py lines that moved).

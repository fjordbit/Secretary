# bunt — U137 notes to Kai (the large installation has two sides)

- Worktree C:/Users/stian/Prosjekter-u137, branch u137-two-sides from 67866d8 (main tip checked from u05). Venv
  inside line_beta (.venv, ignored). Measured data not opened.
- Plant: plants/plant_large.toml = 2 sides x 3 stations x 17 winches = 102 ropes, 204 SWS, 408 halves. Stations
  ST1-ST3 on side A (first positions 1/18/35), ST4-ST6 on side B: ASSUMED and editable in the file.
  plant_first.toml: only sws_letters -> sws_labels ["1"], side "" (sides not on record), station name ST1.
  No one-side plant file kept: tests did not need it (plant.ropes = 51 runs side A).
- Names (proposal, settings plant.name_*): rope = winch "{position}{side}" -> 1A..51A, 1B..51B; SWS
  "{rope}-SWS{label}" -> 1A-SWS1, 1A-SWS2; half "{sws}.{half}" -> 51B-SWS2.1. First installation: 1..6, 1-SWS1.
  load_plant also returns `hierarchy` (side -> station -> ropes). The truth file adds side and position.
- Half id: one byte, (2 x SWS + half) mod 256, as the pipeline already makes it. 408 halves repeat ids across the
  plant. The old guard ">256 halves" is replaced by a check that ids are unique inside each root box. The root
  box checks only its own port, and the logger keys by winch/head/half, so this is safe (falsifier checked it).
- Day figures (root_box_reduction.md, reduction_for_review.md, tables/reduction_study.json per_day): recomputed
  with `study_reduction.py --per-day-only` (new flag, no simulation; with halves_large = 204 it reproduces the
  stored block exactly). All large figures x 2 (408/204): today 436.4 GB; rest held 98.91; rest held +
  compression 68.7 / 61.0 / 85.0; dead band at rest + compression 205.5 / 131.9 / 130.2; compression only
  302.8 / 269.2 / 375.3 (delta_varint / delta_rice / zlib). The first installation is unchanged.
- The falsifier noted an older gap: the shown "5.248 h" gives 98.901 against JSON 98.907 (2 x 9 447 s = 5.2483
  h). It was there before; left as it is.
- README line 154 area (U110 replay, measured on one side): doubled with the arithmetic, not re-measured. Its
  "14.7 MB in 60 s" does not match 122 400 frames x 1 238 B = 151 MB. Left as is, for Kai.
- Outside line_beta: NOTHING changed. Places that still state the one-side size (51 winches / 3 stations / 102
  SWS or heads / 204 halves, or figures derived from it: 816 000 values/s, 3 264 channels, 216 GB/day, 9.1
  GB/h): 75 lines in 23 files. The grep was pattern-based, so a reworded statement may be missing:
  docs/sws/build_results.py 358; docs/sws/parts.html 348 377 378; docs/sws/results.html 199 301;
  flow/examples-0.2-draft/make_sws_shiplift.py 241 (says the functional spec has 102 hoists with one SWS each);
  sws/data-path/answers/answer_1.md 9 141 196 205; answer_2.md 89 162 173; answer_3.md 133 174 190 191 209;
  sws/data-path/data_path.md 19 27 118 121 131 168 174; sws/data-path/fig_t3.html 13; fig_t3b.html 13;
  sws/data-path/terms.md 15; sws/data-path/traffic.py 10; sws/data-path/traffic_tables.md 31 37 43 49 55 61
  71 77 83 89 95 101; sws/parts_table/README.md 87; parts.yaml 1852 1857 1858 2041 2044 2045 2052 2055 2056;
  parts_table.html 24; parts_table.md 357 358 372; sws/transmitter/answers/claude-claude-opus-5-5.md 291 340
  345 396; cursor-cursor-grok-4.5-high.md 188 210; cursor-gpt-5.3-codex-high.md 110 200 234 260 275 319 357;
  sws/transmitter/fig_d1.html 13; sws/transmitter/terms.md 19; sws/transmitter/transmitter_line.md 44 362
  396 495. The answers/ files are outside models' answers: quote, do not correct. The pages (docs/sws) come
  from parts.yaml and the builders.
- Scale (twin_scale.py, 30 s stretch scaled to one pass of 4 687.5 s; one shared PC, indicative): 102 ropes, 0
  workers 57.31 s wall -> 57.31 x 4 687.5 / 30 = 8 955 s (2.5 h), 321 MB; 12 workers 37.57 s -> 5 870 s (1.6 h),
  6 379 MB in all processes; 24.8 GB stored per pass (2 x 12.4); 122 400 frames, 0 lost.
- Suite: main (clean copy of 67866d8) 125 passed + 1 known failure (27.28 mm); branch 126 + the same 1 (new test:
  a winch position twice on one side is refused). Tests changed for the new size: test_twin.py
  plant_large_and_first, names_and_places, the two-SWS tests (names), full_scale_no_replay (408 halves),
  scenario_add_list_remove, command_line_form, scenario_faults_never_dropped, truth_partial.
- Byte check: `run_beta.py --out` with defaults, main copy against branch: 22 of 27 files identical (every raw
  and index file). The other 5 are report.json, per_second.json, session.json and fig_b3 html/png, which hold wall
  time and timing and differ between two runs of main too (as whipstaff found).
- Falsifier (fresh agent, files only): totals, names, per-root-box half ids, nothing outside line_beta, defaults
  all hold. Fixed after it: README label of the 9.1 GB figure; the 102-rope rows added; a position overlap check.
  Left: "installation B" wording kept beside "side A/B" in the README's U110 section.
- Commits 7bd36f3, 9907ae0, f7c72d4 (tip). idscan 0 (231 added lines); scan_tree 0 on added lines and commit
  messages (this note: 2, its own local path).

— bunt

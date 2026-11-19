# Futtock — U86 notes (17 Nov)

U86 builder (Opus): export increment for U83 + U85 (5f415b6..84af27a, max/ subtree, first-parent) grafted on 0f7b145,
Pages snapshot in publish/SWS on 1a58533, link proof on nine pages. Method as gybe.md / gasket.md. No identifier
values, no personal names.

- 00:37 (machine clock) started; timebox 1 h.
- Start verified: Prosjekter-u05 main 84af27a = D:/git/prosjekter.git main; ls-remote fjordbit/max main 0f7b145 =
  export clone tip; publish/SWS 1a58533 = ls-remote origin and maxflow. first-parent 5f415b6..84af27a = 2 (U83, U85
  merges); increment touches only max/.
- Export: work/ refs/mono/main16; tools/replay16.py -> replay16 2a14a7f, both "exact". fast-export
  --reference-excluded-parents refs/exp/out15..replay16, ref renamed (2 commit lines, 0 other), rewrite_names:
  48 commands / 5 blobs / 0 messages (rw16.log), fast-import -> export main 1680bc1 (FF of 0f7b145, 2 commits),
  worktree reset, clean. verify_diff vs 84af27a:max: same 6 strategy paths (5 OK, 1 pptx only-in-original).
  refs/exp/out16 = 1680bc1 in work/.
- Answers' front matter (6 answers; round.json, models.yaml the same fields): kind, round, backend, model,
  model_used, label, status, started/finished timestamps, seconds, dry_run, input_sha256 (hash of the input),
  input_bytes, workdir and command (paths start at "~", temp work dirs and CLI paths), sent/not_sent lists (file
  names, bytes). No user name, no expanded machine path, no account/org id, no key fragment. Nothing changed.
- Scans (u05 venv): tiptree16 875 files, 660 whole-word, per-file table identical to tip15. Increment addscan16:
  32 paths (22 A, 10 M, 0 D). Whole blobs report.html 86, sws_data_sources.md 23, TASKS.md 7 = old known hits.
  Added lines 2 (owner-name entry) on re-rendered report.html lines; removed side the same 2. Round folder (both
  briefs, sent/, six answers, synthesis, datasheet_check), sensor/rig sheet pages + builders, AI guide, register
  rows, tests, messages: 0. Substring advisory: no new (sensor.html 1 = known base64). Pattern grep for
  user paths / key / account-id shapes: only regex text in a builder and base64. idscan 0f7b145..1680bc1: 0.
  No pdf; no file from secretary/ or max-private/; standard named only by number.
- Tests in testtree16 (u41 venv): nine --check exit 0; ten SWS test files (p52 skipped) 181 passed.
- Snapshot on 1a58533: 7 M, 22 A, 0 D; sws/ tree = export tip sws/ (db93b36). unlink16 (= unlink15): index 6,
  report 1, easy 2, procedures 2, rig_sheet 1 (as before); 0 new. Switch: eight entries on eight menu pages, current
  once, targets exist; rig_sheet not on menu, opens from procedures #st-proto, its back links and own links pass.
- Sensor new links: 7 to 2026-11-16-sensor/synthesis.md (#L1,L11,L14,L19,L23,L34,L100), 1 to datasheet_check.md#L1,
  2 to 2026-11-12-sensor/synthesis.md#L23 — GitHub blob view in MAx-Flow/SWS-Documentation, files committed in the
  snapshot, lines within length and on the cited bullet; in-page #s-loop (3), #s-life (calibration h2),
  #s-testfield (printed-conductor paragraph), rig_sheet.html#rs-gap, report.html U83/U85 register anchors: exist.
- Links tools/links16.py (= links15), export-v3/links16.txt (relative/own-repo/external, broken): index 384/0/0,
  report 496/63/39, easy 62/0/0, hardware 42/303/0, software 19/310/0, housing 79/156/0, procedures 115/19/0,
  sensor 53/94/2, rig_sheet 23/4/0; broken 0 on all nine.
- External: 38 distinct, same set as U79; 0 new, so no HEAD sent.
- Visible text sensor / rig_sheet (visible16.txt): 0 on every pattern. Print (headless Edge, snapshot copy, A4):
  rig_sheet16.pdf 5 pages, sensor16.pdf 4 pages.
- index.zip rebuilt (snapshot report.html + old mp4, byte-checked), untracked; old at index.zip.before-u86.
  pubtree16 (+_titles, _unzipped) 542 files, 397 hits, per-file table identical to pub15; _titles 0. Snapshot
  increment: added 2 owner-name hits on re-rendered report.html, removed 2. Commit 367549c (tree ee6bed4 = scanned
  staged tree); idscan 1a58533..367549c 0. git status: only index.zip untracked.
- Push commands (Kai's):
  git -C C:/Users/stian/export-v3/export push https://github.com/fjordbit/max.git main:main
  git -C C:/Users/stian/publish/SWS push origin main
  git -C C:/Users/stian/publish/SWS push maxflow main
- 01:43 done (about 6 min over the timebox). Nothing pushed.

— Futtock

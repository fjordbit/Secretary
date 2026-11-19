# Mainsheet — U94 notes (18 Nov)

U94 builder (Opus): export increment for U91 + U93 + U92 + Kai's commit (44a5b0e..062b8bd, max/ subtree,
first-parent) grafted on 7f2b3f7, Pages snapshot in publish/SWS on 36bc5cb, link proof on nine pages. Method as
lazyjack.md / yardarm.md / futtock.md. No identifier values, no personal names.

- 14:45 (machine clock) started; timebox 1 h.
- Start verified: Prosjekter-u05 main 062b8bd = D:/git/prosjekter.git main; ls-remote fjordbit/max main 7f2b3f7 =
  export clone tip; publish/SWS 36bc5cb = ls-remote origin and maxflow (only index.zip untracked). first-parent
  44a5b0e..062b8bd = 3 (U91+U93 merge, U92 merge, Kai's commit); increment touches only max/ (69 paths).
- Export: work/ refs/mono/main19 (fetched 062b8bd); tools/replay19.py -> replay19 df3c625, 3 commits "exact".
  fast-export --reference-excluded-parents refs/exp/out18..replay19 (in19.raw.stream); tools/rename19.py: 3 command
  lines, 0 in data, output == raw with the replacement; rewrite_names: 83 commands / 5 blobs / 0 messages (rw19.log);
  fast-import -> export main 8beade9 (parent chain 4b713c5, 4b97d49 on 7f2b3f7, FF), worktree reset, clean.
  verify_diff vs 062b8bd:max: same 6 strategy paths (5 OK, 1 pptx only-in-original). refs/exp/out19 = 8beade9 in work/.
- Front matter (6 answers; round.json x2, models.yaml x2): kind, round, backend, model, model_used, label, status,
  started/finished, seconds, dry_run, input_sha256, input_bytes, workdir and command (all paths from "~": temp work
  dirs, CLI paths; cursor command also --workspace from "~"; --model names), sent/not_sent (file names, bytes);
  round.json also detail (null) and file; models.yaml one comment line (key test 16 Nov) and three model rows. No
  user name, no expanded machine path, no account/org id, no key fragment. Nothing changed.
- Scans (u05 venv): tiptree19 957 files, 660 whole-word, per-file table identical to tip18. addscan19: 69 paths
  (28 A, 40 M, 1 D). Whole changed blobs carry only old known hits (report.html 86, sws_data_sources.md 23, TASKS.md 7,
  five sws/3d files with the owner-name entry: tip per-file table unchanged). Added lines 2 (owner-name entry) on
  re-rendered report.html lines; removed side the same 2. Board round folder in full, redline, lma_sweep note/JSON,
  changed pages + builders, register rows, messages: 0. Substring advisory: new hits on added lines all inside base64
  image data (ctx8, masked); report 6/6 and 3/3 added = removed; hardware blob advisory same as base. Pattern grep on
  added lines: only base64 fragments and agent-notes/kai.md named as brief source in TASKS (as before). No pdf; nothing
  from secretary/ or max-private/. Standards: ISO 4309 / EN 12927 / ASTM E1571 by number and clause, own words; no long
  quoted passage found near them. idscan 7f2b3f7..8beade9: 0. Old video absent from the export tip; v2 present (only a
  historical docs/paper/review_pack_manifest.txt still names the old file, as text).
- Tests in testtree19 (u41 venv): nine --check exit 0; ten SWS test files (p52 skipped) 181 passed.
- Snapshot on 36bc5cb: 38 M, 28 A, 1 D (old video); sws/ tree = export tip sws/ (3387953); docs/sws = export tip
  except the five unlinked pages. unlink16: index 6, report 1, easy 2, procedures 2, rig_sheet 1 (as before); 0 new.
  Switch: eight entries on eight menu pages, current once, targets exist; rig_sheet no switch, not on the menu.
  v2 video 4,108,176 bytes; video tags on report and easy -> sws_demo_v2_720p.mp4; no page names the old file.
- New links: index -> sensor.html#s-board, #s-ldlma, rig_sheet.html (1 each); easy -> #s-board 1, #s-ldlma 2,
  rig_sheet.html 1; hardware, housing -> #s-board 1 each; report -> #s-ldlma 1. Anchors exist once in the snapshot
  page. Note #s-board: GitHub blob view in MAx-Flow/SWS-Documentation of 2026-11-18-board/summary.md (#L1, L3, L9 x2,
  L11, L13), spoke_dependencies.md#L1, sws_sensor_candidates.md#L225 — committed in the snapshot, same paths in the
  export tip, cited lines are the cited items; report anchors (U91/U93 register sections, spec 6, spec 14) exist.
  Note #s-ldlma: report anchors only (U93 register x16, spec 6, spec 12, f_sync, verif3d 3D-D) — exist. The redline
  is not linked from any page: the report names sws/spec/REDLINE_2026-11-18.md as text (2) in the register; file
  committed in the snapshot. Relative links in new/changed .md (design_inputs, lma_sweep, verification): 0 broken in
  both trees; THEORY.md's six DOI links are already in the external set.
- Links tools/links19.py (= links18), export-v3/links19.txt (relative/own-repo/external, broken): index 388/0/0,
  report 506/63/39, easy 67/0/0, hardware 43/303/0, software 19/310/0, housing 88/163/0, procedures 116/20/0,
  sensor 85/102/2, rig_sheet 24/5/0; broken 0 on all nine; re-run on git archive of the commit: 0 broken.
- External: 38 distinct, same set as U90; 0 new, no HEAD sent.
- Visible text (visible19.txt; new blocks vs 36bc5cb with tools/visdiff19.py): sensor, index, easy, hardware,
  housing, rig_sheet new text 0 on every pattern (role words index 4, easy 2 are the old ones). Report's changed
  parts: 0 local paths, 0 snapshot notes, 0 personal names; but the new U91/U93 register sections carry "owner
  statement, 2026-11-18, relayed in the U9x brief" (10 new, same form as the 6 already there), dates 2026-11-18 (19)
  and 2026-10-07 (1, the spec's first issue), repo paths (sws/spec/REDLINE..., spoke_dependencies.md, demo out/...),
  and two old "spec l.298 / l.407" references in paragraphs reworded by U93. Not changed (snapshot = export tip).
  Print (headless Edge, snapshot copy, A4): rig_sheet19.pdf 5 pages, sensor19.pdf 5 pages.
- index.zip rebuilt: snapshot report.html + sws_demo_v2_720p.mp4 (the old video is gone), byte-checked, untracked;
  old at index.zip.before-u94. pubtree19 (+_titles, _unzipped) 626 files, 397 hits, per-file table identical to
  pub18; _titles 0. Snapshot increment: 2 owner-name hits added on re-rendered report.html, removed 2; advisory as
  above. Commit 67c6e1f (tree bacb73c = scanned staged tree); idscan 36bc5cb..67c6e1f 0. git status: only index.zip.
- Push commands (Kai's):
  git -C C:/Users/stian/export-v3/export push https://github.com/fjordbit/max.git main:main
  git -C C:/Users/stian/publish/SWS push origin main
  git -C C:/Users/stian/publish/SWS push maxflow main
- 14:56 done. Nothing pushed. Local main untouched (062b8bd).

— Mainsheet

# Lazyjack — U90 notes (17 Nov)

U90 builder (Opus): export increment for U89 (1cc9661..44a5b0e, max/ subtree, first-parent) grafted on e6e2c14,
Pages snapshot in publish/SWS on 7054acf, link proof on nine pages. Method as yardarm.md / futtock.md. No identifier
values, no personal names.

- 23:42 (machine clock) started; timebox 1 h.
- Start verified: Prosjekter-u05 main 44a5b0e = D:/git/prosjekter.git main; ls-remote fjordbit/max main e6e2c14 =
  export clone tip; publish/SWS 7054acf = ls-remote origin and maxflow. first-parent 1cc9661..44a5b0e = 1 (U89
  merge); increment touches only max/.
- Export: work/ refs/mono/main18; tools/replay18.py -> replay18 5698878, "exact". fast-export
  --reference-excluded-parents refs/exp/out17..replay18 (in18.raw.stream); tools/rename18.py: 1 command line, 0 in
  data, output == raw with the one replacement; rewrite_names: 49 commands / 5 blobs / 0 messages (rw18.log);
  fast-import -> export main 7f2b3f7 (parent e6e2c14, FF), worktree reset, clean. verify_diff vs 44a5b0e:max: same
  6 strategy paths (5 OK, 1 pptx only-in-original). refs/exp/out18 = 7f2b3f7 in work/.
- Front matter (10 answers; round.json, models.yaml): kind, round, backend, model, model_used, label, status,
  started/finished, seconds, dry_run, input_sha256, input_bytes, workdir and command (paths from "~": temp work dirs,
  CLI paths; cursor command also the workspace path from "~" and the one-line instruction; claude command flags and
  model), sent/not_sent (file names, bytes); round.json also detail (null) and file. models.yaml: one comment line
  (key test 16 Nov) and the model rows. No user name, no expanded machine path, no account/org id, no key fragment.
  Nothing changed.
- Scans (u05 venv): tiptree18 930 files, 660 whole-word, per-file table identical to tip17. addscan18: 47 paths
  (34 A, 13 M, 0 D). Whole blobs report.html 86, sws_data_sources.md 23, TASKS.md 7 = old known hits. Added lines 2
  (owner-name entry) on re-rendered report.html lines; removed side the same 2. Both round folders in full, the
  changed pages + builders, register rows, top page/README, messages: 0. Substring advisory: easy.html and
  index.html now appear as whole changed blobs; the same counts are in their base versions, none on added lines.
  Pattern grep on added lines: only https://github..., the known report.html owner line and agent-notes/kai.md
  named as brief source in TASKS (as before). No pdf; nothing from secretary/ or max-private/; the standard named
  only by number (on a re-rendered report.html line). idscan e6e2c14..7f2b3f7: 0.
- Tests in testtree18 (u41 venv): nine --check exit 0; ten SWS test files (p52 skipped) 181 passed.
- Snapshot on 7054acf: 12 M, 34 A, 0 D; sws/ tree = export tip sws/ (c489762). unlink16: index 6, report 1, easy 2,
  procedures 2, rig_sheet 1 (as before); 0 new. Switch: eight entries on eight menu pages, current once, targets
  exist; rig_sheet has no switch, not on the menu.
- New links: index, easy, procedures -> housing.html#ho-halves (1 each; anchor exists once in the snapshot page).
  From the note (div#ho-halves): 3D results and specification cited as report.html anchors (#p52-5-3d-results...,
  #verif3d-3d-b-..., #theory3d-5-..., #verif3d-limits-..., #spec-5-..., #spec-12-...) — all exist; GitHub blob view
  in MAx-Flow/SWS-Documentation: halves-force/summary.md (#L9, #L10, #L11, plain), release/summary.md (#L11, plain),
  procedures/rounds/2026-11-17-test-sheet/rig_top_page.md — committed in the snapshot and present at the same paths
  in the export tip; cited lines are the cited bullets. Relative links inside the new .md files (../../../3d/THEORY.md,
  answers/, brief_step1.md, ../2026-11-17-halves-force/[summary.md]) resolve in both trees.
- Links tools/links18.py (= links17), export-v3/links18.txt (relative/own-repo/external, broken): index 385/0/0,
  report 498/63/39, easy 63/0/0, hardware 42/303/0, software 19/310/0, housing 87/163/0, procedures 116/20/0,
  sensor 53/94/2, rig_sheet 23/5/0; broken 0 on all nine; re-run on git archive of the commit: 0 broken.
- External: 38 distinct, same set as U88; 0 new, no HEAD sent.
- Visible text housing/index/easy/procedures (visible18.txt): 0 on every pattern except role words index 4, easy 2
  (owner/designer) — identical in the 7054acf versions, not on added lines. Print (headless Edge, snapshot copy, A4):
  rig_sheet18.pdf 5 pages.
- index.zip rebuilt (snapshot report.html + old mp4, byte-checked), untracked; old at index.zip.before-u90.
  pubtree18 (+_titles, _unzipped) 597 files, 397 hits, per-file table identical to pub17; _titles 0. Snapshot
  increment: 2 owner-name hits added on re-rendered report.html, removed 2; advisory as above. Commit 36bc5cb (tree
  839e9b9 = scanned staged tree); idscan 7054acf..36bc5cb 0. git status: only index.zip untracked.
- Slip: a first scan command ran with a relative message path and fell through to a scan of export-v3/ as a whole;
  stopped, its stray counts file in C:/Users/stian removed, scans redone. No effect on the commits.
- Push commands (Kai's):
  git -C C:/Users/stian/export-v3/export push https://github.com/fjordbit/max.git main:main
  git -C C:/Users/stian/publish/SWS push origin main
  git -C C:/Users/stian/publish/SWS push maxflow main
- 23:54 done. Nothing pushed. Local main untouched.

— Lazyjack

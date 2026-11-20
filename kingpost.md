# Kingpost — U121 notes (20 Nov)

U121 builder (Opus): export increment 062b8bd..b5478a7 (max/ subtree, first-parent) grafted on 8beade9, Pages
snapshot in publish/SWS on 67c6e1f, link proof on eleven pages. Method as mainsheet.md / lazyjack.md / yardarm.md /
futtock.md. No identifier values, no personal names.

- 11:56 (machine clock) started. First run stopped on the 5 MB rule (report.html, 16,144,829 bytes); Kai ruled
  report.html exempt (the rule stands for every other file) and gave three conditions; resumed about 12:00.
- Start verified: Prosjekter-u05 main b5478a7 = D:/git/prosjekter.git main; ls-remote fjordbit/max main 8beade9 =
  export clone tip = work refs/exp/out19 (exported refs/mono/main19 = 062b8bd); publish/SWS 67c6e1f = ls-remote
  origin main and maxflow main. Backup branches on origin not touched.
- Increment (tools/incr20.py): 33 first-parent commits, all under max/; 396 paths (362 A, 34 M, 0 D), 46.5 MB at
  the tip. Largest: docs/sws/report.html 16.1 MB (exempt); next stand.json 1.49 MB, results.html 1.35 MB, index.html
  1.24 MB; nothing else over 1.1 MB. By folder: sws/3d (falsify 109, results 27, tradeoff 27, groove_plots 25,
  h40_on_38 18, figures 8, demo 9, notes 5), sws/line_beta 48 (c_half 10, tests 11, linebeta 12, figures 8),
  sws/transmitter 26, sws/data-path 21, sws/hw-selection 34 (element_run_3 21, element_round_1 7), sws/parts_table 5,
  sws/spec 5, docs/sws 17, tests 5, tasks 1, plus the four below.
- Kai's conditions: (1) U119: flow/examples-0.2-draft (make_sws_shiplift.py: one source line and the block type
  "3 x ADS131M08 [rev127]" -> "2 x ... [rev131]"; chart.json: the same type string in 24 places), twin/.../docs/
  architecture.html (one worked example 24 -> 16 channels, 480 000 -> 320 000 values/s), sws/figures/decided
  (two price PNGs re-drawn, U119 "price figures recomputed"); U95-U100: sws/data/sws_data_sources.md = register rows
  (10 added, 1 re-flowed). Each diff is what its commit says; nothing else. (2) rev131 .docx: rev124/127/128/129/130
  .docx already at 8beade9 sws/spec/. Produced by the existing route (forefoot.md, spec README): rev130 docx with 11
  text replacements + one revision-log row, rendered by render_spec.py; not a hand-edited master (the owner's Word
  master still needs the change by hand). Properties: core.xml title, description (a Claude Docs node id), revision;
  app.xml application and version; no author, last-modified-by, company or template; identical to rev130. Text:
  11 hits, all on lines identical to rev130 docx text (the file already public). (3) six logs + run_wire.sh: 0
  expanded paths, user names, host names, env dumps; solver output and a relative venv path only. Carried.
- Other STOP items: no PDF, no data-sheet copy, no compiled binaries/venvs/build/caches (line_beta and c_half source
  only); the prototype-head figures are calculated plots (looked at two), no drawing image; no customer or site
  name new; nothing from secretary/ or max-private/ (agent-notes/kai.md named as brief source in TASKS, as before);
  standards by number/clause, own words, no long quoted passage.
- Export: work/ refs/mono/main20 = b5478a7; tools/replay20.py -> replay20 ca7538d, 33 commits "exact"; fast-export
  --reference-excluded-parents refs/exp/out19..replay20 (in20.raw.stream); tools/rename20.py: 33 command lines, 0 in
  data, output == raw with the replacement; rewrite_names: 471 commands / 5 blobs / 0 messages (rw20.log);
  fast-import -> export main dd24591 (33 commits, FF of 8beade9), worktree reset, clean. verify_diff vs b5478a7:max:
  same 6 strategy paths (5 OK, 1 pptx only-in-original). refs/exp/out20 = dd24591 in work/.
- Scans (u05 venv): tiptree20 1319 files, 671 whole-word = tip19's 660 + 11 in the rev131 render; per-file table
  otherwise identical. Proof (tools/hitlines20.py): the 11 sit on 6 lines byte-identical to rev130 render lines with
  the same counts. addscan20: whole changed blobs with hits are report.html, make_sws_shiplift.py, chart.json,
  sws_data_sources.md, TASKS.md, architecture.html (old counts) + rev131 render; added lines 22 = rev131 render 11 +
  rev131 docx text 11 (both proven old); removed 0. Substring advisory (tools/subclass20.py): ordinary word or digits
  inside longer numbers, 2 inside base64 on results.html. Pattern grep on added lines: 0 user paths, 0 key/account
  shapes; "~/" only inside PNG bytes. idscan 8beade9..dd24591: counted 0 (site entry 10 hits, policy allowed).
- Tests in testtree20 (u41 venv): ten --check exit 0 (build, easy, hardware, housing, procedures, results, rig_sheet,
  sensor, short, software); test_sws_*.py: 209 passed, 2 skipped, 1 failed (test_sws_p52, no yaml) as expected.
- Snapshot on 67c6e1f: 26 M, 361 A, 0 D; sws/ tree = export tip sws/ (5dc73a1). unlink16 on eleven pages: index 6,
  report 1, easy 2, procedures 2, rig_sheet 1 (as before); results, parts 0. Switch: nine entries, Results second,
  on nine menu pages, current once, targets exist; rig_sheet and parts have no switch (parts opens from results, 217
  links; rig_sheet from index, easy, procedures, sensor, parts).
- Base address: every GitHub link on all eleven pages uses github.com/MAx-Flow/SWS-Documentation/blob/main (report
  one tree/main), incl. five iframe srcdoc figures on results.html with <base href=".../blob/main/sws/<folder>/">
  (tradeoff, groove_plots, h40_on_38, data-path, line_beta/figures; 25 links). From the MAx-Flow Pages site they
  land in the same repo's file view; from the fjordbit Pages site they land in the MAx-Flow repo, not fjordbit/SWS.
  Targets exist in the snapshot commit, which both remotes get. Same as every earlier page since U79 (the solved
  case), so not changed. Only if maxflow is not pushed do they point at the old tree.
- Finding fixed in the snapshot only: iframe 4 (line beta fig_b2) linked README.md#terms and #figure-b2 relative to
  sws/line_beta/figures/, where no README is: 2 broken. Repointed to ../README.md (sws/line_beta/README.md, headings
  "Terms", "Figure B2" exist). Source owed: sws/line_beta/figures/fig_b1-b4.html (and the builder) carry the same
  README.md links (8 in total).
- Links tools/links20.py (= links19 + results, parts), export-v3/links20.txt (relative/own-repo/external, broken):
  index 390/0/0, report 509/63/39, easy 69/0/0, hardware 41/284/0, software 20/305/0, housing 89/163/0, procedures
  117/20/0, sensor 86/102/2, rig_sheet 24/5/0, results 226/137/0 (+25 in iframes), parts 22/255/0; broken 0 on all;
  re-run on git archive of the commit (archcheck20): 0. External: 38 distinct, same set as U94; 0 new, no HEAD sent.
- Visible text (tools/visdiff19.py, new blocks vs 67c6e1f; visdiff20_report.txt): 0 local paths, 0 l.NNN, 0
  snapshot notes on every page. Role word "owner" as the status label "ruled by the owner": results 16, parts 18,
  hardware 2, software 1, one iframe 1. Report's changed parts: 24 repo paths (note and script names), 7 ISO dates
  and 4 day-month dates in the spec-history text, 18 "owner" + 1 "session" ("applied by an agent session, U119").
  Not changed (snapshot = export tip). Personal names: scan only (see below).
- Print (headless Edge, snapshot copy snapcheck20, A4): results 8, parts 8, hardware 5, software 6, rig_sheet 5,
  sensor 5 pages.
- index.zip rebuilt (snapshot report.html + v2 mp4, byte-checked), untracked; old at index.zip.before-u121.
  pubtree20 (+_titles, _unzipped) 1021 files, 408 = pub19's 397 + 11 rev131 render (proven old); _titles 0. Snapshot
  increment: added 22 (rev131 render + docx text, proven old), removed 0. Commit f74c6a4 (tree eb13a5b = scanned
  staged tree); idscan 67c6e1f..f74c6a4 counted 0. git status: only index.zip untracked.
- Push commands (Kai's):
  git -C C:/Users/stian/export-v3/export push https://github.com/fjordbit/max.git main:main
  git -C C:/Users/stian/publish/SWS push origin main
  git -C C:/Users/stian/publish/SWS push maxflow main
- 12:12 done. Nothing pushed. Local main untouched (b5478a7).

— Kingpost

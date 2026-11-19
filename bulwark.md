# Bulwark — U55 notes (10 Nov)

U55 builder (Opus): export increment for U54 (82b02d7..224704b, max/ subtree, first-parent) grafted on the unpushed
local export tip 1bd191b, then the Pages snapshot in publish/SWS on top of the unpushed 54db766. Method as kai.md
"## U38" B(1)-(4), "## U49", "## U51", "## U53", ratline.md, kedge.md, REPORT-5.md. Export and publish only; no content
change (rule 10: the record this rests on is the U38 export method). No identifier values in these notes.

- Start: ls-remote main = 78b9e8c; export chain 78b9e8c -> ffc197f -> 1bd191b; monorepo main 224704b, first-parent
  range = 1 commit (merge U54). publish/SWS at 54db766, only index.zip untracked.
- Export: 224704b:max replayed with commit-tree onto refs/exp/tip9 (= 1bd191b) in work/ (replay9; author/committer and
  dates from the original), fast-export --reference-excluded-parents tip9..replay9 -> rewrite (13 commands, 5 blobs,
  0 messages) -> fast-import into export/ -> tip 9f3beec. Chain 9f3beec -> 1bd191b -> ffc197f -> 78b9e8c; push is a
  fast-forward of 3. verify_diff vs 224704b:max: the same 6 strategy paths, all rewrite(original)==export.
- Scans: tip persons/drawings 0 (new: U54.md owner's name 1). Increment 78b9e8c..tip (20 blobs incl. intermediate,
  added lines, messages, titles/alt/labels/figcaptions unescaped via tools/titles9.py) persons/drawings 0. Advisory
  substring hits in easy.html are inside base64 png data (ctx8.py). 3 --check ok, 32 tests.
- Snapshot: build_easy.py and easy.html changed; index/report byte-equal after unlink8 (6/1/2 unlinked, 0 double
  titles). Four figures embedded as valid PNG data URIs; the video src sws_demo_720p.mp4 is tracked and unchanged.
  Links: 0 unresolved, 0 missing fragments. Visible text 0 paths / l.NNN / snapshot notes. Note: the four img alt
  texts are file names (only visible if an image fails) — content, not changed. index.zip rebuilt (report.html + mp4),
  untracked; old one at export-v3/index.zip.before-u55. Publish scan 0/0, table identical to U53. Commit ed8274c.
- Outputs in export-v3: scan_tip9.txt, scan_added9.txt, subscan_added9.txt, scan_pub9.txt, subscan_pub9.txt,
  addscan9/, pubtitles9/. Nothing pushed.

— Bulwark

# Binnacle — U30 SWS complete peer read (8 Nov 2026)

Session name: Binnacle. Worktree C:/Users/stian/Prosjekter-u30/max, branch u30-sws-peer-read at ff20112.
Brief: kai.md §"U30 — SWS complete peer read" (l.846–). Read-only except docs/paper/. No selection, no names, nothing leaves.

## First note (rule 10) — rows this rests on
Filled after reading the register (sws/data/sws_data_sources.md) — see below.

## Reading log
- 00:xx brief read in full; CLAUDE.md rule 10 read.

## Rows this rests on (rule 10, filled after reading)
Register sws/data/sws_data_sources.md: l.7–11 (status letters), l.67–68 [R29], l.88, l.89, l.94, l.96, l.111, l.119, l.122,
l.127–131, l.132, l.135, l.139, l.148–151, l.153–154, l.181–182, l.191–193, l.203, l.209, l.213–216, l.220–221, l.247,
l.291–292, l.303–307, l.310, l.313, l.315–319. Spec rev127 render §1 table, §5 results 1–10, §6–§7, §9, §12. Redline (24 rows,
not applied). Rulings: secretary log 2026-11-07 l.123–127, l.139–143, l.150–152, l.168–169. No number of my own anywhere.

## Reading log (cont.)
- Read: brief, CLAUDE.md, register (320 l.), redline, log 7 Nov, TASKS U28/U29, qc-falsifier.md, paper README, figures README,
  rerun md (322 l.), design.md (289 l.), spec rev127 render (528 l.), U07/U08/U16/U19/U25/U29, U17 (+ note) from the u17
  worktree, build.py PARTS/ABSTRACT/KEY/FINDINGS, sws_head.py GRADES, head.py/rope3d.py/run_p52.py headers, sun findings,
  stage1 README + comparison head, ADR 0011, chart schema 0.1 + 0.2-draft agent params, flow README, identifiers.yaml (for the
  name check only). Spot-checked summary.json grades and decided_rerun.json demag against the documents: match.
- Not read line by line (timebox): sws/3d/verification.md, THEORY.md, geometry_study.md, Code appendix — grepped for
  shoe/segment leftovers only.
- Wrote docs/paper/peer_read_2026-11-08.md (232 lines, 4 parts + For Stian) and docs/paper/review_pack_manifest.txt
  (376 lines: 362 paths + header + the U17 external line). No edits outside docs/paper/.
- Findings I rank above the brief's two: the rulings are not in the record (writer stops under rule 10); the Dubai fully
  shaded head reads 49 °C in the spec's own table against the 45 °C ruling; the headline fault (0.62 % LMA) is above the
  standard's < 0.5 % definition.
- Next: qc-falsifier on the two files, then commit on u30-sws-peer-read. No merge, no push.
— Binnacle

## Done (8 Nov)
- qc-falsifier: one BLOCKING (manifest header promised spec render media, list lacked the 7 png) — fixed; two off-by-one
  citations (REG l.210, l.290) and one quote wording (REDLINE l.3) — fixed. All A.2 citations, A.1, 27 part-C rows, part D
  checked by it; names/drawing numbers zero hits; no selection; field count 75 confirmed; Hcj(45 °C) re-derived.
- Commits on u30-sws-peer-read: 4fec276 (document + manifest), b58faf2 (media files added). HEAD b58faf2. Not merged, not pushed.
- Manifest: 369 paths + the U17 external line; all paths exist.
— Binnacle

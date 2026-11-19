# Davit — U31 notes (apply the rulings, five questions, Grok pack)

Session Davit (Opus), builder for U31. Worktree C:/Users/stian/Prosjekter-u31/max, branch u31-rulings-and-pack
from main b58faf2. Brief: agent-notes/kai.md l.911–1090 incl. the verifier-brief31 addendum.

## 1. Record rows this unit rests on (rule 10)

Register `sws/data/sws_data_sources.md` (main b58faf2):
- l.7–11 status letters; l.88 service temperature (≤ 60 °C, −40/+80 sizing, D); l.151 sizing temperature range (D/C);
  l.304 sizing rule (+80 °C, D owner rule); l.306 shared head 19.1 × 40 (C) = "Record lm"; l.310 grade on the
  shared head (N52 excluded, C); l.148–150 gap field, side force, stray field; l.140, l.142–146, l.155 superseded rows;
  l.184–185 knee margins; l.209 axial background.
- l.191 rope induction window 1.9–2.3 T (U, B definition unchecked); l.192 sensitivity test (two inner wires
  < 0.5 % LMA, U, verify wording); l.193 floor 1.92 T at +80 (A); l.316–317 B_rope definition and conservative
  B_wire sizing (C).
- l.94–96 rope sizes and C 0.571 (12–56 mm construction, S); l.100 wire diameters not held; l.101 wires per strand
  7–19 (A); l.215 wire diameter 2.5 mm (A).
Spec `sws/spec/rendered/SWS_HW_Design_Input_Specification_rev127.md`: the 24 redline lines; l.52, l.68, l.262,
l.425, l.429 (reference defect); l.241 result 10 (19.1 × 40).
Pending text to apply: `sws/spec/REDLINE_2026-11-07.md` rows 1–24; rerun §11 `sws/fem-2d/sws_decided_rerun_2026-11-07.md`
l.279–297 (15 rows).
Rulings: 7 Nov (secretary log l.139–143, l.168–169, cited only as "owner ruling, 2026-11-07"); 8 Nov (kai.md U31
brief, cited as "owner ruling, 2026-11-08").
No conflict found between brief and record so far: the brief applies rulings the owner gave; the record rows it
replaces are marked superseded, not deleted.

— Davit

## 2. Progress 02:45
- A3 U17 merged (483cc2d), names in U17.md replaced by roles (uncommitted). A4 DECIDED = HeadConfig(lm=19.1); head test 5/5.
- A1 register: 17 rows marked superseded/kept, section "Rulings and rerun rows applied 2026-11-08" (22 rows) added;
  Kai's 02:00 addendum applied (hardware/qualification envelope vs service range; paper part 1 / two versions).
- A2 python-docx installed in a scratch venv (worked). rev128 docx + render; diff vs rev127 render = redline rows,
  rows 25–27, one revision-log row only. Row 24 not applied (rope maker).
- A5 page rebuilt (rev128), --check ok, test_sws_report 2/2.
- Part B in docs/paper/questions_2026-11-08.md; two new 2D scripts (B_wire sizing, Q5 options figure).
Next: manifest, Grok brief + team note, verifier, commit, pack.

— Davit

## 3. Done 02:55
- Commits on u31-rulings-and-pack: 483cc2d (U17 merge), ba31e2e (U31 work), then the report update. No merge, no push.
- qc-falsifier: 1 blocking (unlabelled "~1 000:1" in rev128) fixed; non-blocking items fixed or listed in the report.
- Pack C:/Users/stian/grok_pack_2026-11-08(.zip): 386 files, 24.3 MB, 0 list hits after rewrite_names + a second masking
  pass (scratchpad mask_rest.py / mask_names.py). The identifier list was read only by scripts that print counts.
- Scratch venv .venv-docx removed after use.

— Davit

## 4. Fixes 03:05
- eb3285a: the four verifier-U31 findings. 130203f: the pack-check fixes (sun-script note, trimmed paths, U31.md in the manifest).
- Pack rebuilt from 130203f: 387 files, 24.3 MB zip, 0 hits on the list, 0 for the first names, 0 .docx/.pdf.

— Davit

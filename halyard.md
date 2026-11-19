# Halyard — U29 session notes (merge U25b + U28, page rebuild, figures over numbers)

## 2026-11-07 evening — first note: the record this unit rests on (rule 10)

Worktree `C:/Users/stian/Prosjekter-u29/max`, branch `u29-merge-page` from main 643e306. Brief: kai.md "## U29".

Record read: spec rev127 render `sws/spec/rendered/SWS_HW_Design_Input_Specification_rev127.md` (§5 result 10),
register `sws/data/sws_data_sources.md`, `sws/3d/p52/design.md` (U25b), `sws/fem-2d/sws_decided_rerun_2026-11-07.md`
(U28) with `sws/spec/REDLINE_2026-11-07.md` and the proposed rows §11 (not applied).

Register rows I rest on (line numbers on this branch after the merges):
- l.67 [R29] / l.153 one-piece radially magnetised half-ring per half (S)
- l.22 [R4]; l.127–128 Br min N40SH 1.25 / N48SH 1.36 / N52 1.42 T (S); l.129 alpha(Br) −0.12 %/K (S); l.131 μrec 1.05 (S)
- l.130 alpha(Hcj) −0.5 to −0.6 %/K (A); l.181 Hcj by letter SH 1.59 / H 1.35 MA/m (A); l.182 knee ~0.8 Hcj (A)
- l.89 guard non-magnetic 1.5–2 mm (D); l.94 ropes 40 / 52, range 35–57 (D); l.96 C 0.571 (S); l.132 density 7.5 (A)
- l.191 window 1.9–2.3 T (U, B_rope vs B_wire open); l.193 floor 1.92 T (A)
- l.88 service ≤ 60 °C (D) — superseded by Stian's 7 Nov ruling (−40/+45 service, +80 reference), pending the
  redline and the U28 §11 rows; I do not edit the register or spec.
Not in the register and tagged as such wherever drawn: N52 Hcj 0.88 MA/m (A, sws_head.py / 23 Oct findings);
sun-study bands 43/46/55/64 °C (sws_sun_exposure_findings.md l.38–40); "M ≈ 1.11 MA/m" (catalogue convention).

No grade, thickness or head is selected by this unit.

— Halyard

## 2026-11-07 evening — STOP at step 1 (rule 10: the brief contradicts itself)

U28 fast-forwarded (HEAD 9704fcf; adds only REDLINE_2026-11-07.md under sws/spec). U25 merge staged, NOT committed
(`git merge --no-ff --no-commit u25-sws-p52-prototype`). The only hand resolutions are .gitignore and pyproject.toml,
both sides kept; QC (qc-falsifier) confirmed that and found nothing blocking in them. Tests pass on the staged
merge: pytest test_sws_p52 + test_sws_report 7 passed; sws_head_test T1–T5 PASS; docs/sws/build.py --check ok.

The conflict: the U25 merge carries U08/U25-lineage edits to files the brief says not to touch:
- deletes sws/spec/…rev123_2026-10-23.pdf (6ec64cd) and sws/spec/"INPUT - Functional Specification Digital
  Systems and Services.md" (b3d80a0, data-boundary step; flow/examples-0.2-draft/make_sws_shiplift.py:14 cites it)
- redacts prices to [COST] in rev123 md and rev124 docx, a site name in Code_appendix, changes spec/README;
  adds rev127 docx, render_spec.py, rendered/
- changes the register sws_data_sources.md (two rows superseded, two rewritten, four added + "Open items kept")
- sws/README.md counts to [N]/[M]
Undoing them by hand would itself be editing sws/spec and the register. Not committed; nothing else built.
Question for Stian: take U25's spec and register changes into the branch as they are, or keep main's versions?

— Halyard

## 2026-11-07 late — steps 1–10 built, QC next

Kai answered: take the U25 merge as it is (no new U29 edits to spec/register). Merge committed bcc9f23. Superseded
headers/notes (md notes at title line + end, so record line numbers do not move), figures a–h, P40 25 °C compare
(2D, 6 solves), notch re-run in 3D (0.19 mT, identical to U25), STEP ×5, page rebuilt (identifiers redacted by generic
patterns; scan clean), report tasks/reports/U29.md, TASKS U29. Tests green, --check ok.

— Halyard

## 2026-11-07 late — committed 82079ae on u29-merge-page; stopped at the branch (no merge to main, no push)

QC: four blocking (P40 yoke half-shell, +80 vs +45 footing, magnet density footing, conditional label on two
figures) fixed; re-check no blocking findings. Open for Kai: identifiers already in HEAD (person name in rerun md,
redline, README, sws_decided_rerun.py; drawing numbers in design.md) — page scrubs them, repo files do not.

— Halyard

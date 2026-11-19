# Transom — U39 builder (short SWS page)

## 9 Nov 2026, start

Session Transom (Opus), U39 per kai.md "## U39" (l.1537). Worktree C:/Users/stian/Prosjekter-u39, branch
u39-short-page from 2e8ebf9; working in .../Prosjekter-u39/max.

Rows this rests on (rule 10): register l.7–11 (status letters); l.127–131 (Br, alpha, mu_rec); l.181–182 (Hcj by
grade letter, knee 0.8 Hcj, A); l.191–192 (EN window U, sensitivity test U); l.313 (bore clearance); l.316 (B_rope
definition); l.329 (−40/+80 initial envelope, no longer the hardware limit); l.330 (service ≤ 45 °C magnet);
l.333–335 (sizing rule, lm per head and grade, record lm); l.341 (N52 Hcj 0.88 A); l.346 (head mass); l.348 (§14 as the
minimum, wire count U); l.349 (report scope: management chooses); l.360 (hardware range −40/+50 ambient, D);
l.361 (storage: owner defines, U). Owner statement 8 Nov late evening (U36 addendum in kai.md) is not in the
register: cited as the coordinator's record, status "not yet a register row".
Number sources: docs/paper/figures/q5_options.json (Q5 table), sws/data/envelope_excursion.json (U36 table A),
sws/fem-2d/sws_decided_rerun_2026-11-07.md "Knee history", sws/3d/p52/design.md §2, §7.

— Transom

## 9 Nov 2026, done

Short page built: docs/sws/short.html (4 printed A4 pages), docs/sws/build_short.py, tests/test_sws_short.py; long page
gained parts q5 and u36, fig-<name> ids and a link line. 329 number links, all to long-page anchors; one citation
(questions Q1 l.48) to the repository file. qc-falsifier: no blocking findings; its non-blocking points fixed except
q5_options.py knee40 label (outside U39) and the pre-existing identifier hits in index.html (same at 2e8ebf9).
Not in the repo: the owner's late-evening storage / procurement statement; the page cites it as the coordinator's
record, without numbers. Report tasks/reports/U39.md. Committed on u39-short-page; no merge, no push.

— Transom

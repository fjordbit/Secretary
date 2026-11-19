# Taffrail — U36 builder notes (spec rev130, temperature envelope)

- 8 Nov: name claimed. Record rows follow after reading.

## 2026-11-08 22:5x — started
- Unit / branch: U36 / u36-spec-envelope from d5db50c (C:/Users/stian/Prosjekter-u36, work in max/)
- Record rows I rest on (register sws/data/sws_data_sources.md, d5db50c line numbers):
  l.7–11 status convention; l.130 alpha(Hcj) A; l.131 mu_rec S; l.151 temperature range for sizing (superseded as
  sizing T); l.181 Hcj by grade letter A; l.182 knee 0.8 Hcj A; l.186 FAT close-out +80 soak D; l.329 hardware /
  qualification envelope −40/+80 D, origin A; l.330 service range −40…≈45 °C D; l.331 +80 qualification reference D;
  l.332 temperature method D; l.333 sizing rule; l.334 lm per grade (15.84 N52, 16.58 N48SH); l.339–341 knee margin,
  N52 status, Hcj N52 0.88 A.
- Spec rev129 render l.11, 233, 334, 367–376, 384/386 (stay), 428, 429, 497, 506; REDLINE rows 1–31.
- Model: sws_knee_history.py one(...) (U34 A model past the knee), rerun md "Knee history, 2026-11-08".
- Owner ruling 8 Nov evening as quoted in kai.md U36. Rule 10: no number selected; storage max is the owner's.
— Taffrail

## 23:2x — B and C drafted, A running
- Register: l.329 origin corrected + marked; l.331/l.332 "Needs Stian" notes; l.186 soak superseded note; new section
  with 4 rows (ruling D, operating −40/+50 D with U relation to 45 °C, storage U, soak/cycling U).
- Spec rev130 docx built from rev129 run by run (scratch venv outside repo); storage max as placeholder; render diff
  touches l.11, 233, 334, 367, 376, 428, 429, 497 + log row. l.36 carries the same envelope wording, not in brief: left.
- Note: no register row ever carried −40/+70 operating or +85 storage (spec-only numbers).
- A: 90 cases (sws_envelope_excursion.py → one()), first case reproduces U34 −29.0 mT.
— Taffrail

## 2026-11-08 — committed
- Unit / branch: U36 / u36-spec-envelope (C:/Users/stian/Prosjekter-u36)
- Commit: a20291b — spec rev130 envelope, register rows, 2D excursion table; no merge, no push
- Ready for Kai's check: yes (qc-falsifier: no blocking findings; N1–N3 fixed)
- No "U36 addendum" in kai.md at finish: storage max left as "+[owner value] °C".
- Not edited, flagged: spec l.36 and l.385 carry the old envelope wording (outside the brief).
- Needs Stian: storage max; +50 vs 45 °C; rev130 → Word; l.331/l.332.
— Taffrail

## 2026-11-08 — follow-up committed
- Commit 176e0c7: spec l.36 / l.385 envelope wording (redline rows 41–42); "ambient at the sensor" cited as the editor's reading, Needs Stian. Checks pass. No merge, no push.
— Taffrail

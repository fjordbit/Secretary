# cuddy — U113 element round 1 (builder notes for Kai)

- Worktree C:/Users/stian/Prosjekter-u113, branch u113-element-round from 213e36c (verified = tip of u111-element-run).
- Adds only max/sws/hw-selection/element_round_1/: element_round_1.md, answers/ (three answers unchanged + summaries.md),
  r_arith.py, results/arith.json. Commit 0384308. No merge, push or export.
- scan_tree on the three answers BEFORE copying: 0. After: scan_tree 0 (7 files); idscan 213e36c..HEAD 0.
- Git normalises CRLF to LF in the stored answers (content otherwise byte-identical to the source files).
- Sheets read by a sheet-reading subagent (part numbers only); its raw readings are in my scratchpad (sheets.md), not in
  the repo. Not read: TLE4997, HMC1021, AKM HG/HW, TMR2617S-AAC. TLV493D, TLI5590, MLX91205 from third-party copies.
- Key finds: Grok offers CT100 as through-package (sheet: in-plane) — the hunted error. TMR4xx / TMR62xx Z parts do not
  exist. NVE AA/AAH/AAL are omnipolar GMR, <= 3.5 mT. DRV5055 at 3.3 V: 2 mA typ / 4 max (run 3 right; Opus 6, Grok
  6-10 wrong); its zero drift +-1 % VCC is TYPICAL only, no max, vs 25 C: run 3's 0.71 % is a typical half-band.
  Grok's stainless skin depth (~1 mm) is ~40x too small. Codex' converter gains clip.
- Tally agrees/differs: Opus 17/2, Grok 15/7, Codex 13/6 (each +-2; judgement which figures count).
- Figure: none (categorical comparison; standard draws curves on a numeric axis).
- Falsifier (fresh subagent, files only): 5 blocking, all fixed: DRV5055 drift marked not comparable (tallies changed),
  Grok misquoted on "no damage", 3-axis noise sentence, easy-read Hall paragraph firmer than dense part, a question
  misattributed to Codex. Minor fixed: draft scope, gain arithmetic, 3-5x, 10.8 mT, dates, steering words, uneven
  marks. No second pass.

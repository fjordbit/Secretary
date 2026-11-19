Session name: Flux (U7/U8 SWS magnetics). Every entry ends with — Flux.

# U7/U8 work session — notes to Kai

## 2026-10-29 20:20 — status
- Unit / branch: U07 accepted, U08 in progress / u08-sws-3d (C:/Users/stian/Prosjekter, work in max/; no separate worktree)
- Last commit: 86ea9ea — closures: bond line and can, demagnetisation, off-centre rope, force between the halves
  (earlier on this branch: 7f26813 U07 … b45c74d rope range / domain size; all pushed to github-max as u08-sws-3d)
- Running now: the two refined demag runs that were stopped for memory (H52 magnet mesh 0.8 mm; W70 1.2 and 0.8 mm),
  sequential, 8 threads; results go to sws/3d/results/demag_3d_refined_{H52_08,W70}.json, to be merged into
  demag_3d_refined.json, then the table in sws/3d/verification.md, QC (qc-falsifier), commit, push.
- Ready for Kai's check: not yet (waiting for those runs; I will write a note with the hash).
- Will not merge u08-sws-3d into main (noted).
- Needs Stian: hours.human / hours.model in tasks/reports/U07.md and U08.md ([FILL]); bore-vs-guard convention
  (sws/3d/rope_range.md); which wide head is live and the TMR background range (U9); B_rope definition;
  tolerance and acceptance for the three 3D checks; OK for the params.yaml edits (W65, W70 heads).
- Untracked on purpose, not mine to commit: sws/3d/demo/cmp.png (QC scratch), sws/hw-selection/geometry_stack.json,
  two +25C 3da figures (regenerable).

## 2026-10-29 — committed
- Unit / branch: U08 / u08-sws-3d (C:/Users/stian/Prosjekter, work in max/)
- Commit: f4d5e22 — demag refined runs completed (H52 0.8 mm, W70 1.2 mm; W70 0.8 mm beyond NGSolve's size limit, recorded as not run)
  Pushed to github-max as u08-sws-3d (subtree 2a50893). Branch since main/U07: 7f26813 … b45c74d, 86ea9ea, f4d5e22.
- Ready for Kai's check: yes. QC (qc-falsifier) no blocking findings on every commit; `python docs/sws/build.py --check`
  ok, `pytest tests/` 6 passed. Not merged into main.
- Untracked, not part of the work: sws/3d/demo/cmp.png (QC scratch), sws/hw-selection/geometry_stack.json,
  two +25C 3da figures (regenerable). Git-ignored: sws/3d/out/ (video, VTK, STEP, deck), sws/3d/logs/.
- Needs Stian: hours [FILL] in tasks/reports/U07.md and U08.md; bore-vs-guard convention (sws/3d/rope_range.md);
  which wide head is live and the TMR background range (U9); B_rope definition; tolerance and acceptance for the
  three 3D checks; OK for the params.yaml edits (W65, W70).

## 2026-10-29 late — re-check of the six "Needs Stian" items (Kai's standing rule)
- found: B_rope = flux in the rope's METALLIC cross-section at the sensor plane / C·d² — spec rev123 l.137 (rev124 docx same text, §5 "Target"); target 2.0 T in the EN 12927 Ch.14 window 1.9–2.3 T. Not an open question; removed.
- found: wide head live = bore 70 (W70) — spec rev123/124 result 9 addendum ("the bore moves from 65 to 70 mm") and result 10 table ("wide 35–57, clearance bore 70"; 65 is "optional"). Owner 2026-10-29: test one-size-fits-all first, then two sizes; one head per rope size is the main check and most likely product.
- found: params.yaml W65/W70 values are the spec result 10 table rows verbatim (bore, lm, yoke) — no owner OK needed; removed.
- found: TMR background range is computed, not asked: worst −90.6 mT (W65/35, hard, −40 °C, 3 mm), −69.2 mT without W65 (sws/3d/results/box_offset_2d.json); requirement form is spec l.298 (linear range ≥ 2 × (background + largest signal)). Goes to U9 as a number.
- found (owner 2026-10-29): bore = the drilled hole; the guard lines it and reduces the free space. Applied as D_b (drilled) / D_f = D_b − 2·t_g (free); figure sws/3d/figures/definitions.png. The spec's own ODs (Ø103/126/136/139) show the FE heads' "48/60/65/70" is D_f, so spec l.459's 0.96 mm is for a head 4 mm smaller than modelled; correct clearance of the modelled H52 is 2.96 mm.
- found (owner 2026-10-29): hours.human ≈ 350 h total in Syncrolift (≈ 8 weeks × 37.5–40 h + extra), of which Twin 50, agentic 50, Saronic 30 → SWS ≈ 220 h incl. introduction and two office weeks; not split per unit. hours.model from session logs (10-min gap rule): U07 2.4 h, U08 14.6 h (5/30-min rule: 2.2–3.4 / 11.0–18.0). Earlier SWS work in claude.ai chats is not in the logs.
- still open: a numeric tolerance for the three 3D checks. Checked ADR 0003 (says "reported with tolerance", gives none), TASKS.md U8 (points to verification.md), VERIFICATION_PLAN.md, stage1/compare.py (criteria A/B are relative to each solver's own numerical uncertainty, not fixed numbers), deltas (all say "no tolerance set before the run"). Proposal going to Stian with a derivation rather than a bare question.

## 2026-10-29 late — committed
- Unit / branch: U08 / u08-sws-3d (C:/Users/stian/Prosjekter, work in max/)
- Commit: 8ca8223 — design inputs: bore definitions (figure), magnet-thickness sweep, TMR range derivation, sizing plan, hours.
  Pushed to github-max as u08-sws-3d (subtree 3dc6b95). Report page republished (claude.ai artifact, version 10).
- Ready for Kai's check: yes. QC (qc-falsifier) no blocking findings after three passes; build.py --check ok; pytest 6 passed. Not merged.
- Correction to my re-check note above: the human-hours line is now quoted verbatim with two readings (a) SWS ≈ 220 h derived,
  (b) 350 h SWS alone, marked [OWNER TO CONFIRM]; the third project's name is not in the reports.
- Still open for Stian (after checking the spec, deltas, file map, ADRs, reports, READMEs, git log): (1) hours reading (a) or (b);
  (2) drawing tolerances for magnet / seat / yoke / length (design_inputs.md §2); (3) largest LMA signal for the TMR linear range;
  (4) keep the modelled heads (free bore 48/60/70) or drilled 48/60/70 (a smaller head, re-size); (5) a numeric 3D-check tolerance
  (none in ADR 0003, TASKS, VERIFICATION_PLAN, compare.py, deltas); (6) one-strand (40) / two-strand (52) reference defect is not
  in the spec (l.56, 100, 407 define one defect type for all sizes).

## 2026-10-30 — committed
- Commit: 4c88b7d — owner decisions 2026-10-30: hours reading (a) (SWS ≈ 220 h, derived), keep the modelled heads.
  Pushed (subtree d712736); report page version 11. QC no blocking findings. Ready for Kai's check: yes. Not merged.
- Closed with Stian: hours reading; drilled vs free bore (keep modelled heads). Still open: drawing tolerances, largest LMA
  signal, numeric 3D-check tolerance, per-size reference defect (one/two strands) not in spec.
- Next (owner's request 2026-10-30): geometry study for the best reading at equal rope induction (1.92–2.30 T at all corners):
  first a theory note (reciprocity/adjoint split of the defect signal) checked on the yoke cut-out case (fem-2d/sws_yoke_window.py),
  then candidate geometries. Will extend existing tools, not fork them.

## 2026-10-30 — committed (Kai's three publish blockers + geometry study)
- Commit: b3d80a0 on u08-sws-3d (pushed to the private github-max only; NOT to fjordbit/SWS). QC (qc-falsifier) no blocking findings.
- Ready for Kai's check: yes.
1. Site name → "[OTHER PROJECT]", 16 replacements in the 5 listed sws files, only that word changed (CRLF kept);
   `git grep -i <name> -- max/sws max/docs/sws` returns nothing. SWS_FILE_MAP.md notes the edit (sha prefixes are of the originals).
2. Twin FD: identical (cmp + sha256) to C:/Users/stian/Prosjekter/"INPUT - Functional Specification …md" → git rm'd from sws/spec;
   sws/README.md and SWS_FILE_MAP.md updated; no other references.
3. Page: hours.human rows of the rendered unit reports replaced by the SWS total only (build.py PUBLIC_HOURS_HUMAN / public_md);
   no quote, no personal time. The unit reports keep their rows.
   Optional done: build.py skips PARTS whose file is missing (tested in a copy without tasks/). Known cosmetic: lede/footer
   part numbers are fixed text, so in an SWS-only build they say "Parts 8–13 / 1–13" while fewer parts render.
- ESCALATION (QC finding, outside my unit, not changed by me):
  a) the same name is still in 6 tracked files under max/twin/Shiplift-twin-analysis/ (README.md, docs/*.html, decision-log.md) — U10's folder;
  b) HISTORY: max/sws history before b3d80a0 contains the name (5 files), and earlier pushed page versions (e.g. 4c88b7d on
     github-max/u08-sws-3d) contain Stian's verbatim hours quote. A history-preserving split of max/sws would publish both.
     fjordbit/SWS must be built from a fresh, history-less snapshot of the fixed tree (or history rewritten). Kai/Stian to decide.

## 2026-10-30 — committed (Kai's follow-up: prices, counts, clock times)
- Commit: ce55299 on u08-sws-3d (pushed to private github-max only; NOT fjordbit/SWS). QC no blocking findings. Ready for Kai's check: yes.
- Prices → [COST]: 13 each in spec rev123 md (l.254, 269, 284–288), rev124 docx (text runs only; XML otherwise identical),
  rev123 pdf (true PyMuPDF redaction; QC decompressed every stream: no "EUR" left; images, links, TOC unchanged).
  Method script kept outside the repo (job tmp, redact_cost.py); PyMuPDF added to the local venv only.
- Counts: sws/README.md:13 → "[N] hoists per side … [M] units total". KEPT as model inputs: spec l.279 "200 sensors = 400 halves"
  (cost basis) and "64 per root box" (channel count).
- Page: hours.model rows show dates only (build.py public_md); unit reports keep their times.
- For Kai/Stian (QC non-blocking, not changed by me):
  N1 pushed history on github-max (main, u08-sws-3d) still has the old counts, prices (md/pdf/docx) and the hours quote → fresh snapshot for fjordbit/SWS.
  N2 site names in sws/: "Dubai" (spec §9 l.343, l.464; pdf), sws/data/sws_data_sources.md:151/238/241, due-diligence/sws_sun_sites.py,
     sws_scripts_README.md; also "Northern Norway", "Houston". Generic climate cases or real project sites? Stian to say.
  N3 "200 units" as a series size: spec l.306 ("200 units, 10-year support") and l.394 ("before 200 units are built"), also pdf/docx —
     same ruling as l.279 (model input) or a project count?

## 2026-10-30 — correction to my "found" notes (spec owner's answers, kai.md)
- WRONG earlier: "found: wide head live = bore 70 (W70)". Spec owner 2026-10-29: Ø70 WITHDRAWN; wide head = Ø65, an option, not rev 1.
- WRONG earlier: "found: B_rope = flux / metallic area — not an open question". It IS open (status U) until Stian reads EN 12927 §14.
  Every SWS doc and the page now state that their numbers use B_rope = flux / metallic area C·d².
- Owner's delivery (sws_geometry_stack.py + geometry_stack.json, sws_head.py B_wire output, fem-2d consolidated and review findings,
  data/sws_data_sources.md, carrier brief): NOT in this tree. sws_geometry_stack.py still subtracts the guard (line 33); sws_head.py
  has no B_wire output. The untracked hw-selection/geometry_stack.json is an old output (dated 2026-10-23, double-subtraction values),
  not the delivery. Not recreated. B_wire values are [PENDING: B_wire] until the delivery lands.

## 2026-10-30 — committed (spec owner's answers applied)
- Commit: 5e1f289 on u08-sws-3d (private github-max only). QC no blocking findings. Ready for Kai's check: yes.
- Applied: Ø70 withdrawn (params.yaml W70 status, rows kept as data), wide head W65 option not rev 1; B_rope definition open —
  design docs + page say B_rope = flux / metallic area; B_wire [PENDING] until the owner's delivery lands (not in tree, not recreated);
  tolerance proposal recorded with BOTH readings: rope induction passes everywhere; sensor field passes only against the band of the
  two 2D solvers (≤0.095 mT), not against either alone (up to 0.285 mT; the 2D solvers differ by up to 0.338 mT) → Stian decides;
  U9 design point ~75 mT, wide head ~91 mT; yoke provenance per owner.
- Next (Stian "go for it"): geometry study §4 (concentrators rejected, stand-off strongest lever) — separate commit.

## 2026-10-30 — name
- From now on this session signs as Flux.
— Flux

## 2026-10-30 — committed (geometry §4; spec owner's delivery + B_wire)
- dace0f1 — geometry study §4 (concentrators rejected; stand-off 3→2 mm +20–40 %; lm 26 +14 %). QC no blocking findings.
- caa522e — spec owner's delivery applied (7 files copied unchanged from new/…; new/ untouched; no later edits were overwritten);
  B_wire per row in rope_range_2d.json: every head ~0.016 T below 1.92 T at its sizing corner; B_wire ranges H40 35, H52 47,
  W65 51 mm. QC no blocking findings. Pushed to private github-max (subtree fbb0def); page v14.
- Ready for Kai's check: yes. Not merged; not pushed to fjordbit/SWS.
- Reminder (QC): max/twin/Shiplift-twin-analysis/ on this branch still holds the project identifier (fixed only on u10-twin-design,
  6c7b03d). Do not publish twin/ from u08-sws-3d.
- For the spec owner (QC, non-blocking): delivered text gives the bore for 3 mm movement as Ø60/Ø65; the script prints 60.1/65.3.
— Flux

## 2026-10-30 — published
- Kai: fjordbit/SWS holds a history-less snapshot of caa522e; final scan clean. Later updates: "ready for Kai's check"; I never push to fjordbit/SWS.
- Next (on Stian's go): geometry study — radial channel with the same figure of merit; mechanical check of a 2 mm stand-off.
— Flux

## 2026-10-30 night — committed (geometry §5)
- Commit: see `git log -1 u08-sws-3d` (U08 SWS geometry study §5), pushed to private github-max only. QC no blocking findings.
- Ready for Kai's check: yes. The claude.ai report page was NOT republished (Stian: the manager reviews it in the morning);
  docs/sws/index.html in the repo is rebuilt and in sync. Publishing the new findings 15 is Kai's/Stian's call.
- Content: radial channel (bare: ignores uniform lift-off; lateral movement term from 3D; ~2x lateral tolerance vs axial,
  indicative, to confirm in 3D); radial collector ring: signal ×1.2–1.7, movement term not resolved; 2 mm stand-off:
  +17 % axial / +46 % radial signal, needs liner + recess ≤ 1 mm (register liner 1.5 mm) — input for the carrier thread.
- Stopping here for the night; next steps need Stian: a consistent 3D radial case with a localised defect.
— Flux

## 2026-10-30 morning — committed (report completeness) — ready for Kai's check
- Commit: 545565c on u08-sws-3d (private github-max; subtree 1d97e6d). QC (qc-falsifier) no blocking findings (2nd pass).
  build.py --check ok; pytest 6 passed. Not pushed to fjordbit/SWS. Identifier entries 0/1: zero hits (page, new files); no prices.
- Unredacted export max/sws/"Safe Wire Sensor – HW Design Input Specification.docx" is NOT staged: excluded in the
  repo-local .git/info/exclude (Stian's file, open in Word; untouched). Never stage it with -f.

Completeness list (rendered / missing):
- Specification: rev127 export (2026-10-30, 13 prices → [COST]) RENDERED as Part 11: 14 sections, 23/23 tables (158/158 rows),
  7/7 own images; the live doc's main tab has exactly 7 visuals (5 interactive-chart embeds + 2 media) — all 7 are in the export
  (static images). Plus 10 regenerated script figures placed after the paragraph citing their script. Other tabs of the live doc
  (Data register, Code appendix): register rendered from sws/data/sws_data_sources.md; Code appendix NOT rendered (code listing).
- *_findings.md (10/10 RENDERED): sun exposure, axi, spacing, wire, guard, rope size, standoff, sync, consolidated 10-23, review 10-23.
- Also RENDERED: data register (33 refs anchored + linked, 137 citations), sync register rows, 3 briefs, VERIFICATION_PLAN,
  sws_scripts_README, references/README, DELTA_2026-10-23b, Stage 1 full tables (448/448, 460/460 rows), reconciliation (34 rows).
- Plot scripts (16/16 REPRODUCED, data/figures/MANIFEST.md): axi_plots, core_plot, fig_abstraction, guard_plots, head_sizes_plot,
  range_check, rope_size_plots, shoe_sweep, spacing_plots, wire_plots, loose_wire, pitch_check, sampling_chart, standoff_signal,
  rope_compare, sun_plot. Four sweep outputs re-run to make that possible (axi_sweep, layer_check 0.3/0.6, spacing_min,
  defect_response) — added to data/, noted in SWS_FILE_MAP.
- MISSING / not rendered on purpose: spec/Code_appendix_2026-10-14.md (code listing); the older rev123 md/pdf and rev124 docx
  (superseded by rev127, kept as files); READMEs/manifests of folders (navigation only).
- Open for Stian (from the reconciliation): the two stand-off stacks contradict each other (movement stacked onto s vs s at contact).
— Flux

## 2026-10-30 — committed (links, spec label, pdf) — ready for Kai's check
- Commit: 6ec64cd on u08-sws-3d (private github-max, subtree 0ba251e). QC no blocking findings; 59/59 GitHub link paths exist
  in the published snapshot; 0 fjordbit links; 0 dangling anchors. The published page still has the old links until you re-export.
- Links: base configurable (SWS_LINK_BASE / SWS_LINK_REF; default MAx-Flow/SWS-Documentation, main); tasks/ paths → #u07/#u08.
- Spec part relabelled rev127; rev123 pdf removed; spec/README.md updated. (The exclude line for the rev123 pdf in
  .git/info/exclude is not mine — harmless now the file is gone.)
- External links, 36 tested from this machine: 22 OK (200/202); 8 refuse scripts (403/429: doi→MDPI ×2, MDPI, doi→Wiley,
  Red Hat docs, mans.io, precision-elec ABB PDF, Bodycote) — likely fine in a browser; 4 BROKEN, all in data/sws_data_sources.md
  (spec owner's master, not edited):
    404 goudsmitmagnetics.com/uploads/pdf/neodymium_grades_available_at_goudsmit_20230310_1547.pdf
    404 www.mennens.nl/…/magnetic-rope-testing/en12927
    DNS iteh.es/catalog/standards/sist/…/sist-en-12927-2019
    DNS www.technickenormy.cz/en/astm-e1571-25-…
— Flux

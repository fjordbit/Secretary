# Sextant — read-only audit: where the SWS 3D work (U08/U16/U17/U19/U25) and the surviving 2D code depart from the decided design (spec rev127 + register)

2026-11-07, session Sextant. Nothing edited, created or committed in any Prosjekter worktree. Sources read in full:
spec rev127 (`Prosjekter-u25/max/sws/spec/rendered/SWS_HW_Design_Input_Specification_rev127.md`; the u08 copy is byte-equal
apart from trailing whitespace; the u05 "main" worktree has only rev123/124 and no 3d/ work), `data/sws_data_sources.md`,
`fem-2d/sws_consolidated_findings_2026-10-23.md`, `fem-2d/sws_head.py`, `3d/README.md`, `THEORY.md`, `verification.md`,
`reconciliation.md`, `design_inputs.md`, `rope_range.md`, `geometry_study.md` (part), `model3d.py` (options), `rope3d.py`
(head), `rope_construction.yaml`, `params.yaml`, `3d/p52/design.md`, `p52/head.py`, `p52/run_p52.py` and `p52/grades.py`
(grep), the run_*.py defaults (grep), `tasks/reports/U08.md`, `U16.md`, `U19.md`, `U25.md`, `Prosjekter-u17/.../U17.md`,
`VERIFICATION_PLAN.md` (part), `fem-2d/MANIFEST.md`, `due-diligence/sws_scripts_README.md`, `sws_sun_exposure_findings.md` (grep).

Caveat: the u25 worktree was being rewritten by U25b while I read (reconciliation.md row 13, README l.78, p52/head.py and
a new p52/grades.py changed between my first and second read). P52 numbers below are the pre-rewrite snapshot;
segmentation itself is ignored as instructed. Line numbers: spec = rev127 render; others as in the u25 worktree at ~05:00
(U16/U17/U19/U25 report lines as in their files).

## A. Departures and contradictory leftovers

| # | Item | Spec / register says | 3D work / code says | Where | Severity |
|---|---|---|---|---|---|
| 1 | Reference defect used for the "headline" | Acceptance defect: **two inner wires of an outer strand** (a wire below the outer layer), at EN 12927 spacing, **< 0.5 % LMA**, SNR ≥ 2 (spec l.52, l.68, l.114, l.429) | Headline fault = the two **outer-layer** flank wires (±120°) of one strand, **co-located**, **0.62 % LMA**; "hidden" redefined as "no part on the outer envelope". The spec's location (king wire) is the single-wire row: margin 9.6 / 5.7 (3 / 5 mm), i.e. two single breaks if the EN spacing exceeds the signature length. The margin forwarded to the head designer (20 / 12) is for the other defect | verification.md l.887–915; U16.md l.14–21, l.53–66, l.146–148; P52 design.md l.175–178; README l.84 | **blocks a number** (the margin quoted) / misleads |
| 2 | Axial (LMA) sensor radius | Each spoke carries one radial and one axial TMR **at the inner edge**, at the stand-off (5 mm design, 3 mm floor) (spec l.272); no larger radius decided anywhere | R = 36.5 mm (10.5 mm stand-off on 52 mm) from the head designer's P40 note, status A/[UNVERIFIED], carried into `run_3dd.py` (R_BZ_DESIGNER l.63), the U16/U19/U25 result tables and the **P52 dimension table** ("Axial sensor radius 36.5, A"). Stian allowed "B_z may sit at a larger radius" (U16 l.181–184) but no radius was decided | run_3dd.py l.20, l.63; U16.md l.65, l.151; design.md l.129, l.141; U17.md l.23 (notes the conflict with spec l.272) | misleads a future agent |
| 3 | Yoke geometry: outer notch 10 × 2 mm at mid-length | Plain yoke tube, flux rule, 12 mm wall (spec l.207, l.241, l.247 (2)); a yoke cut-out at the sensor plane was tested and **not adopted** (l.247 (5)) | P52 yoke carries the P40 drawing's outer notch "as drawn", status A, "purpose and real depth open"; costs 0.19 mT, raises the yoke to 1.5–1.7 T at the notch section. P40's 1 mm steel shoulder kept as a `shoulder=1.0` variant (dropped in the design, correctly) | design.md l.20, l.50, l.117, l.180, l.209; head.py l.46–48; run_p52.py l.55; params.yaml l.65 | misleads (an undecided feature is now in the prototype table and STEP) |
| 4 | Magnet grade basis in 3D | Grade open: **N48SH preferred**, N48H acceptable ≤ 60 °C, N52 excluded (l.247 (3), l.372, l.484). The result-10 table itself is sized on N40SH (Br 1.25 T min [R4]) | **Every 3D unit and the P52 design are sized on N40SH, Br25 = 1.25 T (grade minimum), αBr −0.12 %/K, Hcj 1.59 MA/m, knee 0.8 Hcj** (params.yaml l.109–117; THEORY A4 l.77; design.md l.5, l.71, l.88, l.123). No unit sized on N48SH, N48H or N52 (U25b's grades.py is now adding N52/N48SH). P40 (drawing N42) modelled with N40SH min Br (U16 l.154, rope3d.py l.488) or N42 Br 1.28 T [UNVERIFIED] (U17 l.21). **Agrees with the spec's baseline.** Two consequences: (a) P52's 20.5 mm is an N40SH thickness; on N48SH the same floor is ~1.7 mm thinner (2D: 19.1 → 17.4, findings l.73) — design.md l.71–73 says not to take the credit before the data sheet; (b) the 3D demagnetisation check (installed / empty head, handling note) was run **only on N40SH, the grade with the most knee margin** (0.48 vs 0.41 N48SH, 0.31 N48H, findings l.71–74); verification.md l.778 states the limit, but the handling note's "no measurable effect" is grade-specific | params.yaml l.108–117; verification.md l.692–780 | no departure on sizing; **misleads** on the demag note |
| 5 | Drawn Ø40 prototype (P40) vs the decided design | One-piece SH magnets, 1.5–2 mm non-magnetic guard, 40 mm magnets at 100 mm, flux-rule yoke, both TMRs at the inner spoke edge | P40 as drawn: **no guard or liner**, **1 mm steel shoulder** in the yoke bore between the poles, **N42** (not SH), 20 mm magnets at **65 mm** pole spacing, S235JR yoke with the outer notch, Ø12 radial holes, axial sensor at R 36.5. P52 "follows the P40 concept" (seats, notch, holes) and inherits items 2 and 3 above | U17.md l.16–23; U16.md l.153–159; rope3d.p40_case; head.py l.9–12 | misleads (the physical prototype is not the spec's head; nothing says so in one place) |
| 6 | Magnet thickness, P52 | H52 = 19.1 × 40 mm at the 1.92 T floor (l.241) | P52 20.5 × 40 mm: a **reasoned, documented** change (stranded rope at an unbounded domain gives 1.915 T at 19.1; margin stack §2); awaits Stian (U25 decision 1). Not an assumption. `sws_head.py DECIDED` still = 17.8 mm (stale; flagged in README l.22, MANIFEST l.22, params l.67) | design.md l.23–76; sws_head.py l.85, l.144 | cosmetic (decision pending) |
| 7 | Split-plane treatment | Yoke halves close steel-to-steel; split parallel to flux; 5–10 % derating budget until 3D (l.203, l.474) | 3D-B: tied magnet + yoke gap sweep first (contradicts the steel-to-steel rule; stated), magnet-only gap run once; P52 adds a **0.5 mm magnet set-back per half** (status A, U25's own value) and finds ~1 %/mm, far below 5–10 % | verification.md l.340–378, l.557–562; design.md l.80, l.122; reconciliation row 13 | cosmetic (labelled A; the set-back value needs a decision) |
| 8 | End caps | Yoke length = spacing + 2 × magnet length, flush; no end caps decided (l.207); `sws_head.py yoke_offset` offers *steel* end caps (l.96) | 3D: flush, no end caps (THEORY S6 l.92; params l.23); P52: 5 mm **non-magnetic** end cover, placeholder P, not in the FE (design.md l.134) | as listed | no departure; open item, consistent |
| 9 | Sensor background figure | Register l.209: "~40 mT axial background" (status C, from sws_spacing_min.py, steel-shoe geometry); spec l.312, l.314 (400:1 / 800:1) rest on it | 3D / 2D decided-config: 45–90 mT (H52/40 hard −40 °C 69 mT; U9 design point ~75 mT, design_inputs l.151); register row **not marked superseded** | design_inputs.md §3; rope_range.md l.45–52; reconciliation rows 1, 2, 11 | misleads (register row unmarked) |
| 10 | Rope-centring side force | Result 6: 0.4–0.8 kN/mm (owner run on sws_axi_head.py, 100 mm head **with the 8 mm steel shoe**; register l.149 status A) | 3D on H40/40: 0.12 kN/mm, decentring (negative stiffness); spec sentence unchanged | verification.md l.379–389; reconciliation row 12 | misleads (spec sentence) |
| 11 | Bore convention | Ø60 free bore for 40 + 52, Ø65 wide option, Ø70 withdrawn (l.247 (4), l.481) | 3D agrees (free bore = guard inner face). Leftover: design_inputs.md l.179 "D_f 48 / 60 / **70**; 65 for W65" (W70 withdrawn); spec l.171 "60–65 mm bore", l.232 "65 mm bore … Decision for revision 1", l.234 "bore moves from 65 to 70", l.243 row "clearance bore 70" | as listed | cosmetic |
| 12 | Magnet service temperature | ≤ 60 °C service precondition (l.36); sizing −40 / +80 | verification.md quotes an owner statement "does not exceed about 50 °C" (not in spec or register) | verification.md l.694–699; U08.md l.123 | cosmetic (see D) |
| 13 | Rope strands | Spec l.76 and l.110: Powerplast "has 18 strands: the outer strands and the strands of the inner rope"; l.496: "18 outer strands" | rope_construction.yaml takes **18 outer strands** + 7 wires (126/18), marked [UNVERIFIED]; the spec contradicts itself | rope_construction.yaml l.15–16; U16.md l.137 | misleads (spec-internal) |
| 14 | 1.9 T "requirement" | Window 1.9–2.3 T is status **U** (register l.191, not checked against EN text); 1.92 T floor is A | U19 and P52 call 1.9 T "the requirement" that "holds" at 1.915 T | U19.md l.9–10, l.283; design.md l.26 | cosmetic (U row treated as settled) |
| 15 | sws_fig_abstraction.py concept figure | Decided head: no steel shoe, 100 mm, 19.1 × 40 | Figure draws the **withdrawn 200 mm head with an 8 mm steel shoe and a 30 × 40 mm magnet** (GEO l.26); it is in the Code appendix and on the published site (`docs/sws/index.html`) | fem-2d/sws_fig_abstraction.py l.26; docs/sws/index.html | misleads (external) |

Checked, **no departure** (one line each):
- Magnet construction: 3D-A/B/C/D, THEORY S1, README l.8 all one-piece half-rings (P52 segmentation excluded per brief).
- Guard: 2.0 mm, μr = 1, non-magnetic, params.yaml l.18–19, THEORY A3, P52 table; agrees with spec l.203/l.382.
- Bore: free bore Ø48 / Ø60 / Ø65 as spec result 10 (after the 2026-10-29 correction); agrees.
- Pole spacing 100 mm / z_in 50 and magnet axial 40 mm: params.yaml l.20–21, P52 table; agrees (P40 is 65 mm — item 5).
- Magnet dimensions H40 17.2 / H52 19.1 / W65 20.1 × 40: params.yaml heads = spec l.240–242; agrees (P52 20.5 — item 6).
- Yoke rule and wall: flux rule of result 7, 8.511 / 11.959 / 13.4 mm, P52 12.0 mm; agrees (notch — item 3).
- Sensor count and pitch: 16 at 22.5°, 8 per half; first spoke 11.25° from the split (offset not in spec, stated as such).
- Stand-off: 3 and 5 mm from the nominal rope surface in every run (params l.122–123); design 5, floor 3; agrees (R 36.5 — item 2).
- Wire B–H corners: hard (1.95 T, 2.5 kA/m), easy (2.01 T, 1.5 kA/m) = register box l.119 (params l.77–78); nominal (2.05/3.0) regression only; agrees. U17/geometry_2d use a "box-centre" curve 1.98 T / 2.0 kA/m at 25 °C, labelled.
- 1.92 T floor and 2.30 T ceiling: applied as spec l.236 in rope_range, lm_plateau, U19, P52; agrees.
- B_rope definition: flux / C·d², stated open (U) in every 3D document; P52 gives the steel-mean too; agrees with l.482.
- Rope construction values: C 0.571, fill 0.727 (params l.71–72); wire 2.5 mm (A), gap 2 mm (A), jacket 1.0 mm (low end of the 1–2 mm estimate), inner rope homogenised — all marked A/[UNVERIFIED]; agrees with register status (strands — item 13).
- Tolerance basis: ±1e-3 T / ±0.2 mT carried as "proposal, status A until Stian accepts" (verification.md l.7, design.md l.208); agrees with l.483.
- Materials status: wire, steel (1010-like), magnet Hcj/knee all A in params.yaml and THEORY A1; agrees. P40's S235JR modelled as 1010-like, [UNVERIFIED].
- Rope centring ≤ 0.5 mm: THEORY A5; ecc runs 0–3 mm; agrees with l.33.
- Head masses: P52 yoke 6.149 kg vs spec 6.1; magnet 2.99 kg at 19.1 reproduced (head.py l.31–32); agrees.
- 3D code is clean of the legacy 2D modules: no 3d/*.py imports sws_axi_head*, sws_fig_abstraction or sws_femm_axi; check4/geometry_2d/lm_plateau use `sws_head.HeadConfig` (decided config).

## B. Leftover sentences that invite a wrong assumption (file, line)

Spec rev127 (Stian fixes; not edited):
- l.474 "Two-halves 3D head model (split line, **segmented magnet blocks**)" — the sentence U25 followed. Also l.201 "possibly segmented blocks … segment manufacturability".
- l.475 "Yoke tube 10–14 mm and **shoe 2–4 mm** to be confirmed in the 3D model" — invites a steel shoe.
- l.159 column "12 mm yoke tube and 4 mm shoes"; l.201 "4 mm pole shoes … 2–4 mm shoes in N45SH–N48SH"; l.203 "flux runs rope → shoe → magnet → yoke"; l.207 "shoes 4 mm"; l.212 "Pole shoes … 0.5 kg"; l.218 "the shoe sweep shows"; l.376 "magnetic parts of the head are about 8 kg" — all steel-shoe era, read as current.
- l.169 "**17.8 × 40 mm / 2.7 kg** … every magnet mass quoted for the decided head from here on is the guard value" vs l.241 "19.1 × 40 mm / 2.99 kg" — two "decided" magnet sizes in one section (and `sws_head.py DECIDED` = 17.8).
- l.175–185 and l.191 "One head still covers the whole range … 200 mm spacing, 30 × 40 mm N40SH rings in a 65 mm bore … The magnet is a one-off decision" — the withdrawn 200 mm head, steel shoe, presented as a current answer.
- l.232 "**Decision for revision 1: one magnet head (65 mm bore, 12.9 × 40 mm N40SH-class or better** at 100 mm spacing)" — steel-shoe map; contradicts result 10 (shared Ø60, 19.1 × 40) and the 2026-10-29 answers (wide head an option, not rev 1).
- l.205 "0.4–0.8 kN of side force per millimetre" and "7 500 mm² of pole face" — steel-shoe head; 3D gives 0.12 kN/mm.
- l.312 "~40 mT axial background … 400:1"; l.314 "800:1"; l.479 "axial ~40 mT" — superseded by 45–90 mT.
- l.372 "NdFeB SH grade or higher (N40SH–N50SH)" vs l.247/484 "N48H acceptable under ≤ 60 °C" — the §9 table excludes the H grade the §5/§12 text allows.
- l.110 "18 strands: the outer strands and the strands of the inner rope" vs l.496 "with 18 outer strands".
- l.173 "At every spacing the magnet inner corners run at 0.1 T hot" — steel-shoe corner reversal; the guard head sits at +0.24 T or more (l.234).
- l.36 "≤ 60 °C in service; sizing … −40 / +80 °C as margin" and l.363 "sizing them at +80 °C therefore costs only 0.01 T" — read as "the +80 corner is free"; the P52 floor decision was taken at +80 °C (see D).

Register (`data/sws_data_sources.md`):
- l.209 "~40 mT at the sensor radius … at every spacing" — status C, not marked superseded (3D: 45–90 mT).
- l.149 "0.4–0.8 kN per mm eccentricity … needs 3D" — 3D done (0.12 kN/mm), row unchanged.
- l.147 "Yoke tube / shoe 12 mm / 4 mm" — shoe row without a superseded tag.
- l.221 "Noise budget < 0.2 mT p-p" — untagged; replacement at l.292 (reconciliation row 31).
- l.151 "Temperature range for sizing −40 to +80 °C magnet … service ≤ 60 °C" — the only register row on temperature; the sun study's head peak is not a row.

3D docs and code:
- 3d/README.md l.8 "the end caps behind the one-piece half-ring magnets" — implies end caps are a decided feature (none decided; THEORY S6 flush).
- 3d/README.md l.13 "spec rev124 result 10"; params.yaml l.13 "spec rev123 … (carries rev124 content)"; run_ecc.py l.13, run_3dc.py l.103 "spec rev123" — all cite superseded revisions (content unchanged, but a future agent may open the wrong file).
- 3d/design_inputs.md l.179 "(D_f 48 / 60 / 70; 65 for W65)" — W70 withdrawn.
- 3d/p52/design.md l.117 "Outer notch … as drawn on P40 … purpose and real depth open" and head.py l.9–12 "follows the Ø40 prototype (P40) concept as the head designer drew it" — invites copying P40 features (shoulder, notch, holes, R 36.5) into every later head.
- 3d/p52/design.md l.26 and U19.md l.10 "the 1.9 T requirement holds" — window is status U.
- 3d/run_3dd.py l.63 `R_BZ_DESIGNER = 36.5  # head designer via Kai [UNVERIFIED]` — a constant with no spec row, used in every fault table.
- tasks/reports/U08.md l.93 "3D-B, the rest: hinge and latch, **magnet segmentation**, end caps"; run_3db.py l.10 "magnet segmentation into blocks"; deltas/DELTA_2026-10-29_U08_check3_3db.md l.26, l.48, l.60, l.64 "segmentation" — the same leftover as spec l.474, repeated four times in the repo.
- fem-2d/sws_head.py l.96 `yoke_offset … (steel end caps behind the magnets)` and l.144 `DECIDED = HeadConfig()  # … 17.8 × 40 mm` with docstring "`DECIDED` below is that configuration" — a stale "decided" head in the one file called the consolidated model.
- due-diligence/briefs/sws_carrier_brief.md l.79 "t_shoe = 2, shoe_magnetic = False" — correct flag, shoe vocabulary.
- verification.md l.694–699 owner operating statement (bolted closed once, 90°, ≤ 50 °C) — not in spec or register; a future agent will size on 50 °C.

## C. The six 2D legacy modules still defaulting to t_shoe = 8.0, and what rests on them

Modules: `fem-2d/sws_axi_head.py` (Head l.63; `lumped_head()` l.92), `sws_axi_head_lite.py` l.50, `sws_axi_head_wire.py` l.47,
`sws_axi_head_guard.py` l.57 (shoe_magnetic default), `sws_fig_abstraction.py` GEO l.26 (also lm 30, z_in 100 = the withdrawn
200 mm head), `sws_femm_axi.py` (per MANIFEST l.21). Callers in fem-2d: sws_axi_check/plots/sweep (lumped_head), sws_spacing_min,
sws_shoe_sweep, sws_temp60, sws_wire_sweep, sws_rope_size_map/_demag/_plots, sws_defect_response, sws_layer_check,
sws_short_head_check, sws_guard_sweep/final_config/guard_config_table (these three set the guard non-magnetic).

Numbers and figures that still rest on them:
- Spec result 1 table l.159–165 and l.167 (sws_spacing_min; 8 mm shoe, declared at l.169) — record of trends, marked.
- Spec l.175–185 one-head table and l.191 (sws_axi_sweep / lumped_head, 200 mm, 30 × 40) — withdrawn head, **not marked** in place.
- Spec image4 l.195 "magnet band: axisymmetric FE (sws_axi_head.py)" — steel-shoe band in a figure still in the document.
- Spec result 6 l.205 (gap field 0.7 T, 200 kPa, 7 500 mm², 0.4–0.8 kN/mm, stray 0.5 mT @ 300 mm, 10 mT @ 200 mm) ← register l.148–150 "owner run on sws_axi_head.py". Stray field never redone in the decided configuration or 3D.
- Spec result 7 l.207–216 (4 mm shoes, 8 kg) and l.376 — register l.155 marks it superseded; spec text does not.
- Spec result 9 table l.224–228, image5 l.230, "Decision for revision 1" l.232 (sws_rope_size_map/_demag/_plots on sws_axi_head_wire) — register marks the rows superseded; the decision sentence stands.
- Spec l.173 pole-spacing floor 60–80 mm and "broken-wire response at 80 mm within 5 % of 200 mm" ← sws_spacing_min, sws_defect_response, sws_layer_check (register l.139) — trend-level; register l.297 says trends unaffected.
- Register l.138 leakage 2.5 (steel-shoe FE) → the yoke flux rule σ = 2.5 in sws_head.py l.140 and params t_yoke; **re-validated** by the explicit-wall sweep in the decided config (register l.309), so the 12 mm stands on its own.
- Register l.209 ~40 mT background (sws_spacing_min) → spec l.312, l.314, l.479 — superseded by 45–90 mT (item 9).
- Code appendix and published site: the sws_fig_abstraction concept figure (steel shoe, 200 mm head) — item 15.
- 3D docs: README l.32 (force, flagged), reconciliation rows 1, 2, 10–12, 22, 26 (all flagged there). No 3D result rests on a legacy module.

## D. Addendum (a): temperature basis of each 3D unit, and whether the sun study's peak is quoted

Spec as written: service ≤ 60 °C precondition, sizing and qualification at −40 / +80 °C (l.36, l.151 register); §9 l.363 "magnets sit at head body temperature: 45 °C shaded, about 60 °C light grey in full sun"; sun findings (`due-diligence/sws_sun_exposure_findings.md` l.38–40, Houston run): magnet head peak **43 °C shielded, 46 °C semi-shielded**, 55 °C unshielded light grey; the spec's Dubai table l.356–361 gives 49–61 °C for the head.

| Unit | Design corner used | Other temperatures run | Service value / sun peak quoted? |
|---|---|---|---|
| U08 3D-A/3D-B (verification.md check 1, 3D-B) | hard wire **+80 °C** (sizing corner of result 10) | easy −40 (reviewer case), hard +25 (video), hard −40 (background worst case); demag +80 / +85 | only the owner's "about 50 °C" aside (verification.md l.694–699, U08.md l.123); sun study never cited |
| U08 2D side studies (rope_range, lm_plateau, bondline, domain) | hard **+80** / easy −40 | hard −40 for backgrounds | no |
| U16 3D-C/3D-D | hard **+80 °C** only (U16.md l.14, l.55, l.150) | none | no |
| U17 (Henrik's questions) | **25 °C**, box-centre wire (U17.md l.7, l.100) | +80 / −40 for the P40 window check (l.59, l.86) | no |
| U19 3D-C2/D2 | hard **+80 °C** (floor) (U19.md l.9–10, l.243) | easy −40 (stage 4) | no |
| U25 P52 | hard **+80 °C** is the floor decision's corner (design.md l.25, l.33, l.169; U25.md l.10) | easy −40 (top corner); hard −40 **not run** | no; `params.yaml` scenarios l.135 list +60 but no 3D unit ran it |
| U25b (in progress) | p52/grades.py l.2–4: N52 and N48SH at **−40 / +45 °C**, +80 kept as a "spec qualification margin" row | | first file to cite the sun findings (45 °C) |

So: every 3D unit and the P52 floor decision used +80 °C as *the* design corner; +60 °C (the spec's own service precondition) was never run in 3D, and the sun study's 43–46 °C peak is not quoted in any 3D document or report before U25b. The 20.5 mm decision's margin stack (design.md §2) is therefore a +80 °C number; at 45 °C Br is 4.2 % higher (−0.12 %/K × 35 K), worth about 10 mT of B_rope by design.md's 2.3 mT per % — more than the 6.9 mT margin the thicker magnet was bought for.

## E. Addendum (b): where "N52 excluded" and "sized on N40SH minimum" live

"N52 excluded" (all rest on the register's assumed Hcj 0.88 MA/m for N52 and the 0.8·Hcj knee, both status A):
- spec l.11 (abstract: "N52 excluded by demagnetisation"), l.173 ("plain N52 is excluded (reversed field at the inner corners hot), so the grade stays SH or higher" — steel-shoe era reasoning), l.247 (3) ("N52 is excluded (64–83 % of the magnet beyond the knee)"), l.372 (§9 table "plain N52 excluded … at +80 °C"), l.484 (§12 open item), l.515 and l.526 (revision log).
- register l.181 (Hcj by grade letter, A — the N52 value is not even in the row; it comes from sws_head.py), l.310 ("N52 64 % (60 °C) / 83 % (80 °C) excluded").
- fem-2d/sws_consolidated_findings_2026-10-23.md l.75; fem-2d/sws_head.py l.47 (`"N52": dict(br25=1.42, hcj20=0.88e6)` — the A number that does the excluding); fem-2d/sws_grade_check.py l.1, l.14.
- 3D: no 3D document says "N52 excluded"; p52/head.py l.36–41 (U25b) copies the same 0.88 MA/m for N52.

"Sized on N40SH minimum Br 1.25 T":
- spec result 10 table l.238–243 (baseline grade N40SH; N48SH row only in the text l.247 (3)); register l.303 ("DECIDED … N40SH"), l.305–307, l.127 (N40SH Br min).
- fem-2d/sws_head.py l.43 (GRADES N40SH), l.89 (`grade: str = "N40SH"` default), l.144 (DECIDED); head_optimise.json (the result-10 numbers).
- sws/params.yaml l.109–110 (`grade: N40SH`, `br25 1.25 "S [R4] N40SH Br (min)"`) — the one input every 3D unit reads through `stage1/common.make_case` (l.76).
- 3d/README.md l.14 ("Grade open, N48SH preferred"); THEORY.md l.77 (A4); design_inputs.md l.105–106 ("the model already uses the supplier's minimum Br for N40SH"); verification.md l.779 (demag limits); due-diligence/stage1/comparison.md l.85.
- 3d/p52/design.md l.4–5, l.71–73, l.88, l.123, l.204; p52/head.py l.150, l.175–181 (default grade N40SH); p52/run_p52.py l.198 (`--grade` default N40SH); rope3d.py l.488–489 (P40 modelled with N40SH min Br instead of the drawing's N42).
- tasks/reports/U16.md l.154; U17.md l.21, l.30 (N42 Br 1.28 T [UNVERIFIED] for P40; H52 "19.1 × 40 mm N40SH"); U25.md l.83.

— Sextant

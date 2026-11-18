# Crane rope standard — extract for the rope tester (MFL / MRT)

Source: `InternationalStandards-Cranes-Ropes/dsc.pdf`. Internal note. Do not put it in a repository.
Read by Bosun for Kai, 2026-11-18.

## The short version

- The PDF is **one document**: ISO 4309:2017, *Cranes — Wire ropes — Care and maintenance, inspection and discard*, 5th edition, 2017-11. It is not a collection.
- **66 PDF pages**: cover and front matter on pages 1–6, standard pages 1–59 on PDF pages 7–65, back cover on page 66.
- **Page rule:** standard page n is PDF page n + 6.
- **No text layer.** It was printed with "Microsoft Print to PDF" and the text was turned into vector outlines, so text extraction returns nothing.
- It is not a scan, so the pages render sharply. I rendered them to temporary images and read them. Every number below was read off a page image.
- The standard treats magnetic rope testing (MRT, its term for MFL) as an **aid** to visual inspection. It defines LF (local fault) and LMA (loss of metallic area) and gives discard limits for both.
- It says **nothing** about instrument performance (sensitivity, resolution, speed, saturation, sensor type, signal-to-noise) or about permanent monitoring. For instruments it points to EN 12927, ASTM E1571 and IMCA SEL 023, which are not in this PDF.

## A. Contents of the PDF

| PDF pages | Std pages | Part |
|---|---|---|
| 1 | — | Cover: ISO 4309, 5th ed., 2017-11 |
| 2 | ii | Copyright page (not read) |
| 3–4 | iii–iv | Contents |
| 5 | v | Foreword (not read) |
| 6 | vi | Introduction |
| 7 | 1 | 1 Scope |
| 8–10 | 2–4 | 2 Normative references; 3 Terms and definitions (3.1–3.15) |
| 10–17 | 4–11 | 4 Care and maintenance (4.1–4.8) |
| 18–21 | 12–15 | 5 Inspection (5.1–5.6; 5.6 is MRT) |
| 21–30 | 15–24 | 6 Discard criteria (6.1–6.7; 6.3 is MRT) |
| 31–32 | 25–26 | Annex A (normative): key areas for close inspection |
| 33–42 | 27–36 | Annex B (informative): typical modes of deterioration (photos) |
| 43–44 | 37–38 | Annex C (informative): discard criteria for MRT |
| 45–47 | 39–41 | Annex D (informative): internal examination with clamps |
| 48–50 | 42–44 | Annex E (informative): inspection records, including an MRT report form |
| 51–53 | 45–47 | Annex F (informative): background on deterioration and discard |
| 54–56 | 48–50 | Annex G (informative): combined-effect severity rating |
| 57–62 | 51–56 | Annex H (informative): rope cross-sections and rope category number (RCN) |
| 63–64 | 57–58 | Annex I (informative): external corrosion photos |
| 65 | 59 | Bibliography |
| 66 | — | Back cover |

## B. Relevant clauses, paraphrased

Page references are PDF pages.

### Scope and definitions

- **1 Scope (p7).** Covers steel wire ropes on cranes and hoists. The crane list includes floating cranes and offshore cranes (fixed or floating). It also covers winches and hoists. Shiplifts are not named. Synthetic or synthetic-lined sheaves with single-layer drums are excluded: no discard criteria are given for that combination, because many internal breaks occur before anything is visible.
- **3.2 Measured diameter d_m (p8).** The mean of two diameter readings taken at right angles.
- **3.3 Reference diameter d_ref (p8).** The measured diameter of an unbent section, taken just after the new rope has been run in. It is the baseline for diameter change.
- **3.7 Periodic inspection (p9).** A detailed visual check plus measurement, and an internal assessment where practicable. It may include MRT by a person competent in the equipment and in reading traces.
- **3.8 Competent person (p9).** If MRT is required, it must be done by someone competent in that discipline.
- **3.9 Valley wire break (p9).** A break at the contact point between two outer strands.
- **3.10 Severity rating (p9).** Deterioration as a percentage of the way to discard. It can cover one mode (for example LMA from MRT) or several modes combined.
- **3.11 MRT (p9).** NDT that measures magnetic flux leakage of a magnetised rope.
- **3.12 Test head (p9).** The part around the rope that creates the magnetising field and holds the sensors.
- **3.13 Base trace (p10).** The MRT record from the first test of the rope. It is the datum for all later comparisons. It reflects the rope construction and magnetic variation along the length, for example permeability differences.
- **3.14 LF (p10).** A short discontinuity, such as a wire break, a welded wire, a corrosion pit or inter-strand nicking.
- **3.15 LMA (p10).** Change in metallic cross-section, as a % of the **nominal metallic area of the new rope**. It is usually caused by corrosion, wear, abrasion or wire breaks.

### Care and maintenance (clause 4)

- **4.2 (p10–11).** Install only the rope specified by the crane maker: length, diameter, construction, lay and minimum breaking force. Record each rope change. A base trace for MRT is called beneficial, taken either before installation or as soon as practical after it.
- **4.3 (p12).** Store ropes cool, dry and off the floor. Re-dress ropes in storage if a competent person thinks it necessary. In warm places, turn the reel half a turn now and then.
- **4.4 (p12).** On receipt, check the rope and its certificate. Measure the new rope diameter (d_m) on a straight, untensioned section and record it. If the rope was stored where it could corrode, a visual check plus MRT may help. Check the sheave and drum grooves. The sheave groove should be **5–10 % larger than nominal rope diameter**, and **at least 1 % larger than the actual new-rope diameter**.
- **4.5 (p13, p16).** Install without adding or removing turn. On multi-layer drums, apply back-tension of about **2.5–5 % of minimum breaking force**.
- **4.6 (p16).** Run in a new rope at reduced speed and load, down to about **10 % of WLL**, for a number of cycles.
- **4.7 (p17).** Dress (lubricate) the rope before it gets dry or corroded, especially where it runs over sheaves. The dressing must suit the maker's lubricant and must penetrate. If no dressing can be applied, or the environment is corrosive, inspect more often. A protruding broken wire may be snapped off, but it still counts as a break and its position should be recorded. A rope damaged only near its termination may be shortened and re-terminated.
- **4.8 (p17).** Check that drums and sheaves turn freely. Stiff sheaves cause severe abrasion.

### Inspection (clause 5)

- **5.2 (p18).** Daily visual check of the working section and the attachment points.
- **5.3.1 (p18).** A competent person does periodic inspection. Severity is stated as a % (20/40/60/80/100) or in words (slight to discard). Any damage present before the rope enters service must be assessed and recorded.
- **Table 1 (p19).** MRT is listed as an assessment method for LMA from broken wires, LMA from corrosion or wear, and corrosion. Broken wires are counted visually. Diameter is measured.
- **5.3.2 (p19).** The competent person sets the interval, considering law, environment, mechanism class, past results, time in service, use and the crane maker. Breaks usually develop faster late in the rope's life. **No fixed interval is given.**
- **5.3.3 (p19–20).** Inspect the full length. For long ropes, the working length plus at least 5 drum wraps may be enough. Critical zones include terminations, sections over sheaves, sections over compensating sheaves, sections in contact with a sheave while loaded during repeated work, crossover zones, abrasion points and hot areas. MRT is named as a help for internal condition.
- **5.3.4 (p20).** Inspect at and near terminations: wire breaks at the entry, ferrule cracks or slip, wedge socket assembly, and eye splices.
- **5.3.5 (p20).** Give a written record after each periodic inspection, with the maximum interval to the next one. A running record is preferred.
- **5.5 (p21).** If the crane has been idle more than **3 months**, do a periodic inspection before use.
- **5.6 MRT (p21).** This is the core clause for us.
  - MRT may be used as an aid to locate suspect sections.
  - If MRT is part of periodic inspection, take a base trace (the "rope signature") as early in the rope's life as possible.
  - Use MRT where defects may not be visible, and always together with a visual inspection.
  - No ISO standard exists for qualifying MRT devices. For instrumentation and instrument verification, take guidance from EN 12927 or ASTM E1571 (the clause misprints it as "E157-11").
  - Listed limits of MRT: ferromagnetic ropes only; break gaps smaller than the instrument's sensitivity are missed; restricted access, for example near terminations or equaliser pulleys.

### Discard criteria (clause 6)

- **6.1 (p21).** Manufacturer instructions come first; otherwise 6.2–6.7 apply. The competent person must assess the combined effect of several modes (Annex G). If the rate of deterioration changes noticeably, investigate. A short damaged length may be cut out.
- **6.2.1, Table 2 (p22).**
  - Random breaks: use Table 3 or Table 4.
  - Localized groups in one or two strands: may require discard below the table values.
  - Valley breaks: discard at **2 or more in one lay length (about 6d)**.
  - At a termination: discard at **2 or more breaks**.
- **6.2.2 (p22).** Limits depend on the **rope category number (RCN)**. The RCN comes from the construction (Annex H), or from n, the number of load-bearing outer-layer wires (filler wires excluded).
- **6.2.3 (p22).** Isolated breaks from manufacture, shipping or installation are not counted, but they should be recorded.
- **6.2.4, Table 3 (p23–24): single-layer and parallel-closed ropes.**
  - Limits are visible broken outer wires over 6d and 30d, by RCN 01–13 and n > 300. They are split into ordinary or Lang lay for sheaves and single-layer drums, and into multi-layer drum crossover zones.
  - Example values, ordinary lay, sheave sections, classes M1–M4: RCN 01 (n ≤ 50) is 2 in 6d and 4 in 30d. RCN 04 is 5 and 10. RCN 08 is 8 and 16. RCN 13 is 12 and 24.
  - For n > 300: 0.04n in 6d and 0.08n in 30d.
  - Lang lay is roughly half these values. Multi-layer crossover zones are double.
  - Mechanism classes M5–M8 may use twice the values.
  - Seale constructions with 19 or fewer wires per strand move up two rows.
- **6.2.5, Table 4 (p25): rotation-resistant ropes.**
  - RCN 21–31. Sheave sections run from 2 in 6d / 4 in 30d (RCN 21–23-1) up to 6 in 6d / 12 in 30d (RCN 30, 31 and n > 300).
  - The note on Seale constructions applies here too.
- **6.3 MRT (p25–26).**
  - For LF evaluation, the MRT person must know either all wire diameters and counts, or the maximum wire diameter and the metallic cross-section.
  - For LMA, the person must at least have the metallic cross-section. The rope maker or supplier should provide these data.
  - MRT discard criteria are in Annex C. If MRT breaks can be confirmed visually as outer breaks, Table 3 or 4 may be used instead of Table C.1.
- **6.4.1, Table 5 (p26): uniform diameter decrease, sheaves and single-layer drums only.**
  - Discard limits: fibre-core single-layer rope at **10 %** of nominal; steel-core single-layer or parallel-closed rope at **7.5 %**; rotation-resistant rope at **5 %**.
  - Bands of 20 % severity are given in between, for example steel core: 3.5 / 4.5 / 5.5 / 6.5 / 7.5 %.
  - These limits do not apply at multi-layer crossover zones.
- **6.4.2 (p27).**
  - Decrease (%) = (d_ref − d_m) / d × 100. The baseline is the reference diameter after running in, not the nominal diameter.
  - Worked example: a 40 mm rope with d_ref = 41.2 mm, i.e. the new rope is 3 % oversize. At 7.5 %, discard comes at a measured 38.2 mm.
- **6.4.3 (p27).** An obvious local decrease, such as core failure or a sunken strand, means discard.
- **6.5 (p27).** A complete strand fracture means immediate discard.
- **6.6, Table 6 (p27–28): corrosion.**
  - External corrosion: wipes off = 0 %; rough to touch = 60 %; heavily pitted with slack wires = discard.
  - Internal corrosion: visible debris coming out of the valleys = discard, unless an internal check per 6.3 (MRT) or Annex C is practicable.
  - Fretting corrosion: investigate; if in doubt, discard.
  - Clean the rope before judging, without solvents. The table notes that internal corrosion is subjective without MRT.
  - Internal or fretting corrosion can increase the diameter.
- **6.7 (p28–30): deformation and damage.**
  - Waviness: discard if the gap is ≥ 1/3·d on a straight part that never runs over a sheave, or ≥ 1/10·d on a part that runs over a sheave or onto the drum.
  - Immediate discard (or cut out the section): basket or birdcage, and core or strand protrusion.
  - Immediate discard: protruding wire loops.
  - Local diameter increase of **≥ 5 % (steel core)** or **≥ 10 % (fibre core)**: investigate and consider discard.
  - Flattening over sheaves: consider discard.
  - Immediate discard: kinks, severe bends, heat damage (heat colours or loss of grease), and arcing on 2 or more wires.

### Annexes

- **Annex A (p31–32, normative).** Diagrams of zones needing close inspection: drum entry at maximum fleet angle, block sheave entry, compensating sheave contact, and the multi-layer case. I read p31 only.
- **Annex C (p43–44): MRT discard limits.** These apply to all rope constructions.
  - **C.1 LF.** Convert wire breaks to lost area, using the actual broken-wire diameter or the largest non-filler wire diameter. **Table C.1:** discard at **6 % LMA over 6d** or **10 % over 30d**.
  - The maximum number of breaks = φ·A·4 / (π·δ_max²), where φ = 6 %, A = metallic area from the certificate and δ_max = largest wire diameter. Worked example: A = 240 mm² and δ_max = 1.45 mm give 9 breaks in 6d.
  - If A is not known, it can be calculated from ISO 2408 factors.
  - **C.2 LMA.** Uses the whole metallic cross-section, independent of construction. **Table C.2:** discard at **10 % LMA over 30d**.
- **Annex E (p48–50): records.**
  - E.1/E.2 are visual record forms. Fields include reference diameter, allowed breaks in 6d/30d and severity per mode.
  - **E.3 is an MRT report form** with these fields: instrument, data recorder, magnetic head, sensors, **speed**, length inspected, rope specification and construction, installation date, last test, original certificate, start and finish rope end, **LMA trace**, **LF trace**, and the competent person's name and signature.
- **Annex F (p51–53): background.**
  - Rotation-resistant ropes can have extensive internal breaks with no visible outer breaks, so MRT is recommended for them, especially ropes with 3 or more strand layers.
  - Bending fatigue: breaks start after some cycles and then accelerate. Track the rate to plan inspections.
  - Two valley breaks in one lay length suggest the core no longer supports the outer strands.
  - Diameter loss can come from internal wear, core failure or inner-strand breaks.
  - Corrosion is worst in marine air and speeds up fatigue. Internal corrosion is hard to see.
  - Several of these sections end by saying MRT gives extra useful information.
- **Annex G (p54–56): combined effect.**
  - Rate each mode as a % of its own limit and add the ratings that occur at the same location. Saying "slight … discard" in words is an alternative.
  - **If MRT finds more breaks than the visual check, use the MRT count.**
  - Example 6 is a 70 mm 35×7 WSC rope on an offshore knuckle-boom crane with a multi-layer drum. MRT LF of 5 % in 30d gives 50 %. LMA (corrosion) of 6 % against the 10 % limit gives 60 %. Together they make 110 %, so discard.
  - Table G.1 has columns for visual breaks, MRT LF, diameter, external corrosion and MRT LMA, with actions from "safe to continue" up to "prepare for replacement".
- **Annex H (p57–62).** Cross-section drawings with their RCN. Page 57 shows 6×7-FC = RCN 01, 6×19S-IWRC = 02, 6×19M-WSC = 04 and 6×25F-IWRC = 04. Pages 58–62 not read.
- **Annex I (p63–64).** External corrosion photos rated 0 %, 20 % and 60 % on p63. The I.4 photo on p64 was not read.
- **Bibliography (p65).** ISO 2408; ISO 4306-1; ISO 16625 (selection of ropes, drums and sheaves); EN 12927:2016 (cableway ropes); **IMCA SEL 023 (2009), guidance on NDE by magnetic rope testing**; **ASTM E1571-11(2016)e1, electromagnetic examination of steel wire rope**.

## C. What bears on our five open points

**1. LMA reference, baseline and calibration**
- A base trace should be taken as early as possible and serves as the datum for all later runs. It also captures permeability variation along the rope (3.13 p10; 5.6 p21).
- It is beneficial to take the base trace before installation or soon after it (4.2 p11).
- LMA is defined as a % of the **nominal metallic area of the new rope**, not of the base trace. The rope maker should supply the metallic area and wire diameters (3.15 p10; 6.3 p25).
- Diameter uses a separate baseline: d_ref, measured after running in (3.3 p8; 6.4.2 p27). So diameter is zeroed after run-in, while LMA is zeroed on the base trace.
- A new rope that already has faults: assess and record pre-service damage (5.3.1 p18). Isolated manufacturing or shipping breaks are recorded but not counted (6.2.3 p22). A rope stored where it may have corroded may get visual inspection plus MRT before installation (4.4 p12).
- Calibration, reference rods, drift and repeatability: **not covered.** The standard points to EN 12927 and ASTM E1571 for instrument verification (5.6 p21; bibliography p65).

**2. Discard criteria**
- Broken wires per 6d and 30d, by rope category (RCN) and lay, are in Table 3 (p23–24) and Table 4 (p25, rotation-resistant). Valley breaks and termination breaks: 2 or more (Table 2, p22).
- Diameter: discard at 10 %, 7.5 % or 5 % below d_ref, as a share of nominal, by rope type (Table 5 p26; 6.4.2 p27).
- MRT: LF limit is 6 % over 6d and 10 % over 30d; LMA limit is 10 % over 30d. Both apply to all constructions (Annex C, Tables C.1 and C.2, p43–44).
- Corrosion is judged in steps (Table 6 p28). Deformation: 6.7 p28–30. Combined effect: Annex G p54–56.

**3. Instrument and inspection requirements**
- No numbers for sensitivity, resolution, speed, saturation, sensor type or SNR. The only performance remark is that break gaps below the instrument's sensitivity are missed (5.6 p21).
- MRT must run together with a visual inspection (5.6 p21).
- Personnel: a competent person in MRT and trace reading (3.7, 3.8 p9). For LF and LMA that person needs the rope's wire data and metallic area (6.3 p25).
- Records: the E.3 MRT report fields include speed, head, sensors, length, and LMA and LF traces (p50). A written record goes with the next-interval date (5.3.5 p20).
- Intervals: set by the competent person; no fixed number (5.3.2 p19). Inspect after 3 months idle (5.5 p21) and after any incident (5.4 p21).

**4. Terminations, sheaves, diameter tolerance, lubrication, temperature, rope type**
- Terminations: inspect closely (5.3.4 p20). Discard at 2 or more breaks there (Table 2 p22). MRT cannot reach near terminations or equaliser pulleys (5.6 p21).
- Sheaves: groove 5–10 % over nominal and at least 1 % over actual (4.4 p12). Check that sheaves turn freely (4.8 p17). Waviness limit on sheave sections is 1/10·d (6.7.2 p28).
- New-rope oversize: no tolerance is stated. The worked example uses 41.2 mm on a 40 mm rope, i.e. +3 % (6.4.2 p27). d_ref is the baseline that absorbs the oversize.
- Lubrication: dress before the rope dries out, with a compatible penetrating dressing (4.7 p17). Loss of grease is a sign of heat damage (6.7.10 p30).
- Temperature: only storage ("cool, dry") and heat damage are mentioned (4.3 p12; 6.7.10 p30).
- Offshore and marine: offshore and floating cranes are in scope (1 p7). Corrosion is worse in marine air (F.3 p52). Annex G Example 6 is an offshore crane (p56).

**5. Continuous or permanently installed monitoring**
- **Nothing in this document.** MRT is treated only as a periodic test done by a competent person.

## D. Not relevant / skipped

- PDF p2, copyright page: not read; boilerplate.
- PDF p5, Foreword: not read; procedural.
- PDF p14–15, Figures 4–5 on uncoiling: not read; installation pictures only. Page 16 was read.
- PDF p32, Annex A Figure A.2 (multi-layer zones): not read. A.1 on p31 was read.
- PDF p33–42, Annex B photos of deterioration modes: not read. They are pictures; the criteria they illustrate are in clause 6.
- PDF p45–47, Annex D, internal examination with clamps: not read; a manual method, not MRT.
- PDF p49, Annex E.2 running-record form: not read. E.1 and E.3 were read.
- PDF p58–62, rest of Annex H (RCN drawings): not read. Only needed to look up the RCN of our actual rope construction.
- PDF p64, Annex I Figure I.4 (likely the discard-level corrosion photo): not read.
- Everything else was read page by page: pages 1, 3–4, 6–13, 16–31, 43–44, 48, 50–57, 63, 65 and 66.

## E. Unsure

- The **LMA baseline is ambiguous.** 3.15 measures LMA against the nominal metallic area of the new rope, while 3.13 and 5.6 make the base trace the datum. The standard does not say how an instrument zeros or scales LMA against the base trace. That would be in ASTM E1571 or IMCA SEL 023, which I did not read and which are not in the PDF.
- 5.6 cites "ASTM E157-11(2016)e1". The bibliography has E1571-11(2016)e1. I take it to be a typo in the standard.
- Table C.1 is labelled LF but expressed as % metallic area over 6d and 30d. It is not clear whether the 10 %/30d LF limit and the 10 %/30d LMA limit (Table C.2) are meant to be checked separately or added. Annex G treats them as separate columns, adding only at the same location.
- In Annex G Example 5 (p55) the text quotes 21.7 mm measured but calculates with 21.8 mm. This is an inconsistency in the standard, not a misreading.
- Shiplifts are not named in the scope (p7). Whether ISO 4309 applies to shiplift hoist ropes is a judgement call, not something stated.
- All values were read from rendered images, not extracted text. The table numbers were clear, but I did not cross-check them against a second copy.
- To read the pages I rendered all 66 to temporary PNGs in the session scratch folder (`dsc_work/r/`), outside the repository. They are deleted after this note; no copy of the PDF or its pages is kept anywhere else.

— Bosun

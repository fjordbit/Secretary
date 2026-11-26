# Sources for the board package (FOR THE OWNER: do not send)

The tags in `board_package.md` refer to the files below. Paths are relative to the project repository
(`max/` at main 0a26739) unless marked otherwise. "Not in main" marks a file that has not been merged yet.

| Tag | File | What it gives |
|---|---|---|
| S1 | max/sws/hw-selection/element_run_3/element_run_3.md (+ source.md, figures fig_e1_*.png, fig_e3_board.png) | the field at each element, N52 / N48SH; positions and pitch; the parts read on their sheets; the cases; what the sheets do not say |
| S2 | max/sws/hw-selection/element_round_1/element_round_1.md | the outside reviews against run 3; Hall against TMR for the axial element; added risks |
| S3 | max/sws/3d/falsify/g_large_box.md, Tables 1 and 2 | the corrected groove depths (large box), levels, nearby steel |
| S4 | max/sws/3d/groove_plots/README.md, figure D | prototype head as drawn: zero 16.7 mm (calculated) |
| S5 | max/sws/parts_table/parts_table.md, by row id | rulings, the values recorded more than once, the converter, temperature, supply, line, potting and housing rows |
| S6 | max/sws/spec/rendered/SWS_HW_Design_Input_Specification_rev131.md, §6, §7, §9, §10 | specification (it still shows the spoke layout and RS-422; those parts are superseded or open) |
| S7 | max/sws/hw-selection/sws_link_and_readout.md §2 | the ADS131M08 data-sheet check (REFIN, input impedance, power, packages) |
| S8 | max/docs/sws/build_hardware.py, section "hw-cases" (hardware.html#hw-cases) | converter cases A / B / D, the multiplexed alternative |
| S9 | max/docs/sws/build_sensor.py, section "s-where" | room per position, 40 mm rope 25.0 mm / 9.82 mm |
| S10 | max/sws/3d/h40_on_38/h40_on_38.md, "In plain words" 5 | 40 mm head on a 38 mm rope: −6 mT at the 16 mm element |
| S12 | secretary/log/2026-11-25.md, "U124 back" (first analysis of the prototype recording; not in main) | measured: the strong-magnet event, 0.4–2.5 mT radial, up to 0.64 mT axial |
| S13 | secretary/log/2026-11-20.md 10:21 (board thickness ours, 5 V only if a part needs it); log/2026-11-18.md (thin plate); START.md 26 Nov (RS-485 ours to propose; board package out 1 Dec); agent-notes/kai.md "## U142" (ruled facts list) | rulings |
| S14 | secretary/log/2026-11-19.md (data-path return: 1-wire workable but weak) | temperature part note |

## Source conflicts found (both values given in the package; the later is named)

1. Groove depth for the zero at 13 / 16 / 19 mm: 4.98 / 4.25 / 3.53 mm (modelled magnet, S3) against N52 4.34 / 3.58 / 2.77 mm and N48SH 3.92 mm for 16 mm (element run 3, later, S1); the old box 6.08 / 5.36 / 4.64 mm is superseded. Parts table also notes 3.92 mm named N40SH in one note and N48SH in another (S5 Y04).
2. Level per 1 % of metal at 16 mm: 0.675 mT (modelled magnet) against 0.774 (N52) / 0.802 (N48SH) mT (run 3, later); 0.768 / 0.806 mT with the groove re-cut (S5 A05).
3. Broken-wire signal at 5 mm: 0.39 mT (literature transfer, specification) against 1.17–1.36 mT outer / 0.113–0.301 mT inner wire (3D) and 1.27 / 2.69 mT for one / two hidden wires (sensor page).
4. Radial noise requirement: 0.11 mT p-p (specification, 52 mm rope) against 0.056 mT p-p derived from the 3D inner-wire signal.
5. Converter reference: "internal 1.2 V only" (specification) against REFIN 1.1–1.3 V (data sheet).
6. Converter power: 21.5 mW typ (data sheet, HR) against 6.0 mW (register).
7. Converter / line rate: 4000 / 500 / 250–1000 per second across notes; line 250 per second is a proposal.
8. Power per half: 0.2–0.4 W (specification) against under about 0.5 W (hardware page).
9. Line: RS-422 one per half (specification) against RS-485 shared (proposed; START 26 Nov). On record the shared RS-485 line is two-wire, polled (log 20 Nov).
10. Board arrangement: spokes (specification, never confirmed) against one thin board (ruled).
11. TMR2584 saturation: ±30 mT (electrical table) against ±20 mT (selection guide).
12. Temperature parts: one per half plus one on the yoke (specification) against nine to ten per half (outside round); two per half ruled.
13. Installation size: 102 SWS / 204 halves (parts table I03) against 204 SWS / 408 halves (ruling of 26 Nov, later). Not used in the package.
14. Frame size at 250 per second: 1 229 bytes against 1 227 bytes (header 25 or 23 bytes).

Measured figures used: only S12 (prototype recording, first analysis). All other field figures are calculated.

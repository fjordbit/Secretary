## 2026-11-10 22:38 (machine clock) — started
- Unit / branch: U61 / u61-software-page from 9b452f9 (C:/Users/stian/Prosjekter-u61/max)
- Rests on: sws/hw-selection/sws_link_and_readout.md (U60 note, SBAS950B facts); spec rev130 render §4/§6/§7/§10; sws_sync_findings.md; sws_link_budget.py; rounds/2026-11-10 (proposals only).
- Timebox 2 h, ends ~00:38 machine clock.
— Forestay

## 2026-11-10 23:06 (machine clock) — committed, done
- Unit / branch: U61 / u61-software-page (C:/Users/stian/Prosjekter-u61/max); commits fbaa040, cc083e9, 3f03b44, b616745.
- software.html 5 A4, hardware.html 4 A4; five --check ok; 78 SWS tests; identifier scan 0.
- Three review rounds: reader YES WITH RESERVATIONS x3; falsifier PASS WITH FIXES x3, fixes applied.
- Ready for Kai's check: yes. Needs Stian: ADS114S08/ADS124S08 data sheets unchecked (D looks one-sided); 1.0 ms split vs 0.25-0.6 ms; spec §7 reference statement; noise-limit definition and engagement terms.
— Forestay

## 2026-11-10 23:2x (machine clock) - round 4 committed
- Case D checked against SBAS660C/SBAS815A; sws_mux_rate.py; two time requirements on both pages. Commits 7a9bf09, then the final one. 80 tests; 6 / 4 A4; scan 0.
- Forestay

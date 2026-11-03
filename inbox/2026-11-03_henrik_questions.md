# Henrik — questions on the SWS head geometry and Bz sensor radius (3 Nov 2026)

Pasted by Stian, 3 Nov. Drawings: `Prosjekter/new/henrik_2026-11-03/` (yoke sd00039125 A.1, ring magnet N-S sd00037347 A.1).
Answered by agent Compass (Fable) on branch u17-bz-radius-henrik; reply draft in inbox/drafts/.

---

Dette er geometrien. Tror du misforsto cutout'en, fikk inntrykk av at du hadde modellert det som to separate biter? Er et mindre "notch" som går på utsiden av yoke. En annen ting -- Bz sensorer per idag er ikke plassert på samme radius som Br sensorer. De ligger vel på R=36.5 om jeg ikke tar feil, for å komme seg vekk ifra "background-flux" og mindre direkte påvirkning av local-flux-leakage. Kanskje dårlig design da det blir et slags low-pass filter (les: diffust), men jeg har i grunn tenkt at det er hensiktsmessig med "separation-of-concerns" (igjen, kanskje dårlig design). Det eksisterer en radius i z=0 planet hvor B=0. Uten cutout er denne radius lik inner-radius på yoke. Området rundt radius hvor B=0 ble funnet som sensitiv for LMA. Cutout kunne brukes for å påvirke radius (flux-leakage på motgående side av kretsen), og flytte den lengre inn i sensor-hode (for å fysisk få plass til Bz sensor i sensitivt område). Ordet sensitiv er kanskje feil -- rettere, forhold mellom "background-flux" (ref. sensor-ranges) og utslag -- så, andel "utilized-sensor-range". Bz ble plassert litt utenfor r=r(B=0), for å oppnå "stivhet".

Jeg er veldig interessert i en analyse av radius for Bz ift. LMA/LMV med den "enginen" vi har nå, spesielt når vi er på stage 2/3 (?) altså med faktisk vaier-geometri. Får inntrykk av at du i hovedsak har fokusert på Br? Mulig jeg kanskje ikke helt har forstått alt som er skrevet, men du har kanskje funnet en plassering/geometri med nær-null "background-flux" for Bz? TMR sensorene er bi-direktionelle/0->X stort sett, men hall-sensorer skal kunne ha et range hvor vi har X->Y. Kan være en tanke.

Interessant angående powerplast ift. paraplast (helt annen konstruksjon), og hvordan fokuset per ISO 4089 (?) bør være LMA.

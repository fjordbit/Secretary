# Utkast — svar til Henrik (sendes av Stian)

Til: Henrik · Emne: SWS-hode: notch, r(B=0) og Bz-radius — svar med tall

Hei Henrik,

takk for tegningene (sd00039125 YOKE A.1, sd00037347 RING MAGNET A.1). Vi har kjørt dem gjennom den samme 2D-aksesymmetriske FEM-en som før (Ø40-prototypen slik den er tegnet: magnet R24–R44 × 20 mm, åk Ø86/Ø102 × 105, polavstand 65 mm, 25 °C). Vaieren i modellen er en 40 mm Powerplast-lik vaier (stålfyll 0,727). Jeg forstår at prototypen ble testet med en annen 40 mm vaier — hvilken konstruksjon og stålkvalitet var det? Det påvirker metning og signal per % LMA, så tallene under gjelder modellvaieren inntil vi har den. Tallene under er fra én mesh per hode, intakt mot en ringdefekt (30 % ståltap i de ytterste 2 mm over 8 mm = 5,7 % LMA). Full rapport og figurer ligger i repoet (U17).

**1. Cutout-en var modellert feil.** Ja. Vi hadde modellert et luftvindu gjennom hele åkveggen (10–90 mm bredt) på 52-hodet. Tegningen viser et 10 mm bredt × 2 mm dypt spor på utsiden ved midten (Ø102 → Ø98), 6 av 8 mm vegg står igjen. Kjørt på nytt med det riktige sporet:
- B i vaieren: 1,994 T uten spor, 1,989 T med (−0,2 %). Vinduet vi hadde regnet på kostet 14 %; sporet koster nesten ingenting.
- Defektsignal ved 3 mm avstand fra vaieren: Bz −14,3 mT uten, −14,2 med, −14,4 med spor og magnet skalert til lik induksjon. Br: +13,5 / +13,3 / +13,5 mT. Altså innenfor ±1 %.
- Konklusjonen fra før står: sporet gir ikke bedre avlesning i noen kanal ved lik induksjon. Men det er billig, og det gjør det du bruker det til (punkt 2). Ingen 3D nødvendig for dette.

**2. Radien der B = 0 i z = 0-planet.** Du har rett på begge punkter.
- Uten spor: r₀ = 42,5 mm, dvs. åkets innerradius (43,0). Grunn: H er kontinuerlig over boringsflaten, så lufta ved åket bærer μ₀·H(B_åk) ≈ 1,2 mT ved 1,37 T i stålet.
- Med spor: r₀ = 39,6 mm (2,9 mm innover). Mekanismen er at sporet laster stålet ved z = 0 opp fra 1,37 til 1,81 T; da trengs ~11 kA/m, og lufta ved boringen bærer ~13 mT i returretning. Lekkasjen ut gjennom selve sporet er liten (12 mT i sporet).
- r₀ er ikke et fast punkt: 40,5 mm ved hard tråd/+80 °C, 38,5 mm ved myk tråd/−40 °C. Bz ved R = 36,5 varierer tilsvarende −8 til −12,5 mT (−11,0 ved 25 °C).
- I vår modell ligger 36,5 mm 3,1 mm *innenfor* r₀, ikke utenfor. Hva får du for r₀ i din modell? Og kan du bekrefte 36,5 mm og at magneten er N42 (vi har ikke datablad, har brukt Br 1,28 T)?

**3. Bz-radius (hovedspørsmålet).** Sveip av sensorradius, Ø40-hodet med spor, Bz i z = 0:

| r_s | avstand | bakgrunn | signal 5,7 % LMA | bevegelse 0,5 mm (2D-gradient) | signal/(bakgrunn+bevegelse) |
|---|---|---|---|---|---|
| 23 mm | 3 mm | −45,7 mT | −14,2 mT | 0,9 mT | 0,30 |
| 36,5 mm | 16,5 mm | −11,0 mT | −1,30 mT | 1,7 mT | 0,10 |
| 39,5 mm (≈ r₀) | 19,5 mm | −0,5 mT | −0,77 mT | 1,8 mT | 0,33 (kun i ±0,5 mm, og ved én temperatur) |

- Signalet faller 11× fra 3 til 16,5 mm, bakgrunnen 4×, og "stivheten" blir dårligere, ikke bedre: gradienten er 1,9 mT/mm ved vaieren og 3,7 mT/mm ved r₀. Vi finner ingen stiv sone nær åket i 2D. Ditt "low-pass filter" stemmer.
- Nær null bakgrunn finnes ved r₀ = 39,6 mm, og det koster 18× signal, en bevegelsesterm på 2,4× signalet, et ±0,5 mm vindu, og r₀ flytter seg 2 mm over temperaturboksen.
- LMA: 0,23 mT per % LMA ved 36,5 mm mot 2,5 mT per % ved 3 mm. Et 10 % LMA-trinn gir 2,3 mT ved 36,5 mm, 18× støybudsjettet (0,13 mT p-p for 40 mm). LMA-funksjonen overlever på 36,5 mm.
- Lokal defekt (LF/LMV) ved 36,5 mm gjør det ikke: kort ring 0,23 mT mot 5,4 mT ved 3 mm, og en ekte brutt tråd faller raskere (dipol-anslag ~1/170 av 3 mm-verdien). 2D kan ikke regne en brutt tråd; det går til 3D.
- Br på egen radius, samme målestokk: ved 3 mm og z = 4 mm gir ringdefekten +13,3 mT på 7,1 mT bakgrunn med løft-følsomhet 0,25 mT/mm, dvs. 1,8 på samme figure of merit — 6× Bz på samme radius. Det er derfor vi har brukt Br som LF-kanal, ikke fordi vi har glemt Bz. Begge kanaler vil ha minst mulig avstand; Bz er LMA-kanalen (summert = hovedfluks), Br er LF-kanalen.

**4. TMR (bipolar 0→±X) mot Hall med offset-område (X→Y).** Når bakgrunnen er uunngåelig (−46 mT ved 3 mm, −11 mT ved 36,5) utnytter et område sentrert på bakgrunnen spennet bedre (14 mT signal = 12 % av ±60 mT, men 47 % av et 30 mT spenn rundt −46 mT). Med 24-bit ADC er spennet likevel ikke det som begrenser; det er forsterkningsdrift × bakgrunn (f.eks. 0,1 %/K × 46 mT = 0,046 mT/K mot 0,13 mT p-p-budsjett — eksempeltall, ikke en komponentspek). Ved bakgrunn ≈ 0 (r₀) er bipolar riktig, men se punkt 3: r₀ flytter seg. Valget avhenger av radius (bakgrunn og signal der), spredningen i bakgrunn over vaierstørrelse/temperatur/magnetparti, driftstallene til komponenten, og om Bz-kanalen får være en ren LMA-kanal. Komponentvalg er U9.

**5. Powerplast / Paraplast og standarden.** Standarden er ISO 4309:2017 (kraner — ståltau — vedlikehold, inspeksjon, kassering), ikke 4089. Vi har den ikke i hus ennå; i spesifikasjonen står at den gir kasseringskriterier i % LMA og trådbruddtall, og at for rotasjonsfattige tau er indre nedbrytning den styrende feilmoden. Det er derfor LMA-fokuset følger for Powerplast: stålkjernen ligger bak en plastkappe, ~13 mm dypt; én brutt kjernetråd gir 0,065 mT ved 5 mm og reagerer knapt på avstand, så indre slitasje kan bare sees som LMA. Ytre trådbrudd er LF for Br. Paraplast har vi ingen data på her — kan du sende kataloglinjen (slag, kjerne, kappe, C-faktor)? Da kjører vi samme modell på den.

**Hva som går til 3D (Strand, U16, pågår):** brutt tråd mot sensorradius 23/25/30/36,5/39,6 mm på ditt Ø40-hode, ekte bevegelsesterm (eksentrisk vaier 0,5 mm) ved 36,5 og 39,6 mm, og ringdefekten i 3D som kobling til 2D-tallene over. Første tall sender jeg så snart kjøringen er ferdig.

Hvis du kan bekrefte spor 10 × 2 mm, R = 36,5, N42 og hvilken vaier prototypen gikk med, så låser vi geometrien og vaieren i modellen.

Mvh
Stian

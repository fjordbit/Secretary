# Deadeye — U101 section F (magnet and mechanics), falsifier

Worktree C:/Users/stian/Prosjekter-u101f, branch u101f-falsify from c19d94c (verified). Adds only under
max/sws/3d/falsify/. Timebox 180 min.

Plan: real thicker magnet (N48SH, N52) with the groove re-cut for the zero at 16 mm on H52, steps 1.90-2.10 T;
demag at +45 C against each grade's knee (register / sws_head.py values); halves force and pull on the rope by
Maxwell stress (2D thin-gap estimate, checked against the 3D P52 value); stray field 50/100/300 mm and the 0.5 mT
radius; weight; F3 competitors (uniform thin yoke, wide steps, narrow and inner grooves, other steels).

— Deadeye

## Done (tip c1ee951 on u101f-falsify, about 95 min)
Note max/sws/3d/falsify/f_magnet_mech.md. Main finding: with a real thicker magnet the yoke face moves out and the
groove cannot hold the zero at 16 mm above about 2.0 T (even a 16 mm yoke cut to 0.5 mm); magnet null 1.955-1.958 T
(knob 1.97) and the magnet error grows about 4x faster above it. N52 head empty at +45 C: 57-88 % beyond knee.
Halves hold 560 -> 400-490 N (x1.5) -> 270-400 N (x1.9); empty push 1.26 -> 2.1-2.7 kN. F3: thin yoke reaches 16 mm
on H52 but needs 1.6-1.7x magnet; best competitor 5 mm groove, 3 % less. 0.5 mT radius not resolved (box).
Checks: build --check 8/9 and pytest 180/181, both only stale report.html (base); idscan 0; scan_tree 0.
Results were first written to sws/3d/results/ by the script and moved into falsify/results/ before commit.
— Deadeye

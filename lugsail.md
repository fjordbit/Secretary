# lugsail — U138 (steel near the SWS in 3D, screening)

Builder notes to Kai. Worktree C:/Users/stian/Prosjekter-u138, branch u138-steel-nearby from 67866d8.

- Start: main verified at 67866d8; worktree made. Machine: 24 threads, 62 GB RAM (about 38 GB free at start,
  other python processes present).
- Record read: falsify/g_large_box.md (the "1-8 % of metal" is 2D axisymmetric: tubes/shells as round stand-ins
  for one-sided steel, in-house 2D solver, box r 2400 x z +-2400, A = 0); element_run_3.md (positions: 16 at
  22.5 deg, split mid-way, radial at 5 mm lift-off r 31, axial at 16 mm r 42, N52 18.1 mm / groove 3.58 mm,
  N48SH 19.1 mm / groove 3.92 mm, middle rope curve, level -0.774 / -0.802 mT per 1 %).
- Plan: 3D NGSolve half-space (mirror x = 0), full z (the platform is one-sided in z), model3d's solver copied
  with the magnet sign per pole; all disturbance solids in one mesh where they do not overlap, switched between
  steel and air, so differences carry no re-meshing noise; warm start from the baseline.
- Kai's two corrections received (stainless holder/arm, wall framing, mu_r 1.0/1.1/magnetic stainless; proposal
  section). Folded into sn_run.py (walls 80-600 mm + 1 x 1 m wall mesh W; stainless bracket mu_r 1.1/2/5/50).
- Test (mesh B3, N52, 381 k elements, 2.0 M dof, order 2): baseline 317 s cold, 10 Newton steps, peak 10.4 GB;
  steel plate case warm-started 59 s, 2 steps. Baseline zero 15.85 mm (2D record 16.0 mm). 300 x 300 x 15 mm steel
  plate at 143 mm: B_z at 16 mm +0.69 ... +0.70 mT all round the rope (nearly uniform: the yoke ring spreads it),
  i.e. about -0.9 % of metal (read as gained) on the record's -0.774 mT per 1 %; B_r and B_phi on the mid-plane 0.
- Launched two queues (F/P/N/N2/W per grade). Mesh F is 787-790 k elements (about 4 M dof); both processes at
  13.5 GB each and rising, 14 GB free. Tried to stop the N48SH queue to stay inside memory: PERMISSION DENIED.
  Stopped work per the brief and handed back. Nothing committed; files uncommitted in the worktree
  (max/sws/3d/steel_nearby/: sn_model.py, sn_run.py, sn_report.py, sn_figures.py, run_queue.sh, logs/).
— lugsail

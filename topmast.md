# topmast — U99 builder notes (plot layout)

- Started 20:03; timebox to 22:03. ab4fe6b = u97-groove-physics tip, verified. Worktree C:/Users/stian/Prosjekter-u99, branch u99-plot-layout.
- Solver venv has plotly 7.1.0, matplotlib 3.11, contourpy 1.4, pillow; no cairo. Test venv (u41) has no numpy/matplotlib.
- Sensor page test: _Walk skips style/title/code/script and reads text nodes only; attributes are not read. So hover text kept in a <script> JSON block (or attributes) is not counted; the plain-text explanation under a plot and any SVG <text> tick labels are counted.
- Technique: inline SVG + ~90 lines own script (plotly self-contained 4.8 MB/plot, measured). Sizes 33 / 46 / 158 kB.
- Commits ff44727 (layout, three plots, standard, test) and ab5ee65 (cold-reader fixes). No page/builder/existing figure touched.
- Verified in headless local Chrome by a scripted harness: About tap, legend focus/toggle, arrow stepping, tap on curve/dot/panel, map keys; dark + light; 360 px iframe (line plots scroll inside the figure); print to PDF written but not looked at (no PDF renderer).
- Checks: interactive_figures --check ok; builders 8/9 (build.py: report.html stale = U95/U96/U97 register rows, rebuilt+diffed, restored); pytest 184/185 (180/181 base + 4 new; same report test fails); idscan 0 (3 long data lines skipped by idscan; scan_tree on the 10 added files 0).
- Owed: SVG tick/contour labels vs the sensor-page number test (test change or labels to attributes); legend tap hides the curve as it explains it (tooltip says so); not tried on a real phone or screen reader.

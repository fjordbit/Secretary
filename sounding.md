# sounding — U104 plot standard (19 Nov)

- Repo C:/Users/stian/model-round, branch plot-standard from bc6c4cd (verified). Commit 573e59b. Not pushed.
- Delivered: docs/PLOT_STANDARD.md, plotstandard.py, examples/plots/ (make_examples.py, research.html/.png,
  presentation.png, terms.md, source.md), tests/test_plotstandard.py; README paragraph "Plots"; CLAUDE.md one line.
- matplotlib >=3.8 added to requirements-dev.txt only (README's "one library the tool needs" stays true);
  installed into the repo .venv from PyPI.
- Source read: ab5ee65 plotlayout.py, PLOT_LAYOUT.md, demo/interactive_figures.py. Generalised: inline SVG +
  small script for hover, matplotlib PNG twin, Okabe-Ito, words beside the data. Dropped: About block, text under
  the plot, map kind, keyboard stepping, bands/lines/points.
- Added beyond the brief: "slide": False per curve (the 4-curve slide with near-identical curves was unreadable).
- Cold reader (one pass): BLOCKING PNG twin lacked how/terms -> legend now says "(measured)" etc. and links are
  printed; grey-readability fixed (markers/dashes vary within a kind, tested); abbreviations banned on slides;
  duplicated numbers cut from the bullets; slide title "afternoon" -> "Around midday". No second pass.
- Hover verified in Chrome via a localhost server with synthetic pointer events (text and value line correct);
  screenshots of the page failed (renderer timeout), so the HTML layout was never seen rendered.
- scan_tree on `git archive plot-standard`: 28 files, 0 hits.
- Mistake: a failed PowerShell one-liner created an EMPTY file C:/Users/stian/secretary/plotstandard.py
  (untracked). Deleting it was refused by the permission classifier; it needs removing by hand.

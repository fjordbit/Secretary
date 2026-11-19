# Sternway — U105 Scotchcast potting resins (builder notes to Kai)

- Worktree C:/Users/stian/Prosjekter-u105, branch u105-scotchcast from 062b8bd (main verified = 062b8bd).
- One file added: max/sws/hw-selection/sws_potting_scotchcast.md. No existing file changed.
- Sheets: multimedia.3m.com and 3m.com refuse (403) to curl and WebFetch; read the same addresses from web.archive.org
  copies (addresses in the note's §7). Distributor copies for 8882, 2130, 2131-2013, 40G, Resin 4, Resin 5.
  All read in full via pdftotext into the session scratchpad (u105/); no PDF in the repo.
- Not readable: the 2123 US sheet (Jan 2015; chipdip copy 404, elliott refused) — search snippets quote Tg −78 °C and
  0 Shore A from it; NOT used. 1400U sheet 404. No sheet for "2114" found.
- Quotes cut to one per source after a check (grep of quoted strings).
- scan_tree on a copy of the note before commit: 0.
</content>
</invoke>
- Falsifier (fresh subagent, note + sheet addresses): numbers and arithmetic hold; 6 blocking wording/attribution
  points (40G shrinkage contradiction, 2131 gel time US not UK, Resin 5 is room-curing, 0.6 K says nothing on stress,
  2131 adhesion "meets" too firm, "semi-rigid"/"rigid" not on sheets) + minors; all fixed, glossary line added,
  MR283 archive address added. No second pass (none blocking after fixes).
- Commit dde443c on u105-scotchcast (1 file, 205 lines). idscan 062b8bd..HEAD 0 (205 lines); scan_tree 0 (before and
  after commit; idscan needs the commit, so it ran on the committed range). No merge, push or export.

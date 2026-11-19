# Fid — U50 (branch u50-task-not-owner, worktree C:/Users/stian/Prosjekter-u50)

10 Nov. Brief: kai.md "## U50" plus Kai's additions (rule 7 no time narration; tyre analogy replacing the river and
the outside links; analogy wording left to the builder).

Rows this rests on (rule 10): register l.17, l.191, l.192, l.329, l.330, l.333, l.340, l.348, l.349, l.350, l.351,
l.360, l.361; design.md l.242; U39 report l.38, l.63; design notes sws-easy-read.md, sws-easy-read-plain.md.

- Provenance now in link titles via prov()/pv() in build_short.py: the attribution is read from the cited row (regex
  group), so a title cannot say what the row does not.
- Test conflict found and resolved in-scope: test_no_unlinked_number_in_tooltips (U42) forbade any number in a title;
  the brief puts dates and row numbers there. Narrowed to its intent: a title's numbers must be on the row the link
  cites; any other tooltip stays number-free. Planted-failure test added.
- Analogy: the first sentence (tyre picture) is plain text; the l.17 anchor sits on "the magnets fill the rope's steel
  with magnetic field" (a picture is no project claim).

— Fid

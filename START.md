# Kai — start here (state as of 10 Nov 2026 01:1x, U48–U51 live)

Read in this order at the start of a session: this file, `todo.md`, the newest `log/*.md`, then
`C:/Users/stian/agent-notes/kai.md` (my briefs to builders; the last sections are the live units) and any new
builder notes in that folder (nautical names). Rules: `CLAUDE.md` here and the memory directory. Rule 10 in
`C:/Users/stian/Prosjekter-u05/max/CLAUDE.md` l.60–71 binds every brief and report.

## Where the work stands

- **Project repo** `C:/Users/stian/Prosjekter-u05/max`, branch main at **5972096** (U50 merged, 10 Nov 00:5x), pushed to the
  local origin (D:/git/prosjekter.git). GitHub fjordbit/max main is **78b9e8c** = the rewritten export of local 5972096
  (fast-forward, nothing deleted). Next increment: same method from the clone `C:/Users/stian/export-v3/export`, range
  from 5972096, graft on 78b9e8c (brief pattern: kai.md "## U49", "## U51"). Pages: publish/SWS at **0e01f10** (index.html = dense
  short page, landing; report.html = full report; easy.html = easy read), pushed to both remotes 10 Nov 01:1x.
- **10 Nov, after Stian read the live page** ("a biography of me"): U50 moved attribution and dates out of the prose
  into link hover titles on the easy read and short page, analogy = his tyre-under-water picture, outside links
  removed; U51 exported it. Rule and the cold-reader check: memory pages-about-the-task-not-stian. The short page
  still reads as a record (cold reader) — in todo, his call how far. Read log/2026-11-10.md.
- **Nothing running.** U48 (standard on file, register notes, river analogy on the easy read) and U49 (export +
  snapshot) closed. Builders: Sheave, Bowline. Bowline could not write export-v3/REPORT-6.md (harness refused); its
  hand-back is in log/2026-11-09.md and agent-notes/bowline.md.
- **Identifier scan script** is session scratch and dies with the session: rewrite as before (flat parse of
  identifiers.yaml, regex `match` per entry or the literal name, added lines of `git diff -U0 <range>` only, print
  entry index and kind, never the name). No PyYAML in the U41 venv.
- **The standard:** BS EN 12927:2019 at C:/Users/stian/max-private/standards/BS-EN_12927-2019.pdf (copyright: never
  in a repo). Beside it: Kai's ch.14 extract and the **clause map** (EN12927-2019_clause_map.md, 9 Nov: every clause
  that bears on the instrument, corrections to the extract, ambiguities). **The owner's B_rope / B_wire reading is
  still his call** — ask him 10 Nov (one question, visible). The map's finding for that question: Annex B is
  informative and does not say whether B is local, over the metallic area or over the nominal area.
- **Open from U48 (Stian):** register l.348 says both "not on file" and "on file 9 Nov"; l.192 value column ("inner",
  "< 0.5 % LMA") does not match 14.3.5.2's wording; the extract lacks 14.2.1 (3-year flux check), 14.2.3 (≥ 1
  sample/mm), 14.3.3 (max 5 m/s), 14.1 (exclusions) — candidates for requirement rows in the register.
- **Decided 9 Nov:** landing page = the dense short page (index.html); easy read = easy.html, third button; full
  report = report.html. Never merge "short" and "easy" again (memory three-sws-formats-easy-is-the-test). Easy-read
  analogy = tyre under water, the sensors do the water's job (Stian's picture, 10 Nov; the river is gone).
- **Backup:** full file copy `D:\backup\2026-11-09_0223\` (2.5 GB; holds identifiers.yaml and the transcript with
  the pasted API key — local disk only). All repos committed and on D:/git.

## Rulings from 8 Nov evening not yet fully in the record

- Envelope −40 / +50 °C for service, storage and transport (49 °C record day → 50); the magnets set the
  transport limit; magnets procured to "zero irreversible loss after a +50 °C excursion in the open-half state";
  no further FE runs until the supplier's data for one-piece radial arcs is on file. Recorded as "U36 addendum" in
  kai.md; register l.361 and rev130 l.233/367/428/429 still say "owner to set" → next spec unit (small, docx route).
- Owner's reading accepted by me: "ambient at the sensor" is the editor's reading (marked so in rev130).

## Waiting on Stian (also in todo.md)

Mail to the head designer sent 8 Nov (draft in inbox/drafts/sent/). Create the GitHub issue from
`inbox/drafts/2026-11-08_github-issue_magnet-spec.md` (gh CLI not installed; his login); Word master rev128–130;
register l.331/332 keep or retire; 52 mm wire diameters from the rope maker; R5 (Ø48 3D) yes/no; rotate the
API key (pasted in chat 8 Nov) after the next review round; the "other hardware" tier-0 pass (Fable + GPT 5.6
Sol via tools/review_round.py with the key loaded in-process) once he names the sections.

## How I am started

A fresh session knows only the files: CLAUDE.md, the memory directory, and what I read from here. Resuming the
previous session (`claude -c` in this folder) also restores the conversation transcript. Either way, this file is
the state; keep it current at every handoff and delete the "running" lines once the units are closed.

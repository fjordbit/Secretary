# Kai — start here (handoff written 9 Nov 2026 23:4x, before a restart onto the newest Fable)

Read in this order at the start of a session: this file, `todo.md`, the newest `log/*.md`, then
`C:/Users/stian/agent-notes/kai.md` (my briefs to builders; the last sections are the live units) and any new
builder notes in that folder (nautical names). Rules: `CLAUDE.md` here and the memory directory. Rule 10 in
`C:/Users/stian/Prosjekter-u05/max/CLAUDE.md` l.60–71 binds every brief and report.

## Where the work stands

- **Project repo** `C:/Users/stian/Prosjekter-u05/max`, branch main at **5c4297f** (U46 easy read merged + link fix, 9 Nov 19:0x), pushed to the local origin
  (D:/git/prosjekter.git). GitHub fjordbit/max main is **6f70bfc** = the rewritten export of local 5c4297f (U38/U40/U43/U44/U47, 9 Nov; fast-forward,
  nothing deleted). Next increment: same method from the clone `C:/Users/stian/export-v3/export`, range from 5c4297f
  (brief pattern: kai.md "## U38" and "## U40"). Pages: publish/SWS at d8c54c9 (index.html = dense short page, landing; report.html = full report; easy.html = easy read), pushed to both remotes 9 Nov 19:3x.
- **Units merged tonight:** U35 (3D appendix runs folded in), U36 (spec rev130: envelope remade; register rows;
  2D excursion table), U37 (identifier sweep of SWS files). Page rebuilt at d455e3d, then U37.
- **Nothing running.** U35–U47 closed 9 Nov 19:3x. **Next, in this order, first thing after the restart:**
  1. Start the U48 builder (Opus) from kai.md "## U48" (easy read + short page wording: the standard is on file; flow-and-leak
     analogy; register notes l.191/192/348 updated to the text, status letters untouched). Brief is written and checked
     against the extract; it has not been started.
  2. Kai's Fable check of U48 (read the changed sentences against max-private/standards/EN12927-2019_ch14_extract.md),
     merge --no-ff into local main, three --check + SWS tests, push to D:.
  3. Export increment + Pages snapshot (brief pattern kai.md "## U47": range from 5c4297f.., graft on 6f70bfc), own scan
     of both diffs with the identifier list (kinds person/customer/drawing/site/project; scratchpad script scan2.py is
     gone with the session — rewrite: regex `match` field per entry, added lines only), then push export to
     fjordbit/max, snapshot to fjordbit/SWS and MAx-Flow/SWS-Documentation, fetch into D:/git/max-export.git.
  Stian wants this live tonight (9 Nov). Then tell him in one message.
- **The standard:** BS EN 12927:2019 is at C:/Users/stian/max-private/standards/BS-EN_12927-2019.pdf (copyright: never
  in a repo); clause extract beside it. Kai's reading of the words is in log/2026-11-09.md 23:2x. **The owner's
  B_rope / B_wire reading is still his call** — ask him once U48 is live (one question, visible).
- **Decided today:** landing page = the dense short page (index.html); easy read = easy.html, third button; full
  report = report.html. Never merge "short" and "easy" again (memory three-sws-formats-easy-is-the-test).
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

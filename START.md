# Kai — start here (state as of 10 Nov 2026 20:3x, U48–U57 live)

Read in this order at the start of a session: this file, `todo.md`, the newest `log/*.md`, then
`C:/Users/stian/agent-notes/kai.md` (my briefs to builders; the last sections are the live units) and any new
builder notes in that folder (nautical names). Rules: `CLAUDE.md` here and the memory directory. Rule 10 in
`C:/Users/stian/Prosjekter-u05/max/CLAUDE.md` l.60–71 binds every brief and report.

## Where the work stands

- **Project repo** `C:/Users/stian/Prosjekter-u05/max`, branch main at **224704b** (U54 merged, 10 Nov 02:5x), pushed to
  the local origin (D:/git/prosjekter.git). GitHub fjordbit/max main is **9f3beec** = the rewritten export of local
  224704b (fast-forward, nothing deleted). Next increment: same method from the clone
  `C:/Users/stian/export-v3/export`, range from 224704b, graft on 9f3beec (brief pattern: kai.md "## U55", "## U53";
  unlink tool export-v3/tools/unlink8.py). Pages: publish/SWS at **ed8274c** (index.html = dense short page, landing;
  report.html = full report; easy.html = easy read), pushed to both remotes 10 Nov 03:0x.
- **Night of 9–10 Nov, after Stian read the live page** ("a biography of me", "a child writing about his father's
  work"): U50 attribution and dates out of the prose into hover titles; U52 status letters, line numbers, file
  names out of the short page's text; U54 easy read rewritten as an explanation (done / found / where we are / what
  is next, figures + video, his tyre-under-water analogy). The rule for readable pages and the cold-reader check:
  memory pages-about-the-task-not-stian. Stian: the pages stay as they are until the rest of the data is in.
  Read log/2026-11-10.md.
- **Next (Stian, for 10 Nov): HW design — the card itself, sensors, PCB parts.** Nothing prepared yet.
- **U56 + U57 live 10 Nov 20:2x:** local main db05b45; GitHub fjordbit/max 9d9a329; Pages 40f186a (working area
  + plot, B_rope reading, LD / LMA). Next increment: range from db05b45, graft on 9d9a329 (brief pattern kai.md
  "## U57"). Known leftovers in log 10 Nov 20:2x (full report still says "open" inside dated documents).
- **HW design started 10 Nov evening:** head designer chose a multiplexed ADC (log 10 Nov 20:1x); spec §7 is behind.
- **Hardware page: local only.** U58 merged, local main ff08f9f on D: (docs/sws/hardware.html, "Hardware selection":
  four cases, two model rounds). Stian reads it locally first and decides whether the head designer's case is
  attributed at all; NO GitHub / Pages push until he says so. U59 prepares export + snapshot without pushing.
  His leaning (10 Nov): simultaneous sampling, no multiplexer; the outside expert chooses.
- **RUNNING 10 Nov 22:5x:** U59 (export + snapshot, no push) and U60 (Opus, worktree C:/Users/stian/Prosjekter-u60,
  branch u60-link-readout: link and read-out note with pseudocode; brief kai.md "## U60"). Delete when closed.
- **A push was refused once by the session's permission check** (10 Nov ~02:2x) when Stian's last word was
  ambiguous; it went through after his explicit "push when done". Get an explicit go for each push round.
- **Identifier scan script** is now kept: `secretary/tools/idscan.py <repo> <range>` (added lines of the range;
  prints entry index and kind, never the name). In identifiers.yaml `match:` is a MODE ("whole-word", "exact
  case"), not a regex — the scratch versions before 10 Nov 22:3x searched for the mode text and so never tested
  10 of the 13 names; the builders' scans (private tools) did. Stricter check for outside bundles and for added
  lines: `Prosjekter-u05/max/.venv/Scripts/python.exe -I max-private/tools/scan_tree.py <dir>` (needs PyYAML).
  Whole-tree scan_tree on the export and publish repos gives 668 / 311 hits from OLD content (a mask-map personal
  name not in identifiers.yaml, e.g. in a 30 Oct snapshot file) — raised with Stian 10 Nov, not yet decided.
- **The standard:** BS EN 12927:2019 at C:/Users/stian/max-private/standards/BS-EN_12927-2019.pdf (copyright: never
  in a repo). Beside it: Kai's ch.14 extract and the **clause map** (EN12927-2019_clause_map.md, 9 Nov: every clause
  that bears on the instrument, corrections to the extract, ambiguities). **B_rope / B_wire: decided 10 Nov — B_rope, B_wire shown beside it** (log 10 Nov 19:1x). The map's finding for that question: Annex B is
  informative and does not say whether B is local, over the metallic area or over the nominal area.
- **Open from U48 (Stian):** register l.348 says both "not on file" and "on file 9 Nov"; l.192 value column ("inner",
  "< 0.5 % LMA") does not match 14.3.5.2's wording; the extract lacks 14.2.1 (3-year flux check), 14.2.3 (≥ 1
  sample/mm), 14.3.3 (max 5 m/s), 14.1 (exclusions) — candidates for requirement rows in the register.
- **Decided 9 Nov:** landing page = the dense short page (index.html); easy read = easy.html, third button; full
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

# Kai — start here (handoff written 9 Nov 2026 02:5x, before a reboot)

Read in this order at the start of a session: this file, `todo.md`, the newest `log/*.md`, then
`C:/Users/stian/agent-notes/kai.md` (my briefs to builders; the last sections are the live units) and any new
builder notes in that folder (nautical names). Rules: `CLAUDE.md` here and the memory directory. Rule 10 in
`C:/Users/stian/Prosjekter-u05/max/CLAUDE.md` l.60–71 binds every brief and report.

## Where the work stands

- **Project repo** `C:/Users/stian/Prosjekter-u05/max`, branch main at **2e8ebf9**, pushed to the local origin
  (D:/git/prosjekter.git). GitHub fjordbit/max main is still **51c9bc1** (the cleaned export of 4 Nov); a plain
  push is refused (no common history). Owner: "push all", "no deletion" → incremental export, fast-forward (U38).
- **Units merged tonight:** U35 (3D appendix runs folded in), U36 (spec rev130: envelope remade; register rows;
  2D excursion table), U37 (identifier sweep of SWS files). Page rebuilt at d455e3d, then U37.
- **Running when the handoff was written** (both die on reboot; check before restarting):
  - **U38 export v3** — scratch folder `C:/Users/stian/export-v3/`; done when `REPORT.md` is there. If the folder
    is half-built and no report: delete the folder, restart the builder with the brief "## U38" in kai.md.
    When the report says persons and drawings = 0 and the tests pass: Kai runs the fast-forward push command from
    the report (never --force), then updates D:/git/max-export.git main from the clone.
  - **U39 short page** — worktree `C:/Users/stian/Prosjekter-u39`, branch u39-short-page; done when
    `tasks/reports/U39.md` is committed there. If the worktree exists without a committed report: check
    `git -C C:/Users/stian/Prosjekter-u39/max status`; a builder may resume from its notes, or start over.
    After it lands: verifier-U39, merge to main, rebuild page, then **the Pages refresh** (snapshot of
    docs/sws/index.html + short.html + sources through the publish pipeline in `C:/Users/stian/publish/SWS`,
    scan 0, push to fjordbit/SWS and MAx-Flow/SWS-Documentation; the site redeploys itself; see
    log/2026-10-29.md l.160–170 and log/2026-11-07.md l.326–340).
- **Backup:** full file copy `D:\backup\2026-11-09_0223\` (2.5 GB; holds identifiers.yaml and the transcript with
  the pasted API key — local disk only). All repos committed and on D:/git.

## Rulings from 8 Nov evening not yet fully in the record

- Envelope −40 / +50 °C for service, storage and transport (49 °C record day → 50); the magnets set the
  transport limit; magnets procured to "zero irreversible loss after a +50 °C excursion in the open-half state";
  no further FE runs until the supplier's data for one-piece radial arcs is on file. Recorded as "U36 addendum" in
  kai.md; register l.361 and rev130 l.233/367/428/429 still say "owner to set" → next spec unit (small, docx route).
- Owner's reading accepted by me: "ambient at the sensor" is the editor's reading (marked so in rev130).

## Waiting on Stian (also in todo.md)

Send the mail draft `inbox/drafts/2026-11-08_henrik_magnet-spec.md`; create the GitHub issue from
`inbox/drafts/2026-11-08_github-issue_magnet-spec.md` (gh CLI not installed; his login); Word master rev128–130;
register l.331/332 keep or retire; 52 mm wire diameters from the rope maker; R5 (Ø48 3D) yes/no; rotate the
API key (pasted in chat 8 Nov) after the next review round; the "other hardware" tier-0 pass (Fable + GPT 5.6
Sol via tools/review_round.py with the key loaded in-process) once he names the sections.

## How I am started

A fresh session knows only the files: CLAUDE.md, the memory directory, and what I read from here. Resuming the
previous session (`claude -c` in this folder) also restores the conversation transcript. Either way, this file is
the state; keep it current at every handoff and delete the "running" lines once the units are closed.

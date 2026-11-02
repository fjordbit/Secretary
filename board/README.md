# Dev board

A live page showing where the work stands. It uses plain names, not U numbers.

    cd C:/Users/stian/secretary
    python board/board.py          # then open http://127.0.0.1:8770/
    python board/board.py --json   # one-shot dump of the board state (for checking)

It uses only the Python standard library. It binds to 127.0.0.1 only and rejects other Host headers. It makes no outbound calls and never writes to the folders it watches. Git runs read-only with `GIT_OPTIONAL_LOCKS=0`. It never reads `max-private/`. The page loads nothing external. It re-reads every source on each load and again every 30 s. The process list is cached for 20 s. Set `BOARD_PORT` to change the port.

## Sources (read only)

- `agent-notes/*.md` – one file per session (the session name, dated `## ` entries and status lines). `kai.md` is read for the `U<n> brief` headings.
- Git in `Prosjekter` – worktrees, `u<n>-*` branches, each unit's last own commit (subject starts `U<n>`/`U0<n>`), ahead/behind `main`, and uncommitted files.
- `secretary/todo.md` – the `## Delivery milestones` table.
- `Prosjekter/max/tasks/TASKS.md` – "Depends on" for units that have not started.
- `secretary/log/*.md` – used only to tell whether Kai checked a commit (see below).
- Processes – one PowerShell call (Win32_Process plus listening ports) to find python processes running `max_core.cli studio` or pytest. The venv launcher and its child count as one process. The worktree comes from the Prosjekter path in the command line or the parent chain.

## Column rules

1. **Not started**: no notes entry, no own commit and no "accepted" mention.
2. **Merged**: there is an own commit and the branch is 0 ahead of `main`. It gets a **?** if the worktree has uncommitted tracked files, or if the latest status note (dated the same day as the tip or later) says work continues.
3. **Running now**: the latest status note is started / milestone / built / reopened / "qc running". It gets a **?** after 24 h with no note, no commit and no running process.
4. **Waiting on Stian**: the latest note is "waiting on Stian" / "ready for Stian", or the session wrote "next steps need Stian" and nothing restarted it later.
5. **Done (not merged)**: Kai has checked the tip commit, or the note says finished / "U<n> accepted".
6. **Ready for check**: the latest note says "Ready for Kai's check: yes", or "committed".

**Kai checked** means the tip hash appears in a notes line "Kai checked <hash>", or in a secretary log line that names the hash and says Kai ran it ("Kai: … pass", "re-ran", "checked") or "Republished".

Entries belong to the unit named on their `- Unit / branch:` line, or else to the unit of the file name. Units marked "accepted" on that line are recorded as accepted.

## Decisions waiting on Stian

These are read per notes file, in order:

- `Needs Stian:` and `Still open:` replace that unit's open list. "nothing" clears it.
- `Waiting on Stian:`, `Open for Stian`, `Still with Stian:` and "next steps need Stian:" add items.
- These lines close items that share a code token such as R2 or ADR, or that match the words of a closed item: "Closed with Stian: …", "Stian decided …", and lines that start with "Stian".
- Items are split on numbered sub-lines, `(1)` markers or `;`. Near-duplicates are merged by word overlap.
- An item dropped because a later list did not repeat it is not deleted. It goes under "earlier asks, may be settled".

Each item links to `/src/notes/<file>#L<line>`, a read-only line view of the source.

Files: `board.py` (server and parsing) and `index.html` (page, inline CSS and JS).

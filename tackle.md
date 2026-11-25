# tackle — U128 (prototype recording, Codex on a copy of the data): STOPPED at confinement

Main tip verified b5478a7 (from Prosjekter-u05). Worktree C:/Users/stian/Prosjekter-u128, branch
u128-prototype-data-codex made at b5478a7; NO commit (nothing to commit). Codex never run with a model: no
prompt, no data sent.

## The program
- No `codex` on PATH. The Codex desktop app carries the CLI: `C:\Program Files\WindowsApps\OpenAI.Codex_26.1120.5083.0_x64__2p2nqsd0c76g0\app\resources\codex.exe`,
  `codex-cli 0.171.0-alpha.13.2`, `codex login status` = "Logged in using ChatGPT" (same CODEX_HOME login the
  round tool's codex backend would use). auth.json not read.
- Model catalog (`codex debug models`): gpt-6.2-sol, gpt-6.2-astra, gpt-6.1-terra, gpt-6.1-sol, gpt-6-astra,
  gpt-6-sol, gpt-6-luna, gpt-5.6-sol/terra/luna (levels up to "ultra"), hidden gpt-reserve, codex-auto-review.
  NO model named "*-codex" is offered by this CLI; gpt-5.3-codex is not in the list (it was offered through
  Cursor in U125). Not tested whether -m gpt-5.3-codex would be accepted (that would mean a model call).

## Confinement: what this machine allows (probed with `codex sandbox`, harmless cmd script, no model)
Windows has two sandbox backends:
- unelevated (restricted token, runs as the user): works on the subst drive. Write outside the work folder:
  denied. Network: curl to a public page HTTP000 (same curl outside the sandbox: HTTP200). READ: unrestricted —
  it listed the user folder and read a file in agent-notes.
- elevated (separate account CodexSandboxOffline): write outside denied, network HTTP000, but it reads the
  user folder too (a file in agent-notes: read; .codex listing: 49 entries). And it CANNOT start on the subst
  drive: "CreateProcessWithLogonW failed: 267" (a subst drive exists only in the user's own logon session).
- A read-restricted permission profile (`:minimal` read + workspace write):
  unelevated -> "Restricted read-only access requires the elevated Windows sandbox backend";
  elevated -> "elevated Windows sandbox requires effective `:root` read access".
  The only read limit left is a deny-list (deny_read ACLs that Codex writes onto named folders of the user's
  own profile). Not tried: it changes ACLs on the owner's folders and is a deny-list, not "only inside".
- Codex's own prompt text says it: "The sandbox allows it read access everywhere, and write access in its
  writable root."
So: write and network confinement work; "read only inside the work folder" cannot be had, and the elevated
backend cannot be combined with subst. The brief says stop. The model could otherwise read the whole user
folder (projects, max-private, Codex's own login file) and send it to the provider.

## Left behind
- Work folder C:/Users/stian/prototype_data_round_2026-11-25/: data/ (copy, md5-identical to the original, 31
  files), pybase/ (copy of the base Python 3.12.10 without site-packages/Scripts/Doc, so no user path shows),
  venv/ (from pybase; numpy 2.5.5, scipy 1.18.1, pandas 3.1.1, matplotlib 3.11.2; pyvenv.cfg holds only R:\
  paths), probe/probe.cmd, out/ with two probe files (p1.txt, probe_inside.txt; delete blocked for me). No
  brief.md written (stopped before item 4). The elevated probe added ACL entries (CodexSandboxUsers: modify)
  on the work folder.
- subst R: removed (no mappings left).
- Outside the work folder: C:/Users/stian/.sbx-denybin/ (ssh/scp .bat/.cmd shims that just `exit /b 1`)
  created by the Codex sandbox at 12:42; Codex's own state in .codex updated. Nothing else from me.
- Headers re-verified: one variant per logger, as gunport found. notes.txt read (no personal, customer or site
  name; logger maker named).

## Options (I chose none)
 a) Run without subst on the real path with the elevated backend: write + network confined, reads not; model
    sees the user-folder path.
 b) Deny-list: :root read, workspace write, deny_read on the user profile's sensitive folders (Codex writes
    deny ACLs there). Needs the owner's yes; still not "only inside".
 c) Another machine / a separate Windows account holding only the work folder and its own Codex login.
 d) Model: decide whether "newest Codex" means gpt-5.3-codex (not offered by this CLI) or the newest model
    this CLI offers.

No background work running. — tackle

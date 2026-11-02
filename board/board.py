"""Live dev board for Stian: where the work stands, in plain names.

Run from C:/Users/stian/secretary:   python board/board.py
Then open http://127.0.0.1:8770/

Standard library only. Read-only on everything it watches: it runs read-only
git commands (with GIT_OPTIONAL_LOCKS=0 so git never refreshes an index) and one
PowerShell query for processes. It binds to 127.0.0.1 and makes no outbound calls.
"""
from __future__ import annotations

import html
import json
import os
import re
import subprocess
import sys
import threading
import time
from datetime import date, datetime, timedelta
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

HOST, PORT = "127.0.0.1", int(os.environ.get("BOARD_PORT", "8770"))
HERE = Path(__file__).resolve().parent
NOTES = Path("C:/Users/stian/agent-notes")
REPO = Path("C:/Users/stian/Prosjekter")
TODO = Path("C:/Users/stian/secretary/todo.md")
LOGDIR = Path("C:/Users/stian/secretary/log")
BLOCKED = Path("C:/Users/stian/max-private")  # never read

# Plain names, as Stian asked for them. Workstream: MAx (MAx/Studio), Twin, SWS, Logging.
UNITS = {
    0: ("Foundation", "MAx"), 1: ("Claude connector", "MAx"), 2: ("OpenAI reviewer", "MAx"),
    3: ("Rule engine", "MAx"), 4: ("Orchestrator", "MAx"), 5: ("Live view on real runs", "MAx"),
    6: ("Paper", "MAx"), 7: ("SWS 2D benchmark", "SWS"), 8: ("SWS 3D FEM", "SWS"),
    9: ("SWS hardware selection", "SWS"), 10: ("Twin & flow design", "Twin"),
    11: ("Hardware on 3D model", "SWS"), 12: ("Agents on subscriptions", "MAx"),
    13: ("Studio front end", "MAx"), 14: ("Shiplift 3D view + semantic zoom", "MAx"),
    15: ("Test model (first principles)", "Twin"),
}
COLUMNS = ["running", "waiting", "ready", "done", "merged", "notstarted"]

GIT_ENV = dict(os.environ, GIT_OPTIONAL_LOCKS="0", GIT_TERMINAL_PROMPT="0", LC_ALL="C")
NOWIN = 0x08000000 if sys.platform == "win32" else 0  # CREATE_NO_WINDOW


# ----------------------------------------------------------------------------- helpers
def run(cmd: list[str], cwd: Path | None = None, timeout: int = 15) -> str:
    try:
        p = subprocess.run(cmd, cwd=cwd, env=GIT_ENV, capture_output=True, timeout=timeout,
                           creationflags=NOWIN)
        return p.stdout.decode("utf-8", "replace")
    except Exception:
        return ""


def git(*args: str, cwd: Path = REPO) -> str:
    return run(["git", "-C", str(cwd), *args])


def read_text(p: Path) -> str:
    if BLOCKED in p.resolve().parents:
        return ""
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def iso(dt: datetime | None) -> str | None:
    return dt.isoformat(timespec="seconds") if dt else None


STOP = set("""a an the and or of to in on for with is are be by as at it its this that from
vs via per not no yes if into than then their there which who what when where whether how
any all one two get gets new now still only also own""".split())


def words(s: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9@.~]+", s.lower()) if w not in STOP and len(w) > 1}


def similar(a: str, b: str, th: float = 0.6) -> bool:
    A, B = words(a), words(b)
    if not A or not B:
        return False
    return len(A & B) / min(len(A), len(B)) >= th


# ----------------------------------------------------------------------------- git
def collect_git() -> dict:
    out: dict = {"worktrees": [], "branches": {}, "main": None, "merge_in_progress": []}
    wt, cur = [], {}
    for line in git("worktree", "list", "--porcelain").splitlines() + [""]:
        if not line.strip():
            if cur:
                wt.append(cur)
            cur = {}
            continue
        k, _, v = line.partition(" ")
        if k == "worktree":
            cur["path"] = v
        elif k == "HEAD":
            cur["head"] = v[:7]
        elif k == "branch":
            cur["branch"] = v.replace("refs/heads/", "")
    out["worktrees"] = wt
    wt_by_branch = {w.get("branch"): w["path"] for w in wt if w.get("branch")}

    m = git("log", "-1", "--format=%h%x09%cI%x09%s", "main").strip().split("\t")
    if len(m) == 3:
        out["main"] = {"hash": m[0], "date": m[1], "subject": m[2], "worktree": wt_by_branch.get("main")}
    for w in wt:  # a merge running in some worktree?
        mh = git("rev-parse", "--git-path", "MERGE_HEAD", cwd=Path(w["path"])).strip()
        if mh and (Path(w["path"]) / mh if not os.path.isabs(mh) else Path(mh)).exists():
            out["merge_in_progress"].append(w["path"])

    refs = git("for-each-ref", "refs/heads",
               "--format=%(refname:short)%09%(objectname:short)%09%(committerdate:iso-strict)%09%(subject)")
    for line in refs.splitlines():
        parts = line.split("\t")
        if len(parts) != 4:
            continue
        name, h, d, subj = parts
        mu = re.match(r"u(\d+)-", name)
        if not mu:
            continue
        n = int(mu.group(1))
        ab = git("rev-list", "--left-right", "--count", f"{name}...main").split()
        ahead, behind = (int(ab[0]), int(ab[1])) if len(ab) == 2 else (None, None)
        own = []
        for l2 in git("log", "-300", "--format=%h%x09%cI%x09%s", name).splitlines():
            hh, dd, ss = (l2.split("\t") + ["", ""])[:3]
            if re.match(rf"U0?{n}\b", ss):
                own.append({"hash": hh, "date": dd, "subject": ss})
        path = wt_by_branch.get(name)
        dirty_tracked = dirty_untracked = 0
        if path:
            for sl in git("status", "--porcelain", cwd=Path(path)).splitlines():
                if sl.startswith("??"):
                    if ".venv" not in sl:
                        dirty_untracked += 1
                elif sl.strip():
                    dirty_tracked += 1
        out["branches"][name] = {
            "unit": n, "name": name, "tip": h, "date": d, "subject": subj,
            "ahead": ahead, "behind": behind, "own": own, "worktree": path,
            "dirty_tracked": dirty_tracked, "dirty_untracked": dirty_untracked,
        }
    return out


def is_ancestor(h: str, ref: str = "main") -> bool:
    try:
        p = subprocess.run(["git", "-C", str(REPO), "merge-base", "--is-ancestor", h, ref],
                           env=GIT_ENV, capture_output=True, timeout=10, creationflags=NOWIN)
        return p.returncode == 0
    except Exception:
        return False


# ----------------------------------------------------------------------------- processes
PS = r"""
$p = Get-CimInstance Win32_Process | Select-Object ProcessId,ParentProcessId,Name,CommandLine,ExecutablePath
$l = Get-NetTCPConnection -State Listen -ErrorAction SilentlyContinue | Select-Object LocalPort,OwningProcess
@{p=@($p);l=@($l)} | ConvertTo-Json -Depth 3 -Compress
"""
_proc_cache: dict = {"t": 0.0, "v": []}


def collect_processes() -> list[dict]:
    if time.time() - _proc_cache["t"] < 20:
        return _proc_cache["v"]
    raw = run(["powershell", "-NoProfile", "-NonInteractive", "-Command", PS], timeout=25)
    try:
        data = json.loads(raw)
    except Exception:
        return _proc_cache["v"]
    procs = {p["ProcessId"]: p for p in data.get("p") or [] if p}
    ports: dict[int, list[int]] = {}
    for c in data.get("l") or []:
        if c:
            ports.setdefault(c["OwningProcess"], []).append(c["LocalPort"])

    def interesting(p):
        cl = p.get("CommandLine") or ""
        return "python" in (p.get("Name") or "").lower() and ("max_core" in cl or "pytest" in cl)

    def sig(p):  # the venv launcher and its base-interpreter child share the arguments
        cl = p.get("CommandLine") or ""
        m = re.search(r"\s-u?\s*-m\s+(.*)$|\s-m\s+(.*)$", cl)
        return (m.group(1) or m.group(2)).strip() if m else cl

    groups = []
    seen = set()
    for pid, p in procs.items():
        if not interesting(p) or pid in seen:
            continue
        par = procs.get(p.get("ParentProcessId"))
        if par and interesting(par) and sig(par) == sig(p):
            continue  # handled from the parent
        members = [p] + [c for c in procs.values() if c.get("ParentProcessId") == pid
                         and interesting(c) and sig(c) == sig(p)]
        seen.update(m["ProcessId"] for m in members)
        # worktree: first Prosjekter path in the group or its ancestors
        tree, chain, cur, hops = None, list(members), par, 0
        while cur and hops < 6:
            chain.append(cur)
            cur, hops = procs.get(cur.get("ParentProcessId")), hops + 1
        for q in chain:
            mm = re.search(r"([A-Za-z]:\\Users\\[^\\]+\\(Prosjekter[\w-]*))", (q.get("ExecutablePath") or "") + " " + (q.get("CommandLine") or ""))
            if mm:
                tree = mm.group(1).replace("\\", "/")
                break
        pp = sorted({pt for m in members for pt in ports.get(m["ProcessId"], [])})
        cl = sig(p)
        if not pp:
            ma = re.search(r"--port[ =](\d+)", cl)
            if ma and "studio" in cl:
                pp = [int(ma.group(1))]
        kind = "Studio" if "cli studio" in cl else ("tests (pytest)" if "pytest" in cl else cl.split()[0])
        groups.append({"kind": kind, "ports": pp, "worktree": tree, "pids": [m["ProcessId"] for m in members],
                       "cmd": cl[:160]})
    _proc_cache.update(t=time.time(), v=groups)
    return groups


# ----------------------------------------------------------------------------- notes
HEAD_RE = re.compile(r"^## (\d{4}-\d{2}-\d{2})([^—]*?)—\s*(.*)$")
UNIT_LINE = re.compile(r"^- Unit / branch:\s*(.*)", re.I)
HASH_RE = re.compile(r"\b[0-9a-f]{7}\b")


def session_name(text: str) -> str | None:
    for pat in (r"^Session name:\s*(\w+)", r"^# .*—\s*(\w+)\s*$", r"session is now named (\w+)"):
        m = re.search(pat, text, re.M | re.I)
        if m:
            return m.group(1)
    sig = re.findall(r"^— (\w+)\s*$", text, re.M)
    return sig[-1] if sig else None


def bullets(lines: list[tuple[int, str]]) -> list[dict]:
    """Join wrapped lines into bullets; numbered indented lines become sub-items."""
    out: list[dict] = []
    for ln, l in lines:
        if l.startswith("- "):
            out.append({"line": ln, "text": l[2:].strip(), "subs": []})
        elif re.match(r"^\s+\d+\.\s", l) and out:
            out[-1]["subs"].append({"line": ln, "text": re.sub(r"^\s+\d+\.\s*", "", l).strip()})
        elif l.startswith((" ", "\t")) and l.strip() and out:
            tgt = out[-1]["subs"][-1] if out[-1]["subs"] else out[-1]
            tgt["text"] += " " + l.strip()
        elif l.strip() and not l.startswith("—"):
            out.append({"line": ln, "text": l.strip(), "subs": []})
    return out


def parse_notes_file(p: Path) -> dict:
    text = read_text(p)
    lines = text.splitlines()
    mfile = re.match(r"u(\d+)", p.stem)
    unit = int(mfile.group(1)) if mfile else None
    entries, cur = [], None
    for i, l in enumerate(lines, 1):
        m = HEAD_RE.match(l)
        if m:
            cur = {"date": m.group(1), "when": m.group(2).strip(), "title": m.group(3).strip(),
                   "line": i, "lines": [], "unit": unit}
            entries.append(cur)
        elif cur is not None:
            cur["lines"].append((i, l))
    accepted: dict[int, dict] = {}
    for e in entries:
        for _, l in e["lines"]:
            mu = UNIT_LINE.match(l)
            if mu:
                spec = mu.group(1).split("/")[0]
                active = None
                for um in re.finditer(r"U0?(\d+)(\s+(accepted|done|finished))?", spec):
                    if um.group(2):
                        accepted[int(um.group(1))] = {"date": e["date"], "line": e["line"]}
                    elif active is None:
                        active = int(um.group(1))
                if active is not None:
                    unit = active
                    e["unit"] = active
                break
        else:
            e["unit"] = unit
        e["bullets"] = bullets(e["lines"])
        e["body"] = "\n".join(l for _, l in e["lines"])
        e["hashes"] = HASH_RE.findall(e["body"])
    st = p.stat()
    return {"file": p.name, "session": session_name(text), "entries": entries, "accepted": accepted,
            "mtime": datetime.fromtimestamp(st.st_mtime).astimezone()}


def entry_state(e: dict) -> str | None:
    t, b = e["title"].lower(), e["body"].lower()
    if re.fullmatch(r"(name|renamed)", t):
        return None
    if re.search(r"\bkai checked\b", b) or t.startswith("published"):
        return "checked"
    if "waiting on stian" in t or "ready for stian" in t or re.search(r"^- waiting on stian:", b, re.M):
        return "waiting"
    if re.search(r"ready for kai's check:\s*yes", b) or "ready for kai" in t or "waiting on kai" in t:
        return "ready"
    if re.search(r"\b(started|running|milestone|built|reopened|in progress)\b", t) or \
            re.search(r"\b(re-?qc running|qc running|qc-falsifier running|running now)\b", b):
        return "running"
    if "committed" in t:
        return "ready"
    if "finished" in t or "session stopped" in b:
        return "done"
    return None


def entry_time(e: dict, nf: dict, is_last: bool) -> datetime:
    d = datetime.fromisoformat(e["date"]).astimezone()
    tm = re.search(r"(\d{1,2}):(\d{2})", e["when"])
    if tm:
        d = d.replace(hour=int(tm.group(1)), minute=int(tm.group(2)))
    if is_last and nf["mtime"].date() >= d.date():
        return nf["mtime"]
    return d


NEXT_RE = re.compile(r"^(next(?: \([^)]*\))?|not done|plan|waiting on stian|needs stian|still open[^:]*|stopping here[^:;]*)\s*[:;,]?\s*(.*)", re.I)


def next_step(entries: list[dict]) -> dict | None:
    for e in reversed(entries):
        for b in e["bullets"]:
            for frag in [b["text"]] + re.split(r"(?<=\.)\s+", b["text"]):
                m = NEXT_RE.match(frag.strip())
                if m:
                    label = m.group(1).split(" (")[0].strip()
                    label = label[0].upper() + label[1:].replace("stian", "Stian")
                    rest = m.group(2).strip() or "; ".join(s["text"] for s in b["subs"])
                    if re.match(r"nothing", rest, re.I):
                        continue
                    if label.lower().startswith("stopping"):
                        label, rest = "Stopped", frag.strip()
                    return {"label": label, "text": rest[:220], "line": b["line"]}
    return None


# ----------------------------------------------------------------------------- decisions
REPLACE_RE = re.compile(r"^(needs stian|still open for stian[^:]*|still open)\s*:\s*(.*)", re.I)
ADD_RE = re.compile(r"^(waiting on stian|still with stian|open for stian[^:]*|decisions? for stian)\s*:\s*(.*)", re.I)
INLINE_ADD = re.compile(r"next steps? need stian:\s*(.*)", re.I)
CLOSE_LINE = re.compile(r"(closed with stian:\s*(.*))|(^stian\b)|(stian decided)|(\bstian:\s*[\"“])", re.I)
TOKEN_RE = re.compile(r"\b(?=[A-Z0-9]*\d|[A-Z]{2,})[A-Z0-9]{2,}\b")
GENERIC_TOK = {"QC", "OK", "AND", "OR"}


def split_items(text: str, subs: list[dict], line: int) -> list[dict]:
    text = text.strip().rstrip(".")
    if subs:
        return [{"text": s["text"].rstrip("."), "line": s["line"]} for s in subs]
    if re.search(r"\(\d\)", text):
        parts = re.split(r"\(\d\)\s*", text)
    else:
        parts = re.split(r";\s*", text)
    return [{"text": x.strip(" ;.,"), "line": line} for x in parts if len(x.strip(" ;.,")) > 3]


def decisions_for(nf: dict) -> tuple[list[dict], list[dict]]:
    open_items: list[dict] = []
    earlier: list[dict] = []
    for e in nf["entries"]:
        close_toks: set[str] = set()
        close_items: list[str] = []
        if re.search(r"stian decided|decided", e["title"], re.I):
            close_toks |= set(TOKEN_RE.findall(e["title"]))
        for b in e["bullets"]:
            mc = CLOSE_LINE.search(b["text"])
            if mc and not (REPLACE_RE.match(b["text"]) or ADD_RE.match(b["text"]) or INLINE_ADD.search(b["text"])):
                if mc.group(2):
                    close_items += re.split(r";\s*", mc.group(2).split("Still open")[0])
                else:
                    close_toks |= set(TOKEN_RE.findall(b["text"]))
        close_toks -= GENERIC_TOK
        close_toks = {t for t in close_toks if not re.fullmatch(r"U\d+", t)}

        def mk(it):
            return {"text": it["text"], "line": it["line"], "date": e["date"], "unit": e["unit"],
                    "file": nf["file"], "session": nf["session"]}

        for b in e["bullets"]:
            t = b["text"]
            # "Closed with Stian: x. Still open: y" lives on one bullet
            if "still open:" in t.lower() and not REPLACE_RE.match(t):
                t = t[t.lower().index("still open:"):]
            mr, ma, mi = REPLACE_RE.match(t), ADD_RE.match(t), INLINE_ADD.search(t)
            if mr:
                new = [] if re.match(r"nothing", mr.group(2), re.I) else \
                    [mk(i) for i in split_items(mr.group(2), b["subs"], b["line"])]
                earlier += [o for o in open_items if not any(similar(o["text"], n["text"]) for n in new)]
                open_items = [o for o in open_items if o["unit"] != e["unit"]] + new
            elif ma:
                open_items += [mk(i) for i in split_items(ma.group(2), b["subs"], b["line"])]
            elif mi:
                open_items += [mk(i) for i in split_items(mi.group(1), [], b["line"])]
        if close_toks or close_items:
            def closed(o):
                if set(TOKEN_RE.findall(o["text"])) & close_toks:
                    return True
                return any(similar(o["text"], c, 0.5) for c in close_items if c.strip())
            open_items = [o for o in open_items if not closed(o)]
            earlier = [o for o in earlier if not closed(o)]
    return open_items, earlier


def dedupe(items: list[dict]) -> list[dict]:
    out: list[dict] = []
    for it in sorted(items, key=lambda x: x["date"], reverse=True):
        for o in out:
            if similar(o["text"], it["text"]):
                o.setdefault("also", []).append({"file": it["file"], "line": it["line"], "date": it["date"]})
                break
        else:
            out.append(dict(it))
    return out


# ----------------------------------------------------------------------------- Kai's checks
def kai_checked_hashes(notes: list[dict]) -> dict[str, str]:
    """Hashes Kai has checked: 'Kai checked <hash>' in notes, or a secretary log line that names
    the hash and says Kai ran it ('Kai: N tests pass', 'Kai re-ran', 'checked') or republished it."""
    out: dict[str, str] = {}
    for nf in notes:
        for e in nf["entries"]:
            for m in re.finditer(r"kai checked ([0-9a-f]{7})", e["body"], re.I):
                out[m.group(1)] = f"notes/{nf['file']}#L{e['line']}"
    rx = re.compile(r"\bKai\b[^.;]*\b(pass(es)?|checked|re-ran)\b|Republished|PUBLISHED", re.I)
    for p in sorted(LOGDIR.glob("*.md")):
        for i, l in enumerate(read_text(p).splitlines(), 1):
            if rx.search(l):
                for h in HASH_RE.findall(l):
                    out.setdefault(h, f"log/{p.name}#L{i}")
    return out


def briefs() -> dict[int, dict]:
    out = {}
    for i, l in enumerate(read_text(NOTES / "kai.md").splitlines(), 1):
        m = re.match(r"^## (\d{4}-\d{2}-\d{2}).*?—\s*U(\d+) brief\s*\((.*)\)", l)
        if m:
            out[int(m.group(2))] = {"date": m.group(1), "title": m.group(3), "line": i}
    return out


def task_deps() -> dict[int, str]:
    out, cur = {}, None
    for l in read_text(REPO / "max/tasks/TASKS.md").splitlines():
        m = re.match(r"^### U(\d+)\b", l)
        if m:
            cur = int(m.group(1))
        elif cur is not None and l.startswith("- **Depends on:**"):
            out[cur] = re.sub(r"`", "", l.split("**Depends on:**", 1)[1]).strip()[:140]
    return out


# ----------------------------------------------------------------------------- milestones
MONTHS = {m: i for i, m in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split(), 1)}
FULLMONTH = {m: i for i, m in enumerate(["january", "february", "march", "april", "may", "june", "july",
                                          "august", "september", "october", "november", "december"], 1)}


def pick_year(mo: int, today: date) -> int:
    y = today.year
    return y + 1 if (date(y, mo, 1) - today).days < -180 else y


def milestones(today: date) -> list[dict]:
    text = read_text(TODO)
    sec = re.search(r"^## Delivery milestones.*?$(.*?)(?=^## |\Z)", text, re.M | re.S)
    out = []
    if not sec:
        return out
    for l in sec.group(1).splitlines():
        m = re.match(r"^\|\s*(M\d+)\s*\|(.*?)\|(.*?)\|(.*?)\|\s*$", l)
        if not m:
            continue
        tgt = m.group(4).strip()
        d, approx = None, None
        md = re.search(r"(\d{1,2})\s+([A-Za-z]{3})", tgt)
        if md and md.group(2).lower()[:3] in MONTHS:
            mo = MONTHS[md.group(2).lower()[:3]]
            d = date(pick_year(mo, today), mo, int(md.group(1)))
            approx = "week" if "week" in tgt.lower() else None
        else:
            for name, mo in FULLMONTH.items():
                if name in tgt.lower():
                    d, approx = date(pick_year(mo, today), mo, 1), "month"
        out.append({"id": m.group(1), "title": m.group(2).strip(), "done_when": m.group(3).strip(),
                    "target": tgt, "date": d.isoformat() if d else None, "approx": approx,
                    "days": (d - today).days if d else None,
                    "units": sorted({int(u) for u in re.findall(r"U(\d+)", m.group(3))})})
    return out


# ----------------------------------------------------------------------------- the board
def build_state() -> dict:
    now = datetime.now().astimezone()
    today = now.date()
    g = collect_git()
    procs = collect_processes()
    notes = [parse_notes_file(p) for p in sorted(NOTES.glob("*.md")) if p.name not in ("README.md", "kai.md")]
    checked = kai_checked_hashes(notes)
    br = briefs()
    deps = task_deps()
    branch_by_unit = {b["unit"]: b for b in g["branches"].values()}
    wt_unit = {b["worktree"].replace("\\", "/").lower(): b["unit"] for b in g["branches"].values() if b["worktree"]}

    for pr in procs:
        u = wt_unit.get((pr["worktree"] or "").lower())
        pr["unit"] = u
        pr["unit_name"] = UNITS[u][0] if u in UNITS else None
        pr["merge_worktree"] = bool(g["main"] and pr["worktree"] and g["main"].get("worktree")
                                    and pr["worktree"].lower() == g["main"]["worktree"].replace("\\", "/").lower())

    cards = []
    for n, (pname, ws) in UNITS.items():
        ents, sessions, files, acc = [], [], [], None
        for nf in notes:
            mine = [e for e in nf["entries"] if e["unit"] == n]
            for e in mine:
                e["_t"] = entry_time(e, nf, e is nf["entries"][-1])
                e["_file"] = nf["file"]
            if mine:
                ents += mine
                files.append(nf["file"])
                if nf["session"] and nf["session"] not in sessions:
                    sessions.append(nf["session"])
            if n in nf["accepted"]:
                acc = {**nf["accepted"][n], "file": nf["file"]}
                if nf["session"] and nf["session"] not in sessions:
                    sessions.append(nf["session"])
                if nf["file"] not in files:
                    files.append(nf["file"])
        ents.sort(key=lambda e: (e["date"], e["line"]))  # notes are append-only: file order is time order
        b = branch_by_unit.get(n)
        own = b["own"] if b else []
        state, state_entry = None, None
        for e in reversed(ents):
            s = entry_state(e)
            if s:
                state, state_entry = s, e
                break
        blocked = None
        for e in ents:
            if re.search(r"next steps? need stian", e["body"], re.I):
                blocked = e
            elif blocked and re.search(r"\b(started|reopened)\b", e["title"], re.I):
                blocked = None
        tip = b["tip"] if b else None
        tip_checked = checked.get(tip) if tip else None
        merged = bool(b and own and b["ahead"] == 0)
        last_commit = None
        if b and own:  # the unit's own last commit (the tip may be a shared commit, e.g. a rule change)
            lc = own[0]
            last_commit = {"hash": lc["hash"], "subject": lc["subject"], "date": lc["date"],
                           "ahead": b["ahead"], "behind": b["behind"], "branch": b["name"],
                           "tip": b["tip"]}
        times = [e["_t"] for e in ents]
        if last_commit:
            times.append(datetime.fromisoformat(last_commit["date"]))
        last_act = max(times) if times else None
        unit_procs = [p for p in procs if p["unit"] == n]

        q, why = False, []
        if not ents and not own and not acc:
            col = "notstarted"
        elif merged:
            col = "merged"
            if b["dirty_tracked"]:
                q = True
                why.append(f"{b['dirty_tracked']} uncommitted file(s) in {Path(b['worktree']).name}")
            if state in ("running", "waiting") and state_entry and \
                    state_entry["_t"].date() >= datetime.fromisoformat(b["date"]).date():
                q = True
                why.append(f"latest note says work continues: '{state_entry['title']}' ({state_entry['date']})")
        elif state == "running":
            col = "running"
            if last_act and (now - last_act) > timedelta(hours=24) and not unit_procs:
                q = True
                why.append(f"no note or commit for {int((now - last_act).total_seconds() // 3600)} h; may have stopped")
        elif state == "waiting" or blocked:
            col = "waiting"
            if blocked and state != "waiting":
                q = True
                why.append(f"last note is '{state_entry['title'] if state_entry else '?'}'"
                           + (" and Kai has checked it" if tip_checked else "")
                           + f"; but the session stopped for Stian's input on {blocked['date']} and nothing restarted it")
        elif tip_checked or state in ("checked", "done") or acc:
            col = "done"
        elif state == "ready":
            col = "ready"
        else:
            col, q = "ready", True
            why.append("no clear status line in the notes")

        nxt = next_step(ents) if ents else None
        if col == "notstarted":
            if n in br:
                nxt = {"label": "Brief ready", "text": f"Kai's brief of {br[n]['date']} ({br[n]['title']})"
                       + (f"; worktree {Path(b['worktree']).name} prepared" if b and b["worktree"] else ""),
                       "src": f"notes/kai.md#L{br[n]['line']}"}
            elif n in deps:
                nxt = {"label": "Depends on", "text": deps[n]}
        action = {
            "ready": f"Kai: check {tip}" if tip else "Kai: check",
            "done": "Stian: merge to main when ready",
            "waiting": "Stian: answer the open points below",
        }.get(col)
        if col == "done" and acc and not tip_checked:
            action = "Accepted; Stian: merge when ready"
        cards.append({
            "unit": n, "name": pname, "ws": ws, "sessions": sessions, "files": files,
            "column": col, "q": q, "why": why, "state": state,
            "state_src": f"notes/{state_entry['_file']}#L{state_entry['line']}" if state_entry else None,
            "last_activity": iso(last_act), "last_commit": last_commit,
            "checked_src": tip_checked, "accepted": acc, "next": nxt, "action": action,
            "dirty": {"tracked": b["dirty_tracked"], "untracked": b["dirty_untracked"]} if b else None,
            "worktree": Path(b["worktree"]).name if b and b["worktree"] else None,
            "procs": unit_procs,
        })

    # decisions
    open_all, earlier_all = [], []
    for nf in notes:
        o, e = decisions_for(nf)
        open_all += o
        earlier_all += e
    open_d = dedupe(open_all)
    def covered(e):  # restated (perhaps shortened) in an open item
        lead = " ".join([w for w in re.findall(r"[a-z0-9@.~-]+", e["text"].lower()) if w not in STOP][:2])
        return any(similar(e["text"], o["text"]) or (lead and lead in o["text"].lower()) for o in open_d)
    earlier_d = [e for e in dedupe(earlier_all) if not covered(e)]
    for d in open_d + earlier_d:
        d["unit_name"] = UNITS.get(d["unit"], ("?",))[0]

    return {
        "generated": iso(now), "today": today.isoformat(), "main": g["main"],
        "merge_in_progress": g["merge_in_progress"], "processes": procs,
        "milestones": milestones(today), "cards": cards, "columns": COLUMNS,
        "decisions": open_d, "decisions_earlier": earlier_d,
        "sources": {"notes": str(NOTES), "repo": str(REPO), "todo": str(TODO), "log": str(LOGDIR)},
    }


# ----------------------------------------------------------------------------- source viewer
def render_source(kind: str, name: str) -> bytes | None:
    if not re.fullmatch(r"[\w.-]+\.md", name):
        return None
    base = {"notes": NOTES, "log": LOGDIR}.get(kind)
    if not base:
        return None
    p = (base / name).resolve()
    if p.parent != base.resolve() or not p.is_file():
        return None
    rows = "".join(f'<tr id="L{i}"><td class="n"><a href="#L{i}">{i}</a></td><td>{html.escape(l)}</td></tr>'
                   for i, l in enumerate(read_text(p).splitlines(), 1))
    return f"""<!doctype html><meta charset="utf-8"><title>{html.escape(name)}</title>
<style>:root{{color-scheme:light dark;--bg:#fff;--fg:#1d2330;--mu:#7a8291;--hl:#fff3bf}}
@media (prefers-color-scheme:dark){{:root{{--bg:#14171d;--fg:#dfe3ea;--mu:#7f8796;--hl:#4a3f12}}}}
body{{background:var(--bg);color:var(--fg);font:13px/1.5 ui-monospace,Consolas,monospace;margin:0;padding:16px}}
h1{{font:600 15px system-ui,sans-serif}} table{{border-collapse:collapse}} td{{white-space:pre-wrap;vertical-align:top;padding:0 8px}}
td.n{{text-align:right;color:var(--mu);user-select:none}} td.n a{{color:inherit;text-decoration:none}}
tr:target{{background:var(--hl)}}</style>
<h1>{html.escape(str(p))} <small style="color:var(--mu)">(read-only view)</small></h1><table>{rows}</table>""".encode()


class Handler(BaseHTTPRequestHandler):
    server_version = "board/1"

    def log_message(self, fmt, *args):
        pass

    def send(self, code: int, body: bytes, ctype: str):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Security-Policy", "default-src 'self' 'unsafe-inline'; connect-src 'self'")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        host = (self.headers.get("Host") or "").split(":")[0]
        if host not in ("127.0.0.1", "localhost"):
            return self.send(403, b"local only", "text/plain")
        path = unquote(urlparse(self.path).path)
        try:
            if path in ("/", "/index.html"):
                return self.send(200, (HERE / "index.html").read_bytes(), "text/html; charset=utf-8")
            if path == "/api/state":
                return self.send(200, json.dumps(build_state(), default=str).encode(), "application/json")
            m = re.fullmatch(r"/src/(notes|log)/(.+)", path)
            if m:
                body = render_source(m.group(1), m.group(2))
                if body:
                    return self.send(200, body, "text/html; charset=utf-8")
            self.send(404, b"not found", "text/plain")
        except Exception as ex:  # keep the board up; show the error
            self.send(500, f"board error: {ex!r}".encode(), "text/plain")


def main():
    if "--json" in sys.argv:  # one-shot dump for checking
        print(json.dumps(build_state(), indent=1, default=str))
        return
    srv = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"Board on http://{HOST}:{PORT}/  (Ctrl+C to stop)")
    threading.Thread(target=collect_processes, daemon=True).start()  # warm the process cache
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()

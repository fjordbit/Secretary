"""Identifier scan of the added lines of a git range. Prints entry index and kind, never the name.
usage: python -I idscan.py <repo> <range>
"""
import re, subprocess, sys

YAML = r"C:/Users/stian/max-private/identifiers.yaml"


def entries():
    out, cur = [], None
    for line in open(YAML, encoding="utf-8").read().splitlines():
        m = re.match(r"^\s*(-\s*)?([A-Za-z_]+):\s*(.*)$", line)
        if not m:
            continue
        dash, key, val = m.groups()
        val = val.strip()
        if len(val) >= 2 and val[0] == val[-1] and val[0] in "'\"":
            q = val[0]
            val = val[1:-1]
            if q == '"':
                val = val.replace("\\\\", "\\")
            else:
                val = val.replace("''", "'")
        if dash or cur is None:
            cur = {}
            out.append(cur)
        cur[key] = val
    return [e for e in out if "name" in e]


def main():
    repo, rng = sys.argv[1], sys.argv[2]
    diff = subprocess.run(["git", "-C", repo, "diff", "-U0", "--text", rng],
                          capture_output=True).stdout.decode("utf-8", "replace")
    added = [l[1:] for l in diff.splitlines() if l.startswith("+") and not l.startswith("+++")]
    text = "\n".join(l for l in added if len(l) < 5000)   # skip embedded image data lines
    long_lines = sum(1 for l in added if len(l) >= 5000)
    ents = entries()
    total = 0
    for i, e in enumerate(ents):
        mode = (e.get("match") or "").split("#")[0].lower()
        pat = re.escape(e["name"])
        if "whole-word" in mode:
            pat = r"(?<![A-Za-z0-9_])" + pat + r"(?![A-Za-z0-9_])"
        rx = re.compile(pat, 0 if "exact case" in mode else re.I)
        n = len(rx.findall(text))
        if e.get("policy", "").lower().startswith("allow"):
            tag = " (policy: allowed)"
        else:
            tag = ""
            total += n
        if n:
            print(f"entry {i} kind={e.get('kind','?')} hits={n}{tag}")
    print(f"{len(ents)} entries, {len(added)} added lines ({long_lines} long data lines skipped), "
          f"hits counted: {total}")


main()

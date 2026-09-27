#!/usr/bin/env python3
"""Merge reader-agent reports (refs_reports/part_*.json) into refs_merged.json, dropping refs covered by whole-set fetches."""
import json, glob, sys, re
src, out = sys.argv[1], sys.argv[2]
COVERED = re.compile(r"github\.com/(aws/(agentcore-cli|bedrock-agentcore-sdk-python|bedrock-agentcore-sdk-typescript|bedrock-agentcore-starter-toolkit|agent-toolkit-for-aws|mcp-proxy-for-aws)|awslabs/(agentcore-samples|amazon-bedrock-agentcore-samples))|docs\.aws\.amazon\.com/cli/latest/reference/(bedrock-agentcore|agent-registry)")
refs = {}
for f in sorted(glob.glob(f"{src}/part_*.json")):
    for r in json.load(open(f))["refs"]:
        k = r["ref"].strip().rstrip(".,;)")
        e = refs.setdefault(k, {"cls": set(), "kind": r.get("kind"), "pages": set()})
        e["cls"].add(r["class"]); e["pages"].update(r.get("pages", []))
res = {}
for k, e in refs.items():
    c = "core" if "core" in e["cls"] else "related" if "related" in e["cls"] else "skip"
    if COVERED.search(k):
        c = "skip"
    res[k] = {"c": c, "kind": e["kind"], "pages": sorted(e["pages"])}
json.dump(res, open(out, "w"), indent=1)
print({c: sum(1 for v in res.values() if v["c"] == c) for c in ("core", "related", "skip")})

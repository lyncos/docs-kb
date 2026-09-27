#!/usr/bin/env python3
"""Fetch the external pages referenced by the AgentCore docs into ~/kb/agentcore/references/.

Input: refs_merged.json ({ref: {c: core|related|skip, kind, pages}}) produced from the reader-agent reports.
Each URL is saved as one Markdown page (with YAML frontmatter) — native .md when the site serves it,
otherwise HTML converted by pandoc, falling back to `tvly extract` for JS-rendered pages.
Whole reference sets (SDK/CLI repos, AWS CLI command reference, samples READMEs) are handled by fetch_ref_sets.sh.
"""
import json, os, re, subprocess, sys, hashlib
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

MERGED, OUT = sys.argv[1], sys.argv[2]
FETCHED = "2026-09-26"
SKIP_HOST = re.compile(r"(console\.aws\.amazon\.com|console\.(cloud|developers)\.google\.com|localhost|127\.0\.0\.1|example\.(com|org)|your-|\{|<|XXXX|amazonaws\.com/(runtimes|identities)|github\.com/.*/(blob|tree)/)")
UA = "Mozilla/5.0 (X11; Linux x86_64) docs-kb-fetcher"


def sh(cmd, inp=None, timeout=60):
    r = subprocess.run(cmd, input=inp, capture_output=True, timeout=timeout)
    return r.returncode, r.stdout


def get(url):
    code, body = sh(["curl", "-sL", "--max-time", "40", "-A", UA, "-w", "\n%{http_code} %{content_type}", url])
    text = body.decode("utf-8", "replace")
    head, _, tail = text.rpartition("\n")
    status, _, ctype = tail.partition(" ")
    return status, ctype, head


def to_md(url):
    base = url.split("#")[0]
    # 1. native markdown (AWS docs, Mintlify, many doc sites)
    cand = re.sub(r"\.html?$", ".md", base) if re.search(r"\.html?$", base) else base.rstrip("/") + ".md"
    status, ctype, body = get(cand)
    if status == "200" and "html" not in ctype and not body.lstrip().lower().startswith("<!doctype"):
        return body, "native-md"
    # 2. HTML -> pandoc (main content heuristics: <main> or <article> if present)
    status, ctype, body = get(base)
    if status == "200" and "html" in ctype:
        m = re.search(r"<(main|article)[^>]*>(.*)</\1>", body, re.S | re.I)
        html = m.group(2) if m else body
        html = re.sub(r"<(script|style|nav|header|footer|svg)[^>]*>.*?</\1>", "", html, flags=re.S | re.I)
        code, md = sh(["pandoc", "-f", "html", "-t", "gfm-raw_html", "--wrap=none"], html.encode())
        md = md.decode("utf-8", "replace").strip()
        if code == 0 and len(md) > 400:
            return md, "pandoc"
    elif status == "200" and ("text/plain" in ctype or "markdown" in ctype):
        return body, "raw"
    # 3. Tavily extract (JS-rendered pages)
    code, out = sh(["tvly", "extract", base, "--format", "markdown", "--json"], timeout=90)
    if code == 0:
        try:
            d = json.loads(out)
            res = (d.get("results") or [{}])[0]
            if res.get("raw_content") and len(res["raw_content"]) > 400:
                return res["raw_content"], "tavily"
        except Exception:
            pass
    return None, f"fail({status})"


def path_for(url):
    u = urlparse(url.split("#")[0])
    p = re.sub(r"\.(html?|md)$", "", u.path.strip("/")) or "index"
    p = re.sub(r"[^A-Za-z0-9._/-]", "_", p)
    if len(p) > 150:
        p = p[:140] + "-" + hashlib.sha1(p.encode()).hexdigest()[:8]
    return os.path.join(u.netloc, p + ".md")


def title_of(md, url):
    m = re.search(r"^#\s+(.+)$", md, re.M)
    return (m.group(1).strip() if m else urlparse(url).path.rsplit("/", 1)[-1] or url)[:200]


def work(item):
    url, meta = item
    dst = os.path.join(OUT, path_for(url))
    if os.path.exists(dst):
        return url, "cached"
    md, how = to_md(url)
    if md is None:
        return url, how
    fm = {
        "title": title_of(md, url),
        "product": "Amazon Bedrock AgentCore",
        "section": "References / " + ("core" if meta["c"] == "core" else "related"),
        "source_url": url,
        "fetched": FETCHED,
        "tags": ["agentcore", "reference", meta["c"]] + (["agent-registry"] if any("registry" in p for p in meta["pages"]) else []),
        "referenced_by": meta["pages"][:30],
        "conversion": how,
    }
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    import yaml
    with open(dst, "w", encoding="utf-8") as fh:
        fh.write("---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=10**6) + "---\n\n" + md.strip() + "\n")
    return url, how


def main():
    refs = json.load(open(MERGED))
    todo = {}
    for ref, meta in refs.items():
        if meta["c"] == "skip" or not ref.startswith("http") or SKIP_HOST.search(ref):
            continue
        todo[ref.split("#")[0].rstrip("/")] = meta
    print(f"{len(todo)} urls to fetch", flush=True)
    stats = {}
    fails = []
    with ThreadPoolExecutor(8) as ex:
        for url, how in ex.map(work, todo.items()):
            k = how.split("(")[0]
            stats[k] = stats.get(k, 0) + 1
            if k == "fail":
                fails.append(f"{how} {url}")
    print(stats)
    open(os.path.join(OUT, "_failed.txt"), "w").write("\n".join(sorted(fails)) + "\n")


main()

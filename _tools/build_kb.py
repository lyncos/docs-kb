#!/usr/bin/env python3
"""Build a frontmatter-annotated Markdown knowledge base from the scraped doc sets."""
import os, re, sys, shutil, yaml
from collections import defaultdict

SRC = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
FETCHED = "2026-09-26"

AWS = {
    "developer-guide": ("Developer Guide", "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide"),
    "api-control-plane": ("Control Plane API", "https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference"),
    "api-data-plane": ("Data Plane API", "https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference"),
    "agent-registry-api-control-plane": ("Agent Registry Control Plane API", "https://docs.aws.amazon.com/agent-registry-control/latest/APIReference"),
    "agent-registry-api-data-plane": ("Agent Registry Data Plane API", "https://docs.aws.amazon.com/agent-registry/latest/APIReference"),
}
PRODUCTS = {
    "agentcore": ("Amazon Bedrock AgentCore", "agentcore-docs"),
    "litellm": ("LiteLLM", "litellm-docs"),
    "coder": ("Coder", "coder-docs"),
    "tavily": ("Tavily", "tavily-docs"),
    "context7": ("Context7", "context7-docs"),
}
MINT_BOILER = re.compile(r"\A> ## Documentation Index\n(?:>.*\n)+\s*", re.M)
FM = re.compile(r"\A---\n(.*?)\n---\n?", re.S)


def split_fm(text):
    m = FM.match(text)
    if not m:
        return {}, text
    try:
        data = yaml.safe_load(m.group(1)) or {}
        if not isinstance(data, dict):
            data = {}
    except yaml.YAMLError:
        data = {}
    return data, text[m.end():]


def first_h1(body):
    cands = [m for m in (re.search(r"^#\s+(.+?)\s*$", body, re.M), re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S | re.I)) if m]
    if not cands:
        return None
    m = min(cands, key=lambda m: m.start())
    return re.sub(r"<[^>]+>", "", m.group(1)).strip() or None


def summary(body):
    # Mintlify: "> summary" right under H1; otherwise first prose paragraph.
    m = re.search(r"^#\s+.+\n+>\s*(.+)", body, re.M)
    if m and not m.group(1).startswith("#"):
        return m.group(1).strip()
    for para in re.split(r"\n\s*\n", body):
        p = para.strip()
        if p and not re.match(r"^(#|<|import |export |!\[|```|\||-|\*|>|:::)", p):
            p = re.sub(r"\s+", " ", re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", p))
            return p[:280]
    return None


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def source_url(product, rel, fm):
    if product == "agentcore":
        guide, name = rel.split("/", 1)
        if guide == "references":
            if fm.get("source_url"):
                return fm["source_url"]
            kind, rest = name.split("/", 1)
            if kind == "repos":
                repo, path = rest.split("/", 1)
                src = open(os.path.join(SRC, "agentcore-docs/references/repos", repo, ".source")).read().strip()
                slug, sha = src.split("@")
                return f"https://github.com/{slug}/blob/{sha}/{path}"
        return f"{AWS[guide][1]}/{name[:-3]}.html"
    if product == "litellm":
        top, rest = rel.split("/", 1)
        path = re.sub(r"\.mdx?$", "", rest)
        path = re.sub(r"(^|/)index$", "", path)
        if fm.get("slug"):
            s = str(fm["slug"])
            return "https://docs.litellm.ai" + (s if top == "docs" and s.startswith("/docs") else (f"/{top}" + s if s.startswith("/") else f"/{top}/{path.rsplit('/',1)[0]}/{s}"))
        return f"https://docs.litellm.ai/{top}/{path}".rstrip("/")
    if product == "coder":
        path = re.sub(r"(^|/)(README|index)\.md$", "", rel)
        return f"https://coder.com/docs/{re.sub(r'\.md$', '', path)}".rstrip("/")
    if product == "tavily":
        return f"https://docs.tavily.com/{rel[:-3]}"
    if product == "context7":
        return f"https://context7.com/{rel[:-3]}"


def section_of(product, rel):
    parts = rel.split("/")
    if product == "agentcore":
        guide = parts[0]
        if guide == "references":
            if parts[1] == "repos":
                return f"References / repo / {parts[2]}"
            if parts[1] == "aws-cli":
                return f"References / AWS CLI / {parts[2]}"
            return f"References / {parts[2]}"
        if guide == "developer-guide":
            stem = parts[1][:-3]
            return f"{AWS[guide][0]} / {stem.split('-')[0]}"
        return AWS[guide][0]
    if product == "litellm":
        return "/".join(parts[:2]) if len(parts) > 2 else parts[0]
    return parts[0] if len(parts) > 1 else "root"


def build():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    index = defaultdict(lambda: defaultdict(list))
    counts = {}
    for product, (pname, srcdir) in PRODUCTS.items():
        root = os.path.join(SRC, srcdir)
        n = 0
        for dp, _, files in os.walk(root):
            for f in sorted(files):
                if not re.search(r"\.mdx?$", f) or f == "README.md" and dp == root:
                    continue
                if f == "full.md":
                    continue  # whole-guide concatenations are shipped separately
                src = os.path.join(dp, f)
                rel = os.path.relpath(src, root).replace(os.sep, "/")
                text = open(src, encoding="utf-8", errors="replace").read()
                fm, body = split_fm(text)
                body = MINT_BOILER.sub("", body)
                title = fm.get("title") or first_h1(body) or fm.get("sidebar_label") or re.sub(r"\.mdx?$", "", f)
                sec = section_of(product, rel)
                meta = {
                    "title": str(title),
                    "description": fm.get("description") or summary(body),
                    "product": pname,
                    "section": sec,
                    "source_url": source_url(product, rel, fm),
                    "fetched": FETCHED,
                    "tags": sorted({product, slugify(sec.split(" / ")[-1]) or "root"}),
                }
                if rel.startswith("references/"):
                    meta["tags"] = sorted(set(meta["tags"]) | {"reference"} | set(fm.get("tags") or []))
                    for k in ("referenced_by", "conversion"):
                        if fm.get(k):
                            meta[k] = fm[k]
                if product == "agentcore" and (rel.startswith("agent-registry") or "registry" in rel.split("/")[-1]):
                    meta["tags"] = sorted(set(meta["tags"]) | {"agent-registry"})
                orig = {k: v for k, v in fm.items() if k not in meta and k not in ("fetched", "product", "section")}
                if orig:
                    meta["original_frontmatter"] = orig
                meta = {k: v for k, v in meta.items() if v not in (None, "")}
                out_rel = re.sub(r"\.mdx$", ".md", rel)
                dst = os.path.join(OUT, product, out_rel)
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                with open(dst, "w", encoding="utf-8") as fh:
                    fh.write("---\n" + yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=10**6) + "---\n\n" + body.lstrip())
                index[product][sec].append((meta["title"], out_rel))
                n += 1
        counts[product] = n
        # carry navigation / raw assets
        extras = os.path.join(OUT, product, "_source")
        os.makedirs(extras, exist_ok=True)
        for dp, _, files in os.walk(root):
            for f in files:
                if f in ("llms.txt", "llms-full.txt", "openapi.json", "manifest.json", "sidebars.js", "sidebars-release-notes.js", "full.md"):
                    rel = os.path.relpath(os.path.join(dp, f), root)
                    d = os.path.join(extras, rel)
                    os.makedirs(os.path.dirname(d), exist_ok=True)
                    shutil.copy(os.path.join(dp, f), d)
    for product, secs in index.items():
        pname = PRODUCTS[product][0]
        lines = ["---", f"title: {pname} — index", f"product: {pname}", "type: index", f"fetched: {FETCHED}", "---", "", f"# {pname}", "", f"{counts[product]} pages.", ""]
        for sec in sorted(secs):
            lines.append(f"## {sec}\n")
            for t, rel in sorted(secs[sec], key=lambda x: x[1]):
                lines.append(f"- [{t}]({rel})")
            lines.append("")
        open(os.path.join(OUT, product, "index.md"), "w", encoding="utf-8").write("\n".join(lines))
    readme = ["---", "title: Documentation knowledge base", "type: index", f"fetched: {FETCHED}", "---", "", "# Documentation knowledge base", "",
              "Every page carries YAML frontmatter: `title`, `description`, `product`, `section`, `source_url`, `fetched`, `tags` (plus `original_frontmatter` when the upstream page had its own).", "",
              "| Product | Pages | Index |", "|---|---|---|"]
    for product, (pname, _) in PRODUCTS.items():
        readme.append(f"| {pname} | {counts[product]} | [{product}/index.md]({product}/index.md) |")
    readme += ["", "Raw navigation files (llms.txt, manifest.json, sidebars.js, full-guide concatenations, OpenAPI) are under each product's `_source/`."]
    open(os.path.join(OUT, "README.md"), "w", encoding="utf-8").write("\n".join(readme) + "\n")
    print(counts)


build()

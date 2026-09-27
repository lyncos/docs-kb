
## Download

Latest snapshot as one zip (no login needed):

```bash
curl -LO https://github.com/lyncos/docs-kb/releases/latest/download/docs-kb.zip
curl -LO https://github.com/lyncos/docs-kb/releases/latest/download/docs-kb.zip.sha256
sha256sum -c docs-kb.zip.sha256
unzip docs-kb.zip -d ~        # creates ~/kb
```

Or `git clone https://github.com/lyncos/docs-kb.git ~/kb`.

PowerShell: `Invoke-WebRequest https://github.com/lyncos/docs-kb/releases/latest/download/docs-kb.zip -OutFile docs-kb.zip`, then compare `(Get-FileHash docs-kb.zip).Hash` with `docs-kb.zip.sha256`.

Hosts to allow on a restricted network: `github.com`, `objects.githubusercontent.com`, `release-assets.githubusercontent.com` (and `codeload.github.com` for clone/zip of the branch).

## Use with Claude Code

1. Put the KB at `~/kb`.
2. Add `"permissions": {"additionalDirectories": ["~/kb"]}` to `~/.claude/settings.json`.
3. Install the per-product skills: `python3 ~/kb/_tools/make_skills.py` (writes `~/.claude/skills/<product>-docs/`).
4. Optional read-only lookup subagent: `mkdir -p ~/.claude/agents && cp ~/kb/_tools/kb-researcher.md ~/.claude/agents/`.

## Layout

- `<product>/index.md` — all pages by section; pages keep the upstream path.
- `agentcore/references/` — material the AgentCore docs cite: `repos/` (official SDK/CLI/samples Markdown), `aws-cli/` (command reference), `pages/<host>/` (specs, AWS pages, framework docs). `referenced_by` lists the citing pages.
- `<product>/_source/` — upstream navigation files (llms.txt, manifest.json, sidebars.js, OpenAPI, full-guide concatenations).
- `_tools/` — fetch/build scripts and the reader-agent reference reports used to produce this snapshot.

See [NOTICE.md](NOTICE.md) for sources and licenses.

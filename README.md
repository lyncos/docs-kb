# docs-kb

Offline Markdown snapshot of public vendor documentation, packaged as a knowledge base for Claude Code and other coding agents.

| Product | Pages | Source |
|---|---|---|
| Amazon Bedrock AgentCore (+ AWS Agent Registry) | 1,592 + ~2,000 references | docs.aws.amazon.com (Developer Guide, Control/Data Plane APIs, Agent Registry APIs), AWS CLI reference, official GitHub repos and cited specs |
| LiteLLM | 1,102 | github.com/BerriAI/litellm-docs |
| Coder | 484 | github.com/coder/coder (docs/) |
| Tavily | 108 | docs.tavily.com |
| Context7 | 136 | context7.com/docs |

Every page has YAML frontmatter (`title`, `description`, `product`, `section`, `source_url`, `fetched`, `tags`) and each product has an `index.md`.

## Download

Latest release asset (no login needed):

```bash
curl -LO https://github.com/lyncos/docs-kb/releases/latest/download/docs-kb.zip
curl -LO https://github.com/lyncos/docs-kb/releases/latest/download/docs-kb.zip.sha256
sha256sum -c docs-kb.zip.sha256
unzip docs-kb.zip -d ~        # creates ~/kb
```

PowerShell:

```powershell
Invoke-WebRequest https://github.com/lyncos/docs-kb/releases/latest/download/docs-kb.zip -OutFile docs-kb.zip
(Get-FileHash docs-kb.zip -Algorithm SHA256).Hash   # compare with docs-kb.zip.sha256
```

Hosts to allow on a restricted network: `github.com`, `objects.githubusercontent.com`, `release-assets.githubusercontent.com`.

## Use with Claude Code

Unzip to `~/kb`, add `"permissions": {"additionalDirectories": ["~/kb"]}` to `~/.claude/settings.json`, and install the per-product skills with `python3 ~/kb/_tools/make_skills.py`. An optional read-only subagent is in `~/kb/_tools/kb-researcher.md` (copy it to `~/.claude/agents/`).

See [NOTICE.md](NOTICE.md) for sources and licenses.

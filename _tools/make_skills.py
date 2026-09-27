#!/usr/bin/env python3
"""Generate one Claude Code skill per KB product in ~/.claude/skills/<product>-docs/."""
import os
KB = os.path.expanduser("~/kb")
SK = os.path.expanduser("~/.claude/skills")
P = {
 "agentcore": ("Amazon Bedrock AgentCore",
  "Local offline docs for Amazon Bedrock AgentCore and AWS Agent Registry (Developer Guide, Control/Data Plane API, Agent Registry APIs). Use for any question about AgentCore Runtime, Gateway, Identity, Memory, Code Interpreter, Browser, Observability, Policy, Evaluations, Harness, Payments, Agent Registry, the agentcore CLI or bedrock-agentcore SDK, or AgentCore API operations and data types.",
  """- `developer-guide/` — concepts, how-tos. Filenames are prefixed by feature: `runtime-*`, `gateway-*`, `identity-*`, `memory-*`, `code-interpreter-*`, `browser-*`, `observability-*`, `policy-*`, `evaluations-*`, `harness-*`, `payments-*`, `registry-*` (Agent Registry), `agentcore-cli-reference`, `agentcore-python-sdk-reference`, `agentcore-typescript-sdk-reference`, `release-notes`, `bedrock-agentcore-limits` (quotas).
- `api-control-plane/` — `API_<Operation>.md` and data types (bedrock-agentcore-control).
- `api-data-plane/` — `API_<Operation>.md` (bedrock-agentcore: InvokeAgentRuntime, memory events, sessions…).
- `agent-registry-api-control-plane/`, `agent-registry-api-data-plane/` — Agent Registry APIs (CreateRegistry, SearchRegistryRecords…).
- `references/` — external material the AgentCore docs cite: `repos/` (Markdown from agentcore-cli, bedrock-agentcore-sdk-python/-typescript, bedrock-agentcore-starter-toolkit, agentcore-samples, mcp-proxy-for-aws, AgentCore MCP server, AgentCore parts of agent-toolkit-for-aws), `aws-cli/` (every `aws bedrock-agentcore[-control]` / `aws agent-registry[-control]` command), `pages/<host>/…` (specs and pages cited: MCP, A2A, OAuth RFCs, Cedar, IAM action/condition-key lists, managed policies, KMS, Strands, LangGraph…). Each has `source_url` and `referenced_by` (the AgentCore pages citing it).
- `_source/*/full.md` — each guide concatenated in one file (only for exhaustive grep)."""),
 "litellm": ("LiteLLM",
  "Local offline docs for LiteLLM (Python SDK and LiteLLM Proxy / AI Gateway). Use for LiteLLM config.yaml, model_list, providers, virtual keys, teams, budgets, routing/fallbacks, callbacks/observability, guardrails, MCP gateway, pass-through endpoints, caching, admin UI, release notes.",
  """- `docs/proxy/` — LiteLLM Proxy (config, keys, teams, budgets, auth, guardrails, deployment).
- `docs/providers/` — one page per provider (bedrock, anthropic, openai, vertex, ollama…).
- `docs/observability/`, `docs/pass_through/`, `docs/tutorials/`, `docs/completion/`, `docs/mcp*`, `docs/caching/`, `docs/secret_managers/`.
- `release_notes/`, `blog/`. Navigation: `_source/sidebars.js`."""),
 "coder": ("Coder",
  "Local offline docs for Coder (coder.com self-hosted cloud development environments). Use for Coder install/deploy, templates (Terraform), workspaces, provisioners, external auth, OIDC, RBAC, coder CLI commands, REST API, Coder AI (ai-coder, tasks, AI Bridge, agent boundaries).",
  """- `reference/cli/` — every `coder` CLI command; `reference/api/` — REST API.
- `admin/` — deployment, templates, users/groups, networking, security, monitoring, licensing.
- `ai-coder/` — Coder Tasks, AI Bridge, agent boundaries, MCP.
- `install/`, `user-guides/`, `tutorials/`, `start/`. Navigation: `_source/manifest.json`."""),
 "tavily": ("Tavily",
  "Local offline docs for Tavily (web search API for AI agents). Use for Tavily search/extract/crawl/map/research endpoints and parameters, API credits, Python/JS SDKs, Tavily MCP server, framework integrations (LangChain, LlamaIndex…), and examples.",
  """- `documentation/api-reference/` — endpoints (search, extract, crawl, map, research, usage).
- `documentation/` — quickstart, best practices, credits, rate limits, MCP, integrations.
- `sdk/` — Python and JavaScript SDK references. `examples/` — use cases.
- `_source/openapi.json` — OpenAPI spec; `_source/llms-full.txt` — whole site in one file."""),
 "context7": ("Context7",
  "Local offline docs for Context7 (Upstash's up-to-date library docs service for AI coding assistants). Use for Context7 MCP server install/config per client, API (search/docs endpoints), adding or claiming libraries, context7.json, private repos, plans/limits, CLI and skills.",
  """- `docs/` — everything: overview, installation per client, API reference, library management, plans."""),
}
TPL = """---
name: {p}-docs
description: {desc}
allowed-tools: Read, Grep, Glob
---

# {name} docs (local KB)

Snapshot of the official {name} documentation in Markdown at `~/kb/{p}/`. Prefer it over web search; each page's `source_url` frontmatter gives the live URL to cite. If the answer may have changed since the `fetched` date, say so.

## Layout
{layout}

## How to find things
1. Start from `~/kb/{p}/index.md` (all pages grouped by section, with titles) when you don't know the page.
2. Search frontmatter (cheap — one line per page):
   - by title: `rg -i '^title:.*<term>' ~/kb/{p} -g '*.md'`
   - by description: `rg -i '^description:.*<term>' ~/kb/{p} -g '*.md' -l`
   - by section/tag: `rg -l '^section: <section>' ~/kb/{p}`
3. Full-text: `rg -il '<term>' ~/kb/{p} -g '!_source'` then read only the best 1–3 pages.
4. Answer with the page's `source_url`. Don't read whole folders; if a lookup needs many pages, delegate to the `kb-researcher` agent.
"""
for p, (name, desc, layout) in P.items():
    d = os.path.join(SK, f"{p}-docs"); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "SKILL.md"), "w").write(TPL.format(p=p, name=name, desc=desc, layout=layout))
    print("wrote", d)

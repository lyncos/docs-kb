---
title: Long-term memory — framework examples
description: End-to-end agent examples that wire AgentCore **long-term memory** (strategies + `retrieve_memories`) into real agent frameworks. The section README covers the strategies, namespaces, and retrieval APIs; these folders show them inside working agents.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/01-features/04-manage-context-of-your-agent/memory/02-long-term-memory/examples/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# Long-term memory — framework examples

End-to-end agent examples that wire AgentCore **long-term memory** (strategies + `retrieve_memories`) into real agent frameworks. The [section README](../README.md) covers the strategies, namespaces, and retrieval APIs; these folders show them inside working agents.

| Folder | What's inside |
|---|---|
| [`single-agent/`](./single-agent/) | One agent per example — Claude SDK, Strands, LangGraph, LlamaIndex — across three integration patterns (built-in hook/callback, custom override, memory-as-tool) |
| [`multi-agent/`](./multi-agent/) | Multiple agents sharing one long-term memory resource (travel booking, healthcare) with per-agent namespaces |

## The three integration patterns

Every framework folder shows the same three ways to wire long-term memory into an agent:

1. **Built-in hook/callback** — the framework saves and recalls on its standard lifecycle.
2. **Custom hook/override** — you control extraction/consolidation models or storage logic.
3. **Memory as a tool** — the model decides when to store and recall via tool calls.

## Where to go next

- Long-term memory overview (strategies, namespaces, retrieval): [`../README.md`](../README.md)
- Short-term memory examples: [`../../01-short-term-memory/examples/`](../../01-short-term-memory/examples/)

---
title: Long-term memory — single-agent examples
description: One agent per example, each giving a single agent long-term memory backed by AgentCore. The folders differ by framework; within each, the same three integration patterns recur (built-in, custom, memory-as-tool).
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/01-features/04-manage-context-of-your-agent/memory/02-long-term-memory/examples/single-agent/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# Long-term memory — single-agent examples

One agent per example, each giving a single agent long-term memory backed by AgentCore. The folders differ by framework; within each, the same three integration patterns recur (built-in, custom, memory-as-tool).

| Framework | Folder | What it demonstrates |
|---|---|---|
| Anthropic Claude SDK (no framework) | [`with-claude-sdk/`](./with-claude-sdk/) | Built-in strategies, custom override, memory-as-tool, and episodic memory — all explicit |
| Strands Agents | [`with-strands-agent/`](./with-strands-agent/) | Built-in hook, custom hook (incl. self-managed strategy), and memory-tool patterns |
| LangGraph | [`with-langgraph-agent/`](./with-langgraph-agent/) | Built-in callback, custom callbacks (user-preference, episodic), and memory-as-tool |
| LlamaIndex | [`with-llamaindex-agent/`](./with-llamaindex-agent/) | Built-in memory block, custom memory block, and memory tool |

## Where to go next

- Multi-agent long-term examples: [`../multi-agent/`](../multi-agent/)
- Long-term memory overview: [`../../README.md`](../../README.md)

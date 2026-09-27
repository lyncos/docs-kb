---
title: Long-term memory — multi-agent examples
description: Multiple specialized agents collaborating through a single shared AgentCore long-term memory resource, each scoped to its own namespace so agents build persistent, non-colliding knowledge.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/01-features/04-manage-context-of-your-agent/memory/02-long-term-memory/examples/multi-agent/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# Long-term memory — multi-agent examples

Multiple specialized agents collaborating through a single shared AgentCore long-term memory resource, each scoped to its own namespace so agents build persistent, non-colliding knowledge.

| Framework | Folder | What it demonstrates |
|---|---|---|
| Anthropic Claude SDK (no framework) | [`with-claude-sdk/`](./with-claude-sdk/) | A research team sharing one memory resource, fully explicit |
| Strands Agents | [`with-strands-agent/`](./with-strands-agent/) | Travel-booking (built-in hook) and healthcare (custom hook, episodic) |
| LangGraph | [`with-langgraph-agent/`](./with-langgraph-agent/) | Shared-memory multi-agent via `create_agent` |
| LlamaIndex | [`with-llamaindex-agent/`](./with-llamaindex-agent/) | Shared-memory multi-agent via `FunctionAgent` |

## Where to go next

- Single-agent long-term examples: [`../single-agent/`](../single-agent/)
- Long-term memory overview: [`../../README.md`](../../README.md)

---
title: Short-term memory — multi-agent examples
description: Multiple specialized agents collaborating through a shared AgentCore short-term memory resource. Branching keeps each agent's conversation context isolated within one session.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/01-features/04-manage-context-of-your-agent/memory/01-short-term-memory/examples/multi-agent/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# Short-term memory — multi-agent examples

Multiple specialized agents collaborating through a shared AgentCore short-term memory resource. Branching keeps each agent's conversation context isolated within one session.

| Folder | What it demonstrates |
|---|---|
| [`with-strands-agent/`](./with-strands-agent/) | A travel-planning coordinator delegating to flight/hotel agents over a shared memory store; `multi-agent-parallel-branches/` gives each subagent its own branch for safe parallel execution |

## Where to go next

- Single-agent short-term examples: [`../single-agent/`](../single-agent/)
- Short-term memory primitives (incl. branching): [`../../README.md`](../../README.md)

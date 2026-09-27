---
title: Short-term memory — Strands multi-agent
description: 'A travel-planning system where a coordinator agent delegates to specialized **flight** and **hotel** booking assistants, all sharing one AgentCore short-term memory resource. Each specialist has its own `actor_id` but shares the `session_id`, so conversation context is preserved '
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/01-features/04-manage-context-of-your-agent/memory/01-short-term-memory/examples/multi-agent/with-strands-agent/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# Short-term memory — Strands multi-agent

A travel-planning system where a coordinator agent delegates to specialized **flight** and **hotel** booking assistants, all sharing one AgentCore short-term memory resource. Each specialist has its own `actor_id` but shares the `session_id`, so conversation context is preserved across agent transitions.

| Information | Details |
|---|---|
| Tutorial type | Short-term conversational (multi-agent) |
| Agent type | Travel Planning Assistant (coordinator + specialists) |
| Framework | Strands Agents |
| LLM model | Anthropic Claude Haiku 4.5 |
| Memory components | Shared short-term memory, lifecycle hooks, `get_last_k_turns` |
| Complexity | Beginner |

## What it does

- [`travel-planning-agent.py`](./travel-planning-agent.py) — specialized agents exposed as tools; a coordinator delegates flight/hotel queries while all agents read and write the shared memory store (via `MemoryClient`).
- [`travel-planning-agent-memory-manager.py`](./travel-planning-agent-memory-manager.py) — the same system using the newer **`MemoryManager`** / **`MemorySessionManager`** APIs.
- [`multi-agent-parallel-branches/`](./multi-agent-parallel-branches/) — branch-per-subagent for safe parallel execution.

## Prerequisites

- Python 3.10+
- AWS account with AgentCore Memory permissions (and an IAM role for memory)
- Access to Amazon Bedrock models

## How to run

```bash
pip install -r requirements.txt
python travel-planning-agent.py
```

See the [multi-agent index](../README.md) and the [short-term memory section README](../../../README.md) for context.

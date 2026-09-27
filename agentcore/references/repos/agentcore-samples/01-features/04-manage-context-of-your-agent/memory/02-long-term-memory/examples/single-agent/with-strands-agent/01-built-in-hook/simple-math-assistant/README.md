---
title: Long-term memory — Strands math assistant (Summary strategy)
description: A math tutor built with **Strands Agents** that stores **conversation summaries** as long-term memory via hooks. It demonstrates the Summary strategy alongside a calculator tool, conversation branching for alternative teaching paths, and event metadata for tracking student progre
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/01-features/04-manage-context-of-your-agent/memory/02-long-term-memory/examples/single-agent/with-strands-agent/01-built-in-hook/simple-math-assistant/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# Long-term memory — Strands math assistant (Summary strategy)

A math tutor built with **Strands Agents** that stores **conversation summaries** as long-term memory via hooks. It demonstrates the Summary strategy alongside a calculator tool, conversation branching for alternative teaching paths, and event metadata for tracking student progress.

| Information | Details |
|---|---|
| Tutorial type | Long-term conversational |
| Agent type | Math Assistant |
| Framework | Strands Agents |
| LLM model | Anthropic Claude Haiku 4.5 |
| Strategies | Summary |
| Memory components | Summary strategy, memory hooks, calculator tool, branching, event metadata |
| Complexity | Intermediate |

## What it does

[`math-assistant.py`](./math-assistant.py):

1. Creates memory with a Summary strategy; hooks store and retrieve summaries automatically.
2. Answers math questions using a calculator tool, informed by summarized history.
3. Uses branching to explore alternative difficulty levels and teaching approaches.
4. Tags events with metadata (difficulty, performance, learning milestones).

## Prerequisites

- Python 3.10+
- AWS credentials with AgentCore Memory permissions
- Amazon Bedrock AgentCore SDK

## How to run

```bash
pip install -r requirements.txt
python math-assistant.py
```

See the [Strands single-agent README](../../README.md) for the other long-term patterns.

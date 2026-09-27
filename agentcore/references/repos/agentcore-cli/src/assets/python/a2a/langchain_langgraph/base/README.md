---
title: '{{ name }}'
description: An A2A (Agent-to-Agent) agent deployed on Amazon Bedrock AgentCore using LangChain + LangGraph.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-cli
source_url: https://github.com/aws/agentcore-cli/blob/805f342/src/assets/python/a2a/langchain_langgraph/base/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-cli
- reference
---

# {{ name }}

An A2A (Agent-to-Agent) agent deployed on Amazon Bedrock AgentCore using LangChain + LangGraph.

## Overview

This agent implements the A2A protocol using LangGraph, enabling agent-to-agent communication.

## Local Development

```bash
uv sync
uv run python main.py
```

The agent starts on port 9000.

## Deploy

```bash
agentcore deploy
```

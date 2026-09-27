---
title: '{{ name }}'
description: An AG-UI agent deployed on Amazon Bedrock AgentCore using LangChain + LangGraph.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-cli
source_url: https://github.com/aws/agentcore-cli/blob/805f342/src/assets/python/agui/langchain_langgraph/base/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-cli
- reference
---

# {{ name }}

An AG-UI agent deployed on Amazon Bedrock AgentCore using LangChain + LangGraph.

## Overview

This agent implements the AG-UI protocol using LangGraph, enabling seamless frontend-to-agent communication with support for streaming, tool calls, and frontend-injected tools.

## Local Development

```bash
uv sync
uv run python main.py
```

The agent starts on port 8080.

## Deploy

```bash
agentcore deploy
```

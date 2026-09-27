---
title: '{{ name }}'
description: An A2A (Agent-to-Agent) agent deployed on Amazon Bedrock AgentCore using Strands SDK.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-cli
source_url: https://github.com/aws/agentcore-cli/blob/805f342/src/assets/python/a2a/strands/base/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-cli
- reference
---

# {{ name }}

An A2A (Agent-to-Agent) agent deployed on Amazon Bedrock AgentCore using Strands SDK.

## Overview

This agent implements the A2A protocol, enabling agent-to-agent communication. Other agents can discover and interact with this agent via the `/.well-known/agent-card.json` endpoint.

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

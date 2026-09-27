---
title: '{{ name }}'
description: An A2A (Agent-to-Agent) agent deployed on Amazon Bedrock AgentCore using Google ADK.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-cli
source_url: https://github.com/aws/agentcore-cli/blob/805f342/src/assets/python/a2a/googleadk/base/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-cli
- reference
---

# {{ name }}

An A2A (Agent-to-Agent) agent deployed on Amazon Bedrock AgentCore using Google ADK.

## Overview

This agent implements the A2A protocol using Google's Agent Development Kit, enabling agent-to-agent communication.

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

---
title: '{{ name }}'
description: An AG-UI agent deployed on Amazon Bedrock AgentCore using Strands SDK.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-cli
source_url: https://github.com/aws/agentcore-cli/blob/805f342/src/assets/python/agui/strands/base/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-cli
- reference
---

# {{ name }}

An AG-UI agent deployed on Amazon Bedrock AgentCore using Strands SDK.

## Overview

This agent implements the AG-UI protocol, enabling streaming agent-to-UI communication. The agent exposes an `/invocations` endpoint that accepts AG-UI protocol requests and streams responses back to the client.

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

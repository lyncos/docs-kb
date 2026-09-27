---
title: Add payments to an existing agent
description: Add AgentCore x402 payment capability to a Python agent you already have -- any framework (Strands, LangGraph, OpenAI Agents SDK, or other).
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/01-features/08-agents-that-transact/01-payments-skills-and-cli/add-to-existing-agent/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# Add payments to an existing agent

Add AgentCore x402 payment capability to a Python agent you already have -- any
framework (Strands, LangGraph, OpenAI Agents SDK, or other).

## Prerequisites

See the [parent README](../README.md) for environment setup and plugin installation.

## Prompt

Point your coding assistant at this folder and use:

> *"Add AgentCore x402 payment capability to my agent at `<path/to/agent>`."*

The assistant reads [`../AGENTS.md`](../AGENTS.md), loads the `aws-agents` payments
skill, and drives the entire process. It will pause only for your provider
credentials and wallet funding.

## What happens

The skill (via the assistant) will:

1. Verify your CLI, credentials, and region
2. Create the payment manager and connector (you enter credentials manually)
3. Deploy payment resources to AWS
4. Wire payments into your agent (native plugin for Strands/LangGraph, or generic
   tool for other frameworks)
5. Provision a per-user wallet and budget
6. Ask you to authorize and fund the wallet
7. Run a test fetch to confirm everything works

## Verify

```
Fetch https://sandbox.node4all.com/v1/x402-test and tell me what you find.
```

Expect `402` -> payment -> `200 OK`. Cleanup and debugging: see the
[parent README](../README.md#cleanup) and [`../AGENTS.md`](../AGENTS.md).

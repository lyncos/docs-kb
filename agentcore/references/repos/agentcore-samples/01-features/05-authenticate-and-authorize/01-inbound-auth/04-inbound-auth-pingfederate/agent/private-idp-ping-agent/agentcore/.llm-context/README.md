---
title: LLM Context Files
description: When editing schema JSON files, reference the corresponding `.ts` file here for type definitions and validation constraints (marked with `@regex`, `@min`, `@max`).
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/01-features/05-authenticate-and-authorize/01-inbound-auth/04-inbound-auth-pingfederate/agent/private-idp-ping-agent/agentcore/.llm-context/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# LLM Context Files

**DO NOT EDIT THESE FILES** - They are read-only reference for AI coding assistants.

## Files

| File             | JSON Config        | Purpose                                   |
| ---------------- | ------------------ | ----------------------------------------- |
| `agentcore.ts`   | `agentcore.json`   | Project, agent, memory, credential config |
| `mcp.ts`         | `agentcore.json`   | Gateways, targets, MCP runtime tools      |
| `aws-targets.ts` | `aws-targets.json` | Deployment targets (account + region)     |

## Usage

When editing schema JSON files, reference the corresponding `.ts` file here for type definitions and validation
constraints (marked with `@regex`, `@min`, `@max`).

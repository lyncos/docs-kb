---
title: LLM Context Files
description: When editing AgentCore JSON config files, reference the corresponding `.ts` file here for type definitions, exact enum values, defaults, and validation constraints (marked with `@regex`, `@min`, and `@max`). Run `agentcore validate` after making changes.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-cli
source_url: https://github.com/aws/agentcore-cli/blob/805f342/src/schema/llm-compacted/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-cli
- reference
---

# LLM Context Files

**DO NOT EDIT THESE FILES** - They are read-only reference for AI coding assistants.

## Files

| File             | JSON Config        | Purpose                               |
| ---------------- | ------------------ | ------------------------------------- |
| `agentcore.ts`   | `agentcore.json`   | Project resources, including gateways |
| `aws-targets.ts` | `aws-targets.json` | Deployment targets (account + region) |

## Usage

When editing AgentCore JSON config files, reference the corresponding `.ts` file here for type definitions, exact enum
values, defaults, and validation constraints (marked with `@regex`, `@min`, and `@max`). Run `agentcore validate` after
making changes.

---
title: Coding Agents on AgentCore Runtime
description: Examples of deploying coding agents on Amazon Bedrock AgentCore Runtime with persistent storage and MCP tool access.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/01-features/02-host-your-agent/01-runtime/04-coding-agents/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# Coding Agents on AgentCore Runtime

Examples of deploying coding agents on Amazon Bedrock AgentCore Runtime with persistent storage and MCP tool access.

| Sample | Description |
|--------|-------------|
| [01-claude-code-with-s3-files](./01-claude-code-with-s3-files) | Claude Code with S3 Files for shared persistent storage |
| [02-claude-code-with-efs](./02-claude-code-with-efs) | Claude Code with EFS for POSIX-compatible file system access |
| [03-code-agents-competition-e2e](./03-code-agents-competition-e2e) | End-to-end deployment of 6 coding agents (Claude Code, Kiro, Codex, Cursor, Hermes, OpenCode) with a shared GitHub MCP Gateway, side-by-side comparison frontend, and Token Vault integration |
| [04-claude-managed-agents-self-hosted-sandbox](./04-claude-managed-agents-self-hosted-sandbox) | Anthropic Claude Managed Agents (CMA) self-hosted sandbox on AgentCore Runtime |
| [05-autonomous-coding-agent-durable](./05-autonomous-coding-agent-durable) | Event-driven autonomous coding agent with durable orchestration, evaluator agent, Cedar sandbox policies, and cross-ticket memory |
| [06-codex-with-efs](./06-codex-with-efs) | OpenAI Codex SDK running against Bedrock-served GPT-5.6 models, with EFS holding `CODEX_HOME` so Codex threads are resumable across sessions |

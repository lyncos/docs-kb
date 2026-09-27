---
title: 'ADR-0008: SEMANTIC + SUMMARIZATION Memory'
description: 'AgentCore Memory supports multiple strategies: SEMANTIC retrieval, SUMMARIZATION, or both.'
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/02-use-cases/02-workflow-automation-agents/event-driven-claims-agent/docs/decisions/0008-semantic-summarization-memory.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# ADR-0008: SEMANTIC + SUMMARIZATION Memory

**Status:** Accepted  
**Date:** 2025-06-17

## Context

AgentCore Memory supports multiple strategies: SEMANTIC retrieval, SUMMARIZATION, or both.

## Decision

Enable both `SEMANTIC` and `SUMMARIZATION` built-in memory strategies.

## Reasoning

`SEMANTIC` retrieval allows the agent to recall facts about repeat claimants (prior claims, policy history patterns) across sessions. `SUMMARIZATION` compresses session history so the context window doesn't overflow for multi-turn interactions. Together they provide the cross-invocation recall needed for realistic claims processing.

## Alternatives Considered

Using only SEMANTIC or only SUMMARIZATION would limit either cross-session recall or long-conversation handling.

## Consequences

Memory adds latency (retrieval on each invocation). The 90-day expiration prevents unbounded growth. Memory is gracefully bypassed if not deployed (wrapped in try/except), so local dev works without memory.

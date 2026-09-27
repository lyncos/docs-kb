---
title: 'ADR-0002: Dual-Agent Over Single-Agent'
description: Claims processing requires both evaluation (is this claim valid?) and validation (is our evaluation correct?). A single agent could perform both roles, but may exhibit confirmation bias.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/02-use-cases/02-workflow-automation-agents/event-driven-claims-agent/docs/decisions/0002-dual-agent-over-single-agent.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# ADR-0002: Dual-Agent Over Single-Agent

**Status:** Accepted  
**Date:** 2025-06-17

## Context

Claims processing requires both evaluation (is this claim valid?) and validation (is our evaluation correct?). A single agent could perform both roles, but may exhibit confirmation bias.

## Decision

Use two sequential Strands `Agent` instances (Claims Processor → Validation Agent) rather than a single agent.

## Reasoning

A single agent asked to both evaluate a claim and validate its own evaluation exhibits confirmation bias — it rarely overrides its first decision. The Validation Agent is intentionally isolated from the Processor's reasoning process until it receives the full output, acting as an independent reviewer. This produces more accurate confidence scores and better human-review routing for edge cases (vague claims, high amounts, category mismatches).

## Alternatives Considered

A single agent with a two-phase prompt shows poor self-correction — the agent consistently validates its own decisions even when they are incorrect.

## Consequences

Two LLM calls per claim instead of one. Adds ~10-15 seconds to processing time. Sequential design (not parallel) simplifies the code — no shared state needed between agents.

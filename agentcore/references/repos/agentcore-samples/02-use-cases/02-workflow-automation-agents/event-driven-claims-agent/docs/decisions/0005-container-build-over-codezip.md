---
title: 'ADR-0005: Container Build Over CodeZip'
description: 'AgentCore Runtime supports two deployment modes: Container (Docker) or CodeZip (bundled Python code).'
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/02-use-cases/02-workflow-automation-agents/event-driven-claims-agent/docs/decisions/0005-container-build-over-codezip.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# ADR-0005: Container Build Over CodeZip

**Status:** Accepted  
**Date:** 2025-06-17

## Context

AgentCore Runtime supports two deployment modes: Container (Docker) or CodeZip (bundled Python code).

## Decision

The Runtime uses `Container` (Docker) build, not `CodeZip`.

## Reasoning

AgentCore Runtime supports both modes so you can pick the best fit per workload. This dual-agent pipeline makes two sequential LLM calls (each up to ~30-60s) and benefits from Container's generous memory headroom and a fully reproducible, pinned runtime image (ARM64/Graviton) that matches the deployed environment exactly.

## Alternatives Considered

**CodeZip** is a great fit for lightweight, fast-iterating agents — it skips the image build for the quickest path to deploy. Container is the better match here precisely because this sample leans on a longer, multi-step pipeline and a controlled dependency set.

## Consequences

The trade for that control is a container build + ECR push on deploy (Docker or Finch required). During local iteration, `agentcore dev` runs the agent directly for a fast inner loop.

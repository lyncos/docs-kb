---
title: 'ADR-0014: Cognito Client Secret via CDK Injection'
description: The agent authenticates to the Gateway with a Cognito M2M client (ADR-0004), which has a client secret. The Runtime needs that secret at runtime to mint tokens. Where does it come from? (Carries the claims sample's ADR-0010.)
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/02-use-cases/02-workflow-automation-agents/receipts-intelligent-document-processing-agent/docs/decisions/0014-cognito-secret-via-cdk-injection.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# ADR-0014: Cognito Client Secret via CDK Injection

**Status:** Accepted
**Date:** 2026-06-24

## Context

The agent authenticates to the Gateway with a Cognito M2M client ([ADR-0004](0004-agent-as-principal-m2m-over-per-user-jwt.md)), which has a client secret. The Runtime needs that secret at runtime to mint tokens. Where does it come from? (Carries the claims sample's ADR-0010.)

## Decision

The CDK reads the generated Cognito client secret and injects it into the Runtime as an environment variable (via the config seam — `app/receiptsagent/config.py`). It is not read from Secrets Manager at runtime.

## Reasoning

This keeps the sample focused on AgentCore mechanics rather than secret-management plumbing. The secret never appears in source — CDK resolves it from the Cognito resource at synth time and sets it as Runtime env. The seam means the agent only ever reads env vars, so swapping the *source* of the secret (to Secrets Manager) changes deployment wiring, not agent code.

## Alternatives Considered

- **Secrets Manager + runtime fetch:** the production-correct choice (rotation, audit, no secret in env). Deliberately deferred to keep the sample's surface area on AgentCore; the seam makes it a drop-in change later.
- **A long-lived static credential:** worse on every axis; rejected.

## Consequences

The client secret is present in the Runtime's environment configuration. Acceptable for a sample in a dev account; **a production deployment should read it from Secrets Manager**. Because the agent reads only env (the seam), that swap touches `cdk-stack.ts` and `config.py`'s source, not the agent logic. (`unsafeUnwrap()` on the CDK secret value is the explicit "yes, I'm inlining this in the sample" marker.)

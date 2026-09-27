---
title: AWS Lambda (standard) — Service Card
description: Event-driven functions, scale to zero, cheapest for short stateless tasks.
product: Amazon Bedrock AgentCore
section: References / repo / agent-toolkit-for-aws
source_url: https://github.com/aws/agent-toolkit-for-aws/blob/dda6148/plugins/aws-startup-advisor/skills/agent-advisor/references/decision-refs/lambda.md
fetched: '2026-09-26'
tags:
- agent-toolkit-for-aws
- agentcore
- reference
---

# AWS Lambda (standard) — Service Card

## One-liner

Event-driven functions, scale to zero, cheapest for short stateless tasks.

## Best for

Seconds-long, stateless, event-driven agent tasks (single tool call, classification).

## Hard limits

- Execution timeout: 15 minutes (eliminates it for minutes-to-hours sessions)

## Six dimensions

- Identity: IAM
- Observability: CloudWatch
- Guardrails: bring-your-own + Bedrock Guardrails
- Scaling: automatic, scale to zero
- Tool/Gateway: AgentCore services available as add-ons
- Protocols: invoke / function URL

## Tradeoffs

15-minute hard cap; no long sessions, no cross-session memory without external state.
Hands off to the source-platform migration skill (`gcp-to-aws` or `heroku-to-aws`) for compute-layer config.

## Serving & security notes

Entry: handler function invoked via invoke API or function URL; event-source wiring as needed. IAM: execution role with `bedrock:InvokeModel` (model-bearing units only — a model-less unit omits it) + service-specific permissions. Networking: public service endpoints over TLS; VPC endpoints only if policy demands.

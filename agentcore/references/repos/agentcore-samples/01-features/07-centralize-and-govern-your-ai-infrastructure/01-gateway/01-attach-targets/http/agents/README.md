---
title: Agent Targets
description: Attach agents to the gateway as HTTP targets, either hosted on AgentCore Runtime or fronted as third-party HTTP endpoints.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/01-features/07-centralize-and-govern-your-ai-infrastructure/01-gateway/01-attach-targets/http/agents/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# Agent Targets

Attach agents to the gateway as HTTP targets, either hosted on AgentCore Runtime or fronted as third-party HTTP endpoints.

![arch](./images/agents.png)

An agent target lets the gateway front an agent so you can apply inbound authorization (Microsoft Entra ID) and outbound credential injection (OBO token exchange, Databricks service-principal OAuth, or header propagation) without changing the agent. Two protocol families are covered:

- **A2A agents** speak the Agent-to-Agent JSON-RPC protocol: a client fetches the agent card, then sends work with `message/send`.
- **Generic HTTP agents** expose a plain HTTP contract (for example the AgentCore Runtime HTTP entrypoint, or a Claude Managed Agents REST API).

Either way the gateway routes by path: `{GATEWAY_URL}/{targetName}/{path}` reaches the agent's endpoint.

## Tutorials

| Section                       | Description                                                       |
| :---------------------------- | :---------------------------------------------------------------- |
| [a2a-agents](a2a-agents/)     | Attach Agent-to-Agent (A2A) protocol agents (on AgentCore Runtime or Databricks Apps) as HTTP targets |
| [http-agents](http-agents/)   | Attach generic HTTP agents (an AgentCore Runtime agent, or Claude Managed Agents) as HTTP targets |

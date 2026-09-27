---
title: MCP Server Target with Token Exchange Auth
description: '[!NOTE]'
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/01-features/07-centralize-and-govern-your-ai-infrastructure/01-gateway/01-attach-targets/mcp/mcp-servers/01-configure-auth/token-exchange/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# MCP Server Target with Token Exchange Auth

> [!NOTE]
> This tutorial is coming soon.

Attach a pre-existing MCP server to AgentCore gateway using OAuth 2.0 token exchange for outbound authentication. The gateway exchanges the inbound user token for a downstream service token, enabling user-scoped access to MCP server resources without exposing user credentials.

![architecture](./images/architecture.png)

## What you will learn

- Configure a gateway with token exchange outbound auth
- Set up a credential provider with `TOKEN_EXCHANGE` grant type
- Connect a Strands agent that accesses user-scoped resources through the gateway

## Documentation

- [AgentCore gateway Developer Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [gateway Outbound Auth](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-outbound-auth.html)
- [OBO Token Exchange](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/on-behalf-of-token-exchange.html)

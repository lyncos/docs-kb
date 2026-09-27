---
title: HTTP Targets
description: For HTTP targets, the gateway sends traffic directly to the target without aggregation or protocol translation. Unlike MCP targets, HTTP targets do not support capability synchronization or semantic tool search. Clients address each target individually through path-based routing.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/01-features/07-centralize-and-govern-your-ai-infrastructure/01-gateway/01-attach-targets/http/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# HTTP Targets

For HTTP targets, the gateway sends traffic directly to the target without aggregation or protocol translation. Unlike MCP targets, HTTP targets do not support capability synchronization or semantic tool search. Clients address each target individually through path-based routing.

![http](./images/agents.png)

![architecture](../../images/proxy.png)

You can attach different AgentCore identity Credential Providers to each HTTP target to securely manage outbound authentication on a per-target basis. You can also configure Token passthrough, in which gateway validates the inbound token and passes it through to the runtime target without modification. This is useful when the runtime handles its own authorization.

## Tutorials

| Section                       | Description                                                                |
| :---------------------------- | :------------------------------------------------------------------------- |
| [agents](agents/)             | Attach A2A and HTTP agents (on AgentCore runtime or third-party) as targets |
| [mcp-servers](mcp-servers/)   | Attach MCP servers (on AgentCore runtime or public) as HTTP targets         |

## Documentation

- [AgentCore gateway Developer Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [HTTP targets](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-targets-http.html)

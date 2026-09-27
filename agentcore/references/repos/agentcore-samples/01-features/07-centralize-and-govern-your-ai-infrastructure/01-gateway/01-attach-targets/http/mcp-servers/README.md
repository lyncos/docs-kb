---
title: MCP Server HTTP Targets
description: Attach MCP servers to the gateway as HTTP targets, addressed directly through path-based routing.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/01-features/07-centralize-and-govern-your-ai-infrastructure/01-gateway/01-attach-targets/http/mcp-servers/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# MCP Server HTTP Targets

Attach MCP servers to the gateway as HTTP targets, addressed directly through path-based routing.

![arch](./images/architecture.png)

These labs attach MCP servers as `http.passthrough` targets (`protocolType=MCP`): the gateway forwards each request to the MCP server's endpoint at `{GATEWAY_URL}/{targetName}/{path}` and passes the response back. Unlike the aggregated MCP targets (Lambda, OpenAPI, Smithy) under [`mcp/`](../../mcp/), an HTTP passthrough target does not aggregate tools or run capability synchronization or semantic tool search; the client speaks MCP straight through to one server. Because the gateway is a transparent proxy, MCP streamable-http rules still apply end to end: the client runs the `initialize` then `notifications/initialized` handshake, and the gateway target must allowlist the `Mcp-Session-Id` and `Content-Type` headers so the session id and SSE stream survive the round trip.

## Tutorials

| Section                                 | Description                                                  |
| :-------------------------------------- | :----------------------------------------------------------- |
| [agentcore-runtime](agentcore-runtime/) | MCP server hosted on AgentCore Runtime, fronted via `http.passthrough` with Entra ID `CUSTOM_JWT` on the runtime and `JWT_PASSTHROUGH` outbound |
| [context7](context7/)                   | Front the public Context7 MCP server via `http.passthrough` on a no-auth gateway, forwarding the caller's optional Context7 API key |
| [github](github/)                       | Front the GitHub MCP server via `http.passthrough` on a no-auth gateway, forwarding the caller's GitHub token |

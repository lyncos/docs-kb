---
title: schema-upfront-diagram
description: 'Admin->>Gateway: CreateGatewayTarget/UpdateGatewayTarget<br/>(MCP endpoint, AgentCore Identity Credential Provider, Tool Schema) Gateway->>Gateway: Parse and cache tool definitions from provided schema Gateway-->>Admin: Target created/updated successfully'
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/06-workshops/02-AgentCore-gateway/05-mcp-server-as-a-target/03-authorization-code-flow/flows/schema-upfront-diagram.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

```mermaid
sequenceDiagram
    participant Admin as Admin User
    participant Gateway as AgentCore Gateway
    participant MCP as MCP Server (Target)

    Admin->>Gateway: CreateGatewayTarget/UpdateGatewayTarget<br/>(MCP endpoint, AgentCore Identity Credential Provider, Tool Schema)
    Gateway->>Gateway: Parse and cache tool definitions from provided schema
    Gateway-->>Admin: Target created/updated successfully

    Note over Admin, MCP: No OAuth flow required during target creation.<br/>Admin provides tool schema directly, eliminating the need<br/>for AgentCore Gateway to connect to the MCP server.

    Note right of MCP: *Also applies to UpdateGatewayTarget
```

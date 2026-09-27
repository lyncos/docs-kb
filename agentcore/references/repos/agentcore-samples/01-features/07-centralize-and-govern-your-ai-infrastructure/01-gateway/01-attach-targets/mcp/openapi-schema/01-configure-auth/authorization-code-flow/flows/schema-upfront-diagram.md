---
title: schema-upfront-diagram
description: 'Admin->>Gateway: CreateGatewayTarget/UpdateGatewayTarget<br/>(OpenAPI spec, AgentCore Identity Credential Provider, Tool Schema) Gateway->>Gateway: Parse and cache tool definitions from provided schema Gateway-->>Admin: Target created/updated successfully'
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/01-features/07-centralize-and-govern-your-ai-infrastructure/01-gateway/01-attach-targets/mcp/openapi-schema/01-configure-auth/authorization-code-flow/flows/schema-upfront-diagram.md
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
    participant API as OpenAPI Schema Target

    Admin->>Gateway: CreateGatewayTarget/UpdateGatewayTarget<br/>(OpenAPI spec, AgentCore Identity Credential Provider, Tool Schema)
    Gateway->>Gateway: Parse and cache tool definitions from provided schema
    Gateway-->>Admin: Target created/updated successfully

    Note over Admin, API: No OAuth flow required during target creation.<br/>Admin provides OpenAPI schema directly, eliminating the need<br/>for AgentCore Gateway to connect to the target API.

    Note right of API: *Also applies to UpdateGatewayTarget
```

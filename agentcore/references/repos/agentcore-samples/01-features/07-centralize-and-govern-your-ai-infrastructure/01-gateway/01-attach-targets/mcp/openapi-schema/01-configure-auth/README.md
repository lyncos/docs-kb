---
title: Configure Outbound Authentication for OpenAPI Targets
description: This section covers different outbound authentication patterns for OpenAPI schema targets.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/01-features/07-centralize-and-govern-your-ai-infrastructure/01-gateway/01-attach-targets/mcp/openapi-schema/01-configure-auth/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# Configure Outbound Authentication for OpenAPI Targets

This section covers different outbound authentication patterns for OpenAPI schema targets.

## Samples

| Sample | Outbound Auth | Description |
| :--- | :--- | :--- |
| [API Key](api-key/) | API Key | NASA Mars InSight weather API with API key authentication |
| [OAuth (Client Credentials)](client-credentials/) | OAuth 2.0 (Client Credentials) | Zendesk support APIs with OAuth client credentials outbound auth |
| [OBO Token Exchange](obo-token-exchange/) | OAuth 2.0 (On-Behalf-Of) | Microsoft Graph API with Entra ID OBO token exchange |
| [Authorization Code Flow](authorization-code-flow/) | OAuth 2.0 (Authorization Code) | Third-party APIs requiring user consent (LinkedIn, etc.) |

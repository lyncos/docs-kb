---
title: Inference inbound authorization
description: Control which callers can reach your gateway's inference endpoint. Inbound auth is how a client authenticates **to the gateway**, distinct from outbound auth, which is how the gateway authenticates to model providers.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/01-features/07-centralize-and-govern-your-ai-infrastructure/01-gateway/02-set-up-inbound-authorization/llm-inference/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# Inference inbound authorization

Control which callers can reach your gateway's inference endpoint. Inbound auth is how a client authenticates **to the gateway**, distinct from outbound auth, which is how the gateway authenticates to model providers.

![arch](../../01-attach-targets/llm-inference/images/architecture.png)

An inference target is invoked over the gateway's `/inference` path using the OpenAI or Anthropic SDK (or any HTTP client), not an MCP client. The gateway's inbound authorizer decides who may call it. AgentCore gateway supports two inbound authorizers for inference:

- **Amazon Cognito (CUSTOM_JWT)**: the caller presents a JWT, passed as the SDK credential. This is the default used across this lab.
- **AWS IAM (SigV4)**: the caller signs requests with AWS credentials. No identity provider is needed.

> [!NOTE]
> For how the gateway authenticates outbound to model providers, see [01-attach-targets/llm-inference/02-configure-outbound-auth](../../01-attach-targets/llm-inference/02-configure-outbound-auth/).

## Topics

| Section                   | Description                                                                        |
| :------------------------ | :--------------------------------------------------------------------------------- |
| [custom_jwt](custom_jwt/) | Amazon Cognito (CUSTOM_JWT) inbound auth. Concept and links to the runnable demos. |
| [iam](iam/)               | AWS IAM (SigV4) inbound auth. Hands-on with Bedrock and OpenAI targets.            |

## Documentation

- [AgentCore gateway Developer Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [AgentCore identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-authentication.html)

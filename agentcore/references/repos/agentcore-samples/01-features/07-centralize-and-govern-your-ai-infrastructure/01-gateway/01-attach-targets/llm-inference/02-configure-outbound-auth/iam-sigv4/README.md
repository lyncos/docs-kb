---
title: IAM (SigV4) outbound auth
description: Configure an inference target so the gateway authenticates **outbound** to Amazon Bedrock using its own IAM role and AWS Signature V4. No API key is stored or managed.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/01-features/07-centralize-and-govern-your-ai-infrastructure/01-gateway/01-attach-targets/llm-inference/02-configure-outbound-auth/iam-sigv4/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# IAM (SigV4) outbound auth

Configure an inference target so the gateway authenticates **outbound** to Amazon Bedrock using its own IAM role and AWS Signature V4. No API key is stored or managed.

## Overview

When a provider accepts AWS IAM authentication, the gateway signs outbound requests with SigV4 using the IAM role attached to the gateway. There is no secret to store, rotate, or leak, which makes this the simplest and most secure outbound option for Amazon Bedrock.

## How it works

1. The client authenticates **inbound** to the gateway with a Cognito JWT (passed as the SDK credential).
2. The gateway authenticates **outbound** to Bedrock by signing the request with SigV4 using its IAM role.
3. The gateway role is granted `bedrock-mantle:ListModels` and `bedrock-mantle:CreateInference`.

## Target configuration

Use `GATEWAY_IAM_ROLE` as the credential provider type. No credential provider block is needed because the gateway uses its own role. These are the [`create_gateway_target`](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateGatewayTarget.html) request parameters:

```json
{
  "gatewayIdentifier": "GATEWAY_ID",
  "name": "bedrock-mantle",
  "targetConfiguration": {
    "inference": {
      "connector": { "source": { "connectorId": "bedrock-mantle" } }
    }
  },
  "credentialProviderConfigurations": [{ "credentialProviderType": "GATEWAY_IAM_ROLE" }]
}
```

## Try it

The [unified multi-provider tutorial](../../01-unified-multi-provider-access/) deploys this Bedrock target with `GATEWAY_IAM_ROLE` outbound auth and invokes it end to end (Step 3.1 shows the same configuration).

## Documentation

- [AgentCore gateway Developer Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [AgentCore identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-authentication.html)

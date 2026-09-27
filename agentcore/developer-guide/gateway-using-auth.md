---
title: Authorize and authenticate to an AgentCore gateway and gateway target
description: 'To invoke your gateway and gateway target, you’ll need to make sure that the following credentials that you set up while fulfilling the prerequisites are recognized during gateway invocation: + Inbound authorization – Authorization and authentication to the gateway. + Outbound au'
product: Amazon Bedrock AgentCore
section: Developer Guide / gateway
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-using-auth.html
fetched: '2026-09-26'
tags:
- agentcore
- gateway
---

# Authorize and authenticate to an AgentCore gateway and gateway target
<a name="gateway-using-auth"></a>

To invoke your gateway and gateway target, you’ll need to make sure that the following credentials that you set up while fulfilling the [prerequisites](gateway-prerequisites.md) are recognized during gateway invocation:
+  [Inbound authorization](gateway-inbound-auth.md) – Authorization and authentication to the gateway.
+  [Outbound authorization](gateway-outbound-auth.md) – Authorization and authentication to the gateway target.

To learn how to obtain and configure credentials, review the provider documentation for the methods that you choose.

The following sections provide examples of obtaining and configuring credentials for different use cases.

**Topics**
+ [Example: Authorization for the default gateway and target created by the AgentCore CLI](gateway-using-auth-ex-starter.md)
+ [Example: Authentication with an authorization code grant when invoking a gateway](gateway-using-auth-ex-3lo.md)
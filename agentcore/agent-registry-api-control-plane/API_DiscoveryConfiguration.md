---
title: DiscoveryConfiguration
description: Discovery configuration for the registry. Controls how consumers are authorized to search the registry and invoke its MCP endpoint.
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_DiscoveryConfiguration.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# DiscoveryConfiguration
<a name="API_DiscoveryConfiguration"></a>

Discovery configuration for the registry. Controls how consumers are authorized to search the registry and invoke its MCP endpoint.

## Contents
<a name="API_DiscoveryConfiguration_Contents"></a>

 ** authorizerConfiguration **   <a name="agentregistrycontrol-Type-DiscoveryConfiguration-authorizerConfiguration"></a>
The authorizer configuration for the registry. Required when authorizerType is CUSTOM\_JWT.  
Type: [AuthorizerConfiguration](API_AuthorizerConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** authorizerType **   <a name="agentregistrycontrol-Type-DiscoveryConfiguration-authorizerType"></a>
The type of authorizer that controls how consumers access the registry's search and MCP invoke operations.  
Type: String  
Valid Values: `CUSTOM_JWT | AWS_IAM`   
Required: No

## See Also
<a name="API_DiscoveryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/DiscoveryConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/DiscoveryConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/DiscoveryConfiguration) 
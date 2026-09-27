---
title: PrivateEndpointOverride
description: A mapping of a domain to the private endpoint used to reach it.
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_PrivateEndpointOverride.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# PrivateEndpointOverride
<a name="API_PrivateEndpointOverride"></a>

A mapping of a domain to the private endpoint used to reach it.

## Contents
<a name="API_PrivateEndpointOverride_Contents"></a>

 ** domain **   <a name="agentregistrycontrol-Type-PrivateEndpointOverride-domain"></a>
The domain name to which this private endpoint override applies.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Required: Yes

 ** privateEndpoint **   <a name="agentregistrycontrol-Type-PrivateEndpointOverride-privateEndpoint"></a>
The private endpoint used to reach the specified domain.  
Type: [PrivateEndpoint](API_PrivateEndpoint.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## See Also
<a name="API_PrivateEndpointOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/PrivateEndpointOverride) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/PrivateEndpointOverride) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/PrivateEndpointOverride) 
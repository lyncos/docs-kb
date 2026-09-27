---
title: ConsentPortalSource
description: A resource served by the consent portal.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ConsentPortalSource.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# ConsentPortalSource
<a name="API_ConsentPortalSource"></a>

A resource served by the consent portal.

## Contents
<a name="API_ConsentPortalSource_Contents"></a>

 ** identifier **   <a name="bedrockagentcorecontrol-Type-ConsentPortalSource-identifier"></a>
The identifier of the source resource. For an `agentcore-gateway` source, this is the gateway ID or its Amazon Resource Name (ARN).  
Type: String  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}$|^arn:aws(-[a-z-]+)?:bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}`   
Required: Yes

 ** type **   <a name="bedrockagentcorecontrol-Type-ConsentPortalSource-type"></a>
The type of the source resource.  
Type: String  
Valid Values: `agentcore-gateway`   
Required: Yes

## See Also
<a name="API_ConsentPortalSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ConsentPortalSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ConsentPortalSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ConsentPortalSource) 
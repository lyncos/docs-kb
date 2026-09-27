---
title: HttpConnectorTargetConfiguration
description: The configuration for an HTTP connector target. Use this configuration when you want to route HTTP requests through a managed connector.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_HttpConnectorTargetConfiguration.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# HttpConnectorTargetConfiguration
<a name="API_HttpConnectorTargetConfiguration"></a>

The configuration for an HTTP connector target. Use this configuration when you want to route HTTP requests through a managed connector.

## Contents
<a name="API_HttpConnectorTargetConfiguration_Contents"></a>

 ** source **   <a name="bedrockagentcorecontrol-Type-HttpConnectorTargetConfiguration-source"></a>
The source configuration identifying which HTTP connector to use.  
Type: [HttpConnectorSource](API_HttpConnectorSource.md) object  
Required: Yes

 ** parameters **   <a name="bedrockagentcorecontrol-Type-HttpConnectorTargetConfiguration-parameters"></a>
The resource parameters for this connector (for example, `memoryId`). The service validates these parameters against the request path at runtime.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 10 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z][a-zA-Z0-9_-]*`   
Value Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: No

## See Also
<a name="API_HttpConnectorTargetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HttpConnectorTargetConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HttpConnectorTargetConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HttpConnectorTargetConfiguration) 
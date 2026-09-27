---
title: SessionConfiguration
description: The session configuration for an MCP gateway. This structure defines settings that control session behavior.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_SessionConfiguration.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# SessionConfiguration
<a name="API_SessionConfiguration"></a>

The session configuration for an MCP gateway. This structure defines settings that control session behavior.

## Contents
<a name="API_SessionConfiguration_Contents"></a>

 ** sessionTimeoutInSeconds **   <a name="bedrockagentcorecontrol-Type-SessionConfiguration-sessionTimeoutInSeconds"></a>
The session timeout in seconds. After this timeout, the session expires and subsequent requests to this session will receive an error. The minimum value is 900 seconds (15 minutes), the maximum value is 28800 seconds (8 hours), and the default value is 3600 seconds (1 hour).  
Type: Integer  
Valid Range: Minimum value of 900. Maximum value of 28800.  
Required: No

## See Also
<a name="API_SessionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/SessionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/SessionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/SessionConfiguration) 
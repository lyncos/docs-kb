---
title: HarnessInlineFunctionConfig
description: Configuration for an inline function tool. When the agent calls this tool, the tool call is returned to the caller for external execution.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_HarnessInlineFunctionConfig.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# HarnessInlineFunctionConfig
<a name="API_HarnessInlineFunctionConfig"></a>

Configuration for an inline function tool. When the agent calls this tool, the tool call is returned to the caller for external execution.

## Contents
<a name="API_HarnessInlineFunctionConfig_Contents"></a>

 ** description **   <a name="bedrockagentcorecontrol-Type-HarnessInlineFunctionConfig-description"></a>
Description of what the tool does, provided to the model.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: Yes

 ** inputSchema **   <a name="bedrockagentcorecontrol-Type-HarnessInlineFunctionConfig-inputSchema"></a>
JSON Schema describing the tool's input parameters.  
Type: JSON value  
Required: Yes

## See Also
<a name="API_HarnessInlineFunctionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessInlineFunctionConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessInlineFunctionConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessInlineFunctionConfig) 
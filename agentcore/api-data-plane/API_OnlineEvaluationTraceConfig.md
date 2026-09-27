---
title: OnlineEvaluationTraceConfig
description: Contains the configuration for reusing agent traces from an online evaluation configuration for recommendation analysis. Because online evaluation is a continuous stream, a time range specifies which evaluated sessions the recommendation includes.
product: Amazon Bedrock AgentCore
section: Data Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_OnlineEvaluationTraceConfig.html
fetched: '2026-09-26'
tags:
- agentcore
- data-plane-api
---

# OnlineEvaluationTraceConfig
<a name="API_OnlineEvaluationTraceConfig"></a>

Contains the configuration for reusing agent traces from an online evaluation configuration for recommendation analysis. Because online evaluation is a continuous stream, a time range specifies which evaluated sessions the recommendation includes.

## Contents
<a name="API_OnlineEvaluationTraceConfig_Contents"></a>

 ** endTime **   <a name="BedrockAgentCore-Type-OnlineEvaluationTraceConfig-endTime"></a>
The end time of the time range. Only sessions evaluated before this timestamp are included.  
Type: Timestamp  
Required: Yes

 ** onlineEvaluationConfigArn **   <a name="BedrockAgentCore-Type-OnlineEvaluationTraceConfig-onlineEvaluationConfigArn"></a>
The ARN of the online evaluation configuration to reuse sessions from.  
Type: String  
Pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:online-evaluation-config\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** startTime **   <a name="BedrockAgentCore-Type-OnlineEvaluationTraceConfig-startTime"></a>
The start time of the time range. Only sessions evaluated at or after this timestamp are included.  
Type: Timestamp  
Required: Yes

## See Also
<a name="API_OnlineEvaluationTraceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/OnlineEvaluationTraceConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/OnlineEvaluationTraceConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/OnlineEvaluationTraceConfig) 
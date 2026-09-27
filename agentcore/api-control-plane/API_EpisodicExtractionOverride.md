---
title: EpisodicExtractionOverride
description: Contains configurations to override the default extraction step for the episodic memory strategy.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_EpisodicExtractionOverride.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# EpisodicExtractionOverride
<a name="API_EpisodicExtractionOverride"></a>

Contains configurations to override the default extraction step for the episodic memory strategy.

## Contents
<a name="API_EpisodicExtractionOverride_Contents"></a>

 ** appendToPrompt **   <a name="bedrockagentcorecontrol-Type-EpisodicExtractionOverride-appendToPrompt"></a>
The text appended to the prompt for the extraction step of the episodic memory strategy.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 30000.  
Required: Yes

 ** modelId **   <a name="bedrockagentcorecontrol-Type-EpisodicExtractionOverride-modelId"></a>
The model ID used for the extraction step of the episodic memory strategy.  
Type: String  
Required: Yes

## See Also
<a name="API_EpisodicExtractionOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/EpisodicExtractionOverride) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/EpisodicExtractionOverride) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/EpisodicExtractionOverride) 
---
title: DerivedEvaluatorConfig
description: The configuration for a derived evaluator. It reuses an existing evaluator's logic on your own model.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DerivedEvaluatorConfig.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# DerivedEvaluatorConfig
<a name="API_DerivedEvaluatorConfig"></a>

 The configuration for a derived evaluator. It reuses an existing evaluator's logic on your own model. 

## Contents
<a name="API_DerivedEvaluatorConfig_Contents"></a>

 ** baseEvaluatorId **   <a name="bedrockagentcorecontrol-Type-DerivedEvaluatorConfig-baseEvaluatorId"></a>
 The identifier of the base evaluator whose logic to run (a `Builtin.*` or `ThirdParty.*` evaluator).   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 111.  
Pattern: `(Builtin\.[a-zA-Z0-9._-]+|ThirdParty\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})`   
Required: Yes

 ** modelConfig **   <a name="bedrockagentcorecontrol-Type-DerivedEvaluatorConfig-modelConfig"></a>
 The configuration of the evaluator model that you supply.   
Type: [EvaluatorModelConfig](API_EvaluatorModelConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## See Also
<a name="API_DerivedEvaluatorConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/DerivedEvaluatorConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/DerivedEvaluatorConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/DerivedEvaluatorConfig) 
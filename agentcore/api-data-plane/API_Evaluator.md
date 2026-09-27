---
title: Evaluator
description: An evaluator to run against sessions during batch evaluation.
product: Amazon Bedrock AgentCore
section: Data Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_Evaluator.html
fetched: '2026-09-26'
tags:
- agentcore
- data-plane-api
---

# Evaluator
<a name="API_Evaluator"></a>

An evaluator to run against sessions during batch evaluation.

## Contents
<a name="API_Evaluator_Contents"></a>

 ** evaluatorId **   <a name="BedrockAgentCore-Type-Evaluator-evaluatorId"></a>
The unique identifier of the evaluator. Can reference built-in evaluators (e.g., `Builtin.Helpfulness`) or custom evaluators.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 111.  
Pattern: `(Builtin\.[a-zA-Z0-9._-]+|ThirdParty\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})`   
Required: Yes

## See Also
<a name="API_Evaluator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/Evaluator) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/Evaluator) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/Evaluator) 
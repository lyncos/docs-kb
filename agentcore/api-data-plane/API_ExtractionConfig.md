---
title: ExtractionConfig
description: The configuration for extraction behavior. Use this structure to specify namespace variable keys and their values for namespace substitution during long-term memory extraction.
product: Amazon Bedrock AgentCore
section: Data Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ExtractionConfig.html
fetched: '2026-09-26'
tags:
- agentcore
- data-plane-api
---

# ExtractionConfig
<a name="API_ExtractionConfig"></a>

The configuration for extraction behavior. Use this structure to specify namespace variable keys and their values for namespace substitution during long-term memory extraction.

## Contents
<a name="API_ExtractionConfig_Contents"></a>

 ** namespaceVariables **   <a name="BedrockAgentCore-Type-ExtractionConfig-namespaceVariables"></a>
A map of `namespaceKeys` to their values. The service substitutes these values into `namespaceTemplates` during long-term memory extraction to control namespace hierarchy.  
Type: String to string map  
Map Entries: Maximum number of 5 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 32.  
Key Pattern: `(?!memoryStrategyId$|actorId$|sessionId$)[a-z][a-z0-9]*`   
Value Length Constraints: Minimum length of 1. Maximum length of 64.  
Value Pattern: `[a-z0-9][a-z0-9-_]*`   
Required: No

## See Also
<a name="API_ExtractionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ExtractionConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ExtractionConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ExtractionConfig) 
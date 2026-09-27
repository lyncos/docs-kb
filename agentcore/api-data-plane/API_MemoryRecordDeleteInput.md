---
title: MemoryRecordDeleteInput
description: Input structure to delete an existing memory record.
product: Amazon Bedrock AgentCore
section: Data Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_MemoryRecordDeleteInput.html
fetched: '2026-09-26'
tags:
- agentcore
- data-plane-api
---

# MemoryRecordDeleteInput
<a name="API_MemoryRecordDeleteInput"></a>

Input structure to delete an existing memory record.

## Contents
<a name="API_MemoryRecordDeleteInput_Contents"></a>

 ** memoryRecordId **   <a name="BedrockAgentCore-Type-MemoryRecordDeleteInput-memoryRecordId"></a>
The unique ID of the memory record to be deleted.  
Type: String  
Length Constraints: Minimum length of 40. Maximum length of 50.  
Pattern: `mem-[a-zA-Z0-9-_]*`   
Required: Yes

 ** namespace **   <a name="BedrockAgentCore-Type-MemoryRecordDeleteInput-namespace"></a>
The namespace of the memory record being deleted. This value is used for IAM condition key authorization.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `[a-zA-Z0-9/*][a-zA-Z0-9-_/*]*(?::[a-zA-Z0-9-_/*]+)*[a-zA-Z0-9-_/*]*`   
Required: No

## See Also
<a name="API_MemoryRecordDeleteInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MemoryRecordDeleteInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MemoryRecordDeleteInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MemoryRecordDeleteInput) 
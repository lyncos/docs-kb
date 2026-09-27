---
title: BatchPutLimitEntry
description: A rate limit definition within a batch put request. If you provide a `rateLimitId`, the service uses it for upsert matching against existing rate limits.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_BatchPutLimitEntry.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# BatchPutLimitEntry
<a name="API_BatchPutLimitEntry"></a>

A rate limit definition within a batch put request. If you provide a `rateLimitId`, the service uses it for upsert matching against existing rate limits.

## Contents
<a name="API_BatchPutLimitEntry_Contents"></a>

 ** dimensionKeys **   <a name="bedrockagentcorecontrol-Type-BatchPutLimitEntry-dimensionKeys"></a>
The ordered list of dimension key names that define the scope of this rate limit.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 80.  
Pattern: `(targetName|toolName|qualifiedModelId|\$\.context\.iam\.principal|\$\.context\.iam\.sourceIdentity|\$\.context\.jwt\.[a-zA-Z_][a-zA-Z0-9_\-\.]{0,61}[a-zA-Z0-9_])`   
Required: Yes

 ** entries **   <a name="bedrockagentcorecontrol-Type-BatchPutLimitEntry-entries"></a>
The list of rule entries that map dimension values to rate configurations.  
Type: Array of [LimitEntry](API_LimitEntry.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 1000 items.  
Required: Yes

 ** description **   <a name="bedrockagentcorecontrol-Type-BatchPutLimitEntry-description"></a>
An optional human-readable description for this rate limit. If not provided, the rate limit is created without a description.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 512.  
Required: No

 ** rateLimitId **   <a name="bedrockagentcorecontrol-Type-BatchPutLimitEntry-rateLimitId"></a>
The unique identifier of the rate limit. If provided, the service uses it for upsert matching against existing rate limits.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 64.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9\-_\.]{0,62}[a-zA-Z0-9]`   
Required: No

## See Also
<a name="API_BatchPutLimitEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/BatchPutLimitEntry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/BatchPutLimitEntry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/BatchPutLimitEntry) 
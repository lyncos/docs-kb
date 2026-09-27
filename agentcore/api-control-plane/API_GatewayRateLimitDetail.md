---
title: GatewayRateLimitDetail
description: Contains detailed information about a gateway rate limit, including its configuration and current status.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GatewayRateLimitDetail.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# GatewayRateLimitDetail
<a name="API_GatewayRateLimitDetail"></a>

Contains detailed information about a gateway rate limit, including its configuration and current status.

## Contents
<a name="API_GatewayRateLimitDetail_Contents"></a>

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-GatewayRateLimitDetail-createdAt"></a>
The timestamp when the rate limit was created.  
Type: Timestamp  
Required: Yes

 ** dimensionKeys **   <a name="bedrockagentcorecontrol-Type-GatewayRateLimitDetail-dimensionKeys"></a>
The ordered list of dimension key names that define the scope of this rate limit.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 80.  
Pattern: `(targetName|toolName|qualifiedModelId|\$\.context\.iam\.principal|\$\.context\.iam\.sourceIdentity|\$\.context\.jwt\.[a-zA-Z_][a-zA-Z0-9_\-\.]{0,61}[a-zA-Z0-9_])`   
Required: Yes

 ** entries **   <a name="bedrockagentcorecontrol-Type-GatewayRateLimitDetail-entries"></a>
The list of rule entries that map dimension values to rate configurations.  
Type: Array of [LimitEntry](API_LimitEntry.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 1000 items.  
Required: Yes

 ** gatewayIdentifier **   <a name="bedrockagentcorecontrol-Type-GatewayRateLimitDetail-gatewayIdentifier"></a>
The unique identifier of the gateway.  
Type: String  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

 ** rateLimitId **   <a name="bedrockagentcorecontrol-Type-GatewayRateLimitDetail-rateLimitId"></a>
The unique identifier of the rate limit.  
Type: String  
Length Constraints: Minimum length of 2. Maximum length of 64.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9\-_\.]{0,62}[a-zA-Z0-9]`   
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-GatewayRateLimitDetail-status"></a>
The current status of the rate limit.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING`   
Required: Yes

 ** updatedAt **   <a name="bedrockagentcorecontrol-Type-GatewayRateLimitDetail-updatedAt"></a>
The timestamp when the rate limit was last updated.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="bedrockagentcorecontrol-Type-GatewayRateLimitDetail-description"></a>
The human-readable description of the rate limit.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 512.  
Required: No

## See Also
<a name="API_GatewayRateLimitDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GatewayRateLimitDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GatewayRateLimitDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GatewayRateLimitDetail) 
---
title: LimitEntry
description: A single rule entry within a rate limit that maps dimension values to rate configurations. Each entry defines the rate limits for a specific combination of dimension values.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_LimitEntry.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# LimitEntry
<a name="API_LimitEntry"></a>

A single rule entry within a rate limit that maps dimension values to rate configurations. Each entry defines the rate limits for a specific combination of dimension values.

## Contents
<a name="API_LimitEntry_Contents"></a>

 ** dimensions **   <a name="bedrockagentcorecontrol-Type-LimitEntry-dimensions"></a>
A map of dimension names to dimension values for this rule entry. Keys must match the parent rate limit's dimension keys. Values may use `*` as a wildcard, but only in trailing positions based on the dimension keys ordering.  
Type: String to string map  
Map Entries: Maximum number of 10 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 80.  
Key Pattern: `(targetName|toolName|qualifiedModelId|\$\.context\.iam\.principal|\$\.context\.iam\.sourceIdentity|\$\.context\.jwt\.[a-zA-Z_][a-zA-Z0-9_\-\.]{0,61}[a-zA-Z0-9_])`   
Value Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

 ** connections **   <a name="bedrockagentcorecontrol-Type-LimitEntry-connections"></a>
The connection rate limit configuration. Specifies the maximum number of concurrent connections allowed.  
Type: Array of [RateConfig](API_RateConfig.md) objects  
Array Members: Fixed number of 1 item.  
Required: No

 ** requests **   <a name="bedrockagentcorecontrol-Type-LimitEntry-requests"></a>
The request rate limit configuration. Specifies the maximum number of requests allowed per time period.  
Type: Array of [RateConfig](API_RateConfig.md) objects  
Array Members: Fixed number of 1 item.  
Required: No

 ** tokens **   <a name="bedrockagentcorecontrol-Type-LimitEntry-tokens"></a>
The token rate limit configuration. Specifies the maximum number of tokens allowed per time period.  
Type: Array of [RateConfig](API_RateConfig.md) objects  
Array Members: Fixed number of 1 item.  
Required: No

## See Also
<a name="API_LimitEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/LimitEntry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/LimitEntry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/LimitEntry) 
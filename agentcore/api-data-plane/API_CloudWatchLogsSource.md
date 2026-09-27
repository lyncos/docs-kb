---
title: CloudWatchLogsSource
description: The configuration for reading agent traces from CloudWatch Logs.
product: Amazon Bedrock AgentCore
section: Data Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_CloudWatchLogsSource.html
fetched: '2026-09-26'
tags:
- agentcore
- data-plane-api
---

# CloudWatchLogsSource
<a name="API_CloudWatchLogsSource"></a>

The configuration for reading agent traces from CloudWatch Logs.

## Contents
<a name="API_CloudWatchLogsSource_Contents"></a>

 ** serviceNames **   <a name="BedrockAgentCore-Type-CloudWatchLogsSource-serviceNames"></a>
The list of agent service names to filter traces within the specified log groups.  
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Required: Yes

 ** filterConfig **   <a name="BedrockAgentCore-Type-CloudWatchLogsSource-filterConfig"></a>
Optional filter configuration to narrow down which sessions to evaluate.  
Type: [CloudWatchFilterConfig](API_CloudWatchFilterConfig.md) object  
Required: No

 ** logGroupNamePrefixes **   <a name="BedrockAgentCore-Type-CloudWatchLogsSource-logGroupNamePrefixes"></a>
The list of CloudWatch log group name prefixes to read agent traces from. Specify this instead of `logGroupNames` to match log groups by prefix. Maximum of 5 prefixes. Specify either `logGroupNames` or `logGroupNamePrefixes`, not both. One of the two is required.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Pattern: `[.\-_/#A-Za-z0-9]+`   
Required: No

 ** logGroupNames **   <a name="BedrockAgentCore-Type-CloudWatchLogsSource-logGroupNames"></a>
The list of CloudWatch log group names to read agent traces from. Maximum of 10 log groups.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Pattern: `[.\-_/#A-Za-z0-9]+`   
Required: No

## See Also
<a name="API_CloudWatchLogsSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CloudWatchLogsSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CloudWatchLogsSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CloudWatchLogsSource) 
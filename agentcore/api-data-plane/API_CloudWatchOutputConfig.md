---
title: CloudWatchOutputConfig
description: CloudWatch Logs destination for batch evaluation results.
product: Amazon Bedrock AgentCore
section: Data Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_CloudWatchOutputConfig.html
fetched: '2026-09-26'
tags:
- agentcore
- data-plane-api
---

# CloudWatchOutputConfig
<a name="API_CloudWatchOutputConfig"></a>

CloudWatch Logs destination for batch evaluation results.

## Contents
<a name="API_CloudWatchOutputConfig_Contents"></a>

 ** logGroupName **   <a name="BedrockAgentCore-Type-CloudWatchOutputConfig-logGroupName"></a>
The name of the CloudWatch log group where evaluation results will be written. This value doesn't apply when `resultDestination` is `SOURCE_LOG_GROUP`, because results are written back to the trace source log group. The name can't be under the service-reserved `/aws/bedrock-agentcore/evaluations/` namespace, apart from the service-managed default group.  
Type: String  
Pattern: `$|^[.\-_/#A-Za-z0-9]+`   
Required: No

 ** logStreamName **   <a name="BedrockAgentCore-Type-CloudWatchOutputConfig-logStreamName"></a>
The name of the CloudWatch log stream where evaluation results will be written.  
Type: String  
Pattern: `[^:*]*`   
Required: No

 ** metricsNamespace **   <a name="BedrockAgentCore-Type-CloudWatchOutputConfig-metricsNamespace"></a>
The CloudWatch metrics namespace where evaluation result metrics are published. If you omit this value, the service publishes metrics to `Bedrock-AgentCore/Evaluations`. This value can't begin with `AWS/`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9._#/:-]+`   
Required: No

 ** resultDestination **   <a name="BedrockAgentCore-Type-CloudWatchOutputConfig-resultDestination"></a>
The destination where evaluation results are written. Valid values:  
+  `DEDICATED_LOG_GROUP` (default) – Writes results to a dedicated result log group.
+  `SOURCE_LOG_GROUP` – Writes results back to the log group that the agent traces were read from. If you use this value, don't specify `logGroupName`.
Type: String  
Valid Values: `DEDICATED_LOG_GROUP | SOURCE_LOG_GROUP`   
Required: No

## See Also
<a name="API_CloudWatchOutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CloudWatchOutputConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CloudWatchOutputConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CloudWatchOutputConfig) 
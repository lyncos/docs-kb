---
title: CloudWatchOutputConfig
description: The configuration for writing evaluation results to CloudWatch logs with embedded metric format (EMF) for monitoring.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CloudWatchOutputConfig.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# CloudWatchOutputConfig
<a name="API_CloudWatchOutputConfig"></a>

 The configuration for writing evaluation results to CloudWatch logs with embedded metric format (EMF) for monitoring. 

## Contents
<a name="API_CloudWatchOutputConfig_Contents"></a>

 ** logGroupName **   <a name="bedrockagentcorecontrol-Type-CloudWatchOutputConfig-logGroupName"></a>
 The name of the CloudWatch log group where evaluation results will be written. An existing log group is used as-is; otherwise the service creates it, which requires the evaluation execution role to grant `logs:CreateLogGroup` on the log group. Don't specify this value when `resultDestination` is `SOURCE_LOG_GROUP`. The name can't be under the service-reserved `/aws/bedrock-agentcore/evaluations/` namespace, apart from this configuration's own service-managed default group.   
Type: String  
Pattern: `$|^[.\-_/#A-Za-z0-9]+`   
Required: No

 ** metricsNamespace **   <a name="bedrockagentcorecontrol-Type-CloudWatchOutputConfig-metricsNamespace"></a>
 The CloudWatch metrics namespace where evaluation result metrics are published. If you omit this value, the service publishes metrics to `Bedrock-AgentCore/Evaluations`. This value can't begin with `AWS/`.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9._#/:-]+`   
Required: No

 ** resultDestination **   <a name="bedrockagentcorecontrol-Type-CloudWatchOutputConfig-resultDestination"></a>
 The destination where evaluation results are written. Valid values:   
+  `DEDICATED_LOG_GROUP` (default) – Writes results to a dedicated result log group.
+  `SOURCE_LOG_GROUP` – Writes results back to the log group that the agent traces were read from. If you use this value, don't specify `logGroupName`.
Type: String  
Valid Values: `DEDICATED_LOG_GROUP | SOURCE_LOG_GROUP`   
Required: No

## See Also
<a name="API_CloudWatchOutputConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CloudWatchOutputConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CloudWatchOutputConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CloudWatchOutputConfig) 
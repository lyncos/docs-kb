---
title: RateConfig
description: Contains the rate configuration for a rate limit metric, specifying the allowed rate and time period.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_RateConfig.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# RateConfig
<a name="API_RateConfig"></a>

Contains the rate configuration for a rate limit metric, specifying the allowed rate and time period.

## Contents
<a name="API_RateConfig_Contents"></a>

 ** period **   <a name="bedrockagentcorecontrol-Type-RateConfig-period"></a>
The time period for the rate limit. Valid values:  
+  `second`—Measures the rate limit over a one-second window.
+  `minute`—Measures the rate limit over a one-minute window.
Type: String  
Valid Values: `second | minute`   
Required: Yes

 ** rate **   <a name="bedrockagentcorecontrol-Type-RateConfig-rate"></a>
The rate value for the limit. For request limits, this is the number of requests allowed per period. For token limits, this is the number of tokens allowed per period. For connection limits, this is the number of concurrent connections allowed.  
Type: Double  
Valid Range: Minimum value of 0. Maximum value of 10000000.  
Required: Yes

## See Also
<a name="API_RateConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/RateConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/RateConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/RateConfig) 
---
title: InstanceLifecycleConfiguration
description: The configuration that manages the lifecycle of instances in a capacity provider, including idle timeout and maximum lifetime.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_InstanceLifecycleConfiguration.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# InstanceLifecycleConfiguration
<a name="API_InstanceLifecycleConfiguration"></a>

The configuration that manages the lifecycle of instances in a capacity provider, including idle timeout and maximum lifetime.

## Contents
<a name="API_InstanceLifecycleConfiguration_Contents"></a>

 ** idleInstanceTimeout **   <a name="bedrockagentcorecontrol-Type-InstanceLifecycleConfiguration-idleInstanceTimeout"></a>
The number of seconds an instance can remain idle before it is stopped. An instance is considered idle when all of its agents are idle. The default is 900 seconds (15 minutes).  
Type: Integer  
Valid Range: Minimum value of 60. Maximum value of 1209600.  
Required: No

 ** maxLifetime **   <a name="bedrockagentcorecontrol-Type-InstanceLifecycleConfiguration-maxLifetime"></a>
The maximum lifetime of an instance, in seconds. When an instance reaches this limit, the service terminates it regardless of activity. The default is 28800 seconds (8 hours). The maximum is 1209600 seconds (14 days).  
Type: Integer  
Valid Range: Minimum value of 60. Maximum value of 1209600.  
Required: No

## See Also
<a name="API_InstanceLifecycleConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/InstanceLifecycleConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/InstanceLifecycleConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/InstanceLifecycleConfiguration) 
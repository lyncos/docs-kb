---
title: VpcConfiguration
description: The VPC configuration for launching Amazon EC2 instances.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_VpcConfiguration.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# VpcConfiguration
<a name="API_VpcConfiguration"></a>

The VPC configuration for launching Amazon EC2 instances.

## Contents
<a name="API_VpcConfiguration_Contents"></a>

 ** securityGroups **   <a name="bedrockagentcorecontrol-Type-VpcConfiguration-securityGroups"></a>
The IDs of the security groups to associate with the instances. You must specify at least one security group.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 16 items.  
Pattern: `sg-[0-9a-zA-Z]{8,17}`   
Required: Yes

 ** subnets **   <a name="bedrockagentcorecontrol-Type-VpcConfiguration-subnets"></a>
The IDs of the subnets in which to launch instances. You must specify at least one subnet.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 16 items.  
Pattern: `subnet-[0-9a-zA-Z]{8,17}`   
Required: Yes

## See Also
<a name="API_VpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/VpcConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/VpcConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/VpcConfiguration) 
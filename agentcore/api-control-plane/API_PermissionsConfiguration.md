---
title: PermissionsConfiguration
description: The permissions configuration for a capacity provider. This specifies the IAM role that AgentCore uses to manage the Amazon EC2 instances for the capacity provider on your behalf.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_PermissionsConfiguration.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# PermissionsConfiguration
<a name="API_PermissionsConfiguration"></a>

The permissions configuration for a capacity provider. This specifies the IAM role that AgentCore uses to manage the Amazon EC2 instances for the capacity provider on your behalf.

## Contents
<a name="API_PermissionsConfiguration_Contents"></a>

 ** capacityProviderOperatorRoleArn **   <a name="bedrockagentcorecontrol-Type-PermissionsConfiguration-capacityProviderOperatorRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that AgentCore assumes to manage the capacity provider, including launching, tagging, and terminating instances and their network interfaces. We recommend scoping this role to the minimum permissions that your workloads require.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`   
Required: Yes

## See Also
<a name="API_PermissionsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/PermissionsConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/PermissionsConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/PermissionsConfiguration) 
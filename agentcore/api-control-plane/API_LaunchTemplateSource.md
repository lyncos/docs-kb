---
title: LaunchTemplateSource
description: The source of the launch template configuration for a capacity provider. The `launchParameters` member specifies the operating system, instance requirements, and other settings used to launch instances.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_LaunchTemplateSource.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# LaunchTemplateSource
<a name="API_LaunchTemplateSource"></a>

The source of the launch template configuration for a capacity provider. The `launchParameters` member specifies the operating system, instance requirements, and other settings used to launch instances.

## Contents
<a name="API_LaunchTemplateSource_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** launchParameters **   <a name="bedrockagentcorecontrol-Type-LaunchTemplateSource-launchParameters"></a>
The parameters that AgentCore uses to create the launch template.  
Type: [LaunchParameters](API_LaunchParameters.md) object  
Required: No

## See Also
<a name="API_LaunchTemplateSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/LaunchTemplateSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/LaunchTemplateSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/LaunchTemplateSource) 
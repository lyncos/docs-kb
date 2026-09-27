---
title: Ec2Configuration
description: The configuration for Amazon EC2-based compute, including the launch template source, networking, storage volumes, and instance lifecycle settings.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_Ec2Configuration.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# Ec2Configuration
<a name="API_Ec2Configuration"></a>

The configuration for Amazon EC2-based compute, including the launch template source, networking, storage volumes, and instance lifecycle settings.

## Contents
<a name="API_Ec2Configuration_Contents"></a>

 ** launchTemplateSource **   <a name="bedrockagentcorecontrol-Type-Ec2Configuration-launchTemplateSource"></a>
The source of the launch template configuration that defines how instances are launched.  
Type: [LaunchTemplateSource](API_LaunchTemplateSource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** vpcConfiguration **   <a name="bedrockagentcorecontrol-Type-Ec2Configuration-vpcConfiguration"></a>
The VPC configuration for launching instances, including subnets and security groups.  
Type: [VpcConfiguration](API_VpcConfiguration.md) object  
Required: Yes

 ** lifecycleConfiguration **   <a name="bedrockagentcorecontrol-Type-Ec2Configuration-lifecycleConfiguration"></a>
The lifecycle configuration for instances in the capacity provider.  
Type: [InstanceLifecycleConfiguration](API_InstanceLifecycleConfiguration.md) object  
Required: No

 ** rootVolume **   <a name="bedrockagentcorecontrol-Type-Ec2Configuration-rootVolume"></a>
The configuration for the instance root volume. Specify the amount of free space to guarantee and, optionally, the Amazon EBS performance and encryption settings. The device name and delete-on-termination behavior are not configurable.  
Type: [RootVolumeConfiguration](API_RootVolumeConfiguration.md) object  
Required: No

 ** volumes **   <a name="bedrockagentcorecontrol-Type-Ec2Configuration-volumes"></a>
The named persistent Amazon EBS volumes for the capacity provider. A capacity provider can define up to five volumes.  
Type: Array of [VolumeConfiguration](API_VolumeConfiguration.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 5 items.  
Required: No

## See Also
<a name="API_Ec2Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/Ec2Configuration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/Ec2Configuration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/Ec2Configuration) 
---
title: EphemeralBlockDeviceMapping
description: A block device mapping for an instance store (ephemeral) volume.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_EphemeralBlockDeviceMapping.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# EphemeralBlockDeviceMapping
<a name="API_EphemeralBlockDeviceMapping"></a>

A block device mapping for an instance store (ephemeral) volume.

## Contents
<a name="API_EphemeralBlockDeviceMapping_Contents"></a>

 ** deviceName **   <a name="bedrockagentcorecontrol-Type-EphemeralBlockDeviceMapping-deviceName"></a>
The device name, for example `/dev/sdh` or `xvdh`.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9/._-]+`   
Required: No

 ** ebs **   <a name="bedrockagentcorecontrol-Type-EphemeralBlockDeviceMapping-ebs"></a>
The shared Amazon EBS performance and encryption properties for a volume. These properties are common across the different volume configurations for a capacity provider.  
Type: [EphemeralEBSVolumeConfiguration](API_EphemeralEBSVolumeConfiguration.md) object  
Required: No

 ** virtualName **   <a name="bedrockagentcorecontrol-Type-EphemeralBlockDeviceMapping-virtualName"></a>
The virtual device name (`ephemeralN`). Instance store volumes are numbered starting from 0. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `ephemeral[0-9]+`   
Required: No

## See Also
<a name="API_EphemeralBlockDeviceMapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/EphemeralBlockDeviceMapping) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/EphemeralBlockDeviceMapping) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/EphemeralBlockDeviceMapping) 
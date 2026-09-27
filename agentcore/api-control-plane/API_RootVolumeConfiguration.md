---
title: RootVolumeConfiguration
description: The configuration for the root volume of a capacity provider instance. Specify the amount of free space to guarantee on the root volume. The device name and delete-on-termination settings are fixed and cannot be changed.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_RootVolumeConfiguration.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# RootVolumeConfiguration
<a name="API_RootVolumeConfiguration"></a>

The configuration for the root volume of a capacity provider instance. Specify the amount of free space to guarantee on the root volume. The device name and delete-on-termination settings are fixed and cannot be changed.

## Contents
<a name="API_RootVolumeConfiguration_Contents"></a>

 ** encrypted **   <a name="bedrockagentcorecontrol-Type-RootVolumeConfiguration-encrypted"></a>
Specifies whether to encrypt the volume. Encrypted volumes can be attached only to instances that support Amazon EBS encryption. If you create a volume from a snapshot, you cannot specify an encryption value.  
Type: Boolean  
Required: No

 ** freeSpaceGiB **   <a name="bedrockagentcorecontrol-Type-RootVolumeConfiguration-freeSpaceGiB"></a>
The free space guaranteed on the root volume, in GiB. AgentCore adds the operating system overhead on top of this value. The default is 8 GiB.  
Type: Integer  
Valid Range: Minimum value of 2. Maximum value of 65000.  
Required: No

 ** iops **   <a name="bedrockagentcorecontrol-Type-RootVolumeConfiguration-iops"></a>
The number of IOPS to provision. For `gp3`, `io1`, and `io2` volumes, this is the number of IOPS provisioned for the volume. For `gp2` volumes, this sets the baseline IOPS performance. It also controls the rate at which the volume accumulates I/O credits for bursting. Supported values: `gp3`, 3,000–80,000; `io1`, 100–64,000; `io2`, 100–256,000.  
Type: Integer  
Valid Range: Minimum value of 100. Maximum value of 256000.  
Required: No

 ** kmsKeyId **   <a name="bedrockagentcorecontrol-Type-RootVolumeConfiguration-kmsKeyId"></a>
The identifier (key ID, key alias, key ARN, or alias ARN) of the customer managed AWS KMS key to use for Amazon EBS encryption.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:kms:[a-z0-9-]+:[0-9]{12}:key/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`   
Required: No

 ** throughput **   <a name="bedrockagentcorecontrol-Type-RootVolumeConfiguration-throughput"></a>
The throughput to provision, in MiB/s. Valid only for `gp3` volumes. Valid range: 125–2,000 MiB/s.  
Type: Integer  
Valid Range: Minimum value of 125. Maximum value of 2000.  
Required: No

 ** volumeType **   <a name="bedrockagentcorecontrol-Type-RootVolumeConfiguration-volumeType"></a>
The Amazon EBS volume type. If you do not specify a type, the default is `gp3`.  
Type: String  
Valid Values: `standard | io1 | io2 | gp2 | sc1 | st1 | gp3`   
Required: No

## See Also
<a name="API_RootVolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/RootVolumeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/RootVolumeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/RootVolumeConfiguration) 
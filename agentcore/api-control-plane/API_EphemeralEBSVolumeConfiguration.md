---
title: EphemeralEBSVolumeConfiguration
description: The shared Amazon EBS performance and encryption properties for a volume. These properties are common across the different volume configurations for a capacity provider.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_EphemeralEBSVolumeConfiguration.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# EphemeralEBSVolumeConfiguration
<a name="API_EphemeralEBSVolumeConfiguration"></a>

The shared Amazon EBS performance and encryption properties for a volume. These properties are common across the different volume configurations for a capacity provider.

## Contents
<a name="API_EphemeralEBSVolumeConfiguration_Contents"></a>

 ** ebsCardIndex **   <a name="bedrockagentcorecontrol-Type-EphemeralEBSVolumeConfiguration-ebsCardIndex"></a>
The index of the Amazon EBS card. Applies to instances with multiple Amazon EBS cards.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** encrypted **   <a name="bedrockagentcorecontrol-Type-EphemeralEBSVolumeConfiguration-encrypted"></a>
Specifies whether to encrypt the volume. Encrypted volumes can be attached only to instances that support Amazon EBS encryption. If you create a volume from a snapshot, you cannot specify an encryption value.  
Type: Boolean  
Required: No

 ** iops **   <a name="bedrockagentcorecontrol-Type-EphemeralEBSVolumeConfiguration-iops"></a>
The number of IOPS to provision. For `gp3`, `io1`, and `io2` volumes, this is the number of IOPS provisioned for the volume. For `gp2` volumes, this sets the baseline IOPS performance. It also controls the rate at which the volume accumulates I/O credits for bursting. Supported values: `gp3`, 3,000–80,000; `io1`, 100–64,000; `io2`, 100–256,000.  
Type: Integer  
Valid Range: Minimum value of 100. Maximum value of 256000.  
Required: No

 ** kmsKeyId **   <a name="bedrockagentcorecontrol-Type-EphemeralEBSVolumeConfiguration-kmsKeyId"></a>
The identifier (key ID, key alias, key ARN, or alias ARN) of the customer managed AWS KMS key to use for Amazon EBS encryption.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:kms:[a-z0-9-]+:[0-9]{12}:key/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`   
Required: No

 ** snapshotId **   <a name="bedrockagentcorecontrol-Type-EphemeralEBSVolumeConfiguration-snapshotId"></a>
The ID of the snapshot.  
Type: String  
Length Constraints: Minimum length of 13. Maximum length of 64.  
Pattern: `snap-[a-f0-9]{8,17}`   
Required: No

 ** throughput **   <a name="bedrockagentcorecontrol-Type-EphemeralEBSVolumeConfiguration-throughput"></a>
The throughput to provision, in MiB/s. Valid only for `gp3` volumes. Valid range: 125–2,000 MiB/s.  
Type: Integer  
Valid Range: Minimum value of 125. Maximum value of 2000.  
Required: No

 ** volumeInitializationRate **   <a name="bedrockagentcorecontrol-Type-EphemeralEBSVolumeConfiguration-volumeInitializationRate"></a>
The rate at which the volume is initialized after creation, in MiB/s. Supported only for volumes created from snapshots. Valid range: 100–300 MiB/s.  
Type: Integer  
Valid Range: Minimum value of 100. Maximum value of 300.  
Required: No

 ** volumeSize **   <a name="bedrockagentcorecontrol-Type-EphemeralEBSVolumeConfiguration-volumeSize"></a>
The size of the volume, in GiB. You must specify either a snapshot ID or a volume size. Supported sizes: `gp2`, 1–16,384; `gp3`, 1–65,536; `io1`, 4–16,384; `io2`, 4–65,536.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65536.  
Required: No

 ** volumeType **   <a name="bedrockagentcorecontrol-Type-EphemeralEBSVolumeConfiguration-volumeType"></a>
The Amazon EBS volume type. If you do not specify a type, the default is `gp3`.  
Type: String  
Valid Values: `standard | io1 | io2 | gp2 | sc1 | st1 | gp3`   
Required: No

## See Also
<a name="API_EphemeralEBSVolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/EphemeralEBSVolumeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/EphemeralEBSVolumeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/EphemeralEBSVolumeConfiguration) 
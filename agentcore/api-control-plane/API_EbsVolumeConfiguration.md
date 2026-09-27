---
title: EbsVolumeConfiguration
description: The configuration for an Amazon EBS-backed persistent volume. The service creates persistent volumes when a session first launches, and the volumes survive instance termination. The volumes persist until you delete the session.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_EbsVolumeConfiguration.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# EbsVolumeConfiguration
<a name="API_EbsVolumeConfiguration"></a>

The configuration for an Amazon EBS-backed persistent volume. The service creates persistent volumes when a session first launches, and the volumes survive instance termination. The volumes persist until you delete the session.

## Contents
<a name="API_EbsVolumeConfiguration_Contents"></a>

 ** name **   <a name="bedrockagentcorecontrol-Type-EbsVolumeConfiguration-name"></a>
The logical name of the volume. Use this name to reference the volume when you mount it into an agent runtime.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[a-zA-Z][a-zA-Z0-9_-]{0,47}`   
Required: Yes

 ** sizeGiB **   <a name="bedrockagentcorecontrol-Type-EbsVolumeConfiguration-sizeGiB"></a>
The size of the volume, in GiB.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 65536.  
Required: Yes

 ** encrypted **   <a name="bedrockagentcorecontrol-Type-EbsVolumeConfiguration-encrypted"></a>
Specifies whether to encrypt the volume. If `true`, the service encrypts the volume with the AWS KMS key that you specify in `kmsKeyId`, or the default AWS KMS key for Amazon EBS if you do not specify one. The default is `true`.  
Type: Boolean  
Required: No

 ** iops **   <a name="bedrockagentcorecontrol-Type-EbsVolumeConfiguration-iops"></a>
The number of IOPS to provision. Valid only for `gp3`, `io1`, and `io2` volumes.  
Type: Integer  
Valid Range: Minimum value of 100. Maximum value of 256000.  
Required: No

 ** kmsKeyId **   <a name="bedrockagentcorecontrol-Type-EbsVolumeConfiguration-kmsKeyId"></a>
The identifier of the AWS KMS key to use for encryption.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:kms:[a-z0-9-]+:[0-9]{12}:key/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`   
Required: No

 ** snapshotId **   <a name="bedrockagentcorecontrol-Type-EbsVolumeConfiguration-snapshotId"></a>
An optional Amazon EBS snapshot ID. If provided, the volume is initialized from this snapshot the first time it is created. On subsequent restarts, the existing volume is used and the snapshot is ignored.  
Type: String  
Length Constraints: Minimum length of 13. Maximum length of 64.  
Pattern: `snap-[a-f0-9]{8,17}`   
Required: No

 ** throughput **   <a name="bedrockagentcorecontrol-Type-EbsVolumeConfiguration-throughput"></a>
The throughput, in MiB/s. Valid only for `gp3` volumes.  
Type: Integer  
Valid Range: Minimum value of 125. Maximum value of 2000.  
Required: No

 ** volumeType **   <a name="bedrockagentcorecontrol-Type-EbsVolumeConfiguration-volumeType"></a>
The Amazon EBS volume type. If you do not specify a type, the default is `gp3`.  
Type: String  
Valid Values: `standard | io1 | io2 | gp2 | sc1 | st1 | gp3`   
Required: No

## See Also
<a name="API_EbsVolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/EbsVolumeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/EbsVolumeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/EbsVolumeConfiguration) 
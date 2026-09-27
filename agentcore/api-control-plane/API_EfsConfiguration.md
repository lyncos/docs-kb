---
title: EfsConfiguration
description: The configuration for mounting an Amazon Elastic File System (Amazon EFS) access point that you own into a session.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_EfsConfiguration.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# EfsConfiguration
<a name="API_EfsConfiguration"></a>

The configuration for mounting an Amazon Elastic File System (Amazon EFS) access point that you own into a session.

## Contents
<a name="API_EfsConfiguration_Contents"></a>

 ** accessPointArn **   <a name="bedrockagentcorecontrol-Type-EfsConfiguration-accessPointArn"></a>
The Amazon Resource Name (ARN) of the Amazon Elastic File System (Amazon EFS) access point to mount.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:access-point/fsap-[0-9a-f]{8,40}`   
Required: Yes

 ** fileSystemArn **   <a name="bedrockagentcorecontrol-Type-EfsConfiguration-fileSystemArn"></a>
The Amazon Resource Name (ARN) of the Amazon Elastic File System (Amazon EFS) file system that owns the access point.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `arn:aws[-a-z]*:elasticfilesystem:[a-z0-9-]+:[0-9]{12}:file-system/fs-[0-9a-f]{8,40}`   
Required: Yes

 ** mountPath **   <a name="bedrockagentcorecontrol-Type-EfsConfiguration-mountPath"></a>
The absolute path within the session at which the access point is mounted, for example `/mnt/efs`. Each mount path must be unique across all file system configurations in the session.  
Type: String  
Length Constraints: Minimum length of 6. Maximum length of 200.  
Pattern: `/mnt/[a-zA-Z0-9._-]+/?`   
Required: Yes

## See Also
<a name="API_EfsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/EfsConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/EfsConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/EfsConfiguration) 
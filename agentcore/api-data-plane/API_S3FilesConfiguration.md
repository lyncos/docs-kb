---
title: S3FilesConfiguration
description: The configuration for mounting an Amazon Simple Storage Service (Amazon S3) Files access point that you own into a session.
product: Amazon Bedrock AgentCore
section: Data Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_S3FilesConfiguration.html
fetched: '2026-09-26'
tags:
- agentcore
- data-plane-api
---

# S3FilesConfiguration
<a name="API_S3FilesConfiguration"></a>

The configuration for mounting an Amazon Simple Storage Service (Amazon S3) Files access point that you own into a session.

## Contents
<a name="API_S3FilesConfiguration_Contents"></a>

 ** accessPointArn **   <a name="BedrockAgentCore-Type-S3FilesConfiguration-accessPointArn"></a>
The Amazon Resource Name (ARN) of the Amazon Simple Storage Service (Amazon S3) Files access point to mount.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}/access-point/fsap-[0-9a-f]{17,40}`   
Required: Yes

 ** fileSystemArn **   <a name="BedrockAgentCore-Type-S3FilesConfiguration-fileSystemArn"></a>
The Amazon Resource Name (ARN) of the Amazon Simple Storage Service (Amazon S3) Files file system that owns the access point.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Pattern: `arn:aws[-a-z]*:s3files:[a-z0-9-]+:[0-9]{12}:file-system/fs-[0-9a-f]{17,40}`   
Required: Yes

 ** mountPath **   <a name="BedrockAgentCore-Type-S3FilesConfiguration-mountPath"></a>
The absolute path within the session at which the access point is mounted, for example `/mnt/s3data`. Each mount path must be unique across all file system configurations in the session.  
Type: String  
Length Constraints: Minimum length of 6. Maximum length of 200.  
Pattern: `/mnt/[a-zA-Z0-9._-]+/?`   
Required: Yes

## See Also
<a name="API_S3FilesConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/S3FilesConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/S3FilesConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/S3FilesConfiguration) 
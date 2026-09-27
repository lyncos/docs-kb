---
title: ToolsFileSystemConfiguration
description: 'Specifies a file system to mount into the session by providing exactly one of the following: + `s3FilesConfiguration` - Mounts an Amazon Simple Storage Service (Amazon S3) Files access point. + `efsConfiguration` - Mounts an Amazon Elastic File System (Amazon EFS) access point.'
product: Amazon Bedrock AgentCore
section: Data Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ToolsFileSystemConfiguration.html
fetched: '2026-09-26'
tags:
- agentcore
- data-plane-api
---

# ToolsFileSystemConfiguration
<a name="API_ToolsFileSystemConfiguration"></a>

Specifies a file system to mount into the session by providing exactly one of the following:
+  `s3FilesConfiguration` - Mounts an Amazon Simple Storage Service (Amazon S3) Files access point.
+  `efsConfiguration` - Mounts an Amazon Elastic File System (Amazon EFS) access point.

## Contents
<a name="API_ToolsFileSystemConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** efsConfiguration **   <a name="BedrockAgentCore-Type-ToolsFileSystemConfiguration-efsConfiguration"></a>
The configuration for mounting your own Amazon Elastic File System (Amazon EFS) access point into the session.  
Type: [EfsConfiguration](API_EfsConfiguration.md) object  
Required: No

 ** s3FilesConfiguration **   <a name="BedrockAgentCore-Type-ToolsFileSystemConfiguration-s3FilesConfiguration"></a>
The configuration for mounting your own Amazon Simple Storage Service (Amazon S3) Files access point into the session.  
Type: [S3FilesConfiguration](API_S3FilesConfiguration.md) object  
Required: No

## See Also
<a name="API_ToolsFileSystemConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ToolsFileSystemConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ToolsFileSystemConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ToolsFileSystemConfiguration) 
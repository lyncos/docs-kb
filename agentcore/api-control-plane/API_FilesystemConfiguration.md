---
title: FilesystemConfiguration
description: Configuration for a filesystem that can be mounted into the AgentCore Runtime.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_FilesystemConfiguration.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# FilesystemConfiguration
<a name="API_FilesystemConfiguration"></a>

Configuration for a filesystem that can be mounted into the AgentCore Runtime.

## Contents
<a name="API_FilesystemConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** capacityProviderVolume **   <a name="bedrockagentcorecontrol-Type-FilesystemConfiguration-capacityProviderVolume"></a>
Configuration for a capacity provider volume to mount into the AgentCore Runtime. This mounts a persistent volume that is defined on the capacity provider, referenced by its logical name.  
Type: [CapacityProviderVolumeConfiguration](API_CapacityProviderVolumeConfiguration.md) object  
Required: No

 ** efsAccessPoint **   <a name="bedrockagentcorecontrol-Type-FilesystemConfiguration-efsAccessPoint"></a>
Configuration for an Amazon EFS access point to mount into the AgentCore Runtime.  
Type: [EfsAccessPointConfiguration](API_EfsAccessPointConfiguration.md) object  
Required: No

 ** s3FilesAccessPoint **   <a name="bedrockagentcorecontrol-Type-FilesystemConfiguration-s3FilesAccessPoint"></a>
Configuration for an Amazon S3 Files access point to mount into the AgentCore Runtime.  
Type: [S3FilesAccessPointConfiguration](API_S3FilesAccessPointConfiguration.md) object  
Required: No

 ** sessionStorage **   <a name="bedrockagentcorecontrol-Type-FilesystemConfiguration-sessionStorage"></a>
Configuration for session storage. Session storage provides persistent storage that is preserved across AgentCore Runtime session invocations.  
Type: [SessionStorageConfiguration](API_SessionStorageConfiguration.md) object  
Required: No

## See Also
<a name="API_FilesystemConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/FilesystemConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/FilesystemConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/FilesystemConfiguration) 
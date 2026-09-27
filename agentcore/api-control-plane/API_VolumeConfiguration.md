---
title: VolumeConfiguration
description: The configuration for a persistent volume attached to a capacity provider. This structure defines the storage backing for the persistent volumes used by agents that run on capacity provider instances.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_VolumeConfiguration.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# VolumeConfiguration
<a name="API_VolumeConfiguration"></a>

The configuration for a persistent volume attached to a capacity provider. This structure defines the storage backing for the persistent volumes used by agents that run on capacity provider instances.

## Contents
<a name="API_VolumeConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** ebsConfiguration **   <a name="bedrockagentcorecontrol-Type-VolumeConfiguration-ebsConfiguration"></a>
The configuration for an Amazon EBS-backed persistent volume.  
Type: [EbsVolumeConfiguration](API_EbsVolumeConfiguration.md) object  
Required: No

## See Also
<a name="API_VolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/VolumeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/VolumeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/VolumeConfiguration) 
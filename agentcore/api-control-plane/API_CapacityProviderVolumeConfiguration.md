---
title: CapacityProviderVolumeConfiguration
description: Configuration for a capacity provider volume mounted into the AgentCore Runtime. This references a persistent volume by its logical name, as defined in the capacity provider's list of volumes.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CapacityProviderVolumeConfiguration.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# CapacityProviderVolumeConfiguration
<a name="API_CapacityProviderVolumeConfiguration"></a>

Configuration for a capacity provider volume mounted into the AgentCore Runtime. This references a persistent volume by its logical name, as defined in the capacity provider's list of volumes.

## Contents
<a name="API_CapacityProviderVolumeConfiguration_Contents"></a>

 ** mountPath **   <a name="bedrockagentcorecontrol-Type-CapacityProviderVolumeConfiguration-mountPath"></a>
The mount path for the capacity provider volume inside the AgentCore Runtime. The path must be under `/mnt` with exactly one subdirectory level (for example, `/mnt/data`).  
Type: String  
Length Constraints: Minimum length of 6. Maximum length of 200.  
Pattern: `/mnt/[a-zA-Z0-9._-]+/?`   
Required: Yes

 ** volumeName **   <a name="bedrockagentcorecontrol-Type-CapacityProviderVolumeConfiguration-volumeName"></a>
The logical name of the capacity provider volume to mount. This name must match a volume that is defined in the capacity provider's list of volumes.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[a-zA-Z][a-zA-Z0-9_-]{0,47}`   
Required: Yes

## See Also
<a name="API_CapacityProviderVolumeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CapacityProviderVolumeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CapacityProviderVolumeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CapacityProviderVolumeConfiguration) 
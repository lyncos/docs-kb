---
title: UpdatedAutoDetectionConfiguration
description: 'A wrapper for updating the auto-detection configuration of a registry with PATCH semantics. Include this wrapper to replace the auto-detection configuration with the specified value. Omit it to leave the auto-detection configuration unchanged. To clear the configuration, include '
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_UpdatedAutoDetectionConfiguration.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# UpdatedAutoDetectionConfiguration
<a name="API_UpdatedAutoDetectionConfiguration"></a>

A wrapper for updating the auto-detection configuration of a registry with PATCH semantics. Include this wrapper to replace the auto-detection configuration with the specified value. Omit it to leave the auto-detection configuration unchanged. To clear the configuration, include the wrapper with a null `optionalValue`.

## Contents
<a name="API_UpdatedAutoDetectionConfiguration_Contents"></a>

 ** optionalValue **   <a name="agentregistrycontrol-Type-UpdatedAutoDetectionConfiguration-optionalValue"></a>
The value to set for this field. Omit the wrapper to leave the field unchanged.  
Type: [AutoDetectionConfiguration](API_AutoDetectionConfiguration.md) object  
Required: No

## See Also
<a name="API_UpdatedAutoDetectionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedAutoDetectionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedAutoDetectionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedAutoDetectionConfiguration) 
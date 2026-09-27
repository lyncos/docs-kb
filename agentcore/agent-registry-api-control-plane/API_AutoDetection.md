---
title: AutoDetection
description: The auto-detection properties for a registry, including the requested configuration and the current detection status. When auto-detection is enabled and the scope preconditions are met, the registry is automatically populated with discovered resources.
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_AutoDetection.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# AutoDetection
<a name="API_AutoDetection"></a>

The auto-detection properties for a registry, including the requested configuration and the current detection status. When auto-detection is enabled and the scope preconditions are met, the registry is automatically populated with discovered resources.

## Contents
<a name="API_AutoDetection_Contents"></a>

 ** configuration **   <a name="agentregistrycontrol-Type-AutoDetection-configuration"></a>
The auto-detection settings that control how resources are discovered for the registry.  
Type: [AutoDetectionConfiguration](API_AutoDetectionConfiguration.md) object  
Required: Yes

 ** status **   <a name="agentregistrycontrol-Type-AutoDetection-status"></a>
The current auto-detection status. `ACTIVE` indicates that the registry is actively being populated with detected resources. `INACTIVE` indicates that the preconditions required at the configured scope are not currently met.  
Type: String  
Valid Values: `ACTIVE | INACTIVE`   
Required: Yes

 ** statusReason **   <a name="agentregistrycontrol-Type-AutoDetection-statusReason"></a>
A human-readable explanation of the current auto-detection status. Typically populated when the status requires additional context.  
Type: String  
Required: No

## See Also
<a name="API_AutoDetection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/AutoDetection) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/AutoDetection) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/AutoDetection) 
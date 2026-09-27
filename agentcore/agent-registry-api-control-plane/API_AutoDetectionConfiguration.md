---
title: AutoDetectionConfiguration
description: The customer-defined auto-detection settings for a registry.
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_AutoDetectionConfiguration.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# AutoDetectionConfiguration
<a name="API_AutoDetectionConfiguration"></a>

The customer-defined auto-detection settings for a registry.

## Contents
<a name="API_AutoDetectionConfiguration_Contents"></a>

 ** enabled **   <a name="agentregistrycontrol-Type-AutoDetectionConfiguration-enabled"></a>
Specifies whether auto-detection is requested for the registry. Setting this to `true` is necessary but not sufficient for auto-detection to become active; the preconditions of the configured scope must also be met.  
Type: Boolean  
Required: Yes

 ** scope **   <a name="agentregistrycontrol-Type-AutoDetectionConfiguration-scope"></a>
The source from which resources are detected. For example, `ORGANIZATION` sources resources from all member accounts of an AWS organization.  
Type: String  
Valid Values: `ORGANIZATION`   
Required: Yes

## See Also
<a name="API_AutoDetectionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/AutoDetectionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/AutoDetectionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/AutoDetectionConfiguration) 
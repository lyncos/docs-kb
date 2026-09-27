---
title: RegistrySummary
description: Registry summary for list operations
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_RegistrySummary.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# RegistrySummary
<a name="API_RegistrySummary"></a>

Registry summary for list operations

## Contents
<a name="API_RegistrySummary_Contents"></a>

 ** createdAt **   <a name="agentregistrycontrol-Type-RegistrySummary-createdAt"></a>
The timestamp when the registry was created  
Type: Timestamp  
Required: Yes

 ** name **   <a name="agentregistrycontrol-Type-RegistrySummary-name"></a>
Registry name  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`   
Required: Yes

 ** registryArn **   <a name="agentregistrycontrol-Type-RegistrySummary-registryArn"></a>
Registry Amazon Resource Name  
Type: String  
Length Constraints: Minimum length of 46. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}`   
Required: Yes

 ** registryId **   <a name="agentregistrycontrol-Type-RegistrySummary-registryId"></a>
Unique registry identifier  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 16.  
Pattern: `[a-zA-Z0-9]{12,16}`   
Required: Yes

 ** status **   <a name="agentregistrycontrol-Type-RegistrySummary-status"></a>
Current status of the registry  
Type: String  
Valid Values: `CREATING | READY | UPDATING | CREATE_FAILED | UPDATE_FAILED | DELETING | DELETE_FAILED`   
Required: Yes

 ** updatedAt **   <a name="agentregistrycontrol-Type-RegistrySummary-updatedAt"></a>
The timestamp when the registry was last updated  
Type: Timestamp  
Required: Yes

 ** autoDetection **   <a name="agentregistrycontrol-Type-RegistrySummary-autoDetection"></a>
The registry's auto-detection properties, including the requested configuration and the current detection status. Present only when auto-detection was configured for the registry.  
Type: [AutoDetection](API_AutoDetection.md) object  
Required: No

 ** description **   <a name="agentregistrycontrol-Type-RegistrySummary-description"></a>
Registry description  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** discoveryConfiguration **   <a name="agentregistrycontrol-Type-RegistrySummary-discoveryConfiguration"></a>
Discovery configuration for the registry  
Type: [DiscoveryConfiguration](API_DiscoveryConfiguration.md) object  
Required: No

 ** statusReason **   <a name="agentregistrycontrol-Type-RegistrySummary-statusReason"></a>
The reason for the current status. Typically populated when the status indicates a failure state.  
Type: String  
Required: No

## See Also
<a name="API_RegistrySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/RegistrySummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/RegistrySummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/RegistrySummary) 
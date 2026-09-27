---
title: AgentSkillsDefinitionDescriptor
description: Descriptor that defines an agent skills registry record and its associated content.
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_AgentSkillsDefinitionDescriptor.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# AgentSkillsDefinitionDescriptor
<a name="API_AgentSkillsDefinitionDescriptor"></a>

Descriptor that defines an agent skills registry record and its associated content.

## Contents
<a name="API_AgentSkillsDefinitionDescriptor_Contents"></a>

 ** additionalData **   <a name="agentregistrycontrol-Type-AgentSkillsDefinitionDescriptor-additionalData"></a>
Additional data associated with the agent skills definition descriptor.  
Type: [AgentSkillsAdditionalData](API_AgentSkillsAdditionalData.md) object  
Required: No

 ** data **   <a name="agentregistrycontrol-Type-AgentSkillsDefinitionDescriptor-data"></a>
The agent skills definition content, serialized as descriptor payload data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 102400.  
Required: No

 ** dataSchemaVersion **   <a name="agentregistrycontrol-Type-AgentSkillsDefinitionDescriptor-dataSchemaVersion"></a>
The schema version of the descriptor payload.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

## See Also
<a name="API_AgentSkillsDefinitionDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/AgentSkillsDefinitionDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/AgentSkillsDefinitionDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/AgentSkillsDefinitionDescriptor) 
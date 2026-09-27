---
title: AgentSkillsMdDescriptor
description: Markdown-format descriptor containing an agent skills document.
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_AgentSkillsMdDescriptor.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# AgentSkillsMdDescriptor
<a name="API_AgentSkillsMdDescriptor"></a>

Markdown-format descriptor containing an agent skills document.

## Contents
<a name="API_AgentSkillsMdDescriptor_Contents"></a>

 ** data **   <a name="agentregistrycontrol-Type-AgentSkillsMdDescriptor-data"></a>
The agent skills markdown content, serialized as descriptor payload data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 102400.  
Required: No

 ** dataSchemaVersion **   <a name="agentregistrycontrol-Type-AgentSkillsMdDescriptor-dataSchemaVersion"></a>
The schema version of the descriptor payload.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** source **   <a name="agentregistrycontrol-Type-AgentSkillsMdDescriptor-source"></a>
The optional source configuration used to synchronize the agent skills markdown content.  
Type: [DescriptorSource](API_DescriptorSource.md) object  
Required: No

## See Also
<a name="API_AgentSkillsMdDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/AgentSkillsMdDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/AgentSkillsMdDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/AgentSkillsMdDescriptor) 
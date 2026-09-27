---
title: Descriptors
description: The typed set of descriptors for a registry record. Exactly one descriptor field is populated based on the record type.
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_Descriptors.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# Descriptors
<a name="API_Descriptors"></a>

The typed set of descriptors for a registry record. Exactly one descriptor field is populated based on the record type.

## Contents
<a name="API_Descriptors_Contents"></a>

 ** a2aAgentCard **   <a name="agentregistrycontrol-Type-Descriptors-a2aAgentCard"></a>
The A2A agent card descriptor, populated when the record type is AGENT.  
Type: [A2aAgentCardDescriptor](API_A2aAgentCardDescriptor.md) object  
Required: No

 ** agentSkillsDefinition **   <a name="agentregistrycontrol-Type-Descriptors-agentSkillsDefinition"></a>
The agent skills definition descriptor, populated when the record type is SKILL.  
Type: [AgentSkillsDefinitionDescriptor](API_AgentSkillsDefinitionDescriptor.md) object  
Required: No

 ** agui **   <a name="agentregistrycontrol-Type-Descriptors-agui"></a>
The AG-UI descriptor, populated for records detected from an AG-UI protocol source.  
Type: [AgUiDescriptor](API_AgUiDescriptor.md) object  
Required: No

 ** custom **   <a name="agentregistrycontrol-Type-Descriptors-custom"></a>
The custom descriptor, populated when the record type is CUSTOM.  
Type: [CustomDescriptor](API_CustomDescriptor.md) object  
Required: No

 ** http **   <a name="agentregistrycontrol-Type-Descriptors-http"></a>
The HTTP descriptor, populated for records detected from an HTTP protocol source.  
Type: [HttpDescriptor](API_HttpDescriptor.md) object  
Required: No

 ** mcpServer **   <a name="agentregistrycontrol-Type-Descriptors-mcpServer"></a>
The MCP server descriptor, populated when the record type is MCP.  
Type: [McpServerDescriptor](API_McpServerDescriptor.md) object  
Required: No

## See Also
<a name="API_Descriptors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/Descriptors) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/Descriptors) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/Descriptors) 
---
title: UpdatedDescriptorsFields
description: The patchable descriptor fields applied during an UpdateRegistryRecord call. Each field is independently patchable.
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_UpdatedDescriptorsFields.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# UpdatedDescriptorsFields
<a name="API_UpdatedDescriptorsFields"></a>

The patchable descriptor fields applied during an UpdateRegistryRecord call. Each field is independently patchable.

## Contents
<a name="API_UpdatedDescriptorsFields_Contents"></a>

 ** a2aAgentCard **   <a name="agentregistrycontrol-Type-UpdatedDescriptorsFields-a2aAgentCard"></a>
The patch for the A2A agent card descriptor.  
Type: [UpdatedA2aAgentCardDescriptor](API_UpdatedA2aAgentCardDescriptor.md) object  
Required: No

 ** agentSkillsDefinition **   <a name="agentregistrycontrol-Type-UpdatedDescriptorsFields-agentSkillsDefinition"></a>
The patch for the agent skills definition descriptor.  
Type: [UpdatedAgentSkillsDefinitionDescriptor](API_UpdatedAgentSkillsDefinitionDescriptor.md) object  
Required: No

 ** agui **   <a name="agentregistrycontrol-Type-UpdatedDescriptorsFields-agui"></a>
The patch for the AG-UI descriptor.  
Type: [UpdatedAgUiDescriptor](API_UpdatedAgUiDescriptor.md) object  
Required: No

 ** custom **   <a name="agentregistrycontrol-Type-UpdatedDescriptorsFields-custom"></a>
The patch for the custom descriptor.  
Type: [UpdatedCustomDescriptor](API_UpdatedCustomDescriptor.md) object  
Required: No

 ** http **   <a name="agentregistrycontrol-Type-UpdatedDescriptorsFields-http"></a>
The patch for the HTTP descriptor.  
Type: [UpdatedHttpDescriptor](API_UpdatedHttpDescriptor.md) object  
Required: No

 ** mcpServer **   <a name="agentregistrycontrol-Type-UpdatedDescriptorsFields-mcpServer"></a>
The patch for the MCP server descriptor.  
Type: [UpdatedMcpServerDescriptor](API_UpdatedMcpServerDescriptor.md) object  
Required: No

## See Also
<a name="API_UpdatedDescriptorsFields_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedDescriptorsFields) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedDescriptorsFields) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedDescriptorsFields) 
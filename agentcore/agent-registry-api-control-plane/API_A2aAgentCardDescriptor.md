---
title: A2aAgentCardDescriptor
description: Descriptor that defines the content of an A2A (Agent-to-Agent) agent card registry record. The content is validated against the A2A protocol schema.
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_A2aAgentCardDescriptor.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# A2aAgentCardDescriptor
<a name="API_A2aAgentCardDescriptor"></a>

Descriptor that defines the content of an A2A (Agent-to-Agent) agent card registry record. The content is validated against the A2A protocol schema.

## Contents
<a name="API_A2aAgentCardDescriptor_Contents"></a>

 ** data **   <a name="agentregistrycontrol-Type-A2aAgentCardDescriptor-data"></a>
The A2A agent card content, serialized as descriptor payload data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 102400.  
Required: No

 ** dataSchemaVersion **   <a name="agentregistrycontrol-Type-A2aAgentCardDescriptor-dataSchemaVersion"></a>
The schema version of the descriptor payload.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** source **   <a name="agentregistrycontrol-Type-A2aAgentCardDescriptor-source"></a>
The optional source configuration used to synchronize the A2A agent card descriptor content.  
Type: [DescriptorSource](API_DescriptorSource.md) object  
Required: No

## See Also
<a name="API_A2aAgentCardDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/A2aAgentCardDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/A2aAgentCardDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/A2aAgentCardDescriptor) 
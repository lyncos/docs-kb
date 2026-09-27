---
title: SourceDetails
description: The details about the upstream source from which a registry record was detected. Exactly one member is populated, corresponding to the source type.
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_SourceDetails.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# SourceDetails
<a name="API_SourceDetails"></a>

The details about the upstream source from which a registry record was detected. Exactly one member is populated, corresponding to the source type.

## Contents
<a name="API_SourceDetails_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** agentcoreGateway **   <a name="agentregistrycontrol-Type-SourceDetails-agentcoreGateway"></a>
The source details for a registry record that was auto-detected from an Amazon Bedrock AgentCore Gateway resource. Populated when the source type is `AWS::BedrockAgentCore::Gateway`.  
Type: [AgentCoreGatewaySourceDetails](API_AgentCoreGatewaySourceDetails.md) object  
Required: No

 ** agentcoreRuntime **   <a name="agentregistrycontrol-Type-SourceDetails-agentcoreRuntime"></a>
The source details for a registry record that was auto-detected from an Amazon Bedrock AgentCore Runtime resource. Populated when the source type is `AWS::BedrockAgentCore::Runtime`.  
Type: [AgentCoreRuntimeSourceDetails](API_AgentCoreRuntimeSourceDetails.md) object  
Required: No

## See Also
<a name="API_SourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/SourceDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/SourceDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/SourceDetails) 
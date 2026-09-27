---
title: Provenance
description: A provenance entry that describes the lineage of a registry record. Records that were auto-detected by AWS Agent Registry carry a provenance entry that links the record back to its upstream source.
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_Provenance.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# Provenance
<a name="API_Provenance"></a>

A provenance entry that describes the lineage of a registry record. Records that were auto-detected by AWS Agent Registry carry a provenance entry that links the record back to its upstream source.

## Contents
<a name="API_Provenance_Contents"></a>

 ** relation **   <a name="agentregistrycontrol-Type-Provenance-relation"></a>
The relationship between the registry record and its upstream source. `DETECTED_FROM` indicates that the record was auto-detected from the source resource.  
Type: String  
Valid Values: `DETECTED_FROM`   
Required: Yes

 ** sourceId **   <a name="agentregistrycontrol-Type-Provenance-sourceId"></a>
The identifier of the upstream source that the registry record was detected from.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:[a-zA-Z0-9-]+:[a-z0-9-]*:[0-9]{12}:.+`   
Required: Yes

 ** sourceDetails **   <a name="agentregistrycontrol-Type-Provenance-sourceDetails"></a>
Additional details about the upstream source that the registry record was detected from, such as the AgentCore Gateway or Runtime configuration. The populated member corresponds to the source type.  
Type: [SourceDetails](API_SourceDetails.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** sourceType **   <a name="agentregistrycontrol-Type-Provenance-sourceType"></a>
The type of the upstream source that the registry record was detected from.  
Type: String  
Valid Values: `AWS::BedrockAgentCore::Runtime | AWS::BedrockAgentCore::Gateway`   
Required: No

## See Also
<a name="API_Provenance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/Provenance) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/Provenance) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/Provenance) 
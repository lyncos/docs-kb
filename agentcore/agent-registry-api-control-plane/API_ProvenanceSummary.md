---
title: ProvenanceSummary
description: A condensed provenance entry surfaced in list results. Contains the source identity of a lineage entry without the source details returned by `GetRegistryRecord`.
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_ProvenanceSummary.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# ProvenanceSummary
<a name="API_ProvenanceSummary"></a>

A condensed provenance entry surfaced in list results. Contains the source identity of a lineage entry without the source details returned by `GetRegistryRecord`.

## Contents
<a name="API_ProvenanceSummary_Contents"></a>

 ** relation **   <a name="agentregistrycontrol-Type-ProvenanceSummary-relation"></a>
The relationship between the registry record and its upstream source. `DETECTED_FROM` indicates that the record was auto-detected from the source resource.  
Type: String  
Valid Values: `DETECTED_FROM`   
Required: Yes

 ** sourceId **   <a name="agentregistrycontrol-Type-ProvenanceSummary-sourceId"></a>
The identifier of the upstream source that the registry record was detected from.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:[a-zA-Z0-9-]+:[a-z0-9-]*:[0-9]{12}:.+`   
Required: Yes

 ** sourceType **   <a name="agentregistrycontrol-Type-ProvenanceSummary-sourceType"></a>
The type of the upstream source that the registry record was detected from.  
Type: String  
Valid Values: `AWS::BedrockAgentCore::Runtime | AWS::BedrockAgentCore::Gateway`   
Required: No

## See Also
<a name="API_ProvenanceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/ProvenanceSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/ProvenanceSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/ProvenanceSummary) 
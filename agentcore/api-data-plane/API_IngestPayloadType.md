---
title: IngestPayloadType
description: A single content payload item to ingest. A payload item contains either conversational or JSON content.
product: Amazon Bedrock AgentCore
section: Data Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_IngestPayloadType.html
fetched: '2026-09-26'
tags:
- agentcore
- data-plane-api
---

# IngestPayloadType
<a name="API_IngestPayloadType"></a>

A single content payload item to ingest. A payload item contains either conversational or JSON content.

## Contents
<a name="API_IngestPayloadType_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** conversational **   <a name="BedrockAgentCore-Type-IngestPayloadType-conversational"></a>
The conversational content for this payload item.  
Type: [Conversational](API_Conversational.md) object  
Required: No

 ** json **   <a name="BedrockAgentCore-Type-IngestPayloadType-json"></a>
The JSON content for this payload item.  
Type: [MemoryJsonData](API_MemoryJsonData.md) object  
Required: No

## See Also
<a name="API_IngestPayloadType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/IngestPayloadType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/IngestPayloadType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/IngestPayloadType) 
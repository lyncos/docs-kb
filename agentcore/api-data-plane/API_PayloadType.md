---
title: PayloadType
description: Contains the payload content for an event.
product: Amazon Bedrock AgentCore
section: Data Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_PayloadType.html
fetched: '2026-09-26'
tags:
- agentcore
- data-plane-api
---

# PayloadType
<a name="API_PayloadType"></a>

Contains the payload content for an event.

## Contents
<a name="API_PayloadType_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** blob **   <a name="BedrockAgentCore-Type-PayloadType-blob"></a>
The binary content of the payload.  
Type: JSON value  
Required: No

 ** conversational **   <a name="BedrockAgentCore-Type-PayloadType-conversational"></a>
The conversational content of the payload.  
Type: [Conversational](API_Conversational.md) object  
Required: No

 ** json **   <a name="BedrockAgentCore-Type-PayloadType-json"></a>
The JSON content of the payload. Use this type to store non-conversational, JSON-formatted data, such as behavioral events, activity logs, or system events.  
Type: [MemoryJsonData](API_MemoryJsonData.md) object  
Required: No

## See Also
<a name="API_PayloadType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/PayloadType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/PayloadType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/PayloadType) 
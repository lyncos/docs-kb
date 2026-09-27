---
title: SessionTraceIds
description: A pairing of a session with the specific trace IDs to evaluate within that session. Use this to evaluate individual traces rather than an entire session.
product: Amazon Bedrock AgentCore
section: Data Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_SessionTraceIds.html
fetched: '2026-09-26'
tags:
- agentcore
- data-plane-api
---

# SessionTraceIds
<a name="API_SessionTraceIds"></a>

A pairing of a session with the specific trace IDs to evaluate within that session. Use this to evaluate individual traces rather than an entire session.

## Contents
<a name="API_SessionTraceIds_Contents"></a>

 ** sessionId **   <a name="BedrockAgentCore-Type-SessionTraceIds-sessionId"></a>
The unique identifier of the session that contains the traces to evaluate.  
Type: String  
Required: Yes

 ** traceIds **   <a name="BedrockAgentCore-Type-SessionTraceIds-traceIds"></a>
The list of trace IDs within the session to evaluate.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Fixed length of 32.  
Required: Yes

## See Also
<a name="API_SessionTraceIds_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/SessionTraceIds) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/SessionTraceIds) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/SessionTraceIds) 
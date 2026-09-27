---
title: NamespaceKeyEntry
description: A namespace variable key definition with optional `NamespaceKeyValidation` rules.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_NamespaceKeyEntry.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# NamespaceKeyEntry
<a name="API_NamespaceKeyEntry"></a>

A namespace variable key definition with optional `NamespaceKeyValidation` rules.

## Contents
<a name="API_NamespaceKeyEntry_Contents"></a>

 ** key **   <a name="bedrockagentcorecontrol-Type-NamespaceKeyEntry-key"></a>
The namespace variable key name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 32.  
Pattern: `(?!memoryStrategyId$|actorId$|sessionId$)[a-z][a-z0-9]*`   
Required: Yes

 ** validation **   <a name="bedrockagentcorecontrol-Type-NamespaceKeyEntry-validation"></a>
The validation rules that constrain values for this namespace variable at runtime (`CreateEvent` API).  
Type: [NamespaceKeyValidation](API_NamespaceKeyValidation.md) object  
Required: No

## See Also
<a name="API_NamespaceKeyEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/NamespaceKeyEntry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/NamespaceKeyEntry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/NamespaceKeyEntry) 
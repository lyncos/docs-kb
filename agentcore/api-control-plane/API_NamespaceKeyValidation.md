---
title: NamespaceKeyValidation
description: The validation rules for namespace variable values. When you specify multiple rules, the service enforces a logical `AND` across all provided key-value pairs.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_NamespaceKeyValidation.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# NamespaceKeyValidation
<a name="API_NamespaceKeyValidation"></a>

The validation rules for namespace variable values. When you specify multiple rules, the service enforces a logical `AND` across all provided key-value pairs.

## Contents
<a name="API_NamespaceKeyValidation_Contents"></a>

 ** allowedValues **   <a name="bedrockagentcorecontrol-Type-NamespaceKeyValidation-allowedValues"></a>
The allowed values for this namespace variable key.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-z0-9][a-z0-9-_]*`   
Required: No

 ** regexPattern **   <a name="bedrockagentcorecontrol-Type-NamespaceKeyValidation-regexPattern"></a>
A regex pattern that the namespace variable key-value must match.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Required: No

## See Also
<a name="API_NamespaceKeyValidation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/NamespaceKeyValidation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/NamespaceKeyValidation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/NamespaceKeyValidation) 
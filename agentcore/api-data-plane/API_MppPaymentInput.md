---
title: MppPaymentInput
description: 'Contains the payment challenge from a 402 Payment Required response. Forward the raw `WWW-Authenticate: Payment` header value verbatim. In response, you receive a payment credential that satisfies the challenge. Provide exactly one challenge per request.'
product: Amazon Bedrock AgentCore
section: Data Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_MppPaymentInput.html
fetched: '2026-09-26'
tags:
- agentcore
- data-plane-api
---

# MppPaymentInput
<a name="API_MppPaymentInput"></a>

Contains the payment challenge from a 402 Payment Required response. Forward the raw `WWW-Authenticate: Payment` header value verbatim. In response, you receive a payment credential that satisfies the challenge. Provide exactly one challenge per request.

## Contents
<a name="API_MppPaymentInput_Contents"></a>

 ** version **   <a name="BedrockAgentCore-Type-MppPaymentInput-version"></a>
The MPP protocol version, for example "1" or "2".  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 10.  
Pattern: `[0-9]+`   
Required: Yes

 ** wwwAuthenticateHeaders **   <a name="BedrockAgentCore-Type-MppPaymentInput-wwwAuthenticateHeaders"></a>
The raw `WWW-Authenticate: Payment` header value from the 402 response, passed verbatim. Provide exactly one entry. The service uses this value to generate the payment credential.  
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 16384.  
Required: Yes

 ** buyerPaysGasFees **   <a name="BedrockAgentCore-Type-MppPaymentInput-buyerPaysGasFees"></a>
Authorizes the service to sign a payment whose blockchain network (gas) fees are charged to your wallet, on top of the payment amount.  
The challenge indicates who sponsors the network fees. When the challenge does not sponsor them, the service signs the payment only if this field is `true`. Otherwise it returns a validation error, so you can decide whether to pay the fees or obtain a challenge that sponsors them.  
Optional. When omitted or `false`, you decline to pay network fees. This field has no effect on challenges that already sponsor the fees.  
Type: Boolean  
Required: No

## See Also
<a name="API_MppPaymentInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MppPaymentInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MppPaymentInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MppPaymentInput) 
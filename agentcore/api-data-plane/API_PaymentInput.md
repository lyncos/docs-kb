---
title: PaymentInput
description: The payment input details, which vary by payment type.
product: Amazon Bedrock AgentCore
section: Data Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_PaymentInput.html
fetched: '2026-09-26'
tags:
- agentcore
- data-plane-api
---

# PaymentInput
<a name="API_PaymentInput"></a>

The payment input details, which vary by payment type.

## Contents
<a name="API_PaymentInput_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cryptoX402 **   <a name="BedrockAgentCore-Type-PaymentInput-cryptoX402"></a>
Input for a crypto X402 payment.  
Type: [CryptoX402PaymentInput](API_CryptoX402PaymentInput.md) object  
Required: No

 ** mpp **   <a name="BedrockAgentCore-Type-PaymentInput-mpp"></a>
Contains the payment challenge from a 402 Payment Required response. Forward the raw `WWW-Authenticate: Payment` header value verbatim. In response, you receive a payment credential that satisfies the challenge. Provide exactly one challenge per request.  
Type: [MppPaymentInput](API_MppPaymentInput.md) object  
Required: No

## See Also
<a name="API_PaymentInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/PaymentInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/PaymentInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/PaymentInput) 
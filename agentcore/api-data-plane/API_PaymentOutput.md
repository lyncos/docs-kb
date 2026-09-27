---
title: PaymentOutput
description: The payment output details, which vary by payment type.
product: Amazon Bedrock AgentCore
section: Data Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_PaymentOutput.html
fetched: '2026-09-26'
tags:
- agentcore
- data-plane-api
---

# PaymentOutput
<a name="API_PaymentOutput"></a>

The payment output details, which vary by payment type.

## Contents
<a name="API_PaymentOutput_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cryptoX402 **   <a name="BedrockAgentCore-Type-PaymentOutput-cryptoX402"></a>
Output from a crypto X402 payment.  
Type: [CryptoX402PaymentOutput](API_CryptoX402PaymentOutput.md) object  
Required: No

 ** mpp **   <a name="BedrockAgentCore-Type-PaymentOutput-mpp"></a>
Contains the payment credential, ready to retry the request.  
Type: [MppPaymentOutput](API_MppPaymentOutput.md) object  
Required: No

## See Also
<a name="API_PaymentOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/PaymentOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/PaymentOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/PaymentOutput) 
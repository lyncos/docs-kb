---
title: CryptoX402PaymentInput
description: The input for a crypto X402 payment.
product: Amazon Bedrock AgentCore
section: Data Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_CryptoX402PaymentInput.html
fetched: '2026-09-26'
tags:
- agentcore
- data-plane-api
---

# CryptoX402PaymentInput
<a name="API_CryptoX402PaymentInput"></a>

The input for a crypto X402 payment.

## Contents
<a name="API_CryptoX402PaymentInput_Contents"></a>

 ** payload **   <a name="BedrockAgentCore-Type-CryptoX402PaymentInput-payload"></a>
The X402 payment payload.  
Type: JSON value  
Required: Yes

 ** version **   <a name="BedrockAgentCore-Type-CryptoX402PaymentInput-version"></a>
The version of the X402 protocol.  
Type: String  
Required: Yes

 ** permit2AllowanceLimit **   <a name="BedrockAgentCore-Type-CryptoX402PaymentInput-permit2AllowanceLimit"></a>
The maximum on-chain Permit2 allowance to grant before signing the payment authorization, in the asset's smallest denomination. This field is valid only for the `upto` (metered) scheme; supplying it for the `exact` scheme returns a validation error.  
When set, the service approves an ERC-20 allowance for this amount before processing the payment. The approval sets, rather than adds to, the wallet's allowance. Set this field only when the wallet needs approving, for example on its first `upto` payment, to avoid a redundant on-chain transaction. Omit the field to skip allowance handling. This is the default, and the only behavior for the `exact` scheme.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 78.  
Pattern: `[0-9]+`   
Required: No

## See Also
<a name="API_CryptoX402PaymentInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/CryptoX402PaymentInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/CryptoX402PaymentInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/CryptoX402PaymentInput) 
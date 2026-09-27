---
title: MppPaymentOutput
description: Contains the payment credential, ready to retry the request.
product: Amazon Bedrock AgentCore
section: Data Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_MppPaymentOutput.html
fetched: '2026-09-26'
tags:
- agentcore
- data-plane-api
---

# MppPaymentOutput
<a name="API_MppPaymentOutput"></a>

Contains the payment credential, ready to retry the request.

## Contents
<a name="API_MppPaymentOutput_Contents"></a>

 ** paymentCredential **   <a name="BedrockAgentCore-Type-MppPaymentOutput-paymentCredential"></a>
Ready-to-send value for the `Authorization` header, in the form "Payment <base64url-token>". Attach this header and retry the original request. To inspect the full credential, base64url-decode the token.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 32768.  
Required: Yes

 ** selectedPaymentId **   <a name="BedrockAgentCore-Type-MppPaymentOutput-selectedPaymentId"></a>
The id of the challenge that was paid, echoed from the input challenge so you can correlate the result without decoding the credential.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 512.  
Required: Yes

 ** version **   <a name="BedrockAgentCore-Type-MppPaymentOutput-version"></a>
The MPP protocol version, for example "1" or "2".  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 10.  
Pattern: `[0-9]+`   
Required: Yes

## See Also
<a name="API_MppPaymentOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/MppPaymentOutput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/MppPaymentOutput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/MppPaymentOutput) 
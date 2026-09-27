---
title: PrivateKeySource
description: Contains the private key source configuration for a JWT client assertion.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_PrivateKeySource.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# PrivateKeySource
<a name="API_PrivateKeySource"></a>

Contains the private key source configuration for a JWT client assertion.

## Contents
<a name="API_PrivateKeySource_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** kmsKeySource **   <a name="bedrockagentcorecontrol-Type-PrivateKeySource-kmsKeySource"></a>
The AWS KMS key source for the JWT client assertion.  
Type: [KmsKeySourceType](API_KmsKeySourceType.md) object  
Required: No

## See Also
<a name="API_PrivateKeySource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/PrivateKeySource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/PrivateKeySource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/PrivateKeySource) 
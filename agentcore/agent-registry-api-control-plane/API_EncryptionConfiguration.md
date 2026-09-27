---
title: EncryptionConfiguration
description: The server-side encryption configuration for a registry. Specifies a customer-managed AWS KMS key used to encrypt the registry's content.
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_EncryptionConfiguration.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# EncryptionConfiguration
<a name="API_EncryptionConfiguration"></a>

The server-side encryption configuration for a registry. Specifies a customer-managed AWS KMS key used to encrypt the registry's content.

## Contents
<a name="API_EncryptionConfiguration_Contents"></a>

 ** kmsKeyArn **   <a name="agentregistrycontrol-Type-EncryptionConfiguration-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the customer-managed AWS KMS key used to encrypt the registry's content. The key must be a symmetric encryption key in the same AWS account and Region as the registry.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: Yes

## See Also
<a name="API_EncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/EncryptionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/EncryptionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/EncryptionConfiguration) 
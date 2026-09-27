---
title: RegistryRecordIamCredentialProvider
description: The configuration for an IAM role credential provider that signs requests to a registry record's source with AWS Signature Version 4 (SigV4).
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_RegistryRecordIamCredentialProvider.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# RegistryRecordIamCredentialProvider
<a name="API_RegistryRecordIamCredentialProvider"></a>

The configuration for an IAM role credential provider that signs requests to a registry record's source with AWS Signature Version 4 (SigV4).

## Contents
<a name="API_RegistryRecordIamCredentialProvider_Contents"></a>

 ** region **   <a name="agentregistrycontrol-Type-RegistryRecordIamCredentialProvider-region"></a>
The AWS Region to use for request signing. If not specified, the Region is derived from the source URL hostname, falling back to the Region of the registry.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-z0-9-]+`   
Required: No

 ** roleArn **   <a name="agentregistrycontrol-Type-RegistryRecordIamCredentialProvider-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role to assume for request signing.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`   
Required: No

 ** service **   <a name="agentregistrycontrol-Type-RegistryRecordIamCredentialProvider-service"></a>
The service name to use for request signing, such as execute-api.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: No

## See Also
<a name="API_RegistryRecordIamCredentialProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/RegistryRecordIamCredentialProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/RegistryRecordIamCredentialProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/RegistryRecordIamCredentialProvider) 
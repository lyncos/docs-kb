---
title: RegistryRecordOAuthCredentialProvider
description: The configuration for an OAuth 2.0 credential provider that authenticates requests to a registry record's source.
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_RegistryRecordOAuthCredentialProvider.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# RegistryRecordOAuthCredentialProvider
<a name="API_RegistryRecordOAuthCredentialProvider"></a>

The configuration for an OAuth 2.0 credential provider that authenticates requests to a registry record's source.

## Contents
<a name="API_RegistryRecordOAuthCredentialProvider_Contents"></a>

 ** providerArn **   <a name="agentregistrycontrol-Type-RegistryRecordOAuthCredentialProvider-providerArn"></a>
The Amazon Resource Name (ARN) of the OAuth 2.0 credential provider resource in Amazon Bedrock AgentCore Identity.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:.*`   
Required: Yes

 ** customParameters **   <a name="agentregistrycontrol-Type-RegistryRecordOAuthCredentialProvider-customParameters"></a>
Additional parameters to include in the OAuth 2.0 token request.  
Type: String to string map  
Required: No

 ** grantType **   <a name="agentregistrycontrol-Type-RegistryRecordOAuthCredentialProvider-grantType"></a>
The OAuth 2.0 grant type used to obtain access tokens.  
Type: String  
Valid Values: `CLIENT_CREDENTIALS`   
Required: No

 ** scopes **   <a name="agentregistrycontrol-Type-RegistryRecordOAuthCredentialProvider-scopes"></a>
The OAuth 2.0 scopes to request when obtaining access tokens.  
Type: Array of strings  
Required: No

## See Also
<a name="API_RegistryRecordOAuthCredentialProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/RegistryRecordOAuthCredentialProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/RegistryRecordOAuthCredentialProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/RegistryRecordOAuthCredentialProvider) 
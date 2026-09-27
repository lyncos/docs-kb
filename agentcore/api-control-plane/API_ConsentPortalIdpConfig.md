---
title: ConsentPortalIdpConfig
description: The identity provider configuration used to authenticate end users to the consent portal.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ConsentPortalIdpConfig.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# ConsentPortalIdpConfig
<a name="API_ConsentPortalIdpConfig"></a>

The identity provider configuration used to authenticate end users to the consent portal.

## Contents
<a name="API_ConsentPortalIdpConfig_Contents"></a>

 ** credentialProviderArn **   <a name="bedrockagentcorecontrol-Type-ConsentPortalIdpConfig-credentialProviderArn"></a>
The Amazon Resource Name (ARN) of the OAuth2 credential provider used to authenticate end users to the consent portal.  
Type: String  
Pattern: `arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b|aws-iso-e|aws-iso-f|aws-eusc):bedrock-agentcore:[a-z0-9-]{1,32}:[0-9]{12}:token-vault/[a-zA-Z0-9_-]{1,64}/oauth2credentialprovider/[a-zA-Z0-9_-]{1,128}`   
Required: Yes

 ** scopes **   <a name="bedrockagentcorecontrol-Type-ConsentPortalIdpConfig-scopes"></a>
The OAuth2 scopes that the consent portal requests when authenticating end users.  
Type: Array of strings  
Array Members: Minimum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[\x21\x23-\x5B\x5D-\x7E]+`   
Required: Yes

 ** audience **   <a name="bedrockagentcorecontrol-Type-ConsentPortalIdpConfig-audience"></a>
The audience value that the consent portal includes when requesting tokens from the identity provider.  
Type: String  
Required: No

## See Also
<a name="API_ConsentPortalIdpConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ConsentPortalIdpConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ConsentPortalIdpConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ConsentPortalIdpConfig) 
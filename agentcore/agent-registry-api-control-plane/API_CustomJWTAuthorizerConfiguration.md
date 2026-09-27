---
title: CustomJWTAuthorizerConfiguration
description: Configuration for a custom JWT authorizer that validates inbound bearer tokens against an OpenID Connect identity provider.
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_CustomJWTAuthorizerConfiguration.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# CustomJWTAuthorizerConfiguration
<a name="API_CustomJWTAuthorizerConfiguration"></a>

Configuration for a custom JWT authorizer that validates inbound bearer tokens against an OpenID Connect identity provider.

## Contents
<a name="API_CustomJWTAuthorizerConfiguration_Contents"></a>

 ** discoveryUrl **   <a name="agentregistrycontrol-Type-CustomJWTAuthorizerConfiguration-discoveryUrl"></a>
The OpenID Connect discovery URL used to retrieve the identity provider's metadata and signing keys.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `.+/\.well-known/openid-configuration`   
Required: Yes

 ** allowedAudience **   <a name="agentregistrycontrol-Type-CustomJWTAuthorizerConfiguration-allowedAudience"></a>
The audience values accepted during JWT validation. A token is rejected if none of its audience claims match.  
Type: Array of strings  
Array Members: Minimum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** allowedClients **   <a name="agentregistrycontrol-Type-CustomJWTAuthorizerConfiguration-allowedClients"></a>
The client identifiers accepted during JWT validation. A token is rejected if it was not issued to one of these clients.  
Type: Array of strings  
Array Members: Minimum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** allowedScopes **   <a name="agentregistrycontrol-Type-CustomJWTAuthorizerConfiguration-allowedScopes"></a>
The scopes accepted during JWT validation. A token is rejected if it does not carry one of these scopes.  
Type: Array of strings  
Array Members: Minimum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[\x21\x23-\x5B\x5D-\x7E]+`   
Required: No

 ** customClaims **   <a name="agentregistrycontrol-Type-CustomJWTAuthorizerConfiguration-customClaims"></a>
Additional custom claim validations applied to the inbound JWT.  
Type: Array of [CustomClaimValidationType](API_CustomClaimValidationType.md) objects  
Array Members: Minimum number of 1 item.  
Required: No

 ** privateEndpoint **   <a name="agentregistrycontrol-Type-CustomJWTAuthorizerConfiguration-privateEndpoint"></a>
The private endpoint used to reach the identity provider's discovery URL over a private network path.  
Type: [PrivateEndpoint](API_PrivateEndpoint.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** privateEndpointOverrides **   <a name="agentregistrycontrol-Type-CustomJWTAuthorizerConfiguration-privateEndpointOverrides"></a>
Per-domain private endpoint overrides that route specific identity provider domains through distinct private endpoints.  
Type: Array of [PrivateEndpointOverride](API_PrivateEndpointOverride.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 5 items.  
Required: No

## See Also
<a name="API_CustomJWTAuthorizerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/CustomJWTAuthorizerConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/CustomJWTAuthorizerConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/CustomJWTAuthorizerConfiguration) 
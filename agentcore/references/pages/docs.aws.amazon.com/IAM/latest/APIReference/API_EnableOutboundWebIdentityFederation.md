---
title: EnableOutboundWebIdentityFederation
description: Enables the outbound identity federation feature for your AWS account. When enabled, IAM principals in your account can use the `GetWebIdentityToken` API to obtain JSON Web Tokens (JWTs) for secure authentication with external services. This operation also generates a unique issu
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_EnableOutboundWebIdentityFederation.html
fetched: '2026-09-26'
tags:
- agentcore
- docs-aws-amazon-com
- reference
- related
referenced_by:
- client-auth-methods.md
- on-behalf-of-token-exchange.md
conversion: native-md
---

# EnableOutboundWebIdentityFederation
<a name="API_EnableOutboundWebIdentityFederation"></a>

Enables the outbound identity federation feature for your AWS account. When enabled, IAM principals in your account can use the `GetWebIdentityToken` API to obtain JSON Web Tokens (JWTs) for secure authentication with external services. This operation also generates a unique issuer URL for your AWS account. 

## Response Elements
<a name="API_EnableOutboundWebIdentityFederation_ResponseElements"></a>

The following element is returned by the service.

 ** IssuerIdentifier **   
A unique issuer URL for your AWS account that hosts the OpenID Connect (OIDC) discovery endpoints at `/.well-known/openid-configuration and /.well-known/jwks.json`. The OpenID Connect (OIDC) discovery endpoints contain verification keys and metadata necessary for token verification.  
Type: String

## Errors
<a name="API_EnableOutboundWebIdentityFederation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** FeatureEnabled **   
The request failed because outbound identity federation is already enabled for your AWS account. You cannot enable the feature multiple times. To fetch the current configuration (including the unique issuer URL), use the `GetOutboundWebIdentityFederationInfo` operation.  
HTTP Status Code: 409

## Examples
<a name="API_EnableOutboundWebIdentityFederation_Examples"></a>

### Example
<a name="API_EnableOutboundWebIdentityFederation_Example_1"></a>

This example illustrates one usage of EnableOutboundWebIdentityFederation.

#### Sample Request
<a name="API_EnableOutboundWebIdentityFederation_Example_1_Request"></a>

```
                https://iam.amazonaws.com/?Action=EnableOutboundWebIdentityFederation
                &Version=2010-05-08
                &AUTHPARAMS
```

#### Sample Response
<a name="API_EnableOutboundWebIdentityFederation_Example_1_Response"></a>

```
                    <EnableOutboundWebIdentityFederationResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
                      <EnableOutboundWebIdentityFederationResult>
                        <IssuerIdentifier>https://a1d2b0fd-1177-4468-9351-2fEXAMPLE723.tokens.sts.global.api.aws</IssuerIdentifier>
                      </EnableOutboundWebIdentityFederationResult>
                      <ResponseMetadata>
                        <RequestId>4a396884-3469-427a-938f-e5EXAMPLE11e</RequestId>
                      </ResponseMetadata>
                    </EnableOutboundWebIdentityFederationResponse>
```

## See Also
<a name="API_EnableOutboundWebIdentityFederation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/EnableOutboundWebIdentityFederation) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/EnableOutboundWebIdentityFederation) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/EnableOutboundWebIdentityFederation) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/EnableOutboundWebIdentityFederation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/EnableOutboundWebIdentityFederation) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/EnableOutboundWebIdentityFederation) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/EnableOutboundWebIdentityFederation) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/EnableOutboundWebIdentityFederation) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/EnableOutboundWebIdentityFederation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/EnableOutboundWebIdentityFederation)

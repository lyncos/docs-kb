---
title: GetWebIdentityToken
description: Returns a signed JSON Web Token (JWT) that represents the calling AWS identity. The returned JWT can be used to authenticate with external services that support OIDC discovery. The token is signed by AWS STS and can be publicly verified using the verification keys published at th
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/STS/latest/APIReference/API_GetWebIdentityToken.html
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

# GetWebIdentityToken
<a name="API_GetWebIdentityToken"></a>

Returns a signed JSON Web Token (JWT) that represents the calling AWS identity. The returned JWT can be used to authenticate with external services that support OIDC discovery. The token is signed by AWS STS and can be publicly verified using the verification keys published at the issuer's JWKS endpoint.

**Note**  
The `GetWebIdentityToken` API is not available on the STS Global endpoint.

## Request Parameters
<a name="API_GetWebIdentityToken_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Audience.member.N**   
The intended recipient of the web identity token. This value populates the `aud` claim in the JWT and should identify the service or application that will validate and use the token. The external service should verify this claim to ensure the token was intended for their use.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 1000.  
Required: Yes

 ** DurationSeconds **   
The duration, in seconds, for which the JSON Web Token (JWT) will remain valid. The value can range from 60 seconds (1 minute) to 3600 seconds (1 hour). If not specified, the default duration is 300 seconds (5 minutes). The token is designed to be short-lived and should be used for proof of identity, then exchanged for credentials or short-lived tokens in the external service.  
Type: Integer  
Valid Range: Minimum value of 60. Maximum value of 3600.  
Required: No

 ** SigningAlgorithm **   
The cryptographic algorithm to use for signing the JSON Web Token (JWT). Valid values are RS256 (RSA with SHA-256) and ES384 (ECDSA using P-384 curve with SHA-384).   
Type: String  
Length Constraints: Fixed length of 5.  
Required: Yes

 **Tags.member.N**   
An optional list of tags to include in the JSON Web Token (JWT). These tags are added as custom claims to the JWT and can be used by the downstream service for authorization decisions.   
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Maximum number of 50 items.  
Required: No

## Response Elements
<a name="API_GetWebIdentityToken_ResponseElements"></a>

The following elements are returned by the service.

 ** Expiration **   
The date and time when the web identity token expires, in UTC. The expiration is determined by adding the `DurationSeconds` value to the time the token was issued. After this time, the token should no longer be considered valid.  
Type: Timestamp

 ** WebIdentityToken **   
A signed JSON Web Token (JWT) that represents the caller's AWS identity. The token contains standard JWT claims such as subject, audience, expiration time, and additional identity attributes added by STS as custom claims. You can also add your own custom claims to the token by passing tags as request parameters to the `GetWebIdentityToken` API. The token is signed using the specified signing algorithm and can be verified using the verification keys available at the issuer's JWKS endpoint.  
Type: String

## Errors
<a name="API_GetWebIdentityToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** JWTPayloadSizeExceeded **   
The requested token payload size exceeds the maximum allowed size. Reduce the number of request tags included in the `GetWebIdentityToken` API call to reduce the token payload size.  
HTTP Status Code: 400

 ** OutboundWebIdentityFederationDisabled **   
The outbound web identity federation feature is not enabled for this account. To use this feature, you must first enable it through the AWS Management Console or API.  
HTTP Status Code: 403

 ** SessionDurationEscalation **   
The requested token duration would extend the session beyond its original expiration time. You cannot use this operation to extend the lifetime of a session beyond what was granted when the session was originally created.  
HTTP Status Code: 403

## Examples
<a name="API_GetWebIdentityToken_Examples"></a>

### Example
<a name="API_GetWebIdentityToken_Example_1"></a>

This example illustrates one usage of GetWebIdentityToken.

#### Sample Request
<a name="API_GetWebIdentityToken_Example_1_Request"></a>

```
               aws sts get-web-identity-token \
               --audience test \
               --signing-algorithm RS256 \
               --duration-seconds 300
```

#### Sample Response
<a name="API_GetWebIdentityToken_Example_1_Response"></a>

```
               {
                   "WebIdentityToken": "token",
                   "Expiration": "2025-11-11T22:44:21.703000+00:00"
               }
```

## See Also
<a name="API_GetWebIdentityToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sts-2011-06-15/GetWebIdentityToken) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sts-2011-06-15/GetWebIdentityToken) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sts-2011-06-15/GetWebIdentityToken) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sts-2011-06-15/GetWebIdentityToken) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sts-2011-06-15/GetWebIdentityToken) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sts-2011-06-15/GetWebIdentityToken) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sts-2011-06-15/GetWebIdentityToken) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sts-2011-06-15/GetWebIdentityToken) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sts-2011-06-15/GetWebIdentityToken) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sts-2011-06-15/GetWebIdentityToken)

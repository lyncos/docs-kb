---
title: DescribeUserPoolClient
description: Given an app client ID, returns configuration information. This operation is useful when you want to inspect an existing app client and programmatically replicate the configuration to another app client. For more information about app clients, see App clients.
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_DescribeUserPoolClient.html
fetched: '2026-09-26'
tags:
- agentcore
- docs-aws-amazon-com
- reference
- related
referenced_by:
- gateway-using-auth-ex-starter.md
conversion: native-md
---

# DescribeUserPoolClient
<a name="API_DescribeUserPoolClient"></a>

Given an app client ID, returns configuration information. This operation is useful when you want to inspect an existing app client and programmatically replicate the configuration to another app client. For more information about app clients, see [App clients](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-client-apps.html).

**Note**  
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.  
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) 
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html) 

## Request Syntax
<a name="API_DescribeUserPoolClient_RequestSyntax"></a>

```
{
   "ClientId": "{{string}}",
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeUserPoolClient_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientId](#API_DescribeUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-DescribeUserPoolClient-request-ClientId"></a>
The ID of the app client that you want to describe.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[\w+]+`   
Required: Yes

 ** [UserPoolId](#API_DescribeUserPoolClient_RequestSyntax) **   <a name="CognitoUserPools-DescribeUserPoolClient-request-UserPoolId"></a>
The ID of the user pool that contains the app client you want to describe.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 55.  
Pattern: `[\w-]+_[0-9a-zA-Z]+`   
Required: Yes

## Response Syntax
<a name="API_DescribeUserPoolClient_ResponseSyntax"></a>

```
{
   "UserPoolClient": { 
      "AccessTokenValidity": number,
      "AllowedOAuthFlows": [ "string" ],
      "AllowedOAuthFlowsUserPoolClient": boolean,
      "AllowedOAuthScopes": [ "string" ],
      "AnalyticsConfiguration": { 
         "ApplicationArn": "string",
         "ApplicationId": "string",
         "ExternalId": "string",
         "RoleArn": "string",
         "UserDataShared": boolean
      },
      "AuthSessionValidity": number,
      "CallbackURLs": [ "string" ],
      "ClientId": "string",
      "ClientName": "string",
      "ClientSecret": "string",
      "CreationDate": number,
      "DefaultRedirectURI": "string",
      "EnablePropagateAdditionalUserContextData": boolean,
      "EnableTokenRevocation": boolean,
      "ExplicitAuthFlows": [ "string" ],
      "IdTokenValidity": number,
      "LastModifiedDate": number,
      "LogoutURLs": [ "string" ],
      "PreventUserExistenceErrors": "string",
      "ReadAttributes": [ "string" ],
      "RefreshTokenRotation": { 
         "Feature": "string",
         "RetryGracePeriodSeconds": number
      },
      "RefreshTokenValidity": number,
      "SupportedIdentityProviders": [ "string" ],
      "TokenValidityUnits": { 
         "AccessToken": "string",
         "IdToken": "string",
         "RefreshToken": "string"
      },
      "UserPoolId": "string",
      "WriteAttributes": [ "string" ]
   }
}
```

## Response Elements
<a name="API_DescribeUserPoolClient_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UserPoolClient](#API_DescribeUserPoolClient_ResponseSyntax) **   <a name="CognitoUserPools-DescribeUserPoolClient-response-UserPoolClient"></a>
The details of the request app client.  
Type: [UserPoolClientType](API_UserPoolClientType.md) object

## Errors
<a name="API_DescribeUserPoolClient_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **   
This exception is thrown when Amazon Cognito encounters an internal error.    
 ** message **   
The message returned when Amazon Cognito throws an internal error exception.
HTTP Status Code: 500

 ** InvalidParameterException **   
This exception is thrown when the Amazon Cognito service encounters an invalid parameter.    
 ** message **   
The message returned when the Amazon Cognito service throws an invalid parameter exception.  
 ** reasonCode **   
The reason code of the exception.
HTTP Status Code: 400

 ** NotAuthorizedException **   
This exception is thrown when a user isn't authorized.    
 ** message **   
The message returned when the Amazon Cognito service returns a not authorized exception.
HTTP Status Code: 400

 ** OperationNotEnabledException **   
This exception is thrown when an operation is not available in the current region or for the current user pool configuration. This can occur when attempting to perform operations that are not supported in secondary replica regions.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
This exception is thrown when the Amazon Cognito service can't find the requested resource.    
 ** message **   
The message returned when the Amazon Cognito service returns a resource not found exception.
HTTP Status Code: 400

 ** TooManyRequestsException **   
This exception is thrown when the user has made too many requests for a given operation.    
 ** message **   
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

## Examples
<a name="API_DescribeUserPoolClient_Examples"></a>

### Example
<a name="API_DescribeUserPoolClient_Example_1"></a>

The following example request describes the app client with the ID `1example23456789`.

#### Sample Request
<a name="API_DescribeUserPoolClient_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-east-1.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.DescribeUserPoolClient
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
   "ClientId": "1example23456789",
   "UserPoolId": "us-east-1_EXAMPLE"
}
```

#### Sample Response
<a name="API_DescribeUserPoolClient_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive

{
      "UserPoolClient": {
        "AccessTokenValidity": 6,
        "AllowedOAuthFlows": [
          "code"
        ],
        "AllowedOAuthFlowsUserPoolClient": true,
        "AllowedOAuthScopes": [
          "aws.cognito.signin.user.admin",
          "openid"
        ],
        "AnalyticsConfiguration": {
          "ApplicationId": "d70b2ba36a8c4dc5a04a0451a31a1e12",
          "ExternalId": "my-external-id",
          "RoleArn": "arn:aws:iam::123456789012:role/test-cognitouserpool-role",
          "UserDataShared": true
        },
        "AuthSessionValidity": 3,
        "CallbackURLs": [
          "https://example.com",
          "http://localhost",
          "myapp://example"
        ],
        "ClientId": "1example23456789",
        "ClientName": "my-test-app-client",
        "ClientSecret": "13ka4h7u28d9oo44tqpq9djqsfvhvu8rk4d2ighvpu0k8fj1c2r9",
        "CreationDate": 1689885426.107,
        "DefaultRedirectURI": "https://example.com",
        "EnablePropagateAdditionalUserContextData": false,
        "EnableTokenRevocation": true,
        "ExplicitAuthFlows": [
          "ALLOW_USER_AUTH",
          "ALLOW_USER_PASSWORD_AUTH",
          "ALLOW_ADMIN_USER_PASSWORD_AUTH",
          "ALLOW_REFRESH_TOKEN_AUTH"
        ],
        "IdTokenValidity": 6,
        "LastModifiedDate": 1689885426.107,
        "LogoutURLs": [
          "https://example.com/logout"
        ],
        "PreventUserExistenceErrors": "ENABLED",
        "ReadAttributes": [
          "address",
          "preferred_username",
          "email"
        ],
        "RefreshTokenValidity": 6,
        "SupportedIdentityProviders": [
          "SignInWithApple",
          "MySSO"
        ],
        "TokenValidityUnits": {
          "AccessToken": "hours",
          "IdToken": "minutes",
          "RefreshToken": "days"
        },
        "UserPoolId": "us-east-1_EXAMPLE",
        "WriteAttributes": [
          "family_name",
          "email"
        ]
      }
}
```

## See Also
<a name="API_DescribeUserPoolClient_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/DescribeUserPoolClient) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/DescribeUserPoolClient) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/DescribeUserPoolClient) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/DescribeUserPoolClient) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/DescribeUserPoolClient) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/DescribeUserPoolClient) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/DescribeUserPoolClient) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/DescribeUserPoolClient) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/DescribeUserPoolClient) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/DescribeUserPoolClient)

---
title: CreateResourceServer
description: Creates a new OAuth2.0 resource server and defines custom scopes within it. Resource servers are associated with custom scopes and machine-to-machine (M2M) authorization. For more information, see Access control with resource servers.
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateResourceServer.html
fetched: '2026-09-26'
tags:
- agentcore
- docs-aws-amazon-com
- reference
- related
referenced_by:
- identity-authentication.md
conversion: native-md
---

# CreateResourceServer
<a name="API_CreateResourceServer"></a>

Creates a new OAuth2.0 resource server and defines custom scopes within it. Resource servers are associated with custom scopes and machine-to-machine (M2M) authorization. For more information, see [Access control with resource servers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-define-resource-servers.html).

**Note**  
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.  
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) 
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html) 

## Request Syntax
<a name="API_CreateResourceServer_RequestSyntax"></a>

```
{
   "Identifier": "{{string}}",
   "Name": "{{string}}",
   "Scopes": [ 
      { 
         "ScopeDescription": "{{string}}",
         "ScopeName": "{{string}}"
      }
   ],
   "UserPoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateResourceServer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Identifier](#API_CreateResourceServer_RequestSyntax) **   <a name="CognitoUserPools-CreateResourceServer-request-Identifier"></a>
A unique resource server identifier for the resource server. The identifier can be an API friendly name like `solar-system-data`. You can also set an API URL like `https://solar-system-data-api.example.com` as your identifier.  
Amazon Cognito represents scopes in the access token in the format `$resource-server-identifier/$scope`. Longer scope-identifier strings increase the size of your access tokens.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[\x21\x23-\x5B\x5D-\x7E]+`   
Required: Yes

 ** [Name](#API_CreateResourceServer_RequestSyntax) **   <a name="CognitoUserPools-CreateResourceServer-request-Name"></a>
A friendly name for the resource server.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[\w\s+=,.@-]+`   
Required: Yes

 ** [Scopes](#API_CreateResourceServer_RequestSyntax) **   <a name="CognitoUserPools-CreateResourceServer-request-Scopes"></a>
A list of custom scopes. Each scope is a key-value map with the keys `ScopeName` and `ScopeDescription`. The name of a custom scope is a combination of `ScopeName` and the resource server `Name` in this request, for example `MyResourceServerName/MyScopeName`.  
Type: Array of [ResourceServerScopeType](API_ResourceServerScopeType.md) objects  
Array Members: Maximum number of 100 items.  
Required: No

 ** [UserPoolId](#API_CreateResourceServer_RequestSyntax) **   <a name="CognitoUserPools-CreateResourceServer-request-UserPoolId"></a>
The ID of the user pool where you want to create a resource server.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 55.  
Pattern: `[\w-]+_[0-9a-zA-Z]+`   
Required: Yes

## Response Syntax
<a name="API_CreateResourceServer_ResponseSyntax"></a>

```
{
   "ResourceServer": { 
      "Identifier": "string",
      "Name": "string",
      "Scopes": [ 
         { 
            "ScopeDescription": "string",
            "ScopeName": "string"
         }
      ],
      "UserPoolId": "string"
   }
}
```

## Response Elements
<a name="API_CreateResourceServer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourceServer](#API_CreateResourceServer_ResponseSyntax) **   <a name="CognitoUserPools-CreateResourceServer-response-ResourceServer"></a>
The details of the new resource server.  
Type: [ResourceServerType](API_ResourceServerType.md) object

## Errors
<a name="API_CreateResourceServer_Errors"></a>

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

 ** LimitExceededException **   
This exception is thrown when a user exceeds the limit for a requested AWS resource.    
 ** message **   
The message returned when Amazon Cognito throws a limit exceeded exception.
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
<a name="API_CreateResourceServer_Examples"></a>

### Example
<a name="API_CreateResourceServer_Example_1"></a>

The following example request creates a resource server for the API at `myapi.example.com` with the scopes `myapi.example.com/international.read` and `myapi.example.com/domestic.read`.

#### Sample Request
<a name="API_CreateResourceServer_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.CreateResourceServer
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
   "Identifier": "myapi.example.com",
   "Name": "Example API with custom access control scopes",
   "Scopes": [
      {
         "ScopeDescription": "International customers",
         "ScopeName": "international.read"
      },
      {
         "ScopeDescription": "Domestic customers",
         "ScopeName": "domestic.read"
      }
   ],
   "UserPoolId": "us-west-2_EXAMPLE"
}
```

#### Sample Response
<a name="API_CreateResourceServer_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{
	"ResourceServer": {
		"Identifier": "myapi.example.com",
		"Name": "Example API with custom access control scopes",
		"Scopes": [
			{
				"ScopeDescription": "International customers",
				"ScopeName": "international.read"
			},
			{
				"ScopeDescription": "Domestic customers",
				"ScopeName": "domestic.read"
			}
		],
		"UserPoolId": "us-west-2_EXAMPLE"
	}
}
```

## See Also
<a name="API_CreateResourceServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/CreateResourceServer) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/CreateResourceServer) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/CreateResourceServer) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/CreateResourceServer) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/CreateResourceServer) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/CreateResourceServer) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/CreateResourceServer) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/CreateResourceServer) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/CreateResourceServer) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/CreateResourceServer)

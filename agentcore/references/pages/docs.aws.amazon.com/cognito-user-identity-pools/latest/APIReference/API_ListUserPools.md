---
title: ListUserPools
description: Lists user pools and their details in the current AWS account.
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ListUserPools.html
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

# ListUserPools
<a name="API_ListUserPools"></a>

Lists user pools and their details in the current AWS account.

**Note**  
Amazon Cognito evaluates AWS Identity and Access Management (IAM) policies in requests for this API operation. For this operation, you must use IAM credentials to authorize requests, and you must grant yourself the corresponding IAM permission in a policy.  
 [Signing AWS API Requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-signing.html) 
 [Using the Amazon Cognito user pools API and user pool endpoints](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html) 

## Request Syntax
<a name="API_ListUserPools_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListUserPools_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListUserPools_RequestSyntax) **   <a name="CognitoUserPools-ListUserPools-request-MaxResults"></a>
The maximum number of user pools that you want Amazon Cognito to return in the response.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 60.  
Required: Yes

 ** [NextToken](#API_ListUserPools_RequestSyntax) **   <a name="CognitoUserPools-ListUserPools-request-NextToken"></a>
This API operation returns a limited number of results. The pagination token is an identifier that you can present in an additional API request with the same parameters. When you include the pagination token, Amazon Cognito returns the next set of items after the current list. Subsequent requests return a new pagination token. By use of this token, you can paginate through the full list of items.  
Type: String  
Length Constraints: Minimum length of 1.  
Pattern: `[\S]+`   
Required: No

## Response Syntax
<a name="API_ListUserPools_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "UserPools": [ 
      { 
         "CreationDate": number,
         "Id": "string",
         "LambdaConfig": { 
            "CreateAuthChallenge": "string",
            "CustomEmailSender": { 
               "LambdaArn": "string",
               "LambdaVersion": "string"
            },
            "CustomMessage": "string",
            "CustomSMSSender": { 
               "LambdaArn": "string",
               "LambdaVersion": "string"
            },
            "DefineAuthChallenge": "string",
            "InboundFederation": { 
               "LambdaArn": "string",
               "LambdaVersion": "string"
            },
            "KMSKeyID": "string",
            "PostAuthentication": "string",
            "PostConfirmation": "string",
            "PreAuthentication": "string",
            "PreSignUp": "string",
            "PreTokenGeneration": "string",
            "PreTokenGenerationConfig": { 
               "LambdaArn": "string",
               "LambdaVersion": "string"
            },
            "UserMigration": "string",
            "VerifyAuthChallengeResponse": "string"
         },
         "LastModifiedDate": number,
         "Name": "string",
         "ReplicaRegions": [ "string" ],
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListUserPools_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListUserPools_ResponseSyntax) **   <a name="CognitoUserPools-ListUserPools-response-NextToken"></a>
The identifier that Amazon Cognito returned with the previous request to this operation. When you include a pagination token in your request, Amazon Cognito returns the next set of items in the list. By use of this token, you can paginate through the full list of items.  
Type: String  
Length Constraints: Minimum length of 1.  
Pattern: `[\S]+` 

 ** [UserPools](#API_ListUserPools_ResponseSyntax) **   <a name="CognitoUserPools-ListUserPools-response-UserPools"></a>
An array of user pools and their configuration details.  
Type: Array of [UserPoolDescriptionType](API_UserPoolDescriptionType.md) objects

## Errors
<a name="API_ListUserPools_Errors"></a>

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

 ** TooManyRequestsException **   
This exception is thrown when the user has made too many requests for a given operation.    
 ** message **   
The message returned when the Amazon Cognito service returns a too many requests exception.
HTTP Status Code: 400

## Examples
<a name="API_ListUserPools_Examples"></a>

### Example
<a name="API_ListUserPools_Example_1"></a>

The following example request lists the first three user pools in the AWS account associated with the user that signed the request.

#### Sample Request
<a name="API_ListUserPools_Example_1_Request"></a>

```
POST HTTP/1.1
Host: cognito-idp.us-west-2.amazonaws.com
X-Amz-Date: 20230613T200059Z
Accept-Encoding: gzip, deflate, br
X-Amz-Target: AWSCognitoIdentityProviderService.ListUserPools
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Length: <PayloadSizeBytes>
{
   "MaxResults": 3
}
```

#### Sample Response
<a name="API_ListUserPools_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 13 Jun 2023 20:00:59 GMT
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
x-amzn-requestid: a1b2c3d4-e5f6-a1b2-c3d4-EXAMPLE11111
Connection: keep-alive
{
    "NextToken": "[Pagination token]",
    "UserPools": [
        {
            "CreationDate": 1681502497.741,
            "Id": "us-west-2_EXAMPLE1",
            "LambdaConfig": {
                "CustomMessage": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
                "PreSignUp": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
                "PreTokenGeneration": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
                "PreTokenGenerationConfig": {
                    "LambdaArn": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction",
                    "LambdaVersion": "V1_0"
                }
            },
            "LastModifiedDate": 1681502497.741,
            "Name": "user pool 1",
            "ReplicaRegions": ["us-west-2", "us-east-1"]
        },
        {
            "CreationDate": 1686064178.717,
            "Id": "us-west-2_EXAMPLE2",
            "LambdaConfig": {
            },
            "LastModifiedDate": 1686064178.873,
            "Name": "user pool 2"
        },
        {
            "CreationDate": 1627681712.237,
            "Id": "us-west-2_EXAMPLE3",
            "LambdaConfig": {
                "UserMigration": "arn:aws:lambda:us-east-1:123456789012:function:MyFunction"
            },
            "LastModifiedDate": 1678486942.479,
            "Name": "user pool 3"
        }
    ]
}
```

## See Also
<a name="API_ListUserPools_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cognito-idp-2016-04-18/ListUserPools) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cognito-idp-2016-04-18/ListUserPools) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/ListUserPools) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cognito-idp-2016-04-18/ListUserPools) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/ListUserPools) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cognito-idp-2016-04-18/ListUserPools) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cognito-idp-2016-04-18/ListUserPools) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cognito-idp-2016-04-18/ListUserPools) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cognito-idp-2016-04-18/ListUserPools) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/ListUserPools)

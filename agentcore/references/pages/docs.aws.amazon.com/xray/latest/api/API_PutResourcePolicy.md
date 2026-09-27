---
title: PutResourcePolicy
description: Sets the resource policy to grant one or more AWS services and accounts permissions to access X-Ray. Each resource policy will be associated with a specific AWS account. Each AWS account can have a maximum of 5 resource policies, and each policy name must be unique within that ac
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/xray/latest/api/API_PutResourcePolicy.html
fetched: '2026-09-26'
tags:
- agentcore
- docs-aws-amazon-com
- reference
- related
referenced_by:
- observability-configure.md
conversion: native-md
---

# PutResourcePolicy
<a name="API_PutResourcePolicy"></a>

 Sets the resource policy to grant one or more AWS services and accounts permissions to access X-Ray. Each resource policy will be associated with a specific AWS account. Each AWS account can have a maximum of 5 resource policies, and each policy name must be unique within that account. The maximum size of each resource policy is 5KB. 

## Request Syntax
<a name="API_PutResourcePolicy_RequestSyntax"></a>

```
POST /PutResourcePolicy HTTP/1.1
Content-type: application/json

{
   "BypassPolicyLockoutCheck": {{boolean}},
   "PolicyDocument": "{{string}}",
   "PolicyName": "{{string}}",
   "PolicyRevisionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutResourcePolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutResourcePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [BypassPolicyLockoutCheck](#API_PutResourcePolicy_RequestSyntax) **   <a name="xray-PutResourcePolicy-request-BypassPolicyLockoutCheck"></a>
A flag to indicate whether to bypass the resource policy lockout safety check.  
Setting this value to true increases the risk that the policy becomes unmanageable. Do not set this value to true indiscriminately.
Use this parameter only when you include a policy in the request and you intend to prevent the principal that is making the request from making a subsequent `PutResourcePolicy` request.  
The default value is false.  
Type: Boolean  
Required: No

 ** [PolicyDocument](#API_PutResourcePolicy_RequestSyntax) **   <a name="xray-PutResourcePolicy-request-PolicyDocument"></a>
The resource policy document, which can be up to 5kb in size.  
Type: String  
Required: Yes

 ** [PolicyName](#API_PutResourcePolicy_RequestSyntax) **   <a name="xray-PutResourcePolicy-request-PolicyName"></a>
The name of the resource policy. Must be unique within a specific AWS account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[\w+=,.@-]+`   
Required: Yes

 ** [PolicyRevisionId](#API_PutResourcePolicy_RequestSyntax) **   <a name="xray-PutResourcePolicy-request-PolicyRevisionId"></a>
Specifies a specific policy revision, to ensure an atomic create operation. By default the resource policy is created if it does not exist, or updated with an incremented revision id. The revision id is unique to each policy in the account.  
If the policy revision id does not match the latest revision id, the operation will fail with an `InvalidPolicyRevisionIdException` exception. You can also provide a `PolicyRevisionId` of 0. In this case, the operation will fail with an `InvalidPolicyRevisionIdException` exception if a resource policy with the same name already exists.   
Type: String  
Required: No

## Response Syntax
<a name="API_PutResourcePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ResourcePolicy": { 
      "LastUpdatedTime": number,
      "PolicyDocument": "string",
      "PolicyName": "string",
      "PolicyRevisionId": "string"
   }
}
```

## Response Elements
<a name="API_PutResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourcePolicy](#API_PutResourcePolicy_ResponseSyntax) **   <a name="xray-PutResourcePolicy-response-ResourcePolicy"></a>
The resource policy document, as provided in the `PutResourcePolicyRequest`.  
Type: [ResourcePolicy](API_ResourcePolicy.md) object

## Errors
<a name="API_PutResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidPolicyRevisionIdException **   
A policy revision id was provided which does not match the latest policy revision. This exception is also if a policy revision id of 0 is provided via `PutResourcePolicy` and a policy with the same name already exists.  
HTTP Status Code: 400

 ** LockoutPreventionException **   
The provided resource policy would prevent the caller of this request from calling PutResourcePolicy in the future.  
HTTP Status Code: 400

 ** MalformedPolicyDocumentException **   
Invalid policy document provided in request.  
HTTP Status Code: 400

 ** PolicyCountLimitExceededException **   
Exceeded the maximum number of resource policies for a target AWS account.  
HTTP Status Code: 400

 ** PolicySizeLimitExceededException **   
Exceeded the maximum size for a resource policy.  
HTTP Status Code: 400

 ** ThrottledException **   
The request exceeds the maximum number of requests per second.  
HTTP Status Code: 429

## See Also
<a name="API_PutResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/PutResourcePolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/PutResourcePolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/PutResourcePolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/PutResourcePolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/PutResourcePolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/PutResourcePolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/PutResourcePolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/PutResourcePolicy) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/PutResourcePolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/PutResourcePolicy)

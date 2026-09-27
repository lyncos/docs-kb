---
title: CreateCapacityProvider
description: Creates a capacity provider. A capacity provider defines the Amazon EC2 infrastructure for AgentCore Runtime, including the operating system, allowed instance types, networking, and storage. It also specifies the IAM permissions that AgentCore uses to manage those instances.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CreateCapacityProvider.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# CreateCapacityProvider
<a name="API_CreateCapacityProvider"></a>

Creates a capacity provider. A capacity provider defines the Amazon EC2 infrastructure for AgentCore Runtime, including the operating system, allowed instance types, networking, and storage. It also specifies the IAM permissions that AgentCore uses to manage those instances.

The capacity provider name must be unique within your account. After you create the capacity provider, it enters a `CREATING` state and transitions to `READY` when it is available for use.

## Request Syntax
<a name="API_CreateCapacityProvider_RequestSyntax"></a>

```
PUT /capacity-providers HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "computeConfiguration": { ... },
   "description": "{{string}}",
   "name": "{{string}}",
   "permissionsConfiguration": { 
      "capacityProviderOperatorRoleArn": "{{string}}"
   },
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateCapacityProvider_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateCapacityProvider_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateCapacityProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateCapacityProvider-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [computeConfiguration](#API_CreateCapacityProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateCapacityProvider-request-computeConfiguration"></a>
The compute configuration for the capacity provider. This defines the Amazon EC2 compute resources used to launch instances: the operating system, allowed instance types, networking, and storage.  
Type: [ComputeConfiguration](API_ComputeConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** [description](#API_CreateCapacityProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateCapacityProvider-request-description"></a>
An optional description of the capacity provider. If you don't specify a description, the service creates the capacity provider without one.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** [name](#API_CreateCapacityProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateCapacityProvider-request-name"></a>
The name of the capacity provider. The name must be unique within your account.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** [permissionsConfiguration](#API_CreateCapacityProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateCapacityProvider-request-permissionsConfiguration"></a>
The permissions configuration for the capacity provider. This specifies the IAM role that AgentCore uses to manage the Amazon EC2 instances on your behalf.  
Type: [PermissionsConfiguration](API_PermissionsConfiguration.md) object  
Required: Yes

 ** [tags](#API_CreateCapacityProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-CreateCapacityProvider-request-tags"></a>
A map of tag keys and values to associate with the capacity provider. If you don't specify tags, the capacity provider is created with no tags.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## Response Syntax
<a name="API_CreateCapacityProvider_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "capacityProviderArn": "string",
   "capacityProviderId": "string",
   "name": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateCapacityProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [capacityProviderArn](#API_CreateCapacityProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateCapacityProvider-response-capacityProviderArn"></a>
The Amazon Resource Name (ARN) of the capacity provider.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:capacity-provider/[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}` 

 ** [capacityProviderId](#API_CreateCapacityProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateCapacityProvider-response-capacityProviderId"></a>
The unique identifier of the created capacity provider.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}` 

 ** [name](#API_CreateCapacityProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateCapacityProvider-response-name"></a>
The name of the capacity provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}` 

 ** [status](#API_CreateCapacityProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-CreateCapacityProvider-response-status"></a>
The current status of the capacity provider. For possible values, see `CapacityProviderStatus`.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | READY | DELETING | DELETE_FAILED` 

## Errors
<a name="API_CreateCapacityProvider_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** ConflictException **   
This exception is thrown when there is a conflict performing an operation  
HTTP Status Code: 409

 ** InternalServerException **   
This exception is thrown if there was an unexpected error during processing of request  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
This exception is thrown when a resource referenced by the operation does not exist  
HTTP Status Code: 404

 ** RetryableConflictException **   
The operation failed because of a conflicting request. Retry the request.  
HTTP Status Code: 409

 ** ServiceQuotaExceededException **   
This exception is thrown when a request is made beyond the service quota  
HTTP Status Code: 402

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_CreateCapacityProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/CreateCapacityProvider) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/CreateCapacityProvider) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CreateCapacityProvider) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/CreateCapacityProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CreateCapacityProvider) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/CreateCapacityProvider) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/CreateCapacityProvider) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/CreateCapacityProvider) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/CreateCapacityProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CreateCapacityProvider) 
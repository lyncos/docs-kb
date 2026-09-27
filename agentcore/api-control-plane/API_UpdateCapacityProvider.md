---
title: UpdateCapacityProvider
description: Updates a capacity provider. Only the description can be changed. To change other configuration, such as instance types, networking, or storage, create a new capacity provider.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_UpdateCapacityProvider.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# UpdateCapacityProvider
<a name="API_UpdateCapacityProvider"></a>

Updates a capacity provider. Only the description can be changed. To change other configuration, such as instance types, networking, or storage, create a new capacity provider.

## Request Syntax
<a name="API_UpdateCapacityProvider_RequestSyntax"></a>

```
PUT /capacity-providers/{{capacityProviderId}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": { 
      "optionalValue": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateCapacityProvider_RequestParameters"></a>

The request uses the following URI parameters.

 ** [capacityProviderId](#API_UpdateCapacityProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateCapacityProvider-request-uri-capacityProviderId"></a>
The unique identifier of the capacity provider to update.  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_UpdateCapacityProvider_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateCapacityProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateCapacityProvider-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_UpdateCapacityProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-UpdateCapacityProvider-request-description"></a>
The updated description of the capacity provider.  
Type: [UpdatedDescription](API_UpdatedDescription.md) object  
Required: No

## Response Syntax
<a name="API_UpdateCapacityProvider_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "capacityProviderArn": "string",
   "capacityProviderId": "string",
   "createdAt": "string",
   "lastUpdatedAt": "string",
   "name": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_UpdateCapacityProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [capacityProviderArn](#API_UpdateCapacityProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateCapacityProvider-response-capacityProviderArn"></a>
The Amazon Resource Name (ARN) of the capacity provider.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:capacity-provider/[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}` 

 ** [capacityProviderId](#API_UpdateCapacityProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateCapacityProvider-response-capacityProviderId"></a>
The unique identifier of the capacity provider.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}` 

 ** [createdAt](#API_UpdateCapacityProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateCapacityProvider-response-createdAt"></a>
The timestamp when the capacity provider was created.  
Type: Timestamp

 ** [lastUpdatedAt](#API_UpdateCapacityProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateCapacityProvider-response-lastUpdatedAt"></a>
The timestamp when the capacity provider was last updated.  
Type: Timestamp

 ** [name](#API_UpdateCapacityProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateCapacityProvider-response-name"></a>
The name of the capacity provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}` 

 ** [status](#API_UpdateCapacityProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-UpdateCapacityProvider-response-status"></a>
The current status of the capacity provider. For possible values, see `CapacityProviderStatus`.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | READY | DELETING | DELETE_FAILED` 

## Errors
<a name="API_UpdateCapacityProvider_Errors"></a>

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

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_UpdateCapacityProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/UpdateCapacityProvider) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/UpdateCapacityProvider) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdateCapacityProvider) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/UpdateCapacityProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdateCapacityProvider) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/UpdateCapacityProvider) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/UpdateCapacityProvider) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/UpdateCapacityProvider) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/UpdateCapacityProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdateCapacityProvider) 
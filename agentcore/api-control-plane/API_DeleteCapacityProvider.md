---
title: DeleteCapacityProvider
description: Deletes a capacity provider. Before you delete a capacity provider, disassociate all agent runtimes and runtime versions that reference it. If any references remain, the operation fails.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_DeleteCapacityProvider.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# DeleteCapacityProvider
<a name="API_DeleteCapacityProvider"></a>

Deletes a capacity provider. Before you delete a capacity provider, disassociate all agent runtimes and runtime versions that reference it. If any references remain, the operation fails.

## Request Syntax
<a name="API_DeleteCapacityProvider_RequestSyntax"></a>

```
DELETE /capacity-providers/{{capacityProviderId}}?clientToken={{clientToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteCapacityProvider_RequestParameters"></a>

The request uses the following URI parameters.

 ** [capacityProviderId](#API_DeleteCapacityProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeleteCapacityProvider-request-uri-capacityProviderId"></a>
The unique identifier of the capacity provider to delete.  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** [clientToken](#API_DeleteCapacityProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-DeleteCapacityProvider-request-uri-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}` 

## Request Body
<a name="API_DeleteCapacityProvider_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteCapacityProvider_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "capacityProviderId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DeleteCapacityProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [capacityProviderId](#API_DeleteCapacityProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteCapacityProvider-response-capacityProviderId"></a>
The unique identifier of the deleted capacity provider.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}` 

 ** [status](#API_DeleteCapacityProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-DeleteCapacityProvider-response-status"></a>
The current status of the capacity provider. For possible values, see `CapacityProviderStatus`.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | READY | DELETING | DELETE_FAILED` 

## Errors
<a name="API_DeleteCapacityProvider_Errors"></a>

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
<a name="API_DeleteCapacityProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/DeleteCapacityProvider) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/DeleteCapacityProvider) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/DeleteCapacityProvider) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/DeleteCapacityProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/DeleteCapacityProvider) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/DeleteCapacityProvider) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/DeleteCapacityProvider) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/DeleteCapacityProvider) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/DeleteCapacityProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/DeleteCapacityProvider) 
---
title: GetCapacityProvider
description: Retrieves information about a capacity provider, including its status, permissions configuration, and compute configuration.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetCapacityProvider.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# GetCapacityProvider
<a name="API_GetCapacityProvider"></a>

Retrieves information about a capacity provider, including its status, permissions configuration, and compute configuration.

## Request Syntax
<a name="API_GetCapacityProvider_RequestSyntax"></a>

```
GET /capacity-providers/{{capacityProviderId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCapacityProvider_RequestParameters"></a>

The request uses the following URI parameters.

 ** [capacityProviderId](#API_GetCapacityProvider_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetCapacityProvider-request-uri-capacityProviderId"></a>
The unique identifier of the capacity provider.  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_GetCapacityProvider_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCapacityProvider_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "capacityProviderArn": "string",
   "capacityProviderId": "string",
   "computeConfiguration": { ... },
   "createdAt": "string",
   "description": "string",
   "lastUpdatedAt": "string",
   "name": "string",
   "permissionsConfiguration": { 
      "capacityProviderOperatorRoleArn": "string"
   },
   "status": "string",
   "statusCode": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_GetCapacityProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [capacityProviderArn](#API_GetCapacityProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetCapacityProvider-response-capacityProviderArn"></a>
The Amazon Resource Name (ARN) of the capacity provider.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:capacity-provider/[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}` 

 ** [capacityProviderId](#API_GetCapacityProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetCapacityProvider-response-capacityProviderId"></a>
The unique identifier of the capacity provider.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}` 

 ** [computeConfiguration](#API_GetCapacityProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetCapacityProvider-response-computeConfiguration"></a>
The compute configuration for the capacity provider.  
Type: [ComputeConfiguration](API_ComputeConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [createdAt](#API_GetCapacityProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetCapacityProvider-response-createdAt"></a>
The timestamp when the capacity provider was created.  
Type: Timestamp

 ** [description](#API_GetCapacityProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetCapacityProvider-response-description"></a>
The description of the capacity provider, if one was provided.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [lastUpdatedAt](#API_GetCapacityProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetCapacityProvider-response-lastUpdatedAt"></a>
The timestamp when the capacity provider was last updated.  
Type: Timestamp

 ** [name](#API_GetCapacityProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetCapacityProvider-response-name"></a>
The name of the capacity provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}` 

 ** [permissionsConfiguration](#API_GetCapacityProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetCapacityProvider-response-permissionsConfiguration"></a>
The permissions configuration for the capacity provider.  
Type: [PermissionsConfiguration](API_PermissionsConfiguration.md) object

 ** [status](#API_GetCapacityProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetCapacityProvider-response-status"></a>
The current status of the capacity provider. For possible values, see `CapacityProviderStatus`.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | READY | DELETING | DELETE_FAILED` 

 ** [statusCode](#API_GetCapacityProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetCapacityProvider-response-statusCode"></a>
A reason code for a capacity provider that is not in the `READY` state. Use this code for programmatic error handling.  
Type: String  
Valid Values: `VALIDATION_ERROR | QUOTA_EXCEEDED | THROTTLED | INTERNAL_SERVER_EXCEPTION` 

 ** [statusReason](#API_GetCapacityProvider_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetCapacityProvider-response-statusReason"></a>
A human-readable message that describes why the capacity provider is not in the `READY` state. Because these messages can change, use `statusCode` for programmatic error handling.  
Type: String

## Errors
<a name="API_GetCapacityProvider_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** InternalServerException **   
This exception is thrown if there was an unexpected error during processing of request  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
This exception is thrown when a resource referenced by the operation does not exist  
HTTP Status Code: 404

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_GetCapacityProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetCapacityProvider) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetCapacityProvider) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetCapacityProvider) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetCapacityProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetCapacityProvider) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetCapacityProvider) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetCapacityProvider) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetCapacityProvider) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetCapacityProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetCapacityProvider) 
---
title: DeleteRegistry
description: 'Deletes a registry. Deletion is asynchronous: the registry transitions to the DELETING status and is removed along with its registry records.'
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_DeleteRegistry.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# DeleteRegistry
<a name="API_DeleteRegistry"></a>

Deletes a registry. Deletion is asynchronous: the registry transitions to the DELETING status and is removed along with its registry records.

## Request Syntax
<a name="API_DeleteRegistry_RequestSyntax"></a>

```
DELETE /registries/{{registryId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteRegistry_RequestParameters"></a>

The request uses the following URI parameters.

 ** [registryId](#API_DeleteRegistry_RequestSyntax) **   <a name="agentregistrycontrol-DeleteRegistry-request-uri-registryId"></a>
The identifier of the registry to delete (ARN or ID)  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

## Request Body
<a name="API_DeleteRegistry_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteRegistry_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "status": "string"
}
```

## Response Elements
<a name="API_DeleteRegistry_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [status](#API_DeleteRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-DeleteRegistry-response-status"></a>
Current status of the registry, set to DELETING when deletion is initiated  
Type: String  
Valid Values: `CREATING | READY | UPDATING | CREATE_FAILED | UPDATE_FAILED | DELETING | DELETE_FAILED` 

## Errors
<a name="API_DeleteRegistry_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The caller is not authorized to perform the requested action.  
HTTP Status Code: 403

 ** ConflictException **   
The request conflicts with the current state of the resource.  
HTTP Status Code: 409

 ** InternalServerException **   
The request failed due to an unexpected internal error; the caller may retry.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The requested resource was not found.  
HTTP Status Code: 404

 ** ThrottlingException **   
The request was denied due to request throttling; the caller may retry after a delay.  
HTTP Status Code: 429

 ** ValidationException **   
The request failed validation of one or more input fields.    
 ** fieldList **   
The list of input fields that failed validation.  
 ** reason **   
The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_DeleteRegistry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/DeleteRegistry) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/DeleteRegistry) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/DeleteRegistry) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/DeleteRegistry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/DeleteRegistry) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/DeleteRegistry) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/DeleteRegistry) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/DeleteRegistry) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/DeleteRegistry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/DeleteRegistry) 
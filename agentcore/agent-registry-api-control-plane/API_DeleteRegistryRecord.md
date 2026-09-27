---
title: DeleteRegistryRecord
description: Deletes a registry record
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_DeleteRegistryRecord.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# DeleteRegistryRecord
<a name="API_DeleteRegistryRecord"></a>

Deletes a registry record

## Request Syntax
<a name="API_DeleteRegistryRecord_RequestSyntax"></a>

```
DELETE /registries/{{registryId}}/records/{{recordId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteRegistryRecord_RequestParameters"></a>

The request uses the following URI parameters.

 ** [recordId](#API_DeleteRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-DeleteRegistryRecord-request-uri-recordId"></a>
The identifier of the registry record to delete (ARN or ID)  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/)?[a-zA-Z0-9]{12}`   
Required: Yes

 ** [registryId](#API_DeleteRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-DeleteRegistryRecord-request-uri-registryId"></a>
The identifier of the registry containing the record (ARN or ID)  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

## Request Body
<a name="API_DeleteRegistryRecord_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteRegistryRecord_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteRegistryRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteRegistryRecord_Errors"></a>

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
<a name="API_DeleteRegistryRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/DeleteRegistryRecord) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/DeleteRegistryRecord) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/DeleteRegistryRecord) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/DeleteRegistryRecord) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/DeleteRegistryRecord) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/DeleteRegistryRecord) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/DeleteRegistryRecord) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/DeleteRegistryRecord) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/DeleteRegistryRecord) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/DeleteRegistryRecord) 
---
title: UpdateRegistryRecordStatus
description: Updates the status of a registry record as part of the registry's curation workflow, for example to approve or reject a record that is pending approval, or to deprecate an approved record so that it is no longer discoverable
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_UpdateRegistryRecordStatus.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# UpdateRegistryRecordStatus
<a name="API_UpdateRegistryRecordStatus"></a>

Updates the status of a registry record as part of the registry's curation workflow, for example to approve or reject a record that is pending approval, or to deprecate an approved record so that it is no longer discoverable

## Request Syntax
<a name="API_UpdateRegistryRecordStatus_RequestSyntax"></a>

```
PATCH /registries/{{registryId}}/records/{{recordId}}/status HTTP/1.1
Content-type: application/json

{
   "status": "{{string}}",
   "statusReason": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateRegistryRecordStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [recordId](#API_UpdateRegistryRecordStatus_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecordStatus-request-uri-recordId"></a>
The identifier of the registry record to update the status of (ARN or ID)  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/)?[a-zA-Z0-9]{12}`   
Required: Yes

 ** [registryId](#API_UpdateRegistryRecordStatus_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecordStatus-request-uri-registryId"></a>
The identifier of the registry containing the record (ARN or ID)  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

## Request Body
<a name="API_UpdateRegistryRecordStatus_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [status](#API_UpdateRegistryRecordStatus_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecordStatus-request-status"></a>
The target status for the registry record  
Type: String  
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | REJECTED | DEPRECATED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED`   
Required: Yes

 ** [statusReason](#API_UpdateRegistryRecordStatus_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecordStatus-request-statusReason"></a>
The reason for the status change, for example why the record was approved, rejected, or deprecated  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 255.  
Required: Yes

## Response Syntax
<a name="API_UpdateRegistryRecordStatus_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "recordArn": "string",
   "recordId": "string",
   "registryArn": "string",
   "status": "string",
   "statusReason": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_UpdateRegistryRecordStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [recordArn](#API_UpdateRegistryRecordStatus_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecordStatus-response-recordArn"></a>
The ARN of the registry record  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}` 

 ** [recordId](#API_UpdateRegistryRecordStatus_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecordStatus-response-recordId"></a>
The ID of the registry record  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[a-zA-Z0-9]{12}` 

 ** [registryArn](#API_UpdateRegistryRecordStatus_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecordStatus-response-registryArn"></a>
The ARN of the registry  
Type: String  
Length Constraints: Minimum length of 46. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}` 

 ** [status](#API_UpdateRegistryRecordStatus_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecordStatus-response-status"></a>
The resulting status of the registry record  
Type: String  
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | REJECTED | DEPRECATED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED` 

 ** [statusReason](#API_UpdateRegistryRecordStatus_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecordStatus-response-statusReason"></a>
The reason for the status change  
Type: String

 ** [updatedAt](#API_UpdateRegistryRecordStatus_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecordStatus-response-updatedAt"></a>
The timestamp when the record was last updated  
Type: Timestamp

## Errors
<a name="API_UpdateRegistryRecordStatus_Errors"></a>

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
<a name="API_UpdateRegistryRecordStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/UpdateRegistryRecordStatus) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/UpdateRegistryRecordStatus) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdateRegistryRecordStatus) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/UpdateRegistryRecordStatus) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdateRegistryRecordStatus) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/UpdateRegistryRecordStatus) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/UpdateRegistryRecordStatus) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/UpdateRegistryRecordStatus) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/UpdateRegistryRecordStatus) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdateRegistryRecordStatus) 
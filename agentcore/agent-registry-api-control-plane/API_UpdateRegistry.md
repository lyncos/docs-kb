---
title: UpdateRegistry
description: 'Updates an existing registry. This operation uses PATCH semantics: specify only the fields you want to change, and omit the rest to leave them unchanged. Updates are applied asynchronously and the registry transitions to the UPDATING status while they are processed.'
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_UpdateRegistry.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# UpdateRegistry
<a name="API_UpdateRegistry"></a>

Updates an existing registry. This operation uses PATCH semantics: specify only the fields you want to change, and omit the rest to leave them unchanged. Updates are applied asynchronously and the registry transitions to the UPDATING status while they are processed.

## Request Syntax
<a name="API_UpdateRegistry_RequestSyntax"></a>

```
PATCH /registries/{{registryId}} HTTP/1.1
Content-type: application/json

{
   "approvalConfiguration": { 
      "optionalValue": { 
         "autoApprovalRules": [ "{{string}}" ]
      }
   },
   "autoDetectionConfiguration": { 
      "optionalValue": { 
         "enabled": {{boolean}},
         "scope": "{{string}}"
      }
   },
   "description": { 
      "optionalValue": "{{string}}"
   },
   "discoveryConfiguration": { 
      "authorizerConfiguration": { 
         "optionalValue": { ... }
      }
   },
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateRegistry_RequestParameters"></a>

The request uses the following URI parameters.

 ** [registryId](#API_UpdateRegistry_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-request-uri-registryId"></a>
The identifier of the registry to update (ARN or ID)  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

## Request Body
<a name="API_UpdateRegistry_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [approvalConfiguration](#API_UpdateRegistry_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-request-approvalConfiguration"></a>
The updated approval configuration. The change applies only to records that move to PENDING\_APPROVAL after the update; records already in PENDING\_APPROVAL are unaffected.  
Type: [UpdatedApprovalConfiguration](API_UpdatedApprovalConfiguration.md) object  
Required: No

 ** [autoDetectionConfiguration](#API_UpdateRegistry_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-request-autoDetectionConfiguration"></a>
The updated auto-detection configuration for the registry, with PATCH semantics. Omit this field to leave the current configuration unchanged. Supply an empty wrapper to unset it. Supply `optionalValue` to replace it.  
Type: [UpdatedAutoDetectionConfiguration](API_UpdatedAutoDetectionConfiguration.md) object  
Required: No

 ** [description](#API_UpdateRegistry_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-request-description"></a>
The updated description of the registry  
Type: [UpdatedDescription](API_UpdatedDescription.md) object  
Required: No

 ** [discoveryConfiguration](#API_UpdateRegistry_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-request-discoveryConfiguration"></a>
The updated discovery configuration. Changing the discovery authorization can break existing consumers that rely on the previous authorization type.  
Type: [UpdatedDiscoveryConfiguration](API_UpdatedDiscoveryConfiguration.md) object  
Required: No

 ** [name](#API_UpdateRegistry_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-request-name"></a>
The updated name of the registry  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`   
Required: No

## Response Syntax
<a name="API_UpdateRegistry_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "approvalConfiguration": { 
      "autoApprovalRules": [ "string" ]
   },
   "autoDetection": { 
      "configuration": { 
         "enabled": boolean,
         "scope": "string"
      },
      "status": "string",
      "statusReason": "string"
   },
   "createdAt": "string",
   "description": "string",
   "discoveryConfiguration": { 
      "authorizerConfiguration": { ... },
      "authorizerType": "string"
   },
   "encryptionConfiguration": { 
      "kmsKeyArn": "string"
   },
   "name": "string",
   "registryArn": "string",
   "registryId": "string",
   "status": "string",
   "statusReason": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_UpdateRegistry_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [approvalConfiguration](#API_UpdateRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-response-approvalConfiguration"></a>
Approval configuration for registry records  
Type: [ApprovalConfiguration](API_ApprovalConfiguration.md) object

 ** [autoDetection](#API_UpdateRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-response-autoDetection"></a>
The registry's auto-detection properties, including the requested configuration and the current detection status. Present only when auto-detection was configured for the registry.  
Type: [AutoDetection](API_AutoDetection.md) object

 ** [createdAt](#API_UpdateRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-response-createdAt"></a>
The timestamp when the registry was created  
Type: Timestamp

 ** [description](#API_UpdateRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-response-description"></a>
The description of the registry  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [discoveryConfiguration](#API_UpdateRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-response-discoveryConfiguration"></a>
Discovery configuration for the registry  
Type: [DiscoveryConfiguration](API_DiscoveryConfiguration.md) object

 ** [encryptionConfiguration](#API_UpdateRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-response-encryptionConfiguration"></a>
The server-side encryption configuration for the registry. Appears only when a customer-managed AWS KMS key encrypts the registry.  
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object

 ** [name](#API_UpdateRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-response-name"></a>
The name of the registry  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*` 

 ** [registryArn](#API_UpdateRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-response-registryArn"></a>
The ARN of the registry  
Type: String  
Length Constraints: Minimum length of 46. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}` 

 ** [registryId](#API_UpdateRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-response-registryId"></a>
The unique identifier of the registry  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 16.  
Pattern: `[a-zA-Z0-9]{12,16}` 

 ** [status](#API_UpdateRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-response-status"></a>
Current status of the registry  
Type: String  
Valid Values: `CREATING | READY | UPDATING | CREATE_FAILED | UPDATE_FAILED | DELETING | DELETE_FAILED` 

 ** [statusReason](#API_UpdateRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-response-statusReason"></a>
The reason for the current status. Typically populated when the status indicates a failure state.  
Type: String

 ** [updatedAt](#API_UpdateRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-response-updatedAt"></a>
The timestamp when the registry was last updated  
Type: Timestamp

## Errors
<a name="API_UpdateRegistry_Errors"></a>

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

 ** ServiceQuotaExceededException **   
The request would exceed a service quota.  
HTTP Status Code: 402

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
<a name="API_UpdateRegistry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/UpdateRegistry) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/UpdateRegistry) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdateRegistry) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/UpdateRegistry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdateRegistry) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/UpdateRegistry) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/UpdateRegistry) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/UpdateRegistry) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/UpdateRegistry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdateRegistry) 
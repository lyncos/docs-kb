---
title: GetRegistry
description: Gets a registry by identifier (ARN or ID)
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_GetRegistry.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# GetRegistry
<a name="API_GetRegistry"></a>

Gets a registry by identifier (ARN or ID)

## Request Syntax
<a name="API_GetRegistry_RequestSyntax"></a>

```
GET /registries/{{registryId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRegistry_RequestParameters"></a>

The request uses the following URI parameters.

 ** [registryId](#API_GetRegistry_RequestSyntax) **   <a name="agentregistrycontrol-GetRegistry-request-uri-registryId"></a>
The identifier of the registry to retrieve (ARN or ID)  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

## Request Body
<a name="API_GetRegistry_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRegistry_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_GetRegistry_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [approvalConfiguration](#API_GetRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistry-response-approvalConfiguration"></a>
Approval configuration for registry records  
Type: [ApprovalConfiguration](API_ApprovalConfiguration.md) object

 ** [autoDetection](#API_GetRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistry-response-autoDetection"></a>
The registry's auto-detection properties, including the requested configuration and the current detection status. Present only when auto-detection was configured for the registry.  
Type: [AutoDetection](API_AutoDetection.md) object

 ** [createdAt](#API_GetRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistry-response-createdAt"></a>
The timestamp when the registry was created  
Type: Timestamp

 ** [description](#API_GetRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistry-response-description"></a>
The description of the registry  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [discoveryConfiguration](#API_GetRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistry-response-discoveryConfiguration"></a>
Discovery configuration for the registry  
Type: [DiscoveryConfiguration](API_DiscoveryConfiguration.md) object

 ** [encryptionConfiguration](#API_GetRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistry-response-encryptionConfiguration"></a>
The server-side encryption configuration for the registry. Appears only when a customer-managed AWS KMS key encrypts the registry.  
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object

 ** [name](#API_GetRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistry-response-name"></a>
The name of the registry  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*` 

 ** [registryArn](#API_GetRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistry-response-registryArn"></a>
The ARN of the registry  
Type: String  
Length Constraints: Minimum length of 46. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}` 

 ** [registryId](#API_GetRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistry-response-registryId"></a>
The unique identifier of the registry  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 16.  
Pattern: `[a-zA-Z0-9]{12,16}` 

 ** [status](#API_GetRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistry-response-status"></a>
Current status of the registry  
Type: String  
Valid Values: `CREATING | READY | UPDATING | CREATE_FAILED | UPDATE_FAILED | DELETING | DELETE_FAILED` 

 ** [statusReason](#API_GetRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistry-response-statusReason"></a>
The reason for the current status. Typically populated when the status indicates a failure state.  
Type: String

 ** [updatedAt](#API_GetRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistry-response-updatedAt"></a>
The timestamp when the registry was last updated  
Type: Timestamp

## Errors
<a name="API_GetRegistry_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The caller is not authorized to perform the requested action.  
HTTP Status Code: 403

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
<a name="API_GetRegistry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/GetRegistry) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/GetRegistry) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/GetRegistry) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/GetRegistry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/GetRegistry) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/GetRegistry) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/GetRegistry) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/GetRegistry) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/GetRegistry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/GetRegistry) 
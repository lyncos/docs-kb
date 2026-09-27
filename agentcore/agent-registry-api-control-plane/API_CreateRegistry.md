---
title: CreateRegistry
description: 'Creates a new registry, a catalog that organizes registry records and defines their discovery authorization and record approval behavior. Creation is asynchronous: the registry begins in the CREATING status and becomes usable once it reaches READY.'
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_CreateRegistry.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# CreateRegistry
<a name="API_CreateRegistry"></a>

Creates a new registry, a catalog that organizes registry records and defines their discovery authorization and record approval behavior. Creation is asynchronous: the registry begins in the CREATING status and becomes usable once it reaches READY.

## Request Syntax
<a name="API_CreateRegistry_RequestSyntax"></a>

```
POST /registries HTTP/1.1
Content-type: application/json

{
   "approvalConfiguration": { 
      "autoApprovalRules": [ "{{string}}" ]
   },
   "autoDetectionConfiguration": { 
      "enabled": {{boolean}},
      "scope": "{{string}}"
   },
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "discoveryConfiguration": { 
      "authorizerConfiguration": { ... },
      "authorizerType": "{{string}}"
   },
   "encryptionConfiguration": { 
      "kmsKeyArn": "{{string}}"
   },
   "name": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

## URI Request Parameters
<a name="API_CreateRegistry_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateRegistry_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [approvalConfiguration](#API_CreateRegistry_RequestSyntax) **   <a name="agentregistrycontrol-CreateRegistry-request-approvalConfiguration"></a>
Approval configuration for registry records  
Type: [ApprovalConfiguration](API_ApprovalConfiguration.md) object  
Required: No

 ** [autoDetectionConfiguration](#API_CreateRegistry_RequestSyntax) **   <a name="agentregistrycontrol-CreateRegistry-request-autoDetectionConfiguration"></a>
The optional auto-detection configuration for the registry. When provided, the registry is automatically populated with resources discovered according to the configuration. Omit this field for registries whose records are managed exclusively through the Agent Registry Control API.  
Type: [AutoDetectionConfiguration](API_AutoDetectionConfiguration.md) object  
Required: No

 ** [clientToken](#API_CreateRegistry_RequestSyntax) **   <a name="agentregistrycontrol-CreateRegistry-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_CreateRegistry_RequestSyntax) **   <a name="agentregistrycontrol-CreateRegistry-request-description"></a>
The description of the registry  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** [discoveryConfiguration](#API_CreateRegistry_RequestSyntax) **   <a name="agentregistrycontrol-CreateRegistry-request-discoveryConfiguration"></a>
Discovery configuration for the registry  
Type: [DiscoveryConfiguration](API_DiscoveryConfiguration.md) object  
Required: No

 ** [encryptionConfiguration](#API_CreateRegistry_RequestSyntax) **   <a name="agentregistrycontrol-CreateRegistry-request-encryptionConfiguration"></a>
The optional server-side encryption configuration for the registry. When you provide this field, the specified customer-managed AWS KMS key encrypts the registry's content. Omit this field to use an AWS-owned encryption key. You cannot change the encryption configuration after registry creation.  
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object  
Required: No

 ** [name](#API_CreateRegistry_RequestSyntax) **   <a name="agentregistrycontrol-CreateRegistry-request-name"></a>
The name of the registry  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`   
Required: Yes

 ** [tags](#API_CreateRegistry_RequestSyntax) **   <a name="agentregistrycontrol-CreateRegistry-request-tags"></a>
Tags to associate with the registry  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## Response Syntax
<a name="API_CreateRegistry_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "registryArn": "string"
}
```

## Response Elements
<a name="API_CreateRegistry_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [registryArn](#API_CreateRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-CreateRegistry-response-registryArn"></a>
The ARN of the created registry  
Type: String  
Length Constraints: Minimum length of 46. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}` 

## Errors
<a name="API_CreateRegistry_Errors"></a>

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
<a name="API_CreateRegistry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/CreateRegistry) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/CreateRegistry) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/CreateRegistry) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/CreateRegistry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/CreateRegistry) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/CreateRegistry) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/CreateRegistry) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/CreateRegistry) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/CreateRegistry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/CreateRegistry) 
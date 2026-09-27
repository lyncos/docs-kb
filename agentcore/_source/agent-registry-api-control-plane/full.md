# AgentRegistry Control Plane API Reference AgentRegistry Control Plane API Reference

-----
*****Copyright &copy; Amazon Web Services, Inc. and/or its affiliates. All rights reserved.*****

-----
Amazon's trademarks and trade dress may not be used in
connection with any product or service that is not Amazon's,
in any manner that is likely to cause confusion among customers,
or in any manner that disparages or discredits Amazon. All other
trademarks not owned by Amazon are the property of their respective
owners, who may or may not be affiliated with, connected to, or
sponsored by Amazon.

-----
## Contents
+ [Welcome](#Welcome)
+ [Actions](#API_Operations)
   + [CreateRegistry](#API_CreateRegistry)
   + [CreateRegistryRecord](#API_CreateRegistryRecord)
   + [DeleteRegistry](#API_DeleteRegistry)
   + [DeleteRegistryRecord](#API_DeleteRegistryRecord)
   + [GetRegistry](#API_GetRegistry)
   + [GetRegistryRecord](#API_GetRegistryRecord)
   + [ListRegistries](#API_ListRegistries)
   + [ListRegistryRecords](#API_ListRegistryRecords)
   + [ListTagsForResource](#API_ListTagsForResource)
   + [SubmitRegistryRecordForApproval](#API_SubmitRegistryRecordForApproval)
   + [TagResource](#API_TagResource)
   + [UntagResource](#API_UntagResource)
   + [UpdateRegistry](#API_UpdateRegistry)
   + [UpdateRegistryRecord](#API_UpdateRegistryRecord)
   + [UpdateRegistryRecordStatus](#API_UpdateRegistryRecordStatus)
+ [Data Types](#API_Types)
   + [A2aAgentCardDescriptor](#API_A2aAgentCardDescriptor)
   + [AgentCoreGatewaySourceDetails](#API_AgentCoreGatewaySourceDetails)
   + [AgentCoreRuntimeProtocolConfiguration](#API_AgentCoreRuntimeProtocolConfiguration)
   + [AgentCoreRuntimeSourceDetails](#API_AgentCoreRuntimeSourceDetails)
   + [AgentSkillsAdditionalData](#API_AgentSkillsAdditionalData)
   + [AgentSkillsDefinitionDescriptor](#API_AgentSkillsDefinitionDescriptor)
   + [AgentSkillsMdDescriptor](#API_AgentSkillsMdDescriptor)
   + [AgUiDescriptor](#API_AgUiDescriptor)
   + [ApprovalConfiguration](#API_ApprovalConfiguration)
   + [AuthorizerConfiguration](#API_AuthorizerConfiguration)
   + [AuthorizingClaimMatchValueType](#API_AuthorizingClaimMatchValueType)
   + [AutoDetection](#API_AutoDetection)
   + [AutoDetectionConfiguration](#API_AutoDetectionConfiguration)
   + [ClaimMatchValueType](#API_ClaimMatchValueType)
   + [CustomClaimValidationType](#API_CustomClaimValidationType)
   + [CustomDescriptor](#API_CustomDescriptor)
   + [CustomJWTAuthorizerConfiguration](#API_CustomJWTAuthorizerConfiguration)
   + [Descriptors](#API_Descriptors)
   + [DescriptorSource](#API_DescriptorSource)
   + [DescriptorSourceFromUrl](#API_DescriptorSourceFromUrl)
   + [DiscoveryConfiguration](#API_DiscoveryConfiguration)
   + [EncryptionConfiguration](#API_EncryptionConfiguration)
   + [HttpDescriptor](#API_HttpDescriptor)
   + [ManagedVpcResource](#API_ManagedVpcResource)
   + [McpServerAdditionalData](#API_McpServerAdditionalData)
   + [McpServerDescriptor](#API_McpServerDescriptor)
   + [McpToolsDescriptor](#API_McpToolsDescriptor)
   + [PrivateEndpoint](#API_PrivateEndpoint)
   + [PrivateEndpointOverride](#API_PrivateEndpointOverride)
   + [Provenance](#API_Provenance)
   + [ProvenanceSummary](#API_ProvenanceSummary)
   + [RegistryFilter](#API_RegistryFilter)
   + [RegistryRecordCredentialProviderConfiguration](#API_RegistryRecordCredentialProviderConfiguration)
   + [RegistryRecordCredentialProviderUnion](#API_RegistryRecordCredentialProviderUnion)
   + [RegistryRecordFilter](#API_RegistryRecordFilter)
   + [RegistryRecordIamCredentialProvider](#API_RegistryRecordIamCredentialProvider)
   + [RegistryRecordOAuthCredentialProvider](#API_RegistryRecordOAuthCredentialProvider)
   + [RegistryRecordSummary](#API_RegistryRecordSummary)
   + [RegistrySummary](#API_RegistrySummary)
   + [SelfManagedLatticeResource](#API_SelfManagedLatticeResource)
   + [SourceDetails](#API_SourceDetails)
   + [UpdatedA2aAgentCardDescriptor](#API_UpdatedA2aAgentCardDescriptor)
   + [UpdatedA2aAgentCardDescriptorFields](#API_UpdatedA2aAgentCardDescriptorFields)
   + [UpdatedAgentSkillsAdditionalData](#API_UpdatedAgentSkillsAdditionalData)
   + [UpdatedAgentSkillsAdditionalDataFields](#API_UpdatedAgentSkillsAdditionalDataFields)
   + [UpdatedAgentSkillsDefinitionDescriptor](#API_UpdatedAgentSkillsDefinitionDescriptor)
   + [UpdatedAgentSkillsDefinitionDescriptorFields](#API_UpdatedAgentSkillsDefinitionDescriptorFields)
   + [UpdatedAgentSkillsMdDescriptor](#API_UpdatedAgentSkillsMdDescriptor)
   + [UpdatedAgentSkillsMdDescriptorFields](#API_UpdatedAgentSkillsMdDescriptorFields)
   + [UpdatedAgUiDescriptor](#API_UpdatedAgUiDescriptor)
   + [UpdatedAgUiDescriptorFields](#API_UpdatedAgUiDescriptorFields)
   + [UpdatedApprovalConfiguration](#API_UpdatedApprovalConfiguration)
   + [UpdatedAuthorizerConfiguration](#API_UpdatedAuthorizerConfiguration)
   + [UpdatedAutoDetectionConfiguration](#API_UpdatedAutoDetectionConfiguration)
   + [UpdatedCustomDescriptor](#API_UpdatedCustomDescriptor)
   + [UpdatedCustomDescriptorFields](#API_UpdatedCustomDescriptorFields)
   + [UpdatedDataSchemaVersion](#API_UpdatedDataSchemaVersion)
   + [UpdatedDescription](#API_UpdatedDescription)
   + [UpdatedDescriptorData](#API_UpdatedDescriptorData)
   + [UpdatedDescriptors](#API_UpdatedDescriptors)
   + [UpdatedDescriptorsFields](#API_UpdatedDescriptorsFields)
   + [UpdatedDescriptorSource](#API_UpdatedDescriptorSource)
   + [UpdatedDiscoveryConfiguration](#API_UpdatedDiscoveryConfiguration)
   + [UpdatedDisplayName](#API_UpdatedDisplayName)
   + [UpdatedHttpDescriptor](#API_UpdatedHttpDescriptor)
   + [UpdatedHttpDescriptorFields](#API_UpdatedHttpDescriptorFields)
   + [UpdatedMcpServerAdditionalData](#API_UpdatedMcpServerAdditionalData)
   + [UpdatedMcpServerAdditionalDataFields](#API_UpdatedMcpServerAdditionalDataFields)
   + [UpdatedMcpServerDescriptor](#API_UpdatedMcpServerDescriptor)
   + [UpdatedMcpServerDescriptorFields](#API_UpdatedMcpServerDescriptorFields)
   + [UpdatedMcpToolsDescriptor](#API_UpdatedMcpToolsDescriptor)
   + [UpdatedMcpToolsDescriptorFields](#API_UpdatedMcpToolsDescriptorFields)
   + [ValidationExceptionField](#API_ValidationExceptionField)
   + [WorkloadIdentityDetails](#API_WorkloadIdentityDetails)
+ [Common Parameters](#CommonParameters)
+ [Common Error Types](#CommonErrors)

-----



# Welcome
<a name="Welcome"></a>

 AWS Agent Registry is a managed catalog for publishing and discovering resources such as MCP servers, agents, and agent skills. Agent Registry Control is its control-plane API: use it to create and manage registries and the records they contain, configure discovery and authorization, govern record approval and curation workflows, and manage automatic detection of resources. Data-plane search and MCP invocation operations are provided by the companion Agent Registry API.

This document was last published on September 25, 2026. 

# Actions
<a name="API_Operations"></a>

The following actions are supported:
+  [CreateRegistry](#API_CreateRegistry) 
+  [CreateRegistryRecord](#API_CreateRegistryRecord) 
+  [DeleteRegistry](#API_DeleteRegistry) 
+  [DeleteRegistryRecord](#API_DeleteRegistryRecord) 
+  [GetRegistry](#API_GetRegistry) 
+  [GetRegistryRecord](#API_GetRegistryRecord) 
+  [ListRegistries](#API_ListRegistries) 
+  [ListRegistryRecords](#API_ListRegistryRecords) 
+  [ListTagsForResource](#API_ListTagsForResource) 
+  [SubmitRegistryRecordForApproval](#API_SubmitRegistryRecordForApproval) 
+  [TagResource](#API_TagResource) 
+  [UntagResource](#API_UntagResource) 
+  [UpdateRegistry](#API_UpdateRegistry) 
+  [UpdateRegistryRecord](#API_UpdateRegistryRecord) 
+  [UpdateRegistryRecordStatus](#API_UpdateRegistryRecordStatus) 

## CreateRegistry
<a name="API_CreateRegistry"></a>

Creates a new registry, a catalog that organizes registry records and defines their discovery authorization and record approval behavior. Creation is asynchronous: the registry begins in the CREATING status and becomes usable once it reaches READY.

### Request Syntax
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

### URI Request Parameters
<a name="API_CreateRegistry_RequestParameters"></a>

The request does not use any URI parameters.

### Request Body
<a name="API_CreateRegistry_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [approvalConfiguration](#API_CreateRegistry_RequestSyntax) **   <a name="agentregistrycontrol-CreateRegistry-request-approvalConfiguration"></a>
Approval configuration for registry records  
Type: [ApprovalConfiguration](#API_ApprovalConfiguration) object  
Required: No

 ** [autoDetectionConfiguration](#API_CreateRegistry_RequestSyntax) **   <a name="agentregistrycontrol-CreateRegistry-request-autoDetectionConfiguration"></a>
The optional auto-detection configuration for the registry. When provided, the registry is automatically populated with resources discovered according to the configuration. Omit this field for registries whose records are managed exclusively through the Agent Registry Control API.  
Type: [AutoDetectionConfiguration](#API_AutoDetectionConfiguration) object  
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
Type: [DiscoveryConfiguration](#API_DiscoveryConfiguration) object  
Required: No

 ** [encryptionConfiguration](#API_CreateRegistry_RequestSyntax) **   <a name="agentregistrycontrol-CreateRegistry-request-encryptionConfiguration"></a>
The optional server-side encryption configuration for the registry. When you provide this field, the specified customer-managed AWS KMS key encrypts the registry's content. Omit this field to use an AWS-owned encryption key. You cannot change the encryption configuration after registry creation.  
Type: [EncryptionConfiguration](#API_EncryptionConfiguration) object  
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

### Response Syntax
<a name="API_CreateRegistry_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "registryArn": "string"
}
```

### Response Elements
<a name="API_CreateRegistry_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [registryArn](#API_CreateRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-CreateRegistry-response-registryArn"></a>
The ARN of the created registry  
Type: String  
Length Constraints: Minimum length of 46. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}` 

### Errors
<a name="API_CreateRegistry_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

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

### See Also
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

## CreateRegistryRecord
<a name="API_CreateRegistryRecord"></a>

Creates a registry record within a registry. A registry record describes a discoverable resource, such as an MCP server, an agent, an agent skill, or a custom resource. Creation is asynchronous: the record is returned with the CREATING status while it is processed.

### Request Syntax
<a name="API_CreateRegistryRecord_RequestSyntax"></a>

```
POST /registries/{{registryId}}/records HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "descriptors": { 
      "a2aAgentCard": { 
         "data": "{{string}}",
         "dataSchemaVersion": "{{string}}",
         "source": { 
            "fromUrl": { 
               "credentialProviderConfigurations": [ 
                  { 
                     "credentialProvider": { ... },
                     "credentialProviderType": "{{string}}"
                  }
               ],
               "url": "{{string}}"
            }
         }
      },
      "agentSkillsDefinition": { 
         "additionalData": { 
            "skillMd": { 
               "data": "{{string}}",
               "dataSchemaVersion": "{{string}}",
               "source": { 
                  "fromUrl": { 
                     "credentialProviderConfigurations": [ 
                        { 
                           "credentialProvider": { ... },
                           "credentialProviderType": "{{string}}"
                        }
                     ],
                     "url": "{{string}}"
                  }
               }
            }
         },
         "data": "{{string}}",
         "dataSchemaVersion": "{{string}}"
      },
      "agui": { 
         "source": { 
            "fromUrl": { 
               "credentialProviderConfigurations": [ 
                  { 
                     "credentialProvider": { ... },
                     "credentialProviderType": "{{string}}"
                  }
               ],
               "url": "{{string}}"
            }
         }
      },
      "custom": { 
         "data": "{{string}}"
      },
      "http": { 
         "source": { 
            "fromUrl": { 
               "credentialProviderConfigurations": [ 
                  { 
                     "credentialProvider": { ... },
                     "credentialProviderType": "{{string}}"
                  }
               ],
               "url": "{{string}}"
            }
         }
      },
      "mcpServer": { 
         "additionalData": { 
            "tools": { 
               "data": "{{string}}",
               "dataSchemaVersion": "{{string}}"
            }
         },
         "data": "{{string}}",
         "dataSchemaVersion": "{{string}}",
         "source": { 
            "fromUrl": { 
               "credentialProviderConfigurations": [ 
                  { 
                     "credentialProvider": { ... },
                     "credentialProviderType": "{{string}}"
                  }
               ],
               "url": "{{string}}"
            }
         }
      }
   },
   "displayName": "{{string}}",
   "name": "{{string}}",
   "provenance": [ 
      { 
         "relation": "{{string}}",
         "sourceDetails": { ... },
         "sourceId": "{{string}}",
         "sourceType": "{{string}}"
      }
   ],
   "recordType": "{{string}}",
   "recordVersion": "{{string}}",
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

### URI Request Parameters
<a name="API_CreateRegistryRecord_RequestParameters"></a>

The request uses the following URI parameters.

 ** [registryId](#API_CreateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-CreateRegistryRecord-request-uri-registryId"></a>
The identifier of the registry in which to create the record (ARN or ID)  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

### Request Body
<a name="API_CreateRegistryRecord_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-CreateRegistryRecord-request-clientToken"></a>
Client token for idempotency  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [description](#API_CreateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-CreateRegistryRecord-request-description"></a>
The description of the registry record  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** [descriptors](#API_CreateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-CreateRegistryRecord-request-descriptors"></a>
The typed descriptor content for the registry record  
Type: [Descriptors](#API_Descriptors) object  
Required: Yes

 ** [displayName](#API_CreateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-CreateRegistryRecord-request-displayName"></a>
The human-readable display name of the registry record  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** [name](#API_CreateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-CreateRegistryRecord-request-name"></a>
The name of the registry record  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`   
Required: Yes

 ** [provenance](#API_CreateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-CreateRegistryRecord-request-provenance"></a>
The provenance lineage entries for the registry record. This field is reserved for the AWS Agent Registry auto-detection service principal. Requests that include this field from other callers are rejected.  
Type: Array of [Provenance](#API_Provenance) objects  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Required: No

 ** [recordType](#API_CreateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-CreateRegistryRecord-request-recordType"></a>
The type of the registry record, which determines the descriptor format  
Type: String  
Valid Values: `MCP | AGENT | CUSTOM | SKILL | GATEWAY`   
Required: Yes

 ** [recordVersion](#API_CreateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-CreateRegistryRecord-request-recordVersion"></a>
The version of the registry record  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9.-]+`   
Required: No

 ** [tags](#API_CreateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-CreateRegistryRecord-request-tags"></a>
Tags to associate with the registry record  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

### Response Syntax
<a name="API_CreateRegistryRecord_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "recordArn": "string",
   "status": "string"
}
```

### Response Elements
<a name="API_CreateRegistryRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [recordArn](#API_CreateRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-CreateRegistryRecord-response-recordArn"></a>
The ARN of the created registry record  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}` 

 ** [status](#API_CreateRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-CreateRegistryRecord-response-status"></a>
The status of the registry record, set to CREATING while the asynchronous workflow is in progress  
Type: String  
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | REJECTED | DEPRECATED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED` 

### Errors
<a name="API_CreateRegistryRecord_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

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

### See Also
<a name="API_CreateRegistryRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/CreateRegistryRecord) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/CreateRegistryRecord) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/CreateRegistryRecord) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/CreateRegistryRecord) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/CreateRegistryRecord) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/CreateRegistryRecord) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/CreateRegistryRecord) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/CreateRegistryRecord) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/CreateRegistryRecord) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/CreateRegistryRecord) 

## DeleteRegistry
<a name="API_DeleteRegistry"></a>

Deletes a registry. Deletion is asynchronous: the registry transitions to the DELETING status and is removed along with its registry records.

### Request Syntax
<a name="API_DeleteRegistry_RequestSyntax"></a>

```
DELETE /registries/{{registryId}} HTTP/1.1
```

### URI Request Parameters
<a name="API_DeleteRegistry_RequestParameters"></a>

The request uses the following URI parameters.

 ** [registryId](#API_DeleteRegistry_RequestSyntax) **   <a name="agentregistrycontrol-DeleteRegistry-request-uri-registryId"></a>
The identifier of the registry to delete (ARN or ID)  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

### Request Body
<a name="API_DeleteRegistry_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_DeleteRegistry_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "status": "string"
}
```

### Response Elements
<a name="API_DeleteRegistry_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [status](#API_DeleteRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-DeleteRegistry-response-status"></a>
Current status of the registry, set to DELETING when deletion is initiated  
Type: String  
Valid Values: `CREATING | READY | UPDATING | CREATE_FAILED | UPDATE_FAILED | DELETING | DELETE_FAILED` 

### Errors
<a name="API_DeleteRegistry_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

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

### See Also
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

## DeleteRegistryRecord
<a name="API_DeleteRegistryRecord"></a>

Deletes a registry record

### Request Syntax
<a name="API_DeleteRegistryRecord_RequestSyntax"></a>

```
DELETE /registries/{{registryId}}/records/{{recordId}} HTTP/1.1
```

### URI Request Parameters
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

### Request Body
<a name="API_DeleteRegistryRecord_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_DeleteRegistryRecord_ResponseSyntax"></a>

```
HTTP/1.1 200
```

### Response Elements
<a name="API_DeleteRegistryRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

### Errors
<a name="API_DeleteRegistryRecord_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

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

### See Also
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

## GetRegistry
<a name="API_GetRegistry"></a>

Gets a registry by identifier (ARN or ID)

### Request Syntax
<a name="API_GetRegistry_RequestSyntax"></a>

```
GET /registries/{{registryId}} HTTP/1.1
```

### URI Request Parameters
<a name="API_GetRegistry_RequestParameters"></a>

The request uses the following URI parameters.

 ** [registryId](#API_GetRegistry_RequestSyntax) **   <a name="agentregistrycontrol-GetRegistry-request-uri-registryId"></a>
The identifier of the registry to retrieve (ARN or ID)  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

### Request Body
<a name="API_GetRegistry_RequestBody"></a>

The request does not have a request body.

### Response Syntax
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

### Response Elements
<a name="API_GetRegistry_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [approvalConfiguration](#API_GetRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistry-response-approvalConfiguration"></a>
Approval configuration for registry records  
Type: [ApprovalConfiguration](#API_ApprovalConfiguration) object

 ** [autoDetection](#API_GetRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistry-response-autoDetection"></a>
The registry's auto-detection properties, including the requested configuration and the current detection status. Present only when auto-detection was configured for the registry.  
Type: [AutoDetection](#API_AutoDetection) object

 ** [createdAt](#API_GetRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistry-response-createdAt"></a>
The timestamp when the registry was created  
Type: Timestamp

 ** [description](#API_GetRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistry-response-description"></a>
The description of the registry  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [discoveryConfiguration](#API_GetRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistry-response-discoveryConfiguration"></a>
Discovery configuration for the registry  
Type: [DiscoveryConfiguration](#API_DiscoveryConfiguration) object

 ** [encryptionConfiguration](#API_GetRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistry-response-encryptionConfiguration"></a>
The server-side encryption configuration for the registry. Appears only when a customer-managed AWS KMS key encrypts the registry.  
Type: [EncryptionConfiguration](#API_EncryptionConfiguration) object

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

### Errors
<a name="API_GetRegistry_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

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

### See Also
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

## GetRegistryRecord
<a name="API_GetRegistryRecord"></a>

Retrieves the details of a registry record

### Request Syntax
<a name="API_GetRegistryRecord_RequestSyntax"></a>

```
GET /registries/{{registryId}}/records/{{recordId}} HTTP/1.1
```

### URI Request Parameters
<a name="API_GetRegistryRecord_RequestParameters"></a>

The request uses the following URI parameters.

 ** [recordId](#API_GetRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-GetRegistryRecord-request-uri-recordId"></a>
The identifier of the registry record to retrieve (ARN or ID)  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/)?[a-zA-Z0-9]{12}`   
Required: Yes

 ** [registryId](#API_GetRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-GetRegistryRecord-request-uri-registryId"></a>
The identifier of the registry containing the record (ARN or ID)  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

### Request Body
<a name="API_GetRegistryRecord_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_GetRegistryRecord_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": "string",
   "createdBy": "string",
   "createdByAutoDetection": boolean,
   "description": "string",
   "descriptors": { 
      "a2aAgentCard": { 
         "data": "string",
         "dataSchemaVersion": "string",
         "source": { 
            "fromUrl": { 
               "credentialProviderConfigurations": [ 
                  { 
                     "credentialProvider": { ... },
                     "credentialProviderType": "string"
                  }
               ],
               "url": "string"
            }
         }
      },
      "agentSkillsDefinition": { 
         "additionalData": { 
            "skillMd": { 
               "data": "string",
               "dataSchemaVersion": "string",
               "source": { 
                  "fromUrl": { 
                     "credentialProviderConfigurations": [ 
                        { 
                           "credentialProvider": { ... },
                           "credentialProviderType": "string"
                        }
                     ],
                     "url": "string"
                  }
               }
            }
         },
         "data": "string",
         "dataSchemaVersion": "string"
      },
      "agui": { 
         "source": { 
            "fromUrl": { 
               "credentialProviderConfigurations": [ 
                  { 
                     "credentialProvider": { ... },
                     "credentialProviderType": "string"
                  }
               ],
               "url": "string"
            }
         }
      },
      "custom": { 
         "data": "string"
      },
      "http": { 
         "source": { 
            "fromUrl": { 
               "credentialProviderConfigurations": [ 
                  { 
                     "credentialProvider": { ... },
                     "credentialProviderType": "string"
                  }
               ],
               "url": "string"
            }
         }
      },
      "mcpServer": { 
         "additionalData": { 
            "tools": { 
               "data": "string",
               "dataSchemaVersion": "string"
            }
         },
         "data": "string",
         "dataSchemaVersion": "string",
         "source": { 
            "fromUrl": { 
               "credentialProviderConfigurations": [ 
                  { 
                     "credentialProvider": { ... },
                     "credentialProviderType": "string"
                  }
               ],
               "url": "string"
            }
         }
      }
   },
   "displayName": "string",
   "name": "string",
   "provenance": [ 
      { 
         "relation": "string",
         "sourceDetails": { ... },
         "sourceId": "string",
         "sourceType": "string"
      }
   ],
   "recordArn": "string",
   "recordId": "string",
   "recordType": "string",
   "recordVersion": "string",
   "registryArn": "string",
   "status": "string",
   "statusReason": "string",
   "updatedAt": "string"
}
```

### Response Elements
<a name="API_GetRegistryRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistryRecord-response-createdAt"></a>
The timestamp when the registry record was created.  
Type: Timestamp

 ** [createdBy](#API_GetRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistryRecord-response-createdBy"></a>
The ID of the AWS account that created the registry record.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[0-9]{12}` 

 ** [createdByAutoDetection](#API_GetRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistryRecord-response-createdByAutoDetection"></a>
Specifies whether the registry record was created by auto-detection. `true` indicates the record was automatically created by the service based on the registry's auto-detection configuration; `false` indicates the record was created through a control-plane API call.  
Type: Boolean

 ** [description](#API_GetRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistryRecord-response-description"></a>
A description of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [descriptors](#API_GetRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistryRecord-response-descriptors"></a>
The typed descriptors that define the content of the registry record.  
Type: [Descriptors](#API_Descriptors) object

 ** [displayName](#API_GetRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistryRecord-response-displayName"></a>
The human-readable display name of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [name](#API_GetRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistryRecord-response-name"></a>
The name of the registry record. Names are unique within a registry.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*` 

 ** [provenance](#API_GetRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistryRecord-response-provenance"></a>
The provenance lineage entries for the registry record. Populated for records created by auto-detection; each entry identifies the upstream source that the record was detected from.  
Type: Array of [Provenance](#API_Provenance) objects  
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [recordArn](#API_GetRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistryRecord-response-recordArn"></a>
The Amazon Resource Name (ARN) of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}` 

 ** [recordId](#API_GetRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistryRecord-response-recordId"></a>
The unique identifier of the registry record.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[a-zA-Z0-9]{12}` 

 ** [recordType](#API_GetRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistryRecord-response-recordType"></a>
The type of the registry record, such as MCP, AGENT, SKILL, or CUSTOM.  
Type: String  
Valid Values: `MCP | AGENT | CUSTOM | SKILL | GATEWAY` 

 ** [recordVersion](#API_GetRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistryRecord-response-recordVersion"></a>
The version identifier of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9.-]+` 

 ** [registryArn](#API_GetRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistryRecord-response-registryArn"></a>
The Amazon Resource Name (ARN) of the parent registry that owns the record.  
Type: String  
Length Constraints: Minimum length of 46. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}` 

 ** [status](#API_GetRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistryRecord-response-status"></a>
The lifecycle status of the registry record.  
Type: String  
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | REJECTED | DEPRECATED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED` 

 ** [statusReason](#API_GetRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistryRecord-response-statusReason"></a>
The reason for the current status. Typically populated when the status indicates a failure state.  
Type: String

 ** [updatedAt](#API_GetRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-GetRegistryRecord-response-updatedAt"></a>
The timestamp when the registry record was last updated.  
Type: Timestamp

### Errors
<a name="API_GetRegistryRecord_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

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

### See Also
<a name="API_GetRegistryRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/GetRegistryRecord) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/GetRegistryRecord) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/GetRegistryRecord) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/GetRegistryRecord) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/GetRegistryRecord) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/GetRegistryRecord) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/GetRegistryRecord) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/GetRegistryRecord) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/GetRegistryRecord) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/GetRegistryRecord) 

## ListRegistries
<a name="API_ListRegistries"></a>

Lists the registries in the caller's account and Region, with optional filtering by status and discovery authorizer type

### Request Syntax
<a name="API_ListRegistries_RequestSyntax"></a>

```
POST /registries-list HTTP/1.1
Content-type: application/json

{
   "filters": [ 
      { 
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

### URI Request Parameters
<a name="API_ListRegistries_RequestParameters"></a>

The request does not use any URI parameters.

### Request Body
<a name="API_ListRegistries_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListRegistries_RequestSyntax) **   <a name="agentregistrycontrol-ListRegistries-request-filters"></a>
Filters to apply to the registry list  
Type: Array of [RegistryFilter](#API_RegistryFilter) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** [maxResults](#API_ListRegistries_RequestSyntax) **   <a name="agentregistrycontrol-ListRegistries-request-maxResults"></a>
Maximum number of results to return  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [nextToken](#API_ListRegistries_RequestSyntax) **   <a name="agentregistrycontrol-ListRegistries-request-nextToken"></a>
Token for pagination  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*`   
Required: No

### Response Syntax
<a name="API_ListRegistries_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "registries": [ 
      { 
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
         "name": "string",
         "registryArn": "string",
         "registryId": "string",
         "status": "string",
         "statusReason": "string",
         "updatedAt": "string"
      }
   ]
}
```

### Response Elements
<a name="API_ListRegistries_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRegistries_ResponseSyntax) **   <a name="agentregistrycontrol-ListRegistries-response-nextToken"></a>
Token for next page of results  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [registries](#API_ListRegistries_ResponseSyntax) **   <a name="agentregistrycontrol-ListRegistries-response-registries"></a>
List of registry summaries  
Type: Array of [RegistrySummary](#API_RegistrySummary) objects

### Errors
<a name="API_ListRegistries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The caller is not authorized to perform the requested action.  
HTTP Status Code: 403

 ** InternalServerException **   
The request failed due to an unexpected internal error; the caller may retry.  
HTTP Status Code: 500

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

### See Also
<a name="API_ListRegistries_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/ListRegistries) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/ListRegistries) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/ListRegistries) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/ListRegistries) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/ListRegistries) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/ListRegistries) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/ListRegistries) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/ListRegistries) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/ListRegistries) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/ListRegistries) 

## ListRegistryRecords
<a name="API_ListRegistryRecords"></a>

Lists the registry records within a registry, with optional filtering by name, status, and record type

### Request Syntax
<a name="API_ListRegistryRecords_RequestSyntax"></a>

```
POST /registries/{{registryId}}/records-list HTTP/1.1
Content-type: application/json

{
   "filters": [ 
      { 
         "name": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

### URI Request Parameters
<a name="API_ListRegistryRecords_RequestParameters"></a>

The request uses the following URI parameters.

 ** [registryId](#API_ListRegistryRecords_RequestSyntax) **   <a name="agentregistrycontrol-ListRegistryRecords-request-uri-registryId"></a>
The identifier of the registry to list records from (ARN or ID)  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

### Request Body
<a name="API_ListRegistryRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListRegistryRecords_RequestSyntax) **   <a name="agentregistrycontrol-ListRegistryRecords-request-filters"></a>
Filters to apply to the registry record list  
Type: Array of [RegistryRecordFilter](#API_RegistryRecordFilter) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** [maxResults](#API_ListRegistryRecords_RequestSyntax) **   <a name="agentregistrycontrol-ListRegistryRecords-request-maxResults"></a>
Maximum number of records to return  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [nextToken](#API_ListRegistryRecords_RequestSyntax) **   <a name="agentregistrycontrol-ListRegistryRecords-request-nextToken"></a>
Token for pagination  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*`   
Required: No

### Response Syntax
<a name="API_ListRegistryRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "registryRecords": [ 
      { 
         "createdAt": "string",
         "createdBy": "string",
         "createdByAutoDetection": boolean,
         "description": "string",
         "displayName": "string",
         "name": "string",
         "provenanceSummaryList": [ 
            { 
               "relation": "string",
               "sourceId": "string",
               "sourceType": "string"
            }
         ],
         "recordArn": "string",
         "recordId": "string",
         "recordType": "string",
         "recordVersion": "string",
         "registryArn": "string",
         "status": "string",
         "updatedAt": "string"
      }
   ]
}
```

### Response Elements
<a name="API_ListRegistryRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRegistryRecords_ResponseSyntax) **   <a name="agentregistrycontrol-ListRegistryRecords-response-nextToken"></a>
Token for next page of results  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [registryRecords](#API_ListRegistryRecords_ResponseSyntax) **   <a name="agentregistrycontrol-ListRegistryRecords-response-registryRecords"></a>
List of registry record summaries  
Type: Array of [RegistryRecordSummary](#API_RegistryRecordSummary) objects

### Errors
<a name="API_ListRegistryRecords_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

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

### See Also
<a name="API_ListRegistryRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/ListRegistryRecords) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/ListRegistryRecords) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/ListRegistryRecords) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/ListRegistryRecords) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/ListRegistryRecords) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/ListRegistryRecords) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/ListRegistryRecords) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/ListRegistryRecords) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/ListRegistryRecords) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/ListRegistryRecords) 

## ListTagsForResource
<a name="API_ListTagsForResource"></a>

Lists the tags associated with the specified AWS Agent Registry resource. Returns the current tag key-value pairs on the resource.

### Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
GET /tags/{{resourceArn+}} HTTP/1.1
```

### URI Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_ListTagsForResource_RequestSyntax) **   <a name="agentregistrycontrol-ListTagsForResource-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource to list tags for. Supported resources include registries and registry records.  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Required: Yes

### Request Body
<a name="API_ListTagsForResource_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "tags": { 
      "string" : "string" 
   }
}
```

### Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="agentregistrycontrol-ListTagsForResource-response-tags"></a>
The tags currently associated with the resource, as a map of tag keys to tag values.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*` 

### Errors
<a name="API_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

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

### See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/ListTagsForResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/ListTagsForResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/ListTagsForResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/ListTagsForResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/ListTagsForResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/ListTagsForResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/ListTagsForResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/ListTagsForResource) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/ListTagsForResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/ListTagsForResource) 

## SubmitRegistryRecordForApproval
<a name="API_SubmitRegistryRecordForApproval"></a>

Submits a DRAFT registry record for approval, moving it into the registry's approval workflow. Depending on the registry's approval configuration, the record is either auto-approved or set to PENDING\_APPROVAL for a curator to approve or reject.

### Request Syntax
<a name="API_SubmitRegistryRecordForApproval_RequestSyntax"></a>

```
POST /registries/{{registryId}}/records/{{recordId}}/submit-for-approval HTTP/1.1
```

### URI Request Parameters
<a name="API_SubmitRegistryRecordForApproval_RequestParameters"></a>

The request uses the following URI parameters.

 ** [recordId](#API_SubmitRegistryRecordForApproval_RequestSyntax) **   <a name="agentregistrycontrol-SubmitRegistryRecordForApproval-request-uri-recordId"></a>
The identifier of the registry record to submit for approval (ARN or ID)  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/)?[a-zA-Z0-9]{12}`   
Required: Yes

 ** [registryId](#API_SubmitRegistryRecordForApproval_RequestSyntax) **   <a name="agentregistrycontrol-SubmitRegistryRecordForApproval-request-uri-registryId"></a>
The identifier of the registry containing the record (ARN or ID)  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

### Request Body
<a name="API_SubmitRegistryRecordForApproval_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_SubmitRegistryRecordForApproval_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "recordArn": "string",
   "recordId": "string",
   "registryArn": "string",
   "status": "string",
   "updatedAt": "string"
}
```

### Response Elements
<a name="API_SubmitRegistryRecordForApproval_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [recordArn](#API_SubmitRegistryRecordForApproval_ResponseSyntax) **   <a name="agentregistrycontrol-SubmitRegistryRecordForApproval-response-recordArn"></a>
The ARN of the registry record  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}` 

 ** [recordId](#API_SubmitRegistryRecordForApproval_ResponseSyntax) **   <a name="agentregistrycontrol-SubmitRegistryRecordForApproval-response-recordId"></a>
The ID of the registry record  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[a-zA-Z0-9]{12}` 

 ** [registryArn](#API_SubmitRegistryRecordForApproval_ResponseSyntax) **   <a name="agentregistrycontrol-SubmitRegistryRecordForApproval-response-registryArn"></a>
The ARN of the registry  
Type: String  
Length Constraints: Minimum length of 46. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}` 

 ** [status](#API_SubmitRegistryRecordForApproval_ResponseSyntax) **   <a name="agentregistrycontrol-SubmitRegistryRecordForApproval-response-status"></a>
The resulting status of the registry record  
Type: String  
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | REJECTED | DEPRECATED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED` 

 ** [updatedAt](#API_SubmitRegistryRecordForApproval_ResponseSyntax) **   <a name="agentregistrycontrol-SubmitRegistryRecordForApproval-response-updatedAt"></a>
The timestamp when the record was last updated  
Type: Timestamp

### Errors
<a name="API_SubmitRegistryRecordForApproval_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

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

### See Also
<a name="API_SubmitRegistryRecordForApproval_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/SubmitRegistryRecordForApproval) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/SubmitRegistryRecordForApproval) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/SubmitRegistryRecordForApproval) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/SubmitRegistryRecordForApproval) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/SubmitRegistryRecordForApproval) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/SubmitRegistryRecordForApproval) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/SubmitRegistryRecordForApproval) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/SubmitRegistryRecordForApproval) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/SubmitRegistryRecordForApproval) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/SubmitRegistryRecordForApproval) 

## TagResource
<a name="API_TagResource"></a>

Adds or overwrites one or more tags for the specified AWS Agent Registry resource. Tags are key-value pairs that you can use to categorize and manage AWS resources. If a tag with the same key already exists on the resource, the service replaces its value with the value you specify.

### Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
POST /tags/{{resourceArn+}} HTTP/1.1
Content-type: application/json

{
   "tags": { 
      "{{string}}" : "{{string}}" 
   }
}
```

### URI Request Parameters
<a name="API_TagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_TagResource_RequestSyntax) **   <a name="agentregistrycontrol-TagResource-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource to tag. Supported resources include registries and registry records.  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Required: Yes

### Request Body
<a name="API_TagResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [tags](#API_TagResource_RequestSyntax) **   <a name="agentregistrycontrol-TagResource-request-tags"></a>
The tags to apply to the resource, as a map of tag keys to tag values. Tag keys must be unique within the request.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: Yes

### Response Syntax
<a name="API_TagResource_ResponseSyntax"></a>

```
HTTP/1.1 204
```

### Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

### Errors
<a name="API_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

 ** AccessDeniedException **   
The caller is not authorized to perform the requested action.  
HTTP Status Code: 403

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

### See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/TagResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/TagResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/TagResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/TagResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/TagResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/TagResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/TagResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/TagResource) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/TagResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/TagResource) 

## UntagResource
<a name="API_UntagResource"></a>

Removes one or more tags from the specified AWS Agent Registry resource. The operation removes only the tags whose keys you supply; other tags on the resource remain unchanged.

### Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
DELETE /tags/{{resourceArn+}}?tagKeys={{tagKeys}} HTTP/1.1
```

### URI Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_UntagResource_RequestSyntax) **   <a name="agentregistrycontrol-UntagResource-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource to remove tags from. Supported resources include registries and registry records.  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Required: Yes

 ** [tagKeys](#API_UntagResource_RequestSyntax) **   <a name="agentregistrycontrol-UntagResource-request-uri-tagKeys"></a>
The keys of the tags to remove from the resource. Tags with keys not included in this list remain on the resource.  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: Yes

### Request Body
<a name="API_UntagResource_RequestBody"></a>

The request does not have a request body.

### Response Syntax
<a name="API_UntagResource_ResponseSyntax"></a>

```
HTTP/1.1 204
```

### Response Elements
<a name="API_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

### Errors
<a name="API_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

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

### See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/UntagResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/UntagResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UntagResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/UntagResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UntagResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/UntagResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/UntagResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/UntagResource) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/UntagResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UntagResource) 

## UpdateRegistry
<a name="API_UpdateRegistry"></a>

Updates an existing registry. This operation uses PATCH semantics: specify only the fields you want to change, and omit the rest to leave them unchanged. Updates are applied asynchronously and the registry transitions to the UPDATING status while they are processed.

### Request Syntax
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

### URI Request Parameters
<a name="API_UpdateRegistry_RequestParameters"></a>

The request uses the following URI parameters.

 ** [registryId](#API_UpdateRegistry_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-request-uri-registryId"></a>
The identifier of the registry to update (ARN or ID)  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

### Request Body
<a name="API_UpdateRegistry_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [approvalConfiguration](#API_UpdateRegistry_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-request-approvalConfiguration"></a>
The updated approval configuration. The change applies only to records that move to PENDING\_APPROVAL after the update; records already in PENDING\_APPROVAL are unaffected.  
Type: [UpdatedApprovalConfiguration](#API_UpdatedApprovalConfiguration) object  
Required: No

 ** [autoDetectionConfiguration](#API_UpdateRegistry_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-request-autoDetectionConfiguration"></a>
The updated auto-detection configuration for the registry, with PATCH semantics. Omit this field to leave the current configuration unchanged. Supply an empty wrapper to unset it. Supply `optionalValue` to replace it.  
Type: [UpdatedAutoDetectionConfiguration](#API_UpdatedAutoDetectionConfiguration) object  
Required: No

 ** [description](#API_UpdateRegistry_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-request-description"></a>
The updated description of the registry  
Type: [UpdatedDescription](#API_UpdatedDescription) object  
Required: No

 ** [discoveryConfiguration](#API_UpdateRegistry_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-request-discoveryConfiguration"></a>
The updated discovery configuration. Changing the discovery authorization can break existing consumers that rely on the previous authorization type.  
Type: [UpdatedDiscoveryConfiguration](#API_UpdatedDiscoveryConfiguration) object  
Required: No

 ** [name](#API_UpdateRegistry_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-request-name"></a>
The updated name of the registry  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`   
Required: No

### Response Syntax
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

### Response Elements
<a name="API_UpdateRegistry_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [approvalConfiguration](#API_UpdateRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-response-approvalConfiguration"></a>
Approval configuration for registry records  
Type: [ApprovalConfiguration](#API_ApprovalConfiguration) object

 ** [autoDetection](#API_UpdateRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-response-autoDetection"></a>
The registry's auto-detection properties, including the requested configuration and the current detection status. Present only when auto-detection was configured for the registry.  
Type: [AutoDetection](#API_AutoDetection) object

 ** [createdAt](#API_UpdateRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-response-createdAt"></a>
The timestamp when the registry was created  
Type: Timestamp

 ** [description](#API_UpdateRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-response-description"></a>
The description of the registry  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [discoveryConfiguration](#API_UpdateRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-response-discoveryConfiguration"></a>
Discovery configuration for the registry  
Type: [DiscoveryConfiguration](#API_DiscoveryConfiguration) object

 ** [encryptionConfiguration](#API_UpdateRegistry_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistry-response-encryptionConfiguration"></a>
The server-side encryption configuration for the registry. Appears only when a customer-managed AWS KMS key encrypts the registry.  
Type: [EncryptionConfiguration](#API_EncryptionConfiguration) object

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

### Errors
<a name="API_UpdateRegistry_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

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

### See Also
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

## UpdateRegistryRecord
<a name="API_UpdateRegistryRecord"></a>

Updates a registry record. The update is asynchronous: the record is returned with the UPDATING status while it is processed. Fields that use update wrappers follow PATCH semantics: omit the field to leave it unchanged.

### Request Syntax
<a name="API_UpdateRegistryRecord_RequestSyntax"></a>

```
PATCH /registries/{{registryId}}/records/{{recordId}} HTTP/1.1
Content-type: application/json

{
   "description": { 
      "optionalValue": "{{string}}"
   },
   "descriptors": { 
      "optionalValue": { 
         "a2aAgentCard": { 
            "optionalValue": { 
               "data": { 
                  "optionalValue": "{{string}}"
               },
               "dataSchemaVersion": { 
                  "optionalValue": "{{string}}"
               },
               "source": { 
                  "optionalValue": { 
                     "fromUrl": { 
                        "credentialProviderConfigurations": [ 
                           { 
                              "credentialProvider": { ... },
                              "credentialProviderType": "{{string}}"
                           }
                        ],
                        "url": "{{string}}"
                     }
                  }
               }
            }
         },
         "agentSkillsDefinition": { 
            "optionalValue": { 
               "additionalData": { 
                  "optionalValue": { 
                     "skillMd": { 
                        "optionalValue": { 
                           "data": { 
                              "optionalValue": "{{string}}"
                           },
                           "dataSchemaVersion": { 
                              "optionalValue": "{{string}}"
                           },
                           "source": { 
                              "optionalValue": { 
                                 "fromUrl": { 
                                    "credentialProviderConfigurations": [ 
                                       { 
                                          "credentialProvider": { ... },
                                          "credentialProviderType": "{{string}}"
                                       }
                                    ],
                                    "url": "{{string}}"
                                 }
                              }
                           }
                        }
                     }
                  }
               },
               "data": { 
                  "optionalValue": "{{string}}"
               },
               "dataSchemaVersion": { 
                  "optionalValue": "{{string}}"
               }
            }
         },
         "agui": { 
            "optionalValue": { 
               "source": { 
                  "optionalValue": { 
                     "fromUrl": { 
                        "credentialProviderConfigurations": [ 
                           { 
                              "credentialProvider": { ... },
                              "credentialProviderType": "{{string}}"
                           }
                        ],
                        "url": "{{string}}"
                     }
                  }
               }
            }
         },
         "custom": { 
            "optionalValue": { 
               "data": { 
                  "optionalValue": "{{string}}"
               }
            }
         },
         "http": { 
            "optionalValue": { 
               "source": { 
                  "optionalValue": { 
                     "fromUrl": { 
                        "credentialProviderConfigurations": [ 
                           { 
                              "credentialProvider": { ... },
                              "credentialProviderType": "{{string}}"
                           }
                        ],
                        "url": "{{string}}"
                     }
                  }
               }
            }
         },
         "mcpServer": { 
            "optionalValue": { 
               "additionalData": { 
                  "optionalValue": { 
                     "tools": { 
                        "optionalValue": { 
                           "data": { 
                              "optionalValue": "{{string}}"
                           },
                           "dataSchemaVersion": { 
                              "optionalValue": "{{string}}"
                           }
                        }
                     }
                  }
               },
               "data": { 
                  "optionalValue": "{{string}}"
               },
               "dataSchemaVersion": { 
                  "optionalValue": "{{string}}"
               },
               "source": { 
                  "optionalValue": { 
                     "fromUrl": { 
                        "credentialProviderConfigurations": [ 
                           { 
                              "credentialProvider": { ... },
                              "credentialProviderType": "{{string}}"
                           }
                        ],
                        "url": "{{string}}"
                     }
                  }
               }
            }
         }
      }
   },
   "displayName": { 
      "optionalValue": "{{string}}"
   },
   "name": "{{string}}",
   "provenance": [ 
      { 
         "relation": "{{string}}",
         "sourceDetails": { ... },
         "sourceId": "{{string}}",
         "sourceType": "{{string}}"
      }
   ],
   "recordType": "{{string}}",
   "recordVersion": "{{string}}",
   "triggerSynchronization": {{boolean}}
}
```

### URI Request Parameters
<a name="API_UpdateRegistryRecord_RequestParameters"></a>

The request uses the following URI parameters.

 ** [recordId](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-request-uri-recordId"></a>
The identifier of the registry record to update (ARN or ID)  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/)?[a-zA-Z0-9]{12}`   
Required: Yes

 ** [registryId](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-request-uri-registryId"></a>
The identifier of the registry containing the record (ARN or ID)  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

### Request Body
<a name="API_UpdateRegistryRecord_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-request-description"></a>
The updated description of the registry record. Omit to leave the description unchanged; provide an empty wrapper to unset it.  
Type: [UpdatedDescription](#API_UpdatedDescription) object  
Required: No

 ** [descriptors](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-request-descriptors"></a>
The updated typed descriptor content for the registry record. Omit to leave the descriptors unchanged.  
Type: [UpdatedDescriptors](#API_UpdatedDescriptors) object  
Required: No

 ** [displayName](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-request-displayName"></a>
The updated display name of the registry record. Omit to leave the display name unchanged; provide an empty wrapper to unset it.  
Type: [UpdatedDisplayName](#API_UpdatedDisplayName) object  
Required: No

 ** [name](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-request-name"></a>
The updated name of the registry record. Omit to leave the name unchanged.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`   
Required: No

 ** [provenance](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-request-provenance"></a>
The provenance lineage re-assertion for the registry record. This field is reserved for the AWS Agent Registry auto-detection service principal. Requests that include this field from other callers are rejected. The source identity of an existing lineage is immutable; a re-assertion may only refresh the source details.  
Type: Array of [Provenance](#API_Provenance) objects  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Required: No

 ** [recordType](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-request-recordType"></a>
The updated type of the registry record. Omit to leave the record type unchanged.  
Type: String  
Valid Values: `MCP | AGENT | CUSTOM | SKILL | GATEWAY`   
Required: No

 ** [recordVersion](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-request-recordVersion"></a>
The updated version of the registry record. Omit to leave the version unchanged.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9.-]+`   
Required: No

 ** [triggerSynchronization](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-request-triggerSynchronization"></a>
Whether to trigger synchronization of the record's descriptor content from its source  
Type: Boolean  
Required: No

### Response Syntax
<a name="API_UpdateRegistryRecord_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "createdAt": "string",
   "createdBy": "string",
   "createdByAutoDetection": boolean,
   "description": "string",
   "descriptors": { 
      "a2aAgentCard": { 
         "data": "string",
         "dataSchemaVersion": "string",
         "source": { 
            "fromUrl": { 
               "credentialProviderConfigurations": [ 
                  { 
                     "credentialProvider": { ... },
                     "credentialProviderType": "string"
                  }
               ],
               "url": "string"
            }
         }
      },
      "agentSkillsDefinition": { 
         "additionalData": { 
            "skillMd": { 
               "data": "string",
               "dataSchemaVersion": "string",
               "source": { 
                  "fromUrl": { 
                     "credentialProviderConfigurations": [ 
                        { 
                           "credentialProvider": { ... },
                           "credentialProviderType": "string"
                        }
                     ],
                     "url": "string"
                  }
               }
            }
         },
         "data": "string",
         "dataSchemaVersion": "string"
      },
      "agui": { 
         "source": { 
            "fromUrl": { 
               "credentialProviderConfigurations": [ 
                  { 
                     "credentialProvider": { ... },
                     "credentialProviderType": "string"
                  }
               ],
               "url": "string"
            }
         }
      },
      "custom": { 
         "data": "string"
      },
      "http": { 
         "source": { 
            "fromUrl": { 
               "credentialProviderConfigurations": [ 
                  { 
                     "credentialProvider": { ... },
                     "credentialProviderType": "string"
                  }
               ],
               "url": "string"
            }
         }
      },
      "mcpServer": { 
         "additionalData": { 
            "tools": { 
               "data": "string",
               "dataSchemaVersion": "string"
            }
         },
         "data": "string",
         "dataSchemaVersion": "string",
         "source": { 
            "fromUrl": { 
               "credentialProviderConfigurations": [ 
                  { 
                     "credentialProvider": { ... },
                     "credentialProviderType": "string"
                  }
               ],
               "url": "string"
            }
         }
      }
   },
   "displayName": "string",
   "name": "string",
   "provenance": [ 
      { 
         "relation": "string",
         "sourceDetails": { ... },
         "sourceId": "string",
         "sourceType": "string"
      }
   ],
   "recordArn": "string",
   "recordId": "string",
   "recordType": "string",
   "recordVersion": "string",
   "registryArn": "string",
   "status": "string",
   "statusReason": "string",
   "updatedAt": "string"
}
```

### Response Elements
<a name="API_UpdateRegistryRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-response-createdAt"></a>
The timestamp when the registry record was created.  
Type: Timestamp

 ** [createdBy](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-response-createdBy"></a>
The ID of the AWS account that created the registry record.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[0-9]{12}` 

 ** [createdByAutoDetection](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-response-createdByAutoDetection"></a>
Specifies whether the registry record was created by auto-detection. `true` indicates the record was automatically created by the service based on the registry's auto-detection configuration; `false` indicates the record was created through a control-plane API call.  
Type: Boolean

 ** [description](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-response-description"></a>
A description of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [descriptors](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-response-descriptors"></a>
The typed descriptors that define the content of the registry record.  
Type: [Descriptors](#API_Descriptors) object

 ** [displayName](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-response-displayName"></a>
The human-readable display name of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [name](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-response-name"></a>
The name of the registry record. Names are unique within a registry.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*` 

 ** [provenance](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-response-provenance"></a>
The provenance lineage entries for the registry record. Populated for records created by auto-detection; each entry identifies the upstream source that the record was detected from.  
Type: Array of [Provenance](#API_Provenance) objects  
Array Members: Minimum number of 0 items. Maximum number of 1 item.

 ** [recordArn](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-response-recordArn"></a>
The Amazon Resource Name (ARN) of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}` 

 ** [recordId](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-response-recordId"></a>
The unique identifier of the registry record.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[a-zA-Z0-9]{12}` 

 ** [recordType](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-response-recordType"></a>
The type of the registry record, such as MCP, AGENT, SKILL, or CUSTOM.  
Type: String  
Valid Values: `MCP | AGENT | CUSTOM | SKILL | GATEWAY` 

 ** [recordVersion](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-response-recordVersion"></a>
The version identifier of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9.-]+` 

 ** [registryArn](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-response-registryArn"></a>
The Amazon Resource Name (ARN) of the parent registry that owns the record.  
Type: String  
Length Constraints: Minimum length of 46. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}` 

 ** [status](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-response-status"></a>
The lifecycle status of the registry record.  
Type: String  
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | REJECTED | DEPRECATED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED` 

 ** [statusReason](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-response-statusReason"></a>
The reason for the current status. Typically populated when the status indicates a failure state.  
Type: String

 ** [updatedAt](#API_UpdateRegistryRecord_ResponseSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-response-updatedAt"></a>
The timestamp when the registry record was last updated.  
Type: Timestamp

### Errors
<a name="API_UpdateRegistryRecord_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

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

### See Also
<a name="API_UpdateRegistryRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/UpdateRegistryRecord) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/UpdateRegistryRecord) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdateRegistryRecord) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/UpdateRegistryRecord) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdateRegistryRecord) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/UpdateRegistryRecord) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/UpdateRegistryRecord) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/UpdateRegistryRecord) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/UpdateRegistryRecord) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdateRegistryRecord) 

## UpdateRegistryRecordStatus
<a name="API_UpdateRegistryRecordStatus"></a>

Updates the status of a registry record as part of the registry's curation workflow, for example to approve or reject a record that is pending approval, or to deprecate an approved record so that it is no longer discoverable

### Request Syntax
<a name="API_UpdateRegistryRecordStatus_RequestSyntax"></a>

```
PATCH /registries/{{registryId}}/records/{{recordId}}/status HTTP/1.1
Content-type: application/json

{
   "status": "{{string}}",
   "statusReason": "{{string}}"
}
```

### URI Request Parameters
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

### Request Body
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

### Response Syntax
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

### Response Elements
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

### Errors
<a name="API_UpdateRegistryRecordStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](#CommonErrors).

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

### See Also
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

# Data Types
<a name="API_Types"></a>

The Agent Registry Control API contains several data types that various actions use. This section describes each data type in detail.

**Note**  
The order of each element in a data type structure is not guaranteed. Applications should not assume a particular order.

The following data types are supported:
+  [A2aAgentCardDescriptor](#API_A2aAgentCardDescriptor) 
+  [AgentCoreGatewaySourceDetails](#API_AgentCoreGatewaySourceDetails) 
+  [AgentCoreRuntimeProtocolConfiguration](#API_AgentCoreRuntimeProtocolConfiguration) 
+  [AgentCoreRuntimeSourceDetails](#API_AgentCoreRuntimeSourceDetails) 
+  [AgentSkillsAdditionalData](#API_AgentSkillsAdditionalData) 
+  [AgentSkillsDefinitionDescriptor](#API_AgentSkillsDefinitionDescriptor) 
+  [AgentSkillsMdDescriptor](#API_AgentSkillsMdDescriptor) 
+  [AgUiDescriptor](#API_AgUiDescriptor) 
+  [ApprovalConfiguration](#API_ApprovalConfiguration) 
+  [AuthorizerConfiguration](#API_AuthorizerConfiguration) 
+  [AuthorizingClaimMatchValueType](#API_AuthorizingClaimMatchValueType) 
+  [AutoDetection](#API_AutoDetection) 
+  [AutoDetectionConfiguration](#API_AutoDetectionConfiguration) 
+  [ClaimMatchValueType](#API_ClaimMatchValueType) 
+  [CustomClaimValidationType](#API_CustomClaimValidationType) 
+  [CustomDescriptor](#API_CustomDescriptor) 
+  [CustomJWTAuthorizerConfiguration](#API_CustomJWTAuthorizerConfiguration) 
+  [Descriptors](#API_Descriptors) 
+  [DescriptorSource](#API_DescriptorSource) 
+  [DescriptorSourceFromUrl](#API_DescriptorSourceFromUrl) 
+  [DiscoveryConfiguration](#API_DiscoveryConfiguration) 
+  [EncryptionConfiguration](#API_EncryptionConfiguration) 
+  [HttpDescriptor](#API_HttpDescriptor) 
+  [ManagedVpcResource](#API_ManagedVpcResource) 
+  [McpServerAdditionalData](#API_McpServerAdditionalData) 
+  [McpServerDescriptor](#API_McpServerDescriptor) 
+  [McpToolsDescriptor](#API_McpToolsDescriptor) 
+  [PrivateEndpoint](#API_PrivateEndpoint) 
+  [PrivateEndpointOverride](#API_PrivateEndpointOverride) 
+  [Provenance](#API_Provenance) 
+  [ProvenanceSummary](#API_ProvenanceSummary) 
+  [RegistryFilter](#API_RegistryFilter) 
+  [RegistryRecordCredentialProviderConfiguration](#API_RegistryRecordCredentialProviderConfiguration) 
+  [RegistryRecordCredentialProviderUnion](#API_RegistryRecordCredentialProviderUnion) 
+  [RegistryRecordFilter](#API_RegistryRecordFilter) 
+  [RegistryRecordIamCredentialProvider](#API_RegistryRecordIamCredentialProvider) 
+  [RegistryRecordOAuthCredentialProvider](#API_RegistryRecordOAuthCredentialProvider) 
+  [RegistryRecordSummary](#API_RegistryRecordSummary) 
+  [RegistrySummary](#API_RegistrySummary) 
+  [SelfManagedLatticeResource](#API_SelfManagedLatticeResource) 
+  [SourceDetails](#API_SourceDetails) 
+  [UpdatedA2aAgentCardDescriptor](#API_UpdatedA2aAgentCardDescriptor) 
+  [UpdatedA2aAgentCardDescriptorFields](#API_UpdatedA2aAgentCardDescriptorFields) 
+  [UpdatedAgentSkillsAdditionalData](#API_UpdatedAgentSkillsAdditionalData) 
+  [UpdatedAgentSkillsAdditionalDataFields](#API_UpdatedAgentSkillsAdditionalDataFields) 
+  [UpdatedAgentSkillsDefinitionDescriptor](#API_UpdatedAgentSkillsDefinitionDescriptor) 
+  [UpdatedAgentSkillsDefinitionDescriptorFields](#API_UpdatedAgentSkillsDefinitionDescriptorFields) 
+  [UpdatedAgentSkillsMdDescriptor](#API_UpdatedAgentSkillsMdDescriptor) 
+  [UpdatedAgentSkillsMdDescriptorFields](#API_UpdatedAgentSkillsMdDescriptorFields) 
+  [UpdatedAgUiDescriptor](#API_UpdatedAgUiDescriptor) 
+  [UpdatedAgUiDescriptorFields](#API_UpdatedAgUiDescriptorFields) 
+  [UpdatedApprovalConfiguration](#API_UpdatedApprovalConfiguration) 
+  [UpdatedAuthorizerConfiguration](#API_UpdatedAuthorizerConfiguration) 
+  [UpdatedAutoDetectionConfiguration](#API_UpdatedAutoDetectionConfiguration) 
+  [UpdatedCustomDescriptor](#API_UpdatedCustomDescriptor) 
+  [UpdatedCustomDescriptorFields](#API_UpdatedCustomDescriptorFields) 
+  [UpdatedDataSchemaVersion](#API_UpdatedDataSchemaVersion) 
+  [UpdatedDescription](#API_UpdatedDescription) 
+  [UpdatedDescriptorData](#API_UpdatedDescriptorData) 
+  [UpdatedDescriptors](#API_UpdatedDescriptors) 
+  [UpdatedDescriptorsFields](#API_UpdatedDescriptorsFields) 
+  [UpdatedDescriptorSource](#API_UpdatedDescriptorSource) 
+  [UpdatedDiscoveryConfiguration](#API_UpdatedDiscoveryConfiguration) 
+  [UpdatedDisplayName](#API_UpdatedDisplayName) 
+  [UpdatedHttpDescriptor](#API_UpdatedHttpDescriptor) 
+  [UpdatedHttpDescriptorFields](#API_UpdatedHttpDescriptorFields) 
+  [UpdatedMcpServerAdditionalData](#API_UpdatedMcpServerAdditionalData) 
+  [UpdatedMcpServerAdditionalDataFields](#API_UpdatedMcpServerAdditionalDataFields) 
+  [UpdatedMcpServerDescriptor](#API_UpdatedMcpServerDescriptor) 
+  [UpdatedMcpServerDescriptorFields](#API_UpdatedMcpServerDescriptorFields) 
+  [UpdatedMcpToolsDescriptor](#API_UpdatedMcpToolsDescriptor) 
+  [UpdatedMcpToolsDescriptorFields](#API_UpdatedMcpToolsDescriptorFields) 
+  [ValidationExceptionField](#API_ValidationExceptionField) 
+  [WorkloadIdentityDetails](#API_WorkloadIdentityDetails) 

## A2aAgentCardDescriptor
<a name="API_A2aAgentCardDescriptor"></a>

Descriptor that defines the content of an A2A (Agent-to-Agent) agent card registry record. The content is validated against the A2A protocol schema.

### Contents
<a name="API_A2aAgentCardDescriptor_Contents"></a>

 ** data **   <a name="agentregistrycontrol-Type-A2aAgentCardDescriptor-data"></a>
The A2A agent card content, serialized as descriptor payload data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 102400.  
Required: No

 ** dataSchemaVersion **   <a name="agentregistrycontrol-Type-A2aAgentCardDescriptor-dataSchemaVersion"></a>
The schema version of the descriptor payload.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** source **   <a name="agentregistrycontrol-Type-A2aAgentCardDescriptor-source"></a>
The optional source configuration used to synchronize the A2A agent card descriptor content.  
Type: [DescriptorSource](#API_DescriptorSource) object  
Required: No

### See Also
<a name="API_A2aAgentCardDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/A2aAgentCardDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/A2aAgentCardDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/A2aAgentCardDescriptor) 

## AgentCoreGatewaySourceDetails
<a name="API_AgentCoreGatewaySourceDetails"></a>

The source details for a registry record that was auto-detected from an Amazon Bedrock AgentCore Gateway resource.

### Contents
<a name="API_AgentCoreGatewaySourceDetails_Contents"></a>

 ** authorizerConfiguration **   <a name="agentregistrycontrol-Type-AgentCoreGatewaySourceDetails-authorizerConfiguration"></a>
The authorizer configuration for a registry. Exactly one member is set.  
Type: [AuthorizerConfiguration](#API_AuthorizerConfiguration) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** authorizerType **   <a name="agentregistrycontrol-Type-AgentCoreGatewaySourceDetails-authorizerType"></a>
The type of authorizer configured on the AgentCore Gateway resource that the registry record was detected from.  
Type: String  
Required: No

 ** protocolType **   <a name="agentregistrycontrol-Type-AgentCoreGatewaySourceDetails-protocolType"></a>
The protocol type of the AgentCore Gateway resource that the registry record was detected from, for example `MCP`.  
Type: String  
Valid Values: `MCP`   
Required: No

 ** workloadIdentityDetails **   <a name="agentregistrycontrol-Type-AgentCoreGatewaySourceDetails-workloadIdentityDetails"></a>
The workload identity details for the AgentCore Gateway resource. Present when the gateway has a workload identity configured.  
Type: [WorkloadIdentityDetails](#API_WorkloadIdentityDetails) object  
Required: No

### See Also
<a name="API_AgentCoreGatewaySourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/AgentCoreGatewaySourceDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/AgentCoreGatewaySourceDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/AgentCoreGatewaySourceDetails) 

## AgentCoreRuntimeProtocolConfiguration
<a name="API_AgentCoreRuntimeProtocolConfiguration"></a>

The protocol configuration of an AgentCore Runtime resource that a registry record was auto-detected from.

### Contents
<a name="API_AgentCoreRuntimeProtocolConfiguration_Contents"></a>

 ** serverProtocol **   <a name="agentregistrycontrol-Type-AgentCoreRuntimeProtocolConfiguration-serverProtocol"></a>
The server protocol used by the AgentCore Runtime, such as `MCP`, `HTTP`, `A2A`, or `AGUI`.  
Type: String  
Valid Values: `HTTP | A2A | MCP | AGUI`   
Required: No

### See Also
<a name="API_AgentCoreRuntimeProtocolConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/AgentCoreRuntimeProtocolConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/AgentCoreRuntimeProtocolConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/AgentCoreRuntimeProtocolConfiguration) 

## AgentCoreRuntimeSourceDetails
<a name="API_AgentCoreRuntimeSourceDetails"></a>

The source details for a registry record that was auto-detected from an Amazon Bedrock AgentCore Runtime resource.

### Contents
<a name="API_AgentCoreRuntimeSourceDetails_Contents"></a>

 ** authorizerConfiguration **   <a name="agentregistrycontrol-Type-AgentCoreRuntimeSourceDetails-authorizerConfiguration"></a>
The authorizer configuration for a registry. Exactly one member is set.  
Type: [AuthorizerConfiguration](#API_AuthorizerConfiguration) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** protocolConfiguration **   <a name="agentregistrycontrol-Type-AgentCoreRuntimeSourceDetails-protocolConfiguration"></a>
The protocol configuration of the AgentCore Runtime resource that the registry record was detected from.  
Type: [AgentCoreRuntimeProtocolConfiguration](#API_AgentCoreRuntimeProtocolConfiguration) object  
Required: No

 ** workloadIdentityDetails **   <a name="agentregistrycontrol-Type-AgentCoreRuntimeSourceDetails-workloadIdentityDetails"></a>
The workload identity details for the AgentCore Runtime resource. Present when the runtime has a workload identity configured.  
Type: [WorkloadIdentityDetails](#API_WorkloadIdentityDetails) object  
Required: No

### See Also
<a name="API_AgentCoreRuntimeSourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/AgentCoreRuntimeSourceDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/AgentCoreRuntimeSourceDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/AgentCoreRuntimeSourceDetails) 

## AgentSkillsAdditionalData
<a name="API_AgentSkillsAdditionalData"></a>

Additional data associated with an agent skills definition descriptor.

### Contents
<a name="API_AgentSkillsAdditionalData_Contents"></a>

 ** skillMd **   <a name="agentregistrycontrol-Type-AgentSkillsAdditionalData-skillMd"></a>
The markdown skill content associated with an agent skills definition.  
Type: [AgentSkillsMdDescriptor](#API_AgentSkillsMdDescriptor) object  
Required: No

### See Also
<a name="API_AgentSkillsAdditionalData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/AgentSkillsAdditionalData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/AgentSkillsAdditionalData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/AgentSkillsAdditionalData) 

## AgentSkillsDefinitionDescriptor
<a name="API_AgentSkillsDefinitionDescriptor"></a>

Descriptor that defines an agent skills registry record and its associated content.

### Contents
<a name="API_AgentSkillsDefinitionDescriptor_Contents"></a>

 ** additionalData **   <a name="agentregistrycontrol-Type-AgentSkillsDefinitionDescriptor-additionalData"></a>
Additional data associated with the agent skills definition descriptor.  
Type: [AgentSkillsAdditionalData](#API_AgentSkillsAdditionalData) object  
Required: No

 ** data **   <a name="agentregistrycontrol-Type-AgentSkillsDefinitionDescriptor-data"></a>
The agent skills definition content, serialized as descriptor payload data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 102400.  
Required: No

 ** dataSchemaVersion **   <a name="agentregistrycontrol-Type-AgentSkillsDefinitionDescriptor-dataSchemaVersion"></a>
The schema version of the descriptor payload.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

### See Also
<a name="API_AgentSkillsDefinitionDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/AgentSkillsDefinitionDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/AgentSkillsDefinitionDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/AgentSkillsDefinitionDescriptor) 

## AgentSkillsMdDescriptor
<a name="API_AgentSkillsMdDescriptor"></a>

Markdown-format descriptor containing an agent skills document.

### Contents
<a name="API_AgentSkillsMdDescriptor_Contents"></a>

 ** data **   <a name="agentregistrycontrol-Type-AgentSkillsMdDescriptor-data"></a>
The agent skills markdown content, serialized as descriptor payload data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 102400.  
Required: No

 ** dataSchemaVersion **   <a name="agentregistrycontrol-Type-AgentSkillsMdDescriptor-dataSchemaVersion"></a>
The schema version of the descriptor payload.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** source **   <a name="agentregistrycontrol-Type-AgentSkillsMdDescriptor-source"></a>
The optional source configuration used to synchronize the agent skills markdown content.  
Type: [DescriptorSource](#API_DescriptorSource) object  
Required: No

### See Also
<a name="API_AgentSkillsMdDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/AgentSkillsMdDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/AgentSkillsMdDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/AgentSkillsMdDescriptor) 

## AgUiDescriptor
<a name="API_AgUiDescriptor"></a>

A registry record descriptor for the AG-UI (Agent-User Interaction) protocol.

### Contents
<a name="API_AgUiDescriptor_Contents"></a>

 ** source **   <a name="agentregistrycontrol-Type-AgUiDescriptor-source"></a>
The source configuration that defines where descriptor content is retrieved from.  
Type: [DescriptorSource](#API_DescriptorSource) object  
Required: No

### See Also
<a name="API_AgUiDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/AgUiDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/AgUiDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/AgUiDescriptor) 

## ApprovalConfiguration
<a name="API_ApprovalConfiguration"></a>

Configuration for the registry's record approval workflow. Controls whether records submitted for approval require manual review before they become approved and discoverable, or are auto-approved. When no auto-approval rules are configured, submitted records require manual review.

### Contents
<a name="API_ApprovalConfiguration_Contents"></a>

 ** autoApprovalRules **   <a name="agentregistrycontrol-Type-ApprovalConfiguration-autoApprovalRules"></a>
The rules that determine which registry records are automatically approved on submission. When omitted or empty, submitted records require manual review.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Valid Values: `APPROVE_ALL`   
Required: No

### See Also
<a name="API_ApprovalConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/ApprovalConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/ApprovalConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/ApprovalConfiguration) 

## AuthorizerConfiguration
<a name="API_AuthorizerConfiguration"></a>

The authorizer configuration for a registry. Exactly one member is set.

### Contents
<a name="API_AuthorizerConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** customJWTAuthorizer **   <a name="agentregistrycontrol-Type-AuthorizerConfiguration-customJWTAuthorizer"></a>
Configuration for a custom JWT authorizer.  
Type: [CustomJWTAuthorizerConfiguration](#API_CustomJWTAuthorizerConfiguration) object  
Required: No

### See Also
<a name="API_AuthorizerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/AuthorizerConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/AuthorizerConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/AuthorizerConfiguration) 

## AuthorizingClaimMatchValueType
<a name="API_AuthorizingClaimMatchValueType"></a>

The value and match operator used to authorize a claim during JWT validation.

### Contents
<a name="API_AuthorizingClaimMatchValueType_Contents"></a>

 ** claimMatchOperator **   <a name="agentregistrycontrol-Type-AuthorizingClaimMatchValueType-claimMatchOperator"></a>
The operator used to compare the claim value against the expected value.  
Type: String  
Valid Values: `EQUALS | CONTAINS | CONTAINS_ANY`   
Required: Yes

 ** claimMatchValue **   <a name="agentregistrycontrol-Type-AuthorizingClaimMatchValueType-claimMatchValue"></a>
The expected value or values that the claim is compared against.  
Type: [ClaimMatchValueType](#API_ClaimMatchValueType) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

### See Also
<a name="API_AuthorizingClaimMatchValueType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/AuthorizingClaimMatchValueType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/AuthorizingClaimMatchValueType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/AuthorizingClaimMatchValueType) 

## AutoDetection
<a name="API_AutoDetection"></a>

The auto-detection properties for a registry, including the requested configuration and the current detection status. When auto-detection is enabled and the scope preconditions are met, the registry is automatically populated with discovered resources.

### Contents
<a name="API_AutoDetection_Contents"></a>

 ** configuration **   <a name="agentregistrycontrol-Type-AutoDetection-configuration"></a>
The auto-detection settings that control how resources are discovered for the registry.  
Type: [AutoDetectionConfiguration](#API_AutoDetectionConfiguration) object  
Required: Yes

 ** status **   <a name="agentregistrycontrol-Type-AutoDetection-status"></a>
The current auto-detection status. `ACTIVE` indicates that the registry is actively being populated with detected resources. `INACTIVE` indicates that the preconditions required at the configured scope are not currently met.  
Type: String  
Valid Values: `ACTIVE | INACTIVE`   
Required: Yes

 ** statusReason **   <a name="agentregistrycontrol-Type-AutoDetection-statusReason"></a>
A human-readable explanation of the current auto-detection status. Typically populated when the status requires additional context.  
Type: String  
Required: No

### See Also
<a name="API_AutoDetection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/AutoDetection) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/AutoDetection) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/AutoDetection) 

## AutoDetectionConfiguration
<a name="API_AutoDetectionConfiguration"></a>

The customer-defined auto-detection settings for a registry.

### Contents
<a name="API_AutoDetectionConfiguration_Contents"></a>

 ** enabled **   <a name="agentregistrycontrol-Type-AutoDetectionConfiguration-enabled"></a>
Specifies whether auto-detection is requested for the registry. Setting this to `true` is necessary but not sufficient for auto-detection to become active; the preconditions of the configured scope must also be met.  
Type: Boolean  
Required: Yes

 ** scope **   <a name="agentregistrycontrol-Type-AutoDetectionConfiguration-scope"></a>
The source from which resources are detected. For example, `ORGANIZATION` sources resources from all member accounts of an AWS organization.  
Type: String  
Valid Values: `ORGANIZATION`   
Required: Yes

### See Also
<a name="API_AutoDetectionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/AutoDetectionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/AutoDetectionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/AutoDetectionConfiguration) 

## ClaimMatchValueType
<a name="API_ClaimMatchValueType"></a>

The expected value used to match a claim. Exactly one member is set.

### Contents
<a name="API_ClaimMatchValueType_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** matchValueString **   <a name="agentregistrycontrol-Type-ClaimMatchValueType-matchValueString"></a>
A single string value to match the claim against.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z0-9_.:/-]+`   
Required: No

 ** matchValueStringList **   <a name="agentregistrycontrol-Type-ClaimMatchValueType-matchValueStringList"></a>
A list of string values to match the claim against.  
Type: Array of strings  
Array Members: Minimum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z0-9_.:/-]+`   
Required: No

### See Also
<a name="API_ClaimMatchValueType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/ClaimMatchValueType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/ClaimMatchValueType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/ClaimMatchValueType) 

## CustomClaimValidationType
<a name="API_CustomClaimValidationType"></a>

A validation rule applied to a single claim of an inbound JWT.

### Contents
<a name="API_CustomClaimValidationType_Contents"></a>

 ** authorizingClaimMatchValue **   <a name="agentregistrycontrol-Type-CustomClaimValidationType-authorizingClaimMatchValue"></a>
The value and match operator used to authorize the claim.  
Type: [AuthorizingClaimMatchValueType](#API_AuthorizingClaimMatchValueType) object  
Required: Yes

 ** inboundTokenClaimName **   <a name="agentregistrycontrol-Type-CustomClaimValidationType-inboundTokenClaimName"></a>
The name of the claim in the inbound token to validate.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z0-9_.-:]+`   
Required: Yes

 ** inboundTokenClaimValueType **   <a name="agentregistrycontrol-Type-CustomClaimValidationType-inboundTokenClaimValueType"></a>
The value type of the claim in the inbound token, either a string or an array of strings.  
Type: String  
Valid Values: `STRING | STRING_ARRAY`   
Required: Yes

### See Also
<a name="API_CustomClaimValidationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/CustomClaimValidationType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/CustomClaimValidationType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/CustomClaimValidationType) 

## CustomDescriptor
<a name="API_CustomDescriptor"></a>

Custom descriptor for user-defined content

### Contents
<a name="API_CustomDescriptor_Contents"></a>

 ** data **   <a name="agentregistrycontrol-Type-CustomDescriptor-data"></a>
The custom descriptor content, serialized as descriptor payload data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 102400.  
Required: No

### See Also
<a name="API_CustomDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/CustomDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/CustomDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/CustomDescriptor) 

## CustomJWTAuthorizerConfiguration
<a name="API_CustomJWTAuthorizerConfiguration"></a>

Configuration for a custom JWT authorizer that validates inbound bearer tokens against an OpenID Connect identity provider.

### Contents
<a name="API_CustomJWTAuthorizerConfiguration_Contents"></a>

 ** discoveryUrl **   <a name="agentregistrycontrol-Type-CustomJWTAuthorizerConfiguration-discoveryUrl"></a>
The OpenID Connect discovery URL used to retrieve the identity provider's metadata and signing keys.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `.+/\.well-known/openid-configuration`   
Required: Yes

 ** allowedAudience **   <a name="agentregistrycontrol-Type-CustomJWTAuthorizerConfiguration-allowedAudience"></a>
The audience values accepted during JWT validation. A token is rejected if none of its audience claims match.  
Type: Array of strings  
Array Members: Minimum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** allowedClients **   <a name="agentregistrycontrol-Type-CustomJWTAuthorizerConfiguration-allowedClients"></a>
The client identifiers accepted during JWT validation. A token is rejected if it was not issued to one of these clients.  
Type: Array of strings  
Array Members: Minimum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** allowedScopes **   <a name="agentregistrycontrol-Type-CustomJWTAuthorizerConfiguration-allowedScopes"></a>
The scopes accepted during JWT validation. A token is rejected if it does not carry one of these scopes.  
Type: Array of strings  
Array Members: Minimum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[\x21\x23-\x5B\x5D-\x7E]+`   
Required: No

 ** customClaims **   <a name="agentregistrycontrol-Type-CustomJWTAuthorizerConfiguration-customClaims"></a>
Additional custom claim validations applied to the inbound JWT.  
Type: Array of [CustomClaimValidationType](#API_CustomClaimValidationType) objects  
Array Members: Minimum number of 1 item.  
Required: No

 ** privateEndpoint **   <a name="agentregistrycontrol-Type-CustomJWTAuthorizerConfiguration-privateEndpoint"></a>
The private endpoint used to reach the identity provider's discovery URL over a private network path.  
Type: [PrivateEndpoint](#API_PrivateEndpoint) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** privateEndpointOverrides **   <a name="agentregistrycontrol-Type-CustomJWTAuthorizerConfiguration-privateEndpointOverrides"></a>
Per-domain private endpoint overrides that route specific identity provider domains through distinct private endpoints.  
Type: Array of [PrivateEndpointOverride](#API_PrivateEndpointOverride) objects  
Array Members: Minimum number of 0 items. Maximum number of 5 items.  
Required: No

### See Also
<a name="API_CustomJWTAuthorizerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/CustomJWTAuthorizerConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/CustomJWTAuthorizerConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/CustomJWTAuthorizerConfiguration) 

## Descriptors
<a name="API_Descriptors"></a>

The typed set of descriptors for a registry record. Exactly one descriptor field is populated based on the record type.

### Contents
<a name="API_Descriptors_Contents"></a>

 ** a2aAgentCard **   <a name="agentregistrycontrol-Type-Descriptors-a2aAgentCard"></a>
The A2A agent card descriptor, populated when the record type is AGENT.  
Type: [A2aAgentCardDescriptor](#API_A2aAgentCardDescriptor) object  
Required: No

 ** agentSkillsDefinition **   <a name="agentregistrycontrol-Type-Descriptors-agentSkillsDefinition"></a>
The agent skills definition descriptor, populated when the record type is SKILL.  
Type: [AgentSkillsDefinitionDescriptor](#API_AgentSkillsDefinitionDescriptor) object  
Required: No

 ** agui **   <a name="agentregistrycontrol-Type-Descriptors-agui"></a>
The AG-UI descriptor, populated for records detected from an AG-UI protocol source.  
Type: [AgUiDescriptor](#API_AgUiDescriptor) object  
Required: No

 ** custom **   <a name="agentregistrycontrol-Type-Descriptors-custom"></a>
The custom descriptor, populated when the record type is CUSTOM.  
Type: [CustomDescriptor](#API_CustomDescriptor) object  
Required: No

 ** http **   <a name="agentregistrycontrol-Type-Descriptors-http"></a>
The HTTP descriptor, populated for records detected from an HTTP protocol source.  
Type: [HttpDescriptor](#API_HttpDescriptor) object  
Required: No

 ** mcpServer **   <a name="agentregistrycontrol-Type-Descriptors-mcpServer"></a>
The MCP server descriptor, populated when the record type is MCP.  
Type: [McpServerDescriptor](#API_McpServerDescriptor) object  
Required: No

### See Also
<a name="API_Descriptors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/Descriptors) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/Descriptors) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/Descriptors) 

## DescriptorSource
<a name="API_DescriptorSource"></a>

The source configuration that defines where descriptor content is retrieved from.

### Contents
<a name="API_DescriptorSource_Contents"></a>

 ** fromUrl **   <a name="agentregistrycontrol-Type-DescriptorSource-fromUrl"></a>
URL-based descriptor source, populated when descriptor content is synchronized from a URL.  
Type: [DescriptorSourceFromUrl](#API_DescriptorSourceFromUrl) object  
Required: No

### See Also
<a name="API_DescriptorSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/DescriptorSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/DescriptorSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/DescriptorSource) 

## DescriptorSourceFromUrl
<a name="API_DescriptorSourceFromUrl"></a>

URL-based descriptor source configuration, with credential provider configurations for authenticated URL retrieval.

### Contents
<a name="API_DescriptorSourceFromUrl_Contents"></a>

 ** url **   <a name="agentregistrycontrol-Type-DescriptorSourceFromUrl-url"></a>
The URL from which the descriptor content is retrieved.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `https://.*`   
Required: Yes

 ** credentialProviderConfigurations **   <a name="agentregistrycontrol-Type-DescriptorSourceFromUrl-credentialProviderConfigurations"></a>
The credential providers used to authenticate when fetching descriptor content from the source URL.  
Type: Array of [RegistryRecordCredentialProviderConfiguration](#API_RegistryRecordCredentialProviderConfiguration) objects  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Required: No

### See Also
<a name="API_DescriptorSourceFromUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/DescriptorSourceFromUrl) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/DescriptorSourceFromUrl) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/DescriptorSourceFromUrl) 

## DiscoveryConfiguration
<a name="API_DiscoveryConfiguration"></a>

Discovery configuration for the registry. Controls how consumers are authorized to search the registry and invoke its MCP endpoint.

### Contents
<a name="API_DiscoveryConfiguration_Contents"></a>

 ** authorizerConfiguration **   <a name="agentregistrycontrol-Type-DiscoveryConfiguration-authorizerConfiguration"></a>
The authorizer configuration for the registry. Required when authorizerType is CUSTOM\_JWT.  
Type: [AuthorizerConfiguration](#API_AuthorizerConfiguration) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** authorizerType **   <a name="agentregistrycontrol-Type-DiscoveryConfiguration-authorizerType"></a>
The type of authorizer that controls how consumers access the registry's search and MCP invoke operations.  
Type: String  
Valid Values: `CUSTOM_JWT | AWS_IAM`   
Required: No

### See Also
<a name="API_DiscoveryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/DiscoveryConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/DiscoveryConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/DiscoveryConfiguration) 

## EncryptionConfiguration
<a name="API_EncryptionConfiguration"></a>

The server-side encryption configuration for a registry. Specifies a customer-managed AWS KMS key used to encrypt the registry's content.

### Contents
<a name="API_EncryptionConfiguration_Contents"></a>

 ** kmsKeyArn **   <a name="agentregistrycontrol-Type-EncryptionConfiguration-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the customer-managed AWS KMS key used to encrypt the registry's content. The key must be a symmetric encryption key in the same AWS account and Region as the registry.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: Yes

### See Also
<a name="API_EncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/EncryptionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/EncryptionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/EncryptionConfiguration) 

## HttpDescriptor
<a name="API_HttpDescriptor"></a>

A registry record descriptor for the HTTP protocol. This descriptor is source-only: its content is synchronized from the configured source URL rather than supplied inline.

### Contents
<a name="API_HttpDescriptor_Contents"></a>

 ** source **   <a name="agentregistrycontrol-Type-HttpDescriptor-source"></a>
The source configuration that defines where descriptor content is retrieved from.  
Type: [DescriptorSource](#API_DescriptorSource) object  
Required: No

### See Also
<a name="API_HttpDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/HttpDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/HttpDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/HttpDescriptor) 

## ManagedVpcResource
<a name="API_ManagedVpcResource"></a>

A service-managed private endpoint provisioned within a customer VPC.

### Contents
<a name="API_ManagedVpcResource_Contents"></a>

 ** endpointIpAddressType **   <a name="agentregistrycontrol-Type-ManagedVpcResource-endpointIpAddressType"></a>
The IP address type used by the private endpoint, either IPV4 or IPV6.  
Type: String  
Valid Values: `IPV4 | IPV6`   
Required: Yes

 ** subnetIds **   <a name="agentregistrycontrol-Type-ManagedVpcResource-subnetIds"></a>
The identifiers of the subnets in which the private endpoint network interfaces are placed.  
Type: Array of strings  
Length Constraints: Minimum length of 15. Maximum length of 24.  
Pattern: `subnet-[0-9a-zA-Z]{8,17}`   
Required: Yes

 ** vpcIdentifier **   <a name="agentregistrycontrol-Type-ManagedVpcResource-vpcIdentifier"></a>
The identifier of the VPC in which the private endpoint is provisioned.  
Type: String  
Length Constraints: Minimum length of 10. Maximum length of 48.  
Pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`   
Required: Yes

 ** routingDomain **   <a name="agentregistrycontrol-Type-ManagedVpcResource-routingDomain"></a>
The routing domain used to resolve traffic through the private endpoint.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 255.  
Required: No

 ** securityGroupIds **   <a name="agentregistrycontrol-Type-ManagedVpcResource-securityGroupIds"></a>
The identifiers of the security groups associated with the private endpoint network interfaces.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 5 items.  
Length Constraints: Minimum length of 10. Maximum length of 48.  
Pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`   
Required: No

 ** tags **   <a name="agentregistrycontrol-Type-ManagedVpcResource-tags"></a>
The tags applied to the service-managed VPC resource.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

### See Also
<a name="API_ManagedVpcResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/ManagedVpcResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/ManagedVpcResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/ManagedVpcResource) 

## McpServerAdditionalData
<a name="API_McpServerAdditionalData"></a>

Additional data for an MCP server descriptor

### Contents
<a name="API_McpServerAdditionalData_Contents"></a>

 ** tools **   <a name="agentregistrycontrol-Type-McpServerAdditionalData-tools"></a>
The MCP tools descriptor that defines the tools exposed by the MCP server.  
Type: [McpToolsDescriptor](#API_McpToolsDescriptor) object  
Required: No

### See Also
<a name="API_McpServerAdditionalData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/McpServerAdditionalData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/McpServerAdditionalData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/McpServerAdditionalData) 

## McpServerDescriptor
<a name="API_McpServerDescriptor"></a>

Descriptor that defines the content of an MCP (Model Context Protocol) server registry record, including the server definition and its tool definitions. The content is validated against the MCP protocol schema.

### Contents
<a name="API_McpServerDescriptor_Contents"></a>

 ** additionalData **   <a name="agentregistrycontrol-Type-McpServerDescriptor-additionalData"></a>
Additional data associated with the MCP server descriptor, such as tool definitions.  
Type: [McpServerAdditionalData](#API_McpServerAdditionalData) object  
Required: No

 ** data **   <a name="agentregistrycontrol-Type-McpServerDescriptor-data"></a>
The MCP server descriptor content, serialized as descriptor payload data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 102400.  
Required: No

 ** dataSchemaVersion **   <a name="agentregistrycontrol-Type-McpServerDescriptor-dataSchemaVersion"></a>
The schema version of the descriptor payload.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** source **   <a name="agentregistrycontrol-Type-McpServerDescriptor-source"></a>
The optional source configuration used to synchronize the MCP server descriptor content.  
Type: [DescriptorSource](#API_DescriptorSource) object  
Required: No

### See Also
<a name="API_McpServerDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/McpServerDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/McpServerDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/McpServerDescriptor) 

## McpToolsDescriptor
<a name="API_McpToolsDescriptor"></a>

MCP tools descriptor containing tool definitions

### Contents
<a name="API_McpToolsDescriptor_Contents"></a>

 ** data **   <a name="agentregistrycontrol-Type-McpToolsDescriptor-data"></a>
The MCP tools descriptor content, serialized as descriptor payload data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 102400.  
Required: No

 ** dataSchemaVersion **   <a name="agentregistrycontrol-Type-McpToolsDescriptor-dataSchemaVersion"></a>
The schema version of the descriptor payload.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

### See Also
<a name="API_McpToolsDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/McpToolsDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/McpToolsDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/McpToolsDescriptor) 

## PrivateEndpoint
<a name="API_PrivateEndpoint"></a>

A private network endpoint used to reach a resource over a private path. Exactly one member is set.

### Contents
<a name="API_PrivateEndpoint_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** managedVpcResource **   <a name="agentregistrycontrol-Type-PrivateEndpoint-managedVpcResource"></a>
A private endpoint backed by a service-managed VPC resource.  
Type: [ManagedVpcResource](#API_ManagedVpcResource) object  
Required: No

 ** selfManagedLatticeResource **   <a name="agentregistrycontrol-Type-PrivateEndpoint-selfManagedLatticeResource"></a>
A private endpoint backed by a self-managed VPC Lattice resource configuration.  
Type: [SelfManagedLatticeResource](#API_SelfManagedLatticeResource) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

### See Also
<a name="API_PrivateEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/PrivateEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/PrivateEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/PrivateEndpoint) 

## PrivateEndpointOverride
<a name="API_PrivateEndpointOverride"></a>

A mapping of a domain to the private endpoint used to reach it.

### Contents
<a name="API_PrivateEndpointOverride_Contents"></a>

 ** domain **   <a name="agentregistrycontrol-Type-PrivateEndpointOverride-domain"></a>
The domain name to which this private endpoint override applies.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 253.  
Required: Yes

 ** privateEndpoint **   <a name="agentregistrycontrol-Type-PrivateEndpointOverride-privateEndpoint"></a>
The private endpoint used to reach the specified domain.  
Type: [PrivateEndpoint](#API_PrivateEndpoint) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

### See Also
<a name="API_PrivateEndpointOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/PrivateEndpointOverride) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/PrivateEndpointOverride) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/PrivateEndpointOverride) 

## Provenance
<a name="API_Provenance"></a>

A provenance entry that describes the lineage of a registry record. Records that were auto-detected by AWS Agent Registry carry a provenance entry that links the record back to its upstream source.

### Contents
<a name="API_Provenance_Contents"></a>

 ** relation **   <a name="agentregistrycontrol-Type-Provenance-relation"></a>
The relationship between the registry record and its upstream source. `DETECTED_FROM` indicates that the record was auto-detected from the source resource.  
Type: String  
Valid Values: `DETECTED_FROM`   
Required: Yes

 ** sourceId **   <a name="agentregistrycontrol-Type-Provenance-sourceId"></a>
The identifier of the upstream source that the registry record was detected from.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:[a-zA-Z0-9-]+:[a-z0-9-]*:[0-9]{12}:.+`   
Required: Yes

 ** sourceDetails **   <a name="agentregistrycontrol-Type-Provenance-sourceDetails"></a>
Additional details about the upstream source that the registry record was detected from, such as the AgentCore Gateway or Runtime configuration. The populated member corresponds to the source type.  
Type: [SourceDetails](#API_SourceDetails) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** sourceType **   <a name="agentregistrycontrol-Type-Provenance-sourceType"></a>
The type of the upstream source that the registry record was detected from.  
Type: String  
Valid Values: `AWS::BedrockAgentCore::Runtime | AWS::BedrockAgentCore::Gateway`   
Required: No

### See Also
<a name="API_Provenance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/Provenance) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/Provenance) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/Provenance) 

## ProvenanceSummary
<a name="API_ProvenanceSummary"></a>

A condensed provenance entry surfaced in list results. Contains the source identity of a lineage entry without the source details returned by `GetRegistryRecord`.

### Contents
<a name="API_ProvenanceSummary_Contents"></a>

 ** relation **   <a name="agentregistrycontrol-Type-ProvenanceSummary-relation"></a>
The relationship between the registry record and its upstream source. `DETECTED_FROM` indicates that the record was auto-detected from the source resource.  
Type: String  
Valid Values: `DETECTED_FROM`   
Required: Yes

 ** sourceId **   <a name="agentregistrycontrol-Type-ProvenanceSummary-sourceId"></a>
The identifier of the upstream source that the registry record was detected from.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:[a-zA-Z0-9-]+:[a-z0-9-]*:[0-9]{12}:.+`   
Required: Yes

 ** sourceType **   <a name="agentregistrycontrol-Type-ProvenanceSummary-sourceType"></a>
The type of the upstream source that the registry record was detected from.  
Type: String  
Valid Values: `AWS::BedrockAgentCore::Runtime | AWS::BedrockAgentCore::Gateway`   
Required: No

### See Also
<a name="API_ProvenanceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/ProvenanceSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/ProvenanceSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/ProvenanceSummary) 

## RegistryFilter
<a name="API_RegistryFilter"></a>

A single filter applied to a ListRegistries request.

### Contents
<a name="API_RegistryFilter_Contents"></a>

 ** name **   <a name="agentregistrycontrol-Type-RegistryFilter-name"></a>
The attribute to filter on  
Type: String  
Valid Values: `status | discoveryConfiguration.authorizerType`   
Required: Yes

 ** values **   <a name="agentregistrycontrol-Type-RegistryFilter-values"></a>
The values to match for the attribute  
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

### See Also
<a name="API_RegistryFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/RegistryFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/RegistryFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/RegistryFilter) 

## RegistryRecordCredentialProviderConfiguration
<a name="API_RegistryRecordCredentialProviderConfiguration"></a>

A credential provider configuration that specifies how to authenticate when fetching descriptor content from a registry record's source URL.

### Contents
<a name="API_RegistryRecordCredentialProviderConfiguration_Contents"></a>

 ** credentialProvider **   <a name="agentregistrycontrol-Type-RegistryRecordCredentialProviderConfiguration-credentialProvider"></a>
The credential provider details corresponding to the specified credential provider type.  
Type: [RegistryRecordCredentialProviderUnion](#API_RegistryRecordCredentialProviderUnion) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** credentialProviderType **   <a name="agentregistrycontrol-Type-RegistryRecordCredentialProviderConfiguration-credentialProviderType"></a>
The type of credential provider.  
Type: String  
Valid Values: `OAUTH | IAM`   
Required: Yes

### See Also
<a name="API_RegistryRecordCredentialProviderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/RegistryRecordCredentialProviderConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/RegistryRecordCredentialProviderConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/RegistryRecordCredentialProviderConfiguration) 

## RegistryRecordCredentialProviderUnion
<a name="API_RegistryRecordCredentialProviderUnion"></a>

The credential provider details for a registry record. Exactly one member is populated, matching the configured credential provider type.

### Contents
<a name="API_RegistryRecordCredentialProviderUnion_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** iamCredentialProvider **   <a name="agentregistrycontrol-Type-RegistryRecordCredentialProviderUnion-iamCredentialProvider"></a>
The IAM role credential provider details.  
Type: [RegistryRecordIamCredentialProvider](#API_RegistryRecordIamCredentialProvider) object  
Required: No

 ** oauthCredentialProvider **   <a name="agentregistrycontrol-Type-RegistryRecordCredentialProviderUnion-oauthCredentialProvider"></a>
The OAuth 2.0 credential provider details.  
Type: [RegistryRecordOAuthCredentialProvider](#API_RegistryRecordOAuthCredentialProvider) object  
Required: No

### See Also
<a name="API_RegistryRecordCredentialProviderUnion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/RegistryRecordCredentialProviderUnion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/RegistryRecordCredentialProviderUnion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/RegistryRecordCredentialProviderUnion) 

## RegistryRecordFilter
<a name="API_RegistryRecordFilter"></a>

A single filter applied to a ListRegistryRecords request.

### Contents
<a name="API_RegistryRecordFilter_Contents"></a>

 ** name **   <a name="agentregistrycontrol-Type-RegistryRecordFilter-name"></a>
The attribute to filter on  
Type: String  
Valid Values: `name | status | recordType`   
Required: Yes

 ** values **   <a name="agentregistrycontrol-Type-RegistryRecordFilter-values"></a>
The values to match for the attribute  
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

### See Also
<a name="API_RegistryRecordFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/RegistryRecordFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/RegistryRecordFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/RegistryRecordFilter) 

## RegistryRecordIamCredentialProvider
<a name="API_RegistryRecordIamCredentialProvider"></a>

The configuration for an IAM role credential provider that signs requests to a registry record's source with AWS Signature Version 4 (SigV4).

### Contents
<a name="API_RegistryRecordIamCredentialProvider_Contents"></a>

 ** region **   <a name="agentregistrycontrol-Type-RegistryRecordIamCredentialProvider-region"></a>
The AWS Region to use for request signing. If not specified, the Region is derived from the source URL hostname, falling back to the Region of the registry.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-z0-9-]+`   
Required: No

 ** roleArn **   <a name="agentregistrycontrol-Type-RegistryRecordIamCredentialProvider-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role to assume for request signing.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`   
Required: No

 ** service **   <a name="agentregistrycontrol-Type-RegistryRecordIamCredentialProvider-service"></a>
The service name to use for request signing, such as execute-api.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: No

### See Also
<a name="API_RegistryRecordIamCredentialProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/RegistryRecordIamCredentialProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/RegistryRecordIamCredentialProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/RegistryRecordIamCredentialProvider) 

## RegistryRecordOAuthCredentialProvider
<a name="API_RegistryRecordOAuthCredentialProvider"></a>

The configuration for an OAuth 2.0 credential provider that authenticates requests to a registry record's source.

### Contents
<a name="API_RegistryRecordOAuthCredentialProvider_Contents"></a>

 ** providerArn **   <a name="agentregistrycontrol-Type-RegistryRecordOAuthCredentialProvider-providerArn"></a>
The Amazon Resource Name (ARN) of the OAuth 2.0 credential provider resource in Amazon Bedrock AgentCore Identity.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:.*`   
Required: Yes

 ** customParameters **   <a name="agentregistrycontrol-Type-RegistryRecordOAuthCredentialProvider-customParameters"></a>
Additional parameters to include in the OAuth 2.0 token request.  
Type: String to string map  
Required: No

 ** grantType **   <a name="agentregistrycontrol-Type-RegistryRecordOAuthCredentialProvider-grantType"></a>
The OAuth 2.0 grant type used to obtain access tokens.  
Type: String  
Valid Values: `CLIENT_CREDENTIALS`   
Required: No

 ** scopes **   <a name="agentregistrycontrol-Type-RegistryRecordOAuthCredentialProvider-scopes"></a>
The OAuth 2.0 scopes to request when obtaining access tokens.  
Type: Array of strings  
Required: No

### See Also
<a name="API_RegistryRecordOAuthCredentialProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/RegistryRecordOAuthCredentialProvider) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/RegistryRecordOAuthCredentialProvider) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/RegistryRecordOAuthCredentialProvider) 

## RegistryRecordSummary
<a name="API_RegistryRecordSummary"></a>

A summary of a registry record returned by list operations. Contains identifying and lifecycle fields but omits descriptor content.

### Contents
<a name="API_RegistryRecordSummary_Contents"></a>

 ** createdAt **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-createdAt"></a>
The timestamp when the registry record was created.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-name"></a>
The name of the registry record. Names are unique within a registry.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`   
Required: Yes

 ** recordArn **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-recordArn"></a>
The Amazon Resource Name (ARN) of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}`   
Required: Yes

 ** recordId **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-recordId"></a>
The unique identifier of the registry record.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[a-zA-Z0-9]{12}`   
Required: Yes

 ** recordType **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-recordType"></a>
The type of the registry record, such as MCP, AGENT, SKILL, or CUSTOM.  
Type: String  
Valid Values: `MCP | AGENT | CUSTOM | SKILL | GATEWAY`   
Required: Yes

 ** recordVersion **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-recordVersion"></a>
The version identifier of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9.-]+`   
Required: Yes

 ** registryArn **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-registryArn"></a>
The Amazon Resource Name (ARN) of the parent registry that owns the record.  
Type: String  
Length Constraints: Minimum length of 46. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}`   
Required: Yes

 ** status **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-status"></a>
The lifecycle status of the registry record.  
Type: String  
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | REJECTED | DEPRECATED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED`   
Required: Yes

 ** updatedAt **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-updatedAt"></a>
The timestamp when the registry record was last updated.  
Type: Timestamp  
Required: Yes

 ** createdBy **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-createdBy"></a>
The ID of the AWS account that created the registry record.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[0-9]{12}`   
Required: No

 ** createdByAutoDetection **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-createdByAutoDetection"></a>
Specifies whether the registry record was created by auto-detection. `true` indicates the record was automatically created by the service based on the registry's auto-detection configuration; `false` indicates the record was created through a control-plane API call.  
Type: Boolean  
Required: No

 ** description **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-description"></a>
A description of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** displayName **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-displayName"></a>
The human-readable display name of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** provenanceSummaryList **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-provenanceSummaryList"></a>
The condensed provenance lineage for the registry record. Each entry contains the source relation, source identifier, and source type of an auto-detection lineage entry. Populated for records created by auto-detection.  
Type: Array of [ProvenanceSummary](#API_ProvenanceSummary) objects  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Required: No

### See Also
<a name="API_RegistryRecordSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/RegistryRecordSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/RegistryRecordSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/RegistryRecordSummary) 

## RegistrySummary
<a name="API_RegistrySummary"></a>

Registry summary for list operations

### Contents
<a name="API_RegistrySummary_Contents"></a>

 ** createdAt **   <a name="agentregistrycontrol-Type-RegistrySummary-createdAt"></a>
The timestamp when the registry was created  
Type: Timestamp  
Required: Yes

 ** name **   <a name="agentregistrycontrol-Type-RegistrySummary-name"></a>
Registry name  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`   
Required: Yes

 ** registryArn **   <a name="agentregistrycontrol-Type-RegistrySummary-registryArn"></a>
Registry Amazon Resource Name  
Type: String  
Length Constraints: Minimum length of 46. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}`   
Required: Yes

 ** registryId **   <a name="agentregistrycontrol-Type-RegistrySummary-registryId"></a>
Unique registry identifier  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 16.  
Pattern: `[a-zA-Z0-9]{12,16}`   
Required: Yes

 ** status **   <a name="agentregistrycontrol-Type-RegistrySummary-status"></a>
Current status of the registry  
Type: String  
Valid Values: `CREATING | READY | UPDATING | CREATE_FAILED | UPDATE_FAILED | DELETING | DELETE_FAILED`   
Required: Yes

 ** updatedAt **   <a name="agentregistrycontrol-Type-RegistrySummary-updatedAt"></a>
The timestamp when the registry was last updated  
Type: Timestamp  
Required: Yes

 ** autoDetection **   <a name="agentregistrycontrol-Type-RegistrySummary-autoDetection"></a>
The registry's auto-detection properties, including the requested configuration and the current detection status. Present only when auto-detection was configured for the registry.  
Type: [AutoDetection](#API_AutoDetection) object  
Required: No

 ** description **   <a name="agentregistrycontrol-Type-RegistrySummary-description"></a>
Registry description  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** discoveryConfiguration **   <a name="agentregistrycontrol-Type-RegistrySummary-discoveryConfiguration"></a>
Discovery configuration for the registry  
Type: [DiscoveryConfiguration](#API_DiscoveryConfiguration) object  
Required: No

 ** statusReason **   <a name="agentregistrycontrol-Type-RegistrySummary-statusReason"></a>
The reason for the current status. Typically populated when the status indicates a failure state.  
Type: String  
Required: No

### See Also
<a name="API_RegistrySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/RegistrySummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/RegistrySummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/RegistrySummary) 

## SelfManagedLatticeResource
<a name="API_SelfManagedLatticeResource"></a>

A self-managed private endpoint backed by a VPC Lattice resource configuration. Exactly one member is set.

### Contents
<a name="API_SelfManagedLatticeResource_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** resourceConfigurationIdentifier **   <a name="agentregistrycontrol-Type-SelfManagedLatticeResource-resourceConfigurationIdentifier"></a>
The identifier of the VPC Lattice resource configuration, specified as a resource configuration ID or ARN.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`   
Required: No

### See Also
<a name="API_SelfManagedLatticeResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/SelfManagedLatticeResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/SelfManagedLatticeResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/SelfManagedLatticeResource) 

## SourceDetails
<a name="API_SourceDetails"></a>

The details about the upstream source from which a registry record was detected. Exactly one member is populated, corresponding to the source type.

### Contents
<a name="API_SourceDetails_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** agentcoreGateway **   <a name="agentregistrycontrol-Type-SourceDetails-agentcoreGateway"></a>
The source details for a registry record that was auto-detected from an Amazon Bedrock AgentCore Gateway resource. Populated when the source type is `AWS::BedrockAgentCore::Gateway`.  
Type: [AgentCoreGatewaySourceDetails](#API_AgentCoreGatewaySourceDetails) object  
Required: No

 ** agentcoreRuntime **   <a name="agentregistrycontrol-Type-SourceDetails-agentcoreRuntime"></a>
The source details for a registry record that was auto-detected from an Amazon Bedrock AgentCore Runtime resource. Populated when the source type is `AWS::BedrockAgentCore::Runtime`.  
Type: [AgentCoreRuntimeSourceDetails](#API_AgentCoreRuntimeSourceDetails) object  
Required: No

### See Also
<a name="API_SourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/SourceDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/SourceDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/SourceDetails) 

## UpdatedA2aAgentCardDescriptor
<a name="API_UpdatedA2aAgentCardDescriptor"></a>

The A2A agent card descriptor patch wrapper. Omit to leave the descriptor unchanged; supply an empty object to remove it; supply optionalValue to patch its fields.

### Contents
<a name="API_UpdatedA2aAgentCardDescriptor_Contents"></a>

 ** optionalValue **   <a name="agentregistrycontrol-Type-UpdatedA2aAgentCardDescriptor-optionalValue"></a>
The value to set for this field. Omit the wrapper to leave the field unchanged.  
Type: [UpdatedA2aAgentCardDescriptorFields](#API_UpdatedA2aAgentCardDescriptorFields) object  
Required: No

### See Also
<a name="API_UpdatedA2aAgentCardDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedA2aAgentCardDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedA2aAgentCardDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedA2aAgentCardDescriptor) 

## UpdatedA2aAgentCardDescriptorFields
<a name="API_UpdatedA2aAgentCardDescriptorFields"></a>

The set of A2A agent card descriptor fields that can be individually updated.

### Contents
<a name="API_UpdatedA2aAgentCardDescriptorFields_Contents"></a>

 ** data **   <a name="agentregistrycontrol-Type-UpdatedA2aAgentCardDescriptorFields-data"></a>
The patch for the descriptor's data field.  
Type: [UpdatedDescriptorData](#API_UpdatedDescriptorData) object  
Required: No

 ** dataSchemaVersion **   <a name="agentregistrycontrol-Type-UpdatedA2aAgentCardDescriptorFields-dataSchemaVersion"></a>
The patch for the descriptor's data schema version field.  
Type: [UpdatedDataSchemaVersion](#API_UpdatedDataSchemaVersion) object  
Required: No

 ** source **   <a name="agentregistrycontrol-Type-UpdatedA2aAgentCardDescriptorFields-source"></a>
The patch for the descriptor's source field.  
Type: [UpdatedDescriptorSource](#API_UpdatedDescriptorSource) object  
Required: No

### See Also
<a name="API_UpdatedA2aAgentCardDescriptorFields_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedA2aAgentCardDescriptorFields) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedA2aAgentCardDescriptorFields) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedA2aAgentCardDescriptorFields) 

## UpdatedAgentSkillsAdditionalData
<a name="API_UpdatedAgentSkillsAdditionalData"></a>

The agent skills additional-data patch wrapper. Omit to leave the additional data unchanged; supply an empty object to remove it; supply optionalValue to patch its fields.

### Contents
<a name="API_UpdatedAgentSkillsAdditionalData_Contents"></a>

 ** optionalValue **   <a name="agentregistrycontrol-Type-UpdatedAgentSkillsAdditionalData-optionalValue"></a>
The value to set for this field. Omit the wrapper to leave the field unchanged.  
Type: [UpdatedAgentSkillsAdditionalDataFields](#API_UpdatedAgentSkillsAdditionalDataFields) object  
Required: No

### See Also
<a name="API_UpdatedAgentSkillsAdditionalData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedAgentSkillsAdditionalData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedAgentSkillsAdditionalData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedAgentSkillsAdditionalData) 

## UpdatedAgentSkillsAdditionalDataFields
<a name="API_UpdatedAgentSkillsAdditionalDataFields"></a>

The set of agent skills additional-data fields that can be individually updated.

### Contents
<a name="API_UpdatedAgentSkillsAdditionalDataFields_Contents"></a>

 ** skillMd **   <a name="agentregistrycontrol-Type-UpdatedAgentSkillsAdditionalDataFields-skillMd"></a>
The patch for the agent skills markdown descriptor field.  
Type: [UpdatedAgentSkillsMdDescriptor](#API_UpdatedAgentSkillsMdDescriptor) object  
Required: No

### See Also
<a name="API_UpdatedAgentSkillsAdditionalDataFields_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedAgentSkillsAdditionalDataFields) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedAgentSkillsAdditionalDataFields) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedAgentSkillsAdditionalDataFields) 

## UpdatedAgentSkillsDefinitionDescriptor
<a name="API_UpdatedAgentSkillsDefinitionDescriptor"></a>

The agent skills definition descriptor patch wrapper. Omit to leave the descriptor unchanged; supply an empty object to remove it; supply optionalValue to patch its fields.

### Contents
<a name="API_UpdatedAgentSkillsDefinitionDescriptor_Contents"></a>

 ** optionalValue **   <a name="agentregistrycontrol-Type-UpdatedAgentSkillsDefinitionDescriptor-optionalValue"></a>
The value to set for this field. Omit the wrapper to leave the field unchanged.  
Type: [UpdatedAgentSkillsDefinitionDescriptorFields](#API_UpdatedAgentSkillsDefinitionDescriptorFields) object  
Required: No

### See Also
<a name="API_UpdatedAgentSkillsDefinitionDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedAgentSkillsDefinitionDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedAgentSkillsDefinitionDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedAgentSkillsDefinitionDescriptor) 

## UpdatedAgentSkillsDefinitionDescriptorFields
<a name="API_UpdatedAgentSkillsDefinitionDescriptorFields"></a>

The set of agent skills definition descriptor fields that can be individually updated.

### Contents
<a name="API_UpdatedAgentSkillsDefinitionDescriptorFields_Contents"></a>

 ** additionalData **   <a name="agentregistrycontrol-Type-UpdatedAgentSkillsDefinitionDescriptorFields-additionalData"></a>
The patch for the descriptor's additional data field.  
Type: [UpdatedAgentSkillsAdditionalData](#API_UpdatedAgentSkillsAdditionalData) object  
Required: No

 ** data **   <a name="agentregistrycontrol-Type-UpdatedAgentSkillsDefinitionDescriptorFields-data"></a>
The patch for the descriptor's data field.  
Type: [UpdatedDescriptorData](#API_UpdatedDescriptorData) object  
Required: No

 ** dataSchemaVersion **   <a name="agentregistrycontrol-Type-UpdatedAgentSkillsDefinitionDescriptorFields-dataSchemaVersion"></a>
The patch for the descriptor's data schema version field.  
Type: [UpdatedDataSchemaVersion](#API_UpdatedDataSchemaVersion) object  
Required: No

### See Also
<a name="API_UpdatedAgentSkillsDefinitionDescriptorFields_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedAgentSkillsDefinitionDescriptorFields) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedAgentSkillsDefinitionDescriptorFields) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedAgentSkillsDefinitionDescriptorFields) 

## UpdatedAgentSkillsMdDescriptor
<a name="API_UpdatedAgentSkillsMdDescriptor"></a>

The agent skills markdown descriptor patch wrapper. Omit to leave the descriptor unchanged; supply an empty object to remove it; supply optionalValue to patch its fields.

### Contents
<a name="API_UpdatedAgentSkillsMdDescriptor_Contents"></a>

 ** optionalValue **   <a name="agentregistrycontrol-Type-UpdatedAgentSkillsMdDescriptor-optionalValue"></a>
The value to set for this field. Omit the wrapper to leave the field unchanged.  
Type: [UpdatedAgentSkillsMdDescriptorFields](#API_UpdatedAgentSkillsMdDescriptorFields) object  
Required: No

### See Also
<a name="API_UpdatedAgentSkillsMdDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedAgentSkillsMdDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedAgentSkillsMdDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedAgentSkillsMdDescriptor) 

## UpdatedAgentSkillsMdDescriptorFields
<a name="API_UpdatedAgentSkillsMdDescriptorFields"></a>

The set of agent skills markdown descriptor fields that can be individually updated.

### Contents
<a name="API_UpdatedAgentSkillsMdDescriptorFields_Contents"></a>

 ** data **   <a name="agentregistrycontrol-Type-UpdatedAgentSkillsMdDescriptorFields-data"></a>
The patch for the descriptor's data field.  
Type: [UpdatedDescriptorData](#API_UpdatedDescriptorData) object  
Required: No

 ** dataSchemaVersion **   <a name="agentregistrycontrol-Type-UpdatedAgentSkillsMdDescriptorFields-dataSchemaVersion"></a>
The patch for the descriptor's data schema version field.  
Type: [UpdatedDataSchemaVersion](#API_UpdatedDataSchemaVersion) object  
Required: No

 ** source **   <a name="agentregistrycontrol-Type-UpdatedAgentSkillsMdDescriptorFields-source"></a>
The patch for the descriptor's source field.  
Type: [UpdatedDescriptorSource](#API_UpdatedDescriptorSource) object  
Required: No

### See Also
<a name="API_UpdatedAgentSkillsMdDescriptorFields_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedAgentSkillsMdDescriptorFields) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedAgentSkillsMdDescriptorFields) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedAgentSkillsMdDescriptorFields) 

## UpdatedAgUiDescriptor
<a name="API_UpdatedAgUiDescriptor"></a>

The AG-UI descriptor patch wrapper. Omit to leave the descriptor unchanged; supply an empty object to remove it; supply optionalValue to patch its fields.

### Contents
<a name="API_UpdatedAgUiDescriptor_Contents"></a>

 ** optionalValue **   <a name="agentregistrycontrol-Type-UpdatedAgUiDescriptor-optionalValue"></a>
The value to set for this field. Omit the wrapper to leave the field unchanged.  
Type: [UpdatedAgUiDescriptorFields](#API_UpdatedAgUiDescriptorFields) object  
Required: No

### See Also
<a name="API_UpdatedAgUiDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedAgUiDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedAgUiDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedAgUiDescriptor) 

## UpdatedAgUiDescriptorFields
<a name="API_UpdatedAgUiDescriptorFields"></a>

The set of AG-UI descriptor fields that can be individually updated.

### Contents
<a name="API_UpdatedAgUiDescriptorFields_Contents"></a>

 ** source **   <a name="agentregistrycontrol-Type-UpdatedAgUiDescriptorFields-source"></a>
The patch for the descriptor's source field.  
Type: [UpdatedDescriptorSource](#API_UpdatedDescriptorSource) object  
Required: No

### See Also
<a name="API_UpdatedAgUiDescriptorFields_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedAgUiDescriptorFields) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedAgUiDescriptorFields) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedAgUiDescriptorFields) 

## UpdatedApprovalConfiguration
<a name="API_UpdatedApprovalConfiguration"></a>

A wrapper for updating the approval configuration of a registry. Include this wrapper to replace the approval configuration with the specified value; omit it to leave the approval configuration unchanged.

### Contents
<a name="API_UpdatedApprovalConfiguration_Contents"></a>

 ** optionalValue **   <a name="agentregistrycontrol-Type-UpdatedApprovalConfiguration-optionalValue"></a>
The value to set for this field. Omit the wrapper to leave the field unchanged.  
Type: [ApprovalConfiguration](#API_ApprovalConfiguration) object  
Required: No

### See Also
<a name="API_UpdatedApprovalConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedApprovalConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedApprovalConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedApprovalConfiguration) 

## UpdatedAuthorizerConfiguration
<a name="API_UpdatedAuthorizerConfiguration"></a>

Wrapper for updating an optional authorizer configuration with PATCH semantics.

### Contents
<a name="API_UpdatedAuthorizerConfiguration_Contents"></a>

 ** optionalValue **   <a name="agentregistrycontrol-Type-UpdatedAuthorizerConfiguration-optionalValue"></a>
The new authorizer configuration to set. Omit to leave the existing configuration unchanged.  
Type: [AuthorizerConfiguration](#API_AuthorizerConfiguration) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

### See Also
<a name="API_UpdatedAuthorizerConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedAuthorizerConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedAuthorizerConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedAuthorizerConfiguration) 

## UpdatedAutoDetectionConfiguration
<a name="API_UpdatedAutoDetectionConfiguration"></a>

A wrapper for updating the auto-detection configuration of a registry with PATCH semantics. Include this wrapper to replace the auto-detection configuration with the specified value. Omit it to leave the auto-detection configuration unchanged. To clear the configuration, include the wrapper with a null `optionalValue`.

### Contents
<a name="API_UpdatedAutoDetectionConfiguration_Contents"></a>

 ** optionalValue **   <a name="agentregistrycontrol-Type-UpdatedAutoDetectionConfiguration-optionalValue"></a>
The value to set for this field. Omit the wrapper to leave the field unchanged.  
Type: [AutoDetectionConfiguration](#API_AutoDetectionConfiguration) object  
Required: No

### See Also
<a name="API_UpdatedAutoDetectionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedAutoDetectionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedAutoDetectionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedAutoDetectionConfiguration) 

## UpdatedCustomDescriptor
<a name="API_UpdatedCustomDescriptor"></a>

The custom descriptor patch wrapper. Omit to leave the descriptor unchanged; supply an empty object to remove it; supply optionalValue to patch its fields.

### Contents
<a name="API_UpdatedCustomDescriptor_Contents"></a>

 ** optionalValue **   <a name="agentregistrycontrol-Type-UpdatedCustomDescriptor-optionalValue"></a>
The value to set for this field. Omit the wrapper to leave the field unchanged.  
Type: [UpdatedCustomDescriptorFields](#API_UpdatedCustomDescriptorFields) object  
Required: No

### See Also
<a name="API_UpdatedCustomDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedCustomDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedCustomDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedCustomDescriptor) 

## UpdatedCustomDescriptorFields
<a name="API_UpdatedCustomDescriptorFields"></a>

The set of custom descriptor fields that can be individually updated.

### Contents
<a name="API_UpdatedCustomDescriptorFields_Contents"></a>

 ** data **   <a name="agentregistrycontrol-Type-UpdatedCustomDescriptorFields-data"></a>
The patch for the descriptor's data field.  
Type: [UpdatedDescriptorData](#API_UpdatedDescriptorData) object  
Required: No

### See Also
<a name="API_UpdatedCustomDescriptorFields_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedCustomDescriptorFields) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedCustomDescriptorFields) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedCustomDescriptorFields) 

## UpdatedDataSchemaVersion
<a name="API_UpdatedDataSchemaVersion"></a>

Leaf patch wrapper for a descriptor's data schema version. Omit to leave unchanged; supply an empty object to unset; supply optionalValue to set.

### Contents
<a name="API_UpdatedDataSchemaVersion_Contents"></a>

 ** optionalValue **   <a name="agentregistrycontrol-Type-UpdatedDataSchemaVersion-optionalValue"></a>
The value to set for this field. Omit the wrapper to leave the field unchanged.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

### See Also
<a name="API_UpdatedDataSchemaVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedDataSchemaVersion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedDataSchemaVersion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedDataSchemaVersion) 

## UpdatedDescription
<a name="API_UpdatedDescription"></a>

Wrapper for updating an optional Description field with PATCH semantics

### Contents
<a name="API_UpdatedDescription_Contents"></a>

 ** optionalValue **   <a name="agentregistrycontrol-Type-UpdatedDescription-optionalValue"></a>
The value to set for this field. Omit the wrapper to leave the field unchanged.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

### See Also
<a name="API_UpdatedDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedDescription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedDescription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedDescription) 

## UpdatedDescriptorData
<a name="API_UpdatedDescriptorData"></a>

Leaf patch wrapper for descriptor data. Omit to leave unchanged; supply an empty object to unset; supply optionalValue to set.

### Contents
<a name="API_UpdatedDescriptorData_Contents"></a>

 ** optionalValue **   <a name="agentregistrycontrol-Type-UpdatedDescriptorData-optionalValue"></a>
The value to set for this field. Omit the wrapper to leave the field unchanged.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 102400.  
Required: No

### See Also
<a name="API_UpdatedDescriptorData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedDescriptorData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedDescriptorData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedDescriptorData) 

## UpdatedDescriptors
<a name="API_UpdatedDescriptors"></a>

The top-level descriptors patch wrapper used in UpdateRegistryRecord. Omit to leave the current descriptors unchanged; supply an empty object to clear them; supply optionalValue to apply a per-field patch.

### Contents
<a name="API_UpdatedDescriptors_Contents"></a>

 ** optionalValue **   <a name="agentregistrycontrol-Type-UpdatedDescriptors-optionalValue"></a>
The value to set for this field. Omit the wrapper to leave the field unchanged.  
Type: [UpdatedDescriptorsFields](#API_UpdatedDescriptorsFields) object  
Required: No

### See Also
<a name="API_UpdatedDescriptors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedDescriptors) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedDescriptors) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedDescriptors) 

## UpdatedDescriptorsFields
<a name="API_UpdatedDescriptorsFields"></a>

The patchable descriptor fields applied during an UpdateRegistryRecord call. Each field is independently patchable.

### Contents
<a name="API_UpdatedDescriptorsFields_Contents"></a>

 ** a2aAgentCard **   <a name="agentregistrycontrol-Type-UpdatedDescriptorsFields-a2aAgentCard"></a>
The patch for the A2A agent card descriptor.  
Type: [UpdatedA2aAgentCardDescriptor](#API_UpdatedA2aAgentCardDescriptor) object  
Required: No

 ** agentSkillsDefinition **   <a name="agentregistrycontrol-Type-UpdatedDescriptorsFields-agentSkillsDefinition"></a>
The patch for the agent skills definition descriptor.  
Type: [UpdatedAgentSkillsDefinitionDescriptor](#API_UpdatedAgentSkillsDefinitionDescriptor) object  
Required: No

 ** agui **   <a name="agentregistrycontrol-Type-UpdatedDescriptorsFields-agui"></a>
The patch for the AG-UI descriptor.  
Type: [UpdatedAgUiDescriptor](#API_UpdatedAgUiDescriptor) object  
Required: No

 ** custom **   <a name="agentregistrycontrol-Type-UpdatedDescriptorsFields-custom"></a>
The patch for the custom descriptor.  
Type: [UpdatedCustomDescriptor](#API_UpdatedCustomDescriptor) object  
Required: No

 ** http **   <a name="agentregistrycontrol-Type-UpdatedDescriptorsFields-http"></a>
The patch for the HTTP descriptor.  
Type: [UpdatedHttpDescriptor](#API_UpdatedHttpDescriptor) object  
Required: No

 ** mcpServer **   <a name="agentregistrycontrol-Type-UpdatedDescriptorsFields-mcpServer"></a>
The patch for the MCP server descriptor.  
Type: [UpdatedMcpServerDescriptor](#API_UpdatedMcpServerDescriptor) object  
Required: No

### See Also
<a name="API_UpdatedDescriptorsFields_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedDescriptorsFields) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedDescriptorsFields) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedDescriptorsFields) 

## UpdatedDescriptorSource
<a name="API_UpdatedDescriptorSource"></a>

Leaf patch wrapper for a descriptor's source configuration. Omit to leave unchanged; supply an empty object to unset; supply optionalValue to set.

### Contents
<a name="API_UpdatedDescriptorSource_Contents"></a>

 ** optionalValue **   <a name="agentregistrycontrol-Type-UpdatedDescriptorSource-optionalValue"></a>
The value to set for this field. Omit the wrapper to leave the field unchanged.  
Type: [DescriptorSource](#API_DescriptorSource) object  
Required: No

### See Also
<a name="API_UpdatedDescriptorSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedDescriptorSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedDescriptorSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedDescriptorSource) 

## UpdatedDiscoveryConfiguration
<a name="API_UpdatedDiscoveryConfiguration"></a>

The discovery configuration fields to update on a registry. Omit this structure to leave the discovery configuration unchanged.

### Contents
<a name="API_UpdatedDiscoveryConfiguration_Contents"></a>

 ** authorizerConfiguration **   <a name="agentregistrycontrol-Type-UpdatedDiscoveryConfiguration-authorizerConfiguration"></a>
Authorization configuration for the registry, with PATCH semantics  
Type: [UpdatedAuthorizerConfiguration](#API_UpdatedAuthorizerConfiguration) object  
Required: No

### See Also
<a name="API_UpdatedDiscoveryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedDiscoveryConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedDiscoveryConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedDiscoveryConfiguration) 

## UpdatedDisplayName
<a name="API_UpdatedDisplayName"></a>

Leaf patch wrapper for a registry record's display name. Omit to leave unchanged; supply an empty object to unset; supply optionalValue to set.

### Contents
<a name="API_UpdatedDisplayName_Contents"></a>

 ** optionalValue **   <a name="agentregistrycontrol-Type-UpdatedDisplayName-optionalValue"></a>
The value to set for this field. Omit the wrapper to leave the field unchanged.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

### See Also
<a name="API_UpdatedDisplayName_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedDisplayName) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedDisplayName) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedDisplayName) 

## UpdatedHttpDescriptor
<a name="API_UpdatedHttpDescriptor"></a>

The HTTP descriptor patch wrapper. Omit to leave the descriptor unchanged; supply an empty object to remove it; supply optionalValue to patch its fields.

### Contents
<a name="API_UpdatedHttpDescriptor_Contents"></a>

 ** optionalValue **   <a name="agentregistrycontrol-Type-UpdatedHttpDescriptor-optionalValue"></a>
The value to set for this field. Omit the wrapper to leave the field unchanged.  
Type: [UpdatedHttpDescriptorFields](#API_UpdatedHttpDescriptorFields) object  
Required: No

### See Also
<a name="API_UpdatedHttpDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedHttpDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedHttpDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedHttpDescriptor) 

## UpdatedHttpDescriptorFields
<a name="API_UpdatedHttpDescriptorFields"></a>

The set of HTTP descriptor fields that can be individually updated.

### Contents
<a name="API_UpdatedHttpDescriptorFields_Contents"></a>

 ** source **   <a name="agentregistrycontrol-Type-UpdatedHttpDescriptorFields-source"></a>
The patch for the descriptor's source field.  
Type: [UpdatedDescriptorSource](#API_UpdatedDescriptorSource) object  
Required: No

### See Also
<a name="API_UpdatedHttpDescriptorFields_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedHttpDescriptorFields) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedHttpDescriptorFields) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedHttpDescriptorFields) 

## UpdatedMcpServerAdditionalData
<a name="API_UpdatedMcpServerAdditionalData"></a>

The MCP server additional-data patch wrapper. Omit to leave the additional data unchanged; supply an empty object to remove it; supply optionalValue to patch its fields.

### Contents
<a name="API_UpdatedMcpServerAdditionalData_Contents"></a>

 ** optionalValue **   <a name="agentregistrycontrol-Type-UpdatedMcpServerAdditionalData-optionalValue"></a>
The value to set for this field. Omit the wrapper to leave the field unchanged.  
Type: [UpdatedMcpServerAdditionalDataFields](#API_UpdatedMcpServerAdditionalDataFields) object  
Required: No

### See Also
<a name="API_UpdatedMcpServerAdditionalData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedMcpServerAdditionalData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedMcpServerAdditionalData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedMcpServerAdditionalData) 

## UpdatedMcpServerAdditionalDataFields
<a name="API_UpdatedMcpServerAdditionalDataFields"></a>

The set of MCP server additional-data fields that can be individually updated.

### Contents
<a name="API_UpdatedMcpServerAdditionalDataFields_Contents"></a>

 ** tools **   <a name="agentregistrycontrol-Type-UpdatedMcpServerAdditionalDataFields-tools"></a>
The patch for the MCP tools descriptor field.  
Type: [UpdatedMcpToolsDescriptor](#API_UpdatedMcpToolsDescriptor) object  
Required: No

### See Also
<a name="API_UpdatedMcpServerAdditionalDataFields_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedMcpServerAdditionalDataFields) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedMcpServerAdditionalDataFields) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedMcpServerAdditionalDataFields) 

## UpdatedMcpServerDescriptor
<a name="API_UpdatedMcpServerDescriptor"></a>

The MCP server descriptor patch wrapper. Omit to leave the descriptor unchanged; supply an empty object to remove it; supply optionalValue to patch its fields.

### Contents
<a name="API_UpdatedMcpServerDescriptor_Contents"></a>

 ** optionalValue **   <a name="agentregistrycontrol-Type-UpdatedMcpServerDescriptor-optionalValue"></a>
The value to set for this field. Omit the wrapper to leave the field unchanged.  
Type: [UpdatedMcpServerDescriptorFields](#API_UpdatedMcpServerDescriptorFields) object  
Required: No

### See Also
<a name="API_UpdatedMcpServerDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedMcpServerDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedMcpServerDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedMcpServerDescriptor) 

## UpdatedMcpServerDescriptorFields
<a name="API_UpdatedMcpServerDescriptorFields"></a>

The set of MCP server descriptor fields that can be individually updated.

### Contents
<a name="API_UpdatedMcpServerDescriptorFields_Contents"></a>

 ** additionalData **   <a name="agentregistrycontrol-Type-UpdatedMcpServerDescriptorFields-additionalData"></a>
The patch for the descriptor's additional data field.  
Type: [UpdatedMcpServerAdditionalData](#API_UpdatedMcpServerAdditionalData) object  
Required: No

 ** data **   <a name="agentregistrycontrol-Type-UpdatedMcpServerDescriptorFields-data"></a>
The patch for the descriptor's data field.  
Type: [UpdatedDescriptorData](#API_UpdatedDescriptorData) object  
Required: No

 ** dataSchemaVersion **   <a name="agentregistrycontrol-Type-UpdatedMcpServerDescriptorFields-dataSchemaVersion"></a>
The patch for the descriptor's data schema version field.  
Type: [UpdatedDataSchemaVersion](#API_UpdatedDataSchemaVersion) object  
Required: No

 ** source **   <a name="agentregistrycontrol-Type-UpdatedMcpServerDescriptorFields-source"></a>
The patch for the descriptor's source field.  
Type: [UpdatedDescriptorSource](#API_UpdatedDescriptorSource) object  
Required: No

### See Also
<a name="API_UpdatedMcpServerDescriptorFields_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedMcpServerDescriptorFields) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedMcpServerDescriptorFields) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedMcpServerDescriptorFields) 

## UpdatedMcpToolsDescriptor
<a name="API_UpdatedMcpToolsDescriptor"></a>

The MCP tools descriptor patch wrapper. Omit to leave the tools descriptor unchanged; supply an empty object to remove it; supply optionalValue to patch its fields.

### Contents
<a name="API_UpdatedMcpToolsDescriptor_Contents"></a>

 ** optionalValue **   <a name="agentregistrycontrol-Type-UpdatedMcpToolsDescriptor-optionalValue"></a>
The value to set for this field. Omit the wrapper to leave the field unchanged.  
Type: [UpdatedMcpToolsDescriptorFields](#API_UpdatedMcpToolsDescriptorFields) object  
Required: No

### See Also
<a name="API_UpdatedMcpToolsDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedMcpToolsDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedMcpToolsDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedMcpToolsDescriptor) 

## UpdatedMcpToolsDescriptorFields
<a name="API_UpdatedMcpToolsDescriptorFields"></a>

The set of MCP tools descriptor fields that can be individually updated.

### Contents
<a name="API_UpdatedMcpToolsDescriptorFields_Contents"></a>

 ** data **   <a name="agentregistrycontrol-Type-UpdatedMcpToolsDescriptorFields-data"></a>
The patch for the descriptor's data field.  
Type: [UpdatedDescriptorData](#API_UpdatedDescriptorData) object  
Required: No

 ** dataSchemaVersion **   <a name="agentregistrycontrol-Type-UpdatedMcpToolsDescriptorFields-dataSchemaVersion"></a>
The patch for the descriptor's data schema version field.  
Type: [UpdatedDataSchemaVersion](#API_UpdatedDataSchemaVersion) object  
Required: No

### See Also
<a name="API_UpdatedMcpToolsDescriptorFields_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UpdatedMcpToolsDescriptorFields) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UpdatedMcpToolsDescriptorFields) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UpdatedMcpToolsDescriptorFields) 

## ValidationExceptionField
<a name="API_ValidationExceptionField"></a>

Describes a single input field that failed validation.

### Contents
<a name="API_ValidationExceptionField_Contents"></a>

 ** message **   <a name="agentregistrycontrol-Type-ValidationExceptionField-message"></a>
A description of why the field failed validation.  
Type: String  
Required: Yes

 ** name **   <a name="agentregistrycontrol-Type-ValidationExceptionField-name"></a>
The name of the field that failed validation.  
Type: String  
Required: Yes

### See Also
<a name="API_ValidationExceptionField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/ValidationExceptionField) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/ValidationExceptionField) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/ValidationExceptionField) 

## WorkloadIdentityDetails
<a name="API_WorkloadIdentityDetails"></a>

The workload identity details associated with a source resource. Present on the source details of a provenance entry when the upstream resource has a workload identity configured.

### Contents
<a name="API_WorkloadIdentityDetails_Contents"></a>

 ** workloadIdentityArn **   <a name="agentregistrycontrol-Type-WorkloadIdentityDetails-workloadIdentityArn"></a>
The Amazon Resource Name (ARN) of the workload identity associated with the source resource.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: Yes

### See Also
<a name="API_WorkloadIdentityDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/WorkloadIdentityDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/WorkloadIdentityDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/WorkloadIdentityDetails) 

# Common Parameters
<a name="CommonParameters"></a>

The following list contains the parameters that all actions use for signing Signature Version 4 requests with a query string. Any action-specific parameters are listed in the topic for that action. For more information about Signature Version 4, see [Signing AWS API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html) in the *IAM User Guide*.

 **X-Amz-Algorithm**   <a name="CommonParameters-X-Amz-Algorithm"></a>
The hash algorithm that you used to create the request signature.  
Condition: Specify this parameter when you include authentication information in a query string instead of in the HTTP authorization header.  
Type: string  
Valid Values: `AWS4-HMAC-SHA256`   
Required: Conditional

 **X-Amz-Credential**   <a name="CommonParameters-X-Amz-Credential"></a>
The credential scope value, which is a string that includes your access key, the date, the region you are targeting, the service you are requesting, and a termination string ("aws4\_request"). The value is expressed in the following format: *access\_key*/*YYYYMMDD*/*region*/*service*/aws4\_request.  
For more information, see [Create a signed AWS API request](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv-create-signed-request.html) in the *IAM User Guide*.  
Condition: Specify this parameter when you include authentication information in a query string instead of in the HTTP authorization header.  
Type: string  
Required: Conditional

 **X-Amz-Date**   <a name="CommonParameters-X-Amz-Date"></a>
The date that is used to create the signature. The format must be ISO 8601 basic format (YYYYMMDD'T'HHMMSS'Z'). For example, the following date time is a valid X-Amz-Date value: `20120325T120000Z`.  
Condition: X-Amz-Date is optional for all requests; it can be used to override the date used for signing requests. If the Date header is specified in the ISO 8601 basic format, X-Amz-Date is not required. When X-Amz-Date is used, it always overrides the value of the Date header. For more information, see [Elements of an AWS API request signature](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv-signing-elements.html) in the *IAM User Guide*.  
Type: string  
Required: Conditional

 **X-Amz-Security-Token**   <a name="CommonParameters-X-Amz-Security-Token"></a>
The temporary security token that was obtained through a call to AWS Security Token Service (AWS STS). For a list of services that support temporary security credentials from AWS STS, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.  
Condition: If you're using temporary security credentials from AWS STS, you must include the security token.  
Type: string  
Required: Conditional

 **X-Amz-Signature**   <a name="CommonParameters-X-Amz-Signature"></a>
Specifies the hex-encoded signature that was calculated from the string to sign and the derived signing key.  
Condition: Specify this parameter when you include authentication information in a query string instead of in the HTTP authorization header.  
Type: string  
Required: Conditional

 **X-Amz-SignedHeaders**   <a name="CommonParameters-X-Amz-SignedHeaders"></a>
Specifies all the HTTP headers that were included as part of the canonical request. For more information about specifying signed headers, see [Create a signed AWS API request](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv-create-signed-request.html) in the *IAM User Guide*.  
Condition: Specify this parameter when you include authentication information in a query string instead of in the HTTP authorization header.  
Type: string  
Required: Conditional

# Common Error Types
<a name="CommonErrors"></a>

This section lists common error types that this AWS service may return. Not all services return all error types listed here. For errors specific to an API action for this service, see the topic for that API action.

 **AccessDeniedException**   <a name="CommonErrors-AccessDeniedException"></a>
You don't have permission to perform this action. Verify that your IAM policy includes the required permissions.  
HTTP Status Code: 403

 **ExpiredTokenException**   <a name="CommonErrors-ExpiredTokenException"></a>
The security token included in the request has expired. Request a new security token and try again.  
HTTP Status Code: 403

 **IncompleteSignature**   <a name="CommonErrors-IncompleteSignature"></a>
The request signature doesn't conform to AWS standards. Verify that you're using valid AWS credentials and that your request is properly formatted. If you're using an SDK, ensure it's up to date.  
HTTP Status Code: 403

 **InternalFailure**   <a name="CommonErrors-InternalFailure"></a>
The request can't be processed right now because of an internal server issue. Try again later. If the problem persists, contact AWS Support.  
HTTP Status Code: 500

 **MalformedHttpRequestException**   <a name="CommonErrors-MalformedHttpRequestException"></a>
The request body can't be processed. This typically happens when the request body can't be decompressed using the specified content encoding algorithm. Verify that the content encoding header matches the compression format used.  
HTTP Status Code: 400

 **NotAuthorized**   <a name="CommonErrors-NotAuthorized"></a>
You don't have permissions to perform this action. Verify that your IAM policy includes the required permissions.  
HTTP Status Code: 401

 **OptInRequired**   <a name="CommonErrors-OptInRequired"></a>
Your AWS account needs a subscription for this service. Verify that you've enabled the service in your account.  
HTTP Status Code: 403

 **RequestAbortedException**   <a name="CommonErrors-RequestAbortedException"></a>
The request was aborted before a response could be returned. This typically happens when the client closes the connection.  
HTTP Status Code: 400

 **RequestEntityTooLargeException**   <a name="CommonErrors-RequestEntityTooLargeException"></a>
The request entity is too large. Reduce the size of the request body and try again.  
HTTP Status Code: 413

 **RequestTimeoutException**   <a name="CommonErrors-RequestTimeoutException"></a>
The request timed out. The server didn't receive the complete request within the expected time frame. Try again.  
HTTP Status Code: 408

 **ServiceUnavailable**   <a name="CommonErrors-ServiceUnavailable"></a>
The service is temporarily unavailable. Try again later.  
HTTP Status Code: 503

 **ThrottlingException**   <a name="CommonErrors-ThrottlingException"></a>
Your request rate is too high. The AWS SDKs automatically retry requests that receive this exception. Reduce the frequency of requests.  
HTTP Status Code: 400

 **UnknownOperationException**   <a name="CommonErrors-UnknownOperationException"></a>
The action or operation isn't recognized. Verify that the action name is spelled correctly and that it's supported by the API version you're using.  
HTTP Status Code: 404

 **UnrecognizedClientException**   <a name="CommonErrors-UnrecognizedClientException"></a>
The X.509 certificate or AWS access key ID you provided doesn't exist in our records. Verify that you're using valid credentials and that they haven't expired.  
HTTP Status Code: 403

 **ValidationError**   <a name="CommonErrors-ValidationError"></a>
The input doesn't meet the required format or constraints. Check that all required parameters are included and that values are valid.  
HTTP Status Code: 400
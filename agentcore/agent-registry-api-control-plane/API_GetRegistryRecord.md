---
title: GetRegistryRecord
description: Retrieves the details of a registry record
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_GetRegistryRecord.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# GetRegistryRecord
<a name="API_GetRegistryRecord"></a>

Retrieves the details of a registry record

## Request Syntax
<a name="API_GetRegistryRecord_RequestSyntax"></a>

```
GET /registries/{{registryId}}/records/{{recordId}} HTTP/1.1
```

## URI Request Parameters
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

## Request Body
<a name="API_GetRegistryRecord_RequestBody"></a>

The request does not have a request body.

## Response Syntax
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

## Response Elements
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
Type: [Descriptors](API_Descriptors.md) object

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
Type: Array of [Provenance](API_Provenance.md) objects  
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

## Errors
<a name="API_GetRegistryRecord_Errors"></a>

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
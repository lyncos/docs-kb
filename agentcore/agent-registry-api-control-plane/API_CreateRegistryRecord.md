---
title: CreateRegistryRecord
description: 'Creates a registry record within a registry. A registry record describes a discoverable resource, such as an MCP server, an agent, an agent skill, or a custom resource. Creation is asynchronous: the record is returned with the CREATING status while it is processed.'
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_CreateRegistryRecord.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# CreateRegistryRecord
<a name="API_CreateRegistryRecord"></a>

Creates a registry record within a registry. A registry record describes a discoverable resource, such as an MCP server, an agent, an agent skill, or a custom resource. Creation is asynchronous: the record is returned with the CREATING status while it is processed.

## Request Syntax
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

## URI Request Parameters
<a name="API_CreateRegistryRecord_RequestParameters"></a>

The request uses the following URI parameters.

 ** [registryId](#API_CreateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-CreateRegistryRecord-request-uri-registryId"></a>
The identifier of the registry in which to create the record (ARN or ID)  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

## Request Body
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
Type: [Descriptors](API_Descriptors.md) object  
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
Type: Array of [Provenance](API_Provenance.md) objects  
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

## Response Syntax
<a name="API_CreateRegistryRecord_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "recordArn": "string",
   "status": "string"
}
```

## Response Elements
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

## Errors
<a name="API_CreateRegistryRecord_Errors"></a>

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
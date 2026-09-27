---
title: UpdateRegistryRecord
description: 'Updates a registry record. The update is asynchronous: the record is returned with the UPDATING status while it is processed. Fields that use update wrappers follow PATCH semantics: omit the field to leave it unchanged.'
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_UpdateRegistryRecord.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# UpdateRegistryRecord
<a name="API_UpdateRegistryRecord"></a>

Updates a registry record. The update is asynchronous: the record is returned with the UPDATING status while it is processed. Fields that use update wrappers follow PATCH semantics: omit the field to leave it unchanged.

## Request Syntax
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

## URI Request Parameters
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

## Request Body
<a name="API_UpdateRegistryRecord_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-request-description"></a>
The updated description of the registry record. Omit to leave the description unchanged; provide an empty wrapper to unset it.  
Type: [UpdatedDescription](API_UpdatedDescription.md) object  
Required: No

 ** [descriptors](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-request-descriptors"></a>
The updated typed descriptor content for the registry record. Omit to leave the descriptors unchanged.  
Type: [UpdatedDescriptors](API_UpdatedDescriptors.md) object  
Required: No

 ** [displayName](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-request-displayName"></a>
The updated display name of the registry record. Omit to leave the display name unchanged; provide an empty wrapper to unset it.  
Type: [UpdatedDisplayName](API_UpdatedDisplayName.md) object  
Required: No

 ** [name](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-request-name"></a>
The updated name of the registry record. Omit to leave the name unchanged.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`   
Required: No

 ** [provenance](#API_UpdateRegistryRecord_RequestSyntax) **   <a name="agentregistrycontrol-UpdateRegistryRecord-request-provenance"></a>
The provenance lineage re-assertion for the registry record. This field is reserved for the AWS Agent Registry auto-detection service principal. Requests that include this field from other callers are rejected. The source identity of an existing lineage is immutable; a re-assertion may only refresh the source details.  
Type: Array of [Provenance](API_Provenance.md) objects  
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

## Response Syntax
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

## Response Elements
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
Type: [Descriptors](API_Descriptors.md) object

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
Type: Array of [Provenance](API_Provenance.md) objects  
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

## Errors
<a name="API_UpdateRegistryRecord_Errors"></a>

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
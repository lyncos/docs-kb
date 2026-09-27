---
title: BatchGetDiscoverableRegistryRecord
description: Retrieves multiple discoverable registry records by ID from a single registry. Records that cannot be retrieved are reported individually in the `errors` list rather than failing the entire request.
product: Amazon Bedrock AgentCore
section: Agent Registry Data Plane API
source_url: https://docs.aws.amazon.com/agent-registry/latest/APIReference/API_BatchGetDiscoverableRegistryRecord.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-data-plane-api
- agentcore
---

# BatchGetDiscoverableRegistryRecord
<a name="API_BatchGetDiscoverableRegistryRecord"></a>

 Retrieves multiple discoverable registry records by ID from a single registry. Records that cannot be retrieved are reported individually in the `errors` list rather than failing the entire request.

## Request Syntax
<a name="API_BatchGetDiscoverableRegistryRecord_RequestSyntax"></a>

```
POST /discoverable-records-batch HTTP/1.1
Content-type: application/json

{
   "entries": [ 
      { 
         "recordIds": [ "{{string}}" ],
         "registryId": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchGetDiscoverableRegistryRecord_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetDiscoverableRegistryRecord_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [entries](#API_BatchGetDiscoverableRegistryRecord_RequestSyntax) **   <a name="agentregistry-BatchGetDiscoverableRegistryRecord-request-entries"></a>
 The registry-scoped groups of record IDs to retrieve. Currently, you can specify exactly one entry.  
Type: Array of [RegistryRecordsEntry](API_RegistryRecordsEntry.md) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

## Response Syntax
<a name="API_BatchGetDiscoverableRegistryRecord_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [ 
      { 
         "errorCode": "string",
         "message": "string",
         "recordId": "string",
         "registryId": "string"
      }
   ],
   "registryRecords": [ 
      { 
         "createdAt": "string",
         "description": "string",
         "descriptors": { 
            "a2aAgentCard": { 
               "data": "string",
               "dataSchemaVersion": "string",
               "source": { 
                  "fromUrl": { 
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
                     "url": "string"
                  }
               }
            }
         },
         "displayName": "string",
         "name": "string",
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

## Response Elements
<a name="API_BatchGetDiscoverableRegistryRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchGetDiscoverableRegistryRecord_ResponseSyntax) **   <a name="agentregistry-BatchGetDiscoverableRegistryRecord-response-errors"></a>
 The per-record errors for records that could not be retrieved. This list is empty when all requested records were returned.  
Type: Array of [BatchGetDiscoverableRegistryRecordError](API_BatchGetDiscoverableRegistryRecordError.md) objects

 ** [registryRecords](#API_BatchGetDiscoverableRegistryRecord_ResponseSyntax) **   <a name="agentregistry-BatchGetDiscoverableRegistryRecord-response-registryRecords"></a>
 The records that were successfully retrieved. Each record correlates to the request by its `recordId`.  
Type: Array of [RegistryRecordSummary](API_RegistryRecordSummary.md) objects

## Errors
<a name="API_BatchGetDiscoverableRegistryRecord_Errors"></a>

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

 ** UnauthorizedException **   
The request could not be authenticated.  
HTTP Status Code: 401

 ** ValidationException **   
The request failed validation of one or more input fields.    
 ** fieldList **   
The list of input fields that failed validation.  
 ** reason **   
The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_BatchGetDiscoverableRegistryRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-2025-12-01/BatchGetDiscoverableRegistryRecord) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-2025-12-01/BatchGetDiscoverableRegistryRecord) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/BatchGetDiscoverableRegistryRecord) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-2025-12-01/BatchGetDiscoverableRegistryRecord) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/BatchGetDiscoverableRegistryRecord) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-2025-12-01/BatchGetDiscoverableRegistryRecord) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-2025-12-01/BatchGetDiscoverableRegistryRecord) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-2025-12-01/BatchGetDiscoverableRegistryRecord) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-2025-12-01/BatchGetDiscoverableRegistryRecord) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/BatchGetDiscoverableRegistryRecord) 
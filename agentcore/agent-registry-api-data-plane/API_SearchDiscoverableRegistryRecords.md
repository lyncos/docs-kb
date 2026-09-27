---
title: SearchDiscoverableRegistryRecords
description: Searches the discoverable registry records in a registry using a natural language query. Returns metadata for the matching records ordered by relevance.
product: Amazon Bedrock AgentCore
section: Agent Registry Data Plane API
source_url: https://docs.aws.amazon.com/agent-registry/latest/APIReference/API_SearchDiscoverableRegistryRecords.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-data-plane-api
- agentcore
---

# SearchDiscoverableRegistryRecords
<a name="API_SearchDiscoverableRegistryRecords"></a>

 Searches the discoverable registry records in a registry using a natural language query. Returns metadata for the matching records ordered by relevance.

## Request Syntax
<a name="API_SearchDiscoverableRegistryRecords_RequestSyntax"></a>

```
POST /discoverable-records-search HTTP/1.1
Content-type: application/json

{
   "filters": {{JSON value}},
   "maxResults": {{number}},
   "registryIds": [ "{{string}}" ],
   "searchQuery": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchDiscoverableRegistryRecords_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchDiscoverableRegistryRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_SearchDiscoverableRegistryRecords_RequestSyntax) **   <a name="agentregistry-SearchDiscoverableRegistryRecords-request-filters"></a>
 An optional structured JSON metadata filter that narrows the search results. Supports the field-level operators `$eq`, `$ne`, and `$in`, and the logical operators `$and` and `$or` on filterable fields.  
Type: JSON value  
Required: No

 ** [maxResults](#API_SearchDiscoverableRegistryRecords_RequestSyntax) **   <a name="agentregistry-SearchDiscoverableRegistryRecords-request-maxResults"></a>
 The maximum number of results to return. Valid values are 1 through 20. The default value is 10.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 20.  
Required: No

 ** [registryIds](#API_SearchDiscoverableRegistryRecords_RequestSyntax) **   <a name="agentregistry-SearchDiscoverableRegistryRecords-request-registryIds"></a>
 The registry identifiers to search within. Currently, you must specify exactly one registry identifier. You can provide either the full AWS Resource Name (ARN) or the registry ID.  
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

 ** [searchQuery](#API_SearchDiscoverableRegistryRecords_RequestSyntax) **   <a name="agentregistry-SearchDiscoverableRegistryRecords-request-searchQuery"></a>
 The natural language query to search for matching registry records.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: Yes

## Response Syntax
<a name="API_SearchDiscoverableRegistryRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
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
<a name="API_SearchDiscoverableRegistryRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [registryRecords](#API_SearchDiscoverableRegistryRecords_ResponseSyntax) **   <a name="agentregistry-SearchDiscoverableRegistryRecords-response-registryRecords"></a>
 The registry records that match the search query, ordered by relevance.  
Type: Array of [RegistryRecordSummary](API_RegistryRecordSummary.md) objects

## Errors
<a name="API_SearchDiscoverableRegistryRecords_Errors"></a>

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
<a name="API_SearchDiscoverableRegistryRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-2025-12-01/SearchDiscoverableRegistryRecords) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-2025-12-01/SearchDiscoverableRegistryRecords) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/SearchDiscoverableRegistryRecords) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-2025-12-01/SearchDiscoverableRegistryRecords) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/SearchDiscoverableRegistryRecords) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-2025-12-01/SearchDiscoverableRegistryRecords) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-2025-12-01/SearchDiscoverableRegistryRecords) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-2025-12-01/SearchDiscoverableRegistryRecords) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-2025-12-01/SearchDiscoverableRegistryRecords) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/SearchDiscoverableRegistryRecords) 
# Agent Registry Data Plane API Reference Agent Registry Data Plane API Reference

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
   + [BatchGetDiscoverableRegistryRecord](#API_BatchGetDiscoverableRegistryRecord)
   + [ListDiscoverableRegistryRecords](#API_ListDiscoverableRegistryRecords)
   + [SearchDiscoverableRegistryRecords](#API_SearchDiscoverableRegistryRecords)
+ [Data Types](#API_Types)
   + [A2aAgentCardDescriptor](#API_A2aAgentCardDescriptor)
   + [AgentSkillsAdditionalData](#API_AgentSkillsAdditionalData)
   + [AgentSkillsDefinitionDescriptor](#API_AgentSkillsDefinitionDescriptor)
   + [AgentSkillsMdDescriptor](#API_AgentSkillsMdDescriptor)
   + [AgUiDescriptor](#API_AgUiDescriptor)
   + [BatchGetDiscoverableRegistryRecordError](#API_BatchGetDiscoverableRegistryRecordError)
   + [CustomDescriptor](#API_CustomDescriptor)
   + [Descriptors](#API_Descriptors)
   + [DescriptorSource](#API_DescriptorSource)
   + [DescriptorSourceFromUrl](#API_DescriptorSourceFromUrl)
   + [DiscoverableRegistryRecordSummary](#API_DiscoverableRegistryRecordSummary)
   + [HttpDescriptor](#API_HttpDescriptor)
   + [McpServerAdditionalData](#API_McpServerAdditionalData)
   + [McpServerDescriptor](#API_McpServerDescriptor)
   + [McpToolsDescriptor](#API_McpToolsDescriptor)
   + [RegistryRecordFilter](#API_RegistryRecordFilter)
   + [RegistryRecordsEntry](#API_RegistryRecordsEntry)
   + [RegistryRecordSummary](#API_RegistryRecordSummary)
   + [ValidationExceptionField](#API_ValidationExceptionField)
+ [Common Parameters](#CommonParameters)
+ [Common Error Types](#CommonErrors)

-----



# Welcome
<a name="Welcome"></a>

 AWS Agent Registry is a managed catalog for publishing and discovering resources such as Model Context Protocol (MCP) servers, agents, and agent skills. The Agent Registry API is its data-plane interface for discovering, searching, and retrieving the approved records published to a registry. The companion Agent Registry Control API provides registry and record management operations.

This document was last published on September 25, 2026. 

# Actions
<a name="API_Operations"></a>

The following actions are supported:
+  [BatchGetDiscoverableRegistryRecord](#API_BatchGetDiscoverableRegistryRecord) 
+  [ListDiscoverableRegistryRecords](#API_ListDiscoverableRegistryRecords) 
+  [SearchDiscoverableRegistryRecords](#API_SearchDiscoverableRegistryRecords) 

## BatchGetDiscoverableRegistryRecord
<a name="API_BatchGetDiscoverableRegistryRecord"></a>

 Retrieves multiple discoverable registry records by ID from a single registry. Records that cannot be retrieved are reported individually in the `errors` list rather than failing the entire request.

### Request Syntax
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

### URI Request Parameters
<a name="API_BatchGetDiscoverableRegistryRecord_RequestParameters"></a>

The request does not use any URI parameters.

### Request Body
<a name="API_BatchGetDiscoverableRegistryRecord_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [entries](#API_BatchGetDiscoverableRegistryRecord_RequestSyntax) **   <a name="agentregistry-BatchGetDiscoverableRegistryRecord-request-entries"></a>
 The registry-scoped groups of record IDs to retrieve. Currently, you can specify exactly one entry.  
Type: Array of [RegistryRecordsEntry](#API_RegistryRecordsEntry) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

### Response Syntax
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

### Response Elements
<a name="API_BatchGetDiscoverableRegistryRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchGetDiscoverableRegistryRecord_ResponseSyntax) **   <a name="agentregistry-BatchGetDiscoverableRegistryRecord-response-errors"></a>
 The per-record errors for records that could not be retrieved. This list is empty when all requested records were returned.  
Type: Array of [BatchGetDiscoverableRegistryRecordError](#API_BatchGetDiscoverableRegistryRecordError) objects

 ** [registryRecords](#API_BatchGetDiscoverableRegistryRecord_ResponseSyntax) **   <a name="agentregistry-BatchGetDiscoverableRegistryRecord-response-registryRecords"></a>
 The records that were successfully retrieved. Each record correlates to the request by its `recordId`.  
Type: Array of [RegistryRecordSummary](#API_RegistryRecordSummary) objects

### Errors
<a name="API_BatchGetDiscoverableRegistryRecord_Errors"></a>

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

### See Also
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

## ListDiscoverableRegistryRecords
<a name="API_ListDiscoverableRegistryRecords"></a>

 Lists the discoverable registry records in a registry. You can optionally filter and paginate the results.

### Request Syntax
<a name="API_ListDiscoverableRegistryRecords_RequestSyntax"></a>

```
POST /registries/{{registryId}}/discoverable-records-list HTTP/1.1
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
<a name="API_ListDiscoverableRegistryRecords_RequestParameters"></a>

The request uses the following URI parameters.

 ** [registryId](#API_ListDiscoverableRegistryRecords_RequestSyntax) **   <a name="agentregistry-ListDiscoverableRegistryRecords-request-uri-registryId"></a>
 The identifier of the registry whose discoverable records are listed. You can provide either the full Amazon Resource Name (ARN) or the registry ID.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

### Request Body
<a name="API_ListDiscoverableRegistryRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListDiscoverableRegistryRecords_RequestSyntax) **   <a name="agentregistry-ListDiscoverableRegistryRecords-request-filters"></a>
 The filters to apply to the discoverable registry record list.  
Type: Array of [RegistryRecordFilter](#API_RegistryRecordFilter) objects  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** [maxResults](#API_ListDiscoverableRegistryRecords_RequestSyntax) **   <a name="agentregistry-ListDiscoverableRegistryRecords-request-maxResults"></a>
 The maximum number of records to return in a single page. Valid values are 1 through 100.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [nextToken](#API_ListDiscoverableRegistryRecords_RequestSyntax) **   <a name="agentregistry-ListDiscoverableRegistryRecords-request-nextToken"></a>
 The pagination token returned by a previous request. Use this value to retrieve the next page of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

### Response Syntax
<a name="API_ListDiscoverableRegistryRecords_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "registryRecords": [ 
      { 
         "createdAt": "string",
         "description": "string",
         "descriptorTypes": [ "string" ],
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

### Response Elements
<a name="API_ListDiscoverableRegistryRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListDiscoverableRegistryRecords_ResponseSyntax) **   <a name="agentregistry-ListDiscoverableRegistryRecords-response-nextToken"></a>
 The pagination token to pass to a subsequent request to retrieve the next page of results. This field is absent when there are no more results.  
Type: String

 ** [registryRecords](#API_ListDiscoverableRegistryRecords_ResponseSyntax) **   <a name="agentregistry-ListDiscoverableRegistryRecords-response-registryRecords"></a>
 The page of discoverable registry record summaries.  
Type: Array of [DiscoverableRegistryRecordSummary](#API_DiscoverableRegistryRecordSummary) objects

### Errors
<a name="API_ListDiscoverableRegistryRecords_Errors"></a>

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

### See Also
<a name="API_ListDiscoverableRegistryRecords_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-2025-12-01/ListDiscoverableRegistryRecords) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-2025-12-01/ListDiscoverableRegistryRecords) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/ListDiscoverableRegistryRecords) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-2025-12-01/ListDiscoverableRegistryRecords) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/ListDiscoverableRegistryRecords) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-2025-12-01/ListDiscoverableRegistryRecords) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-2025-12-01/ListDiscoverableRegistryRecords) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-2025-12-01/ListDiscoverableRegistryRecords) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-2025-12-01/ListDiscoverableRegistryRecords) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/ListDiscoverableRegistryRecords) 

## SearchDiscoverableRegistryRecords
<a name="API_SearchDiscoverableRegistryRecords"></a>

 Searches the discoverable registry records in a registry using a natural language query. Returns metadata for the matching records ordered by relevance.

### Request Syntax
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

### URI Request Parameters
<a name="API_SearchDiscoverableRegistryRecords_RequestParameters"></a>

The request does not use any URI parameters.

### Request Body
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

### Response Syntax
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

### Response Elements
<a name="API_SearchDiscoverableRegistryRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [registryRecords](#API_SearchDiscoverableRegistryRecords_ResponseSyntax) **   <a name="agentregistry-SearchDiscoverableRegistryRecords-response-registryRecords"></a>
 The registry records that match the search query, ordered by relevance.  
Type: Array of [RegistryRecordSummary](#API_RegistryRecordSummary) objects

### Errors
<a name="API_SearchDiscoverableRegistryRecords_Errors"></a>

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

### See Also
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

# Data Types
<a name="API_Types"></a>

The Agent Registry API contains several data types that various actions use. This section describes each data type in detail.

**Note**  
The order of each element in a data type structure is not guaranteed. Applications should not assume a particular order.

The following data types are supported:
+  [A2aAgentCardDescriptor](#API_A2aAgentCardDescriptor) 
+  [AgentSkillsAdditionalData](#API_AgentSkillsAdditionalData) 
+  [AgentSkillsDefinitionDescriptor](#API_AgentSkillsDefinitionDescriptor) 
+  [AgentSkillsMdDescriptor](#API_AgentSkillsMdDescriptor) 
+  [AgUiDescriptor](#API_AgUiDescriptor) 
+  [BatchGetDiscoverableRegistryRecordError](#API_BatchGetDiscoverableRegistryRecordError) 
+  [CustomDescriptor](#API_CustomDescriptor) 
+  [Descriptors](#API_Descriptors) 
+  [DescriptorSource](#API_DescriptorSource) 
+  [DescriptorSourceFromUrl](#API_DescriptorSourceFromUrl) 
+  [DiscoverableRegistryRecordSummary](#API_DiscoverableRegistryRecordSummary) 
+  [HttpDescriptor](#API_HttpDescriptor) 
+  [McpServerAdditionalData](#API_McpServerAdditionalData) 
+  [McpServerDescriptor](#API_McpServerDescriptor) 
+  [McpToolsDescriptor](#API_McpToolsDescriptor) 
+  [RegistryRecordFilter](#API_RegistryRecordFilter) 
+  [RegistryRecordsEntry](#API_RegistryRecordsEntry) 
+  [RegistryRecordSummary](#API_RegistryRecordSummary) 
+  [ValidationExceptionField](#API_ValidationExceptionField) 

## A2aAgentCardDescriptor
<a name="API_A2aAgentCardDescriptor"></a>

 Descriptor that defines the content of an A2A (Agent-to-Agent) agent card registry record. The content is validated against the A2A protocol schema.

### Contents
<a name="API_A2aAgentCardDescriptor_Contents"></a>

 ** data **   <a name="agentregistry-Type-A2aAgentCardDescriptor-data"></a>
 The A2A agent card content, serialized as descriptor payload data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 102400.  
Required: No

 ** dataSchemaVersion **   <a name="agentregistry-Type-A2aAgentCardDescriptor-dataSchemaVersion"></a>
 The schema version of the descriptor payload.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** source **   <a name="agentregistry-Type-A2aAgentCardDescriptor-source"></a>
 The source location from which the A2A (Agent-to-Agent) agent card descriptor content was retrieved.  
Type: [DescriptorSource](#API_DescriptorSource) object  
Required: No

### See Also
<a name="API_A2aAgentCardDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/A2aAgentCardDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/A2aAgentCardDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/A2aAgentCardDescriptor) 

## AgentSkillsAdditionalData
<a name="API_AgentSkillsAdditionalData"></a>

 Additional data for an agent skills definition descriptor.

### Contents
<a name="API_AgentSkillsAdditionalData_Contents"></a>

 ** skillMd **   <a name="agentregistry-Type-AgentSkillsAdditionalData-skillMd"></a>
 The agent skills markdown descriptor associated with the agent skills definition.  
Type: [AgentSkillsMdDescriptor](#API_AgentSkillsMdDescriptor) object  
Required: No

### See Also
<a name="API_AgentSkillsAdditionalData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/AgentSkillsAdditionalData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/AgentSkillsAdditionalData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/AgentSkillsAdditionalData) 

## AgentSkillsDefinitionDescriptor
<a name="API_AgentSkillsDefinitionDescriptor"></a>

 Descriptor that defines an agent skills registry record and its associated content.

### Contents
<a name="API_AgentSkillsDefinitionDescriptor_Contents"></a>

 ** additionalData **   <a name="agentregistry-Type-AgentSkillsDefinitionDescriptor-additionalData"></a>
 Additional data for the agent skills definition, such as the skills markdown descriptor.  
Type: [AgentSkillsAdditionalData](#API_AgentSkillsAdditionalData) object  
Required: No

 ** data **   <a name="agentregistry-Type-AgentSkillsDefinitionDescriptor-data"></a>
 The agent skills definition content, serialized as descriptor payload data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 102400.  
Required: No

 ** dataSchemaVersion **   <a name="agentregistry-Type-AgentSkillsDefinitionDescriptor-dataSchemaVersion"></a>
 The schema version of the descriptor payload.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

### See Also
<a name="API_AgentSkillsDefinitionDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/AgentSkillsDefinitionDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/AgentSkillsDefinitionDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/AgentSkillsDefinitionDescriptor) 

## AgentSkillsMdDescriptor
<a name="API_AgentSkillsMdDescriptor"></a>

 Markdown-format descriptor containing an agent skills document.

### Contents
<a name="API_AgentSkillsMdDescriptor_Contents"></a>

 ** data **   <a name="agentregistry-Type-AgentSkillsMdDescriptor-data"></a>
 The agent skills markdown content, serialized as descriptor payload data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 102400.  
Required: No

 ** dataSchemaVersion **   <a name="agentregistry-Type-AgentSkillsMdDescriptor-dataSchemaVersion"></a>
 The schema version of the descriptor payload.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** source **   <a name="agentregistry-Type-AgentSkillsMdDescriptor-source"></a>
 The source location from which the agent skills markdown content was retrieved.  
Type: [DescriptorSource](#API_DescriptorSource) object  
Required: No

### See Also
<a name="API_AgentSkillsMdDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/AgentSkillsMdDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/AgentSkillsMdDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/AgentSkillsMdDescriptor) 

## AgUiDescriptor
<a name="API_AgUiDescriptor"></a>

 A descriptor for a registry record that exposes an AG-UI protocol endpoint. This descriptor is source-only: it identifies where the endpoint is located and carries no descriptor payload data or schema version.

### Contents
<a name="API_AgUiDescriptor_Contents"></a>

 ** source **   <a name="agentregistry-Type-AgUiDescriptor-source"></a>
 The source location of the AG-UI protocol endpoint.  
Type: [DescriptorSource](#API_DescriptorSource) object  
Required: No

### See Also
<a name="API_AgUiDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/AgUiDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/AgUiDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/AgUiDescriptor) 

## BatchGetDiscoverableRegistryRecordError
<a name="API_BatchGetDiscoverableRegistryRecordError"></a>

 Describes why a requested record could not be retrieved.

### Contents
<a name="API_BatchGetDiscoverableRegistryRecordError_Contents"></a>

 ** errorCode **   <a name="agentregistry-Type-BatchGetDiscoverableRegistryRecordError-errorCode"></a>
 The machine-readable reason that the record could not be retrieved.  
Type: String  
Valid Values: `RESOURCE_NOT_FOUND | ACCESS_DENIED | INTERNAL_ERROR`   
Required: Yes

 ** recordId **   <a name="agentregistry-Type-BatchGetDiscoverableRegistryRecordError-recordId"></a>
 The identifier of the record that could not be retrieved, echoed from the request in the same format that you supplied (ARN or record ID).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/)?[a-zA-Z0-9]{12}`   
Required: Yes

 ** registryId **   <a name="agentregistry-Type-BatchGetDiscoverableRegistryRecordError-registryId"></a>
 The identifier of the registry the record was requested from, echoed from the request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

 ** message **   <a name="agentregistry-Type-BatchGetDiscoverableRegistryRecordError-message"></a>
 An optional human-readable detail about the error. Do not parse this value programmatically.  
Type: String  
Required: No

### See Also
<a name="API_BatchGetDiscoverableRegistryRecordError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/BatchGetDiscoverableRegistryRecordError) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/BatchGetDiscoverableRegistryRecordError) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/BatchGetDiscoverableRegistryRecordError) 

## CustomDescriptor
<a name="API_CustomDescriptor"></a>

Custom descriptor for user-defined content

### Contents
<a name="API_CustomDescriptor_Contents"></a>

 ** data **   <a name="agentregistry-Type-CustomDescriptor-data"></a>
The custom descriptor content, serialized as descriptor payload data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 102400.  
Required: No

### See Also
<a name="API_CustomDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/CustomDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/CustomDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/CustomDescriptor) 

## Descriptors
<a name="API_Descriptors"></a>

 The protocol-specific descriptors that describe how to connect to and use the registry record.

### Contents
<a name="API_Descriptors_Contents"></a>

 ** a2aAgentCard **   <a name="agentregistry-Type-Descriptors-a2aAgentCard"></a>
 The A2A agent card descriptor, populated when the record type is AGENT.  
Type: [A2aAgentCardDescriptor](#API_A2aAgentCardDescriptor) object  
Required: No

 ** agentSkillsDefinition **   <a name="agentregistry-Type-Descriptors-agentSkillsDefinition"></a>
 The agent skills definition descriptor, populated when the record type is SKILL.  
Type: [AgentSkillsDefinitionDescriptor](#API_AgentSkillsDefinitionDescriptor) object  
Required: No

 ** agui **   <a name="agentregistry-Type-Descriptors-agui"></a>
 The AG-UI descriptor, populated when the record exposes an AG-UI protocol endpoint.  
Type: [AgUiDescriptor](#API_AgUiDescriptor) object  
Required: No

 ** custom **   <a name="agentregistry-Type-Descriptors-custom"></a>
 The custom descriptor, populated when the record type is CUSTOM.  
Type: [CustomDescriptor](#API_CustomDescriptor) object  
Required: No

 ** http **   <a name="agentregistry-Type-Descriptors-http"></a>
 The HTTP descriptor, populated when the record exposes an HTTP endpoint.  
Type: [HttpDescriptor](#API_HttpDescriptor) object  
Required: No

 ** mcpServer **   <a name="agentregistry-Type-Descriptors-mcpServer"></a>
 The MCP server descriptor, populated when the record type is MCP.  
Type: [McpServerDescriptor](#API_McpServerDescriptor) object  
Required: No

### See Also
<a name="API_Descriptors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/Descriptors) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/Descriptors) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/Descriptors) 

## DescriptorSource
<a name="API_DescriptorSource"></a>

 The source location from which a descriptor's content was retrieved.

### Contents
<a name="API_DescriptorSource_Contents"></a>

 ** fromUrl **   <a name="agentregistry-Type-DescriptorSource-fromUrl"></a>
 The URL-based descriptor source, populated when descriptor content is synchronized from a URL.  
Type: [DescriptorSourceFromUrl](#API_DescriptorSourceFromUrl) object  
Required: No

### See Also
<a name="API_DescriptorSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/DescriptorSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/DescriptorSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/DescriptorSource) 

## DescriptorSourceFromUrl
<a name="API_DescriptorSourceFromUrl"></a>

 A URL-based descriptor source that identifies where descriptor content is retrieved from.

### Contents
<a name="API_DescriptorSourceFromUrl_Contents"></a>

 ** url **   <a name="agentregistry-Type-DescriptorSourceFromUrl-url"></a>
 The URL from which the descriptor content is retrieved.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `https://.*`   
Required: Yes

### See Also
<a name="API_DescriptorSourceFromUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/DescriptorSourceFromUrl) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/DescriptorSourceFromUrl) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/DescriptorSourceFromUrl) 

## DiscoverableRegistryRecordSummary
<a name="API_DiscoverableRegistryRecordSummary"></a>

 Summary information about a discoverable registry record returned by ` ListDiscoverableRegistryRecords`. This summary does not include descriptors.

### Contents
<a name="API_DiscoverableRegistryRecordSummary_Contents"></a>

 ** createdAt **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-createdAt"></a>
 The timestamp when the registry record was created.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-name"></a>
 The name of the registry record. Names are unique within a registry.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`   
Required: Yes

 ** recordArn **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-recordArn"></a>
 The Amazon Resource Name (ARN) of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}`   
Required: Yes

 ** recordId **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-recordId"></a>
 The unique identifier of the registry record.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[a-zA-Z0-9]{12}`   
Required: Yes

 ** recordType **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-recordType"></a>
 The type of the registry record. `MCP` is a Model Context Protocol server record, `AGENT` is an Agent-to-Agent (A2A) agent card record, `SKILL` is an agent skills definition record, and `CUSTOM` is a record with a custom descriptor.  
Type: String  
Valid Values: `MCP | AGENT | CUSTOM | SKILL | GATEWAY`   
Required: Yes

 ** recordVersion **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-recordVersion"></a>
 The version identifier of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9.-]+`   
Required: Yes

 ** registryArn **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-registryArn"></a>
 The Amazon Resource Name (ARN) of the parent registry that owns the record.  
Type: String  
Length Constraints: Minimum length of 46. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}`   
Required: Yes

 ** status **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-status"></a>
 The lifecycle status of the registry record. A record is `DRAFT` before it is submitted, `PENDING_APPROVAL` while awaiting curator review, and `APPROVED` once it is approved and discoverable. `REJECTED` and `DEPRECATED` records are not discoverable. The `CREATING`, `UPDATING`, `CREATE_FAILED`, and `UPDATE_FAILED` values reflect the state of an in-progress or failed asynchronous change.  
Type: String  
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | REJECTED | DEPRECATED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED`   
Required: Yes

 ** updatedAt **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-updatedAt"></a>
 The timestamp when the registry record was last updated.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-description"></a>
 A human-readable description of the registry record. Use this field to explain the record's purpose or content to consumers discovering it in the registry.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** descriptorTypes **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-descriptorTypes"></a>
 The descriptor types that are present on this registry record. Each value corresponds to a descriptor entry key on the approved record.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** displayName **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-displayName"></a>
 The human-readable display name of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

### See Also
<a name="API_DiscoverableRegistryRecordSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/DiscoverableRegistryRecordSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/DiscoverableRegistryRecordSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/DiscoverableRegistryRecordSummary) 

## HttpDescriptor
<a name="API_HttpDescriptor"></a>

 A descriptor for a registry record that exposes an HTTP endpoint. This descriptor is source-only: it identifies where the endpoint is located and carries no descriptor payload data or schema version.

### Contents
<a name="API_HttpDescriptor_Contents"></a>

 ** source **   <a name="agentregistry-Type-HttpDescriptor-source"></a>
 The source location of the HTTP endpoint.  
Type: [DescriptorSource](#API_DescriptorSource) object  
Required: No

### See Also
<a name="API_HttpDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/HttpDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/HttpDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/HttpDescriptor) 

## McpServerAdditionalData
<a name="API_McpServerAdditionalData"></a>

Additional data for an MCP server descriptor

### Contents
<a name="API_McpServerAdditionalData_Contents"></a>

 ** tools **   <a name="agentregistry-Type-McpServerAdditionalData-tools"></a>
The MCP tools descriptor that defines the tools exposed by the MCP server.  
Type: [McpToolsDescriptor](#API_McpToolsDescriptor) object  
Required: No

### See Also
<a name="API_McpServerAdditionalData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/McpServerAdditionalData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/McpServerAdditionalData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/McpServerAdditionalData) 

## McpServerDescriptor
<a name="API_McpServerDescriptor"></a>

 Descriptor that defines the content of an MCP (Model Context Protocol) server registry record, including the server definition and its tool definitions. The content is validated against the MCP protocol schema.

### Contents
<a name="API_McpServerDescriptor_Contents"></a>

 ** additionalData **   <a name="agentregistry-Type-McpServerDescriptor-additionalData"></a>
 Additional data associated with the MCP server descriptor, such as tool definitions.  
Type: [McpServerAdditionalData](#API_McpServerAdditionalData) object  
Required: No

 ** data **   <a name="agentregistry-Type-McpServerDescriptor-data"></a>
 The MCP server descriptor content, serialized as descriptor payload data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 102400.  
Required: No

 ** dataSchemaVersion **   <a name="agentregistry-Type-McpServerDescriptor-dataSchemaVersion"></a>
 The schema version of the descriptor payload.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** source **   <a name="agentregistry-Type-McpServerDescriptor-source"></a>
 The source location from which the MCP (Model Context Protocol) server descriptor content was retrieved.  
Type: [DescriptorSource](#API_DescriptorSource) object  
Required: No

### See Also
<a name="API_McpServerDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/McpServerDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/McpServerDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/McpServerDescriptor) 

## McpToolsDescriptor
<a name="API_McpToolsDescriptor"></a>

MCP tools descriptor containing tool definitions

### Contents
<a name="API_McpToolsDescriptor_Contents"></a>

 ** data **   <a name="agentregistry-Type-McpToolsDescriptor-data"></a>
The MCP tools descriptor content, serialized as descriptor payload data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 102400.  
Required: No

 ** dataSchemaVersion **   <a name="agentregistry-Type-McpToolsDescriptor-dataSchemaVersion"></a>
The schema version of the descriptor payload.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

### See Also
<a name="API_McpToolsDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/McpToolsDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/McpToolsDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/McpToolsDescriptor) 

## RegistryRecordFilter
<a name="API_RegistryRecordFilter"></a>

 A single filter applied to a `ListDiscoverableRegistryRecords` request.

### Contents
<a name="API_RegistryRecordFilter_Contents"></a>

 ** name **   <a name="agentregistry-Type-RegistryRecordFilter-name"></a>
 The attribute to filter on.  
Type: String  
Valid Values: `recordType | descriptorType`   
Required: Yes

 ** values **   <a name="agentregistry-Type-RegistryRecordFilter-values"></a>
 The values to match for the attribute.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

### See Also
<a name="API_RegistryRecordFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/RegistryRecordFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/RegistryRecordFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/RegistryRecordFilter) 

## RegistryRecordsEntry
<a name="API_RegistryRecordsEntry"></a>

 Binds one registry to the record IDs requested from it.

### Contents
<a name="API_RegistryRecordsEntry_Contents"></a>

 ** recordIds **   <a name="agentregistry-Type-RegistryRecordsEntry-recordIds"></a>
 The record IDs to retrieve from the registry. You can specify 1 through 100 record IDs.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/)?[a-zA-Z0-9]{12}`   
Required: Yes

 ** registryId **   <a name="agentregistry-Type-RegistryRecordsEntry-registryId"></a>
 The identifier of the registry to retrieve the records from. You can provide either the full Amazon Resource Name (ARN) or the registry ID.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

### See Also
<a name="API_RegistryRecordsEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/RegistryRecordsEntry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/RegistryRecordsEntry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/RegistryRecordsEntry) 

## RegistryRecordSummary
<a name="API_RegistryRecordSummary"></a>

 Summary information about a registry record, including its descriptors.

### Contents
<a name="API_RegistryRecordSummary_Contents"></a>

 ** createdAt **   <a name="agentregistry-Type-RegistryRecordSummary-createdAt"></a>
 The timestamp when the registry record was created.  
Type: Timestamp  
Required: Yes

 ** descriptors **   <a name="agentregistry-Type-RegistryRecordSummary-descriptors"></a>
 The protocol-specific descriptors that describe how to connect to and use the record.  
Type: [Descriptors](#API_Descriptors) object  
Required: Yes

 ** name **   <a name="agentregistry-Type-RegistryRecordSummary-name"></a>
 The name of the registry record. Names are unique within a registry.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`   
Required: Yes

 ** recordArn **   <a name="agentregistry-Type-RegistryRecordSummary-recordArn"></a>
 The Amazon Resource Name (ARN) of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}`   
Required: Yes

 ** recordId **   <a name="agentregistry-Type-RegistryRecordSummary-recordId"></a>
 The unique identifier of the registry record.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[a-zA-Z0-9]{12}`   
Required: Yes

 ** recordType **   <a name="agentregistry-Type-RegistryRecordSummary-recordType"></a>
 The type of the registry record. `MCP` is a Model Context Protocol server record, `AGENT` is an Agent-to-Agent (A2A) agent card record, `SKILL` is an agent skills definition record, and `CUSTOM` is a record with a custom descriptor.  
Type: String  
Valid Values: `MCP | AGENT | CUSTOM | SKILL | GATEWAY`   
Required: Yes

 ** recordVersion **   <a name="agentregistry-Type-RegistryRecordSummary-recordVersion"></a>
 The version identifier of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9.-]+`   
Required: Yes

 ** registryArn **   <a name="agentregistry-Type-RegistryRecordSummary-registryArn"></a>
 The Amazon Resource Name (ARN) of the parent registry that owns the record.  
Type: String  
Length Constraints: Minimum length of 46. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}`   
Required: Yes

 ** status **   <a name="agentregistry-Type-RegistryRecordSummary-status"></a>
 The lifecycle status of the registry record. A record is `DRAFT` before it is submitted, `PENDING_APPROVAL` while awaiting curator review, and `APPROVED` once it is approved and discoverable. `REJECTED` and `DEPRECATED` records are not discoverable. The `CREATING`, `UPDATING`, `CREATE_FAILED`, and `UPDATE_FAILED` values reflect the state of an in-progress or failed asynchronous change.  
Type: String  
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | REJECTED | DEPRECATED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED`   
Required: Yes

 ** updatedAt **   <a name="agentregistry-Type-RegistryRecordSummary-updatedAt"></a>
 The timestamp when the registry record was last updated.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="agentregistry-Type-RegistryRecordSummary-description"></a>
 A human-readable description of the registry record. Use this field to explain the record's purpose or content to consumers discovering it in the registry.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** displayName **   <a name="agentregistry-Type-RegistryRecordSummary-displayName"></a>
 The human-readable display name of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

### See Also
<a name="API_RegistryRecordSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/RegistryRecordSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/RegistryRecordSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/RegistryRecordSummary) 

## ValidationExceptionField
<a name="API_ValidationExceptionField"></a>

Describes a single input field that failed validation.

### Contents
<a name="API_ValidationExceptionField_Contents"></a>

 ** message **   <a name="agentregistry-Type-ValidationExceptionField-message"></a>
A description of why the field failed validation.  
Type: String  
Required: Yes

 ** name **   <a name="agentregistry-Type-ValidationExceptionField-name"></a>
The name of the field that failed validation.  
Type: String  
Required: Yes

### See Also
<a name="API_ValidationExceptionField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/ValidationExceptionField) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/ValidationExceptionField) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/ValidationExceptionField) 

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
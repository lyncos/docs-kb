---
title: ListRegistryRecords
description: Lists the registry records within a registry, with optional filtering by name, status, and record type
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_ListRegistryRecords.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# ListRegistryRecords
<a name="API_ListRegistryRecords"></a>

Lists the registry records within a registry, with optional filtering by name, status, and record type

## Request Syntax
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

## URI Request Parameters
<a name="API_ListRegistryRecords_RequestParameters"></a>

The request uses the following URI parameters.

 ** [registryId](#API_ListRegistryRecords_RequestSyntax) **   <a name="agentregistrycontrol-ListRegistryRecords-request-uri-registryId"></a>
The identifier of the registry to list records from (ARN or ID)  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

## Request Body
<a name="API_ListRegistryRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListRegistryRecords_RequestSyntax) **   <a name="agentregistrycontrol-ListRegistryRecords-request-filters"></a>
Filters to apply to the registry record list  
Type: Array of [RegistryRecordFilter](API_RegistryRecordFilter.md) objects  
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

## Response Syntax
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

## Response Elements
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
Type: Array of [RegistryRecordSummary](API_RegistryRecordSummary.md) objects

## Errors
<a name="API_ListRegistryRecords_Errors"></a>

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
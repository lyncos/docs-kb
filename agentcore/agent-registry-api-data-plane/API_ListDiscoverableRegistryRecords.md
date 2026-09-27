---
title: ListDiscoverableRegistryRecords
description: Lists the discoverable registry records in a registry. You can optionally filter and paginate the results.
product: Amazon Bedrock AgentCore
section: Agent Registry Data Plane API
source_url: https://docs.aws.amazon.com/agent-registry/latest/APIReference/API_ListDiscoverableRegistryRecords.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-data-plane-api
- agentcore
---

# ListDiscoverableRegistryRecords
<a name="API_ListDiscoverableRegistryRecords"></a>

 Lists the discoverable registry records in a registry. You can optionally filter and paginate the results.

## Request Syntax
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

## URI Request Parameters
<a name="API_ListDiscoverableRegistryRecords_RequestParameters"></a>

The request uses the following URI parameters.

 ** [registryId](#API_ListDiscoverableRegistryRecords_RequestSyntax) **   <a name="agentregistry-ListDiscoverableRegistryRecords-request-uri-registryId"></a>
 The identifier of the registry whose discoverable records are listed. You can provide either the full Amazon Resource Name (ARN) or the registry ID.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

## Request Body
<a name="API_ListDiscoverableRegistryRecords_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListDiscoverableRegistryRecords_RequestSyntax) **   <a name="agentregistry-ListDiscoverableRegistryRecords-request-filters"></a>
 The filters to apply to the discoverable registry record list.  
Type: Array of [RegistryRecordFilter](API_RegistryRecordFilter.md) objects  
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

## Response Syntax
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

## Response Elements
<a name="API_ListDiscoverableRegistryRecords_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListDiscoverableRegistryRecords_ResponseSyntax) **   <a name="agentregistry-ListDiscoverableRegistryRecords-response-nextToken"></a>
 The pagination token to pass to a subsequent request to retrieve the next page of results. This field is absent when there are no more results.  
Type: String

 ** [registryRecords](#API_ListDiscoverableRegistryRecords_ResponseSyntax) **   <a name="agentregistry-ListDiscoverableRegistryRecords-response-registryRecords"></a>
 The page of discoverable registry record summaries.  
Type: Array of [DiscoverableRegistryRecordSummary](API_DiscoverableRegistryRecordSummary.md) objects

## Errors
<a name="API_ListDiscoverableRegistryRecords_Errors"></a>

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
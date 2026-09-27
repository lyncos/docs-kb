---
title: ListRegistries
description: Lists the registries in the caller's account and Region, with optional filtering by status and discovery authorizer type
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_ListRegistries.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# ListRegistries
<a name="API_ListRegistries"></a>

Lists the registries in the caller's account and Region, with optional filtering by status and discovery authorizer type

## Request Syntax
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

## URI Request Parameters
<a name="API_ListRegistries_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListRegistries_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListRegistries_RequestSyntax) **   <a name="agentregistrycontrol-ListRegistries-request-filters"></a>
Filters to apply to the registry list  
Type: Array of [RegistryFilter](API_RegistryFilter.md) objects  
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

## Response Syntax
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

## Response Elements
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
Type: Array of [RegistrySummary](API_RegistrySummary.md) objects

## Errors
<a name="API_ListRegistries_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

## See Also
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
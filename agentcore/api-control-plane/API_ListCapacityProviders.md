---
title: ListCapacityProviders
description: Lists the capacity providers in your account and returns summary information for each one. To retrieve the full configuration for a specific capacity provider, use `GetCapacityProvider`. Results are paginated; use the `nextToken` parameter to retrieve additional results.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListCapacityProviders.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# ListCapacityProviders
<a name="API_ListCapacityProviders"></a>

Lists the capacity providers in your account and returns summary information for each one. To retrieve the full configuration for a specific capacity provider, use `GetCapacityProvider`. Results are paginated; use the `nextToken` parameter to retrieve additional results.

## Request Syntax
<a name="API_ListCapacityProviders_RequestSyntax"></a>

```
POST /capacity-providers?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCapacityProviders_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListCapacityProviders_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListCapacityProviders-request-uri-maxResults"></a>
The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListCapacityProviders_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListCapacityProviders-request-uri-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, enter the token returned in the `nextToken` field in the response in this field to return the next batch of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Request Body
<a name="API_ListCapacityProviders_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCapacityProviders_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "capacityProviders": [ 
      { 
         "capacityProviderArn": "string",
         "capacityProviderId": "string",
         "lastUpdatedAt": number,
         "name": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCapacityProviders_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [capacityProviders](#API_ListCapacityProviders_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListCapacityProviders-response-capacityProviders"></a>
The list of capacity provider summaries.  
Type: Array of [CapacityProviderSummary](API_CapacityProviderSummary.md) objects

 ** [nextToken](#API_ListCapacityProviders_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListCapacityProviders-response-nextToken"></a>
If the total number of results is greater than the `maxResults` value provided in the request, use this token when making another request in the `nextToken` field to return the next batch of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_ListCapacityProviders_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** InternalServerException **   
This exception is thrown if there was an unexpected error during processing of request  
HTTP Status Code: 500

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_ListCapacityProviders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ListCapacityProviders) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ListCapacityProviders) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListCapacityProviders) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ListCapacityProviders) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListCapacityProviders) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ListCapacityProviders) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ListCapacityProviders) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ListCapacityProviders) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ListCapacityProviders) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListCapacityProviders) 
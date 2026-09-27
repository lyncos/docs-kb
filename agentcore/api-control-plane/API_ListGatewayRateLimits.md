---
title: ListGatewayRateLimits
description: Lists all rate limits for a gateway. Results are paginated. Use the `nextToken` parameter to retrieve additional results.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListGatewayRateLimits.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# ListGatewayRateLimits
<a name="API_ListGatewayRateLimits"></a>

Lists all rate limits for a gateway. Results are paginated. Use the `nextToken` parameter to retrieve additional results.

## Request Syntax
<a name="API_ListGatewayRateLimits_RequestSyntax"></a>

```
GET /gateways/{{gatewayIdentifier}}/rate-limits?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListGatewayRateLimits_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayIdentifier](#API_ListGatewayRateLimits_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListGatewayRateLimits-request-uri-gatewayIdentifier"></a>
The unique identifier of the gateway.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

 ** [maxResults](#API_ListGatewayRateLimits_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListGatewayRateLimits-request-uri-maxResults"></a>
The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the `nextToken` field when making another request to return the next batch of results.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListGatewayRateLimits_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListGatewayRateLimits-request-uri-nextToken"></a>
The token to use to retrieve the next page of results. Use the value returned in a previous `ListGatewayRateLimits` response.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Request Body
<a name="API_ListGatewayRateLimits_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListGatewayRateLimits_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "rateLimits": [ 
      { 
         "createdAt": "string",
         "description": "string",
         "dimensionKeys": [ "string" ],
         "entries": [ 
            { 
               "connections": [ 
                  { 
                     "period": "string",
                     "rate": number
                  }
               ],
               "dimensions": { 
                  "string" : "string" 
               },
               "requests": [ 
                  { 
                     "period": "string",
                     "rate": number
                  }
               ],
               "tokens": [ 
                  { 
                     "period": "string",
                     "rate": number
                  }
               ]
            }
         ],
         "gatewayIdentifier": "string",
         "rateLimitId": "string",
         "status": "string",
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListGatewayRateLimits_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListGatewayRateLimits_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListGatewayRateLimits-response-nextToken"></a>
The token for the next page of results. If this value is absent, there are no more results to retrieve.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [rateLimits](#API_ListGatewayRateLimits_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListGatewayRateLimits-response-rateLimits"></a>
The list of rate limits for the gateway.  
Type: Array of [GatewayRateLimitDetail](API_GatewayRateLimitDetail.md) objects

## Errors
<a name="API_ListGatewayRateLimits_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** InternalServerException **   
This exception is thrown if there was an unexpected error during processing of request  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
This exception is thrown when a resource referenced by the operation does not exist  
HTTP Status Code: 404

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_ListGatewayRateLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ListGatewayRateLimits) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ListGatewayRateLimits) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListGatewayRateLimits) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ListGatewayRateLimits) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListGatewayRateLimits) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ListGatewayRateLimits) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ListGatewayRateLimits) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ListGatewayRateLimits) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ListGatewayRateLimits) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListGatewayRateLimits) 
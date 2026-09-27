---
title: BatchPutGatewayRateLimits
description: Atomically creates or updates multiple rate limits for a gateway. The operation updates existing limits with matching keys and creates new limits for new keys. If the operation fails, the service applies no changes. Retry the request after resolving the issue.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_BatchPutGatewayRateLimits.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# BatchPutGatewayRateLimits
<a name="API_BatchPutGatewayRateLimits"></a>

Atomically creates or updates multiple rate limits for a gateway. The operation updates existing limits with matching keys and creates new limits for new keys. If the operation fails, the service applies no changes. Retry the request after resolving the issue.

## Request Syntax
<a name="API_BatchPutGatewayRateLimits_RequestSyntax"></a>

```
PUT /gateways/{{gatewayIdentifier}}/rate-limits/batch HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "rateLimits": [ 
      { 
         "description": "{{string}}",
         "dimensionKeys": [ "{{string}}" ],
         "entries": [ 
            { 
               "connections": [ 
                  { 
                     "period": "{{string}}",
                     "rate": {{number}}
                  }
               ],
               "dimensions": { 
                  "{{string}}" : "{{string}}" 
               },
               "requests": [ 
                  { 
                     "period": "{{string}}",
                     "rate": {{number}}
                  }
               ],
               "tokens": [ 
                  { 
                     "period": "{{string}}",
                     "rate": {{number}}
                  }
               ]
            }
         ],
         "rateLimitId": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchPutGatewayRateLimits_RequestParameters"></a>

The request uses the following URI parameters.

 ** [gatewayIdentifier](#API_BatchPutGatewayRateLimits_RequestSyntax) **   <a name="bedrockagentcorecontrol-BatchPutGatewayRateLimits-request-uri-gatewayIdentifier"></a>
The unique identifier of the gateway.  
Pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`   
Required: Yes

## Request Body
<a name="API_BatchPutGatewayRateLimits_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_BatchPutGatewayRateLimits_RequestSyntax) **   <a name="bedrockagentcorecontrol-BatchPutGatewayRateLimits-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [rateLimits](#API_BatchPutGatewayRateLimits_RequestSyntax) **   <a name="bedrockagentcorecontrol-BatchPutGatewayRateLimits-request-rateLimits"></a>
The complete set of rate limits for this gateway. This operation replaces all existing rate limits in a single request. If the operation fails, no rate limits are changed.  
Type: Array of [BatchPutLimitEntry](API_BatchPutLimitEntry.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Required: Yes

## Response Syntax
<a name="API_BatchPutGatewayRateLimits_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
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
<a name="API_BatchPutGatewayRateLimits_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [rateLimits](#API_BatchPutGatewayRateLimits_ResponseSyntax) **   <a name="bedrockagentcorecontrol-BatchPutGatewayRateLimits-response-rateLimits"></a>
The resulting set of rate limits after the batch operation.  
Type: Array of [GatewayRateLimitDetail](API_GatewayRateLimitDetail.md) objects

## Errors
<a name="API_BatchPutGatewayRateLimits_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
This exception is thrown when a request is denied per access permissions  
HTTP Status Code: 403

 ** ConflictException **   
This exception is thrown when there is a conflict performing an operation  
HTTP Status Code: 409

 ** InternalServerException **   
This exception is thrown if there was an unexpected error during processing of request  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
This exception is thrown when a resource referenced by the operation does not exist  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
This exception is thrown when a request is made beyond the service quota  
HTTP Status Code: 402

 ** ThrottlingException **   
This exception is thrown when the number of requests exceeds the limit  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_BatchPutGatewayRateLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/BatchPutGatewayRateLimits) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/BatchPutGatewayRateLimits) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/BatchPutGatewayRateLimits) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/BatchPutGatewayRateLimits) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/BatchPutGatewayRateLimits) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/BatchPutGatewayRateLimits) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/BatchPutGatewayRateLimits) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/BatchPutGatewayRateLimits) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/BatchPutGatewayRateLimits) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/BatchPutGatewayRateLimits) 
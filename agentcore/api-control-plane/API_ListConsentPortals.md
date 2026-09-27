---
title: ListConsentPortals
description: Lists all of the consent portals in your account.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListConsentPortals.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# ListConsentPortals
<a name="API_ListConsentPortals"></a>

Lists all of the consent portals in your account.

## Request Syntax
<a name="API_ListConsentPortals_RequestSyntax"></a>

```
POST /identities/ListConsentPortals HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListConsentPortals_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListConsentPortals_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListConsentPortals_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListConsentPortals-request-maxResults"></a>
The maximum number of consent portals to return in a single call.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** [nextToken](#API_ListConsentPortals_RequestSyntax) **   <a name="bedrockagentcorecontrol-ListConsentPortals-request-nextToken"></a>
A token to retrieve the next page of results. Use the value returned in a previous response to request the next page.  
Type: String  
Required: No

## Response Syntax
<a name="API_ListConsentPortals_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "consentPortals": [ 
      { 
         "consentPortalArn": "string",
         "consentPortalId": "string",
         "createdAt": number,
         "description": "string",
         "name": "string",
         "portalUrl": "string",
         "sources": [ 
            { 
               "identifier": "string",
               "type": "string"
            }
         ],
         "status": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListConsentPortals_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [consentPortals](#API_ListConsentPortals_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListConsentPortals-response-consentPortals"></a>
The list of consent portals.  
Type: Array of [ConsentPortalSummary](API_ConsentPortalSummary.md) objects

 ** [nextToken](#API_ListConsentPortals_ResponseSyntax) **   <a name="bedrockagentcorecontrol-ListConsentPortals-response-nextToken"></a>
The token to use in a subsequent request to retrieve the next page of results. This value is null when there are no more results to return.  
Type: String

## Errors
<a name="API_ListConsentPortals_Errors"></a>

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

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_ListConsentPortals_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/ListConsentPortals) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/ListConsentPortals) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ListConsentPortals) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/ListConsentPortals) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ListConsentPortals) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/ListConsentPortals) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/ListConsentPortals) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/ListConsentPortals) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/ListConsentPortals) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ListConsentPortals) 
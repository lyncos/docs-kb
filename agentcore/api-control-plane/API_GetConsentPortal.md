---
title: GetConsentPortal
description: Retrieves information about a consent portal.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetConsentPortal.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# GetConsentPortal
<a name="API_GetConsentPortal"></a>

Retrieves information about a consent portal.

## Request Syntax
<a name="API_GetConsentPortal_RequestSyntax"></a>

```
POST /identities/GetConsentPortal HTTP/1.1
Content-type: application/json

{
   "consentPortalIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetConsentPortal_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetConsentPortal_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [consentPortalIdentifier](#API_GetConsentPortal_RequestSyntax) **   <a name="bedrockagentcorecontrol-GetConsentPortal-request-consentPortalIdentifier"></a>
The identifier of the consent portal. You can specify either the consent portal ID or its Amazon Resource Name (ARN).  
Type: String  
Pattern: `[a-zA-Z0-9\-_]{1,50}-[A-Za-z0-9]{10}`   
Required: Yes

## Response Syntax
<a name="API_GetConsentPortal_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "consentPortalArn": "string",
   "consentPortalId": "string",
   "createdAt": number,
   "description": "string",
   "executionRoleArn": "string",
   "idpConfig": { 
      "audience": "string",
      "credentialProviderArn": "string",
      "scopes": [ "string" ]
   },
   "name": "string",
   "portalUrl": "string",
   "sources": [ 
      { 
         "identifier": "string",
         "type": "string"
      }
   ],
   "status": "string",
   "statusReason": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_GetConsentPortal_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [consentPortalArn](#API_GetConsentPortal_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetConsentPortal-response-consentPortalArn"></a>
The Amazon Resource Name (ARN) of the consent portal.  
Type: String  
Pattern: `arn:aws[^:]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:consent-portal/[a-zA-Z0-9\-_]{1,50}-[A-Za-z0-9]{10}` 

 ** [consentPortalId](#API_GetConsentPortal_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetConsentPortal-response-consentPortalId"></a>
The unique identifier of the consent portal.  
Type: String  
Pattern: `[a-zA-Z0-9\-_]{1,50}-[A-Za-z0-9]{10}` 

 ** [createdAt](#API_GetConsentPortal_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetConsentPortal-response-createdAt"></a>
The timestamp for when the consent portal was created.  
Type: Timestamp

 ** [description](#API_GetConsentPortal_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetConsentPortal-response-description"></a>
The description of the consent portal.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 512.

 ** [executionRoleArn](#API_GetConsentPortal_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetConsentPortal-response-executionRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that the consent portal assumes to access the resources defined in its sources.  
Type: String  
Pattern: `arn:aws(-[a-z-]+)?:iam::[0-9]{12}:role/[a-zA-Z0-9+=,.@\-_/]+` 

 ** [idpConfig](#API_GetConsentPortal_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetConsentPortal-response-idpConfig"></a>
The identity provider configuration that the consent portal uses to authenticate end users.  
Type: [ConsentPortalIdpConfig](API_ConsentPortalIdpConfig.md) object

 ** [name](#API_GetConsentPortal_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetConsentPortal-response-name"></a>
The name of the consent portal.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `[a-zA-Z0-9_-]{1,50}` 

 ** [portalUrl](#API_GetConsentPortal_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetConsentPortal-response-portalUrl"></a>
The URL used to access the consent portal.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.

 ** [sources](#API_GetConsentPortal_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetConsentPortal-response-sources"></a>
The resources served by the consent portal.  
Type: Array of [ConsentPortalSource](API_ConsentPortalSource.md) objects  
Array Members: Fixed number of 1 item.

 ** [status](#API_GetConsentPortal_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetConsentPortal-response-status"></a>
The current status of the consent portal.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | UPDATE_FAILED | DELETING | FAILED` 

 ** [statusReason](#API_GetConsentPortal_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetConsentPortal-response-statusReason"></a>
A message that provides additional information about the current status of the consent portal.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [updatedAt](#API_GetConsentPortal_ResponseSyntax) **   <a name="bedrockagentcorecontrol-GetConsentPortal-response-updatedAt"></a>
The timestamp for when the consent portal was last updated.  
Type: Timestamp

## Errors
<a name="API_GetConsentPortal_Errors"></a>

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

 ** UnauthorizedException **   
This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access  
HTTP Status Code: 401

 ** ValidationException **   
The input fails to satisfy the constraints specified by the service.  
HTTP Status Code: 400

## See Also
<a name="API_GetConsentPortal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-control-2023-06-05/GetConsentPortal) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-control-2023-06-05/GetConsentPortal) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/GetConsentPortal) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-control-2023-06-05/GetConsentPortal) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/GetConsentPortal) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-control-2023-06-05/GetConsentPortal) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-control-2023-06-05/GetConsentPortal) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-control-2023-06-05/GetConsentPortal) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-control-2023-06-05/GetConsentPortal) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/GetConsentPortal) 
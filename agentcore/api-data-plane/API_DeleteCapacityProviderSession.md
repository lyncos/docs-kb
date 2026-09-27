---
title: DeleteCapacityProviderSession
description: Deletes a session associated with a capacity provider in Amazon Bedrock AgentCore and makes the session unavailable for further use. To delete a capacity provider session, specify both the capacity provider identifier and the session ID. After you delete a session, you cannot res
product: Amazon Bedrock AgentCore
section: Data Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_DeleteCapacityProviderSession.html
fetched: '2026-09-26'
tags:
- agentcore
- data-plane-api
---

# DeleteCapacityProviderSession
<a name="API_DeleteCapacityProviderSession"></a>

Deletes a session associated with a capacity provider in Amazon Bedrock AgentCore and makes the session unavailable for further use. To delete a capacity provider session, specify both the capacity provider identifier and the session ID. After you delete a session, you cannot restart it.

## Request Syntax
<a name="API_DeleteCapacityProviderSession_RequestSyntax"></a>

```
DELETE /capacity-providers/{{capacityProviderId}}/sessions/{{sessionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteCapacityProviderSession_RequestParameters"></a>

The request uses the following URI parameters.

 ** [capacityProviderId](#API_DeleteCapacityProviderSession_RequestSyntax) **   <a name="BedrockAgentCore-DeleteCapacityProviderSession-request-uri-capacityProviderId"></a>
The unique identifier of the capacity provider associated with the session.  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** [sessionId](#API_DeleteCapacityProviderSession_RequestSyntax) **   <a name="BedrockAgentCore-DeleteCapacityProviderSession-request-uri-sessionId"></a>
The unique identifier of the capacity provider session to delete.  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: Yes

## Request Body
<a name="API_DeleteCapacityProviderSession_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteCapacityProviderSession_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "capacityProviderArn": "string",
   "sessionId": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DeleteCapacityProviderSession_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [capacityProviderArn](#API_DeleteCapacityProviderSession_ResponseSyntax) **   <a name="BedrockAgentCore-DeleteCapacityProviderSession-response-capacityProviderArn"></a>
The Amazon Resource Name (ARN) of the capacity provider associated with the deleted session.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:capacity-provider/[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}` 

 ** [sessionId](#API_DeleteCapacityProviderSession_ResponseSyntax) **   <a name="BedrockAgentCore-DeleteCapacityProviderSession-response-sessionId"></a>
The unique identifier of the deleted capacity provider session.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*` 

 ** [status](#API_DeleteCapacityProviderSession_ResponseSyntax) **   <a name="BedrockAgentCore-DeleteCapacityProviderSession-response-status"></a>
The current status of the capacity provider session. When the status is `Deleting`, the session is being deleted and is not available. When the status is `Deleted`, the session is no longer available.  
Type: String  
Valid Values: `Provisioning | Deprovisioning | Active | Deleting | Deleted | Stopped` 

## Errors
<a name="API_DeleteCapacityProviderSession_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** InternalServerException **   
The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ThrottlingException **   
The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

## See Also
<a name="API_DeleteCapacityProviderSession_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/DeleteCapacityProviderSession) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/DeleteCapacityProviderSession) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/DeleteCapacityProviderSession) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/DeleteCapacityProviderSession) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/DeleteCapacityProviderSession) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/DeleteCapacityProviderSession) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/DeleteCapacityProviderSession) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/DeleteCapacityProviderSession) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/DeleteCapacityProviderSession) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/DeleteCapacityProviderSession) 
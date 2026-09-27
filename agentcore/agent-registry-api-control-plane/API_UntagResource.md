---
title: UntagResource
description: Removes one or more tags from the specified AWS Agent Registry resource. The operation removes only the tags whose keys you supply; other tags on the resource remain unchanged.
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_UntagResource.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# UntagResource
<a name="API_UntagResource"></a>

Removes one or more tags from the specified AWS Agent Registry resource. The operation removes only the tags whose keys you supply; other tags on the resource remain unchanged.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
DELETE /tags/{{resourceArn+}}?tagKeys={{tagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_UntagResource_RequestSyntax) **   <a name="agentregistrycontrol-UntagResource-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource to remove tags from. Supported resources include registries and registry records.  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Required: Yes

 ** [tagKeys](#API_UntagResource_RequestSyntax) **   <a name="agentregistrycontrol-UntagResource-request-uri-tagKeys"></a>
The keys of the tags to remove from the resource. Tags with keys not included in this list remain on the resource.  
Array Members: Minimum number of 1 item. Maximum number of 50 items.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: Yes

## Request Body
<a name="API_UntagResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_UntagResource_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_UntagResource_Errors"></a>

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

 ** ValidationException **   
The request failed validation of one or more input fields.    
 ** fieldList **   
The list of input fields that failed validation.  
 ** reason **   
The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/UntagResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/UntagResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/UntagResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/UntagResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/UntagResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/UntagResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/UntagResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/UntagResource) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/UntagResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/UntagResource) 
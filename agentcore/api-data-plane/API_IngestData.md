---
title: IngestData
description: Submits content directly for ingestion to generate long-term memory records in a AgentCore Memory resource.
product: Amazon Bedrock AgentCore
section: Data Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_IngestData.html
fetched: '2026-09-26'
tags:
- agentcore
- data-plane-api
---

# IngestData
<a name="API_IngestData"></a>

Submits content directly for ingestion to generate long-term memory records in a AgentCore Memory resource.

To use this operation, you must have the `bedrock-agentcore:IngestData` permission.

## Request Syntax
<a name="API_IngestData_RequestSyntax"></a>

```
POST /memories/{{memoryId}}/ingest HTTP/1.1
Content-type: application/json

{
   "actorId": "{{string}}",
   "clientToken": "{{string}}",
   "contentTimestamp": {{number}},
   "extractionConfig": { 
      "namespaceVariables": { 
         "{{string}}" : "{{string}}" 
      }
   },
   "metadata": { 
      "{{string}}" : { ... }
   },
   "sessionId": "{{string}}",
   "source": { ... }
}
```

## URI Request Parameters
<a name="API_IngestData_RequestParameters"></a>

The request uses the following URI parameters.

 ** [memoryId](#API_IngestData_RequestSyntax) **   <a name="BedrockAgentCore-IngestData-request-uri-memoryId"></a>
The identifier of the AgentCore Memory resource to ingest content into.  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

## Request Body
<a name="API_IngestData_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [actorId](#API_IngestData_RequestSyntax) **   <a name="BedrockAgentCore-IngestData-request-actorId"></a>
The identifier of the actor associated with this content. An actor represents an entity that participates in sessions and generates content.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_/]*(?::[a-zA-Z0-9-_/]+)*[a-zA-Z0-9-_/]*`   
Required: Yes

 ** [clientToken](#API_IngestData_RequestSyntax) **   <a name="BedrockAgentCore-IngestData-request-clientToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, AgentCore ignores the request, but does not return an error.  
Type: String  
Required: No

 ** [contentTimestamp](#API_IngestData_RequestSyntax) **   <a name="BedrockAgentCore-IngestData-request-contentTimestamp"></a>
The timestamp of when the content occurred.  
Type: Timestamp  
Required: Yes

 ** [extractionConfig](#API_IngestData_RequestSyntax) **   <a name="BedrockAgentCore-IngestData-request-extractionConfig"></a>
The extraction configuration for long-term memory records. Use this parameter to specify namespace variable keys and their values for namespace substitution during extraction.  
Type: [ExtractionConfig](API_ExtractionConfig.md) object  
Required: No

 ** [metadata](#API_IngestData_RequestSyntax) **   <a name="BedrockAgentCore-IngestData-request-metadata"></a>
The key-value metadata to attach to the content.  
Type: String to [MetadataValue](API_MetadataValue.md) object map  
Map Entries: Minimum number of 0 items. Maximum number of 15 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

 ** [sessionId](#API_IngestData_RequestSyntax) **   <a name="BedrockAgentCore-IngestData-request-sessionId"></a>
The identifier of the session that the content belongs to. If not provided, a session identifier is generated and returned in the response.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: No

 ** [source](#API_IngestData_RequestSyntax) **   <a name="BedrockAgentCore-IngestData-request-source"></a>
The content to ingest. Only inline content is supported.  
Type: [ContentSource](API_ContentSource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## Response Syntax
<a name="API_IngestData_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "sessionId": "string"
}
```

## Response Elements
<a name="API_IngestData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [sessionId](#API_IngestData_ResponseSyntax) **   <a name="BedrockAgentCore-IngestData-response-sessionId"></a>
The identifier of the session that the service ingested the content into. This value echoes the session identifier from the request, or the identifier that the service generated when you did not provide one.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*` 

## Errors
<a name="API_IngestData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.  
HTTP Status Code: 403

 ** ResourceNotFoundException **   
The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.  
HTTP Status Code: 404

 ** ServiceException **   
The service encountered an internal error. Try your request again later.  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.  
HTTP Status Code: 402

 ** ThrottledException **   
The request was denied due to request throttling. Reduce the frequency of requests and try again.  
HTTP Status Code: 429

 ** ValidationException **   
The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.  
HTTP Status Code: 400

## See Also
<a name="API_IngestData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-agentcore-2024-02-28/IngestData) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-agentcore-2024-02-28/IngestData) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/IngestData) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-agentcore-2024-02-28/IngestData) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/IngestData) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-agentcore-2024-02-28/IngestData) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-agentcore-2024-02-28/IngestData) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-agentcore-2024-02-28/IngestData) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/bedrock-agentcore-2024-02-28/IngestData) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/IngestData) 
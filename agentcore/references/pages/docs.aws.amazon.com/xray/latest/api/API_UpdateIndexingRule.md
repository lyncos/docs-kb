---
title: UpdateIndexingRule
description: Modifies an indexing rule’s configuration.
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/xray/latest/api/API_UpdateIndexingRule.html
fetched: '2026-09-26'
tags:
- agentcore
- docs-aws-amazon-com
- reference
- related
referenced_by:
- observability-configure.md
conversion: native-md
---

# UpdateIndexingRule
<a name="API_UpdateIndexingRule"></a>

 Modifies an indexing rule’s configuration. 

Indexing rules are used for determining the sampling rate for spans indexed from CloudWatch Logs. For more information, see [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html).

## Request Syntax
<a name="API_UpdateIndexingRule_RequestSyntax"></a>

```
POST /UpdateIndexingRule HTTP/1.1
Content-type: application/json

{
   "Name": "{{string}}",
   "Rule": { ... }
}
```

## URI Request Parameters
<a name="API_UpdateIndexingRule_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateIndexingRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_UpdateIndexingRule_RequestSyntax) **   <a name="xray-UpdateIndexingRule-request-Name"></a>
 Name of the indexing rule to be updated.   
Type: String  
Required: Yes

 ** [Rule](#API_UpdateIndexingRule_RequestSyntax) **   <a name="xray-UpdateIndexingRule-request-Rule"></a>
 Rule configuration to be updated.   
Type: [IndexingRuleValueUpdate](API_IndexingRuleValueUpdate.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## Response Syntax
<a name="API_UpdateIndexingRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "IndexingRule": { 
      "ModifiedAt": number,
      "Name": "string",
      "Rule": { ... }
   }
}
```

## Response Elements
<a name="API_UpdateIndexingRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IndexingRule](#API_UpdateIndexingRule_ResponseSyntax) **   <a name="xray-UpdateIndexingRule-response-IndexingRule"></a>
 Updated indexing rule.   
Type: [IndexingRule](API_IndexingRule.md) object

## Errors
<a name="API_UpdateIndexingRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **   
The request is missing required parameters or has invalid parameters.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
The resource was not found. Verify that the name or Amazon Resource Name (ARN) of the resource is correct.  
HTTP Status Code: 404

 ** ThrottledException **   
The request exceeds the maximum number of requests per second.  
HTTP Status Code: 429

## See Also
<a name="API_UpdateIndexingRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/UpdateIndexingRule) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/UpdateIndexingRule) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/UpdateIndexingRule) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/UpdateIndexingRule) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/UpdateIndexingRule) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/UpdateIndexingRule) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/UpdateIndexingRule) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/UpdateIndexingRule) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/UpdateIndexingRule) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/UpdateIndexingRule)

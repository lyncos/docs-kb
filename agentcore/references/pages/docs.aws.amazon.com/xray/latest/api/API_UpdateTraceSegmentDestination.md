---
title: UpdateTraceSegmentDestination
description: Modifies the destination of data sent to `PutTraceSegments`. The Transaction Search feature requires the CloudWatchLogs destination. For more information, see Transaction Search.
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/xray/latest/api/API_UpdateTraceSegmentDestination.html
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

# UpdateTraceSegmentDestination
<a name="API_UpdateTraceSegmentDestination"></a>

 Modifies the destination of data sent to `PutTraceSegments`. The Transaction Search feature requires the CloudWatchLogs destination. For more information, see [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html). 

## Request Syntax
<a name="API_UpdateTraceSegmentDestination_RequestSyntax"></a>

```
POST /UpdateTraceSegmentDestination HTTP/1.1
Content-type: application/json

{
   "Destination": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateTraceSegmentDestination_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateTraceSegmentDestination_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Destination](#API_UpdateTraceSegmentDestination_RequestSyntax) **   <a name="xray-UpdateTraceSegmentDestination-request-Destination"></a>
 The configured destination of trace segments.   
Type: String  
Valid Values: `XRay | CloudWatchLogs`   
Required: No

## Response Syntax
<a name="API_UpdateTraceSegmentDestination_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Destination": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_UpdateTraceSegmentDestination_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Destination](#API_UpdateTraceSegmentDestination_ResponseSyntax) **   <a name="xray-UpdateTraceSegmentDestination-response-Destination"></a>
 The destination of the trace segments.   
Type: String  
Valid Values: `XRay | CloudWatchLogs` 

 ** [Status](#API_UpdateTraceSegmentDestination_ResponseSyntax) **   <a name="xray-UpdateTraceSegmentDestination-response-Status"></a>
 The status of the update.   
Type: String  
Valid Values: `PENDING | ACTIVE` 

## Errors
<a name="API_UpdateTraceSegmentDestination_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **   
The request is missing required parameters or has invalid parameters.  
HTTP Status Code: 400

 ** ThrottledException **   
The request exceeds the maximum number of requests per second.  
HTTP Status Code: 429

## See Also
<a name="API_UpdateTraceSegmentDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/UpdateTraceSegmentDestination) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/UpdateTraceSegmentDestination) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/UpdateTraceSegmentDestination) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/UpdateTraceSegmentDestination) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/UpdateTraceSegmentDestination) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/UpdateTraceSegmentDestination) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/UpdateTraceSegmentDestination) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/UpdateTraceSegmentDestination) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/UpdateTraceSegmentDestination) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/UpdateTraceSegmentDestination)

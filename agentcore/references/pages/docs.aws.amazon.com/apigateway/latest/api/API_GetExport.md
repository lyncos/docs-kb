---
title: GetExport
description: Exports a deployed version of a RestApi in a specified format.
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_GetExport.html
fetched: '2026-09-26'
tags:
- agentcore
- docs-aws-amazon-com
- reference
- related
referenced_by:
- gateway-target-api-gateway.md
conversion: native-md
---

# GetExport
<a name="API_GetExport"></a>

Exports a deployed version of a RestApi in a specified format.

## Request Syntax
<a name="API_GetExport_RequestSyntax"></a>

```
GET /restapis/{{restapi_id}}/stages/{{stage_name}}/exports/{{export_type}}?{{parameters}} HTTP/1.1
Accept: {{accepts}}
```

## URI Request Parameters
<a name="API_GetExport_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accepts](#API_GetExport_RequestSyntax) **   <a name="apigw-GetExport-request-accepts"></a>
The content-type of the export, for example `application/json`. Currently `application/json` and `application/yaml` are supported for `exportType` of`oas30` and `swagger`. This should be specified in the `Accept` header for direct API requests.

 ** [export\_type](#API_GetExport_RequestSyntax) **   <a name="apigw-GetExport-request-uri-exportType"></a>
The type of export. Acceptable values are 'oas30' for OpenAPI 3.0.x and 'swagger' for Swagger/OpenAPI 2.0.  
Required: Yes

 ** [parameters](#API_GetExport_RequestSyntax) **   <a name="apigw-GetExport-request-uri-parameters"></a>
A key-value map of query string parameters that specify properties of the export, depending on the requested `exportType`. For `exportType` `oas30` and `swagger`, any combination of the following parameters are supported: `extensions='integrations'` or `extensions='apigateway'` will export the API with x-amazon-apigateway-integration extensions. `extensions='authorizers'` will export the API with x-amazon-apigateway-authorizer extensions. `postman` will export the API with Postman extensions, allowing for import to the Postman tool

 ** [restapi\_id](#API_GetExport_RequestSyntax) **   <a name="apigw-GetExport-request-uri-restApiId"></a>
The string identifier of the associated RestApi.  
Required: Yes

 ** [stage\_name](#API_GetExport_RequestSyntax) **   <a name="apigw-GetExport-request-uri-stageName"></a>
The name of the Stage that will be exported.  
Required: Yes

## Request Body
<a name="API_GetExport_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetExport_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-Type: {{contentType}}
Content-Disposition: {{contentDisposition}}

{{body}}
```

## Response Elements
<a name="API_GetExport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [contentDisposition](#API_GetExport_ResponseSyntax) **   <a name="apigw-GetExport-response-contentDisposition"></a>
The content-disposition header value in the HTTP response.

 ** [contentType](#API_GetExport_ResponseSyntax) **   <a name="apigw-GetExport-response-contentType"></a>
The content-type header value in the HTTP response. This will correspond to a valid 'accept' type in the request.

The response returns the following as the HTTP body.

 ** [body](#API_GetExport_ResponseSyntax) **   <a name="apigw-GetExport-response-body"></a>
The binary blob response to GetExport, which contains the export.

## Errors
<a name="API_GetExport_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.  
HTTP Status Code: 400

 ** ConflictException **   
The request configuration has conflicts. For details, see the accompanying error message.  
HTTP Status Code: 409

 ** LimitExceededException **   
The request exceeded the rate limit. Retry after the specified time period.  
HTTP Status Code: 429

 ** NotFoundException **   
The requested resource is not found. Make sure that the request URI is correct.  
HTTP Status Code: 404

 ** TooManyRequestsException **   
The request has reached its throttling limit. Retry after the specified time period.  
HTTP Status Code: 429

 ** UnauthorizedException **   
The request is denied because the caller has insufficient permissions.  
HTTP Status Code: 401

## See Also
<a name="API_GetExport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/GetExport) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/GetExport) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/GetExport) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/GetExport) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/GetExport) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/GetExport) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/GetExport) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/GetExport) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/GetExport) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/GetExport)

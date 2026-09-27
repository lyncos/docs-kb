---
title: UpdateMethod
description: Updates an existing Method resource.
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_UpdateMethod.html
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

# UpdateMethod
<a name="API_UpdateMethod"></a>

Updates an existing Method resource.

## Request Syntax
<a name="API_UpdateMethod_RequestSyntax"></a>

```
PATCH /restapis/{{restapi_id}}/resources/{{resource_id}}/methods/{{http_method}} HTTP/1.1
Content-type: application/json

{
   "patchOperations": [ 
      { 
         "from": "{{string}}",
         "op": "{{string}}",
         "path": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateMethod_RequestParameters"></a>

The request uses the following URI parameters.

 ** [http\_method](#API_UpdateMethod_RequestSyntax) **   <a name="apigw-UpdateMethod-request-uri-httpMethod"></a>
The HTTP verb of the Method resource.  
Required: Yes

 ** [resource\_id](#API_UpdateMethod_RequestSyntax) **   <a name="apigw-UpdateMethod-request-uri-resourceId"></a>
The Resource identifier for the Method resource.  
Required: Yes

 ** [restapi\_id](#API_UpdateMethod_RequestSyntax) **   <a name="apigw-UpdateMethod-request-uri-restApiId"></a>
The string identifier of the associated RestApi.  
Required: Yes

## Request Body
<a name="API_UpdateMethod_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [patchOperations](#API_UpdateMethod_RequestSyntax) **   <a name="apigw-UpdateMethod-request-patchOperations"></a>
For more information about supported patch operations, see [Patch Operations](patch-operations.md).  
Type: Array of [PatchOperation](API_PatchOperation.md) objects  
Required: No

## Response Syntax
<a name="API_UpdateMethod_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "apiKeyRequired": boolean,
   "authorizationScopes": [ "string" ],
   "authorizationType": "string",
   "authorizerId": "string",
   "httpMethod": "string",
   "methodIntegration": { 
      "cacheKeyParameters": [ "string" ],
      "cacheNamespace": "string",
      "connectionId": "string",
      "connectionType": "string",
      "contentHandling": "string",
      "credentials": "string",
      "httpMethod": "string",
      "integrationResponses": { 
         "string" : { 
            "contentHandling": "string",
            "responseParameters": { 
               "string" : "string" 
            },
            "responseTemplates": { 
               "string" : "string" 
            },
            "selectionPattern": "string",
            "statusCode": "string"
         }
      },
      "integrationTarget": "string",
      "passthroughBehavior": "string",
      "requestParameters": { 
         "string" : "string" 
      },
      "requestTemplates": { 
         "string" : "string" 
      },
      "responseTransferMode": "string",
      "timeoutInMillis": number,
      "tlsConfig": { 
         "insecureSkipVerification": boolean
      },
      "type": "string",
      "uri": "string"
   },
   "methodResponses": { 
      "string" : { 
         "responseModels": { 
            "string" : "string" 
         },
         "responseParameters": { 
            "string" : boolean 
         },
         "statusCode": "string"
      }
   },
   "operationName": "string",
   "requestModels": { 
      "string" : "string" 
   },
   "requestParameters": { 
      "string" : boolean 
   },
   "requestValidatorId": "string"
}
```

## Response Elements
<a name="API_UpdateMethod_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [apiKeyRequired](#API_UpdateMethod_ResponseSyntax) **   <a name="apigw-UpdateMethod-response-apiKeyRequired"></a>
A boolean flag specifying whether a valid ApiKey is required to invoke this method.  
Type: Boolean

 ** [authorizationScopes](#API_UpdateMethod_ResponseSyntax) **   <a name="apigw-UpdateMethod-response-authorizationScopes"></a>
A list of authorization scopes configured on the method. The scopes are used with a `COGNITO_USER_POOLS` authorizer to authorize the method invocation. The authorization works by matching the method scopes against the scopes parsed from the access token in the incoming request. The method invocation is authorized if any method scopes matches a claimed scope in the access token. Otherwise, the invocation is not authorized. When the method scope is configured, the client must provide an access token instead of an identity token for authorization purposes.  
Type: Array of strings

 ** [authorizationType](#API_UpdateMethod_ResponseSyntax) **   <a name="apigw-UpdateMethod-response-authorizationType"></a>
The method's authorization type. Valid values are `NONE` for open access, `AWS_IAM` for using AWS IAM permissions, `CUSTOM` for using a custom authorizer, or `COGNITO_USER_POOLS` for using a Cognito user pool.  
Type: String

 ** [authorizerId](#API_UpdateMethod_ResponseSyntax) **   <a name="apigw-UpdateMethod-response-authorizerId"></a>
The identifier of an authorizer to use on this method. The method's authorization type must be `CUSTOM` or `COGNITO_USER_POOLS`.  
Type: String

 ** [httpMethod](#API_UpdateMethod_ResponseSyntax) **   <a name="apigw-UpdateMethod-response-httpMethod"></a>
The method's HTTP verb.  
Type: String

 ** [methodIntegration](#API_UpdateMethod_ResponseSyntax) **   <a name="apigw-UpdateMethod-response-methodIntegration"></a>
Gets the method's integration responsible for passing the client-submitted request to the back end and performing necessary transformations to make the request compliant with the back end.  
Type: [Integration](API_Integration.md) object

 ** [methodResponses](#API_UpdateMethod_ResponseSyntax) **   <a name="apigw-UpdateMethod-response-methodResponses"></a>
Gets a method response associated with a given HTTP status code.   
Type: String to [MethodResponse](API_MethodResponse.md) object map

 ** [operationName](#API_UpdateMethod_ResponseSyntax) **   <a name="apigw-UpdateMethod-response-operationName"></a>
A human-friendly operation identifier for the method. For example, you can assign the `operationName` of `ListPets` for the `GET /pets` method in the `PetStore` example.  
Type: String

 ** [requestModels](#API_UpdateMethod_ResponseSyntax) **   <a name="apigw-UpdateMethod-response-requestModels"></a>
A key-value map specifying data schemas, represented by Model resources, (as the mapped value) of the request payloads of given content types (as the mapping key).  
Type: String to string map

 ** [requestParameters](#API_UpdateMethod_ResponseSyntax) **   <a name="apigw-UpdateMethod-response-requestParameters"></a>
A key-value map defining required or optional method request parameters that can be accepted by API Gateway. A key is a method request parameter name matching the pattern of `method.request.{location}.{name}`, where `location` is `querystring`, `path`, or `header` and `name` is a valid and unique parameter name. The value associated with the key is a Boolean flag indicating whether the parameter is required (`true`) or optional (`false`). The method request parameter names defined here are available in Integration to be mapped to integration request parameters or templates.  
Type: String to boolean map

 ** [requestValidatorId](#API_UpdateMethod_ResponseSyntax) **   <a name="apigw-UpdateMethod-response-requestValidatorId"></a>
The identifier of a RequestValidator for request validation.  
Type: String

## Errors
<a name="API_UpdateMethod_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
The submitted request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.  
HTTP Status Code: 400

 ** ConflictException **   
The request configuration has conflicts. For details, see the accompanying error message.  
HTTP Status Code: 409

 ** NotFoundException **   
The requested resource is not found. Make sure that the request URI is correct.  
HTTP Status Code: 404

 ** TooManyRequestsException **   
The request has reached its throttling limit. Retry after the specified time period.  
HTTP Status Code: 429

 ** UnauthorizedException **   
The request is denied because the caller has insufficient permissions.  
HTTP Status Code: 401

## Examples
<a name="API_UpdateMethod_Examples"></a>

### Update a method to require use of an API key
<a name="API_UpdateMethod_Example_1"></a>

This example illustrates one usage of UpdateMethod.

#### Sample Request
<a name="API_UpdateMethod_Example_1_Request"></a>

```
PATCH /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160602T185328Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160602/us-east-1/apigateway/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature={sig4_hash}
Cache-Control: no-cache

{
  "patchOperations" : [ {
    "op" : "replace",
    "path" : "/apiKeyRequired",
    "value" : "true"
  } ]
```

#### Sample Response
<a name="API_UpdateMethod_Example_1_Response"></a>

```
{
  "_links": {
    "curies": [
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html",
        "name": "integration",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-{rel}.html",
        "name": "method",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html",
        "name": "methodresponse",
        "templated": true
      }
    ],
    "self": {
      "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET",
      "name": "GET",
      "title": "GET"
    },
    "integration:put": {
      "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration"
    },
    "method:delete": {
      "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET"
    },
    "method:update": {
      "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET"
    },
    "methodresponse:put": {
      "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/{status_code}",
      "templated": true
    }
  },
  "apiKeyRequired": true,
  "authorizationType": "NONE",
  "httpMethod": "GET"
}
```

## See Also
<a name="API_UpdateMethod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/UpdateMethod) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/UpdateMethod) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/UpdateMethod) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/UpdateMethod) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/UpdateMethod) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/UpdateMethod) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/UpdateMethod) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/UpdateMethod) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/UpdateMethod) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/UpdateMethod)

---
title: PutRestApi
description: A feature of the API Gateway control service for updating an existing API with an input of external API definitions. The update can take the form of merging the supplied definition into the existing API or overwriting the existing API.
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_PutRestApi.html
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

# PutRestApi
<a name="API_PutRestApi"></a>

A feature of the API Gateway control service for updating an existing API with an input of external API definitions. The update can take the form of merging the supplied definition into the existing API or overwriting the existing API.

## Request Syntax
<a name="API_PutRestApi_RequestSyntax"></a>

```
PUT /restapis/{{restapi_id}}?{{parameters}}&failonwarnings={{failOnWarnings}}&mode={{mode}} HTTP/1.1

{{body}}
```

## URI Request Parameters
<a name="API_PutRestApi_RequestParameters"></a>

The request uses the following URI parameters.

 ** [failOnWarnings](#API_PutRestApi_RequestSyntax) **   <a name="apigw-PutRestApi-request-uri-failOnWarnings"></a>
A query parameter to indicate whether to rollback the API update (`true`) or not (`false`) when a warning is encountered. The default value is `false`.

 ** [mode](#API_PutRestApi_RequestSyntax) **   <a name="apigw-PutRestApi-request-uri-mode"></a>
The `mode` query parameter to specify the update mode. Valid values are "merge" and "overwrite". By default, the update mode is "merge".  
When you use `overwrite` mode, the entire API definition is replaced. Any API configurations not explicitly included in the import body are reset to their default values. To preserve existing configurations, use `merge` mode, or ensure that your OpenAPI definition includes all desired API configuration settings, such as API Gateway extensions.
Valid Values: `merge | overwrite` 

 ** [parameters](#API_PutRestApi_RequestSyntax) **   <a name="apigw-PutRestApi-request-uri-parameters"></a>
Custom header parameters as part of the request. For example, to exclude DocumentationParts from an imported API, set `ignore=documentation` as a `parameters` value, as in the AWS CLI command of `aws apigateway import-rest-api --parameters ignore=documentation --body 'file:///path/to/imported-api-body.json'`.

 ** [restapi\_id](#API_PutRestApi_RequestSyntax) **   <a name="apigw-PutRestApi-request-uri-restApiId"></a>
The string identifier of the associated RestApi.  
Required: Yes

## Request Body
<a name="API_PutRestApi_RequestBody"></a>

The request accepts the following binary data.

 ** [body](#API_PutRestApi_RequestSyntax) **   <a name="apigw-PutRestApi-request-body"></a>
The PUT request body containing external API definitions. Currently, only OpenAPI definition JSON/YAML files are supported. The maximum size of the API definition file is 6MB.  
Required: Yes

## Response Syntax
<a name="API_PutRestApi_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "apiKeySource": "string",
   "apiStatus": "string",
   "apiStatusMessage": "string",
   "binaryMediaTypes": [ "string" ],
   "createdDate": number,
   "description": "string",
   "disableExecuteApiEndpoint": boolean,
   "endpointAccessMode": "string",
   "endpointConfiguration": { 
      "ipAddressType": "string",
      "types": [ "string" ],
      "vpcEndpointIds": [ "string" ]
   },
   "id": "string",
   "minimumCompressionSize": number,
   "name": "string",
   "policy": "string",
   "rootResourceId": "string",
   "securityPolicy": "string",
   "tags": { 
      "string" : "string" 
   },
   "version": "string",
   "warnings": [ "string" ]
}
```

## Response Elements
<a name="API_PutRestApi_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [apiKeySource](#API_PutRestApi_ResponseSyntax) **   <a name="apigw-PutRestApi-response-apiKeySource"></a>
The source of the API key for metering requests according to a usage plan. Valid values are: >`HEADER` to read the API key from the `X-API-Key` header of a request. `AUTHORIZER` to read the API key from the `UsageIdentifierKey` from a custom authorizer.  
Type: String  
Valid Values: `HEADER | AUTHORIZER` 

 ** [apiStatus](#API_PutRestApi_ResponseSyntax) **   <a name="apigw-PutRestApi-response-apiStatus"></a>
The ApiStatus of the RestApi.   
Type: String  
Valid Values: `UPDATING | AVAILABLE | PENDING | FAILED` 

 ** [apiStatusMessage](#API_PutRestApi_ResponseSyntax) **   <a name="apigw-PutRestApi-response-apiStatusMessage"></a>
 The status message of the RestApi. When the status message is `UPDATING` you can still invoke it.   
Type: String

 ** [binaryMediaTypes](#API_PutRestApi_ResponseSyntax) **   <a name="apigw-PutRestApi-response-binaryMediaTypes"></a>
The list of binary media types supported by the RestApi. By default, the RestApi supports only UTF-8-encoded text payloads.  
Type: Array of strings

 ** [createdDate](#API_PutRestApi_ResponseSyntax) **   <a name="apigw-PutRestApi-response-createdDate"></a>
The timestamp when the API was created.  
Type: Timestamp

 ** [description](#API_PutRestApi_ResponseSyntax) **   <a name="apigw-PutRestApi-response-description"></a>
The API's description.  
Type: String

 ** [disableExecuteApiEndpoint](#API_PutRestApi_ResponseSyntax) **   <a name="apigw-PutRestApi-response-disableExecuteApiEndpoint"></a>
Specifies whether clients can invoke your API by using the default `execute-api` endpoint. By default, clients can invoke your API with the default `https://{api_id}.execute-api.{region}.amazonaws.com` endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint.  
Type: Boolean

 ** [endpointAccessMode](#API_PutRestApi_ResponseSyntax) **   <a name="apigw-PutRestApi-response-endpointAccessMode"></a>
 The endpoint access mode of the RestApi.   
Type: String  
Valid Values: `BASIC | STRICT` 

 ** [endpointConfiguration](#API_PutRestApi_ResponseSyntax) **   <a name="apigw-PutRestApi-response-endpointConfiguration"></a>
The endpoint configuration of this RestApi showing the endpoint types and IP address types of the API.   
Type: [EndpointConfiguration](API_EndpointConfiguration.md) object

 ** [id](#API_PutRestApi_ResponseSyntax) **   <a name="apigw-PutRestApi-response-id"></a>
The API's identifier. This identifier is unique across all of your APIs in API Gateway.  
Type: String

 ** [minimumCompressionSize](#API_PutRestApi_ResponseSyntax) **   <a name="apigw-PutRestApi-response-minimumCompressionSize"></a>
A nullable integer that is used to enable compression (with non-negative between 0 and 10485760 (10M) bytes, inclusive) or disable compression (with a null value) on an API. When compression is enabled, compression or decompression is not applied on the payload if the payload size is smaller than this value. Setting it to zero allows compression for any payload size.  
Type: Integer

 ** [name](#API_PutRestApi_ResponseSyntax) **   <a name="apigw-PutRestApi-response-name"></a>
The API's name.  
Type: String

 ** [policy](#API_PutRestApi_ResponseSyntax) **   <a name="apigw-PutRestApi-response-policy"></a>
A stringified JSON policy document that applies to this RestApi regardless of the caller and Method configuration.  
Type: String

 ** [rootResourceId](#API_PutRestApi_ResponseSyntax) **   <a name="apigw-PutRestApi-response-rootResourceId"></a>
The API's root resource ID.  
Type: String

 ** [securityPolicy](#API_PutRestApi_ResponseSyntax) **   <a name="apigw-PutRestApi-response-securityPolicy"></a>
 The Transport Layer Security (TLS) version \+ cipher suite for this RestApi.   
Type: String  
Valid Values: `TLS_1_0 | TLS_1_2 | SecurityPolicy_TLS13_1_3_2025_09 | SecurityPolicy_TLS13_1_3_FIPS_2025_09 | SecurityPolicy_TLS13_1_2_PFS_PQ_2025_09 | SecurityPolicy_TLS13_1_2_FIPS_PQ_2025_09 | SecurityPolicy_TLS13_1_2_PQ_2025_09 | SecurityPolicy_TLS13_1_2_2021_06 | SecurityPolicy_TLS13_2025_EDGE | SecurityPolicy_TLS12_PFS_2025_EDGE | SecurityPolicy_TLS12_2018_EDGE` 

 ** [tags](#API_PutRestApi_ResponseSyntax) **   <a name="apigw-PutRestApi-response-tags"></a>
The collection of tags. Each tag element is associated with a given resource.  
Type: String to string map

 ** [version](#API_PutRestApi_ResponseSyntax) **   <a name="apigw-PutRestApi-response-version"></a>
A version identifier for the API.  
Type: String

 ** [warnings](#API_PutRestApi_ResponseSyntax) **   <a name="apigw-PutRestApi-response-warnings"></a>
The warning messages reported when `failonwarnings` is turned on during API import.  
Type: Array of strings

## Errors
<a name="API_PutRestApi_Errors"></a>

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

 ** TooManyRequestsException **   
The request has reached its throttling limit. Retry after the specified time period.  
HTTP Status Code: 429

 ** UnauthorizedException **   
The request is denied because the caller has insufficient permissions.  
HTTP Status Code: 401

## Examples
<a name="API_PutRestApi_Examples"></a>

### Merge a supplied OpenAPI API definition with an existing API
<a name="API_PutRestApi_Example_1"></a>

This example illustrates one usage of PutRestApi.

#### Sample Request
<a name="API_PutRestApi_Example_1_Request"></a>

```
PUT /restapis/wn611yeyp3?mode=merge HTTP/1.1
Content-Type: application/json
Host: apigateway.us-east-1.amazonaws.com
X-Amz-Date: 20160607T154932Z
Authorization: AWS4-HMAC-SHA256 Credential={access_key_ID}/20160607/us-east-1/apigateway/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature={sig4_hash}

{
  "swagger": "2.0",
  "info": {
    "version": "2016-06-07T15:48:21Z",
    "title": "HelloWorld"
  },
  "host": "vys2gggws7.execute-api.us-east-1.amazonaws.com",
  "basepath": "/test",
  "schemes": [
    "https"
  ],
  "paths": {
    "/gello": {
      "get": {
        "consumes": [
          "application/json"
        ],
        "produces": [
          "application/json"
        ],
        "responses": {
          "200": {
            "description": "200 response",
            "schema": {
              "$ref": "#/definitions/Empty"
            }
          }
        },
        "x-amazon-apigateway-integration": {
          "responses": {
            "default": {
              "statusCode": "200"
            }
          },
          "requestTemplates": {
            "application/json": "{}"
          },
          "uri": "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:123456789012:function:GetHelloWorld/invocations",
          "passthroughBehavior": "when_no_match",
          "httpMethod": "POST",
          "type": "aws"
        }
      },
      "post": {
        "produces": [
          "application/json"
        ],
        "responses": {
          "200": {
            "description": "200 response",
            "schema": {
              "$ref": "#/definitions/Empty"
            }
          }
        },
        "x-amazon-apigateway-integration": {
          "responses": {
            "default": {
              "statusCode": "200"
            }
          },
          "uri": "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:123456789012:function:GetHelloWorldName/invocations",
          "passthroughBehavior": "when_no_match",
          "httpMethod": "POST",
          "type": "aws"
        }
      }
    },
    "/hello": {
      "get": {
        "produces": [
          "application/json"
        ],
        "responses": {
          "200": {
            "description": "200 response",
            "schema": {
              "$ref": "#/definitions/Empty"
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "type": "string"
              }
            }
          }
        },
        "x-amazon-apigateway-integration": {
          "responses": {
            "default": {
              "statusCode": "200",
              "responseParameters": {
                "method.response.header.Access-Control-Allow-Origin": "'*'"
              }
            }
          },
          "uri": "https://example.com",
          "passthroughBehavior": "when_no_match",
          "httpMethod": "GET",
          "type": "http"
        }
      },
      "options": {
        "consumes": [
          "application/json"
        ],
        "produces": [
          "application/json"
        ],
        "responses": {
          "200": {
            "description": "200 response",
            "schema": {
              "$ref": "#/definitions/Empty"
            },
            "headers": {
              "Access-Control-Allow-Origin": {
                "type": "string"
              },
              "Access-Control-Allow-Methods": {
                "type": "string"
              },
              "Access-Control-Allow-Headers": {
                "type": "string"
              }
            }
          }
        },
        "x-amazon-apigateway-integration": {
          "responses": {
            "default": {
              "statusCode": "200",
              "responseParameters": {
                "method.response.header.Access-Control-Allow-Methods": "'GET,OPTIONS'",
                "method.response.header.Access-Control-Allow-Headers": "'Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token'",
                "method.response.header.Access-Control-Allow-Origin": "'*'"
              }
            }
          },
          "requestTemplates": {
            "application/json": "{\"statusCode\": 200}"
          },
          "passthroughBehavior": "when_no_match",
          "type": "mock"
        }
      }
    }
  },
  "definitions": {
    "Empty": {
      "type": "object"
    }
  }
}
```

#### Sample Response
<a name="API_PutRestApi_Example_1_Response"></a>

```
{
  "_links": {
    "curies": [
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-authorizer-{rel}.html",
        "name": "authorizer",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-deployment-{rel}.html",
        "name": "deployment",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-model-{rel}.html",
        "name": "model",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-resource-{rel}.html",
        "name": "resource",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-restapi-{rel}.html",
        "name": "restapi",
        "templated": true
      },
      {
        "href": "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-stage-{rel}.html",
        "name": "stage",
        "templated": true
      }
    ],
    "self": {
      "href": "/restapis/wn611yeyp3"
    },
    "authorizer:by-id": {
      "href": "/restapis/wn611yeyp3/authorizers/{authorizer_id}",
      "templated": true
    },
    "authorizer:create": {
      "href": "/restapis/wn611yeyp3/authorizers"
    },
    "deployment:by-id": {
      "href": "/restapis/wn611yeyp3/deployments/{deployment_id}{?embed}",
      "templated": true
    },
    "deployment:create": {
      "href": "/restapis/wn611yeyp3/deployments"
    },
    "model:by-name": {
      "href": "/restapis/wn611yeyp3/models/{model_name}?flatten=false",
      "templated": true
    },
    "model:create": {
      "href": "/restapis/wn611yeyp3/models"
    },
    "resource:by-id": {
      "href": "/restapis/wn611yeyp3/resources/{resource_id}{?embed}",
      "templated": true
    },
    "resource:create": {
      "href": "/restapis/wn611yeyp3/resources/s3dmsjgijc"
    },
    "restapi:authorizers": {
      "href": "/restapis/wn611yeyp3/authorizers"
    },
    "restapi:delete": {
      "href": "/restapis/wn611yeyp3"
    },
    "restapi:deployments": {
      "href": "/restapis/wn611yeyp3/deployments{?limit}",
      "templated": true
    },
    "restapi:models": {
      "href": "/restapis/wn611yeyp3/models"
    },
    "restapi:resources": {
      "href": "/restapis/wn611yeyp3/resources{?limit,embed}",
      "templated": true
    },
    "restapi:stages": {
      "href": "/restapis/wn611yeyp3/stages{?deployment_id}",
      "templated": true
    },
    "restapi:update": {
      "href": "/restapis/wn611yeyp3"
    },
    "stage:by-name": {
      "href": "/restapis/wn611yeyp3/stages/{stage_name}",
      "templated": true
    },
    "stage:create": {
      "href": "/restapis/wn611yeyp3/stages"
    }
  },
  "createdDate": "2016-06-06T23:49:37Z",
  "id": "wn611yeyp3",
  "name": "HelloWorld"
}
```

## See Also
<a name="API_PutRestApi_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/apigateway-2015-07-09/PutRestApi) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/apigateway-2015-07-09/PutRestApi) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/PutRestApi) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/apigateway-2015-07-09/PutRestApi) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/PutRestApi) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/apigateway-2015-07-09/PutRestApi) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/apigateway-2015-07-09/PutRestApi) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/apigateway-2015-07-09/PutRestApi) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/apigateway-2015-07-09/PutRestApi) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/PutRestApi)

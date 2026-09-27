---
title: Method
description: 'Represents a client-facing interface by which the client calls the API to access back-end resources. A Method resource is integrated with an Integration resource. Both consist of a request and one or more responses. The method request takes the client input that is passed to the '
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/apigateway/latest/api/API_Method.html
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

# Method
<a name="API_Method"></a>

 Represents a client-facing interface by which the client calls the API to access back-end resources. A Method resource is integrated with an Integration resource. Both consist of a request and one or more responses. The method request takes the client input that is passed to the back end through the integration request. A method response returns the output from the back end to the client through an integration response. A method request is embodied in a Method resource, whereas an integration request is embodied in an Integration resource. On the other hand, a method response is represented by a MethodResponse resource, whereas an integration response is represented by an IntegrationResponse resource. 

## Contents
<a name="API_Method_Contents"></a>

 ** apiKeyRequired **   <a name="apigw-Type-Method-apiKeyRequired"></a>
A boolean flag specifying whether a valid ApiKey is required to invoke this method.  
Type: Boolean  
Required: No

 ** authorizationScopes **   <a name="apigw-Type-Method-authorizationScopes"></a>
A list of authorization scopes configured on the method. The scopes are used with a `COGNITO_USER_POOLS` authorizer to authorize the method invocation. The authorization works by matching the method scopes against the scopes parsed from the access token in the incoming request. The method invocation is authorized if any method scopes matches a claimed scope in the access token. Otherwise, the invocation is not authorized. When the method scope is configured, the client must provide an access token instead of an identity token for authorization purposes.  
Type: Array of strings  
Required: No

 ** authorizationType **   <a name="apigw-Type-Method-authorizationType"></a>
The method's authorization type. Valid values are `NONE` for open access, `AWS_IAM` for using AWS IAM permissions, `CUSTOM` for using a custom authorizer, or `COGNITO_USER_POOLS` for using a Cognito user pool.  
Type: String  
Required: No

 ** authorizerId **   <a name="apigw-Type-Method-authorizerId"></a>
The identifier of an authorizer to use on this method. The method's authorization type must be `CUSTOM` or `COGNITO_USER_POOLS`.  
Type: String  
Required: No

 ** httpMethod **   <a name="apigw-Type-Method-httpMethod"></a>
The method's HTTP verb.  
Type: String  
Required: No

 ** methodIntegration **   <a name="apigw-Type-Method-methodIntegration"></a>
Gets the method's integration responsible for passing the client-submitted request to the back end and performing necessary transformations to make the request compliant with the back end.  
Type: [Integration](API_Integration.md) object  
Required: No

 ** methodResponses **   <a name="apigw-Type-Method-methodResponses"></a>
Gets a method response associated with a given HTTP status code.   
Type: String to [MethodResponse](API_MethodResponse.md) object map  
Required: No

 ** operationName **   <a name="apigw-Type-Method-operationName"></a>
A human-friendly operation identifier for the method. For example, you can assign the `operationName` of `ListPets` for the `GET /pets` method in the `PetStore` example.  
Type: String  
Required: No

 ** requestModels **   <a name="apigw-Type-Method-requestModels"></a>
A key-value map specifying data schemas, represented by Model resources, (as the mapped value) of the request payloads of given content types (as the mapping key).  
Type: String to string map  
Required: No

 ** requestParameters **   <a name="apigw-Type-Method-requestParameters"></a>
A key-value map defining required or optional method request parameters that can be accepted by API Gateway. A key is a method request parameter name matching the pattern of `method.request.{location}.{name}`, where `location` is `querystring`, `path`, or `header` and `name` is a valid and unique parameter name. The value associated with the key is a Boolean flag indicating whether the parameter is required (`true`) or optional (`false`). The method request parameter names defined here are available in Integration to be mapped to integration request parameters or templates.  
Type: String to boolean map  
Required: No

 ** requestValidatorId **   <a name="apigw-Type-Method-requestValidatorId"></a>
The identifier of a RequestValidator for request validation.  
Type: String  
Required: No

## See Also
<a name="API_Method_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apigateway-2015-07-09/Method) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apigateway-2015-07-09/Method) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apigateway-2015-07-09/Method)

---
title: GetIceServerConfig
description: Gets the Interactive Connectivity Establishment (ICE) server configuration information, including URIs, user name, and password which can be used to configure the WebRTC connection. The ICE component uses this configuration information to set up the WebRTC connection, including a
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/API_signaling_GetIceServerConfig.html
fetched: '2026-09-26'
tags:
- agentcore
- docs-aws-amazon-com
- reference
- related
referenced_by:
- runtime-webrtc-get-started-kvs.md
conversion: native-md
---

# GetIceServerConfig
<a name="API_signaling_GetIceServerConfig"></a>

 **Note:** Before using this API, you must call the `GetSignalingChannelEndpoint` API to request the HTTPS endpoint. You then specify the endpoint and region in your `GetIceServerConfig` API request.

Gets the Interactive Connectivity Establishment (ICE) server configuration information, including URIs, user name, and password which can be used to configure the WebRTC connection. The ICE component uses this configuration information to set up the WebRTC connection, including authenticating with the Traversal Using Relays around NAT (TURN) relay server. 

TURN is a protocol that is used to improve the connectivity of peer-to-peer applications. By providing a cloud-based relay service, TURN ensures that a connection can be established even when one or more peers are incapable of a direct peer-to-peer connection. For more information, see [A REST API For Access To TURN Services](https://tools.ietf.org/html/draft-uberti-rtcweb-turn-rest-00).

 You can invoke this API to establish a fallback mechanism in case either of the peers is unable to establish a direct peer-to-peer connection over a signaling channel. You must specify the Amazon Resource Name (ARN) of your signaling channel in order to invoke this API.

## Request Syntax
<a name="API_signaling_GetIceServerConfig_RequestSyntax"></a>

```
POST /v1/get-ice-server-config HTTP/1.1
Content-type: application/json

{
   "ChannelARN": "{{string}}",
   "ClientId": "{{string}}",
   "Service": "{{string}}",
   "Username": "{{string}}"
}
```

## URI Request Parameters
<a name="API_signaling_GetIceServerConfig_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_signaling_GetIceServerConfig_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ChannelARN](#API_signaling_GetIceServerConfig_RequestSyntax) **   <a name="KinesisVideo-signaling_GetIceServerConfig-request-ChannelARN"></a>
The ARN of the signaling channel to be used for the peer-to-peer connection between configured peers.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`   
Required: Yes

 ** [ClientId](#API_signaling_GetIceServerConfig_RequestSyntax) **   <a name="KinesisVideo-signaling_GetIceServerConfig-request-ClientId"></a>
Unique identifier for the viewer. Must be unique within the signaling channel.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9_.-]+`   
Required: No

 ** [Service](#API_signaling_GetIceServerConfig_RequestSyntax) **   <a name="KinesisVideo-signaling_GetIceServerConfig-request-Service"></a>
Specifies the desired service. Currently, `TURN` is the only valid value.  
Type: String  
Valid Values: `TURN`   
Required: No

 ** [Username](#API_signaling_GetIceServerConfig_RequestSyntax) **   <a name="KinesisVideo-signaling_GetIceServerConfig-request-Username"></a>
An optional user ID to be associated with the credentials.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9_.-]+`   
Required: No

## Response Syntax
<a name="API_signaling_GetIceServerConfig_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "IceServerList": [ 
      { 
         "Password": "string",
         "Ttl": number,
         "Uris": [ "string" ],
         "Username": "string"
      }
   ]
}
```

## Response Elements
<a name="API_signaling_GetIceServerConfig_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IceServerList](#API_signaling_GetIceServerConfig_ResponseSyntax) **   <a name="KinesisVideo-signaling_GetIceServerConfig-response-IceServerList"></a>
The list of ICE server information objects.  
Type: Array of [IceServer](API_signaling_IceServer.md) objects

## Errors
<a name="API_signaling_GetIceServerConfig_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClientLimitExceededException **   
Your request was throttled because you have exceeded the limit of allowed client calls. Try making the call later.  
HTTP Status Code: 400

 ** InvalidArgumentException **   
The value for this input parameter is invalid.  
HTTP Status Code: 400

 ** InvalidClientException **   
The specified client is invalid.  
HTTP Status Code: 400

 ** NotAuthorizedException **   
The caller is not authorized to perform this operation.  
HTTP Status Code: 401

 ** ResourceNotFoundException **   
The specified resource is not found.  
HTTP Status Code: 404

 ** SessionExpiredException **   
If the client session is expired. Once the client is connected, the session is valid for 45 minutes. Client should reconnect to the channel to continue sending/receiving messages.  
HTTP Status Code: 400

## See Also
<a name="API_signaling_GetIceServerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesis-video-signaling-2019-12-04/GetIceServerConfig) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesis-video-signaling-2019-12-04/GetIceServerConfig) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-video-signaling-2019-12-04/GetIceServerConfig) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesis-video-signaling-2019-12-04/GetIceServerConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-video-signaling-2019-12-04/GetIceServerConfig) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesis-video-signaling-2019-12-04/GetIceServerConfig) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesis-video-signaling-2019-12-04/GetIceServerConfig) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesis-video-signaling-2019-12-04/GetIceServerConfig) 
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesis-video-signaling-2019-12-04/GetIceServerConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-video-signaling-2019-12-04/GetIceServerConfig)

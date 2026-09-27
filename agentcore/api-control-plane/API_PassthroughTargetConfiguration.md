---
title: PassthroughTargetConfiguration
description: The configuration for an HTTP passthrough target. A passthrough target forwards requests directly to an external HTTP endpoint.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_PassthroughTargetConfiguration.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# PassthroughTargetConfiguration
<a name="API_PassthroughTargetConfiguration"></a>

The configuration for an HTTP passthrough target. A passthrough target forwards requests directly to an external HTTP endpoint.

## Contents
<a name="API_PassthroughTargetConfiguration_Contents"></a>

 ** endpoint **   <a name="bedrockagentcorecontrol-Type-PassthroughTargetConfiguration-endpoint"></a>
The HTTPS endpoint that the gateway forwards requests to for this passthrough target.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `https://[a-zA-Z0-9\-\.]+(:[0-9]{1,5})?(/.*)?`   
Required: Yes

 ** protocolType **   <a name="bedrockagentcorecontrol-Type-PassthroughTargetConfiguration-protocolType"></a>
The application protocol that the passthrough target implements. This value is required for passthrough targets:  
+  `MCP` - The Model Context Protocol.
+  `A2A` - The Agent-to-Agent protocol.
+  `INFERENCE` - The protocol for routing requests to a large language model (LLM) provider.
+  `CUSTOM` - A custom application protocol.
Type: String  
Valid Values: `MCP | A2A | INFERENCE | CUSTOM`   
Required: Yes

 ** schema **   <a name="bedrockagentcorecontrol-Type-PassthroughTargetConfiguration-schema"></a>
The API schema configuration that defines the structure of the passthrough target's API.  
Type: [HttpApiSchemaConfiguration](API_HttpApiSchemaConfiguration.md) object  
Required: No

 ** staticQueryParameterConflictResolution **   <a name="bedrockagentcorecontrol-Type-PassthroughTargetConfiguration-staticQueryParameterConflictResolution"></a>
Controls precedence when a client request supplies a query parameter whose name matches a configured static query parameter. If not set, defaults to `CLIENT_OVERRIDE`:  
+  `CLIENT_OVERRIDE` - The client-supplied value overrides the configured static value for that parameter name.
+  `STATIC_OVERRIDE` - The configured static value is retained, overriding the client-supplied value for that parameter name.
Type: String  
Valid Values: `CLIENT_OVERRIDE | STATIC_OVERRIDE`   
Required: No

 ** staticQueryParameters **   <a name="bedrockagentcorecontrol-Type-PassthroughTargetConfiguration-staticQueryParameters"></a>
A map of static query parameters that the gateway always appends to the outbound URL when forwarding requests to the target. The total outbound URL length, which includes the endpoint and the percent-encoded query parameters, is enforced by the service.  
Type: String to string map  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9_.-]+`   
Value Pattern: `[^\x00-\x1F\x7F]*`   
Required: No

 ** stickinessConfiguration **   <a name="bedrockagentcorecontrol-Type-PassthroughTargetConfiguration-stickinessConfiguration"></a>
The session stickiness configuration for the passthrough target. This configuration routes requests within the same session to the same target.  
Type: [StickinessConfiguration](API_StickinessConfiguration.md) object  
Required: No

## See Also
<a name="API_PassthroughTargetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/PassthroughTargetConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/PassthroughTargetConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/PassthroughTargetConfiguration) 
---
title: McpServerTargetConfiguration
description: The target configuration for the MCP server.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_McpServerTargetConfiguration.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# McpServerTargetConfiguration
<a name="API_McpServerTargetConfiguration"></a>

The target configuration for the MCP server.

## Contents
<a name="API_McpServerTargetConfiguration_Contents"></a>

 ** endpoint **   <a name="bedrockagentcorecontrol-Type-McpServerTargetConfiguration-endpoint"></a>
The endpoint for the MCP server target configuration.  
Type: String  
Pattern: `https://.*`   
Required: Yes

 ** listingMode **   <a name="bedrockagentcorecontrol-Type-McpServerTargetConfiguration-listingMode"></a>
The listing mode for the MCP server target configuration. MCP resources for default targets are cached at the control plane for faster access. MCP resources for dynamic targets will be dynamically retrieved when listing tools.  
Type: String  
Valid Values: `DEFAULT | DYNAMIC`   
Required: No

 ** mcpToolSchema **   <a name="bedrockagentcorecontrol-Type-McpServerTargetConfiguration-mcpToolSchema"></a>
A static tool list for the MCP server target. It is supported for all credential providers. Dynamic tool discovery/synchronization will be disabled when a target is configured with mcpToolSchema.  
Type: [McpToolSchemaConfiguration](API_McpToolSchemaConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** resourcePriority **   <a name="bedrockagentcorecontrol-Type-McpServerTargetConfiguration-resourcePriority"></a>
Priority for resolving MCP server targets with shared resource URIs. Lower values take precedence. Defaults to 1000 when not set.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 1000.  
Required: No

## See Also
<a name="API_McpServerTargetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/McpServerTargetConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/McpServerTargetConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/McpServerTargetConfiguration) 
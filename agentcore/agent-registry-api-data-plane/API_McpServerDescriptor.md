---
title: McpServerDescriptor
description: Descriptor that defines the content of an MCP (Model Context Protocol) server registry record, including the server definition and its tool definitions. The content is validated against the MCP protocol schema.
product: Amazon Bedrock AgentCore
section: Agent Registry Data Plane API
source_url: https://docs.aws.amazon.com/agent-registry/latest/APIReference/API_McpServerDescriptor.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-data-plane-api
- agentcore
---

# McpServerDescriptor
<a name="API_McpServerDescriptor"></a>

 Descriptor that defines the content of an MCP (Model Context Protocol) server registry record, including the server definition and its tool definitions. The content is validated against the MCP protocol schema.

## Contents
<a name="API_McpServerDescriptor_Contents"></a>

 ** additionalData **   <a name="agentregistry-Type-McpServerDescriptor-additionalData"></a>
 Additional data associated with the MCP server descriptor, such as tool definitions.  
Type: [McpServerAdditionalData](API_McpServerAdditionalData.md) object  
Required: No

 ** data **   <a name="agentregistry-Type-McpServerDescriptor-data"></a>
 The MCP server descriptor content, serialized as descriptor payload data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 102400.  
Required: No

 ** dataSchemaVersion **   <a name="agentregistry-Type-McpServerDescriptor-dataSchemaVersion"></a>
 The schema version of the descriptor payload.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** source **   <a name="agentregistry-Type-McpServerDescriptor-source"></a>
 The source location from which the MCP (Model Context Protocol) server descriptor content was retrieved.  
Type: [DescriptorSource](API_DescriptorSource.md) object  
Required: No

## See Also
<a name="API_McpServerDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/McpServerDescriptor) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/McpServerDescriptor) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/McpServerDescriptor) 
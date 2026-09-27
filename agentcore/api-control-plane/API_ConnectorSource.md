---
title: ConnectorSource
description: The source identifying the connector integration.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ConnectorSource.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# ConnectorSource
<a name="API_ConnectorSource"></a>

The source identifying the connector integration.

## Contents
<a name="API_ConnectorSource_Contents"></a>

 ** connectorId **   <a name="bedrockagentcorecontrol-Type-ConnectorSource-connectorId"></a>
The identifier for the connector integration (for example, `bedrock-knowledge-bases`).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

 ** version **   <a name="bedrockagentcorecontrol-Type-ConnectorSource-version"></a>
The version of the connector to use (for example, `1.1.0`). If you don't specify a version, the service uses the latest available version.  
Type: String  
Length Constraints: Minimum length of 5. Maximum length of 32.  
Pattern: `(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)`   
Required: No

## See Also
<a name="API_ConnectorSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ConnectorSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ConnectorSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ConnectorSource) 
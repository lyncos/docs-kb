---
title: ResourceLocation
description: The location of the browser extension.
product: Amazon Bedrock AgentCore
section: Data Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ResourceLocation.html
fetched: '2026-09-26'
tags:
- agentcore
- data-plane-api
---

# ResourceLocation
<a name="API_ResourceLocation"></a>

The location of the browser extension.

## Contents
<a name="API_ResourceLocation_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** s3 **   <a name="BedrockAgentCore-Type-ResourceLocation-s3"></a>
The Amazon S3 location of the resource. Use this when the resource is stored in an Amazon S3 bucket.  
Type: [S3Location](API_S3Location.md) object  
Required: No

## See Also
<a name="API_ResourceLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/ResourceLocation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/ResourceLocation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/ResourceLocation) 
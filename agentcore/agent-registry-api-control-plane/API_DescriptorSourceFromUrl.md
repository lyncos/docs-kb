---
title: DescriptorSourceFromUrl
description: URL-based descriptor source configuration, with credential provider configurations for authenticated URL retrieval.
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_DescriptorSourceFromUrl.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# DescriptorSourceFromUrl
<a name="API_DescriptorSourceFromUrl"></a>

URL-based descriptor source configuration, with credential provider configurations for authenticated URL retrieval.

## Contents
<a name="API_DescriptorSourceFromUrl_Contents"></a>

 ** url **   <a name="agentregistrycontrol-Type-DescriptorSourceFromUrl-url"></a>
The URL from which the descriptor content is retrieved.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `https://.*`   
Required: Yes

 ** credentialProviderConfigurations **   <a name="agentregistrycontrol-Type-DescriptorSourceFromUrl-credentialProviderConfigurations"></a>
The credential providers used to authenticate when fetching descriptor content from the source URL.  
Type: Array of [RegistryRecordCredentialProviderConfiguration](API_RegistryRecordCredentialProviderConfiguration.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Required: No

## See Also
<a name="API_DescriptorSourceFromUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/DescriptorSourceFromUrl) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/DescriptorSourceFromUrl) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/DescriptorSourceFromUrl) 
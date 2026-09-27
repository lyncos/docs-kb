---
title: LicenseSpecification
description: A license configuration to associate with the instances.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_LicenseSpecification.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# LicenseSpecification
<a name="API_LicenseSpecification"></a>

A license configuration to associate with the instances.

## Contents
<a name="API_LicenseSpecification_Contents"></a>

 ** licenseConfigurationArn **   <a name="bedrockagentcorecontrol-Type-LicenseSpecification-licenseConfigurationArn"></a>
The Amazon Resource Name (ARN) of the license configuration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:license-manager:[a-z0-9-]+:[0-9]{12}:license-configuration:[a-zA-Z0-9_-]+`   
Required: Yes

## See Also
<a name="API_LicenseSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/LicenseSpecification) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/LicenseSpecification) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/LicenseSpecification) 
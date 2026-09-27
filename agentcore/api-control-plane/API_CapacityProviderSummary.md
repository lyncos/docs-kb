---
title: CapacityProviderSummary
description: A summary of a capacity provider, as returned by `ListCapacityProviders`. Each summary includes the capacity provider identifier, Amazon Resource Name (ARN), name, status, and last-updated timestamp.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CapacityProviderSummary.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# CapacityProviderSummary
<a name="API_CapacityProviderSummary"></a>

A summary of a capacity provider, as returned by `ListCapacityProviders`. Each summary includes the capacity provider identifier, Amazon Resource Name (ARN), name, status, and last-updated timestamp.

## Contents
<a name="API_CapacityProviderSummary_Contents"></a>

 ** capacityProviderArn **   <a name="bedrockagentcorecontrol-Type-CapacityProviderSummary-capacityProviderArn"></a>
The Amazon Resource Name (ARN) of the capacity provider.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:capacity-provider/[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** capacityProviderId **   <a name="bedrockagentcorecontrol-Type-CapacityProviderSummary-capacityProviderId"></a>
The unique identifier of the capacity provider.  
Type: String  
Length Constraints: Minimum length of 12. Maximum length of 59.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** lastUpdatedAt **   <a name="bedrockagentcorecontrol-Type-CapacityProviderSummary-lastUpdatedAt"></a>
The timestamp when the capacity provider was last updated.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-CapacityProviderSummary-name"></a>
The name of the capacity provider.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 48.  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-CapacityProviderSummary-status"></a>
The current status of the capacity provider. For possible values, see `CapacityProviderStatus`.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | READY | DELETING | DELETE_FAILED`   
Required: Yes

## See Also
<a name="API_CapacityProviderSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CapacityProviderSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CapacityProviderSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CapacityProviderSummary) 
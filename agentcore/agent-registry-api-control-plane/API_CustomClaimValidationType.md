---
title: CustomClaimValidationType
description: A validation rule applied to a single claim of an inbound JWT.
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_CustomClaimValidationType.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# CustomClaimValidationType
<a name="API_CustomClaimValidationType"></a>

A validation rule applied to a single claim of an inbound JWT.

## Contents
<a name="API_CustomClaimValidationType_Contents"></a>

 ** authorizingClaimMatchValue **   <a name="agentregistrycontrol-Type-CustomClaimValidationType-authorizingClaimMatchValue"></a>
The value and match operator used to authorize the claim.  
Type: [AuthorizingClaimMatchValueType](API_AuthorizingClaimMatchValueType.md) object  
Required: Yes

 ** inboundTokenClaimName **   <a name="agentregistrycontrol-Type-CustomClaimValidationType-inboundTokenClaimName"></a>
The name of the claim in the inbound token to validate.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z0-9_.-:]+`   
Required: Yes

 ** inboundTokenClaimValueType **   <a name="agentregistrycontrol-Type-CustomClaimValidationType-inboundTokenClaimValueType"></a>
The value type of the claim in the inbound token, either a string or an array of strings.  
Type: String  
Valid Values: `STRING | STRING_ARRAY`   
Required: Yes

## See Also
<a name="API_CustomClaimValidationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/CustomClaimValidationType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/CustomClaimValidationType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/CustomClaimValidationType) 
---
title: AuthorizingClaimMatchValueType
description: The value and match operator used to authorize a claim during JWT validation.
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_AuthorizingClaimMatchValueType.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# AuthorizingClaimMatchValueType
<a name="API_AuthorizingClaimMatchValueType"></a>

The value and match operator used to authorize a claim during JWT validation.

## Contents
<a name="API_AuthorizingClaimMatchValueType_Contents"></a>

 ** claimMatchOperator **   <a name="agentregistrycontrol-Type-AuthorizingClaimMatchValueType-claimMatchOperator"></a>
The operator used to compare the claim value against the expected value.  
Type: String  
Valid Values: `EQUALS | CONTAINS | CONTAINS_ANY`   
Required: Yes

 ** claimMatchValue **   <a name="agentregistrycontrol-Type-AuthorizingClaimMatchValueType-claimMatchValue"></a>
The expected value or values that the claim is compared against.  
Type: [ClaimMatchValueType](API_ClaimMatchValueType.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## See Also
<a name="API_AuthorizingClaimMatchValueType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/AuthorizingClaimMatchValueType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/AuthorizingClaimMatchValueType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/AuthorizingClaimMatchValueType) 
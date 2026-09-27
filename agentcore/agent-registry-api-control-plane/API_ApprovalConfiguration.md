---
title: ApprovalConfiguration
description: Configuration for the registry's record approval workflow. Controls whether records submitted for approval require manual review before they become approved and discoverable, or are auto-approved. When no auto-approval rules are configured, submitted records require manual review
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_ApprovalConfiguration.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# ApprovalConfiguration
<a name="API_ApprovalConfiguration"></a>

Configuration for the registry's record approval workflow. Controls whether records submitted for approval require manual review before they become approved and discoverable, or are auto-approved. When no auto-approval rules are configured, submitted records require manual review.

## Contents
<a name="API_ApprovalConfiguration_Contents"></a>

 ** autoApprovalRules **   <a name="agentregistrycontrol-Type-ApprovalConfiguration-autoApprovalRules"></a>
The rules that determine which registry records are automatically approved on submission. When omitted or empty, submitted records require manual review.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Valid Values: `APPROVE_ALL`   
Required: No

## See Also
<a name="API_ApprovalConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/ApprovalConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/ApprovalConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/ApprovalConfiguration) 
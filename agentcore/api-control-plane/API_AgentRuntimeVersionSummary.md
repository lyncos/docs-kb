---
title: AgentRuntimeVersionSummary
description: Summary information about an agent runtime version associated with a capacity provider. This is returned by `ListAgentRuntimeVersionsByCapacityProvider`.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_AgentRuntimeVersionSummary.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# AgentRuntimeVersionSummary
<a name="API_AgentRuntimeVersionSummary"></a>

Summary information about an agent runtime version associated with a capacity provider. This is returned by `ListAgentRuntimeVersionsByCapacityProvider`.

## Contents
<a name="API_AgentRuntimeVersionSummary_Contents"></a>

 ** agentRuntimeArn **   <a name="bedrockagentcorecontrol-Type-AgentRuntimeVersionSummary-agentRuntimeArn"></a>
The Amazon Resource Name (ARN) of the agent runtime.  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:runtime/[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** agentRuntimeVersion **   <a name="bedrockagentcorecontrol-Type-AgentRuntimeVersionSummary-agentRuntimeVersion"></a>
The version of the agent runtime.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `([1-9][0-9]{0,4})`   
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-AgentRuntimeVersionSummary-status"></a>
The current status of the agent runtime version.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | UPDATING | UPDATE_FAILED | READY | DELETING | DELETE_FAILED`   
Required: Yes

## See Also
<a name="API_AgentRuntimeVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/AgentRuntimeVersionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/AgentRuntimeVersionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/AgentRuntimeVersionSummary) 
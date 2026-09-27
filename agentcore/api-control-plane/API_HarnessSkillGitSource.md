---
title: HarnessSkillGitSource
description: A git repository source for a skill.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_HarnessSkillGitSource.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# HarnessSkillGitSource
<a name="API_HarnessSkillGitSource"></a>

A git repository source for a skill.

## Contents
<a name="API_HarnessSkillGitSource_Contents"></a>

 ** url **   <a name="bedrockagentcorecontrol-Type-HarnessSkillGitSource-url"></a>
The HTTPS URL of the git repository.  
Type: String  
Length Constraints: Minimum length of 8. Maximum length of 16383.  
Pattern: `https://[^#@]+`   
Required: Yes

 ** auth **   <a name="bedrockagentcorecontrol-Type-HarnessSkillGitSource-auth"></a>
Authentication configuration for private repositories.  
Type: [HarnessSkillGitAuth](API_HarnessSkillGitAuth.md) object  
Required: No

 ** path **   <a name="bedrockagentcorecontrol-Type-HarnessSkillGitSource-path"></a>
Subdirectory within the repository containing the skill.  
Type: String  
Required: No

## See Also
<a name="API_HarnessSkillGitSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessSkillGitSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessSkillGitSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessSkillGitSource) 
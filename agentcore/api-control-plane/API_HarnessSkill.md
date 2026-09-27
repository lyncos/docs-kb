---
title: HarnessSkill
description: A skill available to the agent.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_HarnessSkill.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# HarnessSkill
<a name="API_HarnessSkill"></a>

A skill available to the agent.

## Contents
<a name="API_HarnessSkill_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** awsSkills **   <a name="bedrockagentcorecontrol-Type-HarnessSkill-awsSkills"></a>
AWS Skills baked into the harness's underlying Runtime.  
Type: [HarnessSkillAwsSkillsSource](API_HarnessSkillAwsSkillsSource.md) object  
Required: No

 ** git **   <a name="bedrockagentcorecontrol-Type-HarnessSkill-git"></a>
A git repository containing the skill.  
Type: [HarnessSkillGitSource](API_HarnessSkillGitSource.md) object  
Required: No

 ** path **   <a name="bedrockagentcorecontrol-Type-HarnessSkill-path"></a>
The filesystem path to the skill definition.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** s3 **   <a name="bedrockagentcorecontrol-Type-HarnessSkill-s3"></a>
An S3 source containing the skill.  
Type: [HarnessSkillS3Source](API_HarnessSkillS3Source.md) object  
Required: No

## See Also
<a name="API_HarnessSkill_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessSkill) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessSkill) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessSkill) 
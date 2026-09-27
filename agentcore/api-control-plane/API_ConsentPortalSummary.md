---
title: ConsentPortalSummary
description: Summary information about a consent portal.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ConsentPortalSummary.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# ConsentPortalSummary
<a name="API_ConsentPortalSummary"></a>

Summary information about a consent portal.

## Contents
<a name="API_ConsentPortalSummary_Contents"></a>

 ** consentPortalArn **   <a name="bedrockagentcorecontrol-Type-ConsentPortalSummary-consentPortalArn"></a>
The Amazon Resource Name (ARN) of the consent portal.  
Type: String  
Pattern: `arn:aws[^:]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:consent-portal/[a-zA-Z0-9\-_]{1,50}-[A-Za-z0-9]{10}`   
Required: Yes

 ** consentPortalId **   <a name="bedrockagentcorecontrol-Type-ConsentPortalSummary-consentPortalId"></a>
The unique identifier of the consent portal.  
Type: String  
Pattern: `[a-zA-Z0-9\-_]{1,50}-[A-Za-z0-9]{10}`   
Required: Yes

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-ConsentPortalSummary-createdAt"></a>
The timestamp for when the consent portal was created.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-ConsentPortalSummary-name"></a>
The name of the consent portal.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `[a-zA-Z0-9_-]{1,50}`   
Required: Yes

 ** sources **   <a name="bedrockagentcorecontrol-Type-ConsentPortalSummary-sources"></a>
The resources served by the consent portal.  
Type: Array of [ConsentPortalSource](API_ConsentPortalSource.md) objects  
Array Members: Fixed number of 1 item.  
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-ConsentPortalSummary-status"></a>
The current status of the consent portal.  
Type: String  
Valid Values: `CREATING | ACTIVE | UPDATING | UPDATE_FAILED | DELETING | FAILED`   
Required: Yes

 ** updatedAt **   <a name="bedrockagentcorecontrol-Type-ConsentPortalSummary-updatedAt"></a>
The timestamp for when the consent portal was last updated.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="bedrockagentcorecontrol-Type-ConsentPortalSummary-description"></a>
The description of the consent portal.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 512.  
Required: No

 ** portalUrl **   <a name="bedrockagentcorecontrol-Type-ConsentPortalSummary-portalUrl"></a>
The URL used to access the consent portal.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Required: No

## See Also
<a name="API_ConsentPortalSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ConsentPortalSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ConsentPortalSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ConsentPortalSummary) 
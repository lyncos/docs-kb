---
title: RegistryRecordFilter
description: A single filter applied to a ListRegistryRecords request.
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_RegistryRecordFilter.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# RegistryRecordFilter
<a name="API_RegistryRecordFilter"></a>

A single filter applied to a ListRegistryRecords request.

## Contents
<a name="API_RegistryRecordFilter_Contents"></a>

 ** name **   <a name="agentregistrycontrol-Type-RegistryRecordFilter-name"></a>
The attribute to filter on  
Type: String  
Valid Values: `name | status | recordType`   
Required: Yes

 ** values **   <a name="agentregistrycontrol-Type-RegistryRecordFilter-values"></a>
The values to match for the attribute  
Type: Array of strings  
Array Members: Fixed number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

## See Also
<a name="API_RegistryRecordFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/RegistryRecordFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/RegistryRecordFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/RegistryRecordFilter) 
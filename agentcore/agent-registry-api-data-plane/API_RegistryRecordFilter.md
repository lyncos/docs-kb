---
title: RegistryRecordFilter
description: A single filter applied to a `ListDiscoverableRegistryRecords` request.
product: Amazon Bedrock AgentCore
section: Agent Registry Data Plane API
source_url: https://docs.aws.amazon.com/agent-registry/latest/APIReference/API_RegistryRecordFilter.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-data-plane-api
- agentcore
---

# RegistryRecordFilter
<a name="API_RegistryRecordFilter"></a>

 A single filter applied to a `ListDiscoverableRegistryRecords` request.

## Contents
<a name="API_RegistryRecordFilter_Contents"></a>

 ** name **   <a name="agentregistry-Type-RegistryRecordFilter-name"></a>
 The attribute to filter on.  
Type: String  
Valid Values: `recordType | descriptorType`   
Required: Yes

 ** values **   <a name="agentregistry-Type-RegistryRecordFilter-values"></a>
 The values to match for the attribute.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: Yes

## See Also
<a name="API_RegistryRecordFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/RegistryRecordFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/RegistryRecordFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/RegistryRecordFilter) 
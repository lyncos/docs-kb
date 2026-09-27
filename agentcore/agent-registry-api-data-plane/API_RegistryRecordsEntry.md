---
title: RegistryRecordsEntry
description: Binds one registry to the record IDs requested from it.
product: Amazon Bedrock AgentCore
section: Agent Registry Data Plane API
source_url: https://docs.aws.amazon.com/agent-registry/latest/APIReference/API_RegistryRecordsEntry.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-data-plane-api
- agentcore
---

# RegistryRecordsEntry
<a name="API_RegistryRecordsEntry"></a>

 Binds one registry to the record IDs requested from it.

## Contents
<a name="API_RegistryRecordsEntry_Contents"></a>

 ** recordIds **   <a name="agentregistry-Type-RegistryRecordsEntry-recordIds"></a>
 The record IDs to retrieve from the registry. You can specify 1 through 100 record IDs.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/)?[a-zA-Z0-9]{12}`   
Required: Yes

 ** registryId **   <a name="agentregistry-Type-RegistryRecordsEntry-registryId"></a>
 The identifier of the registry to retrieve the records from. You can provide either the full Amazon Resource Name (ARN) or the registry ID.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`   
Required: Yes

## See Also
<a name="API_RegistryRecordsEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/RegistryRecordsEntry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/RegistryRecordsEntry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/RegistryRecordsEntry) 
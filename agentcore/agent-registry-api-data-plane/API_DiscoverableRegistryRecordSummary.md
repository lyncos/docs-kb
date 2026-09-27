---
title: DiscoverableRegistryRecordSummary
description: Summary information about a discoverable registry record returned by ` ListDiscoverableRegistryRecords`. This summary does not include descriptors.
product: Amazon Bedrock AgentCore
section: Agent Registry Data Plane API
source_url: https://docs.aws.amazon.com/agent-registry/latest/APIReference/API_DiscoverableRegistryRecordSummary.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-data-plane-api
- agentcore
---

# DiscoverableRegistryRecordSummary
<a name="API_DiscoverableRegistryRecordSummary"></a>

 Summary information about a discoverable registry record returned by ` ListDiscoverableRegistryRecords`. This summary does not include descriptors.

## Contents
<a name="API_DiscoverableRegistryRecordSummary_Contents"></a>

 ** createdAt **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-createdAt"></a>
 The timestamp when the registry record was created.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-name"></a>
 The name of the registry record. Names are unique within a registry.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`   
Required: Yes

 ** recordArn **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-recordArn"></a>
 The Amazon Resource Name (ARN) of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}`   
Required: Yes

 ** recordId **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-recordId"></a>
 The unique identifier of the registry record.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[a-zA-Z0-9]{12}`   
Required: Yes

 ** recordType **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-recordType"></a>
 The type of the registry record. `MCP` is a Model Context Protocol server record, `AGENT` is an Agent-to-Agent (A2A) agent card record, `SKILL` is an agent skills definition record, and `CUSTOM` is a record with a custom descriptor.  
Type: String  
Valid Values: `MCP | AGENT | CUSTOM | SKILL | GATEWAY`   
Required: Yes

 ** recordVersion **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-recordVersion"></a>
 The version identifier of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9.-]+`   
Required: Yes

 ** registryArn **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-registryArn"></a>
 The Amazon Resource Name (ARN) of the parent registry that owns the record.  
Type: String  
Length Constraints: Minimum length of 46. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}`   
Required: Yes

 ** status **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-status"></a>
 The lifecycle status of the registry record. A record is `DRAFT` before it is submitted, `PENDING_APPROVAL` while awaiting curator review, and `APPROVED` once it is approved and discoverable. `REJECTED` and `DEPRECATED` records are not discoverable. The `CREATING`, `UPDATING`, `CREATE_FAILED`, and `UPDATE_FAILED` values reflect the state of an in-progress or failed asynchronous change.  
Type: String  
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | REJECTED | DEPRECATED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED`   
Required: Yes

 ** updatedAt **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-updatedAt"></a>
 The timestamp when the registry record was last updated.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-description"></a>
 A human-readable description of the registry record. Use this field to explain the record's purpose or content to consumers discovering it in the registry.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** descriptorTypes **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-descriptorTypes"></a>
 The descriptor types that are present on this registry record. Each value corresponds to a descriptor entry key on the approved record.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 10 items.  
Required: No

 ** displayName **   <a name="agentregistry-Type-DiscoverableRegistryRecordSummary-displayName"></a>
 The human-readable display name of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

## See Also
<a name="API_DiscoverableRegistryRecordSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-2025-12-01/DiscoverableRegistryRecordSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-2025-12-01/DiscoverableRegistryRecordSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-2025-12-01/DiscoverableRegistryRecordSummary) 
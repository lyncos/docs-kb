---
title: RegistryRecordSummary
description: A summary of a registry record returned by list operations. Contains identifying and lifecycle fields but omits descriptor content.
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_RegistryRecordSummary.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# RegistryRecordSummary
<a name="API_RegistryRecordSummary"></a>

A summary of a registry record returned by list operations. Contains identifying and lifecycle fields but omits descriptor content.

## Contents
<a name="API_RegistryRecordSummary_Contents"></a>

 ** createdAt **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-createdAt"></a>
The timestamp when the registry record was created.  
Type: Timestamp  
Required: Yes

 ** name **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-name"></a>
The name of the registry record. Names are unique within a registry.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`   
Required: Yes

 ** recordArn **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-recordArn"></a>
The Amazon Resource Name (ARN) of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}`   
Required: Yes

 ** recordId **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-recordId"></a>
The unique identifier of the registry record.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[a-zA-Z0-9]{12}`   
Required: Yes

 ** recordType **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-recordType"></a>
The type of the registry record, such as MCP, AGENT, SKILL, or CUSTOM.  
Type: String  
Valid Values: `MCP | AGENT | CUSTOM | SKILL | GATEWAY`   
Required: Yes

 ** recordVersion **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-recordVersion"></a>
The version identifier of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9.-]+`   
Required: Yes

 ** registryArn **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-registryArn"></a>
The Amazon Resource Name (ARN) of the parent registry that owns the record.  
Type: String  
Length Constraints: Minimum length of 46. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}`   
Required: Yes

 ** status **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-status"></a>
The lifecycle status of the registry record.  
Type: String  
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | REJECTED | DEPRECATED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED`   
Required: Yes

 ** updatedAt **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-updatedAt"></a>
The timestamp when the registry record was last updated.  
Type: Timestamp  
Required: Yes

 ** createdBy **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-createdBy"></a>
The ID of the AWS account that created the registry record.  
Type: String  
Length Constraints: Fixed length of 12.  
Pattern: `[0-9]{12}`   
Required: No

 ** createdByAutoDetection **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-createdByAutoDetection"></a>
Specifies whether the registry record was created by auto-detection. `true` indicates the record was automatically created by the service based on the registry's auto-detection configuration; `false` indicates the record was created through a control-plane API call.  
Type: Boolean  
Required: No

 ** description **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-description"></a>
A description of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** displayName **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-displayName"></a>
The human-readable display name of the registry record.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Required: No

 ** provenanceSummaryList **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-provenanceSummaryList"></a>
The condensed provenance lineage for the registry record. Each entry contains the source relation, source identifier, and source type of an auto-detection lineage entry. Populated for records created by auto-detection.  
Type: Array of [ProvenanceSummary](API_ProvenanceSummary.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 1 item.  
Required: No

## See Also
<a name="API_RegistryRecordSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/RegistryRecordSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/RegistryRecordSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/RegistryRecordSummary) 
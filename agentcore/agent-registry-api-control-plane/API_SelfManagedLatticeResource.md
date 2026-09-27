---
title: SelfManagedLatticeResource
description: A self-managed private endpoint backed by a VPC Lattice resource configuration. Exactly one member is set.
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_SelfManagedLatticeResource.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# SelfManagedLatticeResource
<a name="API_SelfManagedLatticeResource"></a>

A self-managed private endpoint backed by a VPC Lattice resource configuration. Exactly one member is set.

## Contents
<a name="API_SelfManagedLatticeResource_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** resourceConfigurationIdentifier **   <a name="agentregistrycontrol-Type-SelfManagedLatticeResource-resourceConfigurationIdentifier"></a>
The identifier of the VPC Lattice resource configuration, specified as a resource configuration ID or ARN.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`   
Required: No

## See Also
<a name="API_SelfManagedLatticeResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/SelfManagedLatticeResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/SelfManagedLatticeResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/SelfManagedLatticeResource) 
---
title: ManagedVpcResource
description: A service-managed private endpoint provisioned within a customer VPC.
product: Amazon Bedrock AgentCore
section: Agent Registry Control Plane API
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_ManagedVpcResource.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control-plane-api
- agentcore
---

# ManagedVpcResource
<a name="API_ManagedVpcResource"></a>

A service-managed private endpoint provisioned within a customer VPC.

## Contents
<a name="API_ManagedVpcResource_Contents"></a>

 ** endpointIpAddressType **   <a name="agentregistrycontrol-Type-ManagedVpcResource-endpointIpAddressType"></a>
The IP address type used by the private endpoint, either IPV4 or IPV6.  
Type: String  
Valid Values: `IPV4 | IPV6`   
Required: Yes

 ** subnetIds **   <a name="agentregistrycontrol-Type-ManagedVpcResource-subnetIds"></a>
The identifiers of the subnets in which the private endpoint network interfaces are placed.  
Type: Array of strings  
Length Constraints: Minimum length of 15. Maximum length of 24.  
Pattern: `subnet-[0-9a-zA-Z]{8,17}`   
Required: Yes

 ** vpcIdentifier **   <a name="agentregistrycontrol-Type-ManagedVpcResource-vpcIdentifier"></a>
The identifier of the VPC in which the private endpoint is provisioned.  
Type: String  
Length Constraints: Minimum length of 10. Maximum length of 48.  
Pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`   
Required: Yes

 ** routingDomain **   <a name="agentregistrycontrol-Type-ManagedVpcResource-routingDomain"></a>
The routing domain used to resolve traffic through the private endpoint.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 255.  
Required: No

 ** securityGroupIds **   <a name="agentregistrycontrol-Type-ManagedVpcResource-securityGroupIds"></a>
The identifiers of the security groups associated with the private endpoint network interfaces.  
Type: Array of strings  
Array Members: Minimum number of 0 items. Maximum number of 5 items.  
Length Constraints: Minimum length of 10. Maximum length of 48.  
Pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`   
Required: No

 ** tags **   <a name="agentregistrycontrol-Type-ManagedVpcResource-tags"></a>
The tags applied to the service-managed VPC resource.  
Type: String to string map  
Map Entries: Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## See Also
<a name="API_ManagedVpcResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/ManagedVpcResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/ManagedVpcResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/ManagedVpcResource) 
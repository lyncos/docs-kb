---
title: CapacityReservationTarget
description: Information about the target Capacity Reservation or Capacity Reservation group for the instances.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CapacityReservationTarget.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# CapacityReservationTarget
<a name="API_CapacityReservationTarget"></a>

Information about the target Capacity Reservation or Capacity Reservation group for the instances.

## Contents
<a name="API_CapacityReservationTarget_Contents"></a>

 ** capacityReservationId **   <a name="bedrockagentcorecontrol-Type-CapacityReservationTarget-capacityReservationId"></a>
The ID of the Capacity Reservation in which to run the instances.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `cr-[0-9a-z]+`   
Required: No

 ** capacityReservationResourceGroupArn **   <a name="bedrockagentcorecontrol-Type-CapacityReservationTarget-capacityReservationResourceGroupArn"></a>
The Amazon Resource Name (ARN) of the Capacity Reservation resource group in which to run the instances.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:resource-groups:[a-z0-9-]+:[0-9]{12}:group/[a-zA-Z0-9_-]+`   
Required: No

## See Also
<a name="API_CapacityReservationTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CapacityReservationTarget) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CapacityReservationTarget) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CapacityReservationTarget) 
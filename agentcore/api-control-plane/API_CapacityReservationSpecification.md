---
title: CapacityReservationSpecification
description: The Capacity Reservation targeting option for the instances.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_CapacityReservationSpecification.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# CapacityReservationSpecification
<a name="API_CapacityReservationSpecification"></a>

The Capacity Reservation targeting option for the instances.

## Contents
<a name="API_CapacityReservationSpecification_Contents"></a>

 ** capacityReservationPreference **   <a name="bedrockagentcorecontrol-Type-CapacityReservationSpecification-capacityReservationPreference"></a>
The Capacity Reservation preference for the instances.  
Type: String  
Valid Values: `capacity-reservations-only | open | none`   
Required: No

 ** capacityReservationTarget **   <a name="bedrockagentcorecontrol-Type-CapacityReservationSpecification-capacityReservationTarget"></a>
The target Capacity Reservation or Capacity Reservation group for the instances.  
Type: [CapacityReservationTarget](API_CapacityReservationTarget.md) object  
Required: No

## See Also
<a name="API_CapacityReservationSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CapacityReservationSpecification) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CapacityReservationSpecification) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CapacityReservationSpecification) 
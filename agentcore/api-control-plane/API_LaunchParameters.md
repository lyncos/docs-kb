---
title: LaunchParameters
description: The parameters for launching Amazon EC2 instances in a capacity provider.
product: Amazon Bedrock AgentCore
section: Control Plane API
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_LaunchParameters.html
fetched: '2026-09-26'
tags:
- agentcore
- control-plane-api
---

# LaunchParameters
<a name="API_LaunchParameters"></a>

The parameters for launching Amazon EC2 instances in a capacity provider.

## Contents
<a name="API_LaunchParameters_Contents"></a>

 ** instanceRequirements **   <a name="bedrockagentcorecontrol-Type-LaunchParameters-instanceRequirements"></a>
The requirements that determine which instance types can be launched.  
Type: [InstanceRequirements](API_InstanceRequirements.md) object  
Required: Yes

 ** operatingSystem **   <a name="bedrockagentcorecontrol-Type-LaunchParameters-operatingSystem"></a>
The operating system and CPU architecture for the instances.  
Type: String  
Valid Values: `LINUX_X86_64 | LINUX_ARM64`   
Required: Yes

 ** capacityReservationSpecification **   <a name="bedrockagentcorecontrol-Type-LaunchParameters-capacityReservationSpecification"></a>
The Capacity Reservation targeting option for the instances.  
Type: [CapacityReservationSpecification](API_CapacityReservationSpecification.md) object  
Required: No

 ** ephemeralVolumes **   <a name="bedrockagentcorecontrol-Type-LaunchParameters-ephemeralVolumes"></a>
The block device mappings for instance store (ephemeral) volumes. You can specify up to five mappings.  
Type: Array of [EphemeralBlockDeviceMapping](API_EphemeralBlockDeviceMapping.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 5 items.  
Required: No

 ** instanceProfileArn **   <a name="bedrockagentcorecontrol-Type-LaunchParameters-instanceProfileArn"></a>
The Amazon Resource Name (ARN) of the IAM instance profile to associate with launched instances. If provided, this overrides the default instance profile.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:instance-profile/([!-~]{1,510}/)?([\w+=,.@-]{1,128})`   
Required: No

 ** licenseSpecifications **   <a name="bedrockagentcorecontrol-Type-LaunchParameters-licenseSpecifications"></a>
The license configurations to associate with the instances. You can specify up to five configurations.  
Type: Array of [LicenseSpecification](API_LicenseSpecification.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 5 items.  
Required: No

 ** monitoring **   <a name="bedrockagentcorecontrol-Type-LaunchParameters-monitoring"></a>
The monitoring level for the instances.  
Type: String  
Valid Values: `BASIC | DETAILED`   
Required: No

 ** propagatedTags **   <a name="bedrockagentcorecontrol-Type-LaunchParameters-propagatedTags"></a>
The tags to propagate to all Amazon EC2 resources (instances, volumes, and network interfaces) that the capacity provider creates.  
Type: String to string map  
Map Entries: Minimum number of 0 items. Maximum number of 50 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Value Length Constraints: Minimum length of 0. Maximum length of 256.  
Value Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

 ** sshKeyName **   <a name="bedrockagentcorecontrol-Type-LaunchParameters-sshKeyName"></a>
The name of the SSH key pair to configure on the instances for SSH connectivity.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[!-~][ -~]*[!-~]$|^[!-~]`   
Required: No

## See Also
<a name="API_LaunchParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/LaunchParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/LaunchParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/LaunchParameters) 
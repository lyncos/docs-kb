---
title: Quotas for Auto Scaling resources and groups
description: Your AWS account has default quotas, formerly referred to as limits, for each AWS service. Unless otherwise noted, each quota is Region-specific. You can request increases for some quotas, and other quotas cannot be increased.
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-quotas.html
fetched: '2026-09-26'
tags:
- agentcore
- docs-aws-amazon-com
- reference
- related
referenced_by:
- bedrock-agentcore-limits.md
conversion: native-md
---

# Quotas for Auto Scaling resources and groups
<a name="ec2-auto-scaling-quotas"></a>

Your AWS account has default quotas, formerly referred to as limits, for each AWS service. Unless otherwise noted, each quota is Region-specific. You can request increases for some quotas, and other quotas cannot be increased.

To view the quotas for Amazon EC2 Auto Scaling, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home). In the navigation pane, choose **AWS services** and select **Amazon EC2 Auto Scaling**.

To request a quota increase, see [Requesting a Quota Increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*. If the quota is not yet available in Service Quotas, use the [Auto Scaling Limits form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-auto-scaling). Quota increases are tied to the Region they were requested for.

**Amazon EC2 Auto Scaling resources**  
Your AWS account has the following quotas related to the number of Auto Scaling groups and launch configurations that you can create. 


| Resource | Default quota | 
| --- | --- | 
| Auto Scaling groups per region | 500 | 
| Launch configurations per region | 200 | 

**Auto Scaling group configuration**  
Your AWS account has the following quotas related to the configuration of Auto Scaling groups. They cannot be changed.


| Resource | Quota | 
| --- | --- | 
| Scaling policies per Auto Scaling group | 50 | 
| Scheduled actions per Auto Scaling group | 125 | 
| Step adjustments per step scaling policy | 20 | 
| Lifecycle hooks per Auto Scaling group | 50 | 
| SNS topics per Auto Scaling group | 10 | 
| Classic Load Balancers per Auto Scaling group | 50 | 
| Elastic Load Balancing target groups per Auto Scaling group | 50 | 
| VPC Lattice target groups per Auto Scaling group | 5 | 

**Auto Scaling group API operations**  
Amazon EC2 Auto Scaling provides API operations to make changes to your Auto Scaling groups in batches. The following are the API limits on the maximum number of items (maximum array members) that are allowed in a single operation. They cannot be changed.


| Operation | Maximum array members | 
| --- | --- | 
| [AttachInstances](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachInstances.html) | 20 instance IDs  | 
| [AttachLoadBalancers](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachLoadBalancers.html) | 10 load balancers | 
| [AttachLoadBalancerTargetGroups](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_AttachLoadBalancerTargetGroups.html) | 10 target groups | 
| [BatchDeleteScheduledAction](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_BatchDeleteScheduledAction.html) | 50 scheduled actions | 
| [BatchPutScheduledUpdateGroupAction](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_BatchPutScheduledUpdateGroupAction.html) | 50 scheduled actions | 
| [DetachInstances](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachInstances.html) | 20 instance IDs | 
| [DetachLoadBalancers](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachLoadBalancers.html) | 10 load balancers | 
| [DetachLoadBalancerTargetGroups](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DetachLoadBalancerTargetGroups.html) | 10 target groups | 
| [EnterStandby](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_EnterStandby.html) | 20 instance IDs | 
| [ExitStandby](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_ExitStandby.html) | 20 instance IDs | 
| [SetInstanceProtection](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_SetInstanceProtection.html) | 50 instance IDs | 

## Request throttling for the Amazon EC2 Auto Scaling API
<a name="api-request-throttling"></a>

Amazon EC2 Auto Scaling API requests are throttled using a token bucket scheme to maintain service bandwidth. For more information, see [API request rate](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/Welcome.html) in the *Amazon EC2 Auto Scaling API Reference*.

## EC2 termination rates
<a name="instance-termination-rates"></a>

Amazon EC2 Auto Scaling dynamically determines the number of EC2 instance termination operations it can perform at a time when your Auto Scaling group scales in. This means you might see variations in the number of instances terminated at a time across Auto Scaling groups. These variations are caused by external considerations, such as whether Amazon EC2 Auto Scaling must deregister instances with a load balancer.

## Other services
<a name="quotas-for-other-services"></a>

Quotas for other services, such as Amazon EC2 and Amazon VPC, can impact your Auto Scaling groups. You can use Service Quotas to update the quotas for EC2 instances and other resources in your AWS account. In the Service Quotas console, you can view all your available service quotas and request increases for them. For more information, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.

For quotas that are specific to launch templates, see [Launch template restrictions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launch-template-restrictions.html) in the *Amazon EC2 User Guide*.

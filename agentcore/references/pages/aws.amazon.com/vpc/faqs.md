---
title: Amazon VPC FAQs
description: Amazon VPC
product: Amazon Bedrock AgentCore
section: References / aws.amazon.com
source_url: https://aws.amazon.com/vpc/faqs
fetched: '2026-09-26'
tags:
- agentcore
- aws-amazon-com
- reference
- related
referenced_by:
- gateway-vpc-egress.md
conversion: pandoc
---

Amazon VPC

- [Overview](/vpc/)
- Features
- [Pricing](/vpc/pricing/)
- [FAQs](/vpc/faqs/)

# Amazon VPC FAQs

- [General Questions](#general-questions--1fg7rww)
  5
- [Billing](#billing--1fg7rww)
  2
- [Connectivity](#connectivity--1fg7rww)
  9
- [IP Addressing](#ip-addressing--1fg7rww)
  16
- [Bring Your Own IP](#bring-your-own-ip--1fg7rww)
  10
- [IP Address Manager](#ip-address-manager--1fg7rww)
  8
- [Topology](#topology--1fg7rww)
  1
- [Security and Filtering](#security-and-filtering--1fg7rww)
  12
- [VPC Traffic Mirroring](#vpc-traffic-mirroring--1fg7rww)
  4
- [Amazon VPC and EC2](#amazon-vpc-and-ec2--1fg7rww)
  18
- [Default VPCs](#default-vpcs--1fg7rww)
  17
- [EC2 Classic](#ec2-classic--1fg7rww)
  6
- [Elastic Network Interfaces](#elastic-network-interfaces--1fg7rww)
  5
- [Peering Connections](#peering-connections--1fg7rww)
  14
- [ClassicLink](#classiclink--1fg7rww)
  10
- [AWS PrivateLink](#aws-privatelink--1fg7rww)
  4
- [Additional Questions](#additional-questions--1fg7rww)
  4
- [VPC Encryption Controls](#vpc-encryption-controls--1fg7rww)
  23

### General Questions

[Open all](#)

#### What is Amazon Virtual Private Cloud?

Amazon VPC lets you provision a logically isolated section of the Amazon Web Services (AWS) cloud where you can launch AWS resources in a virtual network that you define. You have complete control over your virtual networking environment, including selection of your own IP address ranges, creation of subnets, and configuration of route tables and network gateways. You can also create a hardware Virtual Private Network (VPN) connection between your corporate datacenter and your VPC and leverage the AWS cloud as an extension of your corporate datacenter.

You can easily customize the network configuration for your Amazon VPC. For example, you can create a public-facing subnet for your web servers that have access to the Internet, and place your backend systems such as databases or application servers in a private-facing subnet with no Internet access. You can leverage multiple layers of security, including security groups and network access control lists, to help control access to Amazon EC2 instances in each subnet.

#### What are the components of Amazon VPC?

Amazon VPC comprises a variety of objects that will be familiar to customers with existing networks:

- **A Virtual Private Cloud:** A logically isolated virtual network in the AWS cloud. You define a VPC’s IP address space from ranges you select.
- **Subnet:** A segment of a VPC’s IP address range where you can place groups of isolated resources.
- **Internet Gateway:** The Amazon VPC side of a connection to the public Internet.
- **NAT Gateway:** A highly available, managed Network Address Translation (NAT) service for your resources in a private subnet to access the Internet.
- **Virtual private gateway:** The Amazon VPC side of a VPN connection.
- **Peering Connection:** A peering connection enables you to route traffic via private IP addresses between two peered VPCs.
- **VPC Endpoints: **Enables private connectivity to services hosted in AWS, from within your VPC without using an Internet Gateway, VPN, Network Address Translation (NAT) devices, or firewall proxies.
- **Egress-only Internet Gateway:** A stateful gateway to provide egress only access for IPv6 traffic from the VPC to the Internet.

#### Why should I use Amazon VPC?

-  Amazon VPC enables you to build a virtual network in the AWS cloud - no VPNs, hardware, or physical datacenters required. You can define your own network space, and control how your network and the Amazon EC2 resources inside your network are exposed to the Internet. You can also leverage the enhanced security options in Amazon VPC to provide more granular access to and from the Amazon EC2 instances in your virtual network.

#### How do I get started with Amazon VPC?

Your AWS resources are automatically provisioned in a ready-to-use default VPC. You can choose to create additional VPCs by going to the Amazon VPC page in the AWS Management Console and selecting "Start VPC Wizard".

You’ll be presented with four basic options for network architectures. After selecting an option, you can modify the size and IP address range of the VPC and its subnets. If you select an option with Hardware VPN Access, you will need to specify the IP address of the VPN hardware on your network. You can modify the VPC to add or remove secondary IP ranges and gateways, or add more subnets to IP ranges.

The four options are:

1.  Amazon VPC with a single public subnet only
2.  Amazon VPC with public and private subnets
3.  Amazon VPC with public and private subnets and AWS Site-to-Site VPN access
4.  Amazon VPC with a private subnet only and AWS Site-to-Site VPN access

#### What are the different types of VPC endpoints available on Amazon VPC?

VPC endpoints enable you to privately connect your VPC to services hosted on AWS without requiring an Internet gateway, a NAT device, VPN, or firewall proxies. Endpoints are horizontally scalable and highly available virtual devices that allow communication between instances in your VPC and AWS services. Amazon VPC offers two different types of endpoints: gateway type endpoints and interface type endpoints.

Gateway type endpoints are available only for AWS services including S3 and DynamoDB. These endpoints will add an entry to your route table you selected and route the traffic to the supported services through Amazon’s private network.

Interface type endpoints provide private connectivity to services powered by PrivateLink, being AWS services, your own services or SaaS solutions, and supports connectivity over Direct Connect. More AWS and SaaS solutions will be supported by these endpoints in the future. Please refer to VPC Pricing for the price of interface type endpoints.

### Billing

[Open all](#)

#### How will I be charged and billed for my use of Amazon VPC?

There are no additional charges for creating and using the VPC itself. Usage charges for other Amazon Web Services, including Amazon EC2, still apply at published rates for those resources, including data transfer charges. If you connect your VPC to your corporate datacenter using the optional hardware VPN connection, pricing is per VPN connection-hour (the amount of time you have a VPN connection in the "available" state.) Partial hours are billed as full hours. Data transferred over VPN connections will be charged at standard AWS Data Transfer rates. For VPC-VPN pricing information, please visit the [pricing section](/vpc/pricing/) of the [Amazon VPC product page](/vpc).

#### What usage charges will I incur if I use other AWS services, such as Amazon S3, from Amazon EC2 instances in my VPC?

Usage charges for other Amazon Web Services, including Amazon EC2, still apply at published rates for those resources. Data transfer charges are not incurred when accessing Amazon Web Services, such as Amazon S3, via your VPC’s Internet gateway.

If you access AWS resources via your VPN connection, you will incur Internet data transfer charges.

### Connectivity

[Open all](#)

#### What are the connectivity options for my Amazon VPC?

You may connect your Amazon VPC to:

- The internet (via an internet gateway)
- Your corporate data center using an AWS Site-to-Site VPN connection (via the virtual private gateway)
- Both the internet and your corporate data center (utilizing both an internet gateway and a virtual private gateway)
- Other AWS services (via internet gateway, NAT, virtual private gateway, or VPC endpoints)
- Other Amazon VPCs (via VPC peering connections)

#### How do I connect my VPC to the Internet?

-  Amazon VPC supports the creation of an Internet gateway. This gateway enables Amazon EC2 instances in the VPC to directly access the Internet. You can also use an Egress-only internet gateway which is a stateful gateway to provide egress only access for IPv6 traffic from the VPC to the Internet.

#### Are there any bandwidth limitations for Internet gateways? Do I need to be concerned about its availability? Can it be a single point of failure?

-  No. An Internet gateway is horizontally-scaled, redundant, and highly available. It imposes no bandwidth constraints.

#### How do instances in a VPC access the Internet?

-  You can use public IP addresses, including Elastic IP addresses (EIPs) and IPv6 Global Unique addresses (GUA), to give instances in the VPC the ability to both directly communicate outbound to the internet and to receive unsolicited inbound traffic from the internet (e.g., web servers). You can also use the solutions in the next question.

#### When is an IP address considered a Public IP address?

-  Any IP address that is assigned to an instance or a service hosted in a VPC that can be accessed over the internet is considered a public IP address. Only public IPv4 addresses, including Elastic IP addresses (EIPs) and IPv6 GUA can be routable on the internet. To do so, you would need to first connect the VPC to the internet and then update the route table to make them reachable to/from the internet.

#### How do instances without public IP addresses access the Internet?

Instances without public IP addresses can access the Internet in one of two ways:

1.  Instances without public IP addresses can route their traffic through a NAT gateway or a NAT instance to access the Internet. These instances use the public IP address of the NAT gateway or NAT instance to traverse the Internet. The NAT gateway or NAT instance allows outbound communication but doesn’t allow machines on the Internet to initiate a connection to the privately addressed instances.
2.  For VPCs with a hardware VPN connection or Direct Connect connection, instances can route their Internet traffic down the virtual private gateway to your existing datacenter. From there, it can access the Internet via your existing egress points and network security/monitoring devices.

#### Can I connect to my VPC using a software VPN?

-  Yes. You may use a third-party software VPN to create a site to site or remote access VPN connection with your VPC via the Internet gateway.

#### Does traffic go over the internet when two instances communicate using public IP addresses, or when instances communicate with a public AWS service endpoint?

No. When using public IP addresses, all communication between instances and services hosted in AWS use AWS's private network. Packets that originate from the AWS network with a destination on the AWS network stay on the AWS global network, except traffic to or from AWS China Regions and the AWS European Sovereign Cloud Region..

In addition, all data flowing across the AWS global network that interconnects our data centers and Regions is automatically encrypted at the physical layer before it leaves our secured facilities. Additional encryption layers exist as well; for example, all VPC cross-region peering traffic, and customer or service-to-service Transport Layer Security (TLS) connections. 

#### How does an AWS Site-to-Site VPN connection work with Amazon VPC?

-  An AWS Site-to-Site VPN connection connects your VPC to your datacenter. Amazon supports Internet Protocol Security (IPSec) VPN connections. Data transferred between your VPC and datacenter routes over an encrypted VPN connection to help maintain the confidentiality and integrity of data in transit. An internet gateway is not required to establish an AWS Site-to-Site VPN connection.

### IP Addressing

[Open all](#)

#### What IP address ranges can I use within my Amazon VPC?

You can use any [IPv4](https://en.wikipedia.org/wiki/IPv4) address range, including [RFC 1918](https://tools.ietf.org/html/rfc1918) or publicly routable IP ranges, for the primary CIDR block. For the secondary CIDR blocks, certain [restrictions](http://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html#add-cidr-block-restrictions) apply. Publicly routable IP blocks are only reachable via the Virtual Private Gateway and cannot be accessed over the Internet through the Internet gateway. AWS does not advertise customer-owned IP address blocks to the Internet. You can allocate  up to 5 Amazon-provided or BYOIP IPv6 GUA CIDR blocks to a VPC by calling the relevant API or via the AWS Management Console.

#### How do I assign IP address ranges to Amazon VPCs?

You assign a single [Classless Internet Domain Routing (CIDR)](https://en.wikipedia.org/wiki/CIDR) IP address range as the primary CIDR block when you create a VPC and can add up to four (4) secondary CIDR blocks after creation of the VPC. Subnets within a VPC are addressed from these CIDR ranges by you. Please note that while you can create multiple VPCs with overlapping IP address ranges, doing so will prohibit you from connecting these VPCs to a common home network via the hardware VPN connection. . For this reason we recommend using non-overlapping IP address ranges. You can allocate up to 5 Amazon-provided or BYOIP IPv6 CIDR blocks to your VPC.

#### What IP address ranges are assigned to a default Amazon VPC?

-  Default VPCs are assigned a CIDR range of 172.31.0.0/16. Default subnets within a default VPC are assigned /20 netblocks within the VPC CIDR range. 

#### Can I use my IP addresses in VPC and access them over the Internet?

-  Yes, you can bring your public IPv4 addresses and IPv6 GUA addresses into AWS VPC and statically allocate them to subnets and EC2 instances. To access these addresses over the Internet, you will have to advertise them to the Internet from your on-premises network. You will also have to route the traffic over these addresses between your VPC and on-premises network using AWS DX or AWS VPN connection. You can route the traffic from your VPC using the Virtual Private Gateway. Similarly, you can route the traffic from your on-premises network back to your VPC using your routers.

#### How large of a VPC can I create?

Currently, Amazon VPC supports five (5) IP address ranges, one (1) primary and four (4) secondary for IPv4. Each of these ranges can be between /28 (in CIDR notation) and /16 in size. The IP address ranges of your VPC should not overlap with the IP address ranges of your existing network.

For IPv6, the VPC is a fixed size of /56 (in CIDR notation). A VPC can have both IPv4 and IPv6 CIDR blocks associated to it.

#### Can I change the size of a VPC?

-  Yes. You can expand your existing VPC by adding four (4) secondary IPv4 IP ranges (CIDRs) to your VPC. You can shrink your VPC by deleting the secondary CIDR blocks you have added to your VPC.   Likewise, you can add up to five (5) additionally IPv6 IP ranges (CIDRs) to your VPC.  You can shrink your VPC by deleting these additional ranges.

#### How many subnets can I create per VPC?

Currently you can create 200 subnets per VPC. If you would like to create more, please [submit a case at the support center](/contact-us/vpc-request/).

#### Is there a limit on how large or small a subnet can be?

The minimum size of a subnet is a /28 (or 14 IP addresses.) for IPv4. Subnets cannot be larger than the VPC in which they are created.

For IPv6, the subnet size is fixed to be a /64. Only one IPv6 CIDR block can be allocated to a subnet.

#### Can I use all the IP addresses that I assign to a subnet?

-  No. Amazon reserves the first four (4) IP addresses and the last one (1) IP address of every subnet for IP networking purposes.

#### How do I assign private IP addresses to Amazon EC2 instances within a VPC?

-  When you launch an Amazon EC2 instance within a subnet that is not IPv6-only, you may optionally specify the primary private IPv4 address for the instance. If you do not specify the primary private IPv4 address, AWS automatically addresses it from the IPv4 address range you assign to that subnet. You can assign secondary private IPv4 addresses when you launch an instance, when you create an Elastic Network Interface, or any time after the instance has been launched or the interface has been created. In case you launch an Amazon EC2 instance within an IPv6-only subnet, AWS automatically addresses it from the Amazon-provided IPv6 GUA CIDR of that subnet. The instance’s IPv6 GUA will remain private unless you make them reachable to/from the internet with the right security group, NACL, and route table configuration.

#### Can I change the private IP addresses of an Amazon EC2 instance while it is running and/or stopped within a VPC?

-  For an instance launched in an IPv4 or dual-stack subnet, the primary private IPv4 address is retained for the instance's or interface's lifetime. Secondary private IPv4 addresses can be assigned, unassigned, or moved between interfaces or instances at any time. For an instance launched in an IPv6-only subnet, the assigned IPv6 GUA which is also the first IP address on the instance's primary network interface can be modified by associating a new IPv6 GUA and removing the existing IPv6 GUA at any time.

#### If an Amazon EC2 instance is stopped within a VPC, can I launch another instance with the same IP address in the same VPC?

-  No. An IPv4 address assigned to a running instance can only be used again by another instance once that original running instance is in a “terminated” state. However, the IPv6 GUA assigned to a running instance can be used again by another instance after it is removed from the first instance.

#### Can I assign IP addresses for multiple instances simultaneously?

-  No. You can specify the IP address of one instance at a time when launching the instance.

#### Can I assign any IP address to an instance?

You can assign any IP address to your instance as long as it is:

- Part of the associated subnet's IP address range
- Not reserved by Amazon for IP networking purposes
- Not currently assigned to another interface

#### Can I assign multiple IP addresses to an instance?

Yes. You can assign one or more secondary private IP addresses to an Elastic Network Interface or an EC2 instance in Amazon VPC. The number of secondary private IP addresses you can assign depends on the instance type. See [EC2 User Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) for more information on the number of secondary private IP addresses that can be assigned per instance type.

#### Can I assign one or more Elastic IP (EIP) addresses to VPC-based Amazon EC2 instances?

-  Yes, however, the EIP addresses will only be reachable from the Internet (not over the VPN connection). Each EIP address must be associated with a unique private IP address on the instance. EIP addresses should only be used on instances in subnets configured to route their traffic directly to the Internet gateway. EIPs cannot be used on instances in subnets configured to use a NAT gateway or a NAT instance to access the Internet. This is applicable only for IPv4. Amazon VPCs do not support EIPs for IPv6 at this time.

### Bring Your Own IP

[Open all](#)

#### What is the Bring Your Own IP feature?

-  Bring Your Own IP (BYOIP) enables customers to move all or part of their existing publicly routable IPv4 or IPv6 address space to AWS for use with their AWS resources. Customers will continue to own the IP range. Customers can create Elastic IPs from the IPv4 space they bring to AWS and use them with EC2 instances, NAT Gateways, and Network Load Balancers. Customers can also associate up to 5 CIDRs to a VPC from the IPv6 space they bring to AWS. Customers will continue to have access to Amazon-supplied IPs and can choose to use BYOIP Elastic IPs, Amazon-supplied IPs, or both.

#### Why should I use BYOIP?

You may want to bring your own IP addresses to AWS for the following reasons:  
IP Reputation: Many customers consider the reputation of their IP addresses to be a strategic asset and want to use those IPs on AWS with their resources. For example, customers who maintain services such as outbound e-mail MTA and have high reputation IPs, can now bring over their IP space and successfully maintain their existing sending success rate.

Customer whitelisting: BYOIP also enables customers to move workloads that rely on IP address whitelisting to AWS without the need to re-establish the whitelists with new IP addresses.

Hardcoded dependencies: Several customers have IPs hardcoded in devices or have taken architectural dependencies on their IPs. BYOIP enables such customers hassle free migration to AWS.

Regulation and compliance: Many customers are required to use certain IPs because of regulation and compliance reasons. They too are unlocked by BYOIP.

On-prem IPv6 network policy: Many customers can route only their IPv6 in their on-prem network. These customers are unlocked by BYOIP as they can assign their own IPv6 range to their VPC and choose to route to their on-prem network using internet or Direct Connect.

#### What happens if I release a BYOIP Elastic IP?

-  When you release a BYOIP Elastic IP it goes back to the BYOIP IP pool from which it was allocated.

#### In which AWS Regions is BYOIP available?

See our [documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html#byoip-reg-avail) for details on BYOIP availability.

#### Can a BYOIP prefix be shared with multiple VPCs in the same account?

-  Yes. You can use the BYOIP prefix with any number of VPCs in the same account.

#### How many IP ranges can I bring via BYOIP?

-  You can bring a maximum of five IP ranges to your account.

#### What is the most specific prefix that I can bring via BYOIP?

-  Via BYOIP, the most specific IPv4 prefix you can bring is a /24 IPv4 prefix and a /56 IPv6 prefix. If you intend to advertise your Ipv6 prefix to the internet then most specific IPv6 prefix is /48.

#### Which RIR prefixes can I use for BYOIP?

-  You can use ARIN, RIPE, and APNIC registered prefixes.

#### Can I bring a reassigned or reallocated prefix?

-  We are not accepting reassigned or reallocated prefixes at this time. IP ranges should be a net type of direct allocation or direct assignment.

#### Can I move a BYOIP prefix from one AWS Region to another?

-  Yes. You can do that by de-provisioning the BYOIP prefix from the current region and then provisioning it to the new region.

### IP Address Manager

[Open all](#)

#### What is VPC IP Address Manager (IPAM)?

-  Amazon VPC IP Address Manager (IPAM) is a managed service that makes it easier for you to plan, track, and monitor IP addresses for your AWS workloads. Using IPAM, you can easily organize IP addresses based on your routing and security needs and set simple business rules to govern IP address assignments. You can also automate IP address assignment to VPCs, eliminating the need to use spreadsheet-based or homegrown IP address planning applications, which can be hard to maintain and time-consuming. IPAM provides a unified operational view, which can be used as your single source of truth, enabling you to quickly and efficiently perform routine IP address management activities such as tracking IP utilization, troubleshooting, and auditing.

#### Why should you use IPAM?

-  You should use IPAM to make IP address management more efficient. Existing mechanisms that leverage spreadsheets or home-grown tools require manual work, and are error-prone. With IPAM, as an example, you can roll out applications faster as your developers no longer need to wait for the central IP address administration team to allocate IP addresses. You can also detect overlapping IP addresses and fix them before there is a network outage. In addition, you can create alarms for IPAM to notify you if the address pools are nearing exhaustion or if resources fail to comply with allocations rules set on a pool. These are some of the many reasons you should use IPAM.

#### What are the key features offered by IPAM?

AWS IPAM provides the following features:  
 

- **Allocate IP addresses for at-scale networks:** IPAM can automate IP address allocations across hundreds of accounts and VPCs based on configurable business rules.  
   
- **Monitor IP usage across your network:** IPAM can monitor IP addresses and enables you to get alerts when IPAM detects potential issues such as depleting IP addresses that can stall network’s growth or overlapping IP addresses that can result in erroneous routing.  
   
- **Troubleshoot your network:** IPAM can help you quickly identify if connectivity issues are due to IP address misconfigurations or other issues.  
   
- **Audit IP addresses:** IPAM automatically retains your IP address monitoring data (up to a maximum of three years). You can use this historical data to do retrospective analysis and audits for your network.

#### What are the key components of IPAM?

The following are the key components of IPAM:

- A **scope** is the highest-level container within IPAM. An IPAM contains two default scopes. Each scope represents the IP space for a single network. The **private scope** is intended for all private space. The **public scope** is intended for all public space. Scopes enable you to reuse IP addresses across multiple unconnected networks without causing IP address overlap or conflict. Within a scope, you create IPAM pools.  
   
- A **pool** is a collection of contiguous IP address ranges (or CIDRs). IPAM pools enable you to organize your IP addresses according to your routing and security needs. You can have multiple pools within a top-level pool. For example, if you have separate routing and security needs for development and production applications, you can create a pool for each. Within IPAM pools, you allocate CIDRs to AWS resources.
- An **allocation** is a CIDR assignment from an IPAM pool to another resource or IPAM pool. When you create a VPC and choose an IPAM pool for the VPC’s CIDR, the CIDR is allocated from the CIDR provisioned to the IPAM pool. You can monitor and manage the allocation with IPAM.

#### Does IPAM support Bring Your Own IPs (BYOIPs)?

Yes. IPAM supports both BYOIPv4 and BYOIPv6 addresses. BYOIP is an [EC2 feature](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html) that allows you to bring IP addresses owned by you to AWS. With IPAM, you can directly provision and share their IP address blocks across accounts and organization. Existing BYOIP customers using IPv4 can migrate their pools into IPAM to simplify IP management.

#### Does Amazon Provide Contiguous CIDR Blocks and how do they work with IPAM?

-  Yes, Amazon Provides Contiguous IPv6 CIDR blocks for VPC allocation. Contigous CIDR blocks allow you to aggregated CIDRs in a single entry across networking and security constructs like access control lists, route tables, security groups, and firewalls. You can provision Amazon IPv6 CIDRs into a publicly scoped pool, and use all of the IPAM features to manage and monitor IP usage. Allocation of these CIDR blocks start in /52 increments, and larger blocks are available upon request. For example, you can allocate /52 CIDR from Amazon and use IPAM to share across accounts and create VPCs in those accounts.

#### Can you use Amazon Provided Contiguous IPv6 CIDR blocks without IPAM?

-  No, Amazon Provided Contiguous IPv6 CIDR blocks are currently only supported in IPAM.

#### Can I share my IPAM pools with other accounts?

-  You can share IPAM pools with other accounts in your AWS Organization using AWS Resource Access Manager (RAM). You can also share IPAM pools with accounts outside of your primary AWS Organization. For example, these accounts can represent another line of business in your company or a managed service hosted by a partner on your behalf, in another AWS Organization.

### Topology

[Open all](#)

#### Can I specify which subnet will use which gateway as its default?

-  Yes. You may create a default route for each subnet. The default route can direct traffic to egress the VPC via the Internet gateway, the virtual private gateway, or the NAT gateway.

### Security and Filtering

[Open all](#)

#### How do I secure Amazon EC2 instances running within my VPC?

Amazon EC2 security groups can be used to help secure instances within an Amazon VPC. Security groups in a VPC enable you to specify both inbound and outbound network traffic that is allowed to or from each Amazon EC2 instance. Traffic which is not explicitly allowed to or from an instance is automatically denied.

In addition to security groups, network traffic entering and exiting each subnet can be allowed or denied via network Access Control Lists (ACLs).

#### What are the differences between security groups in a VPC and network ACLs in a VPC?

-  Security groups in a VPC specify which traffic is allowed to or from an Amazon EC2 instance. Network ACLs operate at the subnet level and evaluate traffic entering and exiting a subnet. Network ACLs can be used to set both Allow and Deny rules. Network ACLs do not filter traffic between instances in the same subnet. In addition, network ACLs perform stateless filtering while security groups perform stateful filtering.

#### What is the difference between stateful and stateless filtering?

Stateful filtering tracks the origin of a request and can automatically allow the reply to the request to be returned to the originating computer. For example, a stateful filter that allows inbound traffic to TCP port 80 on a webserver will allow the return traffic, usually on a high numbered port (e.g., destination TCP port 63, 912) to pass through the stateful filter between the client and the webserver. The filtering device maintains a state table that tracks the origin and destination port numbers and IP addresses. Only one rule is required on the filtering device: Allow traffic inbound to the web server on TCP port 80.

Stateless filtering, on the other hand, only examines the source or destination IP address and the destination port, ignoring whether the traffic is a new request or a reply to a request. In the above example, two rules would need to be implemented on the filtering device: one rule to allow traffic inbound to the web server on TCP port 80, and another rule to allow outbound traffic from the webserver (TCP port range 49, 152 through 65, 535).

#### Can Amazon EC2 instances within a VPC communicate with Amazon EC2 instances not within a VPC?

-  Yes. If an Internet gateway has been configured, Amazon VPC traffic bound for Amazon EC2 instances not within a VPC traverses the Internet gateway and then enters the public AWS network to reach the EC2 instance. If an Internet gateway has not been configured, or if the instance is in a subnet configured to route through the virtual private gateway, the traffic traverses the VPN connection, egresses from your datacenter, and then re-enters the public AWS network.

#### Can Amazon EC2 instances within a VPC in one region communicate with Amazon EC2 instances within a VPC in another region?

-  Yes. Instances in one region can communicate with each other using Inter-Region VPC Peering, public IP addresses, NAT gateway, NAT instances, VPN Connections or Direct Connect connections.

#### Can Amazon EC2 instances within a VPC communicate with Amazon S3?

-  Yes. There are multiple options for your resources within a VPC to communicate with Amazon S3. You can use VPC Endpoint for S3, which makes sure all traffic remains within Amazon's network and enables you to apply additional access policies to your Amazon S3 traffic. You can use an Internet gateway to enable Internet access from your VPC and instances in the VPC can communicate with Amazon S3. You can also make all traffic to Amazon S3 traverse the Direct Connect or VPN connection, egress from your datacenter, and then re-enter the public AWS network.

#### Can I monitor the network traffic in my VPC?

-  Yes. You can use Amazon VPC traffic mirroring and Amazon VPC flow logs features to monitor the network traffic in your Amazon VPC.

#### What is Amazon VPC flow logs?

VPC flow logs is a feature that enables you to capture information about the IP traffic going to and from network interfaces in your VPC. Flow logs data can be published to either Amazon CloudWatch Logs or Amazon S3. You can monitor your VPC flow logs to gain operational visibility about your network dependencies and traffic patterns, detect anomalies and prevent data leakage, or troubleshoot network connectivity and configuration issues. The enriched metadata in flow logs help you gain additional insights about who initiated your TCP connections, and the actual packet-level source and destination for traffic flowing through intermediate layers such as the NAT Gateway. You can also archive your flow logs to meet compliance requirements. To learn more about Amazon VPC flow logs, please refer to the [documentation](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/flow-logs.html).

#### How can I use VPC flow logs?

-  You can create a flow log for a VPC, a subnet, or a network interface. If you create a flow log for a subnet or VPC, each network interface in that subnet or VPC is monitored. While creating a flow log subscription, you can choose the metadata fields you wish to capture, the maximum aggregation interval, and your preferred log destination. You can also choose to capture all traffic or only accepted or rejected traffic. You can use tools like CloudWatch Log Insights or CloudWatch Contributor Insights to analyze your VPC flow logs delivered to CloudWatch Logs. You can use tools like Amazon Athena or AWS QuickSight to query and visualize your VPC flow logs delivered to Amazon S3. You can also build a custom downstream application to analyze your logs or use partner solutions such as Splunk, Datadog, Sumo Logic, Cisco StealthWatch, Checkpoint CloudGuard, New Relic etc.

#### Do VPC flow logs support AWS Transit Gateway?

Yes, you can create VPC flow log for a Transit Gateway or for an individual Transit Gateway attachment. With this feature Transit Gateway can export detailed information such as source/destination IPs, ports, protocol, traffic counters, timestamps and various metadata for network flows traversing via the Transit Gateway. To learn more about Amazon VPC flow logs support for Transit Gateway, please refer to the [documentation.](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html)

#### Does using Flow Logs impact my network latency or performance?

-  Flow log data is collected outside of the path of your network traffic, and therefore does not affect network throughput or latency. You can create or delete flow logs without any risk of impact to network performance.

#### How much VPC flow logs cost?

Data ingestion and archival charges for vended logs apply when you publish flow logs to CloudWatch Logs or to Amazon S3. For more information and examples, see [Amazon CloudWatch Pricing](/cloudwatch/pricing/). You can also track charges from publishing flow logs using cost allocation tags.

### VPC Traffic Mirroring

[Open all](#)

#### What is Amazon VPC traffic mirroring?

-  Amazon VPC traffic mirroring makes it easy for customers to replicate network traffic to and from an Amazon EC2 instance and forward it to out-of-band security and monitoring appliances for use-cases such as content inspection, threat monitoring, and troubleshooting. These appliances can be deployed on an individual EC2 instance or a fleet of instances behind a Network Load Balancer (NLB) with User Datagram Protocol (UDP) listener.

#### Which resources can be monitored with Amazon VPC traffic mirroring ?

Traffic mirroring supports network packet captures at the Elastic Network Interface (ENI) level for EC2 instances. Refer to the [Traffic Mirroring documentation](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-considerations.html) for the EC2 instances that support Amazon VPC Traffic Mirroring.

#### What type of appliances are supported with Amazon VPC traffic mirroring?

-  Customers can either use open source tools or choose from a wide-range of monitoring solution available on AWS Marketplace. Traffic mirroring allows customers to stream replicated traffic to any network packet collector/broker or analytics tool, without requiring them to install vendor-specific agents.

#### How is Amazon VPC traffic mirroring different from Amazon VPC flow logs?

Amazon VPC flow logs allow customers to collect, store, and analyze network flow logs. The information captured in flow logs includes information about allowed and denied traffic, source and destination IP addresses, ports, protocol number, packet and byte counts, and an action (accept or reject). You can use this feature to troubleshoot connectivity and security issues and to make sure that the network access rules are working as expected.

Amazon VPC traffic mirroring, provides deeper insight into network traffic by allowing you to analyze actual traffic content, including payload, and is targeted for use-cases when you need to analyze the actual packets to determine the root cause a performance issue, reverse-engineer a sophisticated network attack, or detect and stop insider abuse or compromised workloads.

### Amazon VPC and EC2

[Open all](#)

#### Within which Amazon EC2 region(s) is Amazon VPC available?

Amazon VPC is currently available in multiple [Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) in all Amazon EC2 regions.

#### Can a VPC span multiple Availability Zones?

-  Yes. 

#### Can a subnet span Availability Zones?

-  No. A subnet must reside within a single Availability Zone.

#### How do I specify which Availability Zone my Amazon EC2 instances are launched in?

-  When you launch an Amazon EC2 instance, you must specify the subnet in which to launch the instance. The instance will be launched in the Availability Zone associated with the specified subnet.

#### How do I determine which Availability Zone my subnets are located in?

-  When you create a subnet you must specify the Availability Zone in which to place the subnet. When using the VPC Wizard, you can select the subnet's Availability Zone in the wizard confirmation screen. When using the API or the CLI you can specify the Availability Zone for the subnet as you create the subnet. If you don’t specify an Availability Zone, the default "No Preference" option will be selected and the subnet will be created in an available Availability Zone in the region.

#### Am I charged for network bandwidth between instances in different subnets?

-  If the instances reside in subnets in different Availability Zones, you will be charged \$0.01 per GB for data transfer.

#### When I call DescribeInstances(), do I see all of my Amazon EC2 instances, including those in EC2-Classic and EC2-VPC?

-  Yes. DescribeInstances() will return all running Amazon EC2 instances. You can differentiate EC2-Classic instances from EC2-VPC instances by an entry in the subnet field. If there is a subnet ID listed, the instance is within a VPC.

#### When I call DescribeVolumes(), do I see all of my Amazon EBS volumes, including those in EC2-Classic and EC2-VPC?

-  Yes. DescribeVolumes() will return all your EBS volumes.

#### How many Amazon EC2 instances can I use within a VPC?

For instances that require IPv4 addressing, you can run any number of Amazon EC2 instances within a VPC, so long as your VPC is appropriately sized to have an IPv4 address assigned to each instance. You are initially limited to launching 20 Amazon EC2 instances at any one time and a maximum VPC size of /16 (65,536 IPs). If you would like to increase these limits, please [complete the following form](/contact-us/vpc-request/). For IPv6 only instances, the VPC size of /56 provides you the ability to launch virtually unlimited number of Amazon EC2 instances.

#### Can I use my existing AMIs in Amazon VPC?

You can use AMIs in Amazon VPC that are registered within the same region as your VPC. For example, you can use AMIs registered in us-east-1 with a VPC in us-east-1. More information is available in the [](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)Amazon EC2 Region and Availability Zone FAQ.

#### Can I use my existing Amazon EBS snapshots?

Yes, you may use Amazon EBS snapshots if they are located in the same region as your VPC. More details are available in the [Amazon EC2 Region and Availability Zone FAQ.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)

#### Can I boot an Amazon EC2 instance from an Amazon EBS volume within Amazon VPC?

-  Yes, however, an instance launched in a VPC using an Amazon EBS-backed AMI maintains the same IP address when stopped and restarted. This is in contrast to similar instances launched outside a VPC, which get a new IP address. The IP addresses for any stopped instances in a subnet are considered unavailable.

#### Can I employ Amazon CloudWatch within Amazon VPC?

-  Yes.

#### Can I employ Auto Scaling within Amazon VPC?

-  Yes. 

#### Can I launch Amazon EC2 Cluster Instances in a VPC?

-  Yes. Cluster instances are supported in Amazon VPC, however, not all instance types are available in all regions and Availability Zones.

#### What are instance hostnames?

-  When you launch an instance, it is assigned a hostname. There are two options available, an IP based name or a Resource based name, and this parameter is configurable at instance launch. The IP based name uses a form of the Private IPv4 address while the Resource based name uses a form of the instance-id.

#### Can I change the instance hostname of my Amazon EC2 instance?

-  Yes, you can change the hostname of an instance form IP based to Resource based or vice versa by stopping the instance and then changing the resource based naming options.

#### Can I use the instance hostnames as DNS hostnames?

-  Yes, the instance hostname can be used as DNS hostnames. For instances launched in an IPv4-only or dual-stack subnet, the IP based name always resolves to the Private IPv4 address on the primary network interface of the instance and this cannot be turned off. Additionally, the Resource based name can be configured to resolve to either the Private IPv4 address on the primary network interface, or the first IPv6 GUA on the primary network interface, or both. For instances launched in an IPv6-only subnet, the Resource based name will be configured to resolve to the first IPv6 GUA on the primary network interface. 

### Default VPCs

[Open all](#)

#### What is a default VPC?

-  A default VPC is a logically isolated virtual network in the AWS cloud that is automatically created for your AWS account the first time you provision Amazon EC2 resources. When you launch an instance without specifying a subnet-ID, your instance will be launched in your default VPC.

#### What are the benefits of a default VPC?

-  When you launch resources in a default VPC, you can benefit from the advanced networking functionalities of Amazon VPC (EC2-VPC) with the ease of use of Amazon EC2 (EC2-Classic). You can enjoy features such as changing security group membership on the fly, security group egress filtering, multiple IP addresses, and multiple network interfaces without having to explicitly create a VPC and launch instances in the VPC.

#### What accounts are enabled for default VPC?

If your AWS account was created after March 18, 2013 your account may be able to launch resources in a default VPC. See this [Forum Announcement](https://forums.aws.amazon.com/ann.jspa?annID=1875) to determine which regions have been enabled for the default VPC feature set. Also, accounts created prior to the listed dates may utilize default VPCs in any default VPC enabled region in which you’ve not previously launched EC2 instances or provisioned Amazon Elastic Load Balancing, Amazon RDS, Amazon ElastiCache, or Amazon Redshift resources.

#### Will I need to know anything about Amazon VPC in order to use a default VPC?

-  No. You can use the AWS Management Console, AWS EC2 CLI, or the Amazon EC2 API to launch and manage EC2 instances and other AWS resources in a default VPC. AWS will automatically create a default VPC for you and will create a default subnet in each Availability Zone in the AWS region. Your default VPC will be connected to an Internet gateway and your instances will automatically receive public IP addresses, just like EC2-Classic.

#### What are the differences between instances launched in EC2-Classic and EC2-VPC?

See [Differences between EC2-Classic and EC2-VPC](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-vpc.html) in the EC2 User Guide.

#### Do I need to have a VPN connection to use a default VPC?

-  No. Default VPCs are attached to the Internet and all instances launched in default subnets in the default VPC automatically receive public IP addresses. You can add a VPN connection to your default VPC if you choose.

#### Can I create other VPCs and use them in addition to my default VPC?

-  Yes. To launch an instance into nondefault VPCs you must specify a subnet-ID during instance launch.

#### Can I create additional subnets in my default VPC, such as private subnets?

-  Yes. To launch into nondefault subnets, you can target your launches using the console or the --subnet option from the CLI, API, or SDK.

#### How many default VPCs can I have?

-  You can have one default VPC in each AWS region where your Supported Platforms attribute is set to "EC2-VPC".

#### How many default subnets are in a default VPC?

-  One default subnet is created for each Availability Zone in your default VPC.

#### Can I specify which VPC is my default VPC?

-  Not at this time.

#### Can I specify which subnets are my default subnets?

-  Not at this time.

#### Can I delete a default VPC?

-  Yes, you can delete a default VPC. Once deleted, you can create a new default VPC directly from the VPC Console or by using the CLI. This will create a new default VPC in the region. This does not restore the previous VPC that was deleted.

#### Can I delete a default subnet?

-  Yes, you can delete a default subnet. Once deleted, you can create a new default subnet in the availability zone by using the CLI or SDK. This will create a new default subnet in the availability zone specified. This does not restore the previous subnet that was deleted.

#### I have an existing EC2-Classic account. Can I get a default VPC?

-  The simplest way to get a default VPC is to create a new account in a region that is enabled for default VPCs, or use an existing account in a region you've never been to before, as long as the Supported Platforms attribute for that account in that region is set to "EC2-VPC".

#### I really want a default VPC for my existing EC2 account. Is that possible?

Yes, however, we can only enable an existing account for a default VPC if you have no EC2-Classic resources for that account in that region. Additionally, you must terminate all non-VPC provisioned Elastic Load Balancers, Amazon RDS, Amazon ElastiCache, and Amazon Redshift resources in that region. After your account has been configured for a default VPC, all future resource launches, including instances launched via Auto Scaling, will be placed in your default VPC. To request your existing account be setup with a default VPC, please go to *Account and Billing* -\> *Service: Account* -\> *Category: Convert EC2 Classic to VPC* and raise a request. We will review your request, your existing AWS services and EC2-Classic presence and guide you through the next steps.

#### How are IAM accounts impacted by default VPC?

-  If your AWS account has a default VPC, any IAM accounts associated with your AWS account use the same default VPC as your AWS account.

### EC2 Classic

[Open all](#)

#### What is EC2-Classic?

-  EC2-Classic is a flat network that we launched with EC2 in the summer of 2006. With EC2-Classic, your instances run in a single, flat network that you share with other customers. Over time, inspired by our customers’ evolving needs, we launched Amazon Virtual Private Cloud (VPC) in 2009 to allow you to run instances in a virtual private cloud that's logically isolated to your AWS account. Today, while majority of our customers use Amazon VPC, we have a few customers who still use EC2-Classic.

#### What’s changing?

-  We are retiring Amazon EC2-Classic on August 15, 2022 and we need you to migrate any EC2 instances and other AWS resources running on EC2-Classic to Amazon VPC before this date. The following section provides more information on the EC2-Class retirement as well as tools and resources to assist you in migration.

#### How is my account impacted by the retirement of EC2-Classic?

You are affected by this change only if you have EC2-Classic enabled on your account in any of the AWS regions. You can use the console or the [describe-account-attributes](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-account-attributes.html) command to check whether you have EC2-Classic enabled for an AWS region; please refer to this [document](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-classic-platform.html#ec2-supported-platforms) for more details.  
  
If you do not have any active AWS resources running on EC2-Classic in any region, we request you to turn off EC2-Classic from your account for that region. Turning off EC2-Classic in a region allows you to launch Default VPC there. To do so go to the AWS Support Center at [console.aws.amazon.com/support](https://console.aws.amazon.com/support), choose “Create case” and then “Account and billing support”, for “Type” choose “Account”, for “Category” choose “Convert EC2 Classic to VPC”, fill in the other details as required, and choose “Submit”.  
  
We will automatically turn off EC2-Classic from your account on October 30, 2021 for any AWS region where you have not had any AWS resources (EC2 Instances, Amazon Relational Database, AWS Elastic Beanstalk, Amazon Redshift, AWS Data Pipeline, Amazon EMR, AWS OpsWorks) on EC2-Classic since January 1, 2021.  
  
On the other hand, if you have AWS resources running on EC2-Classic, we request you to plan their migration to Amazon VPC as soon as possible. You will not be able to launch any instances or AWS services on EC2-Classic platform beyond August 15, 2022. Any workloads or services in running state will gradually loose access to all AWS services on EC2-Classic as we retire them beginning August 16, 2022.

You can find the migration guides for your AWS resources in subsequent question.

#### What are the benefits of moving from EC2-Classic to Amazon VPC?

Amazon VPC gives you complete control over your virtual network environment on AWS, logically isolated to your AWS account. In the EC2-Classic environment, your workloads are sharing a single flat network with other customers. The Amazon VPC environment offers many other advantages over the EC2-Classic environment including the ability to select your own IP address space, public and private subnet configuration, and management of route tables and network gateways. All services and instances currently available in EC2-Classic have comparable services available in the Amazon VPC environment. Amazon VPC also offers a much wider and latest generation of instances than EC2-Classic. Further information about Amazon VPC is available [in this link](/vpc/).

#### How do I migrate from EC2-Classic to VPC?

To help you migrate your resources, we have published playbooks and built solutions that you will find below. To migrate, you must recreate your EC2-Classic resources in your VPC. First, you can use this [](https://github.com/aws-samples/ec2-classic-resource-finder)[](/blogs/aws/ec2-classic-is-retiring-heres-how-to-prepare/)[](/blogs/aws/ec2-classic-is-retiring-heres-how-to-prepare/)script to identify all resources provisioned in EC2-Classic across all regions in an account. You can then use the migration guide for the relevant AWS resources from below:

- [Instances and Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-migrate.html)
- [Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/migrate-classic-load-balancer.html#migrate-step-by-step-classiclink)
- [Amazon Relational Database Service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.html#USER_VPC.VPC2VPC)
- [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/vpc-ec2migration.html)
- [Amazon Redshift for migration of DC1 Clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-migrating-from-dc1-to-dc2) and [for other node types](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-upgrading-ds2-cluster-ec2-classic-to-ec2-vpc)
- [AWS Data Pipeline](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-resources-vpc.html#dp-ec2classic-to-vpc) 
- [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-vpc-subnet.html) 
- [AWS OpsWorks](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/aws-opsworks.html)

Besides the above migration guides, we are also offering a highly automated lift-and-shift (rehost) solution, AWS Application Migration Service (AWS MGN), that simplifies, expedites, and reduces the cost of migrating applications. You can find relevant resources about AWS MGN here:

- [Getting started with AWS Application Migration Service](/application-migration-service/) 
- [AWS Application Migration Service on-demand technical training](https://www.aws.training/Details/eLearning?id=71732)
- [Documentation to dive deep into AWS Application Migration Service Features and Functionalities](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html)
- [Service Architecture and Network Architecture video](https://www.youtube.com/watch?v=ao8geVzmmRo)

For simple individual EC2 instance migrations from EC2-Classic to VPC, besides AWS MGN or the [Instances Migration Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/vpc-migrate.html), you can also use the “AWSSupport-MigrateEC2 ClassicToVPC“ runbook from ”AWS Systems Manager \> Automation“. This runbooks automates the steps that are required to migrate an instance from EC2-Classic to VPC by creating an AMI of the instance in EC2-Classic, creating a new instance from the AMI in VPC, and optionally terminating the EC2-Classic instance.

If you have any questions or concerns, you can contact the AWS Support Team via [AWS Premium Support](/support).  
  
Please Note: If you have AWS resources running on EC2-Classic in multiple AWS regions, we recommend that you turn off EC2-Classic for each of those regions as soon as you have migrated all your resources to VPC in them.

#### What are the important dates I should be aware of?

We will take the following two actions ahead of the August 15, 2022 retirement date:

- We will stop issuing 3-year reserved instances (RI) and 1-year RI for the EC2-Classic environment on Oct 30, 2021. RIs already in place on the EC2-Classic environment will not be affected at this time. RIs that are set to expire after 8/15/2022 will need to be modified to use the Amazon VPC environment for the remaining period of the lease. For information on how to modify your RIs, please visit our [document](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-modifying.html).
- On Aug 15, 2022, we will no longer allow the creation of new instances (Spot or on-demand) or other AWS services in the EC2-Classic environment. Any workloads or services in running state will gradually loose access to all AWS services on EC2-Classic as we retire them beginning August 16, 2022.

### Elastic Network Interfaces

[Open all](#)

#### Can I attach or detach one or more network interfaces to an EC2 instance while it’s running?

-  Yes.

#### Can I attach a network interface in one Availability Zone to an instance in another Availability Zone?

-  Network interfaces can only be attached to instances residing in the same Availability Zone.

#### Can I attach a network interface in one VPC to an instance in another VPC?

Network interfaces can only be attached to instances in VPCs in the same account.

#### Can I use Elastic Network Interfaces as a way to host multiple websites requiring separate IP addresses on a single instance?

-  Yes, however, this is not a use case best suited for multiple interfaces. Instead, assign additional private IP addresses to the instance and then associate EIPs to the private IPs as needed.

#### Can I detach the primary interface (eth0) on my EC2 instance?

-  No. You can attach and detach secondary interfaces (eth1-ethn) on an EC2 instance, but you can’t detach the eth0 interface.

### Peering Connections

[Open all](#)

#### Can I create a peering connection to a VPC in a different region?

-  Yes. Peering connections can be created with VPCs in different regions. Inter-region VPC peering is available globally in all commercial regions (excluding China).

#### Can I peer my VPC with a VPC belonging to another AWS account?

-  Yes, assuming the owner of the other VPC accepts your peering connection request.

#### How much do VPC peering connections cost?

There is no charge for creating VPC peering connections, however, data transfer across peering connections is charged. See the Data Transfer section of the [EC2 Pricing page](/ec2/pricing/) for data transfer rates.

#### Do I need an Internet Gateway to use peering connections?

-  No. VPC peering connections do not require an Internet Gateway.

#### Is VPC peering traffic within the region encrypted?

-  No. Traffic between instances in peered VPCs remains private and isolated – similar to how traffic between two instances in the same VPC is private and isolated.

#### If I delete my side of a peering connection, will the other side still have access to my VPC?

-  No. Either side of the peering connection can terminate the peering connection at any time. Terminating a peering connection means traffic won’t flow between the two VPCs.

#### If I peer VPC A to VPC B and I peer VPC B to VPC C, does that mean VPCs A and C are peered?

-  No. Transitive peering relationships are not supported.

#### What if my peering connection goes down?

AWS uses the existing infrastructure of a VPC to create a VPC peering connection; it is neither a gateway nor a VPN connection, and does not rely on a separate piece of physical hardware. There is no single point of failure for communication or a bandwidth bottleneck.

Inter-Region VPC Peering operates on the same horizontally scaled, redundant, and highly available technology that powers VPC today. Inter-Region VPC Peering traffic goes over the AWS backbone that has in-built redundancy and dynamic bandwidth allocation. There is no single point of failure for communication.

If an Inter-Region peering connection does go down, the traffic will not be routed over the internet.

#### Are there any bandwidth limitations for peering connections?

Bandwidth between instances in peered VPCs is no different than bandwidth between instances in the same VPC. Read more about [Placement Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html).

#### Is Inter-Region VPC Peering traffic encrypted?

-  Traffic is encrypted using modern AEAD (Authenticated Encryption with Associated Data) algorithms. Key agreement and key management is handled by AWS.

#### How do DNS translations work with Inter-Region VPC Peering?

-  By default, a query for a public hostname of an instance in a peered VPC in a different region will resolve to a public IP address. Route 53 private DNS can be used to resolve to a private IP address with Inter-Region VPC Peering.

#### Can I reference security groups across an Inter-Region VPC Peering connection?

-  No. Security groups cannot be referenced across an Inter-Region VPC Peering connection.

#### Does Inter-Region VPC Peering support IPv6?

-  Yes. Inter-Region VPC Peering supports IPv6.

#### Can Inter-Region VPC Peering be used with EC2-Classic Link?

-  No. Inter-Region VPC Peering cannot be used with EC2-ClassicLink.

### ClassicLink

[Open all](#)

#### What is ClassicLink?

-  Amazon Virtual Private Cloud (VPC) ClassicLink allows EC2 instances in the EC2-Classic platform to communicate with instances in a VPC using private IP addresses. To use ClassicLink, enable it for a VPC in your account, and associate a Security Group from that VPC with an instance in EC2-Classic. All the rules of your VPC Security Group will apply to communications between instances in EC2-Classic and instances in the VPC. 

#### What does ClassicLink cost?

There is no additional charge for using ClassicLink; however, existing cross Availability Zone data transfer charges will apply. For more information, consult the [EC2 pricing page](/ec2/pricing/).

#### How do I use ClassicLink?

-  In order to use ClassicLink, you first need to enable at least one VPC in your account for ClassicLink. Then you associate a Security Group from the VPC with the desired EC2-Classic instance. The EC2-Classic instance is now linked to the VPC and is a member of the selected Security Group in the VPC. Your EC2-Classic instance cannot be linked to more than one VPC at the same time.

#### Does the EC2-Classic instance become a member of the VPC?

-  The EC2-Classic instance does not become a member of the VPC. It becomes a member of the VPC Security Group that was associated with the instance. All the rules and references to the VPC Security Group apply to communication between instances in EC2-Classic instance and resources within the VPC.

#### Can I use EC2 public DNS hostnames from my EC2-Classic and EC2-VPC instances to address each other, in order to communicate using private IP?

-  No. The EC2 public DNS hostname will not resolve to the private IP address of the EC2-VPC instance when queried from an EC2-Classic instance, and vice-versa.

#### Are there any VPCs for which I cannot enable ClassicLink?

-  Yes. ClassicLink cannot be enabled for a VPC that has a Classless Inter-Domain Routing (CIDR) that is within the 10.0.0.0/8 range, with the exception of 10.0.0.0/16 and 10.1.0.0/16. In addition, ClassicLink cannot be enabled for any VPC that has a route table entry pointing to the 10.0.0.0/8 CIDR space to a target other than "local".

#### Can traffic from an EC2-Classic instance travel through the Amazon VPC and egress through the Internet gateway, virtual private gateway, or to peered VPCs?

-  Traffic from an EC2-Classic instance can only be routed to private IP addresses within the VPC. They will not be routed to any destinations outside the VPC, including Internet gateway, virtual private gateway, or peered VPC destinations.

#### Does ClassicLink affect the access control between the EC2-Classic instance, and other instances that are in the EC2-Classic platform?

-  ClassicLink does not change the access control defined for an EC2-Classic instance through its existing Security Groups from the EC2-Classic platform.

#### Will ClassicLink settings on my EC2-Classic instance persist through stop/start cycles?

-  The ClassicLink connection will not persist through stop/start cycles of the EC2-Classic instance. The EC2-Classic instance will need to be linked back to a VPC after it is stopped and started. However, the ClassicLink connection will persist through instance reboot cycles.

#### Does ClassicLink allow EC2-Classic Security Group rules to reference VPC Security Groups, or vice versa?

-  ClassicLink does not allow EC2-Classic Security Group rules to reference VPC Security Groups, or vice versa.

### AWS PrivateLink

[Open all](#)

#### What is AWS PrivateLink?

-  AWS PrivateLink enables customers to access services hosted on AWS in a highly available and scalable manner, while keeping all the network traffic within the AWS network. Service users can use this to privately access services powered by PrivateLink from their Amazon Virtual Private Cloud (VPC) or their on-premises, without using public IPs, and without requiring the traffic to traverse across the Internet. Service owners can register their Network Load Balancers to PrivateLink services and provide the services to other AWS customers.

#### How can I use AWS PrivateLink?

As a service user, you will need to create interface type VPC endpoints for services that are powered by PrivateLink. These service endpoints will appear as Elastic Network Interfaces (ENIs) with private IPs in your VPCs. Once these endpoints are created, any traffic destined to these IPs will get privately routed to the corresponding AWS services.

As a service owner, you can onboard your service to AWS PrivateLink by establishing a Network Load Balancer (NLB) to front your service and create a PrivateLink service to register with the NLB. Your customers will be able to establish endpoints within their VPC to connect to your service after you whitelisted their accounts and IAM roles.

#### Which services are currently available on AWS PrivateLink?

The following AWS services support this feature: Amazon Elastic Compute Cloud (EC2), Elastic Load Balancing (ELB), Kinesis Streams, Service Catalog, EC2 Systems Manager, Amazon SNS, and AWS DataSync. Many SaaS solutions support this feature as well. Please visit [AWS Marketplace](/marketplace) for more SaaS products powered by AWS PrivateLink.

#### Can I privately access services powered by AWS PrivateLink over AWS Direct Connect?

-  Yes. The application in your on-premises can connect to the service endpoints in Amazon VPC over AWS Direct Connect. The service endpoints will automatically direct the traffic to AWS services powered by AWS PrivateLink.

### Additional Questions

[Open all](#)

#### Can I use the AWS Management Console to control and manage Amazon VPC?

-  Yes. You can use the AWS Management Console to manage Amazon VPC objects such as VPCs, subnets, route tables, Internet gateways, and IPSec VPN connections. Additionally, you can use a simple wizard to create a VPC.

#### How many VPCs, subnets, Elastic IP addresses, and internet gateways can I create?

See the Amazon VPC [user guide](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Appendix_Limits.html) for information on VPC limits.

#### Can I obtain AWS support with Amazon VPC?

Yes. [Click here](/premiumsupport/) for more information on AWS support.

#### Can I use ElasticFox with Amazon VPC?

[ElasticFox](https://sourceforge.net/projects/elasticfox/) is no longer officially supported for managing your Amazon VPC. Amazon VPC support is available via the AWS APIs, command line tools, and the AWS Management Console, as well as a variety of third-party utilities.

### VPC Encryption Controls

[Open all](#)

#### What is VPC Encryption Controls?

A security and compliance feature that provides centralized control to monitor and enforce encryption of traffic flows within and across VPCs in a region. For further information please read documentation [here](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html).

#### What are the two modes of operation?

Monitor mode (for visibility, assessment and initiate migration) and Enforce mode (for preventing unencrypted traffic).

#### Who is this feature designed for?

Security administrators and cloud architects, especially in industries requiring compliance with standards like HIPAA, FedRamp, and PCI DSS.

#### How does VPC Encryption Controls work?

It uses both application-layer encryption and AWS Nitro system hardware's built-in encryption capabilities to ensure encryption enforcement.

#### What does Monitor mode allow me to do?

Monitor mode provides visibility into encryption status of traffic flows, helps identify non-compliant resources, and populates VPC flow logs with encryption status information. Resources such as Network Load Balancers, Application Load Balancers, Fargate clusters, EKS Control Plane will automatically and gradually migrate to hardware that natively supports encryption once you turn on the monitor mode.

#### How can I track encryption status in Monitor mode?

Through:

- VPC flow logs with the encryption-status field
- Console dashboard
- GetVpcResourcesBlockingEncryptionEnforcement command

#### Do existing flow logs automatically show encryption status?

No, you need to create new flow logs adding the encryption-status field manually. It is also recommended to add the traffic-path and flow-direction fields.

#### What happens when Enforce mode is enabled?

Once a VPC is in Enforce mode it prevents the creation or attachment of resources that allow unencrypted traffic within the VPC boundary. You will be blocked from running instances that don’t support native nitro encryption.

#### Can I enable Enforce mode on an existing VPC immediately?

No, you must first:

- Enable Monitor mode
- Identify non-compliant resources
- Modify or create exclusions for non-compliant resources
- Then switch to Enforce mode

#### What if I need to run non-compliant resources in Enforce mode?

You must create an exclusion for that resource from the eight supported exclusion types. Other unsupported resources must be migrated out of the VPC or deleted before turning on enforce mode. Resources that are supported by Encryption Controls must be migrated to encryption [compliant instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html#encryption-transit) before turning on enforce.

#### How do I transition from Monitor to Enforce mode?

Follow these steps:

- Review Flow Logs and resource compliance
- Plan necessary resource migrations
- Configure required exclusions when switching to Enforce mode

#### Can I switch back from Enforce to Monitor mode?

Yes, except in the scenario where you have VPC peering established between two VPCs without any exclusions. In this case, you must delete the VPC peering between the two VPCs and then move to monitor mode.

#### How do I verify my VPC is ready for Enforce mode?

Use the GetVpcResourcesBlockingEncryptionEnforcement command to identify any resources that would block enforcement. Alternatively, you can use console to find resources that are unencrypted.

#### What are the supported exclusions?

There are eight supported exclusions:

- Internet Gateway
- NAT Gateway
- Egress-only Internet Gateway
- VPC Peering connections to encryption un-enforced VPCs
- Virtual Private Gateway
- Lambda functions
- VPC Lattice
- Elastic File System

#### What are the possible encryption status values in VPC Flow Logs?

0: not encrypted  
1: nitro-encrypted  
2: application-encrypted  
3: both nitro AND application encrypted  
(-): Unknown/VPC encryption controls off

#### How can I encrypt traffic between my VPCs in a region?

To encrypt traffic between your VPCs that have encryption controls enabled, you can use VPC Peering or Transit Gateway. When using Transit Gateway, you need to turn on encryption support explicitly using console or modify-transit-gateway command. There are no separate charges for turning on Encryption on Transit Gateway, but you incur standard VPC Encryption Controls charges for all the VPCs associated with the Transit Gateway (regardless whether you turn on Encryption Controls on these VPCs).

#### How do I enable encryption on a Transit Gateway?

Use the 'modify-transit-gateway' command or enable it through the AWS Console. You must enable encryption support on a Transit Gateway explicitly to encrypt traffic between your VPCs that have encryption controls turned on.

#### How does Transit Gateway support encryption with VPC Encryption Controls?

Enabling encryption on existing TGW is non-disruptive to existing traffic flows and migration of VPC attachments to encrypted lanes will happen seamlessly and automatically. You can enable encryption support on a Transit Gateway to encrypt traffic between your VPCs. Traffic between two VPCs in enforce mode (without exclusions) is end-to-end encrypted via the TGW. Encryption on Transit Gateway also allows you to connect two VPCs that are in different Encryption Controls modes.

#### Will traffic be encrypted end-to-end between VPCs connected via TGW with Encryption Support enabled?

It depends. Traffic between two VPCs in enforce mode (without exclusions) is end-to-end encrypted via the TGW. Encryption on Transit Gateway also allows you to connect two VPCs that are in different Encryption Controls modes. You should use it when you want to enforce encryption controls in a VPC that is connected to a non-encryption-enforced VPC. In such a scenario, all your traffic inside your encryption-enforced VPC, including the inter-VPC traffic is encrypted. The inter-VPC traffic is encrypted between the resources in the encryption-enforced VPC and the Transit Gateway. Beyond that, encryption depends on the resources to which the traffic is going to in the non-enforced VPC and is not guaranteed to be encrypted (since the VPC is not in enforce mode). All VPCs must be in the same region.

#### Can I connect an encryption-enforced VPC to a non-enforced VPC through TGW?

Yes, traffic will remain encrypted until it reaches the TGW attachment in the non-enforced VPC. The traffic remains encrypted from the source until the TGW attachment in the destination VPC, regardless of the destination VPC's encryption status.

#### How do I migrate existing TGW connections to use encryption?

Enable encryption on the TGW while maintaining existing connections - the transition is handled automatically. Enabling encryption on TGW is non- disruptive to existing traffic flows.

#### Can I gradually migrate VPCs to encryption while using TGW?

Yes, TGW supports incremental migration by handling both encrypted and unencrypted traffic during the transition.

#### Can I connect VPCs belonging to different accounts using Private Link (VPC Endpoints) and be guaranteed that all traffic is encrypted when using VPC Encryption Controls?

No. Private Link with VPC Encryption Controls is only supported for AWS Services. VPC Endpoints to non-AWS Services cannot stay in VPCs where you want to enforce encryption. You would have to delete those endpoints before proceeding to Enforce mode on the VPC. VPCs running in enforce mode can be connected VPC Peering or Transit Gateway to guarantee end-to-end encryption.

## Getting started with Amazon VPC

[](/vpc/details/)

Getting started

## Learn more about Amazon VPC

Visit the product detail page

![](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/product-categories/migration/transfer/approved/images/9a605cb9-314c-47f4-a88a-ee7d5ecee185.8a802f5c73264d91b9decdcf86b6ad8edc7bf105.jpeg)

[](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html)

Getting started

## Ready to get started?

Sign up

![](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/product-categories/networking/approved/images/639ddfa6-eb09-4561-a2e1-4d2d80814a15.d2a1f4455448ddf1d5d8151790f43b818ddcce18.jpeg)

[](/contact-us/)

Contact us

## Have more questions?

Contact us

![](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/product-categories/networking/approved/images/2c50fb03-8156-4fb1-9937-1dfed809a9e2.9c07ca48d05bef0e3fe799d218f134c44c59cbf3.jpeg)

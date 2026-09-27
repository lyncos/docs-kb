---
title: Shared Responsibility Model
description: AWS Cloud Security
product: Amazon Bedrock AgentCore
section: References / aws.amazon.com
source_url: https://aws.amazon.com/compliance/shared-responsibility-model
fetched: '2026-09-26'
tags:
- agent-registry
- agentcore
- aws-amazon-com
- reference
- related
referenced_by:
- data-protection.md
- identity-data-protection.md
- registry-data-protection.md
- runtime-get-started-code-deploy.md
- security.md
- storage-encryption.md
conversion: pandoc
---

AWS Cloud Security

- [Security Services](/products/security/)
- Use Cases
- Compliance
- Data Protection
- [Blog](/security/blog/)
- Partners
- Resources

# Shared Responsibility Model

## Overview

Security and Compliance is a shared responsibility between AWS and the customer. This shared model can help relieve the customer’s operational burden as AWS operates, manages and controls the components from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates. The customer assumes responsibility and management of the guest operating system (including updates and security patches), other associated application software as well as the configuration of the AWS provided security group firewall. Customers should carefully consider the services they choose as their responsibilities vary depending on the services used, the integration of those services into their IT environment, and applicable laws and regulations. The nature of this shared responsibility also provides the flexibility and customer control that permits the deployment. As shown in the chart below, this differentiation of responsibility is commonly referred to as Security “of” the Cloud versus Security “in” the Cloud.

![Diagram illustrating the AWS shared responsibility model for security and compliance. The chart describes the division of security responsibilities between the customer (security 'in' the cloud: customer data, platform, applications, OS and firewall configuration, encryption, and traffic protection) and AWS (security 'of' the cloud: software, compute, storage, database, networking, hardware/infrastructure, regions, availability zones, edge locations).](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/product-categories/security-identity-compliance/compliance/approved/images/7a404923-5572-409c-b30e-6d44706bcd89.92c57224d8acd09bf44d94bc25db5c58419a8941.jpeg)

## Understanding the AWS Shared Responsibility Model

### AWS responsibility “Security of the Cloud”

AWS is responsible for protecting the infrastructure that runs all of the services offered in the AWS Cloud. This infrastructure is composed of the hardware, software, networking, and facilities that run AWS Cloud services.

### Customer responsibility “Security in the Cloud”

Customer responsibility will be determined by the AWS Cloud services that a customer selects. This determines the amount of configuration work the customer must perform as part of their security responsibilities. For example, a service such as Amazon Elastic Compute Cloud (Amazon EC2) is categorized as Infrastructure as a Service (IaaS) and, as such, requires the customer to perform all of the necessary security configuration and management tasks. Customers that deploy an Amazon EC2 instance are responsible for management of the guest operating system (including updates and security patches), any application software or utilities installed by the customer on the instances, and the configuration of the AWS-provided firewall (called a security group) on each instance. For abstracted services, such as Amazon S3 and Amazon DynamoDB, AWS operates the infrastructure layer, the operating system, and platforms, and customers access the endpoints to store and retrieve data. Customers are responsible for managing their data (including encryption options), classifying their assets, and using IAM tools to apply the appropriate permissions.

This customer/AWS shared responsibility model also extends to IT controls. Just as the responsibility to operate the IT environment is shared between AWS and its customers, so is the management, operation and verification of IT controls shared. AWS can help relieve customer burden of operating controls by managing those controls associated with the physical infrastructure deployed in the AWS environment that may previously have been managed by the customer. As every customer is deployed differently in AWS, customers can take advantage of shifting management of certain IT controls to AWS which results in a (new) distributed control environment. Customers can then use the AWS control and compliance documentation available to them to perform their control evaluation and verification procedures as required. Below are examples of controls that are managed by AWS, AWS Customers and/or both.

### Inherited Controls

Controls which a customer fully inherits from AWS.

- Physical and Environmental controls

### Shared Controls

Controls which apply to both the infrastructure layer and customer layers, but in completely separate contexts or perspectives. In a shared control, AWS provides the requirements for the infrastructure and the customer must provide their own control implementation within their use of AWS services. Examples include:

- Patch Management – AWS is responsible for patching and fixing flaws within the infrastructure, but customers are responsible for patching their guest OS and applications.
- Configuration Management – AWS maintains the configuration of its infrastructure devices, but a customer is responsible for configuring their own guest operating systems, databases, and applications.
- Awareness & Training - AWS trains AWS employees, but a customer must train their own employees.

### Customer Specific

Controls which are solely the responsibility of the customer based on the application they are deploying within AWS services. Examples include:

- Service and Communications Protection or Zone Security which may require a customer to route or zone data within specific security environments.

## Applying the AWS Shared Responsibility Model in Practice

Once a customer understands the AWS Shared Responsibility Model and how it generally applies to operating in the cloud, they must determine how it applies to their use case. Customer responsibility varies based on many factors, including the AWS services and Regions they choose, the integration of those services into their IT environment, and the laws and regulations applicable to their organization and workload.

The following exercises can help customers in determining the distribution of responsibility based on specific use case:

- [Get started](#get-started--1e0ixp6)
  9

### Get started

[Open all](#)

#### Consider

![](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/product-categories/security-identity-compliance/compliance/approved/images/icons/financial-resource-center_segment-sec-ocie-audit-guide_illustration.da5b6e4c5584b601eeb7ad9b0d4ff8fd38a29f91.png)

Consider employing the [AWS Cloud Adoption Framework (CAF)](/professional-services/CAF/) and [Well-Architected best practices](/architecture/well-architected/) to plan and execute your digital transformation at scale.

#### Review

![](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/product-categories/security-identity-compliance/compliance/approved/images/icons/financial-resource-center_segment-coalfire-audit-guide_illustration.e199e67fefcfe93fc8ef1b3f0edd36eb9c95af45.png)

Review the security functionality and configuration options of individual AWS services within the security chapters of [AWS service documentation](https://docs.aws.amazon.com/security/).

#### Determine

![](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/product-categories/security-identity-compliance/compliance/approved/images/icons/detect.23d74ce4a6f4313042afd3ea780c8e04acfab5e4.png) 

Determine external and internal security and related compliance requirements and objectives, and consider industry frameworks like the [NIST Cybersecurity Framework (CSF)](https://www.nist.gov/cyberframework) and [ISO](/compliance/iso-certified/).

#### Evaluate

![](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/product-categories/security-identity-compliance/compliance/approved/images/icons/page-illo_remediate.72dfe2427cb3d0614b47ee07af1667d11ca11b9e.png)

Evaluate the [AWS Security, Identity, and Compliance services](/products/security/) to understand how they can be used to help meet your security and compliance objectives.

#### Review

![](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/product-categories/security-identity-compliance/compliance/approved/images/icons/page-illo_prevent.50ef5da5df5b591e7a53103e804e187928082b35.png)

Review [third-party audit attestation documents](/artifact/) to determine inherited controls and what required controls may be remaining for you to implement in your environment.

#### Provide

![](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/product-categories/security-identity-compliance/compliance/approved/images/icons/page-illo_respond.ba7ea98554885dcd25619c3ae90f2b1c4fbbfe71.png)

Provide your internal and external audit teams with cloud-specific learning opportunities by leveraging the [Cloud Audit Academy](/compliance/auditor-learning-path/) training programs.

#### Perform

![](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/product-categories/security-identity-compliance/compliance/approved/images/icons/page-illo_vulnerability_reporting.8b12e29cbaf7b00fde6a91cbe594015b056a2269.png)

Perform a [Well-Architected Review](/well-architected-tool/) of your AWS workloads to evaluate the implementation of best practices for security, reliability, and performance.

#### Explore

![](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/product-categories/security-identity-compliance/compliance/approved/images/icons/page-illo_expert-guidance.8b4beced72cd281567d33675635cdd53113fd08d.png)

Explore [AWS Security Competency Partners](/security/partner-solutions/?partner-solutions-cards.sort-by=item.additionalFields.partnerNameLower&partner-solutions-cards.sort-order=asc&awsf.partner-solutions-filter-partner-type=*all&awsf.Filter%20Name:%20partner-solutions-filter-partner-categories=*all&awsf.partner-solutions-filter-partner-location=*all) offering expertise and proven customer success securing every stage of cloud adoption, from initial migration through ongoing day-to-day management.

#### Explore

![](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/product-categories/security-identity-compliance/compliance/approved/images/icons/page-illos_mg-use-cases_configuration_3-column_audit.7ce7019a50ab45b66b9e60b21e17345e4f043f55.png)

Explore solutions available in the [AWS Marketplace](/marketplace/solutions/security/) digital catalog with thousands of software listings from independent software vendors that enable you to find, test, buy, and deploy software that runs on AWS.

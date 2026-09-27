---
title: Data Privacy FAQs
description: AWS Cloud Security
product: Amazon Bedrock AgentCore
section: References / aws.amazon.com
source_url: https://aws.amazon.com/compliance/data-privacy-faq
fetched: '2026-09-26'
tags:
- agent-registry
- agentcore
- aws-amazon-com
- reference
- related
referenced_by:
- identity-data-protection.md
- registry-data-protection.md
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

# Data Privacy FAQs

## At AWS, customer trust is our top priority

Maintaining customer trust is an ongoing commitment. AWS continually monitors the evolving privacy regulatory and legislative landscape to identify changes and determine what tools our customers might need to meet their compliance goals. We strive to inform you of the privacy and data security policies, practices, and technologies we’ve put in place.

- [Commitments](#commitments--1yvnqhg)
  4
- [Data Privacy FAQs](#data-privacy-faqs--1yvnqhg)
  11

### Commitments

[Open all](#)

#### Access

As a customer, you maintain full control of your content that you upload to the AWS services under your AWS account, and responsibility for configuring access to AWS services and resources. We provide an advanced set of access, encryption, and logging features to help you do this effectively (e.g., [AWS Identity and Access Management](/iam/), [AWS Organizations](/organizations/) and [AWS CloudTrail](/cloudtrail/)). We also provide APIs for you to configure access control permissions for any of the services you develop or deploy in an AWS environment. We do not access or use your content for any purpose without your agreement. We do not use your content or derive information from it for marketing or advertising purposes.

#### Storage

You choose the AWS Region(s) in which your content is stored. You can replicate and back up your content in more than one AWS Region. We will not move or replicate your content outside of your chosen AWS Region(s) without your agreement.

#### Security

You choose how your content is secured. We offer you industry-leading encryption features to protect your content in transit and at rest, and we provide you with the option to manage your own encryption keys. These data protection features include:

- [Data encryption capabilities available in over 100 AWS services](/compliance/privacy-features/).
- [Flexible key management options using AWS Key Management Service (KMS)](/kms/features/#AWS_Service_Integration), allowing customers to choose whether to have AWS manage their encryption keys or keep complete control over their keys.
- Securityassurance program, using best practices for security and data protection to help you operate securely within AWS, and to make the best use of our security control environment. These security protections and control processes are independently validated by [multiple third-party independent assessments](/compliance/programs/).

#### Disclosure of customer content

We will not disclose customer content (see How does AWS classify customer information? below) unless we're required to do so to comply with the law or a valid and binding order of a government body. If a governmental body sends AWS a demand for your customer content, we will attempt to redirect the governmental body to request that data directly from you. If compelled to disclose your customer content to a government body, we will give you reasonable notice of the demand to allow you to seek a protective order or other appropriate remedy unless AWS is legally prohibited from doing so.

### Data Privacy FAQs

[Open all](#)

#### What is customer content?

We define customer content as software (including machine images), data, text, audio, video, or images that a customer or any end user transfers to us for processing, storage, or hosting by AWS services in connection with a customer's account, and any computational results that a customer or their end user derives from the foregoing through their use of AWS services. For example, customer content includes content that a customer or their end user stores in Amazon Simple Storage Service (S3). Customer content does not include account information, which we describe below. Customer content also does not include information included in resource identifiers, metadata tags, access controls, rules, usage policies, permissions, and similar items related to the management of AWS resources. AWS recommends that you do not include personally identifying, confidential, or sensitive information in these items. The terms of the [AWS Customer Agreement](/agreement/) and the [AWS Service Terms](/service-terms/) apply to your customer content.

#### What is account information?

We define account information as information about a customer that a customer provides to us in connection with the creation or administration of a customer account. For example, account information includes names, usernames, phone numbers, email addresses, and billing information associated with a customer account. The information practices described in the [AWS Privacy Notice](/privacy/) apply to account information.

#### Who owns customer content?

As a customer, you own your customer content, and you select which AWS services can process, store, and host your customer content. We do not access or use your customer content for any purpose without your agreement. We do not use customer content or derive information from it for marketing or advertising.

#### Who controls customer content?

As a customer, you control your content:

- You determine the geographic region where your customer content will be stored and the type of storage.
- You choose the secured state of your customer content. We offer you industry-leading encryption features to protect your content in transit and at rest, and we provide you with the option to manage your own encryption keys.
- You manage access to your customer content, and access to AWS services and resources through users, groups, permissions, and credentials that you control.

#### How do you use my account information?

The [AWS Privacy Notice](/privacy/) describes how we collect and use account information.

#### How does AWS use information included in resource identifiers and other items related to the management of AWS resources?

AWS uses that information to provide the AWS services, and to protect and improve the customer experience. For example, AWS uses resource identifiers to help customers generate cost and usage reports, which can be used to break down AWS spend by cost center, and IAM permissions to determine whether a specific user can purchase reserved instances. When customers contact AWS for technical assistance, AWS may also analyze resource identifiers and permissions to help resolve their issues.

#### What happens when AWS receives a legal request for customer content?

We are vigilant about our customers' privacy. We will not disclose customer content unless we're required to do so to comply with the law or a valid and binding order of a governmental body. If a governmental body sends AWS a demand for customer content, we will attempt to redirect the governmental body to request that data directly from the customer. Governmental and regulatory bodies need to follow the applicable legal process to obtain valid and binding orders. We review all orders and object to overbroad or otherwise inappropriate ones. If compelled to disclose customer content to a government body, we will give customers reasonable notice of the demand to allow the customer to seek a protective order or other appropriate remedy unless AWS is legally prohibited from doing so. It is also important to point out that our customers can encrypt their customer content, and we provide customers with the option to manage their own encryption keys.

We know that transparency matters to our customers, so we regularly publish a report about the types and volume of information requests we receive on the [Amazon Information Requests](/compliance/amazon-information-requests/) webpage.

#### Where is customer content stored?

The [AWS Global Infrastructure](/about-aws/global-infrastructure/) gives you the flexibility to choose where and how you want to run your workloads using the same network, control plane, APIs, and AWS services. If you would like to run your applications globally you can choose from any of the AWS Regions and Availability Zones. As a customer, you choose the AWS Region(s) in which your customer content is stored, allowing you to deploy AWS services in the location(s) of your choice, in accordance with your specific geographic requirements. For example, if an AWS customer in Australia wants to store their data only in Australia, they can choose to deploy their AWS services exclusively in the Asia Pacific (Sydney) AWS Region. If you want to discover other flexible storage options see the [AWS Regions](/about-aws/global-infrastructure/regions_az/) webpage.

You can also replicate and back up your customer content in more than one AWS Region. We will not move or replicate your content outside of your chosen AWS Region(s), except as necessary to provide the services you initiated, or as necessary to comply with the law or a binding order of a governmental body. However, it is important to note that some AWS services may not be available in all AWS Regions. For more information about which services are available in which AWS Regions, see the [AWS Regional Services](/about-aws/global-infrastructure/regional-product-services/) webpage.

#### What is my role in securing my content?

When evaluating the security of a cloud solution, it is important for you to understand and distinguish between the security of the cloud, and your security in the cloud. Security of the cloud encompasses the security measures that AWS implements and operates. We are responsible for security of the cloud. Security in the cloud encompasses the security measures that you implement and operate, related to the AWS services you use. You are responsible for your security in the cloud. For more information, see the [AWS Shared Responsibility](/compliance/shared-responsibility-model/) webpage.

#### What step does AWS take to protect my privacy?

At AWS, our highest priority is securing our customers’ data, and we implement rigorous contractual, technical, and organizational measures to protect data confidentiality, integrity, and availability regardless of which AWS Region a customer has selected.

AWS complies with ISO 27018, a code of practice that focuses on protection of personal data in the cloud. It extends ISO information security standard 27001 to cover the regulatory requirements for the protection of personally identifiable information (PII) or personal data for the public cloud computing environment and specifies implementation guidance based on ISO 27002 controls that is applicable to PII processed by public cloud service providers. For more information, or to view the AWS ISO 27018 Certification, see the [AWS ISO 27018 Compliance](/compliance/iso-27018-faqs/) webpage.

Additionally, AWS publishes a SOC 2 Type II report, developed by the American Institute of CPAs (AICPA), which establishes criteria for evaluating controls related to how personal data is collected, used, retained, disclosed, and disposed to meet the entity’s objectives. The AWS SOC 2 Type II report provides third-party attestation of our systems and the suitability of the design of our controls. The scope of the report includes information about how we handle the content that you upload to AWS and how it is protected in all of the services and locations that are in scope for the latest [AWS SOC reports](/compliance/soc-faqs/). The SOC 2 Type II report can be downloaded through [AWS Artifact](/artifact/) in the [AWS Management Console](https://console.aws.amazon.com/console/home).

#### Who should I contact if I have questions regarding AWS and data protection?

We recommend that customers with questions regarding AWS and data protection contact their AWS account manager. If customers have signed up for Enterprise Support, they can also reach out to their Technical Account Manager (TAM) for support. AWS account managers and TAMs work with Solutions Architects to help customers meet their compliance needs. AWS can’t provide legal advice to customers, and we recommend that customers consult their legal counsel if they have legal questions regarding data protection.

We also have teams of Enterprise Support Representatives, Professional Services Consultants, and other staff to help with privacy questions. You can contact us with questions [here](/contact-us/compliance-support/).

## Resources

[](/compliance/data-privacy/)

### Data Privacy Center

Learn more

[](/compliance/privacy-features/)

### Privacy Features of AWS Services

Learn more

[](/compliance/amazon-information-requests/)

### Amazon Information Requests

Learn more

[](/privacy/)

### AWS Privacy Notice

Learn more

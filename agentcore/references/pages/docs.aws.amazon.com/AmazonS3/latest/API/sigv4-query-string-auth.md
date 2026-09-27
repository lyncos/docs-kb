---
title: Welcome
description: 'We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can '
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html
fetched: '2026-09-26'
tags:
- agentcore
- docs-aws-amazon-com
- reference
- related
referenced_by:
- gateway-setup-tools-credentials.md
conversion: tavily
---

## Select your cookie preferences

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies.   
  
 If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

We use cookies and similar tools (collectively, "cookies") for the following purposes.

### Essential

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

### Performance

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Allowed

### Functional

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Allowed

### Advertising

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Allowed

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

[Skip to main content](#skip-link)

[English](# "Language Selector. Currently set to: English")

[Preferences](#)

[Contact Us](https://aws.amazon.com/contact-us/?cmpid=docs_headercta_contactus)

[Feedback](https://docs.aws.amazon.com/feedback/doc-feedback.html?hidden_service_name=S3&topic_url=https%3A%2F%2Fdocs.aws.amazon.com%2FAmazonS3%2Flatest%2FAPI%2FWelcome.html)

[![AWS Documentation](/assets/r/images/aws_logo_light.svg)](https://docs.aws.amazon.com)

[Get started](#)

[Service guides](#)

[Developer tools](#)

[AI resources](#)

[Create an AWS Account](https://portal.aws.amazon.com)

# Welcome

[PDF](/pdfs/AmazonS3/latest/API/s3-api.pdf#Welcome)

[Markdown](Welcome.md "Download Markdown")

Up-to-date AWS docs, tested procedures, and IAM guardrails via a single setup prompt in your AI coding agent.

Focus mode

Welcome - Amazon S3

[Documentation](/index.html)[Amazon Simple Storage Service (S3)](/s3/index.html)[API Reference](Welcome.html)

[Amazon S3](#Welcome_Amazon_Simple_Storage_Service)[Amazon S3 Control](#Welcome_AWS_S3_Control)[Amazon S3 Files](#Welcome_Amazon_S3_Files)[Amazon S3 on Outposts](#Welcome_Amazon_S3_on_Outposts)[Amazon S3 Tables](#Welcome_Amazon_S3_Tables)[Amazon S3 Vectors](#Welcome_Amazon_S3_Vectors)

## Amazon S3

###### Note

For information about using the Amazon S3 API—including authentication, signing requests, code examples, and error handling—see the [Amazon S3 Developer Guide](https://docs.aws.amazon.com/AmazonS3/latest/developerguide/Welcome.html).

Welcome to the *Amazon S3 API Reference*. This guide explains the Amazon Simple Storage Service (Amazon S3)
application programming interface (API).

Welcome to the *Amazon S3 API Reference*. This guide explains the Amazon Simple Storage Service (Amazon S3)
application programming interface (API).

You can use any toolkit that supports HTTP to use the REST API. You can even use a browser
to fetch objects, as long as they are anonymously readable.

The REST API uses the standard HTTP headers and status codes, so that standard browsers and toolkits work as expected. In some areas, we have added functionality to HTTP (for example, we added headers to support access control). In these cases, we have done our best to add the new functionality in a way that matched the style of standard HTTP usage.

The current version of the Amazon S3 API is `2006-03-01`.

Amazon S3 supports the REST API.

###### Note

Support for SOAP over HTTP is deprecated, but it is still available over HTTPS.
However, new Amazon S3 features will not be supported for SOAP. We recommend that
you use either this REST API or the AWS SDKs.

## Amazon S3 Control

AWS S3 Control provides access to Amazon S3 control plane actions.

## Amazon S3 Files

S3 Files makes S3 buckets accessible as high-performance file systems powered by EFS. This service enables file system interface access to S3 data with sub-millisecond latencies through mount targets, supporting AI/ML workloads, media processing, and hybrid storage workflows that require both file system and object storage access to the same data.

## Amazon S3 on Outposts

Amazon S3 on Outposts provides access to S3 on Outposts operations.

## Amazon S3 Tables

An Amazon S3 table represents a structured dataset consisting of tabular data in [Apache Parquet](https://parquet.apache.org/docs/) format and related metadata. This data is stored inside an S3 table as a subresource. All tables in a table bucket are stored in the [Apache Iceberg](https://iceberg.apache.org/docs/latest/) table format. Through integration with the [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html) you can interact with your tables using AWS analytics services, such as [Amazon Athena](https://docs.aws.amazon.com/athena/) and [Amazon Redshift](https://docs.aws.amazon.com/redshift/). Amazon S3 manages maintenance of your tables through automatic file compaction and snapshot management. For more information, see [Amazon S3 table buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets.html).

## Amazon S3 Vectors

Amazon S3 vector buckets are a bucket type to store and search vectors with sub-second
search times. They are designed to provide dedicated API operations for you to interact
with vectors to do similarity search. Within a vector bucket, you use a vector index to
organize and logically group your vector data. When you make a write or read request, you
direct it to a single vector index. You store your vector data as vectors. A vector
contains a key (a name that you assign), a multi-dimensional vector, and, optionally,
metadata that describes a vector. The key uniquely identifies the vector in a vector
index.

[Document Conventions](/general/latest/gr/docconventions.html)

Actions

Did this page help you? - Yes

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Did this page help you? - No

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

### View related pages

  

Abstracts generated by AI

AmazonS3 › developerguide

[What is Amazon S3?![](https://prod.us-west-2.tcx-beacon.docs.aws.dev/recommendation-beacon/similar/impressions/null/vVriRebZhwlPLRC-9c2nKfDhosWTxUMQBrswZ-tYcxPohgjg7zLQ4A==/https:%7C%7Cdocs.aws.amazon.com%7CAmazonS3%7Clatest%7CAPI%7CWelcome.html/https:%7C%7Cdocs.aws.amazon.com%7CAmazonS3%7Clatest%7Cdeveloperguide%7CWelcome.html)](https://docs.aws.amazon.com/AmazonS3/latest/developerguide/Welcome.html)

Learn what Amazon S3 is and how to use the S3 REST API, including authentication, permissions, and recommendations for using AWS SDKs or the AWS CLI.

*June 9, 2026*

AmazonS3 › developerguide

[Developing with Amazon S3![](https://prod.us-west-2.tcx-beacon.docs.aws.dev/recommendation-beacon/similar/impressions/null/vVriRebZhwlPLRC-9c2nKfDhosWTxUMQBrswZ-tYcxPohgjg7zLQ4A==/https:%7C%7Cdocs.aws.amazon.com%7CAmazonS3%7Clatest%7CAPI%7CWelcome.html/https:%7C%7Cdocs.aws.amazon.com%7CAmazonS3%7Clatest%7Cdeveloperguide%7Cdeveloping-s3.html)](https://docs.aws.amazon.com/AmazonS3/latest/developerguide/developing-s3.html)

Not applicable

*June 9, 2026*

* ### On this page
* Recommended tasks

  ### Learn about

  [AWS Signature Version 4 authentication process![](https://prod.us-west-2.tcx-beacon.docs.aws.dev/recommendation-beacon/journey/impressions/null/vVriRebZhwlPLRC-9c2nKfDhosWTxUMQBrswZ-tYcxPohgjg7zLQ4A==/https:%7C%7Cdocs.aws.amazon.com%7CAmazonS3%7Clatest%7CAPI%7CWelcome.html/https:%7C%7Cdocs.aws.amazon.com%7CIAM%7Clatest%7CUserGuide%7Creference_sigv.html)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html)

  [Amazon S3 basics and REST API usage![](https://prod.us-west-2.tcx-beacon.docs.aws.dev/recommendation-beacon/journey/impressions/null/vVriRebZhwlPLRC-9c2nKfDhosWTxUMQBrswZ-tYcxPohgjg7zLQ4A==/https:%7C%7Cdocs.aws.amazon.com%7CAmazonS3%7Clatest%7CAPI%7CWelcome.html/https:%7C%7Cdocs.aws.amazon.com%7CAmazonS3%7Clatest%7Cdeveloperguide%7CWelcome.html)](https://docs.aws.amazon.com/AmazonS3/latest/developerguide/Welcome.html)

  [AWS SigV4 and SigV4a signing protocols guide![](https://prod.us-west-2.tcx-beacon.docs.aws.dev/recommendation-beacon/journey/impressions/null/vVriRebZhwlPLRC-9c2nKfDhosWTxUMQBrswZ-tYcxPohgjg7zLQ4A==/https:%7C%7Cdocs.aws.amazon.com%7CAmazonS3%7Clatest%7CAPI%7CWelcome.html/https:%7C%7Cdocs.aws.amazon.com%7CIAM%7Clatest%7CUserGuide%7Creference_sigv-create-signed-request.html)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv-create-signed-request.html)

  [Amazon S3 API operations and features![](https://prod.us-west-2.tcx-beacon.docs.aws.dev/recommendation-beacon/journey/impressions/null/vVriRebZhwlPLRC-9c2nKfDhosWTxUMQBrswZ-tYcxPohgjg7zLQ4A==/https:%7C%7Cdocs.aws.amazon.com%7CAmazonS3%7Clatest%7CAPI%7CWelcome.html/https:%7C%7Cdocs.aws.amazon.com%7CAmazonS3%7Clatest%7CAPI%7CAPI_Operations_Amazon_Simple_Storage_Service.html)](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Amazon_Simple_Storage_Service.html)

  [Amazon S3 API actions and services overview![](https://prod.us-west-2.tcx-beacon.docs.aws.dev/recommendation-beacon/journey/impressions/null/vVriRebZhwlPLRC-9c2nKfDhosWTxUMQBrswZ-tYcxPohgjg7zLQ4A==/https:%7C%7Cdocs.aws.amazon.com%7CAmazonS3%7Clatest%7CAPI%7CWelcome.html/https:%7C%7Cdocs.aws.amazon.com%7CAmazonS3%7Clatest%7CAPI%7CAPI_Operations.html)](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations.html)

  ### How to

  [Use Amazon S3 PutObject API to upload files![](https://prod.us-west-2.tcx-beacon.docs.aws.dev/recommendation-beacon/journey/impressions/null/vVriRebZhwlPLRC-9c2nKfDhosWTxUMQBrswZ-tYcxPohgjg7zLQ4A==/https:%7C%7Cdocs.aws.amazon.com%7CAmazonS3%7Clatest%7CAPI%7CWelcome.html/https:%7C%7Cdocs.aws.amazon.com%7CAmazonS3%7Clatest%7CAPI%7CAPI_PutObject.html)](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)
* [Provide feedback](https://docs.aws.amazon.com/feedback/doc-feedback.html?hidden_service_name=S3&topic_url=https%3A%2F%2Fdocs.aws.amazon.com%2FAmazonS3%2Flatest%2FAPI%2FWelcome.html)

#### Next topic:

[Actions](./API_Operations.html)

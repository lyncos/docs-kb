---
title: cloudtrail[¶](#cloudtrail "Permalink to this heading")
description: AWS CLI Command Reference
product: Amazon Bedrock AgentCore
section: References / docs.aws.amazon.com
source_url: https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/index.html
fetched: '2026-09-26'
tags:
- agentcore
- docs-aws-amazon-com
- reference
- related
referenced_by:
- gateway-cloudtrail.md
conversion: pandoc
---

[AWS CLI Command Reference](../../index.html)

- [Home](../../index.html)
- [User Guide](https://docs.aws.amazon.com/cli/latest/userguide/)
- [Forum](https://forums.aws.amazon.com/forum.jspa?forumID=150)
- [GitHub](https://github.com/aws/aws-cli)

[ ](#) [](#)

### Navigation

- [index](../../genindex.html "General Index")
- [next](add-tags.html "add-tags") \|
- [previous](../cloudsearchdomain/upload-documents.html "upload-documents") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [cloudtrail]()

- [← upload-documents](../cloudsearchdomain/upload-documents.html "previous chapter (use the left arrow)") /
- [add-tags →](add-tags.html "next chapter (use the right arrow)")

[![Amazon Web Services logo](../../_static/logo.png)](../../index.html)

### [Table of Contents](../../index.html)

- [cloudtrail](#)
  - [Description](#description)
  - [Available Commands](#available-commands)

### Quick search

Search box

Search

### Feedback

Did you find this page useful? Do you have a suggestion to improve the documentation? [Give us feedback](https://docs.aws.amazon.com/forms/aws-doc-feedback?hidden_service_name=AWS%20Command%20Line%20Interface&hidden_guide_name=Reference&topic_url=https%3A%2F%2Fdocs.aws.amazon.com%2Fcli%2Flatest%2Freference/cloudtrail/index.html).  
If you would like to suggest an improvement or fix for the AWS CLI, check out our [contributing guide](https://github.com/aws/aws-cli/blob/v2/CONTRIBUTING.rst) on GitHub.

### User Guide

First time using the AWS CLI? See the [User Guide](https://docs.aws.amazon.com/cli/latest/userguide/) for help getting started.

\[ [aws](../index.html#cli-aws) \]

# cloudtrail[¶](#cloudtrail "Permalink to this heading")

## Description[¶](#description "Permalink to this heading")

This is the CloudTrail API Reference. It provides descriptions of actions, data types, common parameters, and common errors for CloudTrail.

CloudTrail is a web service that records Amazon Web Services API calls for your Amazon Web Services account and delivers log files to an Amazon S3 bucket. The recorded information includes the identity of the user, the start time of the Amazon Web Services API call, the source IP address, the request parameters, and the response elements returned by the service.

### Note

As an alternative to the API, you can use one of the Amazon Web Services SDKs, which consist of libraries and sample code for various programming languages and platforms (Java, Ruby, .NET, iOS, Android, etc.). The SDKs provide programmatic access to CloudTrail. For example, the SDKs handle cryptographically signing requests, managing errors, and retrying requests automatically. For more information about the Amazon Web Services SDKs, including how to download and install them, see [Tools to Build on Amazon Web Services](http://aws.amazon.com/tools/) .

See the [CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) for information about the data that is included with each Amazon Web Services API call listed in the log files.

## Available Commands[¶](#available-commands "Permalink to this heading")

- [add-tags](add-tags.html)
- [cancel-query](cancel-query.html)
- [create-channel](create-channel.html)
- [create-dashboard](create-dashboard.html)
- [create-event-data-store](create-event-data-store.html)
- [create-trail](create-trail.html)
- [delete-channel](delete-channel.html)
- [delete-dashboard](delete-dashboard.html)
- [delete-event-data-store](delete-event-data-store.html)
- [delete-resource-policy](delete-resource-policy.html)
- [delete-trail](delete-trail.html)
- [deregister-organization-delegated-admin](deregister-organization-delegated-admin.html)
- [describe-query](describe-query.html)
- [describe-trails](describe-trails.html)
- [disable-federation](disable-federation.html)
- [enable-federation](enable-federation.html)
- [generate-query](generate-query.html)
- [get-channel](get-channel.html)
- [get-dashboard](get-dashboard.html)
- [get-event-configuration](get-event-configuration.html)
- [get-event-data-store](get-event-data-store.html)
- [get-event-selectors](get-event-selectors.html)
- [get-import](get-import.html)
- [get-insight-selectors](get-insight-selectors.html)
- [get-query-results](get-query-results.html)
- [get-resource-policy](get-resource-policy.html)
- [get-trail](get-trail.html)
- [get-trail-status](get-trail-status.html)
- [list-channels](list-channels.html)
- [list-dashboards](list-dashboards.html)
- [list-event-data-stores](list-event-data-stores.html)
- [list-import-failures](list-import-failures.html)
- [list-imports](list-imports.html)
- [list-insights-data](list-insights-data.html)
- [list-insights-metric-data](list-insights-metric-data.html)
- [list-public-keys](list-public-keys.html)
- [list-queries](list-queries.html)
- [list-tags](list-tags.html)
- [list-trails](list-trails.html)
- [lookup-events](lookup-events.html)
- [put-event-configuration](put-event-configuration.html)
- [put-event-selectors](put-event-selectors.html)
- [put-insight-selectors](put-insight-selectors.html)
- [put-resource-policy](put-resource-policy.html)
- [register-organization-delegated-admin](register-organization-delegated-admin.html)
- [remove-tags](remove-tags.html)
- [restore-event-data-store](restore-event-data-store.html)
- [search-sample-queries](search-sample-queries.html)
- [start-dashboard-refresh](start-dashboard-refresh.html)
- [start-event-data-store-ingestion](start-event-data-store-ingestion.html)
- [start-import](start-import.html)
- [start-logging](start-logging.html)
- [start-query](start-query.html)
- [stop-event-data-store-ingestion](stop-event-data-store-ingestion.html)
- [stop-import](stop-import.html)
- [stop-logging](stop-logging.html)
- [update-channel](update-channel.html)
- [update-dashboard](update-dashboard.html)
- [update-event-data-store](update-event-data-store.html)
- [update-trail](update-trail.html)
- [validate-logs](validate-logs.html)
- [verify-query-results](verify-query-results.html)

- [← upload-documents](../cloudsearchdomain/upload-documents.html "previous chapter (use the left arrow)") /
- [add-tags →](add-tags.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](add-tags.html "add-tags") \|
- [previous](../cloudsearchdomain/upload-documents.html "upload-documents") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [cloudtrail]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

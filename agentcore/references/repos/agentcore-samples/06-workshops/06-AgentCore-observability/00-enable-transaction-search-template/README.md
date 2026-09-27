---
title: Enable Transaction Search for Amazon Bedrock AgentCore Observability
description: This tutorial demonstrates how to enable Amazon CloudWatch Transaction Search for AgentCore observability. Transaction Search provides an interactive analytics experience for complete visibility of your application transaction spans and traces across distributed systems.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/06-workshops/06-AgentCore-observability/00-enable-transaction-search-template/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# Enable Transaction Search for Amazon Bedrock AgentCore Observability

This tutorial demonstrates how to enable Amazon CloudWatch Transaction Search for AgentCore observability. Transaction Search provides an interactive analytics experience for complete visibility of your application transaction spans and traces across distributed systems.

## Getting Started

The Project folder has the following:

- A Jupyter notebook demonstrating how to enable Transaction Search using CloudFormation
- A CloudFormation template (transaction_search.yml) for automated deployment
- Sample images showing before and after Transaction Search enablement

## Cleanup

After completing the tutorial:

1. Delete the CloudFormation stack: `transaction-search`
2. This removes the resource policy and disables Transaction Search
3. Existing traces and logs are retained according to retention policies

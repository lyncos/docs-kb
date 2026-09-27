---
title: CrewAI Agent with Amazon Bedrock AgentCore Runtime and Observability
description: This tutorial demonstrates how to deploy a CrewAI travel agent to Amazon Bedrock AgentCore Runtime with observability through Amazon CloudWatch.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/06-workshops/06-AgentCore-observability/01-Agentcore-runtime-hosted/CrewAI/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# CrewAI Agent with Amazon Bedrock AgentCore Runtime and Observability

This tutorial demonstrates how to deploy a [CrewAI](https://www.crewai.com/) travel agent to Amazon Bedrock AgentCore Runtime with observability through Amazon CloudWatch.

## Overview

Learn to host a CrewAI agent using Amazon Bedrock models with comprehensive observability with AWS OpenTelemetry instrumentation and Amazon CloudWatch monitoring.

## Prerequisites

* Python 3.10+
* AWS credentials configured with appropriate permissions
* Amazon Bedrock AgentCore SDK
* CrewAI framework
* Amazon CloudWatch access
* Enable [transaction search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Enable-TransactionSearch.html) on Amazon CloudWatch

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Open the Jupyter notebook: `runtime-with-crewai-and-bedrock-models.ipynb`

3. Follow the tutorial to:
   - Create and test a CrewAI agent locally
   - Deploy the agent to AgentCore Runtime
   - Enable observability with OpenTelemetry
   - Monitor performance on CloudWatch

## Key Features

* CrewAI travel agent with web search capabilities
* Amazon Bedrock models (Anthropic Claude Haiku 4.5)
* AgentCore Runtime hosting
* CloudWatch observability and tracing

## Cleanup

After completing the tutorial:
1. Remove AgentCore Runtime deployments
2. Clean up ECR repositories
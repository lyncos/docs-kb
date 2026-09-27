---
title: TypeScript CDK Samples
description: Deploy Amazon Bedrock AgentCore resources using AWS CDK with TypeScript.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/04-infrastructure-as-code/cdk/typescript/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# TypeScript CDK Samples

Deploy Amazon Bedrock AgentCore resources using AWS CDK with TypeScript.

## Prerequisites

- Node.js 18+ and npm
- AWS CDK v2.236.0 or later (for BedrockAgentCore alpha support)
- AWS CLI configured
- Docker installed and running
- Access to Amazon Bedrock AgentCore

```bash
npm install -g aws-cdk
```

## General Deployment Pattern

```bash
cd <sample-directory>
npm install
npm run build
cdk deploy --all
```

## Samples

- **[knowledge-base-rag-agent/](./knowledge-base-rag-agent/)** - Full-stack RAG agent with Knowledge Base, OpenSearch Serverless, web interface, and Cognito authentication

## TypeScript CDK Advantages

- Strong type safety and IDE support
- Compile-time error checking
- Rich ecosystem of npm packages
- Familiar syntax for JavaScript developers
- Uses `DockerImageAsset` for container building

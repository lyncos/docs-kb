---
title: AgentCore CDK Project
description: This CDK project is managed by the AgentCore CLI. It deploys your agent infrastructure into AWS using the `@aws/agentcore-cdk` L3 constructs.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/06-workshops/03-AgentCore-identity/08-IDP-examples/PingFederate/agent/private-idp-ping-agent/agentcore/cdk/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# AgentCore CDK Project

This CDK project is managed by the AgentCore CLI. It deploys your agent infrastructure into AWS using the `@aws/agentcore-cdk` L3 constructs.

## Structure

- `bin/cdk.ts` — Entry point. Reads project configuration from `agentcore/` and creates a stack per deployment target.
- `lib/cdk-stack.ts` — Defines `AgentCoreStack`, which wraps the `AgentCoreApplication` L3 construct.
- `test/cdk.test.ts` — Unit tests for stack synthesis.

## Useful commands

- `npm run build` compile TypeScript to JavaScript
- `npm run test` run unit tests
- `npx cdk synth` emit the synthesized CloudFormation template
- `npx cdk deploy` deploy this stack to your default AWS account/region
- `npx cdk diff` compare deployed stack with current state

## Usage

You typically don't need to interact with this directory directly. The AgentCore CLI handles synthesis and deployment:

```bash
agentcore deploy    # synthesizes and deploys via CDK
agentcore status    # checks deployment status
```

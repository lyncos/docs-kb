---
title: CDK app — Secure IDE Gateway Tool (Figma)
description: CDK TypeScript app that deploys the serverless OAuth proxy and AgentCore Gateway for this sample. See DEPLOYMENT.md for the full deployment guide and ../README.md for the architecture.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/06-workshops/02-AgentCore-gateway/04-integration/06-secure-ide-gateway-tool/cdk/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# CDK app — Secure IDE Gateway Tool (Figma)

CDK TypeScript app that deploys the serverless OAuth proxy and AgentCore Gateway for this sample.
See [DEPLOYMENT.md](DEPLOYMENT.md) for the full deployment guide and [../README.md](../README.md)
for the architecture.

The `cdk.json` file tells the CDK Toolkit how to execute the app (`ts-node bin/cdk.ts`).

## Useful commands

* `pnpm install`      install dependencies
* `pnpm run build`    compile TypeScript to JS
* `pnpm run watch`    watch for changes and compile
* `pnpm cdk deploy`   deploy this stack to your default AWS account/region
* `pnpm cdk diff`     compare deployed stack with current state
* `pnpm cdk synth`    emit the synthesized CloudFormation template

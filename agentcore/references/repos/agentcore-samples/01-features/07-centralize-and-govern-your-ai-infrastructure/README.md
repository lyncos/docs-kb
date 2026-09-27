---
title: AI Governance Layer
description: 'Add a gateway to a runtime project with the AgentCore CLI:'
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/01-features/07-centralize-and-govern-your-ai-infrastructure/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# AI Governance Layer

## AgentCore CLI

Add a gateway to a runtime project with the AgentCore CLI:

```bash
npm install -g @aws/agentcore@0.30.0
node -e 'process.exit(+process.versions.node.split(".")[0] >= 20 ? 0 : 1)' \
  || { echo "ERROR: Node.js 20+ required by the AgentCore CLI (found $(node -v))"; exit 1; }
agentcore --version | grep -q '^0\.' \
  || { echo "ERROR: these samples need AgentCore CLI v0. Run: npm install -g @aws/agentcore@0.30.0"; exit 1; }

# Add a gateway interactively
agentcore add gateway

# Add a gateway target (Lambda, MCP server, OpenAPI, or Smithy)
agentcore add gateway-target --type lambda-function-arn --gateway mygateway --lambda-arn $LAMBDA_ARN

# Deploy all resources
agentcore deploy
```

See [`01-gateway/README.md`](01-gateway/README.md) for the full CLI reference.

## Documentation

- [AgentCore gateway Developer Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [AgentCore policy Developer Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html)
- [AWS Agent registry Developer Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html)

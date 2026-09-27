---
title: Amazon Bedrock AgentCore gateway Targets
description: 'Targets define the tools and models that your AgentCore gateway will host. AgentCore gateway supports three categories of targets:'
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/01-features/07-centralize-and-govern-your-ai-infrastructure/01-gateway/01-attach-targets/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# Amazon Bedrock AgentCore gateway Targets

![arch](../images/architecture.png)

Targets define the tools and models that your AgentCore gateway will host. AgentCore gateway supports three categories of targets:

- **MCP targets**: operate in aggregation mode. AgentCore gateway acts as an MCP server whose capabilities combine those of all its MCP targets into a single unified virtual MCP server.

- **HTTP targets**: AgentCore gateway sends traffic directly to HTTP targets without aggregation or protocol translation. You define tools using an OpenAPI or Smithy schema so that agents can discover and invoke them.

- **Inference targets**: AgentCore gateway acts as a unified LLM proxy, routing inference requests to model providers (Amazon Bedrock, OpenAI, Anthropic, and other OpenAI-compatible services) based on the model in the request.

You can attach different AgentCore identity Credential Providers to different targets, which lets you securely control outbound authentication on a per-target basis.

## Tutorials

| Section                         | Description                                                      |
| :------------------------------ | :--------------------------------------------------------------- |
| [http](http/)                   | Attach targets in HTTP mode                                      |
| [mcp](mcp/)                     | Attach targets in MCP mode                                       |
| [llm-inference](llm-inference/) | Attach inference targets to route LLM traffic to model providers |

## Documentation

- [AgentCore gateway Developer Guide](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)

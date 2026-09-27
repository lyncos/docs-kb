---
title: End-to-End AgentCore Workshop
description: This workshop walks you through building a complete customer support agent from prototype to production using Amazon Bedrock AgentCore services. The same workshop is implemented in three different agentic frameworks so you can follow along with whichever framework you prefer.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/06-workshops/09-AgentCore-E2E/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# End-to-End AgentCore Workshop

This workshop walks you through building a complete customer support agent from prototype to production using Amazon Bedrock AgentCore services. The same workshop is implemented in three different agentic frameworks so you can follow along with whichever framework you prefer.

> [!IMPORTANT]
> These workshops are for educational purposes. It demonstrates how AgentCore services are used when migrating an agentic use case from prototype to production. It is not intended for direct use in production environments.

## Frameworks

| Framework                                              | Folder                             | Status      |
| ------------------------------------------------------ | ---------------------------------- | ----------- |
| [Strands Agents](https://strandsagents.com/)           | [strands-agents/](strands-agents/) | Available   |
| [Google ADK](https://google.github.io/adk-docs/)       | [google-adk/](google-adk/)         | Coming soon |
| [LangGraph](https://langchain-ai.github.io/langgraph/) | [langgraph/](langgraph/)           | Coming soon |

## What You'll Build

Across six labs, you'll incrementally build a production-ready customer support agent that includes AgentCore Runtime for serverless deployment, AgentCore Memory for personalized conversations, AgentCore Gateway and Identity for secure shared tools, AgentCore Policy for fine-grained access control with Cedar policies, AgentCore Observability for tracing and monitoring agent behavior, AgentCore Evaluations for continuous quality monitoring, and a Streamlit frontend for customer interaction.

Each framework folder is self-contained with its own README, notebooks, and dependencies. Pick a framework and follow the instructions in its README to get started.

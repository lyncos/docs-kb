---
title: How it works
description: Amazon Bedrock AgentCore Evaluations provides capabilities to assess the performance of AI agents. It can compute metrics such as an agent’s end-to-end task completion (goal attainment) correctness, the accuracy of a tool invoked by the agent while handling a user request, and an
product: Amazon Bedrock AgentCore
section: Developer Guide / how
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/how-it-works-evaluations.html
fetched: '2026-09-26'
tags:
- agentcore
- how
---

# How it works
<a name="how-it-works-evaluations"></a>

Amazon Bedrock AgentCore Evaluations provides capabilities to assess the performance of AI agents. It can compute metrics such as an agent’s end-to-end task completion (goal attainment) correctness, the accuracy of a tool invoked by the agent while handling a user request, and any custom metric defined to evaluate specific dimensions of an agent’s behavior. The AgentCore Evaluations can evaluate the AI agents that are hosted under AgentCore Runtime as well as AI agents hosted outside of AgentCore.

You can create and manage evaluation or relevant resources using the AgentCore CLI, the AgentCore Python SDK, the AWS Management Console or directly through AWS SDKs.

**Topics**
+ [Evaluation terminology](evaluations-terminology.md)
+ [Evaluators](evaluators.md)
+ [Evaluation types](evaluations-types.md)
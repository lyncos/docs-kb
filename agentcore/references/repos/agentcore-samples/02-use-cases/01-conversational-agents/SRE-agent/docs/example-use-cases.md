---
title: Example Use Cases
description: The agents collaborate to check pod status, analyze events, examine memory usage trends, and provide remediation steps.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/02-use-cases/01-conversational-agents/SRE-agent/docs/example-use-cases.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# Example Use Cases

## Investigating Pod Failures

```bash
sre-agent --prompt "Our database pods are crash looping in production"
```

The agents collaborate to check pod status, analyze events, examine memory usage trends, and provide remediation steps.

## Diagnosing Performance Issues

```bash
sre-agent --prompt "API response times have degraded 3x in the last hour"
```

The system correlates metrics across multiple dimensions to identify latency sources and configuration issues.

## Interactive Troubleshooting Session

```bash
sre-agent --interactive

👤 You: We're seeing intermittent 502 errors from the payment service
🤖 Multi-Agent System: Investigating intermittent 502 errors...

👤 You: What's causing the queue buildup?
🤖 Multi-Agent System: Analyzing payment queue patterns...
```

Interactive mode allows multi-turn conversations for complex investigations.

## Proactive Monitoring

```bash
# Morning health check
sre-agent --prompt "Perform a comprehensive health check of all production services"

# Capacity planning
sre-agent --prompt "Analyze resource utilization trends and predict when we'll need to scale"

# Security audit
sre-agent --prompt "Check for any suspicious patterns in authentication logs"
```

Examples of proactive monitoring and health check queries.
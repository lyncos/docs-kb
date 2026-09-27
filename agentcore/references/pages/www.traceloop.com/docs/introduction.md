---
title: Introduction
description: Monitor, debug and test the quality of your LLM outputs
product: Amazon Bedrock AgentCore
section: References / www.traceloop.com
source_url: https://www.traceloop.com/docs/introduction
fetched: '2026-09-26'
tags:
- agentcore
- reference
- related
- www-traceloop-com
referenced_by:
- observability-configure.md
conversion: native-md
---

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Introduction

> Monitor, debug and test the quality of your LLM outputs

Traceloop automatically monitors the quality of your LLM outputs. It helps you to debug and test changes to your models and prompts.

* Get real-time alerts about your model's quality
* Execution tracing for every request
* Gradually rollout changes to models and prompts
* Debug and re-run issues from production in your IDE

Need help using Traceloop? Ping us at [dev@traceloop.com](mailto:dev@traceloop.com)

### Get Started - with OpenLLMetry SDK or Traceloop Hub

Traceloop uses OpenTelemetry to monitor and trace your LLM application.
You can install the OpenLLMetry SDK in your application, or use Traceloop Hub as a smart proxy to all your LLM calls.

To get started, pick the language you are using and follow the instructions.

<CardGroup cols={3}>
  <Card title="Hub" icon="arrows-to-dot" href="/docs/hub/getting-started">
    Beta
  </Card>

  <Card title="Python SDK" icon="python" href="/docs/openllmetry/getting-started-python">
    Available
  </Card>

  <Card title="Typescript SDK" icon="node" href="/docs/openllmetry/getting-started-ts">
    Available
  </Card>

  <Card title="Go SDK" icon="golang" href="/docs/openllmetry/getting-started-go">
    Beta
  </Card>

  <Card title="Ruby SDK" icon="gem" href="/docs/openllmetry/getting-started-ruby">
    Beta
  </Card>
</CardGroup>

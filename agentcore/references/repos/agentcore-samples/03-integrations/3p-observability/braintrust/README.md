---
title: AgentCore + Braintrust observability
description: Deploy a Strands travel agent to AgentCore runtime with traces sent to Braintrust via OTLP.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/03-integrations/3p-observability/braintrust/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# AgentCore + Braintrust observability

Deploy a Strands travel agent to AgentCore runtime with traces sent to [Braintrust](https://www.braintrust.dev/)
via OTLP.

## Architecture

```
AgentCore runtime → travel_agent.py
  └── StrandsTelemetry().setup_otlp_exporter()
        └── https://api.braintrust.dev/otel
              └── Braintrust → Logs
```

`DISABLE_ADOT_OBSERVABILITY=true` bypasses the default CloudWatch ADOT pipeline.
Braintrust auth uses a Bearer token header.

## Prerequisites

- Python 3.10+, uv
- AWS credentials configured
- Braintrust account with API key and project ID

## Quick Start

```bash
pip install bedrock-agentcore boto3 python-dotenv
cp .env.example .env
# Edit .env: set BRAINTRUST_API_KEY and BRAINTRUST_PROJECT_ID
python deploy.py
python invoke.py
# View traces: https://www.braintrust.dev → your project → Logs
python cleanup.py
```

## Files

| File | Description |
|:-----|:------------|
| `utils/travel_agent.py` | Agent with Braintrust OTLP setup via StrandsTelemetry |
| `deploy.py` | Deploys to AgentCore runtime with Braintrust env vars |
| `invoke.py` | Invokes the deployed agent |
| `cleanup.py` | Deletes all created AWS resources |

## Additional Resources

- [Braintrust Documentation](https://www.braintrust.dev/docs)
- [AgentCore observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html)

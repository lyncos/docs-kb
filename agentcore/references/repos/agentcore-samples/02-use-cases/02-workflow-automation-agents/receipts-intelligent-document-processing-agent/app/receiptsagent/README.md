---
title: receiptsagent
description: The AgentCore Runtime application for the Receipts IDP sample. Phase 1 is a stub entrypoint (`main.py`) that proves the Runtime deploys and is invokable. The OCR + dual-agent extraction pipeline lands in later phases — see the repo `IMPLEMENTATION-PLAN.md`.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/02-use-cases/02-workflow-automation-agents/receipts-intelligent-document-processing-agent/app/receiptsagent/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# receiptsagent

The AgentCore Runtime application for the Receipts IDP sample. Phase 1 is a stub
entrypoint (`main.py`) that proves the Runtime deploys and is invokable. The OCR
+ dual-agent extraction pipeline lands in later phases — see the repo
`IMPLEMENTATION-PLAN.md`.

`config.py` is the single place env vars are read (the replaceable deploy seam).

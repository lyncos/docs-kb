---
title: Confirm — Assemble confirm.json
description: '**Assembler unit.** Confirm reads the scoring result, asks only what the'
product: Amazon Bedrock AgentCore
section: References / repo / agent-toolkit-for-aws
source_url: https://github.com/aws/agent-toolkit-for-aws/blob/dda6148/plugins/aws-startup-advisor/skills/agent-advisor/references/phases/confirm/confirm-assemble.md
fetched: '2026-09-26'
tags:
- agent-toolkit-for-aws
- agentcore
- reference
original_frontmatter:
  _assemble: assemble-confirm
  _of_phase: confirm
  _reads:
  - winner-specific runtime and model/path confirmations (collected inline in confirm.md)
  _produces:
  - confirm.json
---

# Confirm — Assemble confirm.json

> **Assembler unit.** Confirm reads the scoring result, asks only what the
> winning runtime needs (deployment model, AgentCore services, co_recommend
> pick, native-vs-gateway tool choices), and writes `confirm.json` inline within
> `confirm.md` (Step 5). This unit records the artifact-level contract for
> the phase: it is the single creator of `confirm.json`, and its postconditions
> (declared on the phase) are the phase's completion gate. See `confirm.md`
> § Step 5 for the confirm.json shape (`deployment_model`, `agentcore_services`,
> `chosen_runtime` when co_recommend, `tool_choices`, and accepted `model_decision`).
> `model_decision.accepted` records strategy acceptance; `verification_status`
> independently records whether the exact model/path was invocable in the target account.

---
title: Validate and test policies
description: Before deploying policies to production, Policy in AgentCore provides validation capabilities to catch errors and identify potential issues. Validation works differently depending on whether you are generating policies from natural language or creating and updating policies direc
product: Amazon Bedrock AgentCore
section: Developer Guide / policy
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-validate-policies.html
fetched: '2026-09-26'
tags:
- agentcore
- policy
---

# Validate and test policies
<a name="policy-validate-policies"></a>

Before deploying policies to production, Policy in AgentCore provides validation capabilities to catch errors and identify potential issues. Validation works differently depending on whether you are generating policies from natural language or creating and updating policies directly.

Schema checks always run to verify that policies comply with the Cedar schema for your gateways. Semantic validation (automated reasoning) detects security and logic issues and can be controlled through the `validationMode` parameter. For more information about these capabilities and the validation modes, see [Validation and analysis overview](policy-validation-overview.md).

**Topics**
+ [Test a policy in LOG\_ONLY mode](policy-test-a-policy.md)
+ [Validation and analysis overview](policy-validation-overview.md)
+ [Policy generation: per-policy validation](policy-generation-validation.md)
+ [Policy create and update: per-policy engine validation](policy-create-update-validation.md)
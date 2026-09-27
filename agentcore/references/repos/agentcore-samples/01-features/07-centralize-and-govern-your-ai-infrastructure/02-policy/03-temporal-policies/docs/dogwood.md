---
title: The Dogwood Policy Language
description: 'Dogwood extends Cedar with temporal operators. A Dogwood policy has the same structure as a Cedar policy: a `permit` or `forbid` head followed by optional condition blocks, with one addition: the `when temporal { }` block for history-aware conditions.'
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/01-features/07-centralize-and-govern-your-ai-infrastructure/02-policy/03-temporal-policies/docs/dogwood.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# The Dogwood Policy Language

Dogwood extends Cedar with temporal operators. A Dogwood policy has the same structure as a Cedar policy: a `permit` or `forbid` head followed by optional condition blocks, with one addition: the `when temporal { }` block for history-aware conditions.

A single policy can carry all three block types at once:

- `when { }`: standard Cedar conditions evaluated against the current request's attributes
- `when temporal { }`: conditions evaluated against the session's recorded history
- `unless { }`: conditions that, if true, cause a `permit` to not apply (or a `forbid` to not trigger)

All blocks that are present must hold simultaneously for the policy to apply. This lets you combine a historical requirement with a content-based guardrail check and a principal-attribute check in a single, readable rule.

Because Dogwood is a superset of Cedar, every valid Cedar policy is also a valid Dogwood policy. Your existing point-in-time policies continue to work without changes, and you add temporal conditions only where a rule must consider more than the current request.

The complete Dogwood language reference is available at [https://dogwood-policy.github.io/dogwood/index.html](https://dogwood-policy.github.io/dogwood/index.html).

---

Next: [Policy Sessions](./sessions.md)

---
title: Benefits Advisor Instructions
description: Explain an Acme employee benefit, including eligibility, employee cost, coverage, and key details
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/01-features/06-observe-evaluate-optimize-your-agent/02-evaluate/skills-evaluation/skills/benefits-advisor/SKILL.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
original_frontmatter:
  name: benefits-advisor
  allowed-tools:
  - get_benefits_summary
---

# Benefits Advisor Instructions

Use this skill when an employee asks about health, dental, vision, 401(k), or life-insurance benefits.

## Required workflow

1. Identify the benefit type in the employee's request.
2. Call `get_benefits_summary` for that benefit type. Do not answer from general knowledge.
3. If the tool reports that the benefit type is unavailable, list the available types and ask the employee to choose one.
4. Return a concise **Benefits Summary** containing:
   - Benefit type
   - Eligibility
   - Employee cost
   - Coverage or employer contribution
   - Important plan details returned by the tool
5. Clearly distinguish plan facts from general guidance, and do not invent coverage, costs, or eligibility rules.

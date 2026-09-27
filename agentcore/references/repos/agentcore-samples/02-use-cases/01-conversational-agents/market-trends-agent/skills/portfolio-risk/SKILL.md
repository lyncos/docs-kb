---
title: Portfolio Risk Assessment Skill
description: Assess the risk profile of a set of stocks or a sector allocation, scoring concentration risk, volatility exposure, and overall risk tier
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/02-use-cases/01-conversational-agents/market-trends-agent/skills/portfolio-risk/SKILL.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
original_frontmatter:
  name: portfolio-risk
  allowed-tools:
  - get_stock_data
  - get_sector_data
---

# Portfolio Risk Assessment Skill

Use this skill when a user asks about portfolio risk, how risky a set of holdings is, concentration risk, diversification, or whether a portfolio is suitable for a given risk tolerance.

## Required workflow

1. For each stock in the portfolio, retrieve data using `get_stock_data`.
2. Retrieve sector data for each unique sector represented using `get_sector_data`.
3. Compute concentration risk:
   - If any single sector > 50% of holdings → **High Concentration Risk**
   - If any single sector 30–50% → **Moderate Concentration Risk**
   - Otherwise → **Diversified**
4. Assess volatility exposure:
   - High-beta sectors (Technology, Consumer Discretionary): count them
   - If > 50% of holdings in high-beta sectors → **High Volatility Exposure**
   - If 25–50% → **Moderate**; < 25% → **Low**
5. Identify the single largest risk factor from sector risk lists.
6. Score overall risk tier: **Conservative**, **Moderate**, **Aggressive**:
   - Conservative: Low volatility + Diversified
   - Aggressive: High volatility OR High Concentration
   - Moderate: all other combinations
7. Suggest one defensive addition (from Consumer Staples or Healthcare sectors) if risk is Aggressive.

## Output Format

```
Portfolio Risk Assessment
  Holdings analyzed : {symbols list}
  Sector breakdown  : {sector: count breakdown}
  Concentration     : {High | Moderate | Diversified}
  Volatility exposure: {High | Moderate | Low}
  Top risk factor   : {single biggest risk from sector data}
  Overall risk tier : {Conservative | Moderate | Aggressive}
  Recommendation    : {1-2 sentences on risk mitigation or confirmation}
```

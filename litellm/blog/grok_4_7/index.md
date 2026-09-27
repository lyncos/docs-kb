---
title: 'Day 0 Support: Grok 4.7'
description: Day 0 support for Grok 4.7 on LiteLLM, at the same price as Grok 4.6.
product: LiteLLM
section: blog/grok_4_7
source_url: https://docs.litellm.ai/blog/grok_4_7/grok_4_7
fetched: '2026-09-26'
tags:
- blog-grok-4-7
- litellm
original_frontmatter:
  slug: grok_4_7
  date: 2026-09-21 10:00:00
  image: ./hero.png
  authors:
  - misbah
  - mateo
  - kerry
  hide_table_of_contents: false
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

![LiteLLM x Grok 4.7](./hero.png)

LiteLLM supports `grok-4.7` on day 0, on `/chat/completions` and `/responses`. It keeps Grok 4.6's prices, limits and capabilities.

{/* truncate */}

SpaceXAI, the company formerly called xAI, built 4.7 and reports the model is better at checking its own work and holding long context. Against Grok 4.6, Terminal-Bench 4.0 goes from 20.3% to 38.0% and EEBench from 53.0% to 64.0%.

## Pricing

Per 1M tokens: $2.00 input, $0.50 cached, $6.00 output, identical to Grok 4.6. Every rate doubles past 200K input tokens, to $4.00, $1.00 and $12.00, so a long-context request costs twice what the headline suggests.

## Usage

<Tabs>
<TabItem value="sdk" label="SDK">

```python
from litellm import completion

response = completion(
    model="xai/grok-4.7",
    messages=[{"role": "user", "content": "Refactor this migration script."}],
    reasoning_effort="xhigh",  # low | medium | high (default) | xhigh
)

print(response.choices[0].message.content)
```

</TabItem>
<TabItem value="proxy" label="Proxy">

```yaml
model_list:
  - model_name: grok-4.7
    litellm_params:
      model: xai/grok-4.7
      api_key: os.environ/XAI_API_KEY

  - model_name: grok-4.7-openrouter
    litellm_params:
      model: openrouter/x-ai/grok-4.7
      api_key: os.environ/OPENROUTER_API_KEY
```

</TabItem>
</Tabs>

Pricing landed in [PR #42264](https://github.com/BerriAI/litellm/pull/42264). Hit **Reload Model Cost Map** in the Admin UI, or `POST /reload/model_cost_map`, to pick it up without a redeploy on `v1.76.0` and above.

## Feedback

Running Grok 4.7 through LiteLLM and hitting something unexpected? Share it on [GitHub discussion #42287](https://github.com/BerriAI/litellm/discussions/42287).

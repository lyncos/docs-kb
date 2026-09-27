---
title: '[BETA] Image Variations'
description: OpenAI's `/image/variations` endpoint is now supported.
product: LiteLLM
section: docs
source_url: https://docs.litellm.ai/docs/image_variations
fetched: '2026-09-26'
tags:
- docs
- litellm
---

# [BETA] Image Variations

OpenAI's `/image/variations` endpoint is now supported.

## Quick Start

```python
from litellm import image_variation
import os 

# set env vars 
os.environ["OPENAI_API_KEY"] = ""
os.environ["TOPAZ_API_KEY"] = ""

# openai call
response = image_variation(
    model="dall-e-2", image=image_url
)

# topaz call
response = image_variation(
    model="topaz/Standard V2", image=image_url
)

print(response)
```

## Supported Providers

- OpenAI
- Topaz

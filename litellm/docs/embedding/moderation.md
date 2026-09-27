---
title: litellm.moderation()
product: LiteLLM
section: docs/embedding
source_url: https://docs.litellm.ai/docs/embedding/moderation
fetched: '2026-09-26'
tags:
- docs-embedding
- litellm
---

# litellm.moderation()
LiteLLM supports the moderation endpoint for OpenAI

## Usage
```python
import os
from litellm import moderation
os.environ['OPENAI_API_KEY'] = ""
response = moderation(input="i'm ishaan cto of litellm")   
```

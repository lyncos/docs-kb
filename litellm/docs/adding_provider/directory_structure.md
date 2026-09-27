---
title: Directory Structure
description: 'When adding a new provider, you need to create a directory for the provider that follows the following structure:'
product: LiteLLM
section: docs/adding_provider
source_url: https://docs.litellm.ai/docs/adding_provider/directory_structure
fetched: '2026-09-26'
tags:
- docs-adding-provider
- litellm
---

# Directory Structure

When adding a new provider, you need to create a directory for the provider that follows the following structure:

```
litellm/llms/
└── provider_name/
    ├── completion/ # use when endpoint is equivalent to openai's `/v1/completions`
    │   ├── handler.py
    │   └── transformation.py
    ├── chat/ # use when endpoint is equivalent to openai's `/v1/chat/completions`
    │   ├── handler.py
    │   └── transformation.py
    ├── embed/ # use when endpoint is equivalent to openai's `/v1/embeddings`
    │   ├── handler.py
    │   └── transformation.py
    ├── audio_transcription/ # use when endpoint is equivalent to openai's `/v1/audio/transcriptions`
    │   ├── handler.py
    │   └── transformation.py
    └── rerank/ # use when endpoint is equivalent to cohere's `/rerank` endpoint.
        ├── handler.py
        └── transformation.py
```


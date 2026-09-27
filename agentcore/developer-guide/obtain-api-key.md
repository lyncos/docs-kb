---
title: Obtain API key
description: 'Once you have stored your API keys in the AgentCore Identity vault, you can retrieve them directly in your agent using the AgentCore SDK and the `@requires_api_key` annotation. For example, the code below will retrieve the API key from the “your-service-name” API key provider so '
product: Amazon Bedrock AgentCore
section: Developer Guide / obtain
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/obtain-api-key.html
fetched: '2026-09-26'
tags:
- agentcore
- obtain
---

# Obtain API key
<a name="obtain-api-key"></a>

Once you have stored your API keys in the AgentCore Identity vault, you can retrieve them directly in your agent using the AgentCore SDK and the `@requires_api_key` annotation. For example, the code below will retrieve the API key from the “your-service-name” API key provider so that you can use it in the `need_api_key` function.

```
import asyncio
from bedrock_agentcore.identity.auth import requires_api_key

@requires_api_key(
    provider_name= "your-service-name" # replace with your own credential provider name
)
async def need_api_key(*, api_key: str):
    # Use the API key
    pass

# To invoke:
# asyncio.run(need_api_key())
```
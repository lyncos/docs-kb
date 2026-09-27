---
title: 'auth: run ''gcloud auth application-default'''
description: https://github.com/BerriAI/litellm
product: Amazon Bedrock AgentCore
section: References / docs.litellm.ai
source_url: https://docs.litellm.ai
fetched: '2026-09-26'
tags:
- agentcore
- docs-litellm-ai
- reference
- related
referenced_by:
- harness-models.md
conversion: pandoc
---

[https://github.com/BerriAI/litellm](https://github.com/BerriAI/litellm)

## **Call 100+ LLMs using the OpenAI Input/Output Format**[​](#call-100-llms-using-the-openai-inputoutput-format "Direct link to call-100-llms-using-the-openai-inputoutput-format")

- Translate inputs to provider's endpoints (`/chat/completions`, `/responses`, `/embeddings`, `/images`, `/audio`, `/batches`, and more)
- [Consistent output](https://docs.litellm.ai/docs/supported_endpoints) - same response format regardless of which provider you use
- Retry/fallback logic across multiple deployments (e.g. Azure/OpenAI) - [Router](https://docs.litellm.ai/docs/routing)
- Track spend & set budgets per project [LiteLLM Proxy Server](https://docs.litellm.ai/docs/simple_proxy)

## How to use LiteLLM[​](#how-to-use-litellm "Direct link to How to use LiteLLM")

You can use LiteLLM through either the Proxy Server or Python SDK. Both gives you a unified interface to access multiple LLMs (100+ LLMs). Choose the option that best fits your needs:

**[LiteLLM Proxy Server](#litellm-proxy-server-llm-gateway)**

**[LiteLLM Python SDK](#basic-usage)**

**Use Case**

Central service (LLM Gateway) to access multiple LLMs

Use LiteLLM directly in your Python code

**Who Uses It?**

Gen AI Enablement / ML Platform Teams

Developers building LLM projects

**Key Features**

• Centralized API gateway with authentication & authorization  
• Multi-tenant cost tracking and spend management per project/user  
• Per-project customization (logging, guardrails, caching)  
• Virtual keys for secure access control  
• Admin dashboard UI for monitoring and management

• Direct Python library integration in your codebase  
• Router with retry/fallback logic across multiple deployments (e.g. Azure/OpenAI) - [Router](https://docs.litellm.ai/docs/routing)  
• Application-level load balancing and cost tracking  
• Exception handling with OpenAI-compatible errors  
• Observability callbacks (Lunary, MLflow, Langfuse, etc.)

## **LiteLLM Python SDK**[​](#litellm-python-sdk "Direct link to litellm-python-sdk")

### Basic usage[​](#basic-usage "Direct link to Basic usage")

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BerriAI/litellm/blob/main/cookbook/liteLLM_Getting_Started.ipynb)

``` prism-code
uv add litellm
```

- OpenAI
- Anthropic
- xAI
- VertexAI
- NVIDIA
- HuggingFace
- Azure OpenAI
- Ollama
- Openrouter
- Novita AI
- Vercel AI Gateway

``` prism-code
from litellm import completion
import os

## set ENV variables
os.environ["OPENAI_API_KEY"] = "your-api-key"

response = completion(
  model="openai/gpt-5",
  messages=[{ "content": "Hello, how are you?","role": "user"}]
)
```

``` prism-code
from litellm import completion
import os

## set ENV variables
os.environ["ANTHROPIC_API_KEY"] = "your-api-key"

response = completion(
  model="anthropic/claude-sonnet-4-5-20250929",
  messages=[{ "content": "Hello, how are you?","role": "user"}]
)
```

``` prism-code
from litellm import completion
import os

## set ENV variables
os.environ["XAI_API_KEY"] = "your-api-key"

response = completion(
  model="xai/grok-2-latest",
  messages=[{ "content": "Hello, how are you?","role": "user"}]
)
```

``` prism-code
from litellm import completion
import os

# auth: run 'gcloud auth application-default'
os.environ["VERTEXAI_PROJECT"] = "hardy-device-386718"
os.environ["VERTEXAI_LOCATION"] = "us-central1"

response = completion(
  model="vertex_ai/gemini-1.5-pro",
  messages=[{ "content": "Hello, how are you?","role": "user"}]
)
```

``` prism-code
from litellm import completion
import os

## set ENV variables
os.environ["NVIDIA_NIM_API_KEY"] = "nvidia_api_key"
os.environ["NVIDIA_NIM_API_BASE"] = "nvidia_nim_endpoint_url"

response = completion(
  model="nvidia_nim/<model_name>",
  messages=[{ "content": "Hello, how are you?","role": "user"}]
)
```

``` prism-code
from litellm import completion
import os

os.environ["HUGGINGFACE_API_KEY"] = "huggingface_api_key"

# e.g. Call 'WizardLM/WizardCoder-Python-34B-V1.0' hosted on HF Inference endpoints
response = completion(
  model="huggingface/WizardLM/WizardCoder-Python-34B-V1.0",
  messages=[{ "content": "Hello, how are you?","role": "user"}],
  api_base="https://my-endpoint.huggingface.cloud"
)

print(response)
```

``` prism-code
from litellm import completion
import os

## set ENV variables
os.environ["AZURE_API_KEY"] = ""
os.environ["AZURE_API_BASE"] = ""
os.environ["AZURE_API_VERSION"] = ""

# azure call
response = completion(
  "azure/<your_deployment_name>",
  messages = [{ "content": "Hello, how are you?","role": "user"}]
)
```

``` prism-code
from litellm import completion

response = completion(
            model="ollama/llama2",
            messages = [{ "content": "Hello, how are you?","role": "user"}],
            api_base="http://localhost:11434"
)
```

``` prism-code
from litellm import completion
import os

## set ENV variables
os.environ["OPENROUTER_API_KEY"] = "openrouter_api_key"

response = completion(
  model="openrouter/google/palm-2-chat-bison",
  messages = [{ "content": "Hello, how are you?","role": "user"}],
)
```

``` prism-code
from litellm import completion
import os

## set ENV variables. Visit https://novita.ai/settings/key-management to get your API key
os.environ["NOVITA_API_KEY"] = "novita-api-key"

response = completion(
  model="novita/deepseek/deepseek-r1",
  messages=[{ "content": "Hello, how are you?","role": "user"}]
)
```

``` prism-code
from litellm import completion
import os

## set ENV variables. Visit https://vercel.com/docs/ai-gateway#using-the-ai-gateway-with-an-api-key for instructions on obtaining a key
os.environ["VERCEL_AI_GATEWAY_API_KEY"] = "your-vercel-api-key"

response = completion(
  model="vercel_ai_gateway/openai/gpt-5",
  messages=[{ "content": "Hello, how are you?","role": "user"}]
)
```

### Response Format (OpenAI Chat Completions Format)[​](#response-format-openai-chat-completions-format "Direct link to Response Format (OpenAI Chat Completions Format)")

``` prism-code
{
    "id": "chatcmpl-565d891b-a42e-4c39-8d14-82a1f5208885",
    "created": 1734366691,
    "model": "gpt-5",
    "object": "chat.completion",
    "system_fingerprint": null,
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "message": {
                "content": "Hello! As an AI language model, I don't have feelings, but I'm operating properly and ready to assist you with any questions or tasks you may have. How can I help you today?",
                "role": "assistant",
                "tool_calls": null,
                "function_call": null
            }
        }
    ],
    "usage": {
        "completion_tokens": 43,
        "prompt_tokens": 13,
        "total_tokens": 56,
        "completion_tokens_details": null,
        "prompt_tokens_details": {
            "audio_tokens": null,
            "cached_tokens": 0
        },
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0
    }
}
```

### Responses API[​](#responses-api "Direct link to Responses API")

Use `litellm.responses()` for advanced models that support reasoning content like GPT-5, o3, etc.

- OpenAI
- Anthropic (Claude)
- VertexAI
- Azure OpenAI

``` prism-code
from litellm import responses
import os

## set ENV variables
os.environ["OPENAI_API_KEY"] = "your-api-key"

response = responses(
  model="gpt-5-mini",
  messages=[{ "content": "What is the capital of France?","role": "user"}],
  reasoning_effort="medium"
)

print(response)
print(response.choices[0].message.content) # response
print(response.choices[0].message.reasoning_content) # reasoning
```

``` prism-code
from litellm import responses
import os

## set ENV variables
os.environ["ANTHROPIC_API_KEY"] = "your-api-key"

response = responses(
  model="claude-3.5-sonnet",
  messages=[{ "content": "What is the capital of France?","role": "user"}]
)
```

``` prism-code
from litellm import responses
import os

# auth: run 'gcloud auth application-default'
os.environ["VERTEXAI_PROJECT"] = "jr-smith-386718"
os.environ["VERTEXAI_LOCATION"] = "us-central1"

response = responses(
  model="vertex_ai/gemini-1.5-pro",
  messages=[{ "content": "What is the capital of France?","role": "user"}]
)
```

``` prism-code
from litellm import responses
import os

## set ENV variables
os.environ["AZURE_API_KEY"] = ""
os.environ["AZURE_API_BASE"] = ""
os.environ["AZURE_API_VERSION"] = ""

# azure call
response = responses(
  "azure/<your_deployment_name>",
  messages = [{ "content": "What is the capital of France?","role": "user"}]
)

print(response)
```

### Streaming[​](#streaming "Direct link to Streaming")

Set `stream=True` in the `completion` args.

- OpenAI
- Anthropic
- xAI
- VertexAI
- NVIDIA
- HuggingFace
- Azure OpenAI
- Ollama
- Openrouter
- Novita AI
- Vercel AI Gateway

``` prism-code
from litellm import completion
import os

## set ENV variables
os.environ["OPENAI_API_KEY"] = "your-api-key"

response = completion(
  model="openai/gpt-5",
  messages=[{ "content": "Hello, how are you?","role": "user"}],
  stream=True,
)
```

``` prism-code
from litellm import completion
import os

## set ENV variables
os.environ["ANTHROPIC_API_KEY"] = "your-api-key"

response = completion(
  model="anthropic/claude-sonnet-4-5-20250929",
  messages=[{ "content": "Hello, how are you?","role": "user"}],
  stream=True,
)
```

``` prism-code
from litellm import completion
import os

## set ENV variables
os.environ["XAI_API_KEY"] = "your-api-key"

response = completion(
  model="xai/grok-2-latest",
  messages=[{ "content": "Hello, how are you?","role": "user"}],
  stream=True,
)
```

``` prism-code
from litellm import completion
import os

# auth: run 'gcloud auth application-default'
os.environ["VERTEXAI_PROJECT"] = "hardy-device-386718"
os.environ["VERTEXAI_LOCATION"] = "us-central1"

response = completion(
  model="vertex_ai/gemini-1.5-pro",
  messages=[{ "content": "Hello, how are you?","role": "user"}],
  stream=True,
)
```

``` prism-code
from litellm import completion
import os

## set ENV variables
os.environ["NVIDIA_NIM_API_KEY"] = "nvidia_api_key"
os.environ["NVIDIA_NIM_API_BASE"] = "nvidia_nim_endpoint_url"

response = completion(
  model="nvidia_nim/<model_name>",
  messages=[{ "content": "Hello, how are you?","role": "user"}],
  stream=True,
)
```

``` prism-code
from litellm import completion
import os

os.environ["HUGGINGFACE_API_KEY"] = "huggingface_api_key"

# e.g. Call 'WizardLM/WizardCoder-Python-34B-V1.0' hosted on HF Inference endpoints
response = completion(
  model="huggingface/WizardLM/WizardCoder-Python-34B-V1.0",
  messages=[{ "content": "Hello, how are you?","role": "user"}],
  api_base="https://my-endpoint.huggingface.cloud",
  stream=True,
)

print(response)
```

``` prism-code
from litellm import completion
import os

## set ENV variables
os.environ["AZURE_API_KEY"] = ""
os.environ["AZURE_API_BASE"] = ""
os.environ["AZURE_API_VERSION"] = ""

# azure call
response = completion(
  "azure/<your_deployment_name>",
  messages = [{ "content": "Hello, how are you?","role": "user"}],
  stream=True,
)
```

``` prism-code
from litellm import completion

response = completion(
            model="ollama/llama2",
            messages = [{ "content": "Hello, how are you?","role": "user"}],
            api_base="http://localhost:11434",
            stream=True,
)
```

``` prism-code
from litellm import completion
import os

## set ENV variables
os.environ["OPENROUTER_API_KEY"] = "openrouter_api_key"

response = completion(
  model="openrouter/google/palm-2-chat-bison",
  messages = [{ "content": "Hello, how are you?","role": "user"}],
  stream=True,
)
```

``` prism-code
from litellm import completion
import os

## set ENV variables. Visit https://novita.ai/settings/key-management to get your API key
os.environ["NOVITA_API_KEY"] = "novita_api_key"

response = completion(
  model="novita/deepseek/deepseek-r1",
  messages = [{ "content": "Hello, how are you?","role": "user"}],
  stream=True,
)
```

``` prism-code
from litellm import completion
import os

## set ENV variables. Visit https://vercel.com/docs/ai-gateway#using-the-ai-gateway-with-an-api-key for instructions on obtaining a key
os.environ["VERCEL_AI_GATEWAY_API_KEY"] = "your-vercel-api-key"

response = completion(
  model="vercel_ai_gateway/openai/gpt-5",
  messages = [{ "content": "Hello, how are you?","role": "user"}],
  stream=True,
)
```

### Streaming Response Format (OpenAI Format)[​](#streaming-response-format-openai-format "Direct link to Streaming Response Format (OpenAI Format)")

``` prism-code
{
    "id": "chatcmpl-2be06597-eb60-4c70-9ec5-8cd2ab1b4697",
    "created": 1734366925,
    "model": "claude-sonnet-4-5-20250929",
    "object": "chat.completion.chunk",
    "system_fingerprint": null,
    "choices": [
        {
            "finish_reason": null,
            "index": 0,
            "delta": {
                "content": "Hello",
                "role": "assistant",
                "function_call": null,
                "tool_calls": null,
                "audio": null
            },
            "logprobs": null
        }
    ]
}
```

### Exception handling[​](#exception-handling "Direct link to Exception handling")

LiteLLM maps exceptions across all supported providers to the OpenAI exceptions. All our exceptions inherit from OpenAI's exception types, so any error-handling you have for that, should work out of the box with LiteLLM.

``` prism-code
import litellm
from litellm import completion
import os

os.environ["ANTHROPIC_API_KEY"] = "bad-key"
try:
    completion(model="anthropic/claude-instant-1", messages=[{"role": "user", "content": "Hey, how's it going?"}])
except litellm.AuthenticationError as e:
    # Thrown when the API key is invalid
    print(f"Authentication failed: {e}")
except litellm.RateLimitError as e:
    # Thrown when you've exceeded your rate limit
    print(f"Rate limited: {e}")
except litellm.APIError as e:
    # Thrown for general API errors
    print(f"API error: {e}")
```

### Logging Observability - Log LLM Input/Output ([Docs](https://docs.litellm.ai/docs/observability/callbacks))[​](#logging-observability---log-llm-inputoutput-docs "Direct link to logging-observability---log-llm-inputoutput-docs")

LiteLLM exposes pre defined callbacks to send data to MLflow, Lunary, Langfuse, Helicone, Promptlayer, Traceloop, Slack

``` prism-code
from litellm import completion

## set env variables for logging tools (API key set up is not required when using MLflow)
os.environ["LUNARY_PUBLIC_KEY"] = "your-lunary-public-key" # get your key at https://app.lunary.ai/settings
os.environ["HELICONE_API_KEY"] = "your-helicone-key"
os.environ["LANGFUSE_PUBLIC_KEY"] = ""
os.environ["LANGFUSE_SECRET_KEY"] = ""

os.environ["OPENAI_API_KEY"]

# set callbacks
litellm.success_callback = ["lunary", "mlflow", "langfuse", "helicone"] # log input/output to lunary, mlflow, langfuse, helicone

#openai call
response = completion(model="openai/gpt-5", messages=[{"role": "user", "content": "Hi 👋 - i'm openai"}])
```

### Track Costs, Usage, Latency for streaming[​](#track-costs-usage-latency-for-streaming "Direct link to Track Costs, Usage, Latency for streaming")

Use a callback function for this - more info on custom callbacks: [https://docs.litellm.ai/docs/observability/custom_callback](https://docs.litellm.ai/docs/observability/custom_callback)

``` prism-code
import litellm

# track_cost_callback
def track_cost_callback(
    kwargs,                 # kwargs to completion
    completion_response,    # response from completion
    start_time, end_time    # start/end time
):
    try:
      response_cost = kwargs.get("response_cost", 0)
      print("streaming response_cost", response_cost)
    except:
        pass
# set callback
litellm.success_callback = [track_cost_callback] # set custom callback function

# litellm.completion() call
response = completion(
    model="openai/gpt-5",
    messages=[
        {
            "role": "user",
            "content": "Hi 👋 - i'm openai"
        }
    ],
    stream=True
)
```

## **LiteLLM Proxy Server (LLM Gateway)**[​](#litellm-proxy-server-llm-gateway "Direct link to litellm-proxy-server-llm-gateway")

Track spend across multiple projects/people

![ui_3](https://github.com/BerriAI/litellm/assets/29436595/47c97d5e-b9be-4839-b28c-43d7f4f10033)

The proxy provides:

1.  [Hooks for auth](https://docs.litellm.ai/docs/proxy/virtual_keys#custom-auth)
2.  [Hooks for logging](https://docs.litellm.ai/docs/proxy/logging#step-1---create-your-custom-litellm-callback-class)
3.  [Cost tracking](https://docs.litellm.ai/docs/proxy/virtual_keys#tracking-spend)
4.  [Rate Limiting](https://docs.litellm.ai/docs/proxy/users#set-rate-limits)

### 📖 Proxy Endpoints - [Swagger Docs](https://docs.litellm.ai/api-reference/)[​](#-proxy-endpoints---swagger-docs "Direct link to -proxy-endpoints---swagger-docs")

Go here for a complete tutorial with keys + rate limits - [**here**](https://docs.litellm.ai/docs/proxy/docker_quick_start)

### Quick Start Proxy - CLI[​](#quick-start-proxy---cli "Direct link to Quick Start Proxy - CLI")

``` prism-code
uv tool install 'litellm[proxy]'
```

#### Step 1: Start litellm proxy[​](#step-1-start-litellm-proxy "Direct link to Step 1: Start litellm proxy")

- LiteLLM CLI
- Docker container

``` prism-code
$ litellm --model huggingface/bigcode/starcoder

#INFO: Proxy running on http://0.0.0.0:4000
```

### Step 1. CREATE config.yaml[​](#step-1-create-configyaml "Direct link to Step 1. CREATE config.yaml")

Example `litellm_config.yaml`

``` prism-code
model_list:
  - model_name: gpt-5
    litellm_params:
      model: azure/<your-azure-model-deployment>
      api_base: os.environ/AZURE_API_BASE # runs os.getenv("AZURE_API_BASE")
      api_key: os.environ/AZURE_API_KEY # runs os.getenv("AZURE_API_KEY")
      api_version: "2023-07-01-preview"

general_settings:
  master_key: os.environ/LITELLM_MASTER_KEY
  database_url: postgres://
```

### Step 2. RUN Docker Image[​](#step-2-run-docker-image "Direct link to Step 2. RUN Docker Image")

``` prism-code
docker run \
    -v $(pwd)/litellm_config.yaml:/app/config.yaml \
    -e AZURE_API_KEY=d6*********** \
    -e AZURE_API_BASE=https://openai-***********/ \
    -p 4000:4000 \
    docker.litellm.ai/berriai/litellm:main-latest \
    --config /app/config.yaml --detailed_debug
```

#### Step 2: Make ChatCompletions Request to Proxy[​](#step-2-make-chatcompletions-request-to-proxy "Direct link to Step 2: Make ChatCompletions Request to Proxy")

- Chat Completions
- Responses API

``` prism-code
import openai # openai v1.0.0+
client = openai.OpenAI(api_key="anything",base_url="http://0.0.0.0:4000") # set proxy to base_url
# request sent to model set on litellm proxy, `litellm --model`
response = client.chat.completions.create(model="gpt-5", messages = [
    {
        "role": "user",
        "content": "this is a test request, write a short poem"
    }
])

print(response)
```

``` prism-code
from openai import OpenAI

client = OpenAI(
    api_key="sk-<your-litellm-api-key>",
    base_url="http://0.0.0.0:4000"
)

response = client.responses.create(
  model="gpt-5",
  input="Tell me a three sentence bedtime story about a unicorn."
)

print(response)
```

## More details[​](#more-details "Direct link to More details")

- [exception mapping](/docs/exception_mapping)
- [E2E Tutorial for LiteLLM Proxy Server](/docs/proxy/docker_quick_start)
- [proxy virtual keys & spend management](/docs/proxy/virtual_keys)

- [**Call 100+ LLMs using the OpenAI Input/Output Format**](#call-100-llms-using-the-openai-inputoutput-format)
- [How to use LiteLLM](#how-to-use-litellm)
- [**LiteLLM Python SDK**](#litellm-python-sdk)
  - [Basic usage](#basic-usage)
  - [Response Format (OpenAI Chat Completions Format)](#response-format-openai-chat-completions-format)
  - [Responses API](#responses-api)
  - [Streaming](#streaming)
  - [Streaming Response Format (OpenAI Format)](#streaming-response-format-openai-format)
  - [Exception handling](#exception-handling)
  - [Logging Observability - Log LLM Input/Output (Docs)](#logging-observability---log-llm-inputoutput-docs)
  - [Track Costs, Usage, Latency for streaming](#track-costs-usage-latency-for-streaming)
- [**LiteLLM Proxy Server (LLM Gateway)**](#litellm-proxy-server-llm-gateway)
  - [📖 Proxy Endpoints - Swagger Docs](#-proxy-endpoints---swagger-docs)
  - [Quick Start Proxy - CLI](#quick-start-proxy---cli)
  - [Step 1. CREATE config.yaml](#step-1-create-configyaml)
  - [Step 2. RUN Docker Image](#step-2-run-docker-image)
- [More details](#more-details)

🚅

LiteLLM Enterprise

SSO/SAML, audit logs, spend tracking, multi-team management, and guardrails — built for production.

[Learn more →](/docs/enterprise)

---
title: openllmetry
description: traceloop / **openllmetry** Public
product: Amazon Bedrock AgentCore
section: References / github.com
source_url: https://github.com/traceloop/openllmetry
fetched: '2026-09-26'
tags:
- agentcore
- github-com
- reference
- related
referenced_by:
- observability-configure.md
conversion: pandoc
---

[traceloop](/traceloop) / **[openllmetry](/traceloop/openllmetry)** Public

- [Notifications](/login?return_to=%2Ftraceloop%2Fopenllmetry) You must be signed in to change notification settings

- [Fork 1.1k](/login?return_to=%2Ftraceloop%2Fopenllmetry)

- [ Star 7.5k](/login?return_to=%2Ftraceloop%2Fopenllmetry)

[](/traceloop/openllmetry)

main

[Branches](/traceloop/openllmetry/branches)[Tags](/traceloop/openllmetry/tags)

[](/traceloop/openllmetry/branches)[](/traceloop/openllmetry/tags)

Go to file

Code

Open more actions menu

## Latest commit

 

## History

[1,419 Commits](/traceloop/openllmetry/commits/main/)

[](/traceloop/openllmetry/commits/main/)1,419 Commits

## Folders and files

[TABLE]

## Repository files navigation

[![](https://raw.githubusercontent.com/traceloop/openllmetry/main/img/logo-light.png)](https://www.traceloop.com/openllmetry#gh-light-mode-only) [![](https://raw.githubusercontent.com/traceloop/openllmetry/main/img/logo-dark.png)](https://www.traceloop.com/openllmetry#gh-dark-mode-only)

Open-source observability for your LLM application

#### [**Get started »**](https://traceloop.com/docs/openllmetry/getting-started-python)  [Slack](https://traceloop.com/slack) \| [Docs](https://traceloop.com/docs/openllmetry/introduction) \| [Website](https://www.traceloop.com/openllmetry)

[](#----get-started-----------slack---docs---website)

#### [![](https://camo.githubusercontent.com/08ebf7d51ab5d26aa07ef8ce12799b42ae5f0d8dff1a096a81c014925ea24110/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f72656c656173652f74726163656c6f6f702f6f70656e6c6c6d65747279)](https://github.com/traceloop/openllmetry/releases) [![](https://camo.githubusercontent.com/3e82e0ab62bf70c16ecac62232c2bbb83fb76115eff7f1717de8eb30c0bd5a91/68747470733a2f2f7374617469632e706570792e746563682f62616467652f6f70656e74656c656d657472792d696e737472756d656e746174696f6e2d6f70656e61692f6d6f6e7468)](https://pepy.tech/project/opentelemetry-instrumentation-openai) [![OpenLLMetry is released under the Apache-2.0 License](https://camo.githubusercontent.com/8b070c15932a4d8d10def730bae59a3746212a59d6948c0ea8118bccc248dbc2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d41706163686520322e302d626c75652e737667)](https://github.com/traceloop/openllmetry/blob/main/LICENSE) [![](https://github.com/traceloop/openllmetry/actions/workflows/ci.yml/badge.svg)](https://github.com/traceloop/openllmetry/actions/workflows/ci.yml) [![git commit activity](https://camo.githubusercontent.com/9825524dafa9b1acb53a25de7a4223c9744812f507e2bfa63032e9178eda8054/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f636f6d6d69742d61637469766974792f6d2f74726163656c6f6f702f6f70656e6c6c6d65747279)](https://github.com/traceloop/openllmetry/issues) [![](https://camo.githubusercontent.com/98434cc5073c57fed966f2a34648b7ced3c313f697987b87bd893ed30e1d9c7c/68747470733a2f2f696d672e736869656c64732e696f2f776562736974653f636f6c6f723d25323366323635323226646f776e5f6d6573736167653d59253230436f6d62696e61746f72266c6162656c3d4261636b6564266c6f676f3d79636f6d62696e61746f72267374796c653d666c61742d7371756172652675705f6d6573736167653d59253230436f6d62696e61746f722675726c3d68747470732533412532462532467777772e79636f6d62696e61746f722e636f6d)](https://www.ycombinator.com/companies/traceloop) [![PRs welcome!](https://camo.githubusercontent.com/8b64edb761ec7596a43482857c533fd47931c4ca8842545ea8668db29dc09705/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5052732d57656c636f6d652d627269676874677265656e)](https://github.com/traceloop/openllmetry/blob/main/CONTRIBUTING.md) [![Slack community channel](https://camo.githubusercontent.com/7ee1ecd410834b74b55b71c37b136b835c0e9b3697cf51c9090ae9739fecddc5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636861742d6f6e253230536c61636b2d626c756576696f6c6574)](https://traceloop.com/slack) [![Traceloop Twitter](https://camo.githubusercontent.com/d5714cb1ba7d9343c4b45fe0a30e070c870fa852148caadb0d454471c0b1160c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f666f6c6c6f772d25343074726163656c6f6f706465762d3144413146323f6c6f676f3d74776974746572267374796c653d736f6369616c)](https://twitter.com/traceloopdev)

[](#---------------------------------------------------------------)

**🎉 New**: Our semantic conventions are now part of OpenTelemetry! Join the [discussion](https://github.com/open-telemetry/community/blob/1c71595874e5d125ca92ec3b0e948c4325161c8a/projects/llm-semconv.md) and help us shape the future of LLM observability.

Looking for the JS/TS version? Check out [OpenLLMetry-JS](https://github.com/traceloop/openllmetry-js).

OpenLLMetry is a set of extensions built on top of [OpenTelemetry](https://opentelemetry.io/) that gives you complete observability over your LLM application. Because it uses OpenTelemetry under the hood, [it can be connected to your existing observability solutions](https://www.traceloop.com/docs/openllmetry/integrations/introduction) - Datadog, Honeycomb, and others.

It's built and maintained by Traceloop under the Apache 2.0 license.

The repo contains standard OpenTelemetry instrumentations for LLM providers and Vector DBs, as well as a Traceloop SDK that makes it easy to get started with OpenLLMetry, while still outputting standard OpenTelemetry data that can be connected to your observability stack. If you already have OpenTelemetry instrumented, you can just add any of our instrumentations directly.

## 🚀 Getting Started

[](#-getting-started)

The easiest way to get started is to use our SDK. For a complete guide, go to our [docs](https://traceloop.com/docs/openllmetry/getting-started-python).

Install the SDK:

    pip install traceloop-sdk

Then, to start instrumenting your code, just add this line to your code:

    from traceloop.sdk import Traceloop

    Traceloop.init()

That's it. You're now tracing your code with OpenLLMetry! If you're running this locally, you may want to disable batch sending, so you can see the traces immediately:

    Traceloop.init(disable_batch=True)

## ⏫ Supported (and tested) destinations

[](#-supported-and-tested-destinations)

- ✅ [Traceloop](https://www.traceloop.com/docs/openllmetry/integrations/traceloop)
- ✅ [Axiom](https://www.traceloop.com/docs/openllmetry/integrations/axiom)
- ✅ [Azure Application Insights](https://www.traceloop.com/docs/openllmetry/integrations/azure)
- ✅ [Braintrust](https://www.traceloop.com/docs/openllmetry/integrations/braintrust)
- ✅ [Dash0](https://www.traceloop.com/docs/openllmetry/integrations/dash0)
- ✅ [Datadog](https://www.traceloop.com/docs/openllmetry/integrations/datadog)
- ✅ [Dynatrace](https://www.traceloop.com/docs/openllmetry/integrations/dynatrace)
- ✅ [Google Cloud](https://www.traceloop.com/docs/openllmetry/integrations/gcp)
- ✅ [Grafana](https://www.traceloop.com/docs/openllmetry/integrations/grafana)
- ✅ [Highlight](https://www.traceloop.com/docs/openllmetry/integrations/highlight)
- ✅ [Honeycomb](https://www.traceloop.com/docs/openllmetry/integrations/honeycomb)
- ✅ [HyperDX](https://www.traceloop.com/docs/openllmetry/integrations/hyperdx)
- ✅ [IBM Instana](https://www.traceloop.com/docs/openllmetry/integrations/instana)
- ✅ [KloudMate](https://www.traceloop.com/docs/openllmetry/integrations/kloudmate)
- ✅ [Laminar](https://www.traceloop.com/docs/openllmetry/integrations/laminar)
- ✅ [New Relic](https://www.traceloop.com/docs/openllmetry/integrations/newrelic)
- ✅ [OpenTelemetry Collector](https://www.traceloop.com/docs/openllmetry/integrations/otel-collector)
- ✅ [Oracle Cloud](https://www.traceloop.com/docs/openllmetry/integrations/oraclecloud)
- ✅ [Scorecard](https://www.traceloop.com/docs/openllmetry/integrations/scorecard)
- ✅ [Service Now Cloud Observability](https://www.traceloop.com/docs/openllmetry/integrations/service-now)
- ✅ [SigNoz](https://www.traceloop.com/docs/openllmetry/integrations/signoz)
- ✅ [Sentry](https://www.traceloop.com/docs/openllmetry/integrations/sentry)
- ✅ [Splunk](https://www.traceloop.com/docs/openllmetry/integrations/splunk)
- ✅ [Tencent Cloud](https://www.traceloop.com/docs/openllmetry/integrations/tencent)

See [our docs](https://traceloop.com/docs/openllmetry/integrations/exporting) for instructions on connecting to each one.

## 🪗 What do we instrument?

[](#-what-do-we-instrument)

OpenLLMetry can instrument everything that [OpenTelemetry already instruments](https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation) - so things like your DB, API calls, and more. On top of that, we built a set of custom extensions that instrument things like your calls to OpenAI or Anthropic, or your Vector DB like Chroma, Pinecone, Qdrant or Weaviate.

- ✅ [Aleph Alpha](https://www.aleph-alpha.com/)
- ✅ [Anthropic](https://www.anthropic.com/)
- ✅ [Bedrock (AWS)](https://aws.amazon.com/bedrock/)
- ✅ [Cohere](https://cohere.com/)
- ✅ [Google Generative AI (Gemini)](https://ai.google/)
- ✅ [Groq](https://groq.com/)
- ✅ [HuggingFace](https://huggingface.co/)
- ✅ [IBM Watsonx AI](https://www.ibm.com/watsonx)
- ✅ [Mistral AI](https://mistral.ai/)
- ✅ [Ollama](https://ollama.com/)
- ✅ [OpenAI / Azure OpenAI](https://openai.com/)
- ✅ [Replicate](https://replicate.com/)
- ✅ [SageMaker (AWS)](https://aws.amazon.com/sagemaker/)
- ✅ [Together AI](https://together.xyz/)
- ✅ [Vertex AI (GCP)](https://cloud.google.com/vertex-ai)
- ✅ [WRITER](https://writer.com/)

### Vector DBs

[](#vector-dbs)

- ✅ [Chroma](https://www.trychroma.com/)
- ✅ [LanceDB](https://lancedb.com/)
- ✅ [Marqo](https://marqo.ai/)
- ✅ [Milvus](https://milvus.io/)
- ✅ [Pinecone](https://www.pinecone.io/)
- ✅ [Qdrant](https://qdrant.tech/)
- ✅ [Weaviate](https://weaviate.io/)

### Frameworks

[](#frameworks)

- ✅ [Agno](https://github.com/agno-agi/agno)
- ✅ [AWS Strands](https://strandsagents.com/) (built-in OTEL support)
- ✅ [CrewAI](https://docs.crewai.com/introduction)
- ✅ [Haystack](https://haystack.deepset.ai/integrations/traceloop)
- ✅ [LangChain](https://python.langchain.com/docs/introduction/)
- ✅ [Langflow](https://docs.langflow.org/)
- ✅ [LangGraph](https://langchain-ai.github.io/langgraph/concepts/why-langgraph/)
- ✅ [LiteLLM](https://docs.litellm.ai/docs/observability/opentelemetry_integration)
- ✅ [LlamaIndex](https://docs.llamaindex.ai/en/stable/module_guides/observability/observability.html#openllmetry)
- ✅ [OpenAI Agents](https://openai.github.io/openai-agents-python/)

### Protocol

[](#protocol)

- ✅ [MCP](https://modelcontextprotocol.io/)

## 🔎 Telemetry

[](#-telemetry)

We no longer log or collect any telemetry in the SDK or in the instrumentations. Make sure to bump to v0.49.2 and above.

### Why we collect telemetry

[](#why-we-collect-telemetry)

- The primary purpose is to detect exceptions within instrumentations. Since LLM providers frequently update their APIs, this helps us quickly identify and fix any breaking changes.
- We only collect anonymous data, with no personally identifiable information. You can view exactly what data we collect in our [Privacy documentation](https://www.traceloop.com/docs/openllmetry/privacy/telemetry).
- Telemetry is only collected in the SDK. If you use the instrumentations directly without the SDK, no telemetry is collected.

## 🌱 Contributing

[](#-contributing)

Whether big or small, we love contributions ❤️ Check out our guide to see how to [get started](https://traceloop.com/docs/openllmetry/contributing/overview).

Not sure where to get started? You can:

- [Book a free pairing session with one of our teammates](mailto:nir@traceloop.com?subject=Pairing%20session&body=I'd%20like%20to%20do%20a%20pairing%20session!)!
- Join our [Slack](https://traceloop.com/slack), and ask us any questions there.

## 💚 Community & Support

[](#-community--support)

- [Slack](https://traceloop.com/slack) (For live discussion with the community and the Traceloop team)
- [GitHub Discussions](https://github.com/traceloop/openllmetry/discussions) (For help with building and deeper conversations about features)
- [GitHub Issues](https://github.com/traceloop/openllmetry/issues) (For any bugs and errors you encounter using OpenLLMetry)
- [Twitter](https://twitter.com/traceloopdev) (Get news fast)

## 🙏 Special Thanks

[](#-special-thanks)

To @patrickdebois, who [suggested the great name](https://x.com/patrickdebois/status/1695518950715473991?s=46&t=zn2SOuJcSVq-Pe2Ysevzkg) we're now using for this repo!

## 💫 Contributors

[](#-contributors)

[![contributors](https://camo.githubusercontent.com/46c766f3d08f47282afc3e8120a83fdad21b57422cef39f04bb5847f144c34cf/68747470733a2f2f636f6e747269622e726f636b732f696d6167653f7265706f3d74726163656c6f6f702f6f70656e6c6c6d65747279)](https://github.com/traceloop/openllmetry/graphs/contributors)

## About

Open-source observability for your GenAI or LLM application, based on OpenTelemetry

[www.traceloop.com/openllmetry](https://www.traceloop.com/openllmetry)

### Topics

[artifical-intelligence](/topics/artifical-intelligence)[datascience](/topics/datascience)[generative-ai](/topics/generative-ai)[good-first-issue](/topics/good-first-issue)[good-first-issues](/topics/good-first-issues)[help-wanted](/topics/help-wanted)[llm](/topics/llm)[llmops](/topics/llmops)[metrics](/topics/metrics)[ml](/topics/ml)[model-monitoring](/topics/model-monitoring)[monitoring](/topics/monitoring)[observability](/topics/observability)[open-source](/topics/open-source)[open-telemetry](/topics/open-telemetry)[opentelemetry](/topics/opentelemetry)[opentelemetry-python](/topics/opentelemetry-python)[python](/topics/python)

### Resources

[Readme](#readme-ov-file)

[Apache-2.0 license](#Apache-2.0-1-ov-file)

### Code of conduct

[Code of conduct](/traceloop/openllmetry#coc-ov-file)

### Contributing

[Contributing](#contributing-ov-file)

### Security policy

[Security policy](#security-ov-file)

[Activity](/traceloop/openllmetry/activity)

[Custom properties](/traceloop/openllmetry/custom-properties)

### Stars

**7.5k** stars

### Watchers

**21** watching

### Forks

[**1.1k** forks](/traceloop/openllmetry/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Ftraceloop%2Fopenllmetry&report=traceloop+%28user%29)

## Releases

## Used by

## Contributors

## Languages

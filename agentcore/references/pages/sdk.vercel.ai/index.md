---
title: Universal AI layer for building frameworks and agents
description: '[](https://vercel.com/oss)'
product: Amazon Bedrock AgentCore
section: References / sdk.vercel.ai
source_url: https://sdk.vercel.ai
fetched: '2026-09-26'
tags:
- agentcore
- reference
- related
- sdk-vercel-ai
referenced_by:
- supported-frameworks-vercel-ai.md
conversion: pandoc
---

[](https://vercel.com/oss)

Grok 4.7 is now available in the AI SDK. [Learn more.](/providers/ai-sdk-providers/xai)

# Universal AI layer for building frameworks and agents

A unified TypeScript SDK for building AI apps with modern streaming, fallbacks, and multi-model support—powered by Vercel

For humans

For agents

\$npm install ainpm install ai

Text Generation

Image Generation

Speech

Transcription

Video Generation

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-grok-color-light.0_lirfgjkrkc5.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-grok-color-dark.0_eskvzjfhse5.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)

Run it with

AI GatewayProviderCustom

``` prism-code
1import { generateText } from 'ai';2
3const { text } = await generateText({4  model: "spacexai/grok-4.7",5  prompt: 'Explain the concept of quantum entanglement.',6});7
8console.log(text);
```

Explain quantum entanglement in simple terms.

Entanglement is nature's way of keeping a secret between two particles. Once entangled, observing one instantly reveals information about the other — no signal needed, no matter how far apart they are.

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-grok-color-light.0_lirfgjkrkc5.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-grok-color-dark.0_eskvzjfhse5.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-open-ai-light.0rampvbx3gsfc.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-open-ai-dark.00f-3em_ivbjc.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-anthropic-light.0m3~ak04~9ano.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-anthropic-dark.0c24entp60~my.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-google-light.0pjgige7~kpjk.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-google-dark.0wgffgvi7tvcj.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-mistral-light.0122o1_0_rtaj.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-mistral-dark.0mk9~xj9vw271.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-meta-light.059o-lsd_n5jj.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-meta-dark.12y4z0db2pbhl.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-perplexity-light.18e0ri-8o9zbe.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-perplexity-dark.0zrl6fjaubel7.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-deepseek-light.14v5vcu9ivkd6.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-deepseek-dark.0g6jj3wcbd39y.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-moonshot-light.0dm_xundzyfj-.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-moonshot-dark.02jm0o5a-c4pr.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-zai-light.0wg~~cai6xyww.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-zai-dark.179wh_59daup..svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)

See all [supported LLM models](https://vercel.com/ai-gateway/models)

29.4M  
Weekly downloads

27K  
GitHub stars

718+  
Contributors

100+  
Models supported

### The Framework Agnostic AI Toolkit

The open-source AI toolkit designed to help developers build AI-powered applications and agents with React, Next.js, Vue, Svelte, Node.js, and more.

Multi-provider support. Switch providers with one line of code.

Streaming that just works. Real-time responses without custom parsing.

Built-in fallbacks.  
Reliable production behavior by default.

generate-text.ts

Run it with

AI GatewayProviderCustom

``` prism-code
1import { generateText } from 'ai';2
3const { text } = await generateText({4  model: "openai/gpt-5.5",5  prompt: 'Explain the concept of quantum entanglement.',6});7
8console.log(text);
```

Text Generation

Speech

Transcription

Image Generation

Video Generation

Tool Calling

Error Handling

DevTools

AI SDK Core

A unified API for generating text, structured objects, tool calls, and building agents with LLMs.

AI SDK UI

A set of framework-agnostic hooks for quickly building chat and generative user interface.

[Go to playground](/playground)

Supports

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-anthropic-light.0m3~ak04~9ano.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-anthropic-dark.0c24entp60~my.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-open-ai-light.0rampvbx3gsfc.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-open-ai-dark.00f-3em_ivbjc.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-google-light.0pjgige7~kpjk.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-google-dark.0wgffgvi7tvcj.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-grok-light.0_lirfgjkrkc5.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo-grok-dark.0_eskvzjfhse5.svg&w=32&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)

+ [16 providers](https://vercel.com/ai-gateway/models)

### Scale with confidence

Plug the AI SDK into an entire ecosystem designed for the way modern AI applications that scale.

[](https://vercel.com/ai-gateway)

Vercel AI Gateway

Access 100+ models with no markup or having to manage multiple API keys.

``` geist-overflow-scroll-y
npm i ai
```

[](https://vercel.com/sandbox)

Vercel Sandbox

Run agent generated code securely and at scale.

``` geist-overflow-scroll-y
npm i @vercel/sandbox
```

[](https://vercel.com/workflow)

Workflows NEW

Build long running AI agents and apps that can suspend, resume, and survive function timeouts.

``` geist-overflow-scroll-y
npm i workflow
```

[](https://elements.ai-sdk.dev/)

AI Elements

A UI component library and custom registry built to build AI-native applications faster.

``` geist-overflow-scroll-y
npx ai-elements
```

We built a full AI agent with 40+ tools, resumable streams, and multi-step reasoning on AI SDK. Every hard problem we'd solved with duct tape before, streaming, tool call repair, message management, tool based UI, they already had a clean API for. It feels like their team hit every wall we did, just before us.

Adir DuchanSenior AI Engineer

OpenCode uses AI SDK.

Dax RaadCEO & Founder

### Build with our ![AiSdk](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fai-sdk-light.0-.nn6z_67.-e.svg&w=640&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ)![AiSdk](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fai-sdk-dark.04dc-6v2tifye.svg&w=640&q=75&dpl=dpl_EsVpepSgNiXuSEaZgAqYgezMVNbJ) today

Get started with the AI SDK by using our recipes or templates.

[Visit Documentation](/docs)

``` geist-overflow-scroll-y
npm i ai
```

Chatbot Starter Template

Learn how to build a full-featured AI chatbot with persistence, multi-modal chat, and more.

``` geist-overflow-scroll-y
Copy install prompt
```

Build a Slackbot Agent

Learn how to build a Slackbot that responds to direct messages and mentions in channels.

``` geist-overflow-scroll-y
Copy install prompt
```

Build a SQL Agent

Learn how to build an app that interacts with a PostgreSQL database using natural language.

``` geist-overflow-scroll-y
Copy install prompt
```

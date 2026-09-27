---
title: How can I help you today?
description: '[](/)'
product: Amazon Bedrock AgentCore
section: References / docs.copilotkit.ai
source_url: https://docs.copilotkit.ai/crewai-flows
fetched: '2026-09-26'
tags:
- agentcore
- docs-copilotkit-ai
- reference
- related
referenced_by:
- runtime-agui.md
conversion: pandoc
---

[](/)

FrontendReact

Agent backendCrewAI Flows

[Introduction](/crewai-crews)[Quickstart](/crewai-crews/quickstart)[Intelligence](/crewai-crews/intelligence/overview)

Basics

Chat

Rich Threads

[Frontend-tools](/crewai-crews/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](/crewai-crews/webmcp)

Agent capabilities

CrewAI Flows

[Sub-agents](/crewai-crews/multi-agent/subagents)

Intelligence

[Overview](/crewai-crews/intelligence/overview)

Get started

Features

[Rich Threads](/crewai-crews/threads)

[Automatic Learning](/crewai-crews/learning)

[User Memories](/crewai-crews/intelligence/memories)[Product Analytics](/crewai-crews/intelligence/analytics)[Channels](/crewai-crews/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](/cookbook)[Reference](/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](/crewai-crews/telemetry)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

# How can I help you today?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLXBsdXMgY3BrOnNpemUtWzIwcHhdIiBhcmlhLWhpZGRlbj0idHJ1ZSI+PHBhdGggZD0iTTUgMTJoMTQiIC8+PHBhdGggZD0iTTEyIDV2MTQiIC8+PC9zdmc+)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLWFycm93LXVwIGNwazpzaXplLVsxOHB4XSIgYXJpYS1oaWRkZW49InRydWUiPjxwYXRoIGQ9Im01IDEyIDctNyA3IDciIC8+PHBhdGggZD0iTTEyIDE5VjUiIC8+PC9zdmc+)

AI can make mistakes. Please verify important information.

**Loading Chat…**

Previous slide

Chat

Rich Threads

Automatic Learning

Generative UI

Declarative UI

Human-in-the-loop

Frontend tools

Shared state

Headless UI

Sub-agents

Next slide

CrewAI and CopilotKit running together, in the React frontend. Every demo below is the same integration with one capability turned on.

## Build with CrewAI Flows

CrewAI gives you the flow: steps, state and the crew that works through them. What it does not give you is the surface. Somewhere for the conversation to happen, a way to show the flow while it runs, and a moment for a person to step in. Each capability below builds on something your flow already does.

### Generative UI

Your flow emits state and tool calls as each step completes. CopilotKit streams those to the browser and renders them as React components your users watch update while the flow runs.

[Read the docs](/crewai-crews/generative-ui)

### Human-in-the-loop

A flow can stop and wait for a person. CopilotKit renders your own UI for that decision and resumes the flow with the answer.

[Read the docs](/crewai-crews/human-in-the-loop/flow)

### Shared state

Flow state is the one object every step reads and writes. CopilotKit mirrors it into your app and back, so a user edit and a step write land in the same place.

[Read the docs](/crewai-crews/shared-state)

Chat surfaces, headless UI, frontend tools and multi-agent flows work with CrewAI too. [And more](/crewai-crews/build-with-agents)

## Start building

Connect an existing agent or build a new one. Get a tailored setup prompt.

Step 1 of 4Setup

### What are you building?

Tell us what you already have. We’ll tailor your setup.

Existing projectAdd a CrewAI Flows agent to your app

Existing agentConnect your CrewAI Flows agent to your app

New projectBuild an app and agent from scratch

Step 1 of 4Setup

## Connect your agent

Your flow keeps running as its own Python service, with the AG-UI bridge from ag_ui_crewai in front of it. CopilotKit reaches that service over HTTP, so nothing inside the flow changes.

app/api/copilotkit/route.ts

``` min-w-full
import {
  CopilotRuntime,
  createCopilotRuntimeHandler,
} from "@copilotkit/runtime/v2";
import { HttpAgent } from "@ag-ui/client";

const runtime = new CopilotRuntime({
  agents: {
    my_agent: new HttpAgent({ url: process.env.AGENT_URL! }),
  },
});

const handler = createCopilotRuntimeHandler({
  runtime,
  basePath: "/api/copilotkit",
});

export const GET = handler;
export const POST = handler;
```

[Read the setup guide](/crewai-crews/quickstart)

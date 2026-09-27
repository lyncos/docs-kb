---
title: How can I help you today?
description: '[](/)'
product: Amazon Bedrock AgentCore
section: References / docs.copilotkit.ai
source_url: https://docs.copilotkit.ai/aws-strands
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

Agent backendAWS Strands (Python)

[Introduction](/strands)[Quickstart](/strands/quickstart)[Intelligence](/strands/intelligence/overview)

Basics

Chat

Rich Threads

[Frontend-tools](/strands/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](/strands/webmcp)

Agent capabilities

AWS Strands (Python)

[Sub-agents](/strands/multi-agent/subagents)

Intelligence

[Overview](/strands/intelligence/overview)

Get started

Features

[Rich Threads](/strands/threads)

[Automatic Learning](/strands/learning)

[User Memories](/strands/intelligence/memories)[Product Analytics](/strands/intelligence/analytics)[Channels](/strands/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

[Cookbook](/cookbook)[Reference](/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](/strands/telemetry)

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

Strands and CopilotKit running together, in the React frontend. Every demo below is the same integration with one capability turned on.

## Build with AWS Strands

Strands gives you the agent: a model, a tool loop and the state it carries between turns. What it does not give you is the surface. Somewhere for the conversation to happen, a way to show the run while it is running, and a moment for a person to step in. Each capability below builds on something your agent already does.

### Generative UI

Your agent calls tools and reports progress as it works. CopilotKit streams that to the browser and renders each step as a React component, instead of leaving the user with a spinner.

[Read the docs](/strands/generative-ui)

### Human-in-the-loop

A frontend tool registered with useHumanInTheLoop renders your own UI, waits for the user's answer, and hands it back to the agent as the tool result.

[Read the docs](/strands/human-in-the-loop)

### Shared state

Your agent keeps state on the server between turns. CopilotKit mirrors it into your app and back, so a user edit and an agent write land in the same place.

[Read the docs](/strands/shared-state)

Chat surfaces, headless UI, frontend tools and multi-agent flows work with Strands too. [And more](/strands/build-with-agents)

## Start building

Connect an existing agent or build a new one. Get a tailored setup prompt.

Step 1 of 4Setup

### What are you building?

Tell us what you already have. We’ll tailor your setup.

Existing projectAdd a AWS Strands (Python) agent to your app

Existing agentConnect your AWS Strands (Python) agent to your app

New projectBuild an app and agent from scratch

Step 1 of 4Setup

## Connect your agent

Your agent keeps running as its own Python service, with the AG-UI bridge from ag_ui_strands in front of it. CopilotKit reaches that service over HTTP, so nothing inside the agent changes.

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

[Read the setup guide](/strands/quickstart)

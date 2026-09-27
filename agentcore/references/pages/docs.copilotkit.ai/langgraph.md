---
title: How can I help you today?
description: '[](/)'
product: Amazon Bedrock AgentCore
section: References / docs.copilotkit.ai
source_url: https://docs.copilotkit.ai/langgraph
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

Agent backendLangGraph (Python)

[Introduction](/langgraph-python)[Quickstart](/langgraph-python/quickstart)[Intelligence](/langgraph-python/intelligence/overview)

Basics

Chat

Rich Threads

[Frontend-tools](/langgraph-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](/langgraph-python/webmcp)

Agent capabilities

LangGraph (Python)

[Sub-agents](/langgraph-python/multi-agent/subagents)

Intelligence

[Overview](/langgraph-python/intelligence/overview)

Get started

Features

[Rich Threads](/langgraph-python/threads)

[Automatic Learning](/langgraph-python/learning)

[User Memories](/langgraph-python/intelligence/memories)[Product Analytics](/langgraph-python/intelligence/analytics)[Channels](/langgraph-python/intelligence/channels)

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

[Open-source telemetry](/langgraph-python/telemetry)

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

LangGraph and CopilotKit running together, in the React frontend. Every demo below is the same integration with one capability turned on.

## Build with LangGraph

LangGraph gives you the graph: nodes, edges, one state object, and interrupts that stop a run mid-node. What it does not give you is the surface. Somewhere for the conversation to happen, a way to show the run while it is running, and a moment for a person to step in. Each capability below builds on something your graph already does.

### Generative UI

Your nodes return state updates and tool calls as they run. CopilotKit streams both to the browser by default and renders them as React components your users watch update while the graph works.

[Read the docs](/langgraph-python/generative-ui)

### Human-in-the-loop

A node calls interrupt() and stops mid-execution. CopilotKit catches that event, renders your own UI for the decision, and resumes the graph with the answer.

[Read the docs](/langgraph-python/human-in-the-loop/interrupt-flow)

### Shared state

Your graph carries one state object from node to node. CopilotKit mirrors it into your app and back, so a user edit and a node write land in the same place.

[Read the docs](/langgraph-python/shared-state)

Chat surfaces, headless UI, frontend tools and subagent flows work with LangGraph too. [And more](/langgraph-python/build-with-agents)

## Start building

Connect an existing agent or build a new one. Get a tailored setup prompt.

Step 1 of 4Setup

### What are you building?

Tell us what you already have. We’ll tailor your setup.

Existing projectAdd a LangGraph (Python) agent to your app

Existing agentConnect your LangGraph (Python) agent to your app

New projectBuild an app and agent from scratch

Step 1 of 4Setup

## Connect your agent

Your graph stays where it runs today: LangGraph Platform, LangSmith, or your own FastAPI service. CopilotKit reaches it over AG-UI, so nothing inside the graph changes.

    import { CopilotRuntime, createCopilotRuntimeHandler } from "@copilotkit/runtime/v2";
    import { LangGraphAgent } from "@copilotkit/runtime/langgraph";

    const runtime = new CopilotRuntime({
      agents: {
        sample_agent: new LangGraphAgent({
          deploymentUrl: process.env.LANGGRAPH_DEPLOYMENT_URL!,
          graphId: "sample_agent",
          langsmithApiKey: process.env.LANGSMITH_API_KEY!,
        }),
      },
    });

    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
    });

    export const GET = handler;
    export const POST = handler;
    export const PATCH = handler;
    export const DELETE = handler;

[Read the setup guide](/langgraph-python/quickstart)

## Already have LangGraph conversations?

When you add a user-facing app to an existing LangGraph agent, your users may need to open and continue conversations they already started. [CopilotKit Intelligence](/intelligence/overview) can import supported LangGraph history as Rich Threads so your app does not start with an empty thread list.

The importer reads LangGraph Server, LangGraph Platform, or LangSmith Deployment thread and run APIs. It does not import standalone LangChain message stores, LangSmith traces, or embedded checkpointers that are not exposed through those APIs.

Import history once; future CopilotKit-mediated runs synchronize with Intelligence and continue through LangGraph's native persistence path when your durable checkpointer or Platform deployment remains configured. This is not a continuous mirror of runs made outside CopilotKit.

[Import and synchronize LangGraph threads](/langgraph-python/threads-import) for source setup, agent mapping, and thread continuity.

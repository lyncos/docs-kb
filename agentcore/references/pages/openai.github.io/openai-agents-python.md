---
title: OpenAI Agents SDK
description: ' Quickstart '
product: Amazon Bedrock AgentCore
section: References / openai.github.io
source_url: https://openai.github.io/openai-agents-python
fetched: '2026-09-26'
tags:
- agentcore
- openai-github-io
- reference
- related
referenced_by:
- supported-frameworks-openai-agents.md
conversion: pandoc
---

[ Quickstart ](quickstart/)

[ Configuration ](config/)

Documentation

Realtime agents

Voice agents

[ Models ](models/)

[ Tools ](tools/)

[ Guardrails ](guardrails/)

[ Running agents ](running_agents/)

[ Streaming ](streaming/)

[ Agent orchestration ](multi_agent/)

[ Handoffs ](handoffs/)

[ Results ](results/)

[ Human-in-the-loop ](human_in_the_loop/)

Sessions

[ Context management ](context/)

[ Usage ](usage/)

[ Model context protocol (MCP) ](mcp/)

[ Tracing ](tracing/)

[ Testing ](testing/)

[ Agent visualization ](visualization/)

[ REPL utility ](repl/)

[ Release process/changelog ](release/)

API Reference

[ Sandbox clients ](ref/sandbox/session/sandbox_client/)

[ SandboxSession ](ref/sandbox/session/sandbox_session/)

[ SandboxSessionState ](ref/sandbox/session/sandbox_session_state/)

[ Unix local sandbox ](ref/sandbox/sandboxes/unix_local/)

[ Docker sandbox ](ref/sandbox/sandboxes/docker/)

[ Responses WebSocket session ](ref/responses_websocket_session/)

[ Run error handlers ](ref/run_error_handlers/)

[ Memory ](ref/memory/)

[ REPL ](ref/repl/)

[ Tools ](ref/tool/)

[ Decorators ](ref/decorators/)

[ Tool context ](ref/tool_context/)

[ Results ](ref/result/)

[ Streaming events ](ref/stream_events/)

[ Handoffs ](ref/handoffs/)

[ Lifecycle ](ref/lifecycle/)

[ Items ](ref/items/)

[ Run context ](ref/run_context/)

[ Usage ](ref/usage/)

[ Exceptions ](ref/exceptions/)

[ Guardrails ](ref/guardrail/)

[ Prompts ](ref/prompts/)

[ Model settings ](ref/model_settings/)

[ Strict schema ](ref/strict_schema/)

[ Tool guardrails ](ref/tool_guardrails/)

[ Computer ](ref/computer/)

[ Agent output ](ref/agent_output/)

[ Function schema ](ref/function_schema/)

[ Model interface ](ref/models/interface/)

[ OpenAI Chat Completions model ](ref/models/openai_chatcompletions/)

[ OpenAI Responses model ](ref/models/openai_responses/)

[ OpenAI provider ](ref/models/openai_provider/)

[ Multi provider ](ref/models/multi_provider/)

[ MCP servers ](ref/mcp/server/)

[ MCP util ](ref/mcp/util/)

[ MCP manager ](ref/mcp/manager/)

Tracing

Realtime

Voice

Extensions

[ Tool output trimmer ](ref/extensions/tool_output_trimmer/)

[ SQLAlchemySession ](ref/extensions/memory/sqlalchemy_session/)

[ Async SQLite session ](ref/extensions/memory/async_sqlite_session/)

[ RedisSession ](ref/extensions/memory/redis_session/)

[ MongoDBSession ](ref/extensions/memory/mongodb_session/)

[ DaprSession ](ref/extensions/memory/dapr_session/)

[ EncryptedSession ](ref/extensions/memory/encrypt_session/)

[ AdvancedSQLiteSession ](ref/extensions/memory/advanced_sqlite_session/)

# OpenAI Agents SDK

The [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) enables you to build agentic AI apps in a lightweight, easy-to-use package with very few abstractions. It's a production-ready upgrade of our previous experimentation for agents, [Swarm](https://github.com/openai/swarm/tree/main). The Agents SDK has a very small set of primitives:

- **Agents**, which are LLMs equipped with instructions and tools
- **Agents as tools / Handoffs**, which allow agents to delegate to other agents for specific tasks
- **Guardrails**, which enable validation of agent inputs and outputs

In combination with Python, these primitives are powerful enough to express complex relationships between tools and agents, and allow you to build real-world applications without a steep learning curve. In addition, the SDK comes with built-in **tracing** that lets you visualize and debug your agentic flows, as well as evaluate them and even fine-tune models for your application.

## Why use the Agents SDK

The SDK has two driving design principles:

1.  Enough features to be worth using, but few enough primitives to make it quick to learn.
2.  Works great out of the box, but you can customize exactly what happens.

Here are the main features of the SDK:

- **Agents**: Build agents with instructions, tools, guardrails, handoffs, and a built-in loop that continues until the task is complete.
- **Sandbox agents**: Run specialists inside real isolated workspaces. Sandbox agents support manifest-defined files, sandbox client selection, and resumable sandbox sessions.
- **Realtime agents**: Build powerful voice agents with `gpt-realtime-2.1`, automatic interruption detection, context management, guardrails, and more.
- **Voice agents**: Build voice pipelines that combine speech-to-text, an agent workflow, and text-to-speech.
- **Python-first**: Use built-in language features to orchestrate and chain agents, rather than needing to learn new abstractions.
- **Agents as tools / Handoffs**: A powerful mechanism for coordinating and delegating work across multiple agents.
- **Guardrails**: Run input validation and safety checks in parallel with agent execution, and fail fast when checks do not pass.
- **Function tools**: Turn any Python function into a tool with automatic schema generation and Pydantic-powered validation.
- **MCP server tool calling**: Built-in integration that exposes remote MCP tools to agents alongside function tools.
- **Sessions**: A persistent memory layer for maintaining working context within an agent loop.
- **Human in the loop**: Built-in mechanisms for involving humans during agent runs.
- **Tracing**: Built-in tracing for visualizing, debugging, and monitoring workflows, with support for the OpenAI suite of evaluation, fine-tuning, and distillation tools.

## Agents SDK or Responses API?

The SDK uses the Responses API by default for OpenAI models, but it wraps model calls in a higher-level runtime.

Use the Responses API directly when:

- you want to own the loop, tool dispatch, and state handling yourself
- your workflow is short-lived and mainly about returning the model's response

Use the Agents SDK when:

- you want the runtime to manage turns, tool execution, guardrails, handoffs, or sessions
- your agent should produce artifacts or operate across multiple coordinated steps
- you need a real workspace or resumable execution through [Sandbox agents](sandbox_agents/)

You do not need to choose one globally. Many applications use the SDK for managed workflows and call the Responses API directly for lower-level paths.

## Installation

    pip install openai-agents

## Hello world example

    from agents import Agent, Runner

    agent = Agent(name="Assistant", instructions="You are a helpful assistant")

    result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
    print(result.final_output)

    # Code within the code,
    # Functions calling themselves,
    # Infinite loop's dance.

(*If running this, ensure you set the `OPENAI_API_KEY` environment variable*)

    export OPENAI_API_KEY=sk-...

## Start here

- Build your first text-based agent with the [Quickstart](quickstart/).
- Then decide how you want to carry state across turns in [Running agents](running_agents/#choose-a-memory-strategy).
- If the task depends on real files, repos, or isolated per-agent workspace state, read the [Sandbox agents quickstart](sandbox_agents/).
- If you are deciding between handoffs and manager-style orchestration, read [Agent orchestration](multi_agent/).

## Choose your path

Use this table when you know the job you want to do, but not which page explains it.

| Goal | Start here |
|----|----|
| Build the first text agent and see one complete run | [Quickstart](quickstart/) |
| Add function tools, hosted tools, or agents as tools | [Tools](tools/) |
| Run a coding, review, or document agent inside a real isolated workspace | [Sandbox agents quickstart](sandbox_agents/) and [Sandbox clients](sandbox/clients/) |
| Decide between handoffs and manager-style orchestration | [Agent orchestration](multi_agent/) |
| Keep memory across turns | [Running agents](running_agents/#choose-a-memory-strategy) and [Sessions](sessions/) |
| Use OpenAI models, websocket transport, or non-OpenAI providers | [Models](models/) |
| Review outputs, run items, interruptions, and resume state | [Results](results/) |
| Build a low-latency voice agent with `gpt-realtime-2.1` | [Realtime agents quickstart](realtime/quickstart/) and [Realtime transport](realtime/transport/) |
| Build a speech-to-text / agent / text-to-speech pipeline | [Voice pipeline quickstart](voice/quickstart/) |

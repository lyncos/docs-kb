---
title: 🦜️🔗 LangChain 🤝 Amazon Web Services (AWS)
description: langchain-ai / **langchain-aws** Public
product: Amazon Bedrock AgentCore
section: References / github.com
source_url: https://github.com/langchain-ai/langchain-aws
fetched: '2026-09-26'
tags:
- agentcore
- github-com
- reference
- related
referenced_by:
- memory-integrate-lang.md
conversion: pandoc
---

[langchain-ai](/langchain-ai) / **[langchain-aws](/langchain-ai/langchain-aws)** Public

- [Notifications](/login?return_to=%2Flangchain-ai%2Flangchain-aws) You must be signed in to change notification settings

- [Fork 310](/login?return_to=%2Flangchain-ai%2Flangchain-aws)

- [ Star 350](/login?return_to=%2Flangchain-ai%2Flangchain-aws)

[](/langchain-ai/langchain-aws)

main

[Branches](/langchain-ai/langchain-aws/branches)[Tags](/langchain-ai/langchain-aws/tags)

[](/langchain-ai/langchain-aws/branches)[](/langchain-ai/langchain-aws/tags)

Go to file

Code

Open more actions menu

## Latest commit

 

## History

[877 Commits](/langchain-ai/langchain-aws/commits/main/)

[](/langchain-ai/langchain-aws/commits/main/)877 Commits

## Folders and files

[TABLE]

## Repository files navigation

# 🦜️🔗 LangChain 🤝 Amazon Web Services (AWS)

[](#️-langchain--amazon-web-services-aws)

This monorepo provides LangChain and LangGraph components for various AWS services. It aims to replace and expand upon the existing LangChain AWS components found in the `langchain-community` package in the LangChain repository.

The following packages are hosted in this repository:

- `langchain-aws` ([PyPI](https://pypi.org/project/langchain-aws/))
- `langgraph-checkpoint-aws` ([PyPI](https://pypi.org/project/langgraph-checkpoint-aws/))
- `langchain-agentcore-codeinterpreter` ([PyPI](https://pypi.org/project/langchain-agentcore-codeinterpreter/))

## Features

[](#features)

### LangChain

[](#langchain)

- **LLMs**: Includes LLM classes for AWS services like [Bedrock](https://aws.amazon.com/bedrock) and [SageMaker Endpoints](https://aws.amazon.com/sagemaker/deploy/), allowing you to leverage their language models within LangChain.
- **VectorStores**: Supports vectorstores for services like [Amazon MemoryDB](https://aws.amazon.com/memorydb/), [Amazon S3 Vectors](https://aws.amazon.com/s3/features/vectors/), and [AWS ElastiCache for Valkey](https://aws.amazon.com/elasticache/), providing efficient and scalable vector database for your applications.
- **Retrievers**: Supports retrievers for services like [Amazon Kendra](https://aws.amazon.com/kendra/) and [KnowledgeBases for Amazon Bedrock](https://aws.amazon.com/bedrock/knowledge-bases/), enabling efficient retrieval of relevant information in your RAG applications.
- **Graphs**: Provides components for working with [AWS Neptune](https://aws.amazon.com/neptune/) graphs within LangChain.
- **Agents**: Includes Runnables to support [Amazon Bedrock Agents](https://aws.amazon.com/bedrock/agents/), allowing you to leverage Bedrock Agents within LangChain and LangGraph.
- **Tools**: Includes tools and toolkits to enable use of [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)'s built-in tools with LangChain and LangGraph agents.

### LangGraph

[](#langgraph)

- **Checkpointers**: Provides custom checkpointing solutions for LangGraph agents using several AWS services, including [Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html), [Bedrock Session Management](https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html), [DynamoDB](https://aws.amazon.com/dynamodb/), and [ElastiCache Valkey](https://aws.amazon.com/elasticache/).
- **Memory Stores** - Provides memory store solutions for saving, processing, and retrieving intelligent long term memories using services like [Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) and [ElastiCache Valkey](https://aws.amazon.com/elasticache/).

### Deep Agents

[](#deep-agents)

- **Sandboxes**: Provides an [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) Code Interpreter sandbox backend for [Deep Agents](https://github.com/langchain-ai/deepagents), enabling secure code execution in isolated MicroVM environments.

...and more to come. This repository will continue to expand and offer additional components for various AWS services as development progresses.

**Note**: This repository will replace all AWS integrations currently present in the `langchain-community` package. Users are encouraged to migrate to this repository as soon as possible.

## Installation

[](#installation)

You can install the `langchain-aws` package from PyPI.

    pip install langchain-aws

The `langgraph-checkpoint-aws` package can also be installed from PyPI.

    pip install langgraph-checkpoint-aws

The `langchain-agentcore-codeinterpreter` package can also be installed from PyPI.

    pip install langchain-agentcore-codeinterpreter

## Usage

[](#usage)

### `langchain-aws`

[](#langchain-aws)

Here's a simple example of how to use the `langchain-aws` package.

    from langchain_aws import ChatBedrockConverse

    # Initialize the Bedrock chat model
    model = ChatBedrockConverse(
        model="us.anthropic.claude-sonnet-4-5-20250929-v1:0"
    )

    # Invoke the model
    response = model.invoke("Hello! How are you today?")
    print(response)

### AgentCore Tools

[](#agentcore-tools)

    from langchain_aws.tools import create_browser_toolkit, create_code_interpreter_toolkit

    # Browser automation
    browser_toolkit, browser_tools = create_browser_toolkit(region="us-west-2")

    # Code execution (async)
    code_toolkit, code_tools = await create_code_interpreter_toolkit(region="us-west-2")

    # Use with LangGraph agent
    agent = create_react_agent(model, tools=browser_tools + code_tools)
    result = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "Navigate to example.com"}]},
        config={"configurable": {"thread_id": "session-1"}}
    )

    # Cleanup
    await browser_toolkit.cleanup()
    await code_toolkit.cleanup()

For more detailed usage examples and documentation, please refer to the [LangChain docs](https://python.langchain.com/docs/integrations/platforms/aws/).

Tip

For developing, debugging, and deploying AI agents and LLM applications, see [LangSmith](https://docs.langchain.com/langsmith/home).

### `langgraph-checkpoint-aws`

[](#langgraph-checkpoint-aws)

You can find usage examples for `langgraph-checkpoint-aws` [in the README](https://github.com/langchain-ai/langchain-aws/blob/main/libs/langgraph-checkpoint-aws/README.md).

### `langchain-agentcore-codeinterpreter`

[](#langchain-agentcore-codeinterpreter)

    from bedrock_agentcore.tools.code_interpreter_client import CodeInterpreter
    from langchain_agentcore_codeinterpreter import AgentCoreSandbox

    interpreter = CodeInterpreter(region="us-west-2")
    interpreter.start()

    backend = AgentCoreSandbox(interpreter=interpreter)
    result = backend.execute("echo hello")
    print(result.output)  # hello

    interpreter.stop()

## Contributing

[](#contributing)

We welcome contributions to this repository! To get started, please follow the [Contributing Guide](https://github.com/langchain-ai/langchain-aws/blob/main/.github/CONTRIBUTING.md).

This guide provides detailed instructions on how to set up each project for development and guidance on how to contribute effectively.

## License

[](#license)

This project is licensed under the [MIT License](/langchain-ai/langchain-aws/blob/main/LICENSE).

## About

Build LangChain Applications on AWS

### Topics

[aws](/topics/aws)[generative-ai](/topics/generative-ai)[langchain](/topics/langchain)[langchain-python](/topics/langchain-python)

### Resources

[Readme](#readme-ov-file)

[MIT license](#MIT-1-ov-file)

### Code of conduct

[Code of conduct](/langchain-ai/langchain-aws#coc-ov-file)

### Contributing

[Contributing](#contributing-ov-file)

### Security policy

[Security policy](#security-ov-file)

[Activity](/langchain-ai/langchain-aws/activity)

[Custom properties](/langchain-ai/langchain-aws/custom-properties)

### Stars

**350** stars

### Watchers

**7** watching

### Forks

[**310** forks](/langchain-ai/langchain-aws/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Flangchain-ai%2Flangchain-aws&report=langchain-ai+%28user%29)

## Releases

## Packages

## Used by

## Contributors

## Languages

Generated from [langchain-ai/integration-repo-template](/langchain-ai/integration-repo-template)

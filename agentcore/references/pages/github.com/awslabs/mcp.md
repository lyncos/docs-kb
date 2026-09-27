---
title: Open source MCP servers for AWS
description: awslabs / **mcp** Public
product: Amazon Bedrock AgentCore
section: References / github.com
source_url: https://github.com/awslabs/mcp
fetched: '2026-09-26'
tags:
- agentcore
- core
- github-com
- reference
referenced_by:
- release-notes.md
conversion: pandoc
---

[awslabs](/awslabs) / **[mcp](/awslabs/mcp)** Public

- [Notifications](/login?return_to=%2Fawslabs%2Fmcp) You must be signed in to change notification settings

- [Fork 1.8k](/login?return_to=%2Fawslabs%2Fmcp)

- [ Star 9.7k](/login?return_to=%2Fawslabs%2Fmcp)

[](/awslabs/mcp)

main

[Branches](/awslabs/mcp/branches)[Tags](/awslabs/mcp/tags)

[](/awslabs/mcp/branches)[](/awslabs/mcp/tags)

Go to file

Code

Open more actions menu

## Latest commit

 

## History

[1,861 Commits](/awslabs/mcp/commits/main/)

[](/awslabs/mcp/commits/main/)1,861 Commits

## Folders and files

[TABLE]

## Repository files navigation

# Open source MCP servers for AWS

[](#open-source-mcp-servers-for-aws)

A suite of specialized MCP servers that help you get the most out of AWS, wherever you use MCP.

[![GitHub](https://camo.githubusercontent.com/7bef95b38a27f6f93d54756cbcc6c0836290979aac3dc4073c363d8415d4895a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6769746875622d6177736c6162732f6d63702d626c75652e7376673f7374796c653d666c6174266c6f676f3d676974687562)](https://github.com/awslabs/mcp) [![License](https://camo.githubusercontent.com/1ab15760a37e02017d01e83deb523ea4fcd0c2c1ff40582248e5993d4b4bdf8b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4170616368652d2d322e302d627269676874677265656e)](/awslabs/mcp/blob/main/LICENSE) [![Codecov](https://camo.githubusercontent.com/a9f1209a67280570750b6567cf1a9f0bfe6b8608b366071a90f9ccce6c45f33e/68747470733a2f2f696d672e736869656c64732e696f2f636f6465636f762f632f6769746875622f6177736c6162732f6d6370)](https://app.codecov.io/gh/awslabs/mcp) [![OSSF-Scorecard Score](https://camo.githubusercontent.com/0ad45245621b0ec67a2ce434e53827983a300dab2b2175a11f8071e602526a6f/68747470733a2f2f696d672e736869656c64732e696f2f6f7373662d73636f7265636172642f6769746875622e636f6d2f6177736c6162732f6d6370)](https://scorecard.dev/viewer/?uri=github.com/awslabs/mcp)

Tip

The [Agent Toolkit for AWS](https://aws.amazon.com/about-aws/whats-new/2026/05/agent-toolkit/) is now live! The Agent Toolkit for AWS is the successor to the MCP servers, plugins, and skills available on AWS Labs, and was informed by feedback from customers like you. If you're building production software using coding agents or building agents for your own customers, we recommend Agent Toolkit for AWS. It includes IAM condition keys to distinguish agent actions from human ones, CloudWatch and CloudTrail visibility, and skills that have been evaluated for accuracy and effectiveness. This repo continues to work and accept contributions. Over time, the most useful projects here will move into Agent Toolkit for AWS.

## Table of Contents

[](#table-of-contents)

- [Open source MCP servers for AWS](#open-source-mcp-servers-for-aws)
  - [Table of Contents](#table-of-contents)
  - [What is the Model Context Protocol (MCP) and how does it work with MCP Servers for AWS?](#what-is-the-model-context-protocol-mcp-and-how-does-it-work-with-mcp-servers-for-aws)
  - [Open source MCP servers for AWS Transport Mechanisms](#open-source-mcp-servers-for-aws-transport-mechanisms)
    - [Supported transport mechanisms](#supported-transport-mechanisms)
    - [Server Sent Events Support Removal](#server-sent-events-support-removal)
    - [Why MCP Servers for AWS?](#why-mcp-servers-for-aws)
  - [Available MCP Servers: Quick Installation](#available-mcp-servers-quick-installation)
    - [🚀 Getting Started with AWS](#-getting-started-with-aws)
    - [Browse by What You're Building](#browse-by-what-youre-building)
      - [📚 Real-time access to official AWS documentation](#-real-time-access-to-official-aws-documentation)
    - [🏗️ Infrastructure & Deployment](#%EF%B8%8F-infrastructure--deployment)
      - [Container Platforms](#container-platforms)
      - [Serverless & Functions](#serverless--functions)
      - [Support](#support)
    - [🤖 AI & Machine Learning](#-ai--machine-learning)
    - [📊 Data & Analytics](#-data--analytics)
      - [SQL & NoSQL Databases](#sql--nosql-databases)
        - [Search & Analytics](#search--analytics)
      - [Backend API Providers](#backend-api-providers)
      - [Caching & Performance](#caching--performance)
    - [🛠️ Developer Tools & Support](#%EF%B8%8F-developer-tools--support)
    - [📡 Integration & Messaging](#-integration--messaging)
    - [💰 Cost & Operations](#-cost--operations)
    - [🧬 Healthcare & Lifesciences](#-healthcare--lifesciences)
    - [Browse by How You're Working](#browse-by-how-youre-working)
      - [👨‍💻 Vibe Coding & Development](#-vibe-coding--development)
        - [Core Development Workflow](#core-development-workflow)
        - [Infrastructure as Code](#infrastructure-as-code)
        - [Application Development](#application-development)
        - [Container & Serverless Development](#container--serverless-development)
        - [Testing & Data](#testing--data)
        - [Lifesciences Workflow Development](#lifesciences-workflow-development)
        - [Healthcare Data Management](#healthcare-data-management)
      - [💬 Conversational Assistants](#-conversational-assistants)
        - [Knowledge & Search](#knowledge--search)
        - [Content Processing & Generation](#content-processing--generation)
        - [Business Services](#business-services)
      - [🤖 Autonomous Background Agents](#-autonomous-background-agents)
        - [Data Operations & ETL](#data-operations--etl)
        - [Caching & Performance](#caching--performance-1)
        - [Workflow & Integration](#workflow--integration)
        - [Operations & Monitoring](#operations--monitoring)
  - [MCP AWS Lambda Handler Module](#mcp-aws-lambda-handler-module)
  - [When to use Local vs Remote MCP Servers?](#when-to-use-local-vs-remote-mcp-servers)
    - [Local MCP Servers](#local-mcp-servers)
    - [Remote MCP Servers](#remote-mcp-servers)
  - [Use Cases for the Servers](#use-cases-for-the-servers)
  - [Installation and Setup](#installation-and-setup)
    - [For macOS/Linux](#for-macoslinux)
    - [For Windows](#for-windows)
    - [Running MCP servers in containers](#running-mcp-servers-in-containers)
    - [Getting Started with Kiro](#getting-started-with-kiro)
      - [`~/.kiro/settings/mcp.json`](#kirosettingsmcpjson)
    - [Getting Started with Cline and Amazon Bedrock](#getting-started-with-cline-and-amazon-bedrock)
      - [`cline_mcp_settings.json`](#cline_mcp_settingsjson)
    - [Getting Started with Cursor](#getting-started-with-cursor)
      - [`.cursor/mcp.json`](#cursormcpjson)
    - [Getting Started with Windsurf](#getting-started-with-windsurf)
      - [`~/.codeium/windsurf/mcp_config.json`](#codeiumwindsurfmcp_configjson)
    - [Getting Started with VS Code](#getting-started-with-vs-code)
      - [`.vscode/mcp.json`](#vscodemcpjson)
    - [Getting Started with Claude Code](#getting-started-with-claude-code)
      - [`.mcp.json`](#mcpjson)
    - [Getting Started with fx](#getting-started-with-fx)
      - [`~/.fx/mcp.json`](#fxmcpjson)
  - [Samples](#samples)
  - [Vibe coding](#vibe-coding)
  - [Additional Resources](#additional-resources)
  - [Security](#security)
  - [Contributing](#contributing)
  - [Developer guide](#developer-guide)
  - [License](#license)
  - [Disclaimer](#disclaimer)

## What is the Model Context Protocol (MCP) and how does it work with MCP Servers for AWS?

[](#what-is-the-model-context-protocol-mcp-and-how-does-it-work-with-mcp-servers-for-aws)

> The Model Context Protocol (MCP) is an open protocol that enables seamless integration between LLM applications and external data sources and tools. Whether you're building an AI-powered IDE, enhancing a chat interface, or creating custom AI workflows, MCP provides a standardized way to connect LLMs with the context they need.
>
> — [Model Context Protocol README](https://github.com/modelcontextprotocol#:~:text=The%20Model%20Context,context%20they%20need.)

An MCP Server is a lightweight program that exposes specific capabilities through the standardized Model Context Protocol. Host applications (such as chatbots, IDEs, and other AI tools) have MCP clients that maintain 1:1 connections with MCP servers. Common MCP clients include agentic AI coding assistants (like Kiro, Cline, Cursor, Windsurf) as well as chatbot applications like Claude Desktop, with more clients coming soon. MCP servers can access local data sources and remote services to provide additional context that improves the generated outputs from the models.

MCP Servers for AWS use this protocol to provide AI applications access to AWS documentation, contextual guidance, and best practices. Through the standardized MCP client-server architecture, AWS capabilities become an intelligent extension of your development environment or AI application.

MCP Servers for AWS enable enhanced cloud-native development, infrastructure management, and development workflows—making AI-assisted cloud computing more accessible and efficient.

The Model Context Protocol is an open source project run by Anthropic, PBC. and open to contributions from the entire community. For more information on MCP, you can find further documentation [here](https://modelcontextprotocol.io/introduction)

## Open source MCP servers for AWS Transport Mechanisms

[](#open-source-mcp-servers-for-aws-transport-mechanisms)

### Supported transport mechanisms

[](#supported-transport-mechanisms)

The MCP protocol currently defines two standard transport mechanisms for client-server communication:

- stdio, communication over standard in and standard out
- streamable HTTP

The MCP servers in this repository are designed to support stdio only.

You are responsible for ensuring that your use of these servers comply with the terms governing them, and any laws, rules, regulations, policies, or standards that apply to you.

### Server Sent Events Support Removal

[](#server-sent-events-support-removal)

**Important Notice:** On May 26th, 2025, Server Sent Events (SSE) support was removed from all MCP servers in their latest major versions. This change aligns with the Model Context Protocol specification's [backwards compatibility guidelines](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#backwards-compatibility).

We are actively working towards supporting [Streamable HTTP](https://modelcontextprotocol.io/specification/draft/basic/transports#streamable-http), which will provide improved transport capabilities for future versions.

For applications still requiring SSE support, please use the previous major version of the respective MCP server until you can migrate to alternative transport methods.

### Why MCP Servers for AWS?

[](#why-mcp-servers-for-aws)

MCP servers enhance the capabilities of foundation models (FMs) in several key ways:

- **Improved Output Quality**: By providing relevant information directly in the model's context, MCP servers significantly improve model responses for specialized domains like AWS services. This approach reduces hallucinations, provides more accurate technical details, enables more precise code generation, and ensures recommendations align with current AWS best practices and service capabilities.

- **Access to Latest Documentation**: FMs may not have knowledge of recent releases, APIs, or SDKs. MCP servers bridge this gap by pulling in up-to-date documentation, ensuring your AI assistant always works with the latest AWS capabilities.

- **Workflow Automation**: MCP servers convert common workflows into tools that foundation models can use directly. Whether it's CDK, Terraform, or other AWS-specific workflows, these tools enable AI assistants to perform complex tasks with greater accuracy and efficiency.

- **Specialized Domain Knowledge**: MCP servers provide deep, contextual knowledge about AWS services that might not be fully represented in foundation models' training data, enabling more accurate and helpful responses for cloud development tasks.

## Available MCP Servers: Quick Installation

[](#available-mcp-servers-quick-installation)

Get started quickly with one-click installation buttons for popular MCP clients. Click the buttons below to install servers directly in Cursor or VS Code:

### 🚀 Getting Started with AWS

[](#-getting-started-with-aws)

For AWS interactions, we recommend starting with:

[TABLE]

### Browse by What You're Building

[](#browse-by-what-youre-building)

#### 📚 Real-time access to official AWS documentation

[](#-real-time-access-to-official-aws-documentation)

[TABLE]

### 🏗️ Infrastructure & Deployment

[](#️-infrastructure--deployment)

Build, deploy, and manage cloud infrastructure with Infrastructure as Code best practices.

[TABLE]

#### Container Platforms

[](#container-platforms)

[TABLE]

#### Serverless & Functions

[](#serverless--functions)

[TABLE]

#### Migration & Modernization

[](#migration--modernization)

[TABLE]

#### Support

[](#support)

[TABLE]

### 🤖 AI & Machine Learning

[](#-ai--machine-learning)

Enhance AI applications with knowledge retrieval, content generation, and ML capabilities

[TABLE]

### 📊 Data & Analytics

[](#-data--analytics)

Work with databases, caching systems, and data processing workflows.

#### SQL & NoSQL Databases

[](#sql--nosql-databases)

[TABLE]

##### Search & Analytics

[](#search--analytics)

- **[Amazon OpenSearch MCP Server](https://github.com/opensearch-project/opensearch-mcp-server-py)** - OpenSearch powered search, Analytics, and Observability

#### Backend API Providers

[](#backend-api-providers)

[TABLE]

#### Caching & Performance

[](#caching--performance)

[TABLE]

#### Open Data

[](#open-data)

[TABLE]

### 🛠️ Developer Tools & Support

[](#️-developer-tools--support)

Accelerate development with code analysis, documentation, and testing utilities.

[TABLE]

### 📡 Integration & Messaging

[](#-integration--messaging)

Connect systems with messaging, workflows, and location services.

[TABLE]

### 💰 Cost & Operations

[](#-cost--operations)

Monitor, optimize, and manage your AWS infrastructure and costs.

[TABLE]

### 🧬 Healthcare & Lifesciences

[](#-healthcare--lifesciences)

Interact with AWS HealthAI services.

[TABLE]

------------------------------------------------------------------------

### Browse by How You're Working

[](#browse-by-how-youre-working)

#### 👨‍💻 Vibe Coding & Development

[](#‍-vibe-coding--development)

*AI coding assistants like Kiro, Cline, Cursor, and Claude Code helping you build faster*

**Workshop**: Check out the [Vibe Coding with AWS MCP Servers](https://github.com/aws-solutions-library-samples/guidance-for-vibe-coding-with-aws-mcp-servers) workshop for hands-on guidance and examples.

##### Core Development Workflow

[](#core-development-workflow)

[TABLE]

##### Infrastructure as Code

[](#infrastructure-as-code)

[TABLE]

##### Application Development

[](#application-development)

[TABLE]

##### Container & Serverless Development

[](#container--serverless-development)

[TABLE]

##### Testing & Data

[](#testing--data)

| Server Name | Description | Install |
|-------------|-------------|---------|

##### Lifesciences Workflow Development

[](#lifesciences-workflow-development)

[TABLE]

##### Healthcare Data Management

[](#healthcare-data-management)

[TABLE]

#### 💬 Conversational Assistants

[](#-conversational-assistants)

*Customer-facing chatbots, business agents, and interactive Q&A systems*

##### Knowledge & Search

[](#knowledge--search)

[TABLE]

##### Content Processing & Generation

[](#content-processing--generation)

[TABLE]

##### Business Services

[](#business-services)

[TABLE]

#### 🤖 Autonomous Background Agents

[](#-autonomous-background-agents)

*Headless automation, ETL pipelines, and operational systems*

##### Data Operations & ETL

[](#data-operations--etl)

[TABLE]

\| [Amazon RDS Oracle MCP Server](/awslabs/mcp/blob/main/src/oracle-mcp-server) \| Oracle Database operations via Secrets Manager authentication \| [![Install](https://camo.githubusercontent.com/bce0080ea9cb732c2d6f497e4ad2f8c724a148ecfc57e602665ce0109944476a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f496e7374616c6c2d4b69726f2d3930343646463f7374796c653d666c61742d737175617265266c6f676f3d6b69726f)](https://kiro.dev/launch/mcp/add?name=awslabs.oracle-mcp-server&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22awslabs.oracle-mcp-server%40latest%22%2C%22--db_endpoint%22%2C%22%5Byour%20data%5D%22%2C%22--secret_arn%22%2C%22%5Byour%20data%5D%22%2C%22--database%22%2C%22%5Byour%20data%5D%22%2C%22--region%22%2C%22%5Byour%20data%5D%22%5D%2C%22env%22%3A%7B%22AWS_PROFILE%22%3A%22your-aws-profile%22%2C%22AWS_REGION%22%3A%22us-east-1%22%2C%22FASTMCP_LOG_LEVEL%22%3A%22ERROR%22%7D%7D)  
[![Install](https://camo.githubusercontent.com/4d3e06d6b1e8e227fd2832bd07fa928253a7e73216d4ffd1c89559cb56664b25/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f496e7374616c6c2d437572736f722d626c75653f7374796c653d666c61742d737175617265266c6f676f3d637572736f72)](https://cursor.com/en/install-mcp?name=awslabs.oracle-mcp-server&config=eyJjb21tYW5kIjogInV2eCBhd3NsYWJzLm9yYWNsZS1tY3Atc2VydmVyQGxhdGVzdCAtLWRiX2VuZHBvaW50IFt5b3VyIGRhdGFdIC0tc2VjcmV0X2FybiBbeW91ciBkYXRhXSAtLWRhdGFiYXNlIFt5b3VyIGRhdGFdIC0tcmVnaW9uIFt5b3VyIGRhdGFdIiwgImVudiI6IHsiQVdTX1BST0ZJTEUiOiAieW91ci1hd3MtcHJvZmlsZSIsICJBV1NfUkVHSU9OIjogInVzLWVhc3QtMSIsICJGQVNUTUNQX0xPR19MRVZFTCI6ICJFUlJPUiJ9LCAiZGlzYWJsZWQiOiBmYWxzZSwgImF1dG9BcHByb3ZlIjogW119)  
[![Install on VS Code](https://camo.githubusercontent.com/212f7838b46046e2e2aed6b559e0dddc15d4b911c8aef29f6571d931aa98700a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f496e7374616c6c2d56535f436f64652d4646393930303f7374796c653d666c61742d737175617265266c6f676f3d76697375616c73747564696f636f6465266c6f676f436f6c6f723d7768697465)](https://insiders.vscode.dev/redirect/mcp/install?name=Oracle%20MCP%20Server&config=%7B%22command%22%3A%22uvx%22%2C%22args%22%3A%5B%22awslabs.oracle-mcp-server%40latest%22%2C%22--db_endpoint%22%2C%22%5Byour%20data%5D%22%2C%22--secret_arn%22%2C%22%5Byour%20data%5D%22%2C%22--database%22%2C%22%5Byour%20data%5D%22%2C%22--region%22%2C%22%5Byour%20data%5D%22%5D%2C%22env%22%3A%7B%22AWS_PROFILE%22%3A%22your-aws-profile%22%2C%22AWS_REGION%22%3A%22us-east-1%22%2C%22FASTMCP_LOG_LEVEL%22%3A%22ERROR%22%7D%2C%22disabled%22%3Afalse%2C%22autoApprove%22%3A%5B%5D%7D) \|

##### Caching & Performance

[](#caching--performance-1)

[TABLE]

##### Workflow & Integration

[](#workflow--integration)

[TABLE]

##### Operations & Monitoring

[](#operations--monitoring)

[TABLE]

## MCP AWS Lambda Handler Module

[](#mcp-aws-lambda-handler-module)

A Python library for creating serverless HTTP handlers for the Model Context Protocol (MCP) using AWS Lambda. This module provides a flexible framework for building MCP HTTP endpoints with pluggable session management, including built-in DynamoDB support.

**Features:**

- Easy serverless MCP HTTP handler creation using AWS Lambda
- Pluggable session management system
- Built-in DynamoDB session backend support
- Customizable authentication and authorization
- Example implementations and tests

See [`src/mcp-lambda-handler/README.md`](/awslabs/mcp/blob/main/src/mcp-lambda-handler/README.md) for full usage, installation, and development instructions.

## When to use Local vs Remote MCP Servers?

[](#when-to-use-local-vs-remote-mcp-servers)

MCP servers can be run either locally on your development machine or remotely on the cloud. Here's when to use each approach:

### Local MCP Servers

[](#local-mcp-servers)

- **Development & Testing**: Perfect for local development, testing, and debugging
- **Offline Work**: Continue working when internet connectivity is limited
- **Data Privacy**: Keep sensitive data and credentials on your local machine
- **Low Latency**: Minimal network overhead for faster response times
- **Resource Control**: Direct control over server resources and configuration

### Remote MCP Servers

[](#remote-mcp-servers)

- **Team Collaboration**: Share consistent server configurations across your team
- **Resource Intensive Tasks**: Offload heavy processing to dedicated cloud resources
- **Always Available**: Access your MCP servers from anywhere, any device
- **Automatic Updates**: Get the latest features and security patches automatically
- **Scalability**: Easily handle varying workloads without local resource constraints
- **Security**: Centralized security controls with IAM-based permissions and zero credential exposure
- **Governance**: Comprehensive audit logging and compliance monitoring for enterprise-grade governance

> **Note**: Some MCP servers, like the [official AWS MCP server](https://docs.aws.amazon.com/aws-mcp/latest/userguide/what-is-mcp-server.html) (in preview) and AWS Knowledge MCP, are provided as fully managed services by AWS. These AWS-managed remote servers require no setup or infrastructure management on your part - just connect and start using them.

## Use Cases for the Servers

[](#use-cases-for-the-servers)

For example, you can use the **AWS Documentation MCP Server** to help your AI assistant research and generate up-to-date code for any AWS service, like Amazon Bedrock Inline agents. Alternatively, you could use the **CDK MCP Server** or the **Terraform MCP Server** to have your AI assistant create infrastructure-as-code implementations that use the latest APIs and follow AWS best practices. With the **AWS Pricing MCP Server**, you could ask "What would be the estimated monthly cost for this CDK project before I deploy it?" or "Can you help me understand the potential AWS service expenses for this infrastructure design?" and receive detailed cost estimations and budget planning insights. The **Valkey MCP Server** enables natural language interaction with Valkey data stores, allowing AI assistants to efficiently manage data operations through a simple conversational interface.

## Installation and Setup

[](#installation-and-setup)

Each server has specific installation instructions with one-click installs for Kiro, Cursor, and VSCode. Generally, you can:

1.  Install `uv` from [Astral](https://docs.astral.sh/uv/getting-started/installation/)
2.  Install Python using `uv python install 3.10`
3.  Configure AWS credentials with access to required services
4.  Add the server to your MCP client configuration

Example configuration for Kiro MCP settings (`~/.kiro/settings/mcp.json`):

### For macOS/Linux

[](#for-macoslinux)

    {
      "mcpServers": {
        "awslabs-core-mcp-server": {
          "command": "uvx",
          "args": [
            "awslabs.core-mcp-server@latest"
          ],
          "env": {
            "FASTMCP_LOG_LEVEL": "ERROR"
          }
        }
      }
    }

See individual server READMEs for specific requirements and configuration options.

### For Windows

[](#for-windows)

When configuring MCP servers on Windows, you'll need to use a slightly different configuration format:

    {
      "mcpServers": {
        "awslabs-core-mcp-server": {
          "disabled": false,
          "timeout": 60,
          "type": "stdio",
          "command": "uv",
          "args": [
            "tool",
            "run",
            "--from",
            "awslabs.core-mcp-server@latest",
            "awslabs.core-mcp-server.exe"
          ],
          "env": {
            "FASTMCP_LOG_LEVEL": "ERROR"
          }
        }
      }
    }

If you have problems with MCP configuration or want to check if the appropriate parameters are in place, you can try the following:

    # Run MCP server manually with timeout 15s
    $ timeout 15s uv tool run <MCP Name> <args> 2>&1 || echo "Command completed or timed out"

    # Example (Aurora MySQL MCP Server)
    $ timeout 15s uv tool run awslabs.mysql-mcp-server --resource_arn <Your Resource ARN> --secret_arn <Your Secret ARN> ... 2>&1 || echo "Command completed or timed out"

    # If the arguments are not set appropriately, you may see the following message:
    usage: awslabs.mysql-mcp-server [-h] --resource_arn RESOURCE_ARN --secret_arn SECRET_ARN --database DATABASE
                                    --region REGION --readonly READONLY
    awslabs.mysql-mcp-server: error: the following arguments are required: --resource_arn, --secret_arn, --database, --region, --readonly

**Note about performance when using `uvx` *"@latest"* suffix:**

Using the *"@latest"* suffix checks and downloads the latest MCP server package from pypi every time you start your MCP clients, but it comes with a cost of increased initial load times. If you want to minimize the initial load time, remove *"@latest"* and manage your uv cache yourself using one of these approaches:

- `uv cache clean <tool>`: where {tool} is the mcp server you want to delete from cache and install again (e.g.: "awslabs.lambda-tool-mcp-server") (remember to remove the '\<\>').
- `uvx <tool>@latest`: this will refresh the tool with the latest version and add it to the uv cache.

### Running MCP servers in containers

[](#running-mcp-servers-in-containers)

Docker images for each MCP server are published to the [public AWS ECR registry](https://gallery.ecr.aws/awslabs-mcp).

*This example uses docker with the "awslabs.aws-documentation-mcp-server and can be repeated for each MCP server*

- Optionally save sensitive environmental variables in a file:

      # contents of a .env file with fictitious AWS temporary credentials
      AWS_ACCESS_KEY_ID=ASIAIOSFODNN7EXAMPLE
      AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
      AWS_SESSION_TOKEN=AQoEXAMPLEH4aoAH0gNCAPy...truncated...zrkuWJOgQs8IZZaIv2BXIa2R4Olgk

- Use the docker options: `--env`, `--env-file`, and `--volume` as needed because the `"env": {}` are not available within the container.

      {
        "mcpServers": {
          "awslabs.aws-documentation-mcp-server": {
            "command": "docker",
            "args": [
              "run",
              "--rm",
              "--interactive",
              "--env",
              "FASTMCP_LOG_LEVEL=ERROR",
              "--env",
              "AWS_REGION=us-east-1",
              "--env-file",
              "/full/path/to/.env",
              "--volume",
              "/full/path/to/.aws:/app/.aws",
              "public.ecr.aws/awslabs-mcp/awslabs/aws-documentation-mcp-server:latest"
            ],
            "env": {}
          }
        }
      }

- For testing local changes you can build and tag the image. You have to update the MCP configuration to use this tag instead of the ECR image.

  ``` notranslate
  cd src/aws-documentation-mcp-server
  docker build -t awslabs/aws-documentation-mcp-server .
  ```

### Getting Started with Kiro

[](#getting-started-with-kiro)

Install in Kiro

See the [Kiro IDE documentation](https://kiro.dev/docs/mcp/configuration/) or the [Kiro CLI documentation](https://kiro.dev/docs/cli/mcp/configuration/) for details.

In the Kiro IDE:

1.  Navigate `Kiro` \> `MCP Servers`
2.  Add a new MCP server by clicking the `+ Add` button.
3.  Paste the configuration given below.

For global configuration, edit `~/.kiro/settings/mcp.json`. For project-specific configuration, edit `.kiro/settings/mcp.json` in your project directory.

#### `~/.kiro/settings/mcp.json`

[](#kirosettingsmcpjson)

For macOS/Linux:

    {
      "mcpServers": {
        "awslabs-core-mcp-server": {
          "command": "uvx",
          "args": ["awslabs.core-mcp-server@latest"],
          "env": {
            "FASTMCP_LOG_LEVEL": "ERROR"
          }
        }
      }
    }

For Windows:

    {
      "mcpServers": {
        "awslabs-core-mcp-server": {
          "disabled": false,
          "timeout": 60,
          "type": "stdio",
          "command": "uv",
          "args": [
            "tool",
            "run",
            "--from",
            "awslabs.core-mcp-server@latest",
            "awslabs.core-mcp-server.exe"
          ],
          "env": {
            "FASTMCP_LOG_LEVEL": "ERROR"
          }
        }
      }
    }

### Getting Started with Cline and Amazon Bedrock

[](#getting-started-with-cline-and-amazon-bedrock)

Getting Started with Cline and Amazon Bedrock

**IMPORTANT:** Following these instructions may incur costs and are subject to the [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/). You are responsible for any associated costs. In addition to selecting the desired model in the Cline settings, ensure you have your selected model (e.g. `anthropic.claude-3-7-sonnet`) also enabled in Amazon Bedrock. For more information on this, see [these AWS docs](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access-modify.html) on enabling model access to Amazon Bedrock Foundation Models (FMs).

1.  Follow the steps above in the **Installation and Setup** section to install `uv` from [Astral](https://docs.astral.sh/uv/getting-started/installation/), install Python, and configure AWS credentials with the required services.

2.  If using Visual Studio Code, install the [Cline VS Code Extension](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev) (or equivalent extension for your preferred IDE). Once installed, click the extension to open it. When prompted, select the tier that you wish. In this case, we will be using Amazon Bedrock, so the free tier of Cline is fine as we will be sending requests using the Amazon Bedrock API instead of the Cline API.

[![](/awslabs/mcp/raw/main/docs/images/root-readme/install-cline-extension.png)](/awslabs/mcp/blob/main/docs/images/root-readme/install-cline-extension.png)

3.  Select the **MCP Servers** button.

[![](/awslabs/mcp/raw/main/docs/images/root-readme/select-mcp-servers.png)](/awslabs/mcp/blob/main/docs/images/root-readme/select-mcp-servers.png)

4.  Select the **Installed** tab, then click **Configure MCP Servers** to open the `cline_mcp_settings.json` file.

[![](/awslabs/mcp/raw/main/docs/images/root-readme/configure-mcp-servers.png)](/awslabs/mcp/blob/main/docs/images/root-readme/configure-mcp-servers.png)

5.  In the `cline_mcp_settings.json` file, add your desired MCP servers in the `mcpServers` object. See the following example that will use some of the current MCP servers that are available in this repository. Ensure you save the file to install the MCP servers.

#### `cline_mcp_settings.json`

[](#cline_mcp_settingsjson)

For macOS/Linux:

    {
      "mcpServers": {
        "awslabs-core-mcp-server": {
          "command": "uvx",
          "args": ["awslabs.core-mcp-server@latest"],
          "env": {
            "FASTMCP_LOG_LEVEL": "ERROR",
            "MCP_SETTINGS_PATH": "path to your mcp settings file"
          }
        }
       }
     }

For Windows:

    {
      "mcpServers": {
        "awslabs-core-mcp-server": {
          "disabled": false,
          "timeout": 60,
          "type": "stdio",
          "command": "uv",
          "args": [
            "tool",
            "run",
            "--from",
            "awslabs.core-mcp-server@latest",
            "awslabs.core-mcp-server.exe"
          ],
          "env": {
            "FASTMCP_LOG_LEVEL": "ERROR",
            "MCP_SETTINGS_PATH": "path to your mcp settings file"
          }
        }
      }
    }

6.  Once installed, you should see a list of your MCP Servers under the MCP Server Installed tab, and they should have a green slider to show that they are enabled. See the following for an example with two of the possible MCP servers for AWS. Click **Done** when finished. You should now see the Cline chat interface.

[![](/awslabs/mcp/raw/main/docs/images/root-readme/mcp-servers-installed.png)](/awslabs/mcp/blob/main/docs/images/root-readme/mcp-servers-installed.png)

[![](/awslabs/mcp/raw/main/docs/images/root-readme/cline-chat-interface.png)](/awslabs/mcp/blob/main/docs/images/root-readme/cline-chat-interface.png)

7.  By default, Cline will be set as the API provider, which has limits for the free tier. Next, let's update the API provider to be AWS Bedrock, so we can use the LLMs through Bedrock, which would have billing go through your connected AWS account.

8.  Click the settings gear to open up the Cline settings. Then under **API Provider**, switch this from `Cline` to `AWS Bedrock` and select `AWS Profile` for the authentication type. As a note, the `AWS Credentials` option works as well, however it uses a static credentials (Access Key ID and Secret Access Key) instead of temporary credentials that are automatically redistributed when the token expires, so the temporary credentials with an AWS Profile is the more secure and recommended method.

[![](/awslabs/mcp/raw/main/docs/images/root-readme/cline-select-bedrock.png)](/awslabs/mcp/blob/main/docs/images/root-readme/cline-select-bedrock.png)

9.  Fill out the configuration based on the existing AWS Profile you wish to use, select the desired AWS Region, and enable cross-region inference.

[![](/awslabs/mcp/raw/main/docs/images/root-readme/cline-select-aws-profile.png)](/awslabs/mcp/blob/main/docs/images/root-readme/cline-select-aws-profile.png)

[![](/awslabs/mcp/raw/main/docs/images/root-readme/cline-api-provider-filled.png)](/awslabs/mcp/blob/main/docs/images/root-readme/cline-api-provider-filled.png)

10. Next, scroll down on the settings page until you reach the text box that says Custom Instructions. Paste in the following snippet to ensure the `mcp-core` server is used as the starting point for every prompt:

``` notranslate
For every new project, always look at your MCP servers and use mcp-core as the starting point every time. Also after a task completion include the list of MCP servers used in the operation.
```

[![](/awslabs/mcp/raw/main/docs/images/root-readme/cline-custom-instructions.png)](/awslabs/mcp/blob/main/docs/images/root-readme/cline-custom-instructions.png)

11. Once the custom prompt is pasted in, click **Done** to return to the chat interface.

12. Now you can begin asking questions and testing out the functionality of your installed MCP servers. The default option in the chat interface is is `Plan` which will provide the output for you to take manual action on (e.g. providing you a sample configuration that you copy and paste into a file). However, you can optionally toggle this to `Act` which will allow Cline to act on your behalf (e.g. searching for content using a web browser, cloning a repository, executing code, etc). You can optionally toggle on the "Auto-approve" section to avoid having to click to approve the suggestions, however we recommend leaving this off during testing, especially if you have the Act toggle selected.

**Note:** For the best results, please prompt Cline to use the desired MCP server you wish to use. For example, `Using the Terraform MCP Server, do...`

### Getting Started with Cursor

[](#getting-started-with-cursor)

Getting Started with Cursor

1.  Follow the steps above in the **Installation and Setup** section to install `uv` from [Astral](https://docs.astral.sh/uv/getting-started/installation/), install Python, and configure AWS credentials with the required services.

2.  You can place MCP configuration in two locations, depending on your use case:

A. **Project Configuration** - For tools specific to a project, create a `.cursor/mcp.json` file in your project directory. - This allows you to define MCP servers that are only available within that specific project.

B. **Global Configuration** - For tools that you want to use across all projects, create a `~/.cursor/mcp.json` file in your home directory. - This makes MCP servers available in all your Cursor workspaces.

#### `.cursor/mcp.json`

[](#cursormcpjson)

For macOS/Linux:

     {
      "mcpServers": {
        "awslabs-core-mcp-server": {
          "command": "uvx",
          "args": ["awslabs.core-mcp-server@latest"],
          "env": {
            "FASTMCP_LOG_LEVEL": "ERROR"
          }
        }
      }
    }

For Windows:

    {
      "mcpServers": {
        "awslabs-core-mcp-server": {
          "disabled": false,
          "timeout": 60,
          "type": "stdio",
          "command": "uv",
          "args": [
            "tool",
            "run",
            "--from",
            "awslabs.core-mcp-server@latest",
            "awslabs.core-mcp-server.exe"
          ],
          "env": {
            "FASTMCP_LOG_LEVEL": "ERROR"
          }
        }
      }
    }

3.  **Using MCP in Chat** The Composer Agent will automatically use any MCP tools that are listed under Available Tools on the MCP settings page if it determines them to be relevant. To prompt tool usage intentionally, please prompt Cursor to use the desired MCP server you wish to use. For example, `Using the Terraform MCP Server, do...`

4.  **Tool Approval** By default, when Agent wants to use an MCP tool, it will display a message asking for your approval. You can use the arrow next to the tool name to expand the message and see what arguments the Agent is calling the tool with.

### Getting Started with Windsurf

[](#getting-started-with-windsurf)

Getting Started with Windsurf

1.  Follow the steps above in the **Installation and Setup** section to install `uv` from [Astral](https://docs.astral.sh/uv/getting-started/installation/), install Python, and configure AWS credentials with the required services.

2.  **Access MCP Settings**

    - Navigate to Windsurf - Settings \> Advanced Settings or use the Command Palette \> Open Windsurf Settings Page
    - Look for the "Model Context Protocol (MCP) Servers" section

3.  **Add MCP Servers**

    - Click "Add Server" to add a new MCP server
    - You can choose from available templates like GitHub, Puppeteer, PostgreSQL, etc.
    - Alternatively, click "Add custom server" to configure your own server

4.  **Manual Configuration**

    - You can also manually edit the MCP configuration file located at `~/.codeium/windsurf/mcp_config.json`

#### `~/.codeium/windsurf/mcp_config.json`

[](#codeiumwindsurfmcp_configjson)

For macOS/Linux:

    {
      "mcpServers": {
        "awslabs-core-mcp-server": {
          "command": "uvx",
          "args": ["awslabs.core-mcp-server@latest"],
          "env": {
            "FASTMCP_LOG_LEVEL": "ERROR",
            "MCP_SETTINGS_PATH": "path to your mcp settings file"
          }
        }
       }
     }

For Windows:

    {
      "mcpServers": {
        "awslabs-core-mcp-server": {
          "disabled": false,
          "timeout": 60,
          "type": "stdio",
          "command": "uv",
          "args": [
            "tool",
            "run",
            "--from",
            "awslabs.core-mcp-server@latest",
            "awslabs.core-mcp-server.exe"
          ],
          "env": {
            "FASTMCP_LOG_LEVEL": "ERROR",
            "MCP_SETTINGS_PATH": "path to your mcp settings file"
          }
        }
      }
    }

### Getting Started with VS Code

[](#getting-started-with-vs-code)

Install in VS Code

Configure MCP servers in VS Code settings or in `.vscode/mcp.json` (see [VS Code MCP docs](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) for more info.):

#### `.vscode/mcp.json`

[](#vscodemcpjson)

For macOS/Linux:

    {
      "mcpServers": {
        "awslabs-core-mcp-server": {
          "command": "uvx",
          "args": ["awslabs.core-mcp-server@latest"],
          "env": {
            "FASTMCP_LOG_LEVEL": "ERROR"
          }
        }
      }
    }

For Windows:

    {
      "mcpServers": {
        "awslabs-core-mcp-server": {
          "disabled": false,
          "timeout": 60,
          "type": "stdio",
          "command": "uv",
          "args": [
            "tool",
            "run",
            "--from",
            "awslabs.core-mcp-server@latest",
            "awslabs.core-mcp-server.exe"
          ],
          "env": {
            "FASTMCP_LOG_LEVEL": "ERROR"
          }
        }
      }
    }

### Getting Started with Claude Code

[](#getting-started-with-claude-code)

Install in Claude Code

Configure MCP servers in Claude Code through the CLI or in `.mcp.json`

1.  Follow the steps above in the **Installation and Setup** section to install `uv` from [Astral](https://docs.astral.sh/uv/getting-started/installation/), install Python, and configure AWS credentials with the required services.

2.  **Using Claude Code CLI Commands**

    Claude Code CLI commands to add MCP servers:

        # Add core AWS services
        claude mcp add aws-api uvx awslabs.aws-api-mcp-server@latest
        claude mcp add aws-iac uvx awslabs.aws-iac-mcp-server@latest
        claude mcp add aws-docs uvx awslabs.aws-documentation-mcp-server@latest
        claude mcp add aws-support uvx awslabs.aws-support-mcp-server@latest
        claude mcp add aws-pricing uvx awslabs.aws-pricing-mcp-server@latest

        # Add AI/ML and Bedrock services
        claude mcp add bedrock-kb uvx awslabs.bedrock-kb-retrieval-mcp-server@latest

        # Add data and analytics services
        claude mcp add aws-dataprocessing uvx awslabs.aws-dataprocessing-mcp-server@latest
        claude mcp add aurora-dsql uvx awslabs.aurora-dsql-mcp-server@latest
        claude mcp add valkey uvx awslabs.valkey-mcp-server@latest

        # List installed servers
        claude mcp list

3.  **Manual Configuration (Alternative)**

    You can also manually configure MCP servers by creating a `.mcp.json` file in your project root:

#### `.mcp.json`

[](#mcpjson)

For macOS/Linux:

    {
      "mcpServers": {
        "awslabs.aws-iac-mcp-server": {
          "command": "uvx",
          "args": ["awslabs.aws-iac-mcp-server@latest"],
          "env": {
            "FASTMCP_LOG_LEVEL": "ERROR"
          }
        },
        "awslabs.aws-documentation-mcp-server": {
          "command": "uvx",
          "args": ["awslabs.aws-documentation-mcp-server@latest"],
          "env": {
            "FASTMCP_LOG_LEVEL": "ERROR",
            "AWS_DOCUMENTATION_PARTITION": "aws"
          }
        }
      }
    }

### Getting Started with fx

[](#getting-started-with-fx)

Install in fx

[fx](https://fx.sh) manages MCP servers from the terminal and stores them in `~/.fx/mcp.json`, so they are available in every project.

1.  Follow the steps above in the **Installation and Setup** section to install `uv` from [Astral](https://docs.astral.sh/uv/getting-started/installation/), install Python, and configure AWS credentials with the required services.

2.  **Using fx CLI commands**

        # The hosted AWS Knowledge MCP Server needs no credentials
        fx mcp add --transport http aws-knowledge https://knowledge-mcp.global.api.aws

        # Local servers take the executable and its arguments
        fx mcp add aws-api uvx awslabs.aws-api-mcp-server@latest
        fx mcp add aws-iac uvx awslabs.aws-iac-mcp-server@latest
        fx mcp add aws-iam uvx awslabs.iam-mcp-server@latest

        # List configured servers
        fx mcp list

3.  **Manual configuration (alternative)**

    Add the servers under the `mcp` key. fx uses `mcp` rather than `mcpServers`, `type` to select the transport, and a single `command` array holding the executable and its arguments.

#### `~/.fx/mcp.json`

[](#fxmcpjson)

    {
      "mcp": {
        "aws-knowledge-mcp-server": {
          "type": "http",
          "url": "https://knowledge-mcp.global.api.aws"
        },
        "awslabs.aws-iac-mcp-server": {
          "type": "local",
          "command": ["uvx", "awslabs.aws-iac-mcp-server@latest"],
          "environment": {
            "FASTMCP_LOG_LEVEL": "ERROR"
          }
        }
      }
    }

The first launch of a `uvx` server downloads the package, which can exceed the default startup timeout. Raise it for that server if needed:

    "startup_timeout_ms": 30000

If a session is already open when you edit the file, run `/mcp reload` to pick up the change.

## Samples

[](#samples)

Ready-to-use examples of open source MCP servers for AWS in action are available in the [samples](/awslabs/mcp/blob/main/samples) directory. These samples provide working code and step-by-step guides to help you get started with each MCP server.

## Vibe coding

[](#vibe-coding)

You can use these MCP servers with your AI coding assistant to [vibe code](https://en.wikipedia.org/wiki/Vibe_coding). For tips and tricks on how to improve your vibe coding experience, please refer to our [guide](/awslabs/mcp/blob/main/VIBE_CODING_TIPS_TRICKS.md).

## Additional Resources

[](#additional-resources)

- [Introducing AWS MCP Servers for code assistants](https://aws.amazon.com/blogs/machine-learning/introducing-aws-mcp-servers-for-code-assistants-part-1/)
- [Vibe coding with AWS MCP Servers \| AWS Show & Tell](https://www.youtube.com/watch?v=qXGQQRMrcz0)
- [Supercharging AWS database development with AWS MCP servers](https://aws.amazon.com/blogs/database/supercharging-aws-database-development-with-aws-mcp-servers/)
- [AWS costs estimation using Amazon Q CLI and AWS Pricing MCP Server](https://aws.amazon.com/blogs/machine-learning/aws-costs-estimation-using-amazon-q-cli-and-aws-cost-analysis-mcp/)
- [Introducing AWS Serverless MCP Server: AI-powered development for modern applications](https://aws.amazon.com/blogs/compute/introducing-aws-serverless-mcp-server-ai-powered-development-for-modern-applications/)
- [Announcing new Model Context Protocol (MCP) Servers for AWS Serverless and Containers](https://aws.amazon.com/about-aws/whats-new/2025/05/new-model-context-protocol-servers-aws-serverless-containers/)
- [Accelerating application development with the Amazon EKS MCP server](https://aws.amazon.com/blogs/containers/accelerating-application-development-with-the-amazon-eks-model-context-protocol-server/)
- [Amazon Neptune announces MCP (Model Context Protocol) Server](https://aws.amazon.com/about-aws/whats-new/2025/05/amazon-neptune-mcp-server/)
- [Terraform MCP Server Vibe Coding](https://youtu.be/i2nBD65md0Y)
- [How to Generate AWS Architecture Diagrams Using Amazon Q CLI and MCP](https://community.aws/content/2vPiiPiBSdRalaEax2rVDtshpf3/how-to-generate-aws-architecture-diagrams-using-amazon-q-cli-and-mcp)
- [Harness the power of MCP servers with Amazon Bedrock Agents](https://aws.amazon.com/blogs/machine-learning/harness-the-power-of-mcp-servers-with-amazon-bedrock-agents/)
- [Unlocking the power of Model Context Protocol (MCP) on AWS](https://aws.amazon.com/blogs/machine-learning/unlocking-the-power-of-model-context-protocol-mcp-on-aws/)
- [AWS Price List Gets a Natural Language Upgrade: Introducing the AWS Pricing MCP Server](https://aws.amazon.com/blogs/aws-cloud-financial-management/aws-price-list-gets-a-natural-language-upgrade-introducing-the-aws-pricing-mcp-server/)
- [AWS SheBuilds: AWS Team's Journey from Internal Tools to Open Source AI Infrastructure](https://www.youtube.com/watch?v=DZFgufNCvAo)
- [Guidance for Vibe Coding with AWS MCP servers](https://aws.amazon.com/solutions/guidance/vibe-coding-with-aws-mcp-servers/)
- [Vibe coding with AWS MCP Servers \| Hands-on Workshop](https://github.com/aws-solutions-library-samples/guidance-for-vibe-coding-with-aws-mcp-servers)

## Security

[](#security)

See [CONTRIBUTING](/awslabs/mcp/blob/main/CONTRIBUTING.md#security-issue-notifications) for more information.

## Contributing

[](#contributing)

Big shout out to our awesome contributors! Thank you for making this project better!

[![contributors](https://camo.githubusercontent.com/62c1e0b7920b3825087356da858bddccb02f64198618012265645287d8e93a54/68747470733a2f2f636f6e747269622e726f636b732f696d6167653f7265706f3d6177736c6162732f6d6370266d61783d32303030)](https://github.com/awslabs/mcp/graphs/contributors)

Contributions of all kinds are welcome! Check out our [contributor guide](/awslabs/mcp/blob/main/CONTRIBUTING.md) for more information.

## Developer guide

[](#developer-guide)

If you want to add a new MCP Server to the library, check out our [development guide](/awslabs/mcp/blob/main/DEVELOPER_GUIDE.md) and be sure to follow our [design guidelines](/awslabs/mcp/blob/main/DESIGN_GUIDELINES.md).

## License

[](#license)

This project is licensed under the Apache-2.0 License.

## Disclaimer

[](#disclaimer)

Before using an MCP Server, you should consider conducting your own independent assessment to ensure that your use would comply with your own specific security and quality control practices and standards, as well as the laws, rules, and regulations that govern you and your content.

## About

Open source MCP Servers for AWS

[awslabs.github.io/mcp/](https://awslabs.github.io/mcp/)

### Topics

[aws](/topics/aws)[mcp](/topics/mcp)[mcp-client](/topics/mcp-client)[mcp-clients](/topics/mcp-clients)[mcp-host](/topics/mcp-host)[mcp-server](/topics/mcp-server)[mcp-servers](/topics/mcp-servers)[mcp-tools](/topics/mcp-tools)[modelcontextprotocol](/topics/modelcontextprotocol)

### Resources

[Readme](#readme-ov-file)

[Apache-2.0 license](#Apache-2.0-1-ov-file)

### Code of conduct

[Code of conduct](/awslabs/mcp#coc-ov-file)

### Contributing

[Contributing](#contributing-ov-file)

### Security policy

[Security policy](#security-ov-file)

[Activity](/awslabs/mcp/activity)

[Custom properties](/awslabs/mcp/custom-properties)

### Stars

**9.7k** stars

### Watchers

**82** watching

### Forks

[**1.8k** forks](/awslabs/mcp/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fawslabs%2Fmcp&report=awslabs+%28user%29)

## Releases

## Packages

## Used by

## Contributors

## Languages

Generated from [amazon-archives/\_\_template_Apache-2.0](/amazon-archives/__template_Apache-2.0)

---
title: A2A on Amzon Bedrock AgentCore Runtime Frontend
description: 'This is a single-page application that provides a chat interface for interacting with Host Google ADK Agent. The app handles OAuth authentication via AWS Cognito, streams responses from the agent in real-time, and displays the complete agentic workflow including tool invocations '
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/02-use-cases/01-conversational-agents/A2A-multi-agent-incident-response/frontend/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# A2A on Amzon Bedrock AgentCore Runtime Frontend

## Overview

This is a single-page application that provides a chat interface for interacting with Host Google ADK Agent. The app handles OAuth authentication via AWS Cognito, streams responses from the agent in real-time, and displays the complete agentic workflow including tool invocations and their results.

## Getting Started

### Prerequisites

- Node.js 18 or higher, use [documentation](https://nodejs.org/en/download).

### Installation

```bash
cd frontend
npm install
```

### Configuration

Create a `.env` file in this directory:

```bash
chmod +x ./setup-env.sh
./setup-env.sh
```

### Running Locally

```bash
npm run dev
```

The app will be available at `http://localhost:5173`

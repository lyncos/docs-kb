---
title: Serverless Telephony with Sonic and AgentCore Runtime
description: aws-samples / **sample-vonage-serverless-sonic** Public
product: Amazon Bedrock AgentCore
section: References / github.com
source_url: https://github.com/aws-samples/sample-vonage-serverless-sonic
fetched: '2026-09-26'
tags:
- agentcore
- github-com
- reference
- related
referenced_by:
- runtime-bidirectional-streaming-examples.md
conversion: pandoc
---

[aws-samples](/aws-samples) / **[sample-vonage-serverless-sonic](/aws-samples/sample-vonage-serverless-sonic)** Public

- [Notifications](/login?return_to=%2Faws-samples%2Fsample-vonage-serverless-sonic) You must be signed in to change notification settings

- [Fork 0](/login?return_to=%2Faws-samples%2Fsample-vonage-serverless-sonic)

- [ Star 4](/login?return_to=%2Faws-samples%2Fsample-vonage-serverless-sonic)

[](/aws-samples/sample-vonage-serverless-sonic)

main

[Branches](/aws-samples/sample-vonage-serverless-sonic/branches)[Tags](/aws-samples/sample-vonage-serverless-sonic/tags)

[](/aws-samples/sample-vonage-serverless-sonic/branches)[](/aws-samples/sample-vonage-serverless-sonic/tags)

Go to file

Code

Open more actions menu

## Latest commit

 

## History

[10 Commits](/aws-samples/sample-vonage-serverless-sonic/commits/main/)

[](/aws-samples/sample-vonage-serverless-sonic/commits/main/)10 Commits

## Folders and files

[TABLE]

## Repository files navigation

# Serverless Telephony with Sonic and AgentCore Runtime

[](#serverless-telephony-with-sonic-and-agentcore-runtime)

by Reilly Manton

A serverless contact center agent that enables natural conversations using Amazon Bedrock's Nova Sonic model and AWS AgentCore Runtime's bidirectional streaming capabilities.

## Overview

[](#overview)

This project demonstrates how to build a voice agent that handles phone calls through the Vonage Voice API, processing audio in real-time with Amazon Bedrock's Nova Sonic model.

AgentCore Runtime's bidirectional streaming support enables natural, interruptible conversations over WebSocket connections. Previously, connecting Nova Sonic to voice APIs over the phone required managing EC2, ECS, or EKS infrastructure to handle the WebSocket connections. AgentCore Runtime provides a serverless, purpose-built agent runtime environment that manages these voice API connections without requiring container orchestration or server provisioning.

## Architecture

[](#architecture)

[![Architecture Diagram](/aws-samples/sample-vonage-serverless-sonic/raw/main/images/vonage-serverless-sonic.png)](/aws-samples/sample-vonage-serverless-sonic/blob/main/images/vonage-serverless-sonic.png)

The application uses a two-tier architecture: H

1.  **Lambda URL Generator**: Receives Vonage answer requests and generates presigned WebSocket URLs for AgentCore Runtime
2.  **AgentCore Runtime WebSocket Bridge**: Bridges Vonage's WebSocket audio stream (16kHz, 16-bit PCM) directly to Amazon Bedrock's Nova Sonic model

This enables:

- Continuous audio input processing
- Real-time speech-to-text transcription
- Natural language understanding and response generation
- Text-to-speech audio output streaming back to the caller

## Prerequisites

[](#prerequisites)

- AWS Account with Bedrock access
- Amazon Nova Sonic model enabled in your AWS region
- Vonage API account
- Python 3.12+
- AWS CDK (for deployment)

## Project Structure

[](#project-structure)

``` notranslate
.
├── .env
├── lambda/
│   └── api/
│       ├── index.py           # Vonage webhook handler
│       └── requirements.txt   # Lambda dependencies
├── runtime/
│   ├── index.py               # AgentCore Runtime application
│   ├── requirements.txt       # Runtime dependencies
│   └── Dockerfile             # Container configuration
└── cdk/
    ├── lib/
    │   └── cdk-stack.ts       # Infrastructure as code
    └── bin/
        └── cdk.ts             # CDK app entry point
```

## Deployment

[](#deployment)

### 1. Prerequisites

[](#1-prerequisites)

- AWS account w/ CDK bootstrap complete
- AWS CLI configured with appropriate credentials
- Node.js and npm installed
- Docker installed and running (for building the runtime container)

### \### 2. Create a Vonage Application

[](#-2-create-a-vonage-application)

1.  Create a Vonage application in the Vonage Dashboard and capture the `APPLICATION ID` from the Vonage console.
2.  Copy .env.template to a new file .env and add your vonage application ID.

### 2. Deploy Infrastructure

[](#2-deploy-infrastructure)

    cd cdk
    npm install
    cdk deploy

### 3. Configure Vonage

[](#3-configure-vonage)

After deployment, the CDK will output the API Gateway URLs. Configure your Vonage application:

1.  Go to the vonage application page where you previously got your application ID.
2.  Set the **Answer URL** to the `AnswerUrl` output (e.g., `https://xxx.execute-api.us-east-1.amazonaws.com/vonage/answer`)
3.  Set the **Event URL** to the `EventUrl` output (e.g., `https://xxx.execute-api.us-east-1.amazonaws.com/vonage/event`)
4.  Set the **Fallback URL** to the `FallbackUrl` output (e.g., `https://xxx.execute-api.us-east-1.amazonaws.com/vonage/fallback`)
5.  Configure a phone number to use the application

## How It Works

[](#how-it-works)

### 1. Incoming Call

[](#1-incoming-call)

When a call comes in, Vonage sends an HTTP GET request to the `/vonage/answer` endpoint.

### 2. Presigned URL Generation

[](#2-presigned-url-generation)

The Lambda function:

- Receives the webhook with call metadata (UUID, caller number)
- Generates a presigned WebSocket URL for the AgentCore Runtime (valid for 5 minutes)
- Returns an NCCO (Nexmo Call Control Object) instructing Vonage to connect to the WebSocket

### 3. WebSocket Connection

[](#3-websocket-connection)

Vonage establishes a WebSocket connection to the AgentCore Runtime using the presigned URL. The first message contains metadata about the call.

### 4. Audio Streaming

[](#4-audio-streaming)

Vonage streams raw PCM audio (16kHz, 16-bit, mono) in 20ms chunks (640 bytes). The application:

- Receives audio chunks via WebSocket
- Base64 encodes and forwards to Nova Sonic
- Maintains the bidirectional stream connection

### 5. Response Processing

[](#5-response-processing)

Nova Sonic processes the audio stream and returns:

- Speech-to-text transcriptions
- Natural language responses (text)
- Text-to-speech audio output

The application streams audio responses back to Vonage in real-time.

## Key Components

[](#key-components)

### Lambda Webhook Handler (`lambda/api/index.py`)

[](#lambda-webhook-handler-lambdaapiindexpy)

Handles Vonage webhook callbacks:

- `/vonage/answer`: Generates presigned WebSocket URL and returns NCCO
- `/vonage/event`: Logs call events (start, end, etc.)
- `/vonage/fallback`: Handles connection failures

### AgentCore Runtime (`runtime/index.py`)

[](#agentcore-runtime-runtimeindexpy)

#### NovaSonicBridge Class

[](#novasonicbridge-class)

Manages the bidirectional stream with Nova Sonic:

- Session initialization with system prompt
- Audio input/output configuration
- Event processing (transcriptions, audio, usage)
- Graceful session cleanup

#### WebSocket Handler

[](#websocket-handler)

Bridges Vonage and Nova Sonic:

- Accepts incoming WebSocket connections
- Routes audio between Vonage and Nova Sonic
- Handles connection lifecycle

## Configuration

[](#configuration)

The runtime uses the following defaults (hardcoded in `runtime/index.py`):

- **Voice ID**: `tiffany`
- **System Prompt**: "You are a friendly phone assistant. Keep responses short and conversational."
- **Region**: `us-east-1`

To customize these, modify the values in `runtime/index.py`:

    MODEL_ID = "amazon.nova-2-sonic-v1:0"
    REGION = os.getenv("AWS_DEFAULT_REGION", "us-east-1")
    VOICE_ID = os.getenv("VOICE_ID", "tiffany")
    SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT", "You are a friendly phone assistant. Keep responses short and conversational.")

## Contributing

[](#contributing)

Contributions welcome! Please open an issue or submit a pull request.

## About

No description, website, or topics provided.

### Resources

[Readme](#readme-ov-file)

[MIT-0 license](#MIT-0-1-ov-file)

### Code of conduct

[Code of conduct](/aws-samples/sample-vonage-serverless-sonic#coc-ov-file)

### Contributing

[Contributing](#contributing-ov-file)

### Security policy

[Security policy](#security-ov-file)

[Activity](/aws-samples/sample-vonage-serverless-sonic/activity)

[Custom properties](/aws-samples/sample-vonage-serverless-sonic/custom-properties)

### Stars

**4** stars

### Watchers

**0** watching

### Forks

[**0** forks](/aws-samples/sample-vonage-serverless-sonic/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Faws-samples%2Fsample-vonage-serverless-sonic&report=aws-samples+%28user%29)

## Releases

## Packages

## Used by

## Contributors

## Languages

Generated from [amazon-archives/\_\_template_MIT-0](/amazon-archives/__template_MIT-0)

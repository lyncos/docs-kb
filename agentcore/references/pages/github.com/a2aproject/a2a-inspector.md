---
title: A2A Protocol Inspector
description: a2aproject / **a2a-inspector** Public
product: Amazon Bedrock AgentCore
section: References / github.com
source_url: https://github.com/a2aproject/a2a-inspector
fetched: '2026-09-26'
tags:
- agentcore
- github-com
- reference
- related
referenced_by:
- runtime-a2a.md
conversion: pandoc
---

[a2aproject](/a2aproject) / **[a2a-inspector](/a2aproject/a2a-inspector)** Public

- [Notifications](/login?return_to=%2Fa2aproject%2Fa2a-inspector) You must be signed in to change notification settings

- [Fork 154](/login?return_to=%2Fa2aproject%2Fa2a-inspector)

- [ Star 492](/login?return_to=%2Fa2aproject%2Fa2a-inspector)

[](/a2aproject/a2a-inspector)

main

[Branches](/a2aproject/a2a-inspector/branches)[Tags](/a2aproject/a2a-inspector/tags)

[](/a2aproject/a2a-inspector/branches)[](/a2aproject/a2a-inspector/tags)

Go to file

Code

Open more actions menu

## Latest commit

 

## History

[75 Commits](/a2aproject/a2a-inspector/commits/main/)

[](/a2aproject/a2a-inspector/commits/main/)75 Commits

## Folders and files

[TABLE]

## Repository files navigation

# A2A Protocol Inspector

[](#a2a-protocol-inspector)

The A2A Inspector is a web-based tool designed to help developers inspect, debug, and validate servers that implement the A2A (Agent2Agent) protocol. It provides a user-friendly interface to interact with an A2A agent, view communication, and ensure specification compliance.

The application is built with a FastAPI backend and a TypeScript frontend.

## Features

[](#features)

- **Connect to a local A2A Agent:** Specify the base URL of any agent server to connect (e.g., `http://localhost:5555`).
- **View Agent Card:** Automatically fetches and displays the agent's card.
- **Spec Compliance Checks:** Performs basic validation on the agent card to ensure it adheres to the A2A specification.
- **Live Chat:** A chat interface to send and receive messages with the connected agent.
- **Debug Console:** A slide-out console shows the raw JSON-RPC 2.0 messages sent and received between the inspector and the agent server.

## Prerequisites

[](#prerequisites)

- Python 3.10+
- [uv](https://github.com/astral-sh/uv)
- Node.js and npm

## Project Structure

[](#project-structure)

This repository is organized into two main parts:

- `./backend/`: Contains the Python FastAPI server that handles WebSocket connections and communication with the A2A agent.
- `./frontend/`: Contains the TypeScript and CSS source files for the web interface.

## Setup and Running the Application

[](#setup-and-running-the-application)

Follow these steps to get the A2A Inspector running on your local machine. The setup is a three-step process: install Python dependencies, install Node.js dependencies, and then run the two processes.

### 1. Clone the repository

[](#1-clone-the-repository)

    git clone https://github.com/a2aproject/a2a-inspector.git
    cd a2a-inspector

### 2. Install Dependencies

[](#2-install-dependencies)

First, install the Python dependencies for the backend from the root directory. `uv sync` reads the `uv.lock` file and installs the exact versions of the packages into a virtual environment.

    # Run from the root of the project
    uv sync

Next, install the Node.js dependencies for the frontend.

    # Navigate to the frontend directory
    cd frontend

    # Install npm packages
    npm install

    # Go back to the root directory
    cd ..

### 3. Run the Application

[](#3-run-the-application)

You can run the A2A Inspector in two ways. Choose the option that best fits your workflow:

- Option 1 (Run Locally): Best for developers who are actively modifying the code. This method uses two separate terminal processes and provides live-reloading for both the frontend and backend.
- Option 2 (Run with Docker): Best for quickly running the application without managing local Python and Node.js environments. Docker encapsulates all dependencies into a single container.

#### Option 1: Run Locally

[](#option-1-run-locally)

This approach requires you to run two processes concurrently. You can either use the provided convenience script or run them separately in different terminals.

**Using the convenience script (recommended):**

    # Make the script executable (first time only)
    chmod +x scripts/run.sh

    # Run both frontend and backend with a single command
    bash scripts/run.sh

This will start both the frontend build process and backend server, displaying their outputs with colored prefixes. Press `Ctrl+C` to stop both services.

**Or manually in separate terminals:**

Make sure you are in the root directory of the project (`a2a-inspector`) before starting.

**In your first terminal**, run the frontend development server. This will build the assets and automatically rebuild them when you make changes.

    # Navigate to the frontend directory
    cd frontend

    # Build the frontend and watch for changes
    npm run build -- --watch

**In a second terminal**, run the backend Python server.

    # Navigate to the backend directory
    cd backend

    # Run the FastAPI server with live reload
    uv run -- uvicorn app:app --host 127.0.0.1 --port 5001 --reload

##### Access the Inspector

[](#access-the-inspector)

Once both processes are running, open your web browser and navigate to: **[http://127.0.0.1:5001](http://127.0.0.1:5001)**

#### Option Two: Run with Docker

[](#option-two-run-with-docker)

This approach builds the entire application into a single Docker image and runs it as a container. This is the simplest way to run the inspector if you have Docker installed and don't need to modify the code.

From the root directory of the project, run the following command. This will build the frontend, copy the results into the backend, and package everything into an image named a2a-inspector.

    docker build -t a2a-inspector .

Once the image is built, run it as a container.

    # It will run the container in detached mode (in the background)
    docker run -d -p 8080:8080 a2a-inspector

The container is now running in the background. Open your web browser and navigate to: **[http://127.0.0.1:8080](http://127.0.0.1:8080)**

### 4. Inspect your agents

[](#4-inspect-your-agents)

- Try inputting a sample agent URL such as `https://sample-a2a-agent-908687846511.us-central1.run.app`

## About

Validation Tools for A2A Agents

### Resources

[Readme](#readme-ov-file)

[Apache-2.0 license](#Apache-2.0-1-ov-file)

### Code of conduct

[Code of conduct](/a2aproject/a2a-inspector#coc-ov-file)

### Contributing

[Contributing](#contributing-ov-file)

### Security policy

[Security policy](#security-ov-file)

[Activity](/a2aproject/a2a-inspector/activity)

[Custom properties](/a2aproject/a2a-inspector/custom-properties)

### Stars

**492** stars

### Watchers

**5** watching

### Forks

[**154** forks](/a2aproject/a2a-inspector/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fa2aproject%2Fa2a-inspector&report=a2aproject+%28user%29)

## Releases

## Used by

## Contributors

## Languages

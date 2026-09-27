---
title: The open source toolkit for building production agents.
description: 'Quick start GitHub '
product: Amazon Bedrock AgentCore
section: References / strandsagents.com
source_url: https://strandsagents.com
fetched: '2026-09-26'
tags:
- agentcore
- reference
- related
- strandsagents-com
referenced_by:
- diagnose-evaluation-skill-source.md
- harness-vs-runtime.md
- harness.md
conversion: pandoc
---

# The open source toolkit for building production agents.

[Quick start ](/docs/user-guide/harness/quickstart/)[GitHub ](https://github.com/strands-agents)

`$``npm install @strands-agents/harness`

copy

### Explore by Toolkit

### Start

#### /harness

Strands harness is a state-of-the-art, fully assembled agent harness.

- Optimized
- CLI or library
- Fully customizable

#### /harness

Strands harness is a fully assembled, state-of-the-art agent harness. It gives you an optimized agent with benchmarked defaults for the system prompt, tools, memory, sessions, and context management, ready to take from idea to production.

- 

  **Optimized defaults** Every default is tuned and optimized. Spend your time on what makes your agent different, not on wiring up a harness piece by piece.

- 

  **CLI or library** Build an agent with the strands CLI, or import it in Python or TypeScript.

- 

  **Customize anything** Strands harness is built on the Strands Harness SDK, so nothing is a black box. Swap the model provider, override any default, add your own tools, or go all the way down to the primitives, with no rewrite.

``` toolkit__card-terminal-code
                          1
                          import { createHarness } from "@strands-agents/harness"
                        
                          2
                          
                        
                          3
                          const agent = await createHarness()
                        
                          4
                          await agent.invoke("Summarize what this repository does")
                        
```

``` toolkit__card-terminal-code
                        1
                        from strands_harness import create_harness
                      
                        2
                        
                      
                        3
                        agent = create_harness()
                      
                        4
                        agent("Summarize what this repository does")
                      
```

[View more ](/docs/user-guide/harness/)

### Build

#### /harness-sdk

The Harness SDK for building an agent harness from the ground up.

- Own the loop
- Tools & MCP
- Any model

#### /harness-sdk

Build an agent harness from the ground up, end to end. The Strands Harness SDK runs the agent loop and gives you the pieces to attach to it: tools, model providers, memory, sessions, and hooks. Nothing is pre-decided.

- 

  **You own the loop** Choose every component and how they fit. Hooks, interventions, and context management give you control at every step.

- 

  **Tools, your way** Turn any function into a tool with the @tool decorator, or connect MCP servers. The schema comes from your type hints and docstring.

- 

  **Any model provider** Bedrock, Anthropic, OpenAI, Google, Ollama, and more. The model is one object you hand to the agent; the rest of your code stays the same.

``` toolkit__card-terminal-code
                          1
                          import { Agent, tool } from "@strands-agents/sdk"
                        
                          2
                          import { z } from "zod"
                        
                          3
                          
                        
                          4
                          const searchDocs = tool({
                        
                          5
                            name: "search_docs",
                        
                          6
                            description: "Search the documentation.",
                        
                          7
                            inputSchema: z.object({ query: z.string() }),
                        
                          8
                            callback: (input) => index.search(input.query),
                        
                          9
                          })
                        
                          10
                          
                        
                          11
                          const agent = new Agent({ model: "global.anthropic.claude-sonnet-5", tools: [searchDocs] })
                        
                          12
                          await agent.invoke("Find the pricing guide")
                        
```

``` toolkit__card-terminal-code
                        1
                        from strands import Agent, tool
                      
                        2
                        
                      
                        3
                        @tool
                      
                        4
                        def search_docs(query: str) -> str:
                      
                        5
                            """Search the documentation."""
                      
                        6
                            return index.search(query)
                      
                        7
                        
                      
                        8
                        agent = Agent(
                      
                        9
                          model="global.anthropic.claude-sonnet-5",
                      
                        10
                          tools=[search_docs],
                      
                        11
                        )
                      
                        12
                        agent("Find the pricing guide")
                      
```

[View more ](/docs/user-guide/sdk/tools/)

### Control

#### /shell

A virtual shell designed for AI agents to use safely.

- Sandboxed
- MCP server
- Python/TS

#### /shell

Strands Shell is a Bourne-compatible shell that runs inside your own process. It ships grep, sed, jq, curl, find, and dozens of other commands without fork, exec, or a raw syscall. You declare which host files, URLs, and credentials it can reach, and everything else is invisible to the agent.

- 

  **In-process sandbox** Runs dozens of Unix commands inside your process: no fork, no exec, no raw syscall, no container to manage.

- 

  **You declare the surface** Bind directories, inject credentials, and set the network allowlist. Everything else does not exist to the agent.

- 

  **Python, Node, or MCP** Embed it directly from Python or Node.js, or point any MCP client at the built-in server.

``` toolkit__card-terminal-code
                          1
                          import { Shell } from "@strands-agents/shell"
                        
                          2
                          
                        
                          3
                          const shell = await Shell.create({
                        
                          4
                            binds: [{ source: "/my/project", destination: "/workspace", mode: "copy" }],
                        
                          5
                          })
                        
                          6
                          
                        
                          7
                          const result = await shell.run("grep -rn TODO /workspace")
                        
                          8
                          console.log(result.stdout)
                        
```

``` toolkit__card-terminal-code
                        1
                        import strands_shell
                      
                        2
                        
                      
                        3
                        shell = strands_shell.Shell(
                      
                        4
                          binds=[strands_shell.Bind("/my/project", "/workspace", mode="copy")],
                      
                        5
                        )
                      
                        6
                        
                      
                        7
                        result = shell.run("grep -rn TODO /workspace")
                      
                        8
                        print(result.stdout)
                      
```

[View more ](/docs/user-guide/shell/)

### Validate

#### /evals

Validate your agent before you ship.

- Score
- Diagnose
- Simulate

#### /evals

Strands Evals lets you validate your agent before you ship. Score its output and its trajectory, find the root cause when a case fails, and simulate the users and tools it will meet in production.

- 

  **Score** 25+ built-in evaluators check a single answer, a full turn, or a whole conversation: output quality, tool selection, trajectory, goal success, and safety.

- 

  **Diagnose** When a case fails, detectors read the trace, find the span where things went wrong, and propose a root cause. Scoring says whether; diagnosis says why.

- 

  **Simulate** Simulators play the user or stand in for a tool, so you can score multi-turn behavior and run red-team attacks without a human in the loop.

``` toolkit__card-terminal-code
                        1
                        from strands import Agent
                      
                        2
                        from strands_evals import eval_task, Case, Experiment
                      
                        3
                        from strands_evals.evaluators import OutputEvaluator
                      
                        4
                        
                      
                        5
                        @eval_task()
                      
                        6
                        def task():
                      
                        7
                            return Agent(system_prompt="You are helpful.")
                      
                        8
                        
                      
                        9
                        cases = [Case[str, str](
                      
                        10
                          input="Capital of France?", expected_output="Paris")]
                      
                        11
                        
                      
                        12
                        Experiment[str, str](cases=cases,
                      
                        13
                          evaluators=[OutputEvaluator(rubric="Correct?")],
                      
                        14
                        ).run_evaluations(task)
                      
```

The Evals SDK is Python-only.

[View more ](/docs/user-guide/evals-sdk/quickstart/)

### Explore

#### /labs

Experimental projects pushing the boundaries of what agents can do.

- Robotics
- World models
- Benchmarks

#### /labs

Strands Labs is the experimental arm of Strands Agents: open source projects that take the Strands Harness SDK into new problem spaces. They move faster and cover more surface area than the core Strands Harness SDK, so expect more frequent changes and newer integrations.

- 

  **Robots** Control, simulate, and train robots with natural language. Sim-first, with 70+ robots behind one interface.

- 

  **World models and benchmarks** Agentic benchmark harnesses, harness optimization, and world-model research built on the Strands Harness SDK.

- 

  **Works alongside the Strands Harness SDK today** Each project is published to package repositories and lives in its own repository under strands-labs. Some graduate into the core Strands Harness SDK; others stay experimental.

[View more ](/docs/labs/)

Bring your own model — works with every major provider

-  Automate workflowsClassify, score, and route. One agent, one job. Replace brittle scripts with tools that adapt when your process changes.
-  Build AI AssistantsBuild assistants that reason over your own data by giving an agent retrieval tools. Strands harness manages context across turns, keeping the conversation within the model’s window.
-  Build research agentsBuild agents that work autonomously through multi-step tasks, calling tools to gather and synthesize information. The agent loops on its own — you describe the goal, not the steps.
-  Control robotsDrive arms, humanoids, quadrupeds, and drones with natural language. One Robot() call gives an agent a MuJoCo simulation or a real robot — same code, sim or hardware.

``` terminal__code
                1
                import { createHarness } from '@strands-agents/harness'
              
                2
                import { tool } from '@strands-agents/sdk'
              
                3
                import z from 'zod'
              
                4
                
              
                5
                const classifyLead = tool({
              
                6
                  name: 'classify_lead',
              
                7
                  description: 'Score and classify a lead.',
              
                8
                  inputSchema: z.object({
              
                9
                    email: z.string(),
              
                10
                    company: z.string(),
              
                11
                  }),
              
                12
                  callback: ({ email, company }) => {
              
                13
                    const data = crm.lookup(company)
              
                14
                    return {
              
                15
                      leadId: crm.createLead(email, company),
              
                16
                      score: computeIcpScore(data),
              
                17
                      segment: data.industry,
              
                18
                    }
              
                19
                  },
              
                20
                })
              
                21
                
              
                22
                const routeToRep = tool({
              
                23
                  name: 'route_to_rep',
              
                24
                  description: 'Assign a lead to a rep.',
              
                25
                  inputSchema: z.object({
              
                26
                    leadId: z.string(),
              
                27
                    region: z.string(),
              
                28
                  }),
              
                29
                  callback: ({ leadId, region }) => {
              
                30
                    const rep = crm.getRepForRegion(region)
              
                31
                    crm.assign(leadId, rep)
              
                32
                    return `Assigned to ${rep}`
              
                33
                  },
              
                34
                })
              
                35
                
              
                36
                const agent = await createHarness({
              
                37
                  tools: [classifyLead, routeToRep],
              
                38
                })
              
                39
                
              
                40
                await agent.invoke(
              
                41
                  'New lead: jane@acme.com, Acme Corp, US-West'
              
                42
                )
              
```

``` terminal__code
                1
                from strands import tool
              
                2
                from strands_harness import create_harness
              
                3
                
              
                4
                @tool
              
                5
                def classify_lead(email: str, company: str) -> dict:
              
                6
                    """Score and classify a lead."""
              
                7
                    data = crm.lookup(company)
              
                8
                    return {
              
                9
                        "lead_id": crm.create_lead(email, company),
              
                10
                        "score": compute_icp_score(data),
              
                11
                        "segment": data["industry"],
              
                12
                    }
              
                13
                
              
                14
                @tool
              
                15
                def route_to_rep(lead_id: str, region: str) -> str:
              
                16
                    """Assign a lead to a rep."""
              
                17
                    rep = crm.get_rep_for_region(region)
              
                18
                    crm.assign(lead_id, rep)
              
                19
                    return f"Assigned to {rep}"
              
                20
                
              
                21
                agent = create_harness(tools=[classify_lead, route_to_rep])
              
                22
                agent("New lead: jane@acme.com, Acme Corp, US-West")
              
```

``` terminal__code
                1
                import { createHarness } from '@strands-agents/harness'
              
                2
                import { tool } from '@strands-agents/sdk'
              
                3
                import z from 'zod'
              
                4
                
              
                5
                const issueRefund = tool({
              
                6
                  name: 'issue_refund',
              
                7
                  description: 'Process a customer refund.',
              
                8
                  inputSchema: z.object({ orderId: z.string(), amount: z.number() }),
              
                9
                  callback: ({ orderId, amount }) => payments.refund(orderId, amount),
              
                10
                })
              
                11
                
              
                12
                const agent = await createHarness({
              
                13
                  instructions: 'Support assistant. Use the KB. Refunds require approval.',
              
                14
                  tools: [issueRefund],
              
                15
                  mcpServers: { kb: { command: 'uvx', args: ['kb-server'] } },
              
                16
                  interventions: 'Ask before issuing any refund.',
              
                17
                })
              
                18
                
              
                19
                await agent.invoke('Order A1234 wants a $40 refund. Policy, and can you process it?')
              
```

``` terminal__code
                1
                from strands import tool
              
                2
                from strands_harness import create_harness
              
                3
                
              
                4
                @tool
              
                5
                def issue_refund(order_id: str, amount: float) -> str:
              
                6
                    """Process a customer refund."""
              
                7
                    return payments.refund(order_id, amount)
              
                8
                
              
                9
                agent = create_harness(
              
                10
                    instructions="Support assistant. Use the KB. Refunds require approval.",
              
                11
                    tools=[issue_refund],
              
                12
                    mcp_servers={"kb": {"command": "uvx", "args": ["kb-server"]}},
              
                13
                    interventions="Ask before issuing any refund.",
              
                14
                )
              
                15
                agent("Order A1234 wants a $40 refund. Policy, and can you process it?")
              
```

``` terminal__code
                1
                import { createHarness } from '@strands-agents/harness'
              
                2
                
              
                3
                // Web fetch and search are built in, on by default.
              
                4
                const agent = await createHarness({
              
                5
                  instructions: 'Research the goal, fetch sources, cite them.',
              
                6
                })
              
                7
                
              
                8
                await agent.invoke(
              
                9
                  'Summarize recent advances in solid-state batteries from https://en.wikipedia.org/wiki/Solid-state_battery'
              
                10
                )
              
```

``` terminal__code
                1
                from strands_harness import create_harness
              
                2
                
              
                3
                # Web fetch and search are built in, on by default.
              
                4
                agent = create_harness(instructions="Research the goal, fetch sources, cite them.")
              
                5
                agent(
              
                6
                    "Summarize recent advances in solid-state batteries from https://en.wikipedia.org/wiki/Solid-state_battery"
              
                7
                )
              
```

``` terminal__code
                1
                # strands-robots is Python-first — toggle to Python for the sample.
              
                2
                
              
                3
                from strands_harness import create_harness
              
                4
                from strands_robots import Robot
              
                5
                
              
                6
                robot = Robot("so100")
              
                7
                create_harness(tools=[robot])("pick up the red cube")
              
```

``` terminal__code
                1
                from strands_harness import create_harness
              
                2
                from strands_robots import Robot
              
                3
                
              
                4
                # MuJoCo sim by default — no GPU, no hardware.
              
                5
                # Pass mode="real" to drive a physical robot with the same code.
              
                6
                robot = Robot("so100")
              
                7
                
              
                8
                agent = create_harness(tools=[robot])
              
                9
                agent("pick up the red cube")
              
                10
                
              
                11
                # Every robot is a Zenoh peer — coordinate a fleet:
              
                12
                robot.mesh.tell(robot.mesh.peers[0]["peer_id"],
              
                13
                                "hold the tray steady")
              
```

TypeScript

Python

> At Smartsheet, we chose Strands for our next generation of AI capabilities because it provided the perfect balance of enterprise-ready features and development efficiency. Its robust conversation memory and dynamic tool registration systems were crucial for creating a responsive, context-aware intelligent AI assistant. With Strands, we were able to quickly implement a secure and scalable solution, giving us a production-ready foundation to deliver a secure, high-performance, and enterprise-grade AI experience.

> Transform traditional error alerts into intelligent incident responses using Amazon Bedrock, RAG with Amazon OpenSearch, Multi-Agent Orchestration with Strands SDK, and Kiro AI IDE - reducing MTTR by 60% without manual coding.

> Strands’ SDK and great integration with AWS native services streamlined Landchecker’s development of agents. With easier integration of AgentCore Runtime, Bedrock Guardrails, and built-in support for OpenTelemetry, we could focus on what we do best – developing property information tools and data integrations.

> At Swisscom, we need an agentic AI backbone that is both enterprise-ready and future-proof. Strands Agents gives us the best of both worlds: a native fit with our cloud environment, yet fully open source and flexible. That combination allowed us to build proof-of-concepts within just a few weeks and now sets us on the path to scale multi-agent systems with confidence, while keeping our focus on delivering real value to customers and the business.

> The advisor is where things get interesting. We use the Strands Agents SDK to define an agent with a tool, a function the model can call during its reasoning loop.

> We chose Strands because it’s AWS-native, intuitive, and made agent development accessible across our engineering team. Its abstraction layer and built-in multi-agent patterns (like Agent-as-Tool and Swarm) let us focus on remediation logic instead of infrastructure work. We’ve already built multiple agents, and wiring them together has been seamless. On top of that, we layered our [Agentic Remediation™](https://www.zafran.io/resources/agentic-remediation-unlocks-a-new-approach-to-solving-enterprise-vulnerabilities "Agentic Remediation Unlocks New Approach to Solving Enterprise Vulnerabilities") capability to automate vulnerability fixes and configuration validation/fault correction workflows, coordinating cross-agent remediation with precision

> Scaling our global trading platform required reimagining our support capabilities, and Strands Agents was the key to making it happen at enterprise scale. What would traditionally take months of development, Strands allowed us to achieve in just 10 days - delivering a secure, robust, production-ready agentic solution. The results speak for themselves: investigation time dropped on average from 30 minutes to 45 seconds, investigation quality improved by 94%, and we saved \$5M in operational costs. Strands didn’t just accelerate our development - it gave us the confidence to explore other agentic AI use cases across our entire business, including launching our Agentic Security Operations Center

> Adding bidirectional voice to my existing Strands agent was surprisingly straightforward. BidiAgent handles the WebSocket complexity and interruption logic, my @tool functions carried over unchanged, and the same code deploys to AgentCore without modification. Strands made real-time voice feel like a natural extension, not a separate project.

> We see Strands as a great fit to power TeamForm’s next evolution of Agentic AI. Our customers need enterprise-grade security and scalability, which is exactly what Strands delivers. Its seamless integration with AWS and simplicity enables us to focus on innovating our AI capabilities and delivering value to our customers.

> For Jit’s infrastructure drift detection agent, we leverage Strands Agents, an open-source framework developed by AWS for building production-ready AI agents. Strands Agents provides several advantages including simplified development, native AWS integration, and built-in security.

> As someone who builds agents with LangGraph daily at work, Strands was a genuine surprise. The model-driven approach cut my setup from 40 lines to 3 — and for the 80% case, it just works without sacrificing flexibility.

> Strands Agents on Bedrock turns autonomous agents into an enterprise product: governed, observable, and safe by design. Together with Claude models, we analyze live webpages and generate code responsibly - helping customers reduce risk while accelerating delivery. Safety is non-negotiable in offensive security. On Amazon Bedrock, Strands Agents plus Claude let us scale autonomous pen-testing with Bedrock Guardrails - increasing coverage without increasing risk.

> The combination of the Strands Agents SDK and Tavily represents a significant advancement in enterprise-grade research agent development. This integration can help organizations build sophisticated, secure, and scalable AI agents while maintaining the highest standards of security and performance. Learn more in this [blog](https://aws.amazon.com/blogs/machine-learning/build-dynamic-web-research-agents-with-the-strands-agents-sdk-and-tavily/ "Read the official blog post on Build dynamic web research agents with the Strands Agents SDK and Tavily").

> Strands was used to build a growing set of agents that run a company to do actual tasks.

## Community & learning hub

Tutorials, deep-dive articles, and community projects to help you go from your first agent to production, and connect with others building on Strands.

[Start learning ](/docs/learning/how-agents-really-work/)

### What's new on the blog

[Introducing Strands harness: frontier performance with 28% lower token cost](/blog/introducing-strands-harness/)

### Events

- [Oct 3PyBay — Booth + WorkshopMission Bay Conference Center · San Francisco, CA](https://pybay.org/)
- [Oct 7 – 9Open Source Summit Europe — BoothPrague, Czech Republic](https://events.linuxfoundation.org/open-source-summit-europe/)
- [Oct 20 – 21PyTorch Conference NA 2026 — Speaking + BoothSJ Convention Center · San Jose, CA](https://events.linuxfoundation.org/pytorch-conference/)
- [Oct 22 – 23AGNTCon + MCPCon North America — BoothSJ McEnery Convention Center · San Jose, CA](https://events.linuxfoundation.org/agntcon-mcpcon-north-america/)

## Push the boundaries of what agents can do.

[Quick start ](/docs/user-guide/harness/quickstart/)[Migrate ](/docs/user-guide/migrate/choosing-an-agent-foundation/)[Deploy ](/docs/user-guide/sdk/deploy/operating-agents-in-production/)

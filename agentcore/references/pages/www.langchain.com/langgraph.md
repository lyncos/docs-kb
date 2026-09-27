---
title: Balance agent control with agency
description: langgraph
product: Amazon Bedrock AgentCore
section: References / www.langchain.com
source_url: https://www.langchain.com/langgraph
fetched: '2026-09-26'
tags:
- agentcore
- reference
- related
- www-langchain-com
referenced_by:
- gateway-setup-tools-credentials.md
- memory-integrate-lang.md
conversion: pandoc
---

![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69983caa0521ea61da792805_Frame%202147254720.svg)

langgraph

# Balance agent control with agency

Design agents that reliably handle complex tasks with LangGraph, an agent runtime and low-level orchestration framework.

[](https://github.com/langchain-ai/langgraph)

Start building

[](https://docs.langchain.com/oss/python/langgraph/overview)

Read the docs

![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/699ea59bbdd3163a372a1124_langgraph%20ilu.svg)

## Trusted by companies shaping the future of agents

[](/built-with-langgraph)

Use cases in production

![Listen](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699ef03498a1d51a63dad3ba_Listen%20logo.svg)

![Rillet](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a91f25cfdec13d1945372e7_rillet-white.png)

![Vanta](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af60a3595f5918eb55b2f_logo_klarna-1.svg)

![clay](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a056e362caf179dbc8ecc60_clay_logo.png)

![RIPPLING](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af613b1e439fab3cbda6d_logo_klarna-2.svg)

![lyft](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af61c4871f1baed6eb36d_logo_klarna-3.svg)

![Harvey](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af648fc78763596e95934_logo_klarna-4.svg)

![ABRIDGE](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699d8dd819b1b50d87a87a7e_logo_gitlab.svg)

![Expedia](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a972fd99360de4bc5964fdb_expedia-white-1x.png)

![Autodesk](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a70d15276db6b56dc2694b1_autodesk-logo-white.svg)

![Bristol Myers Squibb](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a2a6f957755e2245d259a0e_bms%20logo%20(2).svg)

![workday](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69a03aa35f131c951040c55f_workday.svg)

![CISCO](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af6ae78d3de70d5c3fd10_logo_Rakuten.svg)

![Mercor](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69a03b07847c18efb637c5e1_mercor.svg)

![NU](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699d8e487c686f8fc51fd9b0_nu.svg)

![monday.com](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69a03ace58968e58f476ce24_monday.svg)

![Nvidia](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f07e27d6b85b9690276be2_Nvidia%20logo.svg)

![BRIDGEWATER](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69a03b15e423c55ca7219fec_bridgewater.svg)

![servicenow](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699ecc28698fe26c8324c1b2_servicenow.svg)

![coinbase](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af6a5bce126b2dc318630_logo_rakuten-1.svg)

![Listen](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699ef03498a1d51a63dad3ba_Listen%20logo.svg)

![Rillet](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a91f25cfdec13d1945372e7_rillet-white.png)

![Vanta](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af60a3595f5918eb55b2f_logo_klarna-1.svg)

![clay](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a056e362caf179dbc8ecc60_clay_logo.png)

![RIPPLING](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af613b1e439fab3cbda6d_logo_klarna-2.svg)

![lyft](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af61c4871f1baed6eb36d_logo_klarna-3.svg)

![Harvey](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af648fc78763596e95934_logo_klarna-4.svg)

![ABRIDGE](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699d8dd819b1b50d87a87a7e_logo_gitlab.svg)

![Expedia](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a972fd99360de4bc5964fdb_expedia-white-1x.png)

![Autodesk](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a70d15276db6b56dc2694b1_autodesk-logo-white.svg)

![Listen](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699ef03498a1d51a63dad3ba_Listen%20logo.svg)

![Rillet](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a91f25cfdec13d1945372e7_rillet-white.png)

![Vanta](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af60a3595f5918eb55b2f_logo_klarna-1.svg)

![clay](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a056e362caf179dbc8ecc60_clay_logo.png)

![RIPPLING](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af613b1e439fab3cbda6d_logo_klarna-2.svg)

![lyft](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af61c4871f1baed6eb36d_logo_klarna-3.svg)

![Harvey](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af648fc78763596e95934_logo_klarna-4.svg)

![ABRIDGE](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699d8dd819b1b50d87a87a7e_logo_gitlab.svg)

![Expedia](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a972fd99360de4bc5964fdb_expedia-white-1x.png)

![Autodesk](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a70d15276db6b56dc2694b1_autodesk-logo-white.svg)

![Bristol Myers Squibb](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a2a6f957755e2245d259a0e_bms%20logo%20(2).svg)

![workday](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69a03aa35f131c951040c55f_workday.svg)

![CISCO](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af6ae78d3de70d5c3fd10_logo_Rakuten.svg)

![Mercor](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69a03b07847c18efb637c5e1_mercor.svg)

![NU](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699d8e487c686f8fc51fd9b0_nu.svg)

![monday.com](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69a03ace58968e58f476ce24_monday.svg)

![Nvidia](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f07e27d6b85b9690276be2_Nvidia%20logo.svg)

![BRIDGEWATER](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69a03b15e423c55ca7219fec_bridgewater.svg)

![servicenow](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699ecc28698fe26c8324c1b2_servicenow.svg)

![coinbase](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af6a5bce126b2dc318630_logo_rakuten-1.svg)

![Bristol Myers Squibb](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a2a6f957755e2245d259a0e_bms%20logo%20(2).svg)

![workday](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69a03aa35f131c951040c55f_workday.svg)

![CISCO](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af6ae78d3de70d5c3fd10_logo_Rakuten.svg)

![Mercor](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69a03b07847c18efb637c5e1_mercor.svg)

![NU](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699d8e487c686f8fc51fd9b0_nu.svg)

![monday.com](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69a03ace58968e58f476ce24_monday.svg)

![Nvidia](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f07e27d6b85b9690276be2_Nvidia%20logo.svg)

![BRIDGEWATER](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69a03b15e423c55ca7219fec_bridgewater.svg)

![servicenow](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699ecc28698fe26c8324c1b2_servicenow.svg)

![coinbase](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af6a5bce126b2dc318630_logo_rakuten-1.svg)

![RIPPLING](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af613b1e439fab3cbda6d_logo_klarna-2.svg)

![CISCO](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af6ae78d3de70d5c3fd10_logo_Rakuten.svg)

![workday](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69a03aa35f131c951040c55f_workday.svg)

![Nvidia](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f07e27d6b85b9690276be2_Nvidia%20logo.svg)

![Bristol Myers Squibb](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a2a6f957755e2245d259a0e_bms%20logo%20(2).svg)

![Rakuten](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a7added5c04530d76c38274_rakuten%20logo%201.svg)

![coinbase](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af6a5bce126b2dc318630_logo_rakuten-1.svg)

![servicenow](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699ecc28698fe26c8324c1b2_servicenow.svg)

![RIPPLING](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af613b1e439fab3cbda6d_logo_klarna-2.svg)

![CISCO](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af6ae78d3de70d5c3fd10_logo_Rakuten.svg)

![workday](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69a03aa35f131c951040c55f_workday.svg)

![Nvidia](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69f07e27d6b85b9690276be2_Nvidia%20logo.svg)

![Bristol Myers Squibb](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a2a6f957755e2245d259a0e_bms%20logo%20(2).svg)

![Rakuten](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a7added5c04530d76c38274_rakuten%20logo%201.svg)

![coinbase](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af6a5bce126b2dc318630_logo_rakuten-1.svg)

![servicenow](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699ecc28698fe26c8324c1b2_servicenow.svg)

![elastic](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699ecc1255c685e273b3c33c_logo_Elastic.svg)

![coinbase](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af6a5bce126b2dc318630_logo_rakuten-1.svg)

![servicenow](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699ecc28698fe26c8324c1b2_servicenow.svg)

![monday.com](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69a03ace58968e58f476ce24_monday.svg)

![Uber](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699ecc45b836198626ab7736_monday-1.svg)

![Vanta](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af60a3595f5918eb55b2f_logo_klarna-1.svg)

![exa](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699eefd08dac0949e801045c_exa%20logo.svg)

![cogent](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699eefe6a83e0a4ada06f254_cogent%20logo.svg)

![Serval](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699eefff06ae2a4cdb46a861_Serval%20logo.svg)

![Zip](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699ef01c5311dcfd79d675ea_zip%20logo.svg)

![Listen](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699ef03498a1d51a63dad3ba_Listen%20logo.svg)

![clay](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a056e362caf179dbc8ecc60_clay_logo.png)

![ABRIDGE](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699d8dd819b1b50d87a87a7e_logo_gitlab.svg)

![Mercor](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69a03b07847c18efb637c5e1_mercor.svg)

![Harmonic](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69a187224c05126b9f52d7e4_harmonic.svg)

![RIPPLING](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af613b1e439fab3cbda6d_logo_klarna-2.svg)

![Harvey](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af648fc78763596e95934_logo_klarna-4.svg)

![Vanta](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af60a3595f5918eb55b2f_logo_klarna-1.svg)

![exa](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699eefd08dac0949e801045c_exa%20logo.svg)

![cogent](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699eefe6a83e0a4ada06f254_cogent%20logo.svg)

![Serval](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699eefff06ae2a4cdb46a861_Serval%20logo.svg)

![Zip](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699ef01c5311dcfd79d675ea_zip%20logo.svg)

![Listen](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699ef03498a1d51a63dad3ba_Listen%20logo.svg)

![Vanta](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af60a3595f5918eb55b2f_logo_klarna-1.svg)

![exa](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699eefd08dac0949e801045c_exa%20logo.svg)

![cogent](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699eefe6a83e0a4ada06f254_cogent%20logo.svg)

![Serval](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699eefff06ae2a4cdb46a861_Serval%20logo.svg)

![Zip](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699ef01c5311dcfd79d675ea_zip%20logo.svg)

![Listen](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699ef03498a1d51a63dad3ba_Listen%20logo.svg)

![clay](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a056e362caf179dbc8ecc60_clay_logo.png)

![ABRIDGE](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699d8dd819b1b50d87a87a7e_logo_gitlab.svg)

![Mercor](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69a03b07847c18efb637c5e1_mercor.svg)

![Harmonic](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69a187224c05126b9f52d7e4_harmonic.svg)

![RIPPLING](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af613b1e439fab3cbda6d_logo_klarna-2.svg)

![Harvey](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af648fc78763596e95934_logo_klarna-4.svg)

![clay](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a056e362caf179dbc8ecc60_clay_logo.png)

![ABRIDGE](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/699d8dd819b1b50d87a87a7e_logo_gitlab.svg)

![Mercor](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69a03b07847c18efb637c5e1_mercor.svg)

![Harmonic](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69a187224c05126b9f52d7e4_harmonic.svg)

![RIPPLING](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af613b1e439fab3cbda6d_logo_klarna-2.svg)

![Harvey](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/698af648fc78763596e95934_logo_klarna-4.svg)

### How does LangGraph help?

#### Guide, moderate, and control your agent with human-in-the-loop

Prevent agents from veering off course with easy-to-add moderation and quality controls. Add human-in-the-loop checks to steer and approve agent actions.

[](https://docs.langchain.com/oss/python/langgraph/interrupts)

Add human-in-the-loop

#### Build expressive, customizable agent workflows

LangGraph’s low-level primitives provide the flexibility needed to create fully customizable agents. Design diverse control flows — single, multi-agent, hierarchical — all using one framework.

[](https://docs.langchain.com/oss/python/langgraph/workflows-agents)

See different agent architectures

#### Persist memory for future interactions

LangGraph’s built-in memory stores conversation histories and maintains context over time, enabling rich, personalized interactions across sessions.

[](https://docs.langchain.com/oss/python/langgraph/add-memory)

Learn about agent memory

#### First-class streaming for better UX design

Bridge user expectations and agent capabilities with native token-by-token streaming, showing agent reasoning and actions in real time.

[](https://docs.langchain.com/oss/python/langgraph/streaming)

See how to use streaming

![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69a025b1c2c9ee3fcc4c8189_LangChain_academy.svg)

## Foundation: Introduction to LangGraph

[![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69a0476f2fa2e7c1969d3d8c_461e5d2b58d59f966d20191502c73294_module2.avif)](https://academy.langchain.com/courses/intro-to-langgraph)

Learn the basics of LangGraph in this LangChain Academy Course. You'll learn about how to leverage state, memory, human-in-the-loop, and more for your agents.

[](https://academy.langchain.com/courses/intro-to-langgraph)

Enroll for free

![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/6999965e520db9b0ccefdaa3_langchain%20vis.png)

## Developers trust LangGraph to build reliable agents

Build and ship agents fast with any model provider. Use high-level abstractions or fine-grained control as needed.

![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69984e317f6e150883472ac6_logo_Elastic.svg)

“LangChain is streets ahead with what they've put forward with LangGraph. LangGraph sets the foundation for how we can build and scale AI workloads — from conversational agents, complex task automation, to custom LLM-backed experiences that 'just work'. The next chapter in building complex production-ready features with LLMs is agentic, and with LangGraph and LangSmith, LangChain delivers an out-of-the-box solution to iterate quickly, debug immediately, and scale effortlessly.”

![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/667b26a1b4576291d6a9335b_garrett%20spong%201.webp)

Garrett Spong

Principal SWE

![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69984e3163bda899d4278b90_logo_Elastic-2.svg)

“LangGraph has been instrumental for our AI development. Its robust framework for building stateful, multi-actor applications with LLMs has transformed how we evaluate and optimize the performance of our AI guest-facing solutions. LangGraph enables granular control over the agent's thought process, which has empowered us to make data-driven and deliberate decisions to meet the diverse needs of our guests.”

![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/667b265bed5f5a9d26d6b7d6_andres%20torres%201.webp)

Andres Torres

Sr. Solutions Architect

![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69984e31113abb3a098b24d7_logo_Elastic-1.svg)

“As Ally advances its exploration of Generative AI, our tech labs is excited by LangGraph, the new library from LangChain, which is central to our experiments with multi-actor agentic workflows. We are committed to deepening our partnership with LangChain.”

![](https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/6679e2d31352c6bd56c84280_ally.webp)

Sathish Muthukrishnan

Chief Information, Data and Digital Officer

### LangGraph FAQs

How is LangGraph different from other agent frameworks?

Other agentic frameworks can work for simple, generic tasks but fall short for complex tasks bespoke to a company’s needs. LangGraph provides a more expressive framework to handle companies’ unique tasks without restricting users to a single black-box cognitive architecture.

Does LangGraph impact the performance of my app?

LangGraph will not add any overhead to your code and is specifically designed with streaming workflows in mind.

Is LangGraph open source? Is it free?

Yes. LangGraph is an MIT-licensed open-source library and is free to use.

### See what your agent is really doing

LangSmith, our agent engineering platform, helps developers debug every agent decision, eval changes, and deploy in one click.

[](/langsmith-platform)

Learn more

[](https://smith.langchain.com/)

Play around

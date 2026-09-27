---
title: Built-in strategies
description: 'AgentCore Memory provides built-in strategies to create memories. Each built-in strategy consists of steps to handle memory creation, including the following (different strategies employ different steps): + **Extraction** – Identifies useful insights from short-term memory to pla'
product: Amazon Bedrock AgentCore
section: Developer Guide / built
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/built-in-strategies.html
fetched: '2026-09-26'
tags:
- agentcore
- built
---

# Built-in strategies
<a name="built-in-strategies"></a>

AgentCore Memory provides built-in strategies to create memories. Each built-in strategy consists of steps to handle memory creation, including the following (different strategies employ different steps):
+  **Extraction** – Identifies useful insights from short-term memory to place into long-term memory as memory records.
+  **Consolidation** – Determines whether to write useful information to a new record or an existing record.
+  **Reflection** – Insights are generated across episodes.

Each step is defined by a system prompt, which is a combination of the following:
+  **Instructions** – Guide the LLM’s behavior. Can include step-by-step processing guidelines (how the model should reason and extract or consolidate information).
+  **Output schema** – How the model should present the result.

Each memory strategy provides a structured output format tailored to its purpose. The output is not uniform across strategies, because the type of information being stored and retrieved differs. This maintains that each memory type exposes only the fields most relevant to its strategy. You can find the output formats in the system prompts for each strategy.

You can combine multiple strategies when creating memories.

**Topics**
+ [Semantic memory strategy](semantic-memory-strategy.md)
+ [User preference memory strategy](user-preference-memory-strategy.md)
+ [Summary strategy](summary-strategy.md)
+ [Episodic memory strategy](episodic-memory-strategy.md)
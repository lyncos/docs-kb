---
title: Get started
description: 'We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can '
product: Amazon Bedrock AgentCore
section: References / strandsagents.com
source_url: https://strandsagents.com/latest/documentation/docs
fetched: '2026-09-26'
tags:
- agentcore
- reference
- related
- strandsagents-com
referenced_by:
- code-interpreter-getting-started.md
- gateway-setup-tools-credentials.md
conversion: tavily
---

## Select your cookie preferences

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies.   
  
 If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

We use cookies and similar tools (collectively, "cookies") for the following purposes.

### Essential

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

### Performance

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Allowed

### Functional

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Allowed

### Advertising

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Allowed

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

## Your privacy choices

We and our advertising partners (“we”) may use information we collect from or about you to show you ads on other websites and online services. Under certain laws, this activity is referred to as “cross-context behavioral advertising” or “targeted advertising.”

To opt out of our use of cookies or similar technologies to engage in these activities, select “Opt out of cross-context behavioral ads” and “Save preferences” below. If you clear your browser cookies or visit this site from a different device or browser, you will need to make your selection again. For more information about cookies and how we use them, read our [Cookie Notice](https://aws.amazon.com/legal/cookies/).

To opt out of the use of other identifiers, such as contact information, for these activities, fill out the form [here](https://pulse.aws/application/ZRPLWLL6?p=0).

For more information about how AWS handles your information, read the [AWS Privacy Notice](https://aws.amazon.com/privacy/).

## Unable to save cookie preferences

We will only store essential cookies at this time, because we were unable to save your cookie preferences.  
  
If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

[Skip to content](#_top)

Strands Harness

[PY
Python SDK
↗](https://github.com/strands-agents/harness-sdk/tree/main/strands-py)
[TS
TypeScript SDK
↗](https://github.com/strands-agents/harness-sdk/tree/main/strands-ts)

Strands

[EV
Evals
↗](https://github.com/strands-agents/evals)
[SH
Shell
↗](https://github.com/strands-agents/shell)

Organizations

[strands-agents
↗](https://github.com/strands-agents)
[strands-labs
↗](https://github.com/strands-labs)

# Get started

The Strands Agents SDK empowers developers to quickly build, manage, evaluate and deploy AI-powered agents. These quick start guides get you set up and running a simple agent in less than 20 minutes.

[Python Quickstart](../python/)Create your first Python Strands agent with full feature access!

[TypeScript Quickstart](../typescript/)Create your first TypeScript Strands agent!

---

## A library, not a platform

[Section titled “A library, not a platform”](#a-library-not-a-platform)

Strands runs inside your own process. Creating an agent is constructing an object
in Python or Node.js: there is no hosted control plane, scheduler, or database to
stand up first. Any [model provider](/docs/user-guide/concepts/model-providers/) works. Amazon
Bedrock is the default; switching to Anthropic, OpenAI, Google, or Ollama means
installing that provider’s package and changing one line, so an AWS account is
only required if you keep the default.
Adding an agent to an existing FastAPI, Express, or Next.js app is a dependency
and a few lines of code, not new infrastructure.

## Language support

[Section titled “Language support”](#language-support)

Strands Agents SDK is available in both Python and TypeScript.

### Feature availability

[Section titled “Feature availability”](#feature-availability)

The table below compares feature availability between the Python and TypeScript SDKs.

| Category | Feature | Python | TypeScript |
| --- | --- | --- | --- |
| **Core** | [Agent creation and invocation](/docs/user-guide/concepts/agents/agent-loop/) | ✅ | ✅ |
|  | [Streaming responses](/docs/user-guide/concepts/streaming/) | ✅ | ✅ |
|  | [Structured output](/docs/user-guide/concepts/agents/structured-output/) | ✅ | ✅ |
| **Model providers** | [Amazon Bedrock](/docs/user-guide/concepts/model-providers/amazon-bedrock/) | ✅ | ✅ |
|  | [OpenAI](/docs/user-guide/concepts/model-providers/openai/) | ✅ | ✅ |
|  | [OpenAI Responses API](/docs/user-guide/concepts/model-providers/openai-responses/) | ✅ | ✅ |
|  | [Anthropic](/docs/user-guide/concepts/model-providers/anthropic/) | ✅ | ✅ |
|  | [Google](/docs/user-guide/concepts/model-providers/google/) | ✅ | ✅ |
|  | [Ollama](/docs/user-guide/concepts/model-providers/ollama/) | ✅ | ❌ |
|  | [LiteLLM](/docs/user-guide/concepts/model-providers/litellm/) | ✅ | ❌ |
|  | [Custom providers](/docs/user-guide/concepts/model-providers/custom_model_provider/) | ✅ | ✅ |
|  | [Additional providers](/docs/user-guide/concepts/model-providers/) | 5+ | 1+ |
| **Tools** | [Custom function tools](/docs/user-guide/concepts/tools/custom-tools/) | ✅ | ✅ |
|  | [MCP (Model Context Protocol)](/docs/user-guide/concepts/tools/mcp-tools/) | ✅ | ✅ |
|  | [Built-in tools](/docs/user-guide/concepts/tools/community-tools-package/) | 30+ via community package | 4 built-in |
| **Conversation** | [Null manager](/docs/user-guide/concepts/agents/conversation-management/) | ✅ | ✅ |
|  | [Sliding window manager](/docs/user-guide/concepts/agents/conversation-management/) | ✅ | ✅ |
|  | [Summarizing manager](/docs/user-guide/concepts/agents/conversation-management/) | ✅ | ✅ |
| **Hooks** | [Lifecycle hooks](/docs/user-guide/concepts/agents/hooks/) | ✅ | ✅ |
|  | [Custom hook providers](/docs/user-guide/concepts/agents/hooks/) | ✅ | ✅ |
| **Multi-agent** | [Swarms](/docs/user-guide/concepts/multi-agent/swarm/) | ✅ | ✅ |
|  | [Graphs](/docs/user-guide/concepts/multi-agent/graph/) | ✅ | ✅ |
|  | [Workflows](/docs/user-guide/concepts/multi-agent/workflow/) | ✅ | ✅ |
|  | [Agents as tools](/docs/user-guide/concepts/multi-agent/agents-as-tools/) | ✅ | ✅ |
|  | [Agent-to-Agent (A2A)](/docs/user-guide/concepts/multi-agent/agent-to-agent/) | ✅ | ✅ |
| **Session management** | [File, S3, repository managers](/docs/user-guide/concepts/agents/session-management/) | ✅ | ✅ |
| **Observability** | [OpenTelemetry integration](/docs/user-guide/observability-evaluation/observability/) | ✅ | ✅ |
| **Steering** | [Agent steering](/docs/user-guide/concepts/plugins/steering/) | ✅ | ✅ |
| **Experimental** | [Bidirectional streaming](/docs/user-guide/concepts/bidirectional-streaming/quickstart/) | ✅ | ❌ |

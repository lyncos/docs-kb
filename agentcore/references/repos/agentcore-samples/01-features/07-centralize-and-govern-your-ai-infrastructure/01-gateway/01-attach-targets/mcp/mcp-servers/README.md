---
title: Integrate your MCP Server with AgentCore gateway
description: AgentCore gateway supports all three MCP primitives, tools, prompts, and resources. Tool definitions in MCP include an optional `outputSchema` for defining expected output structure and annotations describing behavioral properties such as whether a tool is read-only or destructiv
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/01-features/07-centralize-and-govern-your-ai-infrastructure/01-gateway/01-attach-targets/mcp/mcp-servers/README.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

# Integrate your MCP Server with AgentCore gateway

![architecture](./images/arcitecture.png)

AgentCore gateway supports all three MCP primitives, tools, prompts, and resources. Tool definitions in MCP include an optional `outputSchema` for defining expected output structure and annotations describing behavioral properties such as whether a tool is read-only or destructive, alongside the standard `name`, `icons`, `annotations`, `description`, and `inputSchema`. The gateway also supports prompts, resources, and resource templates through their full set of MCP methods: `tools/list`, `tools/call`, `prompts/list`, `prompts/get`, `resources/list`, `resources/read`, and `resources/templates/list`. The following architecture diagram shows how AgentCore gateway facilitates list and invoke calls.
The gateway is a centralized management framework for tool/prompt/resource discovery, security, and routing — letting enterprises scale from dozens to hundreds of MCP servers behind a single endpoint without fragmenting their security and operational standards.

## MCP primitives forwarded by the gateway

For each MCP server target, the gateway forwards all three MCP primitive types:

- **Tools**: `tools/list` (cached or live, depending on the target's `listingMode`) and `tools/call` (always live). 
- **Prompts**: `prompts/list` (cached or live) and `prompts/get` (always live). Prompt names are auto-prefixed `{targetName}___{promptName}` (triple underscore — same convention as tools).
- **Resources**: `resources/list`, `resources/templates/list` (cached or live) and `resources/read` (always live). Resource URIs are returned **as-is** (no prefix); cross-target URI collisions are resolved by `resourcePriority` (lower wins; default 1000).

>**Security warning for resources** (verbatim from the AWS docs): resource URIs are not validated or sanitized by the gateway. A malicious or compromised MCP server target could return URIs pointing to internal endpoints (SSRF) or local filesystem paths (e.g. `file:///etc/passwd`). Validate and sanitize URIs from untrusted targets before following them.

## Samples

| Sample | Description |
| :--- | :--- |
| [01-configure-auth](01-configure-auth/) | Inbound and outbound authentication patterns (client credentials, authorization code flow) |
| [02-mcp-target-synchronization](02-mcp-target-synchronization/) | Explicit sync, implicit sync, and dynamic listing modes |
| [03-streaming](03-streaming/) | Server-Sent Events streaming with progress, logging, and keep-alive |
| [04-session-management](04-session-management/) | Stateful sessions with per-session state and session isolation |
| [05-elicitation](05-elicitation/) | Form-mode and URL-mode elicitation, sampling |

### Three ways to keep the catalog in sync

Tool, prompt, and resource definitions on an MCP server change over time. AgentCore gateway has three mechanisms for keeping its catalog in sync with what each MCP server target actually exposes:

1. **Explicit synchronization** — call `SynchronizeGatewayTargets` on demand after the upstream MCP server changes. 
2. **Implicit synchronization** — `CreateGatewayTarget` and `UpdateGatewayTarget` always re-read the upstream server's catalog as part of the operation. 
3. **Dynamic listing** (`listingMode='DYNAMIC'`) — gateway forwards every list request (`tools/list`, `prompts/list`, `resources/list`, `resources/templates/list`) live to the MCP server, so no synchronization is ever required.

(1) and (2) are **control-plane operations on `listingMode='DEFAULT'` targets** — they populate the gateway's catalog _cache_ that DEFAULT-mode list calls will be answered from. `CreateGatewayTarget` is the very first cache fill (implicit at create time); `UpdateGatewayTarget` refills it as a side effect of every update; `SynchronizeGatewayTargets` is the on-demand refill in between. DYNAMIC-mode targets skip this cache entirely — the gateway proxies each list call straight through to the server, so no `Synchronize`/`Update` call ever needs to run on them.

![dynamic](./images/dynamic.png)

> **DYNAMIC compatibility caveats:** `listingMode='DYNAMIC'` is rejected on gateways with `searchType='SEMANTIC'` and is incompatible with outbound three-legged OAuth (3LO). Notebook 02 stands up its own gateway with `searchType='NONE'` for the dynamic-listing demo for this reason.

#### Explicit sync (control plane → cache fill)

![Explicit sync](images/mcp-server-target-explicit-sync.png)

#### Implicit sync (during Create/UpdateGatewayTarget)

![Implicit sync](images/mcp-server-target-implicit-sync.png)

---
title: Schema Module
description: The `schema` module contains the high level schemas which serve as abstractions enabling a streamlined L3 implementation to model AgentCore resources.
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-cli
source_url: https://github.com/aws/agentcore-cli/blob/805f342/src/schema/AGENTS.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-cli
- reference
---

# Schema Module

The `schema` module contains the high level schemas which serve as abstractions enabling a streamlined L3 implementation
to model AgentCore resources.

This module only houses schemas and zod validation logic. Schemas are modeled separately with types and interfaces for
readability and clean imports. Zod validators take a dependency on the top level types and serve only validation.

## Function

**Schemas**: The core interface for both CLI and the input props to the L3 CDK constructs. These schemas allow
high-level definitions for agent use case and behavior to be translated into AgentCore infrastructure.

### Tags

The tags primitive schema is defined at `src/schema/schemas/primitives/tags.ts` and supports project-level and
resource-level tagging with AWS tagging constraints.

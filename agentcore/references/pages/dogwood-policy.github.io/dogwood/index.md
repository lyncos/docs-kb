---
title: '[The Dogwood Guide](#the-dogwood-guide)'
description: Complete documentation for the Dogwood policy language — its syntax, its temporal expressions and information providers, its schemas, and the Rust API for evaluating policies.
product: Amazon Bedrock AgentCore
section: References / dogwood-policy.github.io
source_url: https://dogwood-policy.github.io/dogwood/index.html
fetched: '2026-09-26'
tags:
- agentcore
- dogwood-policy-github-io
- reference
- related
referenced_by:
- what-is-bedrock-agentcore.md
conversion: pandoc
---

# [The Dogwood Guide](#the-dogwood-guide)

Complete documentation for the Dogwood policy language — its syntax, its temporal expressions and information providers, its schemas, and the Rust API for evaluating policies.

The guide is organized so the **core language** comes first, read through the lens of a fixed setup: the event schema, the information providers, and the macro library are all taken as *given*. The **Advanced topics** section then covers how each of those fixed inputs is built.

## [A. Introduction to the language](#a-introduction-to-the-language)

The core language, assuming the event schema, providers, and macros are given.

- **[Introduction](./guide/00-introduction.html)** — what Dogwood is, the problem it solves, and the concepts you need. Read this first if you are new.
- **[Getting started](./guide/01-getting-started.html)** — your first schema, policy, and authorization, end to end, with runnable code.
- **[The policy language](./guide/02-policy-language.html)** — the core (Cedar-derived) syntax: the **action schema** (entity/action declarations and the `context.input` / `context.output` convention), `permit`/`forbid`, the `(principal, action, resource)` scope, `when`/`unless` conditions, and the full expression language.
- **[Temporal expressions](./guide/04-temporal-expressions.html)** — the `when temporal { … }` sublanguage: reasoning about event history with `formerly`, `previous`, `since`, windows, `exists`, `tp`, and the `count` / `sum` aggregations.
- **[Information providers](./guide/05-information-providers.html)** — consulting values computed on demand: calling a provider as a plain Cedar call inside an ordinary `when { … }` clause, and how its output composes with a condition.
- **[Calling macros](./guide/09-calling-macros.html)** — invoking `def cedar` and `def temporal` macros: where a call may appear and what shape its arguments take.

## [B. Advanced topics](#b-advanced-topics)

Deep dives on the three fixed inputs the core language takes as given, plus MCP schema generation.

- **[The event schema](./guide/03-event-schema.html)** — the event-schema DSL (`.dwschema`): the four selectors, spreads, named fields, nested records, pins, decision kinds, and the default request/response schema.
- **[The provider schema](./guide/10-provider-schema.html)** — declaring providers: the `providers.json` format, the Rhai implementation contract (sandbox, host functions, decimal, the `net` feature), output methods, no-implementation providers, and the `guardrails { … }` sugar.
- **[Macros](./guide/06-macros.html)** — defining macros: `def cedar` / `def temporal`, the two parameter sigils, hygiene, every rejection rule, and the macro library.
- **[Generating the action schema from an MCP manifest](./guide/11-mcp-schema-generation.html)** — a Dogwood action schema *is* an MCP tool manifest; the manifest format, the JSON→Cedar type mapping, and the Drupe template.

## [C. Running Dogwood](#c-running-dogwood)

- **[The command line](./guide/12-cli.html)** — the `dogwood` CLI: `validate`, `replay`, `lower`, `check-parse`, and the `schema` subcommands, driven over plain files. The quickest way to check a policy or watch a temporal policy decide across a trace, with no Rust.
- **[The API and workflow](./guide/07-api-and-workflow.html)** — the Rust API reference and end-to-end workflow: `ServiceSchema`/`PolicySchema` → `LoweredPolicySet` → `Validator` → `Authorizer` → `Event` → `Response`.

## [D. Reference](#d-reference)

- **[Formal specification](./guide/08-formal-specification.html)** — the precise reference: the grammars in BNF, the abstract syntax, and the lowering / validation / authorization rules, each cross-referenced to its source of record.

## [Runnable examples](#runnable-examples)

Every policy-level example in this guide is a complete, runnable **bundle** under this crate’s [`examples/`](./examples/index.html) directory — a `policy.dw`, its `schema.cedarschema`, and (for history-dependent examples) a `trace.log` plus the expected verdict stream, along with any `providers.json` / `macros.dw` / event schema the example needs. A test harness checks every bundle on each build (validating each policy, and replaying traces against the expected verdict stream), so a guide example that stops parsing, validating, or replaying as written is a build failure. To run one yourself, see [The command line](./guide/12-cli.html).

To *embed* the engine rather than drive it over files — building events programmatically and feeding them one at a time to a stateful `Authorizer` — use the Rust API, walked through end to end in [The API and workflow](./guide/07-api-and-workflow.html).

## [Reading order](#reading-order)

If you read straight through, this order builds naturally:

1.  [Introduction](./guide/00-introduction.html)
2.  [Getting started](./guide/01-getting-started.html)
3.  [The policy language](./guide/02-policy-language.html)
4.  [Temporal expressions](./guide/04-temporal-expressions.html)
5.  [Information providers](./guide/05-information-providers.html)
6.  [Calling macros](./guide/09-calling-macros.html)

Then reach into the Advanced topics as you need them: [the event schema](./guide/03-event-schema.html), [the provider schema](./guide/10-provider-schema.html), [macros](./guide/06-macros.html), and [MCP schema generation](./guide/11-mcp-schema-generation.html). Integrate from Rust with [The API and workflow](./guide/07-api-and-workflow.html), and consult the [Formal specification](./guide/08-formal-specification.html) as the reference.

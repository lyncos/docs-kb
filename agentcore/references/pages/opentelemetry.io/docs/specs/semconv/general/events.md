---
title: Semantic conventions for events
description: This document describes the semantic conventions for Events that are represented in the data model by an `EventRecord` (a `LogRecord` with an event name).
product: Amazon Bedrock AgentCore
section: References / opentelemetry.io
source_url: https://opentelemetry.io/docs/specs/semconv/general/events
fetched: '2026-09-26'
tags:
- agentcore
- opentelemetry-io
- reference
- related
referenced_by:
- supported-frameworks-telemetry.md
conversion: pandoc
---

# Semantic conventions for events

**Status**: [Development](/docs/specs/otel/document-status/)

This document describes the semantic conventions for Events that are represented in the data model by an [`EventRecord`](https://github.com/open-telemetry/opentelemetry-specification/blob/v1.59.0/specification/logs/data-model.md#log-and-event-record-definition) (a `LogRecord` with an event name).

- [When to define events](#when-to-define-events)
- [Event name](#event-name)
- [Timestamps](#timestamps)
- [Severity](#severity)
- [Attributes](#attributes)
- [Body](#body)

## When to define events[](#when-to-define-events)

Events describe named occurrences at a meaningful point in time.

When to define events:

- The occurrence does not require a new trace context or child operations.
- The occurrence represents a checkpoint, state change, point-in-time occurrence, or outcome in a longer operation or asynchronous flow.

For example, define events for user interactions, state transitions, feature flag evaluations, lifecycle moments such as service startup, configuration reload, or shutdown completion, and exceptions that occur while an operation is being executed.

When not to define events:

- For operations that have a duration and meaningful boundary - use spans instead.
- For properties that describe a whole operation and do not need their own timestamp - use span attributes instead.
- For unstructured diagnostic messages that are not intended to be queried as named events - emit regular log records instead. These records are not modeled as events, but can still follow [Semantic conventions for logs](/docs/specs/semconv/general/logs/).

Events often complement span definitions. Events can be emitted inside or outside an active trace context.

Use an event instead of a span attribute when the data describes a distinct occurrence within the operation, can happen zero or more times for the same span, or needs its own timestamp, severity, or occurrence-specific attributes. Use a span attribute when the data describes the operation as a whole, especially when it is useful for sampling or is known when the span starts.

An event definition should describe when the event is recorded and what domain-specific occurrence it represents in the instrumented component, the [event name](#event-name), which [timestamp](#timestamps) to use, the default [severity](#severity), and the applicable [attributes](#attributes).

## Event name[](#event-name)

Semantic conventions MUST document the event name.

An event MUST have an [event name](https://github.com/open-telemetry/opentelemetry-specification/blob/v1.59.0/specification/logs/data-model.md#field-eventname) that uniquely identifies the event structure.

Event names uniquely identify an event structure. When users query for a specific event name, they should get events that comply with the corresponding semantic convention.

- Event names SHOULD follow the [Naming guidelines](/docs/specs/semconv/general/naming/).
- Event names MUST NOT include dynamic values. Use attributes for identifiers, names, or other values that vary per occurrence.
- Use a fully qualified, domain-specific name when the event is tied to a specific operation or system. For example, `http.client.request.exception` represents exceptions during HTTP client requests.
- Use a shared name only when the same definition applies to all occurrences recorded with that name.
- When modeling events from an existing system as OpenTelemetry Events, it’s common for the system to lack a single name field or require multiple fields to identify the event. In such cases, semantic conventions can use a combination of fields to create a low-cardinality event name.

## Timestamps[](#timestamps)

Events MUST have [Timestamp](https://github.com/open-telemetry/opentelemetry-specification/blob/v1.59.0/specification/logs/data-model.md#field-timestamp) set to the time when the event occurred.

Semantic conventions MUST NOT define a value for [ObservedTimestamp](https://github.com/open-telemetry/opentelemetry-specification/blob/v1.59.0/specification/logs/data-model.md#field-observedtimestamp); SDKs, collectors, or other components should populate it to reflect when the event was observed/received.

## Severity[](#severity)

Semantic conventions SHOULD specify a default [severity number](https://github.com/open-telemetry/opentelemetry-specification/blob/v1.59.0/specification/logs/data-model.md#field-severitynumber).

Define the severity number based on the expected impact of the occurrence. If the same event can have different severity depending on context, document the conditions for setting each severity.

For exception events, follow the severity guidance in [Semantic conventions for exceptions in logs](/docs/specs/semconv/exceptions/exceptions-logs/#severity).

Semantic conventions MUST NOT define a [severity text](https://github.com/open-telemetry/opentelemetry-specification/blob/v1.59.0/specification/logs/data-model.md#field-severitytext).

## Attributes[](#attributes)

Semantic conventions MUST document the event attributes to represent structured event details and context:

- Reuse existing attributes when possible, especially attributes that are used on related spans, metrics, resources, or other events.
- Include attributes that users are likely to filter, group, aggregate, or correlate on.
- When the event is normally associated with a span, avoid copying every span attribute by default. Reference span-level attributes on the event only when they are needed to understand, route, or retain the event without the span.
- Prefer flat attributes when the value can be represented clearly without structure. Use complex attributes only when the structure is part of the event semantics and a flat representation would be awkward or lossy.
- Include `error.type` when defining an event that represents a failure or an operation outcome that can be either success or failure.
- Specify [requirement level](/docs/specs/semconv/general/attribute-requirement-level/) and tailor the brief and note to the event.
- Document attributes that may contain sensitive information, be expensive to collect, or be especially large.

## Body[](#body)

Semantic conventions MUST NOT define a value for [body](https://github.com/open-telemetry/opentelemetry-specification/blob/v1.59.0/specification/logs/data-model.md#field-body) except to represent a string display message of the event.

## Feedback

Was this page helpful?

Yes

No

Thank you. Your feedback is appreciated!

Please let us know [how we can improve this page](https://github.com/open-telemetry/opentelemetry.io/issues/new?template=PAGE_FEEDBACK.yml&title=%5BPage+feedback%5D%3A+ADD+A+SUMMARY+OF+YOUR+FEEDBACK+HERE). Your feedback is appreciated!

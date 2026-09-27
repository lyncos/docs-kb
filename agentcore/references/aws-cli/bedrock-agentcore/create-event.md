---
title: aws bedrock-agentcore create-event
description: \ [aws . bedrock-agentcore \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore/create-event.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore](index.html#cli-aws-bedrock-agentcore) \]

# create-event

## Description

Creates an event in an AgentCore Memory resource. Events represent interactions or activities that occur within a session and are associated with specific actors.

To use this operation, you must have the `bedrock-agentcore:CreateEvent` permission.

This operation is subject to request rate limiting.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-2024-02-28/CreateEvent)

`create-event` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

      create-event
    --memory-id <value>
    --actor-id <value>
    [--session-id <value>]
    --event-timestamp <value>
    --payload <value>
    [--branch <value>]
    [--client-token <value>]
    [--metadata <value>]
    [--extraction-mode <value>]
    [--extraction-config <value>]
    [--cli-input-json | --cli-input-yaml]
    [--generate-cli-skeleton <value>]
    [--debug]
    [--endpoint-url <value>]
    [--no-verify-ssl]
    [--no-paginate]
    [--output <value>]
    [--query <value>]
    [--profile <value>]
    [--region <value>]
    [--version <value>]
    [--color <value>]
    [--no-sign-request]
    [--ca-bundle <value>]
    [--cli-read-timeout <value>]
    [--cli-connect-timeout <value>]
    [--cli-binary-format <value>]
    [--no-cli-pager]
    [--cli-auto-prompt]
    [--no-cli-auto-prompt]
    [--cli-error-format <value>]

## Options

`--memory-id` (string) \[required\]

> The identifier of the AgentCore Memory resource in which to create the event.
>
> Constraints:
>
> - min: `12`
> - pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`

`--actor-id` (string) \[required\]

> The identifier of the actor associated with this event. An actor represents an entity that participates in sessions and generates events.
>
> Constraints:
>
> - min: `1`
> - max: `255`
> - pattern: `[a-zA-Z0-9][a-zA-Z0-9-_/]*(?::[a-zA-Z0-9-_/]+)*[a-zA-Z0-9-_/]*`

`--session-id` (string)

> The identifier of the session in which this event occurs. A session represents a sequence of related events.
>
> Constraints:
>
> - min: `1`
> - max: `100`
> - pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`

`--event-timestamp` (timestamp) \[required\]

> The timestamp when the event occurred. If not specified, the current time is used.

`--payload` (list) \[required\]

> The content payload of the event. This can include conversational data, JSON data, or binary content.
>
> Constraints:
>
> - min: `0`
> - max: `100`
>
> (tagged union structure)
>
> > Contains the payload content for an event.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `conversational`, `blob`, `json`.
> >
> > conversational -\> (structure)
> >
> > > The conversational content of the payload.
> > >
> > > content -\> (tagged union structure) \[required\]
> > >
> > > > The content of the conversation message.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `text`.
> > > >
> > > > text -\> (string)
> > > >
> > > > > The text content of the memory item.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `100000`
> > >
> > > role -\> (string) \[required\]
> > >
> > > > The role of the participant in the conversation (for example, “user” or “assistant”).
> > > >
> > > > Possible values:
> > > >
> > > > - `ASSISTANT`
> > > > - `USER`
> > > > - `TOOL`
> > > > - `OTHER`
> >
> > blob -\> (document)
> >
> > > The binary content of the payload.
> >
> > json -\> (structure)
> >
> > > The JSON content of the payload. Use this type to store non-conversational, JSON-formatted data, such as behavioral events, activity logs, or system events.
> > >
> > > content -\> (document) \[required\]
> > >
> > > > The JSON content of the payload. Accepts any JSON value, including objects, arrays, strings, numbers, booleans, and null. The maximum size is 100 KB.

Shorthand Syntax:

    conversational={content={text=string},role=string},json={} ...

JSON Syntax:

    [
      {
        "conversational": {
          "content": {
            "text": "string"
          },
          "role": "ASSISTANT"|"USER"|"TOOL"|"OTHER"
        },
        "blob": {...},
        "json": {
          "content": {...}
        }
      }
      ...
    ]

`--branch` (structure)

> The branch information for this event. Branches allow for organizing events into different conversation threads or paths.
>
> rootEventId -\> (string)
>
> > The identifier of the root event for this branch.
> >
> > Constraints:
> >
> > - pattern: `[0-9]+#[a-fA-F0-9]+`
>
> name -\> (string) \[required\]
>
> > The name of the branch.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `100`
> > - pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`

Shorthand Syntax:

    rootEventId=string,name=string

JSON Syntax:

    {
      "rootEventId": "string",
      "name": "string"
    }

`--client-token` (string)

> A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, AgentCore ignores the request, but does not return an error.

`--metadata` (map)

> The key-value metadata to attach to the event.
>
> Constraints:
>
> - min: `0`
> - max: `15`
>
> key -\> (string)
>
> > Constraints:
> >
> > - min: `1`
> > - max: `128`
> > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
>
> value -\> (tagged union structure)
>
> > Value associated with the `eventMetadata` key.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`.
> >
> > stringValue -\> (string)
> >
> > > Value associated with the `eventMetadata` key.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `256`
> > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`

Shorthand Syntax:

    KeyName1={stringValue=string},KeyName2={stringValue=string}

JSON Syntax:

    {"string": {
          "stringValue": "string"
        }
      ...}

`--extraction-mode` (string)

> Controls long-term memory extraction for this event. When set to `SKIP` , the event is stored in short-term memory but is excluded from long-term memory extraction. If not specified, the event is processed for extraction as usual.
>
> Possible values:
>
> - `SKIP`

`--extraction-config` (structure)

> The extraction configuration for long-term memory records. Use this parameter to specify namespace variable keys and their values for namespace substitution during extraction.
>
> namespaceVariables -\> (map)
>
> > A map of `namespaceKeys` to their values. The service substitutes these values into `namespaceTemplates` during long-term memory extraction to control namespace hierarchy.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `5`
> >
> > key -\> (string)
> >
> > > The name of the namespace variable key. The name cannot be a built-in variable name (`actorId` , `sessionId` , or `memoryStrategyId` ).
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `32`
> > > - pattern: `(?!memoryStrategyId$|actorId$|sessionId$)[a-z][a-z0-9]*`
> >
> > value -\> (string)
> >
> > > The value of a namespace variable key.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `64`
> > > - pattern: `[a-z0-9][a-z0-9-_]*`

Shorthand Syntax:

    namespaceVariables={KeyName1=string,KeyName2=string}

JSON Syntax:

    {
      "namespaceVariables": {"string": "string"
        ...}
    }

`--cli-input-json` \| `--cli-input-yaml` (string) Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--generate-cli-skeleton` (string) Prints a JSON skeleton to standard output without sending an API request. If provided with no value or the value `input`, prints a sample input JSON that can be used as an argument for `--cli-input-json`. Similarly, if provided `yaml-input` it will print a sample input YAML that can be used with `--cli-input-yaml`. If provided with the value `output`, it validates the command inputs and returns a sample output JSON for that command. The generated JSON skeleton is not stable between versions of the AWS CLI and there are no backwards compatibility guarantees in the JSON skeleton generated.

## Global Options

`--debug` (boolean)

Turn on debug logging.

`--endpoint-url` (string)

Override command’s default URL with the given URL.

`--no-verify-ssl` (boolean)

By default, the AWS CLI uses SSL when communicating with AWS services. For each SSL connection, the AWS CLI will verify SSL certificates. This option overrides the default behavior of verifying SSL certificates.

`--no-paginate` (boolean)

Disable automatic pagination. If automatic pagination is disabled, the AWS CLI will only make one call, for the first page of results.

`--output` (string)

The formatting style for command output.

- json
- text
- table
- yaml
- yaml-stream
- off

`--query` (string)

A JMESPath query to use in filtering the response data.

`--profile` (string)

Use a specific profile from your credential file.

`--region` (string)

The region to use. Overrides config/env settings.

`--version` (string)

Display the version of this tool.

`--color` (string)

Turn on/off color output.

- on
- off
- auto

`--no-sign-request` (boolean)

Do not sign requests. Credentials will not be loaded if this argument is provided.

`--ca-bundle` (string)

The CA certificate bundle to use when verifying SSL certificates. Overrides config/env settings.

`--cli-read-timeout` (int)

The maximum socket read time in seconds. If the value is set to 0, the socket read will be blocking and not timeout. The default value is 60 seconds.

`--cli-connect-timeout` (int)

The maximum socket connect time in seconds. If the value is set to 0, the socket connect will be blocking and not timeout. The default value is 60 seconds.

`--cli-binary-format` (string)

The formatting style to be used for binary blobs. The default format is base64. The base64 format expects binary blobs to be provided as a base64 encoded string. The raw-in-base64-out format preserves compatibility with AWS CLI V1 behavior and binary values must be passed literally. When providing contents from a file that map to a binary blob `fileb://` will always be treated as binary and use the file contents directly regardless of the `cli-binary-format` setting. When using `file://` the file contents will need to properly formatted for the configured `cli-binary-format`.

- base64
- raw-in-base64-out

`--no-cli-pager` (boolean)

Disable cli pager for output.

`--cli-auto-prompt` (boolean)

Automatically prompt for CLI input parameters.

`--no-cli-auto-prompt` (boolean)

Disable automatically prompt for CLI input parameters.

`--cli-error-format` (string)

The formatting style for error output. By default, errors are displayed in enhanced format.

- legacy
- json
- yaml
- text
- table
- enhanced

## Output

event -\> (structure)

> The event that was created.
>
> memoryId -\> (string) \[required\]
>
> > The identifier of the AgentCore Memory resource containing the event.
> >
> > Constraints:
> >
> > - min: `12`
> > - pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
>
> actorId -\> (string) \[required\]
>
> > The identifier of the actor associated with the event.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `255`
> > - pattern: `[a-zA-Z0-9][a-zA-Z0-9-_/]*(?::[a-zA-Z0-9-_/]+)*[a-zA-Z0-9-_/]*`
>
> sessionId -\> (string) \[required\]
>
> > The identifier of the session containing the event.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `100`
> > - pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
>
> eventId -\> (string) \[required\]
>
> > The unique identifier of the event.
> >
> > Constraints:
> >
> > - pattern: `[0-9]+#[a-fA-F0-9]+`
>
> eventTimestamp -\> (timestamp) \[required\]
>
> > The timestamp when the event occurred.
>
> payload -\> (list) \[required\]
>
> > The content payload of the event.
> >
> > Constraints:
> >
> > - min: `0`
> > - max: `100`
> >
> > (tagged union structure)
> >
> > > Contains the payload content for an event.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `conversational`, `blob`, `json`.
> > >
> > > conversational -\> (structure)
> > >
> > > > The conversational content of the payload.
> > > >
> > > > content -\> (tagged union structure) \[required\]
> > > >
> > > > > The content of the conversation message.
> > > > >
> > > > > ### Note
> > > > >
> > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `text`.
> > > > >
> > > > > text -\> (string)
> > > > >
> > > > > > The text content of the memory item.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `100000`
> > > >
> > > > role -\> (string) \[required\]
> > > >
> > > > > The role of the participant in the conversation (for example, “user” or “assistant”).
> > > > >
> > > > > Possible values:
> > > > >
> > > > > - `ASSISTANT`
> > > > > - `USER`
> > > > > - `TOOL`
> > > > > - `OTHER`
> > >
> > > blob -\> (document)
> > >
> > > > The binary content of the payload.
> > >
> > > json -\> (structure)
> > >
> > > > The JSON content of the payload. Use this type to store non-conversational, JSON-formatted data, such as behavioral events, activity logs, or system events.
> > > >
> > > > content -\> (document) \[required\]
> > > >
> > > > > The JSON content of the payload. Accepts any JSON value, including objects, arrays, strings, numbers, booleans, and null. The maximum size is 100 KB.
>
> branch -\> (structure)
>
> > The branch information for the event.
> >
> > rootEventId -\> (string)
> >
> > > The identifier of the root event for this branch.
> > >
> > > Constraints:
> > >
> > > - pattern: `[0-9]+#[a-fA-F0-9]+`
> >
> > name -\> (string) \[required\]
> >
> > > The name of the branch.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `100`
> > > - pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
>
> metadata -\> (map)
>
> > Metadata associated with an event.
> >
> > Constraints:
> >
> > - min: `0`
> > - max: `15`
> >
> > key -\> (string)
> >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `128`
> > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> >
> > value -\> (tagged union structure)
> >
> > > Value associated with the `eventMetadata` key.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`.
> > >
> > > stringValue -\> (string)
> > >
> > > > Value associated with the `eventMetadata` key.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0`
> > > > - max: `256`
> > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`

- [← create-ab-test](create-ab-test.html "previous chapter (use the left arrow)") /
- [create-payment-instrument →](create-payment-instrument.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](create-payment-instrument.html "create-payment-instrument") \|
- [previous](create-ab-test.html "create-ab-test") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore](index.html) »
- [create-event]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

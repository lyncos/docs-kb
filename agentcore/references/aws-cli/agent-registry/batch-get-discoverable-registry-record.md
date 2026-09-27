---
title: aws agent-registry batch-get-discoverable-registry-record
description: \ [aws . agent-registry \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / agent-registry
source_url: https://docs.aws.amazon.com/cli/latest/reference/agent-registry/batch-get-discoverable-registry-record.html
fetched: '2026-09-26'
tags:
- agent-registry
- agentcore
- aws-cli
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [agent-registry](index.html#cli-aws-agent-registry) \]

# batch-get-discoverable-registry-record

## Description

Retrieves multiple discoverable registry records by ID from a single registry. Records that cannot be retrieved are reported individually in the `errors` list rather than failing the entire request.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/agent-registry-2025-12-01/BatchGetDiscoverableRegistryRecord)

## Synopsis

      batch-get-discoverable-registry-record
    --entries <value>
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

`--entries` (list) \[required\]

> The registry-scoped groups of record IDs to retrieve. Currently, you can specify exactly one entry.
>
> Constraints:
>
> - min: `1`
> - max: `1`
>
> (structure)
>
> > Binds one registry to the record IDs requested from it.
> >
> > registryId -\> (string) \[required\]
> >
> > > The identifier of the registry to retrieve the records from. You can provide either the full Amazon Resource Name (ARN) or the registry ID.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `2048`
> > > - pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`
> >
> > recordIds -\> (list) \[required\]
> >
> > > The record IDs to retrieve from the registry. You can specify 1 through 100 record IDs.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `100`
> > >
> > > (string)
> > >
> > > > Record identifier that accepts either ARN or ID format
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `2048`
> > > > - pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/)?[a-zA-Z0-9]{12}`

Shorthand Syntax:

    registryId=string,recordIds=string,string ...

JSON Syntax:

    [
      {
        "registryId": "string",
        "recordIds": ["string", ...]
      }
      ...
    ]

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

registryRecords -\> (list)

> The records that were successfully retrieved. Each record correlates to the request by its `recordId` .
>
> (structure)
>
> > Summary information about a registry record, including its descriptors.
> >
> > registryArn -\> (string) \[required\]
> >
> > > The Amazon Resource Name (ARN) of the parent registry that owns the record.
> > >
> > > Constraints:
> > >
> > > - min: `46`
> > > - max: `2048`
> > > - pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}`
> >
> > recordArn -\> (string) \[required\]
> >
> > > The Amazon Resource Name (ARN) of the registry record.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `2048`
> > > - pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}`
> >
> > recordId -\> (string) \[required\]
> >
> > > The unique identifier of the registry record.
> > >
> > > Constraints:
> > >
> > > - min: `12`
> > > - max: `12`
> > > - pattern: `[a-zA-Z0-9]{12}`
> >
> > name -\> (string) \[required\]
> >
> > > The name of the registry record. Names are unique within a registry.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `255`
> > > - pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`
> >
> > description -\> (string)
> >
> > > A human-readable description of the registry record. Use this field to explain the record’s purpose or content to consumers discovering it in the registry.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `4096`
> >
> > displayName -\> (string)
> >
> > > The human-readable display name of the registry record.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `255`
> >
> > recordType -\> (string) \[required\]
> >
> > > The type of the registry record. `MCP` is a Model Context Protocol server record, `AGENT` is an Agent-to-Agent (A2A) agent card record, `SKILL` is an agent skills definition record, and `CUSTOM` is a record with a custom descriptor.
> > >
> > > Possible values:
> > >
> > > - `MCP`
> > > - `AGENT`
> > > - `CUSTOM`
> > > - `SKILL`
> > > - `GATEWAY`
> >
> > descriptors -\> (structure) \[required\]
> >
> > > The protocol-specific descriptors that describe how to connect to and use the record.
> > >
> > > mcpServer -\> (structure)
> > >
> > > > The MCP server descriptor, populated when the record type is MCP.
> > > >
> > > > data -\> (string)
> > > >
> > > > > The MCP server descriptor content, serialized as descriptor payload data.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `102400`
> > > >
> > > > dataSchemaVersion -\> (string)
> > > >
> > > > > The schema version of the descriptor payload.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `255`
> > > >
> > > > additionalData -\> (structure)
> > > >
> > > > > Additional data associated with the MCP server descriptor, such as tool definitions.
> > > > >
> > > > > tools -\> (structure)
> > > > >
> > > > > > The MCP tools descriptor that defines the tools exposed by the MCP server.
> > > > > >
> > > > > > data -\> (string)
> > > > > >
> > > > > > > The MCP tools descriptor content, serialized as descriptor payload data.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `102400`
> > > > > >
> > > > > > dataSchemaVersion -\> (string)
> > > > > >
> > > > > > > The schema version of the descriptor payload.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> > > >
> > > > source -\> (structure)
> > > >
> > > > > The source location from which the MCP (Model Context Protocol) server descriptor content was retrieved.
> > > > >
> > > > > fromUrl -\> (structure)
> > > > >
> > > > > > The URL-based descriptor source, populated when descriptor content is synchronized from a URL.
> > > > > >
> > > > > > url -\> (string) \[required\]
> > > > > >
> > > > > > > The URL from which the descriptor content is retrieved.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `https://.*`
> > >
> > > a2aAgentCard -\> (structure)
> > >
> > > > The A2A agent card descriptor, populated when the record type is AGENT.
> > > >
> > > > data -\> (string)
> > > >
> > > > > The A2A agent card content, serialized as descriptor payload data.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `102400`
> > > >
> > > > dataSchemaVersion -\> (string)
> > > >
> > > > > The schema version of the descriptor payload.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `255`
> > > >
> > > > source -\> (structure)
> > > >
> > > > > The source location from which the A2A (Agent-to-Agent) agent card descriptor content was retrieved.
> > > > >
> > > > > fromUrl -\> (structure)
> > > > >
> > > > > > The URL-based descriptor source, populated when descriptor content is synchronized from a URL.
> > > > > >
> > > > > > url -\> (string) \[required\]
> > > > > >
> > > > > > > The URL from which the descriptor content is retrieved.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `https://.*`
> > >
> > > agentSkillsDefinition -\> (structure)
> > >
> > > > The agent skills definition descriptor, populated when the record type is SKILL.
> > > >
> > > > data -\> (string)
> > > >
> > > > > The agent skills definition content, serialized as descriptor payload data.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `102400`
> > > >
> > > > dataSchemaVersion -\> (string)
> > > >
> > > > > The schema version of the descriptor payload.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `255`
> > > >
> > > > additionalData -\> (structure)
> > > >
> > > > > Additional data for the agent skills definition, such as the skills markdown descriptor.
> > > > >
> > > > > skillMd -\> (structure)
> > > > >
> > > > > > The agent skills markdown descriptor associated with the agent skills definition.
> > > > > >
> > > > > > data -\> (string)
> > > > > >
> > > > > > > The agent skills markdown content, serialized as descriptor payload data.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `102400`
> > > > > >
> > > > > > dataSchemaVersion -\> (string)
> > > > > >
> > > > > > > The schema version of the descriptor payload.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> > > > > >
> > > > > > source -\> (structure)
> > > > > >
> > > > > > > The source location from which the agent skills markdown content was retrieved.
> > > > > > >
> > > > > > > fromUrl -\> (structure)
> > > > > > >
> > > > > > > > The URL-based descriptor source, populated when descriptor content is synchronized from a URL.
> > > > > > > >
> > > > > > > > url -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The URL from which the descriptor content is retrieved.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `2048`
> > > > > > > > > - pattern: `https://.*`
> > >
> > > custom -\> (structure)
> > >
> > > > The custom descriptor, populated when the record type is CUSTOM.
> > > >
> > > > data -\> (string)
> > > >
> > > > > The custom descriptor content, serialized as descriptor payload data.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `102400`
> > >
> > > http -\> (structure)
> > >
> > > > The HTTP descriptor, populated when the record exposes an HTTP endpoint.
> > > >
> > > > source -\> (structure)
> > > >
> > > > > The source location of the HTTP endpoint.
> > > > >
> > > > > fromUrl -\> (structure)
> > > > >
> > > > > > The URL-based descriptor source, populated when descriptor content is synchronized from a URL.
> > > > > >
> > > > > > url -\> (string) \[required\]
> > > > > >
> > > > > > > The URL from which the descriptor content is retrieved.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `https://.*`
> > >
> > > agui -\> (structure)
> > >
> > > > The AG-UI descriptor, populated when the record exposes an AG-UI protocol endpoint.
> > > >
> > > > source -\> (structure)
> > > >
> > > > > The source location of the AG-UI protocol endpoint.
> > > > >
> > > > > fromUrl -\> (structure)
> > > > >
> > > > > > The URL-based descriptor source, populated when descriptor content is synchronized from a URL.
> > > > > >
> > > > > > url -\> (string) \[required\]
> > > > > >
> > > > > > > The URL from which the descriptor content is retrieved.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `https://.*`
> >
> > recordVersion -\> (string) \[required\]
> >
> > > The version identifier of the registry record.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `255`
> > > - pattern: `[a-zA-Z0-9.-]+`
> >
> > status -\> (string) \[required\]
> >
> > > The lifecycle status of the registry record. A record is `DRAFT` before it is submitted, `PENDING_APPROVAL` while awaiting curator review, and `APPROVED` once it is approved and discoverable. `REJECTED` and `DEPRECATED` records are not discoverable. The `CREATING` , `UPDATING` , `CREATE_FAILED` , and `UPDATE_FAILED` values reflect the state of an in-progress or failed asynchronous change.
> > >
> > > Possible values:
> > >
> > > - `DRAFT`
> > > - `PENDING_APPROVAL`
> > > - `APPROVED`
> > > - `REJECTED`
> > > - `DEPRECATED`
> > > - `CREATING`
> > > - `UPDATING`
> > > - `CREATE_FAILED`
> > > - `UPDATE_FAILED`
> >
> > createdAt -\> (timestamp) \[required\]
> >
> > > The timestamp when the registry record was created.
> >
> > updatedAt -\> (timestamp) \[required\]
> >
> > > The timestamp when the registry record was last updated.

errors -\> (list)

> The per-record errors for records that could not be retrieved. This list is empty when all requested records were returned.
>
> (structure)
>
> > Describes why a requested record could not be retrieved.
> >
> > registryId -\> (string) \[required\]
> >
> > > The identifier of the registry the record was requested from, echoed from the request.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `2048`
> > > - pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`
> >
> > recordId -\> (string) \[required\]
> >
> > > The identifier of the record that could not be retrieved, echoed from the request in the same format that you supplied (ARN or record ID).
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `2048`
> > > - pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/)?[a-zA-Z0-9]{12}`
> >
> > errorCode -\> (string) \[required\]
> >
> > > The machine-readable reason that the record could not be retrieved.
> > >
> > > Possible values:
> > >
> > > - `RESOURCE_NOT_FOUND`
> > > - `ACCESS_DENIED`
> > > - `INTERNAL_ERROR`
> >
> > message -\> (string)
> >
> > > An optional human-readable detail about the error. Do not parse this value programmatically.

- [← agent-registry](index.html "previous chapter (use the left arrow)") /
- [list-discoverable-registry-records →](list-discoverable-registry-records.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](list-discoverable-registry-records.html "list-discoverable-registry-records") \|
- [previous](index.html "agent-registry") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [agent-registry](index.html) »
- [batch-get-discoverable-registry-record]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

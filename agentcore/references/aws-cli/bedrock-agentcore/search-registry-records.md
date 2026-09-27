---
title: aws bedrock-agentcore search-registry-records
description: \ [aws . bedrock-agentcore \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore/search-registry-records.html
fetched: '2026-09-26'
tags:
- agent-registry
- agentcore
- aws-cli
- bedrock-agentcore
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore](index.html#cli-aws-bedrock-agentcore) \]

# search-registry-records

## Description

Searches for registry records using semantic, lexical, or hybrid queries. Returns metadata for matching records ordered by relevance within the specified registry.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-2024-02-28/SearchRegistryRecords)

`search-registry-records` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

      search-registry-records
    --search-query <value>
    --registry-ids <value>
    [--max-results <value>]
    [--filters <value>]
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

`--search-query` (string) \[required\]

> The search query to find matching registry records.
>
> Constraints:
>
> - min: `1`
> - max: `256`

`--registry-ids` (list) \[required\]

> The list of registry identifiers to search within. Currently, you can specify exactly one registry identifier. You can provide either the full Amazon Web Services Resource Name (ARN) or the 12-character alphanumeric registry ID.
>
> Constraints:
>
> - min: `1`
> - max: `1`
>
> (string)
>
> > Constraints:
> >
> > - min: `1`
> > - max: `2048`
> > - pattern: `(arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`

Syntax:

    "string" "string" ...

`--max-results` (integer)

> The maximum number of records to return in a single call. Valid values are 1 through 20. The default value is 10.
>
> Constraints:
>
> - min: `1`
> - max: `20`

`--filters` (document)

> A metadata filter expression to narrow search results. Uses structured JSON operators including field-level operators (`$eq` , `$ne` , `$in` ) and logical operators (`$and` , `$or` ) on filterable fields (`name` , `descriptorType` , `version` ). For example, to filter by descriptor type: `{"descriptorType":`` ``{"$eq":`` ``"MCP"}}` . To combine filters: `{"$and":`` ``[{"descriptorType":`` ``{"$eq":`` ``"MCP"}},`` ``{"name":`` ``{"$eq":`` ``"my-tool"}}]}` .

JSON Syntax:

    {...}

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

> The list of registry records that match the search query, ordered by relevance.
>
> (structure)
>
> > Summary information about a registry record.
> >
> > registryArn -\> (string) \[required\]
> >
> > > The Amazon Resource Name (ARN) of the registry that this record belongs to.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `2048`
> > > - pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}`
> >
> > recordArn -\> (string) \[required\]
> >
> > > The Amazon Resource Name (ARN) of the registry record.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `2048`
> > > - pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}`
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
> > > The name of the registry record.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `255`
> > > - pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`
> >
> > description -\> (string)
> >
> > > A description of the registry record.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `4096`
> >
> > descriptorType -\> (string) \[required\]
> >
> > > The type of descriptor associated with this registry record.
> > >
> > > Possible values:
> > >
> > > - `MCP`
> > > - `A2A`
> > > - `CUSTOM`
> > > - `AGENT_SKILLS`
> >
> > descriptors -\> (structure) \[required\]
> >
> > > The descriptor configurations for this registry record.
> > >
> > > mcp -\> (structure)
> > >
> > > > The MCP (Model Context Protocol) descriptor configuration. Populated when the record’s `descriptorType` is `MCP` .
> > > >
> > > > server -\> (structure) \[required\]
> > > >
> > > > > The MCP server definition that describes the server configuration.
> > > > >
> > > > > schemaVersion -\> (string)
> > > > >
> > > > > > The schema version of the MCP server configuration. The schema version identifies the format of the server definition content.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `255`
> > > > >
> > > > > inlineContent -\> (string)
> > > > >
> > > > > > The inline content of the server definition.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `409600`
> > > >
> > > > tools -\> (structure) \[required\]
> > > >
> > > > > The MCP tools definition that describes the available tools.
> > > > >
> > > > > protocolVersion -\> (string)
> > > > >
> > > > > > The MCP protocol version that the tools conform to. This differs from the `schemaVersion` field in the server definition, which identifies the server configuration schema format.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `255`
> > > > >
> > > > > inlineContent -\> (string)
> > > > >
> > > > > > The inline content of the tools definition.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `409600`
> > >
> > > a2a -\> (structure)
> > >
> > > > The A2A (Agent-to-Agent) descriptor configuration. Populated when the record’s `descriptorType` is `A2A` .
> > > >
> > > > agentCard -\> (structure) \[required\]
> > > >
> > > > > The agent card definition that describes the agent’s capabilities and interface.
> > > > >
> > > > > schemaVersion -\> (string)
> > > > >
> > > > > > The schema version of the agent card definition.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `255`
> > > > >
> > > > > inlineContent -\> (string)
> > > > >
> > > > > > The inline content of the agent card definition.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `409600`
> > >
> > > custom -\> (structure)
> > >
> > > > The custom descriptor configuration. Populated when the record’s `descriptorType` is `CUSTOM` .
> > > >
> > > > inlineContent -\> (string)
> > > >
> > > > > The inline content of the custom descriptor.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `409600`
> > >
> > > agentSkills -\> (structure)
> > >
> > > > The agent skills descriptor configuration. Populated when the record’s `descriptorType` is `AGENT_SKILLS` .
> > > >
> > > > skillMd -\> (structure) \[required\]
> > > >
> > > > > The skill description in markdown format.
> > > > >
> > > > > inlineContent -\> (string)
> > > > >
> > > > > > The inline markdown content of the skill definition.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `409600`
> > > >
> > > > skillDefinition -\> (structure)
> > > >
> > > > > The structured skill definition with a schema version and content.
> > > > >
> > > > > schemaVersion -\> (string)
> > > > >
> > > > > > The schema version of the skill definition. If you don’t specify a version, the service detects it automatically.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `255`
> > > > >
> > > > > inlineContent -\> (string)
> > > > >
> > > > > > The inline content of the skill definition.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `409600`
> >
> > version -\> (string) \[required\]
> >
> > > The version of the registry record.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `255`
> > > - pattern: `[a-zA-Z0-9.-]+`
> >
> > status -\> (string) \[required\]
> >
> > > The current status of the registry record.
> > >
> > > Possible values:
> > >
> > > - `DRAFT`
> > > - `PENDING_APPROVAL`
> > > - `APPROVED`
> > > - `REJECTED`
> > > - `DEPRECATED`
> >
> > createdAt -\> (timestamp) \[required\]
> >
> > > The date and time when the registry record was created.
> >
> > updatedAt -\> (timestamp) \[required\]
> >
> > > The date and time when the registry record was last updated.

- [← save-browser-session-profile](save-browser-session-profile.html "previous chapter (use the left arrow)") /
- [start-batch-evaluation →](start-batch-evaluation.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](start-batch-evaluation.html "start-batch-evaluation") \|
- [previous](save-browser-session-profile.html "save-browser-session-profile") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore](index.html) »
- [search-registry-records]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

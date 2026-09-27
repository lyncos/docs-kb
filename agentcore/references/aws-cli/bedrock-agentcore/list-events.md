---
title: aws bedrock-agentcore list-events
description: \ [aws . bedrock-agentcore \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore/list-events.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore](index.html#cli-aws-bedrock-agentcore) \]

# list-events

## Description

Lists events in an AgentCore Memory resource based on specified criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.

To use this operation, you must have the `bedrock-agentcore:ListEvents` permission.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-2024-02-28/ListEvents)

`list-events` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

`list-events` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument. When using `--output`` ``text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `events`

## Synopsis

      list-events
    --memory-id <value>
    --session-id <value>
    --actor-id <value>
    [--include-payloads | --no-include-payloads]
    [--filter <value>]
    [--starting-token <value>]
    [--page-size <value>]
    [--max-items <value>]
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

> The identifier of the AgentCore Memory resource for which to list events.
>
> Constraints:
>
> - min: `12`
> - pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`

`--session-id` (string) \[required\]

> The identifier of the session for which to list events.
>
> Constraints:
>
> - min: `1`
> - max: `100`
> - pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`

`--actor-id` (string) \[required\]

> The identifier of the actor for which to list events.
>
> Constraints:
>
> - min: `1`
> - max: `255`
> - pattern: `[a-zA-Z0-9][a-zA-Z0-9-_/]*(?::[a-zA-Z0-9-_/]+)*[a-zA-Z0-9-_/]*`

`--include-payloads` \| `--no-include-payloads` (boolean)

> Specifies whether to include event payloads in the response. Set to true to include payloads, or false to exclude them.

`--filter` (structure)

> Filter criteria to apply when listing events.
>
> branch -\> (structure)
>
> > The branch filter criteria to apply when listing events.
> >
> > name -\> (string) \[required\]
> >
> > > The name of the branch to filter by.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `100`
> > > - pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
> >
> > includeParentBranches -\> (boolean)
> >
> > > Specifies whether to include parent branches in the results. Set to true to include parent branches, or false to exclude them.
>
> eventMetadata -\> (list)
>
> > Event metadata filter criteria to apply when retrieving events.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `5`
> >
> > (structure)
> >
> > > Filter expression for retrieving events based on metadata associated with an event.
> > >
> > > left -\> (tagged union structure) \[required\]
> > >
> > > > Left operand of the event metadata filter expression.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `metadataKey`.
> > > >
> > > > metadataKey -\> (string)
> > > >
> > > > > Key associated with the metadata in an event.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `128`
> > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > >
> > > operator -\> (string) \[required\]
> > >
> > > > Operator applied to the event metadata filter expression.
> > > >
> > > > Possible values:
> > > >
> > > > - `EQUALS_TO`
> > > > - `EXISTS`
> > > > - `NOT_EXISTS`
> > >
> > > right -\> (tagged union structure)
> > >
> > > > Right operand of the event metadata filter expression.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `metadataValue`.
> > > >
> > > > metadataValue -\> (tagged union structure)
> > > >
> > > > > Value associated with the key in `eventMetadata` .
> > > > >
> > > > > ### Note
> > > > >
> > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`.
> > > > >
> > > > > stringValue -\> (string)
> > > > >
> > > > > > Value associated with the `eventMetadata` key.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `0`
> > > > > > - max: `256`
> > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`

JSON Syntax:

    {
      "branch": {
        "name": "string",
        "includeParentBranches": true|false
      },
      "eventMetadata": [
        {
          "left": {
            "metadataKey": "string"
          },
          "operator": "EQUALS_TO"|"EXISTS"|"NOT_EXISTS",
          "right": {
            "metadataValue": {
              "stringValue": "string"
            }
          }
        }
        ...
      ]
    }

`--starting-token` (string)

> A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.
>
> For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

> The size of each page to get in the AWS service call. This does not affect the number of items returned in the command’s output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.
>
> For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .
>
> Constraints:
>
> - min: `1`
> - max: `100`

`--max-items` (integer)

> The total number of items to return in the command’s output. If the total number of items available is more than the value specified, a `NextToken` is provided in the command’s output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.
>
> For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

events -\> (list)

> The list of events that match the specified criteria.
>
> (structure)
>
> > Contains information about an event in an AgentCore Memory resource.
> >
> > memoryId -\> (string) \[required\]
> >
> > > The identifier of the AgentCore Memory resource containing the event.
> > >
> > > Constraints:
> > >
> > > - min: `12`
> > > - pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
> >
> > actorId -\> (string) \[required\]
> >
> > > The identifier of the actor associated with the event.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `255`
> > > - pattern: `[a-zA-Z0-9][a-zA-Z0-9-_/]*(?::[a-zA-Z0-9-_/]+)*[a-zA-Z0-9-_/]*`
> >
> > sessionId -\> (string) \[required\]
> >
> > > The identifier of the session containing the event.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `100`
> > > - pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
> >
> > eventId -\> (string) \[required\]
> >
> > > The unique identifier of the event.
> > >
> > > Constraints:
> > >
> > > - pattern: `[0-9]+#[a-fA-F0-9]+`
> >
> > eventTimestamp -\> (timestamp) \[required\]
> >
> > > The timestamp when the event occurred.
> >
> > payload -\> (list) \[required\]
> >
> > > The content payload of the event.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `100`
> > >
> > > (tagged union structure)
> > >
> > > > Contains the payload content for an event.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `conversational`, `blob`, `json`.
> > > >
> > > > conversational -\> (structure)
> > > >
> > > > > The conversational content of the payload.
> > > > >
> > > > > content -\> (tagged union structure) \[required\]
> > > > >
> > > > > > The content of the conversation message.
> > > > > >
> > > > > > ### Note
> > > > > >
> > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `text`.
> > > > > >
> > > > > > text -\> (string)
> > > > > >
> > > > > > > The text content of the memory item.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `100000`
> > > > >
> > > > > role -\> (string) \[required\]
> > > > >
> > > > > > The role of the participant in the conversation (for example, “user” or “assistant”).
> > > > > >
> > > > > > Possible values:
> > > > > >
> > > > > > - `ASSISTANT`
> > > > > > - `USER`
> > > > > > - `TOOL`
> > > > > > - `OTHER`
> > > >
> > > > blob -\> (document)
> > > >
> > > > > The binary content of the payload.
> > > >
> > > > json -\> (structure)
> > > >
> > > > > The JSON content of the payload. Use this type to store non-conversational, JSON-formatted data, such as behavioral events, activity logs, or system events.
> > > > >
> > > > > content -\> (document) \[required\]
> > > > >
> > > > > > The JSON content of the payload. Accepts any JSON value, including objects, arrays, strings, numbers, booleans, and null. The maximum size is 100 KB.
> >
> > branch -\> (structure)
> >
> > > The branch information for the event.
> > >
> > > rootEventId -\> (string)
> > >
> > > > The identifier of the root event for this branch.
> > > >
> > > > Constraints:
> > > >
> > > > - pattern: `[0-9]+#[a-fA-F0-9]+`
> > >
> > > name -\> (string) \[required\]
> > >
> > > > The name of the branch.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `100`
> > > > - pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
> >
> > metadata -\> (map)
> >
> > > Metadata associated with an event.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `15`
> > >
> > > key -\> (string)
> > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `128`
> > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > >
> > > value -\> (tagged union structure)
> > >
> > > > Value associated with the `eventMetadata` key.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`.
> > > >
> > > > stringValue -\> (string)
> > > >
> > > > > Value associated with the `eventMetadata` key.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `0`
> > > > > - max: `256`
> > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`

nextToken -\> (string)

> The token to use in a subsequent request to get the next set of results. This value is null when there are no more results to return.

- [← list-code-interpreter-sessions](list-code-interpreter-sessions.html "previous chapter (use the left arrow)") /
- [list-memory-extraction-jobs →](list-memory-extraction-jobs.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](list-memory-extraction-jobs.html "list-memory-extraction-jobs") \|
- [previous](list-code-interpreter-sessions.html "list-code-interpreter-sessions") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore](index.html) »
- [list-events]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

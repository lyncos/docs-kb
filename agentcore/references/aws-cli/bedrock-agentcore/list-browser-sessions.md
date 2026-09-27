---
title: aws bedrock-agentcore list-browser-sessions
description: \ [aws . bedrock-agentcore \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore/list-browser-sessions.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore](index.html#cli-aws-bedrock-agentcore) \]

# list-browser-sessions

## Description

Retrieves a list of browser sessions in Amazon Bedrock AgentCore that match the specified criteria. This operation returns summary information about each session, including identifiers, status, and timestamps.

You can filter the results by browser identifier and session status. The operation supports pagination to handle large result sets efficiently.

We recommend using pagination to ensure that the operation returns quickly and successfully when retrieving large numbers of sessions.

The following operations are related to `ListBrowserSessions` :

- [StartBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html)
- [GetBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-2024-02-28/ListBrowserSessions)

## Synopsis

      list-browser-sessions
    --browser-identifier <value>
    [--max-results <value>]
    [--next-token <value>]
    [--status <value>]
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

`--browser-identifier` (string) \[required\]

> The unique identifier of the browser to list sessions for. If specified, only sessions for this browser are returned. If not specified, sessions for all browsers are returned.

`--max-results` (integer)

> The maximum number of results to return in a single call. The default value is 10. Valid values range from 1 to 100. To retrieve the remaining results, make another call with the returned `nextToken` value.
>
> Constraints:
>
> - min: `1`
> - max: `100`

`--next-token` (string)

> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. If not specified, Amazon Bedrock AgentCore returns the first page of results.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `\S*`

`--status` (string)

> The status of the browser sessions to list. Valid values include ACTIVE, STOPPING, and STOPPED. If not specified, sessions with any status are returned.
>
> Possible values:
>
> - `READY`
> - `TERMINATED`

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

items -\> (list)

> The list of browser sessions that match the specified criteria.
>
> (structure)
>
> > A condensed representation of a browser session in Amazon Bedrock AgentCore. This structure contains key information about a browser session, including identifiers, status, and timestamps, without the full details of the session configuration and streams.
> >
> > browserIdentifier -\> (string) \[required\]
> >
> > > The unique identifier of the browser associated with the session. This identifier specifies which browser environment is used for the session.
> >
> > sessionId -\> (string) \[required\]
> >
> > > The unique identifier of the browser session. This identifier is used in operations that interact with the session.
> > >
> > > Constraints:
> > >
> > > - pattern: `[0-9a-zA-Z]{1,40}`
> >
> > name -\> (string)
> >
> > > The name of the browser session. This name helps identify and manage the session.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `100`
> >
> > status -\> (string) \[required\]
> >
> > > The current status of the browser session. Possible values include ACTIVE, STOPPING, and STOPPED.
> > >
> > > Possible values:
> > >
> > > - `READY`
> > > - `TERMINATED`
> >
> > createdAt -\> (timestamp) \[required\]
> >
> > > The timestamp when the browser session was created. This value is in ISO 8601 format.
> >
> > lastUpdatedAt -\> (timestamp)
> >
> > > The timestamp when the browser session was last updated. This value is in ISO 8601 format.

nextToken -\> (string)

> The token to use in a subsequent `ListBrowserSessions` request to get the next set of results.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `\S*`

- [← list-batch-evaluations](list-batch-evaluations.html "previous chapter (use the left arrow)") /
- [list-code-interpreter-sessions →](list-code-interpreter-sessions.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](list-code-interpreter-sessions.html "list-code-interpreter-sessions") \|
- [previous](list-batch-evaluations.html "list-batch-evaluations") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore](index.html) »
- [list-browser-sessions]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

---
title: aws agent-registry list-discoverable-registry-records
description: \ [aws . agent-registry \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / agent-registry
source_url: https://docs.aws.amazon.com/cli/latest/reference/agent-registry/list-discoverable-registry-records.html
fetched: '2026-09-26'
tags:
- agent-registry
- agentcore
- aws-cli
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [agent-registry](index.html#cli-aws-agent-registry) \]

# list-discoverable-registry-records

## Description

Lists the discoverable registry records in a registry. You can optionally filter and paginate the results.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/agent-registry-2025-12-01/ListDiscoverableRegistryRecords)

`list-discoverable-registry-records` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument. When using `--output`` ``text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `registryRecords`

## Synopsis

      list-discoverable-registry-records
    --registry-id <value>
    [--filters <value>]
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

`--registry-id` (string) \[required\]

> The identifier of the registry whose discoverable records are listed. You can provide either the full Amazon Resource Name (ARN) or the registry ID.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`

`--filters` (list)

> The filters to apply to the discoverable registry record list.
>
> Constraints:
>
> - min: `0`
> - max: `10`
>
> (structure)
>
> > A single filter applied to a `ListDiscoverableRegistryRecords` request.
> >
> > name -\> (string) \[required\]
> >
> > > The attribute to filter on.
> > >
> > > Possible values:
> > >
> > > - `recordType`
> > > - `descriptorType`
> >
> > values -\> (list) \[required\]
> >
> > > The values to match for the attribute.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `10`
> > >
> > > (string)
> > >
> > > > A single filter value. Constrained by length only; the accepted set of values is filter-specific and validated server-side so enum-style values such as READY or AWS_IAM are accepted.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `255`

Shorthand Syntax:

    name=string,values=string,string ...

JSON Syntax:

    [
      {
        "name": "recordType"|"descriptorType",
        "values": ["string", ...]
      }
      ...
    ]

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

registryRecords -\> (list)

> The page of discoverable registry record summaries.
>
> (structure)
>
> > Summary information about a discoverable registry record returned by `ListDiscoverableRegistryRecords` . This summary does not include descriptors.
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
> >
> > descriptorTypes -\> (list)
> >
> > > The descriptor types that are present on this registry record. Each value corresponds to a descriptor entry key on the approved record.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `10`
> > >
> > > (string)

nextToken -\> (string)

> The pagination token to pass to a subsequent request to retrieve the next page of results. This field is absent when there are no more results.

- [← batch-get-discoverable-registry-record](batch-get-discoverable-registry-record.html "previous chapter (use the left arrow)") /
- [search-discoverable-registry-records →](search-discoverable-registry-records.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](search-discoverable-registry-records.html "search-discoverable-registry-records") \|
- [previous](batch-get-discoverable-registry-record.html "batch-get-discoverable-registry-record") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [agent-registry](index.html) »
- [list-discoverable-registry-records]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

---
title: aws bedrock-agentcore batch-delete-memory-records
description: \ [aws . bedrock-agentcore \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore/batch-delete-memory-records.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore](index.html#cli-aws-bedrock-agentcore) \]

# batch-delete-memory-records

## Description

Deletes multiple memory records in a single batch operation from the specified memory.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-2024-02-28/BatchDeleteMemoryRecords)

## Synopsis

      batch-delete-memory-records
    --memory-id <value>
    --records <value>
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

> The unique ID of the memory resource where records will be deleted.
>
> Constraints:
>
> - min: `12`
> - pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`

`--records` (list) \[required\]

> A list of memory record deletion inputs to be processed in the batch operation.
>
> Constraints:
>
> - min: `0`
> - max: `100`
>
> (structure)
>
> > Input structure to delete an existing memory record.
> >
> > memoryRecordId -\> (string) \[required\]
> >
> > > The unique ID of the memory record to be deleted.
> > >
> > > Constraints:
> > >
> > > - min: `40`
> > > - max: `50`
> > > - pattern: `mem-[a-zA-Z0-9-_]*`
> >
> > namespace -\> (string)
> >
> > > The namespace of the memory record being deleted. This value is used for IAM condition key authorization.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `1024`
> > > - pattern: `[a-zA-Z0-9/*][a-zA-Z0-9-_/*]*(?::[a-zA-Z0-9-_/*]+)*[a-zA-Z0-9-_/*]*`

Shorthand Syntax:

    memoryRecordId=string,namespace=string ...

JSON Syntax:

    [
      {
        "memoryRecordId": "string",
        "namespace": "string"
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

successfulRecords -\> (list)

> A list of memory records that were successfully deleted during the batch operation.
>
> (structure)
>
> > Output information returned after processing a memory record operation.
> >
> > memoryRecordId -\> (string) \[required\]
> >
> > > The unique ID associated to the memory record.
> > >
> > > Constraints:
> > >
> > > - min: `40`
> > > - max: `50`
> > > - pattern: `mem-[a-zA-Z0-9-_]*`
> >
> > status -\> (string) \[required\]
> >
> > > The status of the memory record operation (e.g., SUCCEEDED, FAILED).
> > >
> > > Possible values:
> > >
> > > - `SUCCEEDED`
> > > - `FAILED`
> >
> > requestIdentifier -\> (string)
> >
> > > The client-provided identifier that was used to track this record operation.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `80`
> > > - pattern: `[a-zA-Z0-9_-]+`
> >
> > errorCode -\> (integer)
> >
> > > The error code returned when the memory record operation fails.
> >
> > errorMessage -\> (string)
> >
> > > A human-readable error message describing why the memory record operation failed.

failedRecords -\> (list)

> A list of memory records that failed to be deleted, including error details for each failure.
>
> (structure)
>
> > Output information returned after processing a memory record operation.
> >
> > memoryRecordId -\> (string) \[required\]
> >
> > > The unique ID associated to the memory record.
> > >
> > > Constraints:
> > >
> > > - min: `40`
> > > - max: `50`
> > > - pattern: `mem-[a-zA-Z0-9-_]*`
> >
> > status -\> (string) \[required\]
> >
> > > The status of the memory record operation (e.g., SUCCEEDED, FAILED).
> > >
> > > Possible values:
> > >
> > > - `SUCCEEDED`
> > > - `FAILED`
> >
> > requestIdentifier -\> (string)
> >
> > > The client-provided identifier that was used to track this record operation.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `80`
> > > - pattern: `[a-zA-Z0-9_-]+`
> >
> > errorCode -\> (integer)
> >
> > > The error code returned when the memory record operation fails.
> >
> > errorMessage -\> (string)
> >
> > > A human-readable error message describing why the memory record operation failed.

- [← batch-create-memory-records](batch-create-memory-records.html "previous chapter (use the left arrow)") /
- [batch-update-memory-records →](batch-update-memory-records.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](batch-update-memory-records.html "batch-update-memory-records") \|
- [previous](batch-create-memory-records.html "batch-create-memory-records") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore](index.html) »
- [batch-delete-memory-records]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

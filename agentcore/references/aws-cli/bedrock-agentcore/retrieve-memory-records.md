---
title: aws bedrock-agentcore retrieve-memory-records
description: \ [aws . bedrock-agentcore \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore/retrieve-memory-records.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore](index.html#cli-aws-bedrock-agentcore) \]

# retrieve-memory-records

## Description

Searches for and retrieves memory records from an AgentCore Memory resource based on specified search criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.

To use this operation, you must have the `bedrock-agentcore:RetrieveMemoryRecords` permission.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-2024-02-28/RetrieveMemoryRecords)

`retrieve-memory-records` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument. When using `--output`` ``text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `memoryRecordSummaries`

## Synopsis

      retrieve-memory-records
    --memory-id <value>
    [--namespace <value>]
    [--namespace-path <value>]
    --search-criteria <value>
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

> The identifier of the AgentCore Memory resource from which to retrieve memory records.
>
> Constraints:
>
> - min: `12`
> - pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`

`--namespace` (string)

> The namespace prefix to filter memory records by. Searches for memory records in namespaces that start with the provided prefix. Either `namespace` or `namespacePath` is required.
>
> Constraints:
>
> - min: `1`
> - max: `1024`
> - pattern: `[a-zA-Z0-9/*][a-zA-Z0-9-_/*]*(?::[a-zA-Z0-9-_/*]+)*[a-zA-Z0-9-_/*]*`

`--namespace-path` (string)

> Use namespacePath for hierarchical retrievals. Return all memory records where namespace falls under the same parent hierarchy. Either `namespace` or `namespacePath` is required.
>
> Constraints:
>
> - min: `1`
> - max: `1024`
> - pattern: `[a-zA-Z0-9/*][a-zA-Z0-9-_/*]*(?::[a-zA-Z0-9-_/*]+)*[a-zA-Z0-9-_/*]*`

`--search-criteria` (structure) \[required\]

> The search criteria to use for finding relevant memory records. This includes the search query, memory strategy ID, and other search parameters.
>
> searchQuery -\> (string) \[required\]
>
> > The search query to use for finding relevant memory records.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `10000`
>
> memoryStrategyId -\> (string)
>
> > The memory strategy identifier to filter memory records by.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `100`
> > - pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
>
> topK -\> (integer)
>
> > The maximum number of top-scoring memory records to return. This value is used for semantic search ranking.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `100`
>
> metadataFilters -\> (list)
>
> > Filters to apply to metadata associated with a memory.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `5`
> >
> > (structure)
> >
> > > Filters to apply to metadata associated with a memory. Specify the metadata key and value in the `left` and `right` fields and use the `operator` field to define the relationship to match.
> > >
> > > left -\> (tagged union structure) \[required\]
> > >
> > > > The metadata key to evaluate.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `metadataKey`.
> > > >
> > > > metadataKey -\> (string)
> > > >
> > > > > The metadata key to filter on.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `128`
> > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > >
> > > operator -\> (string) \[required\]
> > >
> > > > The relationship between the metadata key and value to match when applying the metadata filter.
> > > >
> > > > Possible values:
> > > >
> > > > - `EQUALS_TO`
> > > > - `EXISTS`
> > > > - `NOT_EXISTS`
> > > > - `BEFORE`
> > > > - `AFTER`
> > > > - `CONTAINS`
> > > > - `GREATER_THAN`
> > > > - `GREATER_THAN_OR_EQUALS`
> > > > - `LESS_THAN`
> > > > - `LESS_THAN_OR_EQUALS`
> > >
> > > right -\> (tagged union structure)
> > >
> > > > The value to compare against. Required for all operators except EXISTS and NOT_EXISTS.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `metadataValue`.
> > > >
> > > > metadataValue -\> (tagged union structure)
> > > >
> > > > > The metadata value to compare against.
> > > > >
> > > > > ### Note
> > > > >
> > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `numberValue`, `dateTimeValue`.
> > > > >
> > > > > stringValue -\> (string)
> > > > >
> > > > > > A string value.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `256`
> > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > >
> > > > > stringListValue -\> (list)
> > > > >
> > > > > > A list of string values.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `5`
> > > > > >
> > > > > > (string)
> > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `64`
> > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > >
> > > > > numberValue -\> (double)
> > > > >
> > > > > > A numeric value.
> > > > >
> > > > > dateTimeValue -\> (timestamp)
> > > > >
> > > > > > A timestamp value in ISO 8601 UTC format.

JSON Syntax:

    {
      "searchQuery": "string",
      "memoryStrategyId": "string",
      "topK": integer,
      "metadataFilters": [
        {
          "left": {
            "metadataKey": "string"
          },
          "operator": "EQUALS_TO"|"EXISTS"|"NOT_EXISTS"|"BEFORE"|"AFTER"|"CONTAINS"|"GREATER_THAN"|"GREATER_THAN_OR_EQUALS"|"LESS_THAN"|"LESS_THAN_OR_EQUALS",
          "right": {
            "metadataValue": {
              "stringValue": "string",
              "stringListValue": ["string", ...],
              "numberValue": double,
              "dateTimeValue": timestamp
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

memoryRecordSummaries -\> (list)

> The list of memory record summaries that match the search criteria, ordered by relevance.
>
> (structure)
>
> > Contains summary information about a memory record.
> >
> > memoryRecordId -\> (string) \[required\]
> >
> > > The unique identifier of the memory record.
> > >
> > > Constraints:
> > >
> > > - min: `40`
> > > - max: `50`
> > > - pattern: `mem-[a-zA-Z0-9-_]*`
> >
> > content -\> (tagged union structure) \[required\]
> >
> > > The content of the memory record.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `text`.
> > >
> > > text -\> (string)
> > >
> > > > The text content of the memory record.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `16000`
> >
> > memoryStrategyId -\> (string) \[required\]
> >
> > > The identifier of the memory strategy associated with this record.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `100`
> > > - pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`
> >
> > namespaces -\> (list) \[required\]
> >
> > > The namespaces associated with this memory record.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `1`
> > >
> > > (string)
> > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `1024`
> > > > - pattern: `[a-zA-Z0-9/*][a-zA-Z0-9-_/*]*(?::[a-zA-Z0-9-_/*]+)*[a-zA-Z0-9-_/*]*`
> >
> > createdAt -\> (timestamp) \[required\]
> >
> > > The timestamp when the memory record was created.
> >
> > score -\> (double)
> >
> > > The relevance score of the memory record when returned as part of a search result. Higher values indicate greater relevance to the search query.
> >
> > metadata -\> (map)
> >
> > > A map of metadata key-value pairs associated with a memory record.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `20`
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
> > > > The value of a memory record metadata entry.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `stringListValue`, `numberValue`, `dateTimeValue`.
> > > >
> > > > stringValue -\> (string)
> > > >
> > > > > A string value.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `256`
> > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > >
> > > > stringListValue -\> (list)
> > > >
> > > > > A list of string values.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `5`
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `64`
> > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > >
> > > > numberValue -\> (double)
> > > >
> > > > > A numeric value.
> > > >
> > > > dateTimeValue -\> (timestamp)
> > > >
> > > > > A timestamp value in ISO 8601 UTC format.

nextToken -\> (string)

> The token to use in a subsequent request to get the next set of results. This value is null when there are no more results to return.

- [← process-payment](process-payment.html "previous chapter (use the left arrow)") /
- [save-browser-session-profile →](save-browser-session-profile.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](save-browser-session-profile.html "save-browser-session-profile") \|
- [previous](process-payment.html "process-payment") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore](index.html) »
- [retrieve-memory-records]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

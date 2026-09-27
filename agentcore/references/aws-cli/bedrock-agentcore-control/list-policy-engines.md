---
title: aws bedrock-agentcore-control list-policy-engines
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/list-policy-engines.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# list-policy-engines

## Description

Retrieves a list of policy engines within the AgentCore Policy system. This operation supports pagination to help administrators discover and manage policy engines across their account. Each policy engine serves as a container for related policies.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/ListPolicyEngines)

`list-policy-engines` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument. When using `--output`` ``text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `policyEngines`

## Synopsis

      list-policy-engines
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

policyEngines -\> (list)

> An array of policy engine objects that exist in the account. Each policy engine object contains the engine metadata, status, and key identifiers for further operations.
>
> Constraints:
>
> - min: `0`
> - max: `100`
>
> (structure)
>
> > Represents a policy engine resource within the AgentCore Policy system. Policy engines serve as containers for grouping related policies and provide the execution context for policy evaluation and management. Each policy engine can be associated with one Gateway (one engine per Gateway), where it intercepts all agent tool calls and evaluates them against the contained policies before allowing tools to execute. The policy engine maintains the Cedar schema generated from the Gateway’s tool manifest, ensuring that policies are validated against the actual tools and parameters available. Policy engines support two enforcement modes that can be configured when associating with a Gateway: log-only mode for testing (evaluates decisions without blocking) and enforce mode for production (actively allows or denies based on policy evaluation).
> >
> > policyEngineId -\> (string) \[required\]
> >
> > > The unique identifier for the policy engine. This system-generated identifier consists of the user name plus a 10-character generated suffix and serves as the primary key for policy engine operations.
> > >
> > > Constraints:
> > >
> > > - min: `12`
> > > - max: `59`
> > > - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`
> >
> > name -\> (string) \[required\]
> >
> > > The customer-assigned immutable name for the policy engine. This human-readable identifier must be unique within the account and cannot exceed 48 characters.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `48`
> > > - pattern: `[A-Za-z][A-Za-z0-9_]*`
> >
> > createdAt -\> (timestamp) \[required\]
> >
> > > The timestamp when the policy engine was originally created. This is automatically set by the service and used for auditing and lifecycle management.
> >
> > updatedAt -\> (timestamp) \[required\]
> >
> > > The timestamp when the policy engine was last modified. This tracks the most recent changes to the policy engine configuration or metadata.
> >
> > policyEngineArn -\> (string) \[required\]
> >
> > > The Amazon Resource Name (ARN) of the policy engine. This globally unique identifier can be used for cross-service references and IAM policy statements.
> > >
> > > Constraints:
> > >
> > > - min: `76`
> > > - max: `136`
> > > - pattern: `arn:aws[-a-z]{0,7}:bedrock-agentcore:[a-z0-9-]{9,15}:[0-9]{12}:policy-engine/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}`
> >
> > status -\> (string) \[required\]
> >
> > > The current status of the policy engine.
> > >
> > > Possible values:
> > >
> > > - `CREATING`
> > > - `ACTIVE`
> > > - `UPDATING`
> > > - `DELETING`
> > > - `CREATE_FAILED`
> > > - `UPDATE_FAILED`
> > > - `DELETE_FAILED`
> >
> > encryptionKeyArn -\> (string)
> >
> > > The Amazon Resource Name (ARN) of the KMS key used to encrypt the policy engine data.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `2048`
> > > - pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`
> >
> > description -\> (string)
> >
> > > A human-readable description of the policy engine’s purpose and scope. Limited to 4,096 characters, this helps administrators understand the policy engine’s role in the overall governance strategy.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `4096`
> >
> > statusReasons -\> (list) \[required\]
> >
> > > Additional information about the policy engine status. This provides details about any failures or the current state of the policy engine lifecycle.
> > >
> > > (string)

nextToken -\> (string)

> A pagination token that can be used in subsequent [ListPolicyEngines](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyEngines.html) calls to retrieve additional results. This token is only present when there are more results available.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `\S*`

- [← list-policy-engine-summaries](list-policy-engine-summaries.html "previous chapter (use the left arrow)") /
- [list-policy-generation-assets →](list-policy-generation-assets.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](list-policy-generation-assets.html "list-policy-generation-assets") \|
- [previous](list-policy-engine-summaries.html "list-policy-engine-summaries") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [list-policy-engines]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

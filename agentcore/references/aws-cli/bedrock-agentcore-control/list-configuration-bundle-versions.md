---
title: aws bedrock-agentcore-control list-configuration-bundle-versions
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/list-configuration-bundle-versions.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# list-configuration-bundle-versions

## Description

Lists all versions of a configuration bundle, with optional filtering by branch name or creation source.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/ListConfigurationBundleVersions)

`list-configuration-bundle-versions` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument. When using `--output`` ``text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `versions`

## Synopsis

      list-configuration-bundle-versions
    --bundle-id <value>
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

`--bundle-id` (string) \[required\]

> The unique identifier of the configuration bundle to list versions for.
>
> Constraints:
>
> - pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`

`--filter` (structure)

> An optional filter for listing versions, including branch name, creation source, and whether to return only the latest version per branch.
>
> branchName -\> (string)
>
> > Filter by branch name.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `128`
> > - pattern: `[a-zA-Z][a-zA-Z0-9_/-]{0,127}`
>
> createdByName -\> (string)
>
> > Filter by creation source name.
>
> latestPerBranch -\> (boolean)
>
> > When true, returns only the latest version for each branch. When false or not specified, returns all versions. Can be combined with `branchName` to get the latest version for a specific branch.

Shorthand Syntax:

    branchName=string,createdByName=string,latestPerBranch=boolean

JSON Syntax:

    {
      "branchName": "string",
      "createdByName": "string",
      "latestPerBranch": true|false
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

versions -\> (list)

> The list of configuration bundle version summaries.
>
> (structure)
>
> > Summary information about a configuration bundle version.
> >
> > bundleArn -\> (string) \[required\]
> >
> > > The Amazon Resource Name (ARN) of the configuration bundle.
> > >
> > > Constraints:
> > >
> > > - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
> >
> > bundleId -\> (string) \[required\]
> >
> > > The unique identifier of the configuration bundle.
> > >
> > > Constraints:
> > >
> > > - pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
> >
> > versionId -\> (string) \[required\]
> >
> > > The version identifier of this configuration bundle version.
> > >
> > > Constraints:
> > >
> > > - pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
> >
> > lineageMetadata -\> (structure)
> >
> > > The version lineage metadata, including parent versions, branch name, and creation source.
> > >
> > > parentVersionIds -\> (list)
> > >
> > > > A list of parent version identifiers. Regular commits have 0-1 parents. Merge commits have 2 parents: the target branch parent and the source branch parent. The first parent represents the primary lineage.
> > > >
> > > > (string)
> > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
> > >
> > > branchName -\> (string)
> > >
> > > > The branch name for this version. If not specified, inherits the parent’s branch or defaults to `mainline` .
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `128`
> > > > - pattern: `[a-zA-Z][a-zA-Z0-9_/-]{0,127}`
> > >
> > > createdBy -\> (structure)
> > >
> > > > The source that created this version.
> > > >
> > > > name -\> (string) \[required\]
> > > >
> > > > > The name of the source (for example, `user` , `optimization-job` , or `system` ).
> > > >
> > > > arn -\> (string)
> > > >
> > > > > The Amazon Resource Name (ARN) of the source, if applicable (for example, a user ARN or optimization job ARN).
> > >
> > > commitMessage -\> (string)
> > >
> > > > A commit message describing the changes in this version.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `500`
> >
> > versionCreatedAt -\> (timestamp) \[required\]
> >
> > > The timestamp when this version was created.

nextToken -\> (string)

> If the total number of results is greater than the `maxResults` value provided in the request, use this token when making another request in the `nextToken` field to return the next batch of results.

- [← list-code-interpreters](list-code-interpreters.html "previous chapter (use the left arrow)") /
- [list-configuration-bundles →](list-configuration-bundles.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](list-configuration-bundles.html "list-configuration-bundles") \|
- [previous](list-code-interpreters.html "list-code-interpreters") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [list-configuration-bundle-versions]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

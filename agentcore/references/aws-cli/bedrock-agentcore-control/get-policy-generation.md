---
title: aws bedrock-agentcore-control get-policy-generation
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/get-policy-generation.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# get-policy-generation

## Description

Retrieves information about a policy generation request within the AgentCore Policy system. Policy generation converts natural language descriptions into Dogwood policy statements using AI-powered translation, enabling non-technical users to create policies.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/GetPolicyGeneration)

## Synopsis

      get-policy-generation
    --policy-generation-id <value>
    --policy-engine-id <value>
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

`--policy-generation-id` (string) \[required\]

> The unique identifier of the policy generation request to be retrieved. This must be a valid generation ID from a previous [StartPolicyGeneration](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_StartPolicyGeneration.html) call.
>
> Constraints:
>
> - min: `12`
> - max: `59`
> - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`

`--policy-engine-id` (string) \[required\]

> The identifier of the policy engine associated with the policy generation request. This provides the context for the generation operation and schema validation.
>
> Constraints:
>
> - min: `12`
> - max: `59`
> - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`

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

policyEngineId -\> (string)

> The identifier of the policy engine associated with this policy generation. This confirms the policy engine context for the generation operation.
>
> Constraints:
>
> - min: `12`
> - max: `59`
> - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`

policyGenerationId -\> (string)

> The unique identifier of the policy generation request. This matches the generation ID provided in the request and serves as the tracking identifier.
>
> Constraints:
>
> - min: `12`
> - max: `59`
> - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`

name -\> (string)

> The customer-assigned name for the policy generation request. This helps identify and track generation operations across multiple requests.
>
> Constraints:
>
> - min: `1`
> - max: `48`
> - pattern: `[A-Za-z][A-Za-z0-9_]*`

policyGenerationArn -\> (string)

> The Amazon Resource Name (ARN) of the policy generation. This globally unique identifier can be used for tracking, auditing, and cross-service references.
>
> Constraints:
>
> - min: `103`
> - max: `210`
> - pattern: `arn:aws[-a-z]{0,7}:bedrock-agentcore:[a-z0-9-]{9,15}:[0-9]{12}:policy-engine/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}/policy-generation/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}`

resource -\> (tagged union structure)

> The resource information associated with the policy generation. This provides context about the target resources for which the policies are being generated.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `arn`.
>
> arn -\> (string)
>
> > The Amazon Resource Name (ARN) of the resource. This globally unique identifier specifies the exact resource that policies will be evaluated against for access control decisions.
> >
> > Constraints:
> >
> > - min: `20`
> > - max: `1011`

createdAt -\> (timestamp)

> The timestamp when the policy generation request was created. This is used for tracking and auditing generation operations and their lifecycle.

updatedAt -\> (timestamp)

> The timestamp when the policy generation was last updated. This tracks the progress of the generation process and any status changes.

status -\> (string)

> The current status of the policy generation. This indicates whether the generation is in progress, completed successfully, or failed during processing.
>
> Possible values:
>
> - `GENERATING`
> - `GENERATED`
> - `GENERATE_FAILED`
> - `DELETE_FAILED`

findings -\> (string)

> The findings and results from the policy generation process. This includes any issues, recommendations, validation results, or insights from the generated policies.

statusReasons -\> (list)

> Additional information about the generation status. This provides details about any failures, warnings, or the current state of the generation process.
>
> (string)

- [← get-policy-engine-summary](get-policy-engine-summary.html "previous chapter (use the left arrow)") /
- [get-policy-generation-summary →](get-policy-generation-summary.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](get-policy-generation-summary.html "get-policy-generation-summary") \|
- [previous](get-policy-engine-summary.html "get-policy-engine-summary") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [get-policy-generation]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

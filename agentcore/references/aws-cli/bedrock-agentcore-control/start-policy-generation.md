---
title: aws bedrock-agentcore-control start-policy-generation
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/start-policy-generation.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# start-policy-generation

## Description

Initiates the AI-powered generation of Dogwood policies from natural language descriptions within the AgentCore Policy system. This feature enables both technical and non-technical users to create policies by describing their authorization requirements in plain English, which is then automatically translated into formal Dogwood policy statements. The generation process analyzes the natural language input along with the Gateway’s tool context to produce validated policy options. Generated policy assets are automatically deleted after 7 days, so you should review and create policies from the generated assets within this timeframe. Once created, policies are permanent and not subject to this expiration. Generated policies should be reviewed and tested in log-only mode before deploying to production. Use this when you want to describe policy intent naturally rather than learning Dogwood syntax, though generated policies may require refinement for complex scenarios.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/StartPolicyGeneration)

## Synopsis

      start-policy-generation
    --policy-engine-id <value>
    --resource <value>
    --content <value>
    --name <value>
    [--client-token <value>]
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

`--policy-engine-id` (string) \[required\]

> The identifier of the policy engine that provides the context for policy generation. This engine’s schema and tool context are used to ensure generated policies are valid and applicable.
>
> Constraints:
>
> - min: `12`
> - max: `59`
> - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`

`--resource` (tagged union structure) \[required\]

> The resource information that provides context for policy generation. This helps the AI understand the target resources and generate appropriate access control rules.
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

Shorthand Syntax:

    arn=string

JSON Syntax:

    {
      "arn": "string"
    }

`--content` (tagged union structure) \[required\]

> The natural language description of the desired policy behavior. This content is processed by AI to generate corresponding Dogwood policy statements that match the described intent.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `rawText`.
>
> rawText -\> (string)
>
> > The raw text content containing natural language descriptions of desired policy behavior. This text is processed by AI to generate corresponding Dogwood policy statements that match the described intent.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `2000`

Shorthand Syntax:

    rawText=string

JSON Syntax:

    {
      "rawText": "string"
    }

`--name` (string) \[required\]

> A customer-assigned name for the policy generation request. This helps track and identify generation operations, especially when running multiple generations simultaneously.
>
> Constraints:
>
> - min: `1`
> - max: `48`
> - pattern: `[A-Za-z][A-Za-z0-9_]*`

`--client-token` (string)

> A unique, case-sensitive identifier to ensure the idempotency of the request. The AWS SDK automatically generates this token, so you don’t need to provide it in most cases. If you retry a request with the same client token, the service returns the same response without starting a duplicate generation.
>
> Constraints:
>
> - min: `33`
> - max: `256`
> - pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`

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

> The identifier of the policy engine associated with the started policy generation.
>
> Constraints:
>
> - min: `12`
> - max: `59`
> - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`

policyGenerationId -\> (string)

> The unique identifier assigned to the policy generation request for tracking progress.
>
> Constraints:
>
> - min: `12`
> - max: `59`
> - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`

name -\> (string)

> The customer-assigned name for the policy generation request.
>
> Constraints:
>
> - min: `1`
> - max: `48`
> - pattern: `[A-Za-z][A-Za-z0-9_]*`

policyGenerationArn -\> (string)

> The ARN of the created policy generation request.
>
> Constraints:
>
> - min: `103`
> - max: `210`
> - pattern: `arn:aws[-a-z]{0,7}:bedrock-agentcore:[a-z0-9-]{9,15}:[0-9]{12}:policy-engine/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}/policy-generation/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}`

resource -\> (tagged union structure)

> The resource information associated with the policy generation request.
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

> The timestamp when the policy generation request was created.

updatedAt -\> (timestamp)

> The timestamp when the policy generation was last updated.

status -\> (string)

> The initial status of the policy generation request.
>
> Possible values:
>
> - `GENERATING`
> - `GENERATED`
> - `GENERATE_FAILED`
> - `DELETE_FAILED`

findings -\> (string)

> Initial findings from the policy generation process.

statusReasons -\> (list)

> Additional information about the generation status.
>
> (string)

- [← set-token-vault-cmk](set-token-vault-cmk.html "previous chapter (use the left arrow)") /
- [submit-registry-record-for-approval →](submit-registry-record-for-approval.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](submit-registry-record-for-approval.html "submit-registry-record-for-approval") \|
- [previous](set-token-vault-cmk.html "set-token-vault-cmk") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [start-policy-generation]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

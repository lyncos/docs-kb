---
title: aws bedrock-agentcore-control create-policy-engine
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/create-policy-engine.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# create-policy-engine

## Description

Creates a new policy engine within the AgentCore Policy system. A policy engine is a collection of policies that evaluates and authorizes agent tool calls. When associated with Gateways (each Gateway can be associated with at most one policy engine, but multiple Gateways can be associated with the same engine), the policy engine intercepts all agent requests and determines whether to allow or deny each action based on the defined policies. This is an asynchronous operation. Use the [GetPolicyEngine](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetPolicyEngine.html) operation to poll the `status` field to track completion.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/CreatePolicyEngine)

## Synopsis

      create-policy-engine
    --name <value>
    [--description <value>]
    [--client-token <value>]
    [--encryption-key-arn <value>]
    [--tags <value>]
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

`--name` (string) \[required\]

> The customer-assigned immutable name for the policy engine. This name identifies the policy engine and cannot be changed after creation.
>
> Constraints:
>
> - min: `1`
> - max: `48`
> - pattern: `[A-Za-z][A-Za-z0-9_]*`

`--description` (string)

> A human-readable description of the policy engine’s purpose and scope (1-4,096 characters). This helps administrators understand the policy engine’s role in the overall governance strategy. Document which Gateway this engine will be associated with, what types of tools or workflows it governs, and the team or service responsible for maintaining it. Clear descriptions are essential when managing multiple policy engines across different services or environments.
>
> Constraints:
>
> - min: `1`
> - max: `4096`

`--client-token` (string)

> A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request with the same client token, the service returns the same response without creating a duplicate policy engine.
>
> Constraints:
>
> - min: `33`
> - max: `256`
> - pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`

`--encryption-key-arn` (string)

> The Amazon Resource Name (ARN) of the KMS key used to encrypt the policy engine data.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`

`--tags` (map)

> A map of tag keys and values to assign to an AgentCore Policy. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.
>
> Constraints:
>
> - min: `0`
> - max: `50`
>
> key -\> (string)
>
> > Constraints:
> >
> > - min: `1`
> > - max: `128`
> > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
>
> value -\> (string)
>
> > Constraints:
> >
> > - min: `0`
> > - max: `256`
> > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`

Shorthand Syntax:

    KeyName1=string,KeyName2=string

JSON Syntax:

    {"string": "string"
      ...}

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

> The unique identifier for the created policy engine. This system-generated identifier consists of the user name plus a 10-character generated suffix and is used for all subsequent policy engine operations.
>
> Constraints:
>
> - min: `12`
> - max: `59`
> - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`

name -\> (string)

> The customer-assigned name of the created policy engine. This matches the name provided in the request and serves as the human-readable identifier.
>
> Constraints:
>
> - min: `1`
> - max: `48`
> - pattern: `[A-Za-z][A-Za-z0-9_]*`

createdAt -\> (timestamp)

> The timestamp when the policy engine was created. This is automatically set by the service and used for auditing and lifecycle management.

updatedAt -\> (timestamp)

> The timestamp when the policy engine was last updated. For newly created policy engines, this matches the `createdAt` timestamp.

policyEngineArn -\> (string)

> The Amazon Resource Name (ARN) of the created policy engine. This globally unique identifier can be used for cross-service references and IAM policy statements.
>
> Constraints:
>
> - min: `76`
> - max: `136`
> - pattern: `arn:aws[-a-z]{0,7}:bedrock-agentcore:[a-z0-9-]{9,15}:[0-9]{12}:policy-engine/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}`

status -\> (string)

> The current status of the policy engine. A status of `ACTIVE` indicates the policy engine is ready for use.
>
> Possible values:
>
> - `CREATING`
> - `ACTIVE`
> - `UPDATING`
> - `DELETING`
> - `CREATE_FAILED`
> - `UPDATE_FAILED`
> - `DELETE_FAILED`

encryptionKeyArn -\> (string)

> The Amazon Resource Name (ARN) of the KMS key used to encrypt the policy engine data.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`

description -\> (string)

> A human-readable description of the policy engine’s purpose.
>
> Constraints:
>
> - min: `1`
> - max: `4096`

statusReasons -\> (list)

> Additional information about the policy engine status. This provides details about any failures or the current state of the policy engine creation process.
>
> (string)

- [← create-policy](create-policy.html "previous chapter (use the left arrow)") /
- [create-registry →](create-registry.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](create-registry.html "create-registry") \|
- [previous](create-policy.html "create-policy") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [create-policy-engine]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

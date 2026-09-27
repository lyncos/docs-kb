---
title: aws bedrock-agentcore-control create-configuration-bundle
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/create-configuration-bundle.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# create-configuration-bundle

## Description

Creates a new configuration bundle resource. A configuration bundle stores versioned component configurations for agent evaluation workflows.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/CreateConfigurationBundle)

`create-configuration-bundle` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

      create-configuration-bundle
    [--client-token <value>]
    --bundle-name <value>
    [--description <value>]
    --components <value>
    [--branch-name <value>]
    [--commit-message <value>]
    [--created-by <value>]
    [--kms-key-arn <value>]
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

`--client-token` (string)

> A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don’t specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn’t return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) .
>
> Constraints:
>
> - min: `33`
> - max: `256`
> - pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`

`--bundle-name` (string) \[required\]

> The name for the configuration bundle. Names must be unique within your account.
>
> Constraints:
>
> - pattern: `[a-zA-Z][a-zA-Z0-9_]{0,99}`

`--description` (string)

> The description for the configuration bundle.
>
> Constraints:
>
> - min: `1`
> - max: `500`
> - pattern: `.+`

`--components` (map) \[required\]

> A map of component identifiers to their configurations. Each component represents a configurable element within the bundle.
>
> key -\> (string)
>
> > Constraints:
> >
> > - min: `1`
> > - max: `2048`
> > - pattern: `[a-zA-Z][a-zA-Z0-9_:/.\-]{0,2047}`
>
> value -\> (structure)
>
> > The configuration for a component within a configuration bundle. The component type is inferred from the component identifier ARN.
> >
> > configuration -\> (document) \[required\]
> >
> > > The configuration values as a flexible JSON document.

Shorthand Syntax:

    KeyName1={},KeyName2={}

JSON Syntax:

    {"string": {
          "configuration": {...}
        }
      ...}

`--branch-name` (string)

> The branch name for version tracking. Defaults to `mainline` if not specified.
>
> Constraints:
>
> - min: `1`
> - max: `128`
> - pattern: `[a-zA-Z][a-zA-Z0-9_/-]{0,127}`

`--commit-message` (string)

> A commit message describing the initial version of the configuration bundle.
>
> Constraints:
>
> - min: `1`
> - max: `500`

`--created-by` (structure)

> The source that created this version, including the source name and optional ARN.
>
> name -\> (string) \[required\]
>
> > The name of the source (for example, `user` , `optimization-job` , or `system` ).
>
> arn -\> (string)
>
> > The Amazon Resource Name (ARN) of the source, if applicable (for example, a user ARN or optimization job ARN).

Shorthand Syntax:

    name=string,arn=string

JSON Syntax:

    {
      "name": "string",
      "arn": "string"
    }

`--kms-key-arn` (string)

> Optional KMS key ARN for encrypting component configurations.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`

`--tags` (map)

> A map of tag keys and values to assign to the configuration bundle. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.
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

bundleArn -\> (string)

> The Amazon Resource Name (ARN) of the created configuration bundle.
>
> Constraints:
>
> - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`

bundleId -\> (string)

> The unique identifier of the created configuration bundle.
>
> Constraints:
>
> - pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`

versionId -\> (string)

> The initial version identifier of the configuration bundle.
>
> Constraints:
>
> - pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

createdAt -\> (timestamp)

> The timestamp when the configuration bundle was created.

- [← create-code-interpreter](create-code-interpreter.html "previous chapter (use the left arrow)") /
- [create-consent-portal →](create-consent-portal.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](create-consent-portal.html "create-consent-portal") \|
- [previous](create-code-interpreter.html "create-code-interpreter") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [create-configuration-bundle]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

---
title: aws bedrock-agentcore-control create-api-key-credential-provider
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/create-api-key-credential-provider.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# create-api-key-credential-provider

## Description

Creates a new API key credential provider.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/CreateApiKeyCredentialProvider)

## Synopsis

      create-api-key-credential-provider
    --name <value>
    [--api-key <value>]
    [--api-key-secret-config <value>]
    [--api-key-secret-source <value>]
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

> The name of the API key credential provider. The name must be unique within your account.
>
> Constraints:
>
> - min: `1`
> - max: `128`
> - pattern: `[a-zA-Z0-9\-_]+`

`--api-key` (string)

> The API key to use for authentication. This value is encrypted and stored securely.
>
> Constraints:
>
> - min: `0`
> - max: `65536`

`--api-key-secret-config` (structure)

> A reference to the Amazon Web Services Secrets Manager secret that stores the API key. This includes the secret ID and the JSON key used to extract the API key value from the secret. Required when `apiKeySecretSource` is set to `EXTERNAL` .
>
> secretId -\> (string) \[required\]
>
> > The ID of the Amazon Web Services Secrets Manager secret that stores the secret value.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `2048`
>
> jsonKey -\> (string) \[required\]
>
> > The JSON key used to extract the secret value from the Amazon Web Services Secrets Manager secret.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `128`

Shorthand Syntax:

    secretId=string,jsonKey=string

JSON Syntax:

    {
      "secretId": "string",
      "jsonKey": "string"
    }

`--api-key-secret-source` (string)

> The source type of the API key secret. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in Amazon Web Services Secrets Manager.
>
> Possible values:
>
> - `MANAGED`
> - `EXTERNAL`

`--tags` (map)

> A map of tag keys and values to assign to the API key credential provider. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.
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

apiKeySecretArn -\> (structure)

> The Amazon Resource Name (ARN) of the secret containing the API key.
>
> secretArn -\> (string) \[required\]
>
> > The Amazon Resource Name (ARN) of the secret in Amazon Web Services Secrets Manager.
> >
> > Constraints:
> >
> > - pattern: `arn:(aws|aws-us-gov):secretsmanager:[A-Za-z0-9-]{1,64}:[0-9]{12}:secret:[a-zA-Z0-9-_/+=.@!]+`

apiKeySecretJsonKey -\> (string)

> The JSON key used to extract the API key value from the Amazon Web Services Secrets Manager secret.
>
> Constraints:
>
> - min: `1`
> - max: `128`

apiKeySecretSource -\> (string)

> The source type of the API key secret. Either `MANAGED` if the secret is managed by the service, or `EXTERNAL` if managed by the user in Amazon Web Services Secrets Manager.
>
> Possible values:
>
> - `MANAGED`
> - `EXTERNAL`

name -\> (string)

> The name of the created API key credential provider.
>
> Constraints:
>
> - min: `1`
> - max: `128`
> - pattern: `[a-zA-Z0-9\-_]+`

credentialProviderArn -\> (string)

> The Amazon Resource Name (ARN) of the created API key credential provider.
>
> Constraints:
>
> - pattern: `arn:(aws|aws-us-gov):acps:[A-Za-z0-9-]{1,64}:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+`

- [← create-agent-runtime-endpoint](create-agent-runtime-endpoint.html "previous chapter (use the left arrow)") /
- [create-browser →](create-browser.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](create-browser.html "create-browser") \|
- [previous](create-agent-runtime-endpoint.html "create-agent-runtime-endpoint") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [create-api-key-credential-provider]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

---
title: aws bedrock-agentcore-control rotate-payment-connector-credentials
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/rotate-payment-connector-credentials.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# rotate-payment-connector-credentials

## Description

Replaces the service-managed credentials of a payment connector with newly issued credentials.

Use this operation only for payment connectors with a `provisionMode` of `QUICK_CREATE` . For payment connectors with a `provisionMode` of `MANUAL` , call `UpdatePaymentCredentialProvider` instead after rotating credentials with the payment provider directly.

The rotation finishes before the response is returned, and only one rotation runs at a time for a given payment connector. When it succeeds, the new credential is in effect and the payment connector stays in the `READY` state. When it fails, an error is returned, the payment connector and its existing credential are left unchanged, and you can retry the request.

Rotation replaces the credential on the connector’s credential provider, so every payment connector that uses that provider is affected. Replace any copy of the previous credential that you use outside AgentCore.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/RotatePaymentConnectorCredentials)

## Synopsis

      rotate-payment-connector-credentials
    --payment-manager-id <value>
    --payment-connector-id <value>
    --credentials-to-rotate <value>
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

`--payment-manager-id` (string) \[required\]

> The unique identifier of the parent payment manager.
>
> Constraints:
>
> - min: `12`
> - max: `211`
> - pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`

`--payment-connector-id` (string) \[required\]

> The unique identifier of the payment connector whose credentials you want to rotate.
>
> Constraints:
>
> - min: `12`
> - max: `211`
> - pattern: `([0-9a-z_][-]?){1,100}-[0-9a-z]{10}`

`--credentials-to-rotate` (tagged union structure) \[required\]

> The credentials to rotate. Specify the member that matches the payment connector’s `type` . Each credential that you select is rotated independently.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `coinbaseCDP`.
>
> coinbaseCDP -\> (structure)
>
> > The credentials to rotate for a Coinbase CDP payment connector.
> >
> > secrets -\> (list) \[required\]
> >
> > > The secrets to rotate. Specify at least one value. Each secret that you specify is rotated independently.
> > >
> > > - `API_KEY` - The API key that the payment connector uses to call Coinbase CDP. Rotate it as routine maintenance, or if you suspect that it is compromised.
> > > - `WALLET_SECRET` - The wallet secret that signs transactions. Rotate it only if it is lost or compromised. Coinbase CDP allows one wallet secret per project, so it is replaced in place and signing can be briefly interrupted.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > >
> > > (string)
> > >
> > > > Possible values:
> > > >
> > > > - `API_KEY`
> > > > - `WALLET_SECRET`

Shorthand Syntax:

    coinbaseCDP={secrets=[string,string]}

JSON Syntax:

    {
      "coinbaseCDP": {
        "secrets": ["API_KEY"|"WALLET_SECRET", ...]
      }
    }

`--client-token` (string)

> A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don’t specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn’t return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) .
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

paymentConnectorId -\> (string)

> The unique identifier of the payment connector.
>
> Constraints:
>
> - min: `12`
> - max: `211`
> - pattern: `([0-9a-z_][-]?){1,100}-[0-9a-z]{10}`

paymentManagerId -\> (string)

> The unique identifier of the parent payment manager.
>
> Constraints:
>
> - min: `12`
> - max: `211`
> - pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`

lastUpdatedAt -\> (timestamp)

> The timestamp when the payment connector was last updated, which is when the rotation completed.

status -\> (string)

> The current status of the payment connector, which is `READY` after a successful rotation.
>
> Possible values:
>
> - `CREATING`
> - `UPDATING`
> - `DELETING`
> - `READY`
> - `CREATE_FAILED`
> - `UPDATE_FAILED`
> - `DELETE_FAILED`
> - `AWS_MARKETPLACE_SUBSCRIPTION_REQUIRED`
> - `PENDING_AUTHENTICATION`
> - `PROVISIONING`
> - `AUTHENTICATION_EXPIRED`
> - `AUTHENTICATION_FAILED`

- [← put-resource-policy](put-resource-policy.html "previous chapter (use the left arrow)") /
- [set-token-vault-cmk →](set-token-vault-cmk.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](set-token-vault-cmk.html "set-token-vault-cmk") \|
- [previous](put-resource-policy.html "put-resource-policy") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [rotate-payment-connector-credentials]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

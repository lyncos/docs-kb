---
title: aws bedrock-agentcore-control get-payment-connector
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/get-payment-connector.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# get-payment-connector

## Description

Retrieves information about a specific payment connector.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/GetPaymentConnector)

## Synopsis

      get-payment-connector
    --payment-manager-id <value>
    --payment-connector-id <value>
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

> The unique identifier of the payment connector to retrieve.
>
> Constraints:
>
> - min: `12`
> - max: `211`
> - pattern: `([0-9a-z_][-]?){1,100}-[0-9a-z]{10}`

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

name -\> (string)

> The name of the payment connector.
>
> Constraints:
>
> - min: `1`
> - max: `48`
> - pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`

description -\> (string)

> The description of the payment connector.
>
> Constraints:
>
> - min: `1`
> - max: `4096`
> - pattern: `[^\p{C}]*`

type -\> (string)

> The type of the payment connector, which determines the payment provider integration.
>
> Possible values:
>
> - `CoinbaseCDP`
> - `StripePrivy`

provisionMode -\> (string)

> Specifies how the payment connector was provisioned. Payment connectors that were created before this field was available return `MANUAL` .
>
> - `MANUAL` - You provided the credential provider configurations, so you own the credentials. Rotate them with the payment provider, then call `UpdatePaymentCredentialProvider` .
> - `QUICK_CREATE` - AgentCore provisioned the credential provider for you, so the credentials are service-managed. You can rotate them with `RotatePaymentConnectorCredentials` .
>
> Possible values:
>
> - `MANUAL`
> - `QUICK_CREATE`

credentialProviderConfigurations -\> (list)

> The credential provider configurations for the payment connector.
>
> Constraints:
>
> - min: `0`
> - max: `1`
>
> (tagged union structure)
>
> > The credential provider configuration for a payment connector. Specifies the payment provider type and its associated credential provider.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `coinbaseCDP`, `stripePrivy`.
> >
> > coinbaseCDP -\> (structure)
> >
> > > The credential provider configuration for a Coinbase CDP payment connector.
> > >
> > > credentialProviderArn -\> (string) \[required\]
> > >
> > > > The Amazon Resource Name (ARN) of the credential provider that stores the authentication credentials for the payment provider.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `69`
> > > > - max: `2048`
> > > > - pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b|aws-iso-e|aws-iso-f|aws-eusc):(acps|bedrock-agentcore):[A-Za-z0-9-]{1,64}:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/paymentcredentialprovider/[a-zA-Z0-9-.]+`
> >
> > stripePrivy -\> (structure)
> >
> > > The credential provider configuration for a Stripe Privy payment connector.
> > >
> > > credentialProviderArn -\> (string) \[required\]
> > >
> > > > The Amazon Resource Name (ARN) of the credential provider that stores the authentication credentials for the payment provider.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `69`
> > > > - max: `2048`
> > > > - pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b|aws-iso-e|aws-iso-f|aws-eusc):(acps|bedrock-agentcore):[A-Za-z0-9-]{1,64}:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/paymentcredentialprovider/[a-zA-Z0-9-.]+`

createdAt -\> (timestamp)

> The timestamp when the payment connector was created.

lastUpdatedAt -\> (timestamp)

> The timestamp when the payment connector was last updated.

status -\> (string)

> The current status of the payment connector. Possible values include `CREATING` , `READY` , `UPDATING` , `DELETING` , `CREATE_FAILED` , `UPDATE_FAILED` , and `DELETE_FAILED` .
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

authorizationUrl -\> (string)

> The URL that the user must open to complete OAuth consent. This field is only present when the payment connector status is `PENDING_AUTHENTICATION` .
>
> Constraints:
>
> - min: `1`
> - max: `4096`
> - pattern: `https://[^\p{C}]*`

credentialsUpdatedAt -\> (timestamp)

> The timestamp when the payment connector’s current service-managed credentials took effect. It is first set when the credentials are provisioned and is updated by each rotation. This field is present only for payment connectors with a `provisionMode` of `QUICK_CREATE` .

- [← get-online-evaluation-config](get-online-evaluation-config.html "previous chapter (use the left arrow)") /
- [get-payment-credential-provider →](get-payment-credential-provider.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](get-payment-credential-provider.html "get-payment-credential-provider") \|
- [previous](get-online-evaluation-config.html "get-online-evaluation-config") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [get-payment-connector]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

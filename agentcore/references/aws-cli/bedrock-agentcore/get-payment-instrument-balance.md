---
title: aws bedrock-agentcore get-payment-instrument-balance
description: \ [aws . bedrock-agentcore \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore/get-payment-instrument-balance.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore](index.html#cli-aws-bedrock-agentcore) \]

# get-payment-instrument-balance

## Description

Get the balance of a payment instrument.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-2024-02-28/GetPaymentInstrumentBalance)

## Synopsis

      get-payment-instrument-balance
    [--user-id <value>]
    [--agent-name <value>]
    --payment-manager-arn <value>
    --payment-connector-id <value>
    --payment-instrument-id <value>
    --chain <value>
    --token <value>
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

`--user-id` (string)

> The user ID associated with this payment instrument.
>
> Constraints:
>
> - min: `0`
> - max: `120`

`--agent-name` (string)

> The agent name associated with this request, used for observability.
>
> Constraints:
>
> - min: `0`
> - max: `256`

`--payment-manager-arn` (string) \[required\]

> The ARN of the payment manager that owns this payment instrument.
>
> Constraints:
>
> - min: `66`
> - max: `2048`
> - pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`

`--payment-connector-id` (string) \[required\]

> The ID of the payment connector associated with this instrument.
>
> Constraints:
>
> - min: `12`
> - max: `211`
> - pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`

`--payment-instrument-id` (string) \[required\]

> The ID of the payment instrument to query balance for.
>
> Constraints:
>
> - min: `34`
> - max: `34`
> - pattern: `payment-instrument-[0-9a-zA-Z-]{15}`

`--chain` (string) \[required\]

> The specific blockchain chain to query balance on. Required because balances are chain-specific.
>
> Possible values:
>
> - `BASE`
> - `BASE_SEPOLIA`
> - `ETHEREUM`
> - `SOLANA`
> - `SOLANA_DEVNET`

`--token` (string) \[required\]

> The token to query balance for. Only tokens supported for X402 payments are returned.
>
> Possible values:
>
> - `USDC`

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

paymentInstrumentId -\> (string)

> The ID of the payment instrument.
>
> Constraints:
>
> - min: `34`
> - max: `34`
> - pattern: `payment-instrument-[0-9a-zA-Z-]{15}`

tokenBalance -\> (structure)

> The balance of the supported token on the requested chain.
>
> amount -\> (string) \[required\]
>
> > Raw balance in the smallest denomination (e.g., USDC base units where 1 USDC = 1000000).
>
> decimals -\> (integer) \[required\]
>
> > Number of decimal places for the token (e.g., 6 for USDC).
>
> token -\> (string) \[required\]
>
> > The supported token for this balance.
> >
> > Possible values:
> >
> > - `USDC`
>
> network -\> (string) \[required\]
>
> > The blockchain network family (ETHEREUM or SOLANA).
> >
> > Possible values:
> >
> > - `ETHEREUM`
> > - `SOLANA`
>
> chain -\> (string) \[required\]
>
> > The specific blockchain chain.
> >
> > Possible values:
> >
> > - `BASE`
> > - `BASE_SEPOLIA`
> > - `ETHEREUM`
> > - `SOLANA`
> > - `SOLANA_DEVNET`

- [← get-payment-instrument](get-payment-instrument.html "previous chapter (use the left arrow)") /
- [get-payment-session →](get-payment-session.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](get-payment-session.html "get-payment-session") \|
- [previous](get-payment-instrument.html "get-payment-instrument") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore](index.html) »
- [get-payment-instrument-balance]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

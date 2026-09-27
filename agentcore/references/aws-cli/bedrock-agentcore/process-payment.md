---
title: aws bedrock-agentcore process-payment
description: \ [aws . bedrock-agentcore \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore/process-payment.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore](index.html#cli-aws-bedrock-agentcore) \]

# process-payment

## Description

Processes a payment using a payment instrument within a payment session.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-2024-02-28/ProcessPayment)

`process-payment` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

      process-payment
    [--user-id <value>]
    [--agent-name <value>]
    --payment-manager-arn <value>
    --payment-session-id <value>
    --payment-instrument-id <value>
    --payment-type <value>
    --payment-input <value>
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

`--user-id` (string)

> The user ID associated with this payment.
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

> The ARN of the payment manager.
>
> Constraints:
>
> - min: `66`
> - max: `2048`
> - pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`

`--payment-session-id` (string) \[required\]

> The ID of the payment session.
>
> Constraints:
>
> - min: `31`
> - max: `31`
> - pattern: `payment-session-[0-9a-zA-Z-]{15}`

`--payment-instrument-id` (string) \[required\]

> The ID of the payment instrument to use.
>
> Constraints:
>
> - min: `34`
> - max: `34`
> - pattern: `payment-instrument-[0-9a-zA-Z-]{15}`

`--payment-type` (string) \[required\]

> The type of payment to process.
>
> Possible values:
>
> - `CRYPTO_X402`
> - `MPP`

`--payment-input` (tagged union structure) \[required\]

> The payment input details specific to the payment type.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `cryptoX402`, `mpp`.
>
> cryptoX402 -\> (structure)
>
> > Input for a crypto X402 payment.
> >
> > version -\> (string) \[required\]
> >
> > > The version of the X402 protocol.
> >
> > payload -\> (document) \[required\]
> >
> > > The X402 payment payload.
> >
> > permit2AllowanceLimit -\> (string)
> >
> > > The maximum on-chain Permit2 allowance to grant before signing the payment authorization, in the asset’s smallest denomination. This field is valid only for the `upto` (metered) scheme; supplying it for the `exact` scheme returns a validation error.
> > >
> > > When set, the service approves an ERC-20 allowance for this amount before processing the payment. The approval sets, rather than adds to, the wallet’s allowance. Set this field only when the wallet needs approving, for example on its first `upto` payment, to avoid a redundant on-chain transaction. Omit the field to skip allowance handling. This is the default, and the only behavior for the `exact` scheme.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `78`
> > > - pattern: `[0-9]+`
>
> mpp -\> (structure)
>
> > Contains the payment challenge from a 402 Payment Required response. Forward the raw `WWW-Authenticate:`` ``Payment` header value verbatim. In response, you receive a payment credential that satisfies the challenge. Provide exactly one challenge per request.
> >
> > version -\> (string) \[required\]
> >
> > > The MPP protocol version, for example “1” or “2”.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `10`
> > > - pattern: `[0-9]+`
> >
> > wwwAuthenticateHeaders -\> (list) \[required\]
> >
> > > The raw `WWW-Authenticate:`` ``Payment` header value from the 402 response, passed verbatim. Provide exactly one entry. The service uses this value to generate the payment credential.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `1`
> > >
> > > (string)
> > >
> > > > A raw `WWW-Authenticate:`` ``Payment` header value from a 402 response, containing RFC 9110 auth-params such as `id` , `realm` , `method` , `intent` , and `request` . Pass this value in the request body, not as an HTTP header.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `16384`
> >
> > buyerPaysGasFees -\> (boolean)
> >
> > > Authorizes the service to sign a payment whose blockchain network (gas) fees are charged to your wallet, on top of the payment amount.
> > >
> > > The challenge indicates who sponsors the network fees. When the challenge does not sponsor them, the service signs the payment only if this field is `true` . Otherwise it returns a validation error, so you can decide whether to pay the fees or obtain a challenge that sponsors them.
> > >
> > > Optional. When omitted or `false` , you decline to pay network fees. This field has no effect on challenges that already sponsor the fees.

Shorthand Syntax:

    cryptoX402={version=string,permit2AllowanceLimit=string},mpp={version=string,wwwAuthenticateHeaders=[string,string],buyerPaysGasFees=boolean}

JSON Syntax:

    {
      "cryptoX402": {
        "version": "string",
        "payload": {...},
        "permit2AllowanceLimit": "string"
      },
      "mpp": {
        "version": "string",
        "wwwAuthenticateHeaders": ["string", ...],
        "buyerPaysGasFees": true|false
      }
    }

`--client-token` (string)

> A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
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

processPaymentId -\> (string)

> The unique identifier of the processed payment.
>
> Constraints:
>
> - min: `36`
> - max: `36`
> - pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`

paymentManagerArn -\> (string)

> The ARN of the payment manager.
>
> Constraints:
>
> - min: `66`
> - max: `2048`
> - pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`

paymentSessionId -\> (string)

> The ID of the payment session used.
>
> Constraints:
>
> - min: `31`
> - max: `31`
> - pattern: `payment-session-[0-9a-zA-Z-]{15}`

paymentInstrumentId -\> (string)

> The ID of the payment instrument used.
>
> Constraints:
>
> - min: `34`
> - max: `34`
> - pattern: `payment-instrument-[0-9a-zA-Z-]{15}`

paymentType -\> (string)

> The type of payment processed.
>
> Possible values:
>
> - `CRYPTO_X402`
> - `MPP`

status -\> (string)

> The status of the payment.
>
> Possible values:
>
> - `PROOF_GENERATED`

paymentOutput -\> (tagged union structure)

> The payment output details specific to the payment type.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `cryptoX402`, `mpp`.
>
> cryptoX402 -\> (structure)
>
> > Output from a crypto X402 payment.
> >
> > version -\> (string) \[required\]
> >
> > > The version of the X402 protocol.
> >
> > payload -\> (document) \[required\]
> >
> > > The X402 payment response payload.
>
> mpp -\> (structure)
>
> > Contains the payment credential, ready to retry the request.
> >
> > version -\> (string) \[required\]
> >
> > > The MPP protocol version, for example “1” or “2”.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `10`
> > > - pattern: `[0-9]+`
> >
> > selectedPaymentId -\> (string) \[required\]
> >
> > > The id of the challenge that was paid, echoed from the input challenge so you can correlate the result without decoding the credential.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `512`
> >
> > paymentCredential -\> (string) \[required\]
> >
> > > Ready-to-send value for the `Authorization` header, in the form “Payment \<base64url-token\>”. Attach this header and retry the original request. To inspect the full credential, base64url-decode the token.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `32768`

createdAt -\> (timestamp)

> The timestamp when the payment was created.

updatedAt -\> (timestamp)

> The timestamp when the payment was last updated.

- [← list-sessions](list-sessions.html "previous chapter (use the left arrow)") /
- [retrieve-memory-records →](retrieve-memory-records.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](retrieve-memory-records.html "retrieve-memory-records") \|
- [previous](list-sessions.html "list-sessions") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore](index.html) »
- [process-payment]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

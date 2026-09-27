---
title: aws bedrock-agentcore create-payment-instrument
description: \ [aws . bedrock-agentcore \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore/create-payment-instrument.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore](index.html#cli-aws-bedrock-agentcore) \]

# create-payment-instrument

## Description

Create a new payment instrument for a connector.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-2024-02-28/CreatePaymentInstrument)

## Synopsis

      create-payment-instrument
    [--user-id <value>]
    [--agent-name <value>]
    --payment-manager-arn <value>
    --payment-connector-id <value>
    --payment-instrument-type <value>
    --payment-instrument-details <value>
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

> The ID of the payment connector to use for this instrument.
>
> Constraints:
>
> - min: `12`
> - max: `211`
> - pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`

`--payment-instrument-type` (string) \[required\]

> The type of payment instrument being created.
>
> Possible values:
>
> - `EMBEDDED_CRYPTO_WALLET`

`--payment-instrument-details` (tagged union structure) \[required\]

> The details of the payment instrument.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `embeddedCryptoWallet`.
>
> embeddedCryptoWallet -\> (structure)
>
> > Embedded crypto wallet managed directly by end user.
> >
> > network -\> (string) \[required\]
> >
> > > The blockchain network for this embedded crypto wallet. Supported networks: ETHEREUM, SOLANA.
> > >
> > > Possible values:
> > >
> > > - `ETHEREUM`
> > > - `SOLANA`
> >
> > linkedAccounts -\> (list) \[required\]
> >
> > > List of linked accounts linked to this wallet. Each represents a way the end user can authenticate to this wallet.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `1`
> > >
> > > (tagged union structure)
> > >
> > > > Represents different linked accounts that can be linked to an embedded wallet. Supports email, SMS, JWT, and OAuth2 approaches.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `email`, `sms`, `developerJwt`, `oAuth2`.
> > > >
> > > > email -\> (structure)
> > > >
> > > > > Email-based linked account.
> > > > >
> > > > > emailAddress -\> (string) \[required\]
> > > > >
> > > > > > The email address used for the linked account. Must be a valid email format.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `254`
> > > > > > - pattern: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`
> > > >
> > > > sms -\> (structure)
> > > >
> > > > > SMS-based linked account using phone number.
> > > > >
> > > > > phoneNumber -\> (string) \[required\]
> > > > >
> > > > > > The phone number in E.164 format (e.g., +1234567890).
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `3`
> > > > > > - max: `16`
> > > > > > - pattern: `\+[1-9]\d{1,14}`
> > > >
> > > > developerJwt -\> (structure)
> > > >
> > > > > Developer JWT linked account with key ID and subject.
> > > > >
> > > > > kid -\> (string) \[required\]
> > > > >
> > > > > > The key ID (kid) from the JWT header. Identifies which key was used to sign the JWT.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `255`
> > > > > > - pattern: `[a-zA-Z0-9_-]{1,255}`
> > > > >
> > > > > sub -\> (string) \[required\]
> > > > >
> > > > > > The subject (sub) claim from the JWT payload. Identifies the principal that is the subject of the JWT.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `255`
> > > >
> > > > oAuth2 -\> (tagged union structure)
> > > >
> > > > > OAuth2 provider linked account (Google, Apple, X, Telegram, GitHub).
> > > > >
> > > > > ### Note
> > > > >
> > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `google`, `apple`, `x`, `telegram`, `github`.
> > > > >
> > > > > google -\> (structure)
> > > > >
> > > > > > Google OAuth2 authentication.
> > > > > >
> > > > > > sub -\> (string) \[required\]
> > > > > >
> > > > > > > The subject (sub) claim from the OAuth2 provider. Uniquely identifies the user at the provider.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> > > > > >
> > > > > > emailAddress -\> (string)
> > > > > >
> > > > > > > The email address from the OAuth2 provider.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `254`
> > > > > > > - pattern: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`
> > > > > >
> > > > > > name -\> (string)
> > > > > >
> > > > > > > The user’s name from the OAuth2 provider.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> > > > > >
> > > > > > username -\> (string)
> > > > > >
> > > > > > > The username from the OAuth2 provider.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> > > > >
> > > > > apple -\> (structure)
> > > > >
> > > > > > Apple OAuth2 authentication.
> > > > > >
> > > > > > sub -\> (string) \[required\]
> > > > > >
> > > > > > > The subject (sub) claim from the OAuth2 provider. Uniquely identifies the user at the provider.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> > > > > >
> > > > > > emailAddress -\> (string)
> > > > > >
> > > > > > > The email address from the OAuth2 provider.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `254`
> > > > > > > - pattern: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`
> > > > > >
> > > > > > name -\> (string)
> > > > > >
> > > > > > > The user’s name from the OAuth2 provider.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> > > > > >
> > > > > > username -\> (string)
> > > > > >
> > > > > > > The username from the OAuth2 provider.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> > > > >
> > > > > x -\> (structure)
> > > > >
> > > > > > X (formerly Twitter) OAuth2 authentication.
> > > > > >
> > > > > > sub -\> (string) \[required\]
> > > > > >
> > > > > > > The subject (sub) claim from the OAuth2 provider. Uniquely identifies the user at the provider.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> > > > > >
> > > > > > emailAddress -\> (string)
> > > > > >
> > > > > > > The email address from the OAuth2 provider.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `254`
> > > > > > > - pattern: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`
> > > > > >
> > > > > > name -\> (string)
> > > > > >
> > > > > > > The user’s name from the OAuth2 provider.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> > > > > >
> > > > > > username -\> (string)
> > > > > >
> > > > > > > The username from the OAuth2 provider.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> > > > >
> > > > > telegram -\> (structure)
> > > > >
> > > > > > Telegram OAuth2 authentication.
> > > > > >
> > > > > > sub -\> (string) \[required\]
> > > > > >
> > > > > > > The subject (sub) claim from the OAuth2 provider. Uniquely identifies the user at the provider.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> > > > > >
> > > > > > emailAddress -\> (string)
> > > > > >
> > > > > > > The email address from the OAuth2 provider.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `254`
> > > > > > > - pattern: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`
> > > > > >
> > > > > > name -\> (string)
> > > > > >
> > > > > > > The user’s name from the OAuth2 provider.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> > > > > >
> > > > > > username -\> (string)
> > > > > >
> > > > > > > The username from the OAuth2 provider.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> > > > >
> > > > > github -\> (structure)
> > > > >
> > > > > > GitHub OAuth2 authentication.
> > > > > >
> > > > > > sub -\> (string) \[required\]
> > > > > >
> > > > > > > The subject (sub) claim from the OAuth2 provider. Uniquely identifies the user at the provider.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> > > > > >
> > > > > > emailAddress -\> (string)
> > > > > >
> > > > > > > The email address from the OAuth2 provider.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `254`
> > > > > > > - pattern: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`
> > > > > >
> > > > > > name -\> (string)
> > > > > >
> > > > > > > The user’s name from the OAuth2 provider.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> > > > > >
> > > > > > username -\> (string)
> > > > > >
> > > > > > > The username from the OAuth2 provider.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> >
> > walletAddress -\> (string)
> >
> > > The wallet address on the specified blockchain network.
> >
> > redirectUrl -\> (string)
> >
> > > URL for the end user to complete a provider-specific action such as wallet linking or onboarding.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `2048`

JSON Syntax:

    {
      "embeddedCryptoWallet": {
        "network": "ETHEREUM"|"SOLANA",
        "linkedAccounts": [
          {
            "email": {
              "emailAddress": "string"
            },
            "sms": {
              "phoneNumber": "string"
            },
            "developerJwt": {
              "kid": "string",
              "sub": "string"
            },
            "oAuth2": {
              "google": {
                "sub": "string",
                "emailAddress": "string",
                "name": "string",
                "username": "string"
              },
              "apple": {
                "sub": "string",
                "emailAddress": "string",
                "name": "string",
                "username": "string"
              },
              "x": {
                "sub": "string",
                "emailAddress": "string",
                "name": "string",
                "username": "string"
              },
              "telegram": {
                "sub": "string",
                "emailAddress": "string",
                "name": "string",
                "username": "string"
              },
              "github": {
                "sub": "string",
                "emailAddress": "string",
                "name": "string",
                "username": "string"
              }
            }
          }
          ...
        ],
        "walletAddress": "string",
        "redirectUrl": "string"
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

paymentInstrument -\> (structure)

> The created payment instrument.
>
> paymentInstrumentId -\> (string) \[required\]
>
> > The unique identifier for this payment instrument.
> >
> > Constraints:
> >
> > - min: `34`
> > - max: `34`
> > - pattern: `payment-instrument-[0-9a-zA-Z-]{15}`
>
> paymentManagerArn -\> (string) \[required\]
>
> > The ARN of the payment manager that owns this payment instrument.
> >
> > Constraints:
> >
> > - min: `66`
> > - max: `2048`
> > - pattern: `arn:(aws|aws-[a-z0-9-]+):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/[a-z0-9]([a-z0-9-]{0,47}[a-z0-9])?-[a-z0-9]{10}`
>
> paymentConnectorId -\> (string) \[required\]
>
> > The ID of the payment connector associated with this instrument.
> >
> > Constraints:
> >
> > - min: `12`
> > - max: `211`
> > - pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`
>
> userId -\> (string) \[required\]
>
> > The user ID associated with this payment instrument.
> >
> > Constraints:
> >
> > - min: `0`
> > - max: `120`
>
> paymentInstrumentType -\> (string) \[required\]
>
> > The type of payment instrument (e.g., EMBEDDED_CRYPTO_WALLET).
> >
> > Possible values:
> >
> > - `EMBEDDED_CRYPTO_WALLET`
>
> paymentInstrumentDetails -\> (tagged union structure) \[required\]
>
> > The details specific to the payment instrument type.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `embeddedCryptoWallet`.
> >
> > embeddedCryptoWallet -\> (structure)
> >
> > > Embedded crypto wallet managed directly by end user.
> > >
> > > network -\> (string) \[required\]
> > >
> > > > The blockchain network for this embedded crypto wallet. Supported networks: ETHEREUM, SOLANA.
> > > >
> > > > Possible values:
> > > >
> > > > - `ETHEREUM`
> > > > - `SOLANA`
> > >
> > > linkedAccounts -\> (list) \[required\]
> > >
> > > > List of linked accounts linked to this wallet. Each represents a way the end user can authenticate to this wallet.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0`
> > > > - max: `1`
> > > >
> > > > (tagged union structure)
> > > >
> > > > > Represents different linked accounts that can be linked to an embedded wallet. Supports email, SMS, JWT, and OAuth2 approaches.
> > > > >
> > > > > ### Note
> > > > >
> > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `email`, `sms`, `developerJwt`, `oAuth2`.
> > > > >
> > > > > email -\> (structure)
> > > > >
> > > > > > Email-based linked account.
> > > > > >
> > > > > > emailAddress -\> (string) \[required\]
> > > > > >
> > > > > > > The email address used for the linked account. Must be a valid email format.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `254`
> > > > > > > - pattern: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`
> > > > >
> > > > > sms -\> (structure)
> > > > >
> > > > > > SMS-based linked account using phone number.
> > > > > >
> > > > > > phoneNumber -\> (string) \[required\]
> > > > > >
> > > > > > > The phone number in E.164 format (e.g., +1234567890).
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `3`
> > > > > > > - max: `16`
> > > > > > > - pattern: `\+[1-9]\d{1,14}`
> > > > >
> > > > > developerJwt -\> (structure)
> > > > >
> > > > > > Developer JWT linked account with key ID and subject.
> > > > > >
> > > > > > kid -\> (string) \[required\]
> > > > > >
> > > > > > > The key ID (kid) from the JWT header. Identifies which key was used to sign the JWT.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> > > > > > > - pattern: `[a-zA-Z0-9_-]{1,255}`
> > > > > >
> > > > > > sub -\> (string) \[required\]
> > > > > >
> > > > > > > The subject (sub) claim from the JWT payload. Identifies the principal that is the subject of the JWT.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> > > > >
> > > > > oAuth2 -\> (tagged union structure)
> > > > >
> > > > > > OAuth2 provider linked account (Google, Apple, X, Telegram, GitHub).
> > > > > >
> > > > > > ### Note
> > > > > >
> > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `google`, `apple`, `x`, `telegram`, `github`.
> > > > > >
> > > > > > google -\> (structure)
> > > > > >
> > > > > > > Google OAuth2 authentication.
> > > > > > >
> > > > > > > sub -\> (string) \[required\]
> > > > > > >
> > > > > > > > The subject (sub) claim from the OAuth2 provider. Uniquely identifies the user at the provider.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > > >
> > > > > > > emailAddress -\> (string)
> > > > > > >
> > > > > > > > The email address from the OAuth2 provider.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `254`
> > > > > > > > - pattern: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`
> > > > > > >
> > > > > > > name -\> (string)
> > > > > > >
> > > > > > > > The user’s name from the OAuth2 provider.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > > >
> > > > > > > username -\> (string)
> > > > > > >
> > > > > > > > The username from the OAuth2 provider.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > >
> > > > > > apple -\> (structure)
> > > > > >
> > > > > > > Apple OAuth2 authentication.
> > > > > > >
> > > > > > > sub -\> (string) \[required\]
> > > > > > >
> > > > > > > > The subject (sub) claim from the OAuth2 provider. Uniquely identifies the user at the provider.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > > >
> > > > > > > emailAddress -\> (string)
> > > > > > >
> > > > > > > > The email address from the OAuth2 provider.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `254`
> > > > > > > > - pattern: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`
> > > > > > >
> > > > > > > name -\> (string)
> > > > > > >
> > > > > > > > The user’s name from the OAuth2 provider.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > > >
> > > > > > > username -\> (string)
> > > > > > >
> > > > > > > > The username from the OAuth2 provider.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > >
> > > > > > x -\> (structure)
> > > > > >
> > > > > > > X (formerly Twitter) OAuth2 authentication.
> > > > > > >
> > > > > > > sub -\> (string) \[required\]
> > > > > > >
> > > > > > > > The subject (sub) claim from the OAuth2 provider. Uniquely identifies the user at the provider.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > > >
> > > > > > > emailAddress -\> (string)
> > > > > > >
> > > > > > > > The email address from the OAuth2 provider.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `254`
> > > > > > > > - pattern: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`
> > > > > > >
> > > > > > > name -\> (string)
> > > > > > >
> > > > > > > > The user’s name from the OAuth2 provider.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > > >
> > > > > > > username -\> (string)
> > > > > > >
> > > > > > > > The username from the OAuth2 provider.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > >
> > > > > > telegram -\> (structure)
> > > > > >
> > > > > > > Telegram OAuth2 authentication.
> > > > > > >
> > > > > > > sub -\> (string) \[required\]
> > > > > > >
> > > > > > > > The subject (sub) claim from the OAuth2 provider. Uniquely identifies the user at the provider.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > > >
> > > > > > > emailAddress -\> (string)
> > > > > > >
> > > > > > > > The email address from the OAuth2 provider.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `254`
> > > > > > > > - pattern: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`
> > > > > > >
> > > > > > > name -\> (string)
> > > > > > >
> > > > > > > > The user’s name from the OAuth2 provider.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > > >
> > > > > > > username -\> (string)
> > > > > > >
> > > > > > > > The username from the OAuth2 provider.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > >
> > > > > > github -\> (structure)
> > > > > >
> > > > > > > GitHub OAuth2 authentication.
> > > > > > >
> > > > > > > sub -\> (string) \[required\]
> > > > > > >
> > > > > > > > The subject (sub) claim from the OAuth2 provider. Uniquely identifies the user at the provider.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > > >
> > > > > > > emailAddress -\> (string)
> > > > > > >
> > > > > > > > The email address from the OAuth2 provider.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `254`
> > > > > > > > - pattern: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`
> > > > > > >
> > > > > > > name -\> (string)
> > > > > > >
> > > > > > > > The user’s name from the OAuth2 provider.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > > >
> > > > > > > username -\> (string)
> > > > > > >
> > > > > > > > The username from the OAuth2 provider.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > >
> > > walletAddress -\> (string)
> > >
> > > > The wallet address on the specified blockchain network.
> > >
> > > redirectUrl -\> (string)
> > >
> > > > URL for the end user to complete a provider-specific action such as wallet linking or onboarding.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0`
> > > > - max: `2048`
>
> createdAt -\> (timestamp) \[required\]
>
> > The timestamp when this payment instrument was created.
>
> status -\> (string) \[required\]
>
> > The current status of this payment instrument.
> >
> > Possible values:
> >
> > - `INITIATED`
> > - `ACTIVE`
> > - `FAILED`
> > - `DELETED`
> > - `BLOCKED`
>
> updatedAt -\> (timestamp) \[required\]
>
> > The timestamp when this payment instrument was last updated.

- [← create-event](create-event.html "previous chapter (use the left arrow)") /
- [create-payment-session →](create-payment-session.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](create-payment-session.html "create-payment-session") \|
- [previous](create-event.html "create-event") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore](index.html) »
- [create-payment-instrument]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

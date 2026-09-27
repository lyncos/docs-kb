---
title: aws bedrock-agentcore get-resource-payment-token
description: \ [aws . bedrock-agentcore \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore/get-resource-payment-token.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore](index.html#cli-aws-bedrock-agentcore) \]

# get-resource-payment-token

## Description

Generates authentication tokens for payment providers that use vendor-specific authentication mechanisms.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-2024-02-28/GetResourcePaymentToken)

## Synopsis

      get-resource-payment-token
    --workload-identity-token <value>
    --resource-credential-provider-name <value>
    --payment-token-request <value>
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

`--workload-identity-token` (string) \[required\]

> Workload access token for authorization.
>
> Constraints:
>
> - min: `1`
> - max: `131072`

`--resource-credential-provider-name` (string) \[required\]

> Name of the payment credential provider to use.
>
> Constraints:
>
> - min: `1`
> - max: `128`
> - pattern: `[a-zA-Z0-9\-_]+`

`--payment-token-request` (tagged union structure) \[required\]

> Vendor-specific token request input. Contains all request parameters in a type-safe, vendor-specific structure.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `coinbaseCdpTokenRequest`, `stripePrivyTokenRequest`.
>
> coinbaseCdpTokenRequest -\> (structure)
>
> > The Coinbase CDP token request.
> >
> > requestMethod -\> (string) \[required\]
> >
> > > The HTTP method for the payment API request.
> > >
> > > Possible values:
> > >
> > > - `GET`
> > > - `POST`
> > > - `PUT`
> > > - `DELETE`
> > > - `PATCH`
> >
> > requestHost -\> (string)
> >
> > > The host for the payment API request. Defaults to “api.cdp.coinbase.com”.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `256`
> > > - pattern: `[a-zA-Z0-9\-\.]+`
> >
> > requestPath -\> (string) \[required\]
> >
> > > The path of the payment API request.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `2048`
> > > - pattern: `/[a-zA-Z0-9/_\-\.~%?=&]+`
> >
> > includeWalletAuthToken -\> (boolean)
> >
> > > Set to true for wallet write operations (requires walletSecret configured).
> >
> > requestBody -\> (string)
> >
> > > Request body JSON — used to generate wallet auth JWT.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `16384`
> > > - pattern: `[\u0009\u000A\u000D\u0020-\u007E]+`
>
> stripePrivyTokenRequest -\> (structure)
>
> > The Stripe Privy token request.
> >
> > requestHost -\> (string)
> >
> > > The host for the Privy API request. Defaults to “api.privy.io”.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `256`
> > > - pattern: `[a-zA-Z0-9\-\.]+`
> >
> > requestPath -\> (string) \[required\]
> >
> > > The path of the Stripe Privy API request.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `2048`
> > > - pattern: `/[a-zA-Z0-9/_\-\.~%?=&]+`
> >
> > requestBody -\> (string) \[required\]
> >
> > > Request body JSON for the Privy API call.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `16384`
> > > - pattern: `[\u0009\u000A\u000D\u0020-\u007E]+`
> >
> > includeAuthorizationSignature -\> (boolean)
> >
> > > Set to true to generate privy-authorization-signature.

Shorthand Syntax:

    coinbaseCdpTokenRequest={requestMethod=string,requestHost=string,requestPath=string,includeWalletAuthToken=boolean,requestBody=string},stripePrivyTokenRequest={requestHost=string,requestPath=string,requestBody=string,includeAuthorizationSignature=boolean}

JSON Syntax:

    {
      "coinbaseCdpTokenRequest": {
        "requestMethod": "GET"|"POST"|"PUT"|"DELETE"|"PATCH",
        "requestHost": "string",
        "requestPath": "string",
        "includeWalletAuthToken": true|false,
        "requestBody": "string"
      },
      "stripePrivyTokenRequest": {
        "requestHost": "string",
        "requestPath": "string",
        "requestBody": "string",
        "includeAuthorizationSignature": true|false
      }
    }

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

paymentTokenResponse -\> (tagged union structure)

> Vendor-specific token response output. Contains all response data in a type-safe, vendor-specific structure.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `coinbaseCdpTokenResponse`, `stripePrivyTokenResponse`.
>
> coinbaseCdpTokenResponse -\> (structure)
>
> > The Coinbase CDP token response.
> >
> > bearerToken -\> (string) \[required\]
> >
> > > Bearer Token for Authorization header.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `8192`
> >
> > walletAuthToken -\> (string)
> >
> > > Wallet Auth Token for X-Wallet-Auth header.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `8192`
>
> stripePrivyTokenResponse -\> (structure)
>
> > The Stripe Privy token response.
> >
> > authorizationSignature -\> (string)
> >
> > > Base64-encoded ECDSA P-256 authorization signature (only present when includeAuthorizationSignature is true).
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `8192`
> >
> > requestExpiry -\> (long)
> >
> > > Unix timestamp in milliseconds when the authorization signature expires.
> >
> > appId -\> (string) \[required\]
> >
> > > The Privy app ID for the privy-app-id header.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `512`
> > > - pattern: `[a-zA-Z0-9\-_]+`
> >
> > basicAuthToken -\> (string) \[required\]
> >
> > > Base64-encoded Basic Auth token (appId:appSecret) for the Authorization header.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `8192`

- [← get-resource-oauth2-token](get-resource-oauth2-token.html "previous chapter (use the left arrow)") /
- [get-workload-access-token →](get-workload-access-token.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](get-workload-access-token.html "get-workload-access-token") \|
- [previous](get-resource-oauth2-token.html "get-resource-oauth2-token") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore](index.html) »
- [get-resource-payment-token]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

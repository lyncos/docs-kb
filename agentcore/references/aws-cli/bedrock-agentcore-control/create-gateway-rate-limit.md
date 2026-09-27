---
title: aws bedrock-agentcore-control create-gateway-rate-limit
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/create-gateway-rate-limit.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# create-gateway-rate-limit

## Description

Creates a rate limit for a gateway. Rate limits define throttling rules for each dimension that control request rates, token consumption rates, and concurrent connections through the gateway.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/CreateGatewayRateLimit)

## Synopsis

      create-gateway-rate-limit
    --gateway-identifier <value>
    [--client-token <value>]
    [--rate-limit-id <value>]
    [--description <value>]
    --dimension-keys <value>
    --entries <value>
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

`--gateway-identifier` (string) \[required\]

> The unique identifier of the gateway to create the rate limit for.
>
> Constraints:
>
> - pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`

`--client-token` (string)

> A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don’t specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn’t return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) .
>
> Constraints:
>
> - min: `33`
> - max: `256`
> - pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`

`--rate-limit-id` (string)

> An optional customer-defined identifier for the rate limit. If not provided, the system generates one.
>
> Constraints:
>
> - min: `2`
> - max: `64`
> - pattern: `[a-zA-Z0-9][a-zA-Z0-9\-_\.]{0,62}[a-zA-Z0-9]`

`--description` (string)

> An optional human-readable description for this rate limit. If not provided, the rate limit is created without a description.
>
> Constraints:
>
> - min: `0`
> - max: `512`

`--dimension-keys` (list) \[required\]

> The ordered list of dimension key names that define the scope of this rate limit. Must be unique per gateway—no two rate limits can share the same dimension keys.
>
> Constraints:
>
> - min: `1`
> - max: `10`
>
> (string)
>
> > A dimension key specifying the scope dimension for rate limiting.
> >
> > Allowed values: `targetName` , `toolName` , `qualifiedModelId` , or context-path expressions: `$.context.iam.principal` , `$.context.iam.sourceIdentity` , `$.context.jwt.<claim>` where `<claim>` is a JWT claim name (for example, `$.context.jwt.sub` ). Validated server-side to enforce allowed prefixes and patterns.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `80`
> > - pattern: `(targetName|toolName|qualifiedModelId|\$\.context\.iam\.principal|\$\.context\.iam\.sourceIdentity|\$\.context\.jwt\.[a-zA-Z_][a-zA-Z0-9_\-\.]{0,61}[a-zA-Z0-9_])`

Syntax:

    "string" "string" ...

`--entries` (list) \[required\]

> The rule entries that map dimension values to rate configurations.
>
> Constraints:
>
> - min: `1`
> - max: `1000`
>
> (structure)
>
> > A single rule entry within a rate limit that maps dimension values to rate configurations. Each entry defines the rate limits for a specific combination of dimension values.
> >
> > dimensions -\> (map) \[required\]
> >
> > > A map of dimension names to dimension values for this rule entry. Keys must match the parent rate limit’s dimension keys. Values may use `*` as a wildcard, but only in trailing positions based on the dimension keys ordering.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `10`
> > >
> > > key -\> (string)
> > >
> > > > A dimension key specifying the scope dimension for rate limiting.
> > > >
> > > > Allowed values: `targetName` , `toolName` , `qualifiedModelId` , or context-path expressions: `$.context.iam.principal` , `$.context.iam.sourceIdentity` , `$.context.jwt.<claim>` where `<claim>` is a JWT claim name (for example, `$.context.jwt.sub` ). Validated server-side to enforce allowed prefixes and patterns.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `80`
> > > > - pattern: `(targetName|toolName|qualifiedModelId|\$\.context\.iam\.principal|\$\.context\.iam\.sourceIdentity|\$\.context\.jwt\.[a-zA-Z_][a-zA-Z0-9_\-\.]{0,61}[a-zA-Z0-9_])`
> > >
> > > value -\> (string)
> > >
> > > > A dimension value in a rule entry (exact value or `*` wildcard).
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `256`
> >
> > requests -\> (list)
> >
> > > The request rate limit configuration. Specifies the maximum number of requests allowed per time period.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `1`
> > >
> > > (structure)
> > >
> > > > Contains the rate configuration for a rate limit metric, specifying the allowed rate and time period.
> > > >
> > > > rate -\> (double) \[required\]
> > > >
> > > > > The rate value for the limit. For request limits, this is the number of requests allowed per period. For token limits, this is the number of tokens allowed per period. For connection limits, this is the number of concurrent connections allowed.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `0`
> > > > > - max: `10000000`
> > > >
> > > > period -\> (string) \[required\]
> > > >
> > > > > The time period for the rate limit. Valid values:
> > > > >
> > > > > - `second` —Measures the rate limit over a one-second window.
> > > > > - `minute` —Measures the rate limit over a one-minute window.
> > > > >
> > > > > Possible values:
> > > > >
> > > > > - `second`
> > > > > - `minute`
> >
> > tokens -\> (list)
> >
> > > The token rate limit configuration. Specifies the maximum number of tokens allowed per time period.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `1`
> > >
> > > (structure)
> > >
> > > > Contains the rate configuration for a rate limit metric, specifying the allowed rate and time period.
> > > >
> > > > rate -\> (double) \[required\]
> > > >
> > > > > The rate value for the limit. For request limits, this is the number of requests allowed per period. For token limits, this is the number of tokens allowed per period. For connection limits, this is the number of concurrent connections allowed.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `0`
> > > > > - max: `10000000`
> > > >
> > > > period -\> (string) \[required\]
> > > >
> > > > > The time period for the rate limit. Valid values:
> > > > >
> > > > > - `second` —Measures the rate limit over a one-second window.
> > > > > - `minute` —Measures the rate limit over a one-minute window.
> > > > >
> > > > > Possible values:
> > > > >
> > > > > - `second`
> > > > > - `minute`
> >
> > connections -\> (list)
> >
> > > The connection rate limit configuration. Specifies the maximum number of concurrent connections allowed.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `1`
> > >
> > > (structure)
> > >
> > > > Contains the rate configuration for a rate limit metric, specifying the allowed rate and time period.
> > > >
> > > > rate -\> (double) \[required\]
> > > >
> > > > > The rate value for the limit. For request limits, this is the number of requests allowed per period. For token limits, this is the number of tokens allowed per period. For connection limits, this is the number of concurrent connections allowed.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `0`
> > > > > - max: `10000000`
> > > >
> > > > period -\> (string) \[required\]
> > > >
> > > > > The time period for the rate limit. Valid values:
> > > > >
> > > > > - `second` —Measures the rate limit over a one-second window.
> > > > > - `minute` —Measures the rate limit over a one-minute window.
> > > > >
> > > > > Possible values:
> > > > >
> > > > > - `second`
> > > > > - `minute`

Shorthand Syntax:

    dimensions={KeyName1=string,KeyName2=string},requests=[{rate=double,period=string},{rate=double,period=string}],tokens=[{rate=double,period=string},{rate=double,period=string}],connections=[{rate=double,period=string},{rate=double,period=string}] ...

JSON Syntax:

    [
      {
        "dimensions": {"string": "string"
          ...},
        "requests": [
          {
            "rate": double,
            "period": "second"|"minute"
          }
          ...
        ],
        "tokens": [
          {
            "rate": double,
            "period": "second"|"minute"
          }
          ...
        ],
        "connections": [
          {
            "rate": double,
            "period": "second"|"minute"
          }
          ...
        ]
      }
      ...
    ]

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

rateLimitId -\> (string)

> The unique identifier of the created rate limit.
>
> Constraints:
>
> - min: `2`
> - max: `64`
> - pattern: `[a-zA-Z0-9][a-zA-Z0-9\-_\.]{0,62}[a-zA-Z0-9]`

gatewayIdentifier -\> (string)

> The unique identifier of the gateway.
>
> Constraints:
>
> - pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`

description -\> (string)

> The human-readable description of the rate limit.
>
> Constraints:
>
> - min: `0`
> - max: `512`

dimensionKeys -\> (list)

> The ordered list of dimension key names that define the scope of this rate limit.
>
> Constraints:
>
> - min: `1`
> - max: `10`
>
> (string)
>
> > A dimension key specifying the scope dimension for rate limiting.
> >
> > Allowed values: `targetName` , `toolName` , `qualifiedModelId` , or context-path expressions: `$.context.iam.principal` , `$.context.iam.sourceIdentity` , `$.context.jwt.<claim>` where `<claim>` is a JWT claim name (for example, `$.context.jwt.sub` ). Validated server-side to enforce allowed prefixes and patterns.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `80`
> > - pattern: `(targetName|toolName|qualifiedModelId|\$\.context\.iam\.principal|\$\.context\.iam\.sourceIdentity|\$\.context\.jwt\.[a-zA-Z_][a-zA-Z0-9_\-\.]{0,61}[a-zA-Z0-9_])`

entries -\> (list)

> The list of rule entries that map dimension values to rate configurations.
>
> Constraints:
>
> - min: `1`
> - max: `1000`
>
> (structure)
>
> > A single rule entry within a rate limit that maps dimension values to rate configurations. Each entry defines the rate limits for a specific combination of dimension values.
> >
> > dimensions -\> (map) \[required\]
> >
> > > A map of dimension names to dimension values for this rule entry. Keys must match the parent rate limit’s dimension keys. Values may use `*` as a wildcard, but only in trailing positions based on the dimension keys ordering.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `10`
> > >
> > > key -\> (string)
> > >
> > > > A dimension key specifying the scope dimension for rate limiting.
> > > >
> > > > Allowed values: `targetName` , `toolName` , `qualifiedModelId` , or context-path expressions: `$.context.iam.principal` , `$.context.iam.sourceIdentity` , `$.context.jwt.<claim>` where `<claim>` is a JWT claim name (for example, `$.context.jwt.sub` ). Validated server-side to enforce allowed prefixes and patterns.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `80`
> > > > - pattern: `(targetName|toolName|qualifiedModelId|\$\.context\.iam\.principal|\$\.context\.iam\.sourceIdentity|\$\.context\.jwt\.[a-zA-Z_][a-zA-Z0-9_\-\.]{0,61}[a-zA-Z0-9_])`
> > >
> > > value -\> (string)
> > >
> > > > A dimension value in a rule entry (exact value or `*` wildcard).
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `256`
> >
> > requests -\> (list)
> >
> > > The request rate limit configuration. Specifies the maximum number of requests allowed per time period.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `1`
> > >
> > > (structure)
> > >
> > > > Contains the rate configuration for a rate limit metric, specifying the allowed rate and time period.
> > > >
> > > > rate -\> (double) \[required\]
> > > >
> > > > > The rate value for the limit. For request limits, this is the number of requests allowed per period. For token limits, this is the number of tokens allowed per period. For connection limits, this is the number of concurrent connections allowed.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `0`
> > > > > - max: `10000000`
> > > >
> > > > period -\> (string) \[required\]
> > > >
> > > > > The time period for the rate limit. Valid values:
> > > > >
> > > > > - `second` —Measures the rate limit over a one-second window.
> > > > > - `minute` —Measures the rate limit over a one-minute window.
> > > > >
> > > > > Possible values:
> > > > >
> > > > > - `second`
> > > > > - `minute`
> >
> > tokens -\> (list)
> >
> > > The token rate limit configuration. Specifies the maximum number of tokens allowed per time period.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `1`
> > >
> > > (structure)
> > >
> > > > Contains the rate configuration for a rate limit metric, specifying the allowed rate and time period.
> > > >
> > > > rate -\> (double) \[required\]
> > > >
> > > > > The rate value for the limit. For request limits, this is the number of requests allowed per period. For token limits, this is the number of tokens allowed per period. For connection limits, this is the number of concurrent connections allowed.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `0`
> > > > > - max: `10000000`
> > > >
> > > > period -\> (string) \[required\]
> > > >
> > > > > The time period for the rate limit. Valid values:
> > > > >
> > > > > - `second` —Measures the rate limit over a one-second window.
> > > > > - `minute` —Measures the rate limit over a one-minute window.
> > > > >
> > > > > Possible values:
> > > > >
> > > > > - `second`
> > > > > - `minute`
> >
> > connections -\> (list)
> >
> > > The connection rate limit configuration. Specifies the maximum number of concurrent connections allowed.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `1`
> > >
> > > (structure)
> > >
> > > > Contains the rate configuration for a rate limit metric, specifying the allowed rate and time period.
> > > >
> > > > rate -\> (double) \[required\]
> > > >
> > > > > The rate value for the limit. For request limits, this is the number of requests allowed per period. For token limits, this is the number of tokens allowed per period. For connection limits, this is the number of concurrent connections allowed.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `0`
> > > > > - max: `10000000`
> > > >
> > > > period -\> (string) \[required\]
> > > >
> > > > > The time period for the rate limit. Valid values:
> > > > >
> > > > > - `second` —Measures the rate limit over a one-second window.
> > > > > - `minute` —Measures the rate limit over a one-minute window.
> > > > >
> > > > > Possible values:
> > > > >
> > > > > - `second`
> > > > > - `minute`

status -\> (string)

> The current status of the rate limit.
>
> Possible values:
>
> - `CREATING`
> - `ACTIVE`
> - `UPDATING`
> - `DELETING`

createdAt -\> (timestamp)

> The timestamp when the rate limit was created.

updatedAt -\> (timestamp)

> The timestamp when the rate limit was last updated.

- [← create-gateway](create-gateway.html "previous chapter (use the left arrow)") /
- [create-gateway-rule →](create-gateway-rule.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](create-gateway-rule.html "create-gateway-rule") \|
- [previous](create-gateway.html "create-gateway") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [create-gateway-rate-limit]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

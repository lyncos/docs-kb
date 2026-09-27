---
title: aws bedrock-agentcore-control update-gateway-rule
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/update-gateway-rule.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# update-gateway-rule

## Description

Updates a gateway rule’s priority, conditions, actions, or description.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/UpdateGatewayRule)

## Synopsis

      update-gateway-rule
    --gateway-identifier <value>
    --rule-id <value>
    [--priority <value>]
    [--conditions <value>]
    [--actions <value>]
    [--description <value>]
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

> The identifier of the gateway containing the rule.
>
> Constraints:
>
> - pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`

`--rule-id` (string) \[required\]

> The unique identifier of the rule to update.
>
> Constraints:
>
> - min: `36`
> - max: `36`
> - pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

`--priority` (integer)

> The updated priority of the rule.
>
> Constraints:
>
> - min: `1`
> - max: `1000000`

`--conditions` (list)

> The updated conditions for the rule.
>
> Constraints:
>
> - min: `0`
> - max: `2`
>
> (tagged union structure)
>
> > A condition that determines when a gateway rule applies. Conditions can match on principals or request paths.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `matchPrincipals`, `matchPaths`.
> >
> > matchPrincipals -\> (structure)
> >
> > > A condition that matches on the identity of the caller making the request.
> > >
> > > anyOf -\> (list) \[required\]
> > >
> > > > A list of principal entries. The condition is met if any of the entries match the caller’s identity.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `100`
> > > >
> > > > (tagged union structure)
> > > >
> > > > > Union for principal matching. Currently supports IAM principal ARN glob matching.
> > > > >
> > > > > ### Note
> > > > >
> > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `iamPrincipal`.
> > > > >
> > > > > iamPrincipal -\> (structure)
> > > > >
> > > > > > An IAM principal to match against, specified by ARN.
> > > > > >
> > > > > > arn -\> (string) \[required\]
> > > > > >
> > > > > > > The Amazon Resource Name (ARN) of the IAM principal. Supports user, role, and assumed-role ARNs. Wildcards can be used with the `StringLike` operator.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `0`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `(arn:aws[a-zA-Z-]*:iam::(\d{12}|\*):(user|role)/[\w+=,.@*?/-]+|arn:aws[a-zA-Z-]*:sts::(\d{12}|\*):assumed-role/[\w+=,.@*?/-]+)`
> > > > > >
> > > > > > operator -\> (string)
> > > > > >
> > > > > > > The match operator. `StringEquals` requires an exact match. `StringLike` supports wildcard patterns using `*` and `?` .
> > > > > > >
> > > > > > > Possible values:
> > > > > > >
> > > > > > > - `StringEquals`
> > > > > > > - `StringLike`
> >
> > matchPaths -\> (structure)
> >
> > > A condition that matches on the request path.
> > >
> > > anyOf -\> (list) \[required\]
> > >
> > > > A list of path patterns. The condition is met if the request path matches any of the patterns.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `10`
> > > >
> > > > (string)
> > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `0`
> > > > > - max: `512`
> > > > > - pattern: `/[\w\-.]+/\*`

JSON Syntax:

    [
      {
        "matchPrincipals": {
          "anyOf": [
            {
              "iamPrincipal": {
                "arn": "string",
                "operator": "StringEquals"|"StringLike"
              }
            }
            ...
          ]
        },
        "matchPaths": {
          "anyOf": ["string", ...]
        }
      }
      ...
    ]

`--actions` (list)

> The updated actions for the rule.
>
> Constraints:
>
> - min: `1`
> - max: `2`
>
> (tagged union structure)
>
> > An action to take when a gateway rule’s conditions are met.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `configurationBundle`, `routeToTarget`.
> >
> > configurationBundle -\> (tagged union structure)
> >
> > > An action that applies a configuration bundle override to the request.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `staticOverride`, `weightedOverride`.
> > >
> > > staticOverride -\> (structure)
> > >
> > > > A static configuration bundle override that applies a single bundle version to all matching requests.
> > > >
> > > > bundleArn -\> (string) \[required\]
> > > >
> > > > > The Amazon Resource Name (ARN) of the configuration bundle to apply.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
> > > >
> > > > bundleVersion -\> (string) \[required\]
> > > >
> > > > > The version of the configuration bundle to apply.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
> > >
> > > weightedOverride -\> (structure)
> > >
> > > > A weighted configuration bundle override that splits traffic between multiple bundle versions based on configured weights.
> > > >
> > > > trafficSplit -\> (list) \[required\]
> > > >
> > > > > The traffic split entries defining how traffic is distributed between configuration bundle versions.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `2`
> > > > > - max: `2`
> > > > >
> > > > > (structure)
> > > > >
> > > > > > An entry in a traffic split configuration, defining a named variant with a weight and configuration bundle reference.
> > > > > >
> > > > > > name -\> (string) \[required\]
> > > > > >
> > > > > > > The name of this traffic split variant.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `64`
> > > > > > > - pattern: `[a-zA-Z0-9]([a-zA-Z0-9-]{0,62}[a-zA-Z0-9])?`
> > > > > >
> > > > > > weight -\> (integer) \[required\]
> > > > > >
> > > > > > > The percentage of traffic to route to this variant. Weights across all entries must sum to 100.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `99`
> > > > > >
> > > > > > configurationBundle -\> (structure) \[required\]
> > > > > >
> > > > > > > The configuration bundle reference for this variant.
> > > > > > >
> > > > > > > bundleArn -\> (string) \[required\]
> > > > > > >
> > > > > > > > The Amazon Resource Name (ARN) of the configuration bundle.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
> > > > > > >
> > > > > > > bundleVersion -\> (string) \[required\]
> > > > > > >
> > > > > > > > The version of the configuration bundle.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
> > > > > >
> > > > > > description -\> (string)
> > > > > >
> > > > > > > The description of this traffic split variant.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `200`
> > > > > >
> > > > > > metadata -\> (map)
> > > > > >
> > > > > > > Key-value metadata associated with this traffic split variant.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `0`
> > > > > > > - max: `25`
> > > > > > >
> > > > > > > key -\> (string)
> > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `128`
> > > > > > >
> > > > > > > value -\> (string)
> > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `256`
> >
> > routeToTarget -\> (tagged union structure)
> >
> > > An action that routes the request to a specific target.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `staticRoute`, `weightedRoute`.
> > >
> > > staticRoute -\> (structure)
> > >
> > > > A static route that sends all matching requests to a single target.
> > > >
> > > > targetName -\> (string) \[required\]
> > > >
> > > > > The name of the target to route requests to.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `([0-9a-zA-Z][-]?){1,100}`
> > >
> > > weightedRoute -\> (structure)
> > >
> > > > A weighted route that splits traffic between multiple targets.
> > > >
> > > > trafficSplit -\> (list) \[required\]
> > > >
> > > > > The traffic split entries defining how traffic is distributed between targets.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `2`
> > > > > - max: `2`
> > > > >
> > > > > (structure)
> > > > >
> > > > > > An entry in a target traffic split configuration.
> > > > > >
> > > > > > name -\> (string) \[required\]
> > > > > >
> > > > > > > The name of this traffic split variant.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `64`
> > > > > > > - pattern: `[a-zA-Z0-9]([a-zA-Z0-9-]{0,62}[a-zA-Z0-9])?`
> > > > > >
> > > > > > weight -\> (integer) \[required\]
> > > > > >
> > > > > > > The percentage of traffic to route to this variant.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `99`
> > > > > >
> > > > > > targetName -\> (string) \[required\]
> > > > > >
> > > > > > > The name of the target to route traffic to.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - pattern: `([0-9a-zA-Z][-]?){1,100}`
> > > > > >
> > > > > > description -\> (string)
> > > > > >
> > > > > > > The description of this traffic split variant.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `200`
> > > > > >
> > > > > > metadata -\> (map)
> > > > > >
> > > > > > > Key-value metadata associated with this traffic split variant.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `0`
> > > > > > > - max: `25`
> > > > > > >
> > > > > > > key -\> (string)
> > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `128`
> > > > > > >
> > > > > > > value -\> (string)
> > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `256`

JSON Syntax:

    [
      {
        "configurationBundle": {
          "staticOverride": {
            "bundleArn": "string",
            "bundleVersion": "string"
          },
          "weightedOverride": {
            "trafficSplit": [
              {
                "name": "string",
                "weight": integer,
                "configurationBundle": {
                  "bundleArn": "string",
                  "bundleVersion": "string"
                },
                "description": "string",
                "metadata": {"string": "string"
                  ...}
              }
              ...
            ]
          }
        },
        "routeToTarget": {
          "staticRoute": {
            "targetName": "string"
          },
          "weightedRoute": {
            "trafficSplit": [
              {
                "name": "string",
                "weight": integer,
                "targetName": "string",
                "description": "string",
                "metadata": {"string": "string"
                  ...}
              }
              ...
            ]
          }
        }
      }
      ...
    ]

`--description` (string)

> The updated description of the rule.
>
> Constraints:
>
> - min: `1`
> - max: `256`

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

ruleId -\> (string)

> The unique identifier of the gateway rule.
>
> Constraints:
>
> - min: `36`
> - max: `36`
> - pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

gatewayArn -\> (string)

> The Amazon Resource Name (ARN) of the gateway that the rule belongs to.
>
> Constraints:
>
> - pattern: `arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}`

priority -\> (integer)

> The priority of the rule. Rules are evaluated in order of priority, with lower numbers evaluated first.
>
> Constraints:
>
> - min: `1`
> - max: `1000000`

conditions -\> (list)

> The conditions that must be met for the rule to apply.
>
> Constraints:
>
> - min: `0`
> - max: `2`
>
> (tagged union structure)
>
> > A condition that determines when a gateway rule applies. Conditions can match on principals or request paths.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `matchPrincipals`, `matchPaths`.
> >
> > matchPrincipals -\> (structure)
> >
> > > A condition that matches on the identity of the caller making the request.
> > >
> > > anyOf -\> (list) \[required\]
> > >
> > > > A list of principal entries. The condition is met if any of the entries match the caller’s identity.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `100`
> > > >
> > > > (tagged union structure)
> > > >
> > > > > Union for principal matching. Currently supports IAM principal ARN glob matching.
> > > > >
> > > > > ### Note
> > > > >
> > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `iamPrincipal`.
> > > > >
> > > > > iamPrincipal -\> (structure)
> > > > >
> > > > > > An IAM principal to match against, specified by ARN.
> > > > > >
> > > > > > arn -\> (string) \[required\]
> > > > > >
> > > > > > > The Amazon Resource Name (ARN) of the IAM principal. Supports user, role, and assumed-role ARNs. Wildcards can be used with the `StringLike` operator.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `0`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `(arn:aws[a-zA-Z-]*:iam::(\d{12}|\*):(user|role)/[\w+=,.@*?/-]+|arn:aws[a-zA-Z-]*:sts::(\d{12}|\*):assumed-role/[\w+=,.@*?/-]+)`
> > > > > >
> > > > > > operator -\> (string)
> > > > > >
> > > > > > > The match operator. `StringEquals` requires an exact match. `StringLike` supports wildcard patterns using `*` and `?` .
> > > > > > >
> > > > > > > Possible values:
> > > > > > >
> > > > > > > - `StringEquals`
> > > > > > > - `StringLike`
> >
> > matchPaths -\> (structure)
> >
> > > A condition that matches on the request path.
> > >
> > > anyOf -\> (list) \[required\]
> > >
> > > > A list of path patterns. The condition is met if the request path matches any of the patterns.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `10`
> > > >
> > > > (string)
> > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `0`
> > > > > - max: `512`
> > > > > - pattern: `/[\w\-.]+/\*`

actions -\> (list)

> The actions to take when the rule conditions are met.
>
> Constraints:
>
> - min: `1`
> - max: `2`
>
> (tagged union structure)
>
> > An action to take when a gateway rule’s conditions are met.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `configurationBundle`, `routeToTarget`.
> >
> > configurationBundle -\> (tagged union structure)
> >
> > > An action that applies a configuration bundle override to the request.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `staticOverride`, `weightedOverride`.
> > >
> > > staticOverride -\> (structure)
> > >
> > > > A static configuration bundle override that applies a single bundle version to all matching requests.
> > > >
> > > > bundleArn -\> (string) \[required\]
> > > >
> > > > > The Amazon Resource Name (ARN) of the configuration bundle to apply.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
> > > >
> > > > bundleVersion -\> (string) \[required\]
> > > >
> > > > > The version of the configuration bundle to apply.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
> > >
> > > weightedOverride -\> (structure)
> > >
> > > > A weighted configuration bundle override that splits traffic between multiple bundle versions based on configured weights.
> > > >
> > > > trafficSplit -\> (list) \[required\]
> > > >
> > > > > The traffic split entries defining how traffic is distributed between configuration bundle versions.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `2`
> > > > > - max: `2`
> > > > >
> > > > > (structure)
> > > > >
> > > > > > An entry in a traffic split configuration, defining a named variant with a weight and configuration bundle reference.
> > > > > >
> > > > > > name -\> (string) \[required\]
> > > > > >
> > > > > > > The name of this traffic split variant.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `64`
> > > > > > > - pattern: `[a-zA-Z0-9]([a-zA-Z0-9-]{0,62}[a-zA-Z0-9])?`
> > > > > >
> > > > > > weight -\> (integer) \[required\]
> > > > > >
> > > > > > > The percentage of traffic to route to this variant. Weights across all entries must sum to 100.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `99`
> > > > > >
> > > > > > configurationBundle -\> (structure) \[required\]
> > > > > >
> > > > > > > The configuration bundle reference for this variant.
> > > > > > >
> > > > > > > bundleArn -\> (string) \[required\]
> > > > > > >
> > > > > > > > The Amazon Resource Name (ARN) of the configuration bundle.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
> > > > > > >
> > > > > > > bundleVersion -\> (string) \[required\]
> > > > > > >
> > > > > > > > The version of the configuration bundle.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
> > > > > >
> > > > > > description -\> (string)
> > > > > >
> > > > > > > The description of this traffic split variant.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `200`
> > > > > >
> > > > > > metadata -\> (map)
> > > > > >
> > > > > > > Key-value metadata associated with this traffic split variant.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `0`
> > > > > > > - max: `25`
> > > > > > >
> > > > > > > key -\> (string)
> > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `128`
> > > > > > >
> > > > > > > value -\> (string)
> > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `256`
> >
> > routeToTarget -\> (tagged union structure)
> >
> > > An action that routes the request to a specific target.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `staticRoute`, `weightedRoute`.
> > >
> > > staticRoute -\> (structure)
> > >
> > > > A static route that sends all matching requests to a single target.
> > > >
> > > > targetName -\> (string) \[required\]
> > > >
> > > > > The name of the target to route requests to.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `([0-9a-zA-Z][-]?){1,100}`
> > >
> > > weightedRoute -\> (structure)
> > >
> > > > A weighted route that splits traffic between multiple targets.
> > > >
> > > > trafficSplit -\> (list) \[required\]
> > > >
> > > > > The traffic split entries defining how traffic is distributed between targets.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `2`
> > > > > - max: `2`
> > > > >
> > > > > (structure)
> > > > >
> > > > > > An entry in a target traffic split configuration.
> > > > > >
> > > > > > name -\> (string) \[required\]
> > > > > >
> > > > > > > The name of this traffic split variant.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `64`
> > > > > > > - pattern: `[a-zA-Z0-9]([a-zA-Z0-9-]{0,62}[a-zA-Z0-9])?`
> > > > > >
> > > > > > weight -\> (integer) \[required\]
> > > > > >
> > > > > > > The percentage of traffic to route to this variant.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `99`
> > > > > >
> > > > > > targetName -\> (string) \[required\]
> > > > > >
> > > > > > > The name of the target to route traffic to.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - pattern: `([0-9a-zA-Z][-]?){1,100}`
> > > > > >
> > > > > > description -\> (string)
> > > > > >
> > > > > > > The description of this traffic split variant.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `200`
> > > > > >
> > > > > > metadata -\> (map)
> > > > > >
> > > > > > > Key-value metadata associated with this traffic split variant.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `0`
> > > > > > > - max: `25`
> > > > > > >
> > > > > > > key -\> (string)
> > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `128`
> > > > > > >
> > > > > > > value -\> (string)
> > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `256`

description -\> (string)

> The description of the gateway rule.
>
> Constraints:
>
> - min: `1`
> - max: `256`

createdAt -\> (timestamp)

> The timestamp when the rule was created.

status -\> (string)

> The current status of the rule.
>
> Possible values:
>
> - `CREATING`
> - `ACTIVE`
> - `UPDATING`
> - `DELETING`

system -\> (structure)

> System-managed metadata for rules created by automated processes.
>
> managedBy -\> (string) \[required\]
>
> > The identifier of the system or process that manages this rule.

updatedAt -\> (timestamp)

> The timestamp when the rule was last updated.

- [← update-gateway-rate-limit](update-gateway-rate-limit.html "previous chapter (use the left arrow)") /
- [update-gateway-target →](update-gateway-target.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](update-gateway-target.html "update-gateway-target") \|
- [previous](update-gateway-rate-limit.html "update-gateway-rate-limit") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [update-gateway-rule]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

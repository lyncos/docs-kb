---
title: aws bedrock-agentcore create-ab-test
description: \ [aws . bedrock-agentcore \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore/create-ab-test.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore](index.html#cli-aws-bedrock-agentcore) \]

# create-ab-test

## Description

Creates an A/B test for comparing agent configurations. A/B tests split traffic between a control variant and a treatment variant through a gateway, then evaluate performance using online evaluation configurations to determine which variant performs better.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-2024-02-28/CreateABTest)

## Synopsis

      create-ab-test
    --name <value>
    [--description <value>]
    --gateway-arn <value>
    --variants <value>
    [--gateway-filter <value>]
    --evaluation-config <value>
    --role-arn <value>
    [--enable-on-create | --no-enable-on-create]
    [--client-token <value>]
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

> The name of the A/B test. Must be unique within your account.
>
> Constraints:
>
> - pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`

`--description` (string)

> The description of the A/B test.
>
> Constraints:
>
> - min: `1`
> - max: `200`

`--gateway-arn` (string) \[required\]

> The Amazon Resource Name (ARN) of the gateway to use for traffic splitting.
>
> Constraints:
>
> - pattern: `arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}`

`--variants` (list) \[required\]

> The list of variants for the A/B test. Must contain exactly two variants: a control (C) and a treatment (T1), each with a configuration bundle or target reference and a traffic weight.
>
> Constraints:
>
> - min: `2`
> - max: `2`
>
> (structure)
>
> > A variant in an A/B test, representing either the control (C) or treatment (T1) configuration.
> >
> > name -\> (string) \[required\]
> >
> > > The name of the variant. Must be `C` for control or `T1` for treatment.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `2`
> > > - pattern: `(C|T1)`
> >
> > weight -\> (integer) \[required\]
> >
> > > The percentage of traffic to route to this variant. Weights across all variants must sum to 100.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `100`
> >
> > variantConfiguration -\> (structure) \[required\]
> >
> > > The configuration for this variant, including the configuration bundle or target reference.
> > >
> > > configurationBundle -\> (structure)
> > >
> > > > A reference to a configuration bundle version to use for this variant.
> > > >
> > > > bundleArn -\> (string) \[required\]
> > > >
> > > > > The Amazon Resource Name (ARN) of the configuration bundle.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
> > > >
> > > > bundleVersion -\> (string) \[required\]
> > > >
> > > > > The version of the configuration bundle.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
> > >
> > > target -\> (structure)
> > >
> > > > A reference to a gateway target to route traffic to for this variant.
> > > >
> > > > name -\> (string) \[required\]
> > > >
> > > > > The name of the gateway target.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `100`

Shorthand Syntax:

    name=string,weight=integer,variantConfiguration={configurationBundle={bundleArn=string,bundleVersion=string},target={name=string}} ...

JSON Syntax:

    [
      {
        "name": "string",
        "weight": integer,
        "variantConfiguration": {
          "configurationBundle": {
            "bundleArn": "string",
            "bundleVersion": "string"
          },
          "target": {
            "name": "string"
          }
        }
      }
      ...
    ]

`--gateway-filter` (structure)

> Optional filter to restrict which gateway target paths are included in the A/B test.
>
> targetPaths -\> (list)
>
> > A list of target path patterns to include in the A/B test.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `1`
> >
> > (string)
> >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `500`

Shorthand Syntax:

    targetPaths=string,string

JSON Syntax:

    {
      "targetPaths": ["string", ...]
    }

`--evaluation-config` (tagged union structure) \[required\]

> The evaluation configuration specifying which online evaluation configurations to use for measuring variant performance.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `onlineEvaluationConfigArn`, `perVariantOnlineEvaluationConfig`.
>
> onlineEvaluationConfigArn -\> (string)
>
> > The Amazon Resource Name (ARN) of a single online evaluation configuration to use for both variants.
> >
> > Constraints:
> >
> > - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:online-evaluation-config\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
>
> perVariantOnlineEvaluationConfig -\> (list)
>
> > Per-variant online evaluation configurations, allowing different evaluation settings for each variant.
> >
> > Constraints:
> >
> > - min: `2`
> > - max: `2`
> >
> > (structure)
> >
> > > An online evaluation configuration associated with a specific A/B test variant.
> > >
> > > name -\> (string) \[required\]
> > >
> > > > The name of the variant this evaluation configuration applies to.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `2`
> > > > - pattern: `(C|T1)`
> > >
> > > onlineEvaluationConfigArn -\> (string) \[required\]
> > >
> > > > The Amazon Resource Name (ARN) of the online evaluation configuration for this variant.
> > > >
> > > > Constraints:
> > > >
> > > > - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:online-evaluation-config\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`

Shorthand Syntax:

    onlineEvaluationConfigArn=string,perVariantOnlineEvaluationConfig=[{name=string,onlineEvaluationConfigArn=string},{name=string,onlineEvaluationConfigArn=string}]

JSON Syntax:

    {
      "onlineEvaluationConfigArn": "string",
      "perVariantOnlineEvaluationConfig": [
        {
          "name": "string",
          "onlineEvaluationConfigArn": "string"
        }
        ...
      ]
    }

`--role-arn` (string) \[required\]

> The IAM role ARN that grants permissions for the A/B test to access gateway and evaluation resources.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`

`--enable-on-create` \| `--no-enable-on-create` (boolean)

> Whether to enable the A/B test immediately upon creation. If true, traffic splitting begins automatically.

`--client-token` (string)

> A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.
>
> Constraints:
>
> - min: `33`
> - max: `256`
> - pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`

`--tags` (map)

> A map of tag keys and values to associate with the A/B test.
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

abTestId -\> (string)

> The unique identifier of the created A/B test.
>
> Constraints:
>
> - pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`

abTestArn -\> (string)

> The Amazon Resource Name (ARN) of the created A/B test.
>
> Constraints:
>
> - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:ab-test/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`

name -\> (string)

> The name of the A/B test.
>
> Constraints:
>
> - pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`

status -\> (string)

> The status of the A/B test.
>
> Possible values:
>
> - `CREATING`
> - `ACTIVE`
> - `CREATE_FAILED`
> - `UPDATING`
> - `UPDATE_FAILED`
> - `DELETING`
> - `DELETE_FAILED`
> - `FAILED`

executionStatus -\> (string)

> The execution status indicating whether the A/B test is currently running.
>
> Possible values:
>
> - `PAUSED`
> - `RUNNING`
> - `STOPPED`
> - `NOT_STARTED`

createdAt -\> (timestamp)

> The timestamp when the A/B test was created.

- [← complete-resource-token-auth](complete-resource-token-auth.html "previous chapter (use the left arrow)") /
- [create-event →](create-event.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](create-event.html "create-event") \|
- [previous](complete-resource-token-auth.html "complete-resource-token-auth") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore](index.html) »
- [create-ab-test]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

---
title: aws bedrock-agentcore get-ab-test
description: \ [aws . bedrock-agentcore \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore/get-ab-test.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore](index.html#cli-aws-bedrock-agentcore) \]

# get-ab-test

## Description

Retrieves detailed information about an A/B test, including its configuration, status, and statistical results.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-2024-02-28/GetABTest)

## Synopsis

      get-ab-test
    --ab-test-id <value>
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

`--ab-test-id` (string) \[required\]

> The unique identifier of the A/B test to retrieve.
>
> Constraints:
>
> - pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`

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

> The unique identifier of the A/B test.
>
> Constraints:
>
> - pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`

abTestArn -\> (string)

> The Amazon Resource Name (ARN) of the A/B test.
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

description -\> (string)

> The description of the A/B test.
>
> Constraints:
>
> - min: `1`
> - max: `200`

status -\> (string)

> The current status of the A/B test.
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

gatewayArn -\> (string)

> The Amazon Resource Name (ARN) of the gateway used for traffic splitting.
>
> Constraints:
>
> - pattern: `arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}`

variants -\> (list)

> The list of variants in the A/B test.
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

gatewayFilter -\> (structure)

> The gateway filter restricting which target paths are included.
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

evaluationConfig -\> (tagged union structure)

> The evaluation configuration for measuring variant performance.
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

roleArn -\> (string)

> The IAM role ARN used by the A/B test.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`

currentRunId -\> (string)

> The identifier of the current run of the A/B test.

errorDetails -\> (list)

> The error details if the A/B test encountered failures.
>
> Constraints:
>
> - min: `0`
> - max: `1`
>
> (string)
>
> > Constraints:
> >
> > - min: `0`
> > - max: `1000`

startedAt -\> (timestamp)

> The timestamp when the A/B test was started.

stoppedAt -\> (timestamp)

> The timestamp when the A/B test was stopped.

maxDurationExpiresAt -\> (timestamp)

> The timestamp when the A/B test will automatically expire.

createdAt -\> (timestamp)

> The timestamp when the A/B test was created.

updatedAt -\> (timestamp)

> The timestamp when the A/B test was last updated.

results -\> (structure)

> The statistical results of the A/B test, including per-evaluator metrics and significance analysis.
>
> analysisTimestamp -\> (timestamp)
>
> > The timestamp when the analysis was performed.
>
> evaluatorMetrics -\> (list) \[required\]
>
> > The per-evaluator metrics comparing control and treatment variants.
> >
> > (structure)
> >
> > > Statistical metrics for a single evaluator comparing control and treatment variants.
> > >
> > > evaluatorArn -\> (string) \[required\]
> > >
> > > > The Amazon Resource Name (ARN) of the evaluator.
> > >
> > > controlStats -\> (structure) \[required\]
> > >
> > > > The statistics for the control variant.
> > > >
> > > > variantName -\> (string) \[required\]
> > > >
> > > > > The name of the control variant.
> > > >
> > > > sampleSize -\> (integer) \[required\]
> > > >
> > > > > The number of sessions evaluated for the control variant.
> > > >
> > > > mean -\> (double) \[required\]
> > > >
> > > > > The mean evaluation score for the control variant.
> > >
> > > variantResults -\> (list) \[required\]
> > >
> > > > The results for each treatment variant compared against the control.
> > > >
> > > > (structure)
> > > >
> > > > > Statistical results for a treatment variant compared against the control.
> > > > >
> > > > > variantName -\> (string) \[required\]
> > > > >
> > > > > > The name of the treatment variant.
> > > > >
> > > > > sampleSize -\> (integer) \[required\]
> > > > >
> > > > > > The number of sessions evaluated for this variant.
> > > > >
> > > > > mean -\> (double) \[required\]
> > > > >
> > > > > > The mean evaluation score for this variant.
> > > > >
> > > > > absoluteChange -\> (double)
> > > > >
> > > > > > The absolute change in mean score compared to the control variant.
> > > > >
> > > > > percentChange -\> (double)
> > > > >
> > > > > > The percentage change in mean score compared to the control variant.
> > > > >
> > > > > pValue -\> (double)
> > > > >
> > > > > > The p-value indicating the statistical significance of the observed difference.
> > > > >
> > > > > confidenceInterval -\> (structure)
> > > > >
> > > > > > The confidence interval for the observed difference.
> > > > > >
> > > > > > lower -\> (double)
> > > > > >
> > > > > > > The lower bound of the confidence interval.
> > > > > >
> > > > > > upper -\> (double)
> > > > > >
> > > > > > > The upper bound of the confidence interval.
> > > > >
> > > > > isSignificant -\> (boolean) \[required\]
> > > > >
> > > > > > Whether the observed difference is statistically significant.

- [← evaluate](evaluate.html "previous chapter (use the left arrow)") /
- [get-agent-card →](get-agent-card.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](get-agent-card.html "get-agent-card") \|
- [previous](evaluate.html "evaluate") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore](index.html) »
- [get-ab-test]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

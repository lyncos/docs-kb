---
title: aws bedrock-agentcore-control get-online-evaluation-config
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/get-online-evaluation-config.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# get-online-evaluation-config

## Description

Retrieves detailed information about an online evaluation configuration, including its rules, data sources, evaluators, and execution status.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/GetOnlineEvaluationConfig)

## Synopsis

      get-online-evaluation-config
    --online-evaluation-config-id <value>
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

`--online-evaluation-config-id` (string) \[required\]

> The unique identifier of the online evaluation configuration to retrieve.
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

onlineEvaluationConfigArn -\> (string)

> The Amazon Resource Name (ARN) of the online evaluation configuration.
>
> Constraints:
>
> - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:online-evaluation-config\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`

onlineEvaluationConfigId -\> (string)

> The unique identifier of the online evaluation configuration.
>
> Constraints:
>
> - pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`

onlineEvaluationConfigName -\> (string)

> The name of the online evaluation configuration.
>
> Constraints:
>
> - pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`

description -\> (string)

> The description of the online evaluation configuration.
>
> Constraints:
>
> - min: `1`
> - max: `200`
> - pattern: `.+`

rule -\> (structure)

> The evaluation rule containing sampling configuration, filters, and session settings.
>
> samplingConfig -\> (structure) \[required\]
>
> > The sampling configuration that determines what percentage of agent traces to evaluate.
> >
> > samplingPercentage -\> (double) \[required\]
> >
> > > The percentage of agent traces to sample for evaluation, ranging from 0.01% to 100%.
> > >
> > > Constraints:
> > >
> > > - min: `0.01`
> > > - max: `100.0`
>
> filters -\> (list)
>
> > The list of filters that determine which agent traces should be included in the evaluation based on trace properties.
> >
> > Constraints:
> >
> > - min: `0`
> > - max: `5`
> >
> > (structure)
> >
> > > The filter that applies conditions to agent traces during online evaluation to determine which traces should be evaluated.
> > >
> > > key -\> (string) \[required\]
> > >
> > > > The key or field name to filter on within the agent trace data.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `256`
> > > > - pattern: `[a-zA-Z0-9._-]+`
> > >
> > > operator -\> (string) \[required\]
> > >
> > > > The comparison operator to use for filtering.
> > > >
> > > > Possible values:
> > > >
> > > > - `Equals`
> > > > - `NotEquals`
> > > > - `GreaterThan`
> > > > - `LessThan`
> > > > - `GreaterThanOrEqual`
> > > > - `LessThanOrEqual`
> > > > - `Contains`
> > > > - `NotContains`
> > >
> > > value -\> (tagged union structure) \[required\]
> > >
> > > > The value to compare against using the specified operator.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `doubleValue`, `booleanValue`.
> > > >
> > > > stringValue -\> (string)
> > > >
> > > > > The string value for text-based filtering.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `1024`
> > > >
> > > > doubleValue -\> (double)
> > > >
> > > > > The numeric value for numerical filtering and comparisons.
> > > >
> > > > booleanValue -\> (boolean)
> > > >
> > > > > The boolean value for true/false filtering conditions.
>
> sessionConfig -\> (structure)
>
> > The session configuration that defines timeout settings for detecting when agent sessions are complete and ready for evaluation.
> >
> > sessionTimeoutMinutes -\> (integer) \[required\]
> >
> > > The number of minutes of inactivity after which an agent session is considered complete and ready for evaluation. Default is 15 minutes.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `1440`

dataSourceConfig -\> (tagged union structure)

> The data source configuration specifying CloudWatch log groups and service names to monitor.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `cloudWatchLogs`.
>
> cloudWatchLogs -\> (structure)
>
> > The CloudWatch logs configuration for reading agent traces from log groups.
> >
> > logGroupNames -\> (list)
> >
> > > The list of CloudWatch log group names to monitor for agent traces.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `10`
> > >
> > > (string)
> > >
> > > > Constraints:
> > > >
> > > > - pattern: `[.\-_/#A-Za-z0-9]+`
> >
> > logGroupNamePrefixes -\> (list)
> >
> > > The list of CloudWatch log group name prefixes to monitor for agent traces. Specify this instead of `logGroupNames` to match log groups by prefix. Specify either `logGroupNames` or `logGroupNamePrefixes` , not both. One of the two is required.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `5`
> > >
> > > (string)
> > >
> > > > Prefix of a CloudWatch Logs log group name.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `512`
> > > > - pattern: `[.\-_/#A-Za-z0-9]+`
> >
> > serviceNames -\> (list) \[required\]
> >
> > > The list of service names to filter traces within the specified log groups. Used to identify relevant agent sessions.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `1`
> > >
> > > (string)
> > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `256`
> > > > - pattern: `[a-zA-Z0-9._-]+`

evaluators -\> (list)

> The list of evaluators applied during online evaluation.
>
> Constraints:
>
> - min: `0`
> - max: `25`
>
> (tagged union structure)
>
> > The reference to an evaluator used in online evaluation configurations, containing the evaluator identifier.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `evaluatorId`.
> >
> > evaluatorId -\> (string)
> >
> > > The unique identifier of the evaluator. Can reference builtin evaluators (e.g., Builtin.Helpfulness) or custom evaluators.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `111`
> > > - pattern: `(Builtin\.[a-zA-Z0-9._-]+|ThirdParty\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})`

insights -\> (list)

> The list of insight types configured for this evaluation.
>
> Constraints:
>
> - min: `0`
> - max: `10`
>
> (structure)
>
> > A reference to an insight analysis to run against sessions during evaluation. Insights provide deeper analysis beyond individual evaluator scores, including failure detection, user intent clustering, and execution summarization.
> >
> > insightId -\> (string) \[required\]
> >
> > > The unique identifier of the insight to run.
> > >
> > > Constraints:
> > >
> > > - pattern: `(Builtin\.[a-zA-Z0-9._-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})`

clusteringConfig -\> (structure)

> The clustering configuration for periodic batch evaluation.
>
> frequencies -\> (list) \[required\]
>
> > The list of frequencies at which clustering batch evaluations are triggered.
> >
> > Constraints:
> >
> > - min: `0`
> > - max: `3`
> >
> > (string)
> >
> > > Possible values:
> > >
> > > - `DAILY`
> > > - `WEEKLY`
> > > - `MONTHLY`

outputConfig -\> (structure)

> The output configuration specifying where evaluation results are written.
>
> cloudWatchConfig -\> (structure) \[required\]
>
> > The CloudWatch configuration for writing evaluation results to CloudWatch logs with embedded metric format.
> >
> > logGroupName -\> (string)
> >
> > > The name of the CloudWatch log group where evaluation results will be written. An existing log group is used as-is; otherwise the service creates it, which requires the evaluation execution role to grant `logs:CreateLogGroup` on the log group. Don’t specify this value when `resultDestination` is `SOURCE_LOG_GROUP` . The name can’t be under the service-reserved `/aws/bedrock-agentcore/evaluations/` namespace, apart from this configuration’s own service-managed default group.
> > >
> > > Constraints:
> > >
> > > - pattern: `$|^[.\-_/#A-Za-z0-9]+`
> >
> > metricsNamespace -\> (string)
> >
> > > The CloudWatch metrics namespace where evaluation result metrics are published. If you omit this value, the service publishes metrics to `Bedrock-AgentCore/Evaluations` . This value can’t begin with `AWS/` .
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `255`
> > > - pattern: `[a-zA-Z0-9._#/:-]+`
> >
> > resultDestination -\> (string)
> >
> > > The destination where evaluation results are written. Valid values:
> > >
> > > - `DEDICATED_LOG_GROUP` (default) – Writes results to a dedicated result log group.
> > > - `SOURCE_LOG_GROUP` – Writes results back to the log group that the agent traces were read from. If you use this value, don’t specify `logGroupName` .
> > >
> > > Possible values:
> > >
> > > - `DEDICATED_LOG_GROUP`
> > > - `SOURCE_LOG_GROUP`

evaluationExecutionRoleArn -\> (string)

> The Amazon Resource Name (ARN) of the IAM role used for evaluation execution.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`

status -\> (string)

> The status of the online evaluation configuration.
>
> Possible values:
>
> - `ACTIVE`
> - `CREATING`
> - `CREATE_FAILED`
> - `UPDATING`
> - `UPDATE_FAILED`
> - `DELETING`
> - `ERROR`

executionStatus -\> (string)

> The execution status indicating whether the online evaluation is currently running.
>
> Possible values:
>
> - `ENABLED`
> - `DISABLED`

createdAt -\> (timestamp)

> The timestamp when the online evaluation configuration was created.

updatedAt -\> (timestamp)

> The timestamp when the online evaluation configuration was last updated.

failureReason -\> (string)

> The reason for failure if the online evaluation configuration execution failed.

- [← get-oauth2-credential-provider](get-oauth2-credential-provider.html "previous chapter (use the left arrow)") /
- [get-payment-connector →](get-payment-connector.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](get-payment-connector.html "get-payment-connector") \|
- [previous](get-oauth2-credential-provider.html "get-oauth2-credential-provider") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [get-online-evaluation-config]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

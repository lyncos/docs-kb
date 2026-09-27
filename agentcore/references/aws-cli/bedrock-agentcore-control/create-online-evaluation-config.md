---
title: aws bedrock-agentcore-control create-online-evaluation-config
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/create-online-evaluation-config.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# create-online-evaluation-config

## Description

Creates an online evaluation configuration for continuous monitoring of agent performance. Online evaluation automatically samples live traffic from CloudWatch logs at specified rates and applies evaluators to assess agent quality in production.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/CreateOnlineEvaluationConfig)

## Synopsis

      create-online-evaluation-config
    [--client-token <value>]
    --online-evaluation-config-name <value>
    [--description <value>]
    --rule <value>
    --data-source-config <value>
    [--evaluators <value>]
    [--insights <value>]
    [--clustering-config <value>]
    [--output-config <value>]
    --evaluation-execution-role-arn <value>
    --enable-on-create | --no-enable-on-create
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

`--client-token` (string)

> A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don’t specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn’t return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) .
>
> Constraints:
>
> - min: `33`
> - max: `256`
> - pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`

`--online-evaluation-config-name` (string) \[required\]

> The name of the online evaluation configuration. Must be unique within your account.
>
> Constraints:
>
> - pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`

`--description` (string)

> The description of the online evaluation configuration that explains its monitoring purpose and scope.
>
> Constraints:
>
> - min: `1`
> - max: `200`
> - pattern: `.+`

`--rule` (structure) \[required\]

> The evaluation rule that defines sampling configuration, filters, and session detection settings for the online evaluation.
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

JSON Syntax:

    {
      "samplingConfig": {
        "samplingPercentage": double
      },
      "filters": [
        {
          "key": "string",
          "operator": "Equals"|"NotEquals"|"GreaterThan"|"LessThan"|"GreaterThanOrEqual"|"LessThanOrEqual"|"Contains"|"NotContains",
          "value": {
            "stringValue": "string",
            "doubleValue": double,
            "booleanValue": true|false
          }
        }
        ...
      ],
      "sessionConfig": {
        "sessionTimeoutMinutes": integer
      }
    }

`--data-source-config` (tagged union structure) \[required\]

> The data source configuration that specifies CloudWatch log groups and service names to monitor for agent traces.
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

Shorthand Syntax:

    cloudWatchLogs={logGroupNames=[string,string],logGroupNamePrefixes=[string,string],serviceNames=[string,string]}

JSON Syntax:

    {
      "cloudWatchLogs": {
        "logGroupNames": ["string", ...],
        "logGroupNamePrefixes": ["string", ...],
        "serviceNames": ["string", ...]
      }
    }

`--evaluators` (list)

> The list of evaluators to apply during online evaluation. Can include both built-in evaluators and custom evaluators created with `CreateEvaluator` .
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

Shorthand Syntax:

    evaluatorId=string ...

JSON Syntax:

    [
      {
        "evaluatorId": "string"
      }
      ...
    ]

`--insights` (list)

> The list of insight types to run against agent sessions.
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

Shorthand Syntax:

    insightId=string ...

JSON Syntax:

    [
      {
        "insightId": "string"
      }
      ...
    ]

`--clustering-config` (structure)

> Configuration for periodic batch evaluation clustering of insight results.
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

Shorthand Syntax:

    frequencies=string,string

JSON Syntax:

    {
      "frequencies": ["DAILY"|"WEEKLY"|"MONTHLY", ...]
    }

`--output-config` (structure)

> The configuration that specifies where evaluation results should be written for monitoring and analysis.
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

Shorthand Syntax:

    cloudWatchConfig={logGroupName=string,metricsNamespace=string,resultDestination=string}

JSON Syntax:

    {
      "cloudWatchConfig": {
        "logGroupName": "string",
        "metricsNamespace": "string",
        "resultDestination": "DEDICATED_LOG_GROUP"|"SOURCE_LOG_GROUP"
      }
    }

`--evaluation-execution-role-arn` (string) \[required\]

> The Amazon Resource Name (ARN) of the IAM role that grants permissions to read from CloudWatch logs, write evaluation results, and invoke Amazon Bedrock models for evaluation. If the configuration references evaluators encrypted with a customer managed KMS key, this role must also have `kms:Decrypt` permission on the KMS key. The service validates this permission at configuration creation time. For more information, see [Encryption at rest for AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-encryption.html) .
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`

`--enable-on-create` \| `--no-enable-on-create` (boolean) \[required\]

> Whether to enable the online evaluation configuration immediately upon creation. If true, evaluation begins automatically.

`--tags` (map)

> A map of tag keys and values to assign to an AgentCore Online Evaluation Config. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.
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

onlineEvaluationConfigArn -\> (string)

> The Amazon Resource Name (ARN) of the created online evaluation configuration.
>
> Constraints:
>
> - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:online-evaluation-config\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`

onlineEvaluationConfigId -\> (string)

> The unique identifier of the created online evaluation configuration.
>
> Constraints:
>
> - pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`

createdAt -\> (timestamp)

> The timestamp when the online evaluation configuration was created.

outputConfig -\> (structure)

> The configuration that specifies where evaluation results should be written for monitoring and analysis.
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

failureReason -\> (string)

> The reason for failure if the online evaluation configuration creation or execution failed.

- [← create-oauth2-credential-provider](create-oauth2-credential-provider.html "previous chapter (use the left arrow)") /
- [create-payment-connector →](create-payment-connector.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](create-payment-connector.html "create-payment-connector") \|
- [previous](create-oauth2-credential-provider.html "create-oauth2-credential-provider") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [create-online-evaluation-config]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

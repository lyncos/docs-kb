---
title: aws bedrock-agentcore start-batch-evaluation
description: \ [aws . bedrock-agentcore \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore/start-batch-evaluation.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore](index.html#cli-aws-bedrock-agentcore) \]

# start-batch-evaluation

## Description

Starts a batch evaluation job that evaluates agent performance across multiple sessions. Batch evaluations pull agent traces from CloudWatch Logs or an existing online evaluation configuration and run specified evaluators and insights against them.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-2024-02-28/StartBatchEvaluation)

## Synopsis

      start-batch-evaluation
    --batch-evaluation-name <value>
    [--evaluators <value>]
    [--insights <value>]
    --data-source-config <value>
    [--client-token <value>]
    [--evaluation-metadata <value>]
    [--tags <value>]
    [--kms-key-arn <value>]
    [--description <value>]
    [--output-config <value>]
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

`--batch-evaluation-name` (string) \[required\]

> The name of the batch evaluation. Must be unique within your account.
>
> Constraints:
>
> - pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`

`--evaluators` (list)

> The list of evaluators to apply during the batch evaluation. Can include both built-in evaluators and custom evaluators. Maximum of 10 evaluators.
>
> Constraints:
>
> - min: `0`
> - max: `10`
>
> (structure)
>
> > An evaluator to run against sessions during batch evaluation.
> >
> > evaluatorId -\> (string) \[required\]
> >
> > > The unique identifier of the evaluator. Can reference built-in evaluators (e.g., `Builtin.Helpfulness` ) or custom evaluators.
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

> The list of insight analyses to run against sessions during the batch evaluation. Maximum of 10 insights.
>
> Constraints:
>
> - min: `0`
> - max: `10`
>
> (structure)
>
> > A reference to an insight analysis to run against sessions during batch evaluation. Insights provide deeper analysis beyond individual evaluator scores, including failure detection, user intent clustering, and execution summarization.
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

`--data-source-config` (tagged union structure) \[required\]

> The data source configuration that specifies where to pull agent session traces from for evaluation.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `cloudWatchLogs`, `onlineEvaluationConfigSource`.
>
> cloudWatchLogs -\> (structure)
>
> > Configuration for pulling agent session traces from CloudWatch Logs.
> >
> > serviceNames -\> (list) \[required\]
> >
> > > The list of agent service names to filter traces within the specified log groups.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `1`
> > >
> > > (string)
> >
> > logGroupNames -\> (list)
> >
> > > The list of CloudWatch log group names to read agent traces from. Maximum of 10 log groups.
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
> > > The list of CloudWatch log group name prefixes to read agent traces from. Specify this instead of `logGroupNames` to match log groups by prefix. Maximum of 5 prefixes. Specify either `logGroupNames` or `logGroupNamePrefixes` , not both. One of the two is required.
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
> > filterConfig -\> (structure)
> >
> > > Optional filter configuration to narrow down which sessions to evaluate.
> > >
> > > sessionIds -\> (list)
> > >
> > > > A list of specific session IDs to evaluate. If specified, only these sessions are included in the evaluation.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0`
> > > > - max: `500`
> > > >
> > > > (string)
> > >
> > > timeRange -\> (structure)
> > >
> > > > The time range filter for selecting sessions to evaluate.
> > > >
> > > > startTime -\> (timestamp)
> > > >
> > > > > The start time of the time range. Only sessions with activity at or after this timestamp are included.
> > > >
> > > > endTime -\> (timestamp)
> > > >
> > > > > The end time of the time range. Only sessions with activity before this timestamp are included.
> > >
> > > sessionTraceIds -\> (list)
> > >
> > > > A list of session and trace ID pairs that restrict evaluation to specific traces within a session. If specified, only the listed traces are evaluated instead of the entire session.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `500`
> > > >
> > > > (structure)
> > > >
> > > > > A pairing of a session with the specific trace IDs to evaluate within that session. Use this to evaluate individual traces rather than an entire session.
> > > > >
> > > > > sessionId -\> (string) \[required\]
> > > > >
> > > > > > The unique identifier of the session that contains the traces to evaluate.
> > > > >
> > > > > traceIds -\> (list) \[required\]
> > > > >
> > > > > > The list of trace IDs within the session to evaluate.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `100`
> > > > > >
> > > > > > (string)
> > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `32`
> > > > > > > - max: `32`
>
> onlineEvaluationConfigSource -\> (structure)
>
> > Reference an existing OnlineEvaluationConfig as session source
> >
> > onlineEvaluationConfigArn -\> (string) \[required\]
> >
> > > The Amazon Resource Name (ARN) of the online evaluation configuration to use as the session source.
> > >
> > > Constraints:
> > >
> > > - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:online-evaluation-config\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
> >
> > timeRange -\> (structure)
> >
> > > Optional session filter configuration to narrow down which sessions from the online evaluation configuration to include.
> > >
> > > startTime -\> (timestamp)
> > >
> > > > The start time of the time range. Only sessions with activity at or after this timestamp are included.
> > >
> > > endTime -\> (timestamp)
> > >
> > > > The end time of the time range. Only sessions with activity before this timestamp are included.

JSON Syntax:

    {
      "cloudWatchLogs": {
        "serviceNames": ["string", ...],
        "logGroupNames": ["string", ...],
        "logGroupNamePrefixes": ["string", ...],
        "filterConfig": {
          "sessionIds": ["string", ...],
          "timeRange": {
            "startTime": timestamp,
            "endTime": timestamp
          },
          "sessionTraceIds": [
            {
              "sessionId": "string",
              "traceIds": ["string", ...]
            }
            ...
          ]
        }
      },
      "onlineEvaluationConfigSource": {
        "onlineEvaluationConfigArn": "string",
        "timeRange": {
          "startTime": timestamp,
          "endTime": timestamp
        }
      }
    }

`--client-token` (string)

> A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.
>
> Constraints:
>
> - min: `33`
> - max: `256`
> - pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`

`--evaluation-metadata` (tagged union structure)

> Optional metadata for the evaluation, including session-specific ground truth data and test scenario identifiers.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `sessionMetadata`.
>
> sessionMetadata -\> (list)
>
> > A list of session metadata entries containing ground truth data and test scenario identifiers for specific sessions.
> >
> > Constraints:
> >
> > - min: `0`
> > - max: `500`
> >
> > (structure)
> >
> > > Metadata for a specific session in a batch evaluation, including ground truth data and test scenario identifiers.
> > >
> > > sessionId -\> (string) \[required\]
> > >
> > > > The unique identifier of the session this metadata applies to.
> > >
> > > testScenarioId -\> (string)
> > >
> > > > An optional test scenario identifier for categorizing and tracking evaluation results.
> > >
> > > groundTruth -\> (tagged union structure)
> > >
> > > > The ground truth data for this session, including expected responses and assertions.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `inline`.
> > > >
> > > > inline -\> (structure)
> > > >
> > > > > Inline ground truth data provided directly in the request.
> > > > >
> > > > > assertions -\> (list)
> > > > >
> > > > > > Assertions for evaluation, reuses common model EvaluationContentList.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `100`
> > > > > >
> > > > > > (tagged union structure)
> > > > > >
> > > > > > > A content block for ground truth data in evaluation reference inputs. Supports text content for expected responses and assertions.
> > > > > > >
> > > > > > > ### Note
> > > > > > >
> > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `text`.
> > > > > > >
> > > > > > > text -\> (string)
> > > > > > >
> > > > > > > > The text content of the ground truth data. Used for expected response text and assertion statements.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `100000`
> > > > >
> > > > > expectedTrajectory -\> (structure)
> > > > >
> > > > > > The expected tool call sequence for trajectory evaluation.
> > > > > >
> > > > > > toolNames -\> (list)
> > > > > >
> > > > > > > The list of tool names representing the expected tool call sequence.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `0`
> > > > > > > - max: `1000`
> > > > > > >
> > > > > > > (string)
> > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `500`
> > > > >
> > > > > turns -\> (list)
> > > > >
> > > > > > A list of per-turn ground truth data, each containing an input prompt and expected response.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > >
> > > > > > (structure)
> > > > > >
> > > > > > > Ground truth data for a single conversation turn.
> > > > > > >
> > > > > > > input -\> (tagged union structure)
> > > > > > >
> > > > > > > > The input for this conversation turn.
> > > > > > > >
> > > > > > > > ### Note
> > > > > > > >
> > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `prompt`.
> > > > > > > >
> > > > > > > > prompt -\> (string)
> > > > > > > >
> > > > > > > > > The text prompt for this conversation turn.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `0`
> > > > > > > > > - max: `4000`
> > > > > > >
> > > > > > > expectedResponse -\> (tagged union structure)
> > > > > > >
> > > > > > > > The expected response for this conversation turn.
> > > > > > > >
> > > > > > > > ### Note
> > > > > > > >
> > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `text`.
> > > > > > > >
> > > > > > > > text -\> (string)
> > > > > > > >
> > > > > > > > > The text content of the ground truth data. Used for expected response text and assertion statements.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `100000`
> > >
> > > metadata -\> (map)
> > >
> > > > Additional key-value metadata associated with this session.
> > > >
> > > > key -\> (string)
> > > >
> > > > value -\> (string)

JSON Syntax:

    {
      "sessionMetadata": [
        {
          "sessionId": "string",
          "testScenarioId": "string",
          "groundTruth": {
            "inline": {
              "assertions": [
                {
                  "text": "string"
                }
                ...
              ],
              "expectedTrajectory": {
                "toolNames": ["string", ...]
              },
              "turns": [
                {
                  "input": {
                    "prompt": "string"
                  },
                  "expectedResponse": {
                    "text": "string"
                  }
                }
                ...
              ]
            }
          },
          "metadata": {"string": "string"
            ...}
        }
        ...
      ]
    }

`--tags` (map)

> A map of tag keys and values to associate with the batch evaluation.
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

`--kms-key-arn` (string)

> The ARN of the KMS key used to encrypt evaluation data. If provided, customer data is encrypted at rest with the specified key.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`

`--description` (string)

> The description of the batch evaluation.
>
> Constraints:
>
> - min: `0`
> - max: `200`

`--output-config` (tagged union structure)

> Output destination configuration.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `cloudWatchConfig`.
>
> cloudWatchConfig -\> (structure)
>
> > The CloudWatch Logs configuration for writing evaluation results.
> >
> > logGroupName -\> (string)
> >
> > > The name of the CloudWatch log group where evaluation results will be written. This value doesn’t apply when `resultDestination` is `SOURCE_LOG_GROUP` , because results are written back to the trace source log group. The name can’t be under the service-reserved `/aws/bedrock-agentcore/evaluations/` namespace, apart from the service-managed default group.
> > >
> > > Constraints:
> > >
> > > - pattern: `$|^[.\-_/#A-Za-z0-9]+`
> >
> > logStreamName -\> (string)
> >
> > > The name of the CloudWatch log stream where evaluation results will be written.
> > >
> > > Constraints:
> > >
> > > - pattern: `[^:*]*`
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

    cloudWatchConfig={logGroupName=string,logStreamName=string,metricsNamespace=string,resultDestination=string}

JSON Syntax:

    {
      "cloudWatchConfig": {
        "logGroupName": "string",
        "logStreamName": "string",
        "metricsNamespace": "string",
        "resultDestination": "DEDICATED_LOG_GROUP"|"SOURCE_LOG_GROUP"
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

batchEvaluationId -\> (string)

> The unique identifier of the created batch evaluation.
>
> Constraints:
>
> - pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`

batchEvaluationArn -\> (string)

> The Amazon Resource Name (ARN) of the created batch evaluation.

batchEvaluationName -\> (string)

> The name of the batch evaluation.
>
> Constraints:
>
> - pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`

evaluators -\> (list)

> The list of evaluators applied during the batch evaluation.
>
> (structure)
>
> > An evaluator to run against sessions during batch evaluation.
> >
> > evaluatorId -\> (string) \[required\]
> >
> > > The unique identifier of the evaluator. Can reference built-in evaluators (e.g., `Builtin.Helpfulness` ) or custom evaluators.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `111`
> > > - pattern: `(Builtin\.[a-zA-Z0-9._-]+|ThirdParty\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})`

insights -\> (list)

> The list of insight analyses applied during the batch evaluation.
>
> Constraints:
>
> - min: `0`
> - max: `10`
>
> (structure)
>
> > A reference to an insight analysis to run against sessions during batch evaluation. Insights provide deeper analysis beyond individual evaluator scores, including failure detection, user intent clustering, and execution summarization.
> >
> > insightId -\> (string) \[required\]
> >
> > > The unique identifier of the insight to run.
> > >
> > > Constraints:
> > >
> > > - pattern: `(Builtin\.[a-zA-Z0-9._-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})`

status -\> (string)

> The status of the batch evaluation.
>
> Possible values:
>
> - `PENDING`
> - `IN_PROGRESS`
> - `COMPLETED`
> - `COMPLETED_WITH_ERRORS`
> - `FAILED`
> - `STOPPING`
> - `STOPPED`
> - `DELETING`

createdAt -\> (timestamp)

> The timestamp when the batch evaluation was created.

outputConfig -\> (tagged union structure)

> The output configuration specifying where evaluation results are written.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `cloudWatchConfig`.
>
> cloudWatchConfig -\> (structure)
>
> > The CloudWatch Logs configuration for writing evaluation results.
> >
> > logGroupName -\> (string)
> >
> > > The name of the CloudWatch log group where evaluation results will be written. This value doesn’t apply when `resultDestination` is `SOURCE_LOG_GROUP` , because results are written back to the trace source log group. The name can’t be under the service-reserved `/aws/bedrock-agentcore/evaluations/` namespace, apart from the service-managed default group.
> > >
> > > Constraints:
> > >
> > > - pattern: `$|^[.\-_/#A-Za-z0-9]+`
> >
> > logStreamName -\> (string)
> >
> > > The name of the CloudWatch log stream where evaluation results will be written.
> > >
> > > Constraints:
> > >
> > > - pattern: `[^:*]*`
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

tags -\> (map)

> The tags associated with the batch evaluation.
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

kmsKeyArn -\> (string)

> The ARN of the KMS key used to encrypt evaluation data.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`

description -\> (string)

> The description of the batch evaluation.
>
> Constraints:
>
> - min: `0`
> - max: `200`

- [← search-registry-records](search-registry-records.html "previous chapter (use the left arrow)") /
- [start-browser-session →](start-browser-session.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](start-browser-session.html "start-browser-session") \|
- [previous](search-registry-records.html "search-registry-records") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore](index.html) »
- [start-batch-evaluation]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

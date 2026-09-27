---
title: aws bedrock-agentcore get-batch-evaluation
description: \ [aws . bedrock-agentcore \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore/get-batch-evaluation.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore](index.html#cli-aws-bedrock-agentcore) \]

# get-batch-evaluation

## Description

Retrieves detailed information about a batch evaluation, including its status, configuration, results, and any error details.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-2024-02-28/GetBatchEvaluation)

## Synopsis

      get-batch-evaluation
    --batch-evaluation-id <value>
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

`--batch-evaluation-id` (string) \[required\]

> The unique identifier of the batch evaluation to retrieve.
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

batchEvaluationId -\> (string)

> The unique identifier of the batch evaluation.
>
> Constraints:
>
> - pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`

batchEvaluationArn -\> (string)

> The Amazon Resource Name (ARN) of the batch evaluation.

batchEvaluationName -\> (string)

> The name of the batch evaluation.
>
> Constraints:
>
> - pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`

status -\> (string)

> The current status of the batch evaluation.
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

dataSourceConfig -\> (tagged union structure)

> The data source configuration specifying where agent traces are pulled from.
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

evaluationResults -\> (structure)

> The aggregated evaluation results, including session completion counts and evaluator score summaries.
>
> numberOfSessionsCompleted -\> (integer)
>
> > The number of sessions that have been successfully evaluated.
>
> numberOfSessionsInProgress -\> (integer)
>
> > The number of sessions currently being evaluated.
>
> numberOfSessionsFailed -\> (integer)
>
> > The number of sessions that failed evaluation.
>
> totalNumberOfSessions -\> (integer)
>
> > The total number of sessions included in the batch evaluation.
>
> numberOfSessionsIgnored -\> (integer)
>
> > The number of sessions that were ignored during evaluation.
>
> evaluatorSummaries -\> (list)
>
> > A list of per-evaluator summary statistics.
> >
> > (structure)
> >
> > > Summary statistics for a single evaluator within a batch evaluation.
> > >
> > > evaluatorId -\> (string)
> > >
> > > > The unique identifier of the evaluator.
> > >
> > > statistics -\> (structure)
> > >
> > > > The aggregated statistics for this evaluator.
> > > >
> > > > averageScore -\> (double)
> > > >
> > > > > The average score across all evaluated sessions for this evaluator.
> > >
> > > totalEvaluated -\> (integer)
> > >
> > > > The total number of sessions evaluated by this evaluator.
> > >
> > > totalFailed -\> (integer)
> > >
> > > > The total number of sessions that failed evaluation by this evaluator.

failureAnalysisResult -\> (structure)

> The failure analysis results from insights, containing categorized failure clusters with root causes and recommendations.
>
> failures -\> (list) \[required\]
>
> > The list of failure category clusters identified across analyzed sessions.
> >
> > Constraints:
> >
> > - min: `0`
> >
> > (structure)
> >
> > > A top-level failure category identified by clustering similar failure patterns across sessions.
> > >
> > > clusterId -\> (integer) \[required\]
> > >
> > > > The unique identifier of the failure category cluster.
> > >
> > > name -\> (string) \[required\]
> > >
> > > > The name of the failure category.
> > >
> > > description -\> (string) \[required\]
> > >
> > > > A description of the failure category pattern.
> > >
> > > affectedSessionCount -\> (integer) \[required\]
> > >
> > > > The number of sessions affected by this failure category.
> > >
> > > subCategories -\> (list) \[required\]
> > >
> > > > The list of failure subcategories within this category.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0`
> > > >
> > > > (structure)
> > > >
> > > > > A subcategory of failures within a top-level failure category.
> > > > >
> > > > > clusterId -\> (integer) \[required\]
> > > > >
> > > > > > The unique identifier of the failure subcategory cluster.
> > > > >
> > > > > name -\> (string) \[required\]
> > > > >
> > > > > > The name of the failure subcategory.
> > > > >
> > > > > description -\> (string) \[required\]
> > > > >
> > > > > > A description of the failure subcategory pattern.
> > > > >
> > > > > affectedSessionCount -\> (integer) \[required\]
> > > > >
> > > > > > The number of sessions affected by this failure subcategory.
> > > > >
> > > > > rootCauses -\> (list) \[required\]
> > > > >
> > > > > > The list of root cause clusters identified within this subcategory.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `0`
> > > > > >
> > > > > > (structure)
> > > > > >
> > > > > > > A cluster of similar root causes identified within a failure subcategory.
> > > > > > >
> > > > > > > clusterId -\> (integer) \[required\]
> > > > > > >
> > > > > > > > The unique identifier of the root cause cluster.
> > > > > > >
> > > > > > > name -\> (string) \[required\]
> > > > > > >
> > > > > > > > The name of the root cause cluster.
> > > > > > >
> > > > > > > rootCause -\> (string) \[required\]
> > > > > > >
> > > > > > > > The root cause explanation for this cluster of failures.
> > > > > > >
> > > > > > > recommendation -\> (string) \[required\]
> > > > > > >
> > > > > > > > The recommended fix for this root cause.
> > > > > > >
> > > > > > > affectedSessionCount -\> (integer) \[required\]
> > > > > > >
> > > > > > > > The number of sessions affected by this root cause.
> > > > > > >
> > > > > > > affectedSessions -\> (list) \[required\]
> > > > > > >
> > > > > > > > The list of sessions affected by this root cause.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `0`
> > > > > > > >
> > > > > > > > (structure)
> > > > > > > >
> > > > > > > > > A session affected by a detected failure pattern, including root cause details.
> > > > > > > > >
> > > > > > > > > sessionId -\> (string) \[required\]
> > > > > > > > >
> > > > > > > > > > The unique identifier of the affected session.
> > > > > > > > >
> > > > > > > > > explanation -\> (string) \[required\]
> > > > > > > > >
> > > > > > > > > > An explanation of how the failure manifested in this session.
> > > > > > > > >
> > > > > > > > > fixType -\> (string) \[required\]
> > > > > > > > >
> > > > > > > > > > The type of fix recommended for this failure.
> > > > > > > > >
> > > > > > > > > recommendation -\> (string) \[required\]
> > > > > > > > >
> > > > > > > > > > The specific fix recommendation for this session.
> > > > > > > > >
> > > > > > > > > failureSpans -\> (list) \[required\]
> > > > > > > > >
> > > > > > > > > > The list of spans where failures were detected in this session.
> > > > > > > > > >
> > > > > > > > > > Constraints:
> > > > > > > > > >
> > > > > > > > > > - min: `0`
> > > > > > > > > >
> > > > > > > > > > (structure)
> > > > > > > > > >
> > > > > > > > > > > Details about a specific span where a failure was detected.
> > > > > > > > > > >
> > > > > > > > > > > spanId -\> (string) \[required\]
> > > > > > > > > > >
> > > > > > > > > > > > The unique identifier of the span where the failure occurred.
> > > > > > > > > > >
> > > > > > > > > > > traceId -\> (string) \[required\]
> > > > > > > > > > >
> > > > > > > > > > > > The trace identifier associated with the failure span.
> > > > > > > > > > >
> > > > > > > > > > > signals -\> (list) \[required\]
> > > > > > > > > > >
> > > > > > > > > > > > The failure signals detected in this span.
> > > > > > > > > > > >
> > > > > > > > > > > > (structure)
> > > > > > > > > > > >
> > > > > > > > > > > > > A signal indicating a detected failure within a span.
> > > > > > > > > > > > >
> > > > > > > > > > > > > category -\> (string) \[required\]
> > > > > > > > > > > > >
> > > > > > > > > > > > > > The failure category classification for this signal.
> > > > > > > > > > > > > >
> > > > > > > > > > > > > > Possible values:
> > > > > > > > > > > > > >
> > > > > > > > > > > > > > - `execution-error-category-authentication`
> > > > > > > > > > > > > > - `execution-error-category-resource-not-found`
> > > > > > > > > > > > > > - `execution-error-category-service-errors`
> > > > > > > > > > > > > > - `execution-error-category-rate-limiting`
> > > > > > > > > > > > > > - `execution-error-category-formatting`
> > > > > > > > > > > > > > - `execution-error-category-timeout`
> > > > > > > > > > > > > > - `execution-error-category-resource-exhaustion`
> > > > > > > > > > > > > > - `execution-error-category-environment`
> > > > > > > > > > > > > > - `execution-error-category-tool-schema`
> > > > > > > > > > > > > > - `task-instruction-category-non-compliance`
> > > > > > > > > > > > > > - `task-instruction-category-problem-id`
> > > > > > > > > > > > > > - `incorrect-actions-category-tool-selection`
> > > > > > > > > > > > > > - `incorrect-actions-category-poor-information-retrieval`
> > > > > > > > > > > > > > - `incorrect-actions-category-clarification`
> > > > > > > > > > > > > > - `incorrect-actions-category-inappropriate-info-request`
> > > > > > > > > > > > > > - `context-handling-error-category-context-handling-failures`
> > > > > > > > > > > > > > - `hallucination-category-hall-capabilities`
> > > > > > > > > > > > > > - `hallucination-category-hall-misunderstand`
> > > > > > > > > > > > > > - `hallucination-category-hall-usage`
> > > > > > > > > > > > > > - `hallucination-category-hall-history`
> > > > > > > > > > > > > > - `hallucination-category-hall-params`
> > > > > > > > > > > > > > - `hallucination-category-fabricate-tool-outputs`
> > > > > > > > > > > > > > - `repetitive-behavior-category-repetition-tool`
> > > > > > > > > > > > > > - `repetitive-behavior-category-repetition-info`
> > > > > > > > > > > > > > - `repetitive-behavior-category-step-repetition`
> > > > > > > > > > > > > > - `orchestration-related-errors-category-reasoning-mismatch`
> > > > > > > > > > > > > > - `orchestration-related-errors-category-goal-deviation`
> > > > > > > > > > > > > > - `orchestration-related-errors-category-premature-termination`
> > > > > > > > > > > > > > - `orchestration-related-errors-category-unaware-termination`
> > > > > > > > > > > > > > - `llm-output-category-nonsensical`
> > > > > > > > > > > > > > - `configuration-mismatch-category-tool-definition`
> > > > > > > > > > > > > > - `coding-use-case-specific-failure-types-category-edge-case-oversights`
> > > > > > > > > > > > > > - `coding-use-case-specific-failure-types-category-dependency-issues`
> > > > > > > > > > > > > > - `other`
> > > > > > > > > > > > >
> > > > > > > > > > > > > evidence -\> (string) \[required\]
> > > > > > > > > > > > >
> > > > > > > > > > > > > > The evidence supporting the failure detection.
> > > > > > > > > > > > >
> > > > > > > > > > > > > confidence -\> (double) \[required\]
> > > > > > > > > > > > >
> > > > > > > > > > > > > > The confidence score of the failure detection.

userIntentResult -\> (structure)

> The user intent clustering results from insights, containing grouped user intents across evaluated sessions.
>
> userIntents -\> (list) \[required\]
>
> > The list of user intent clusters identified across analyzed sessions.
> >
> > Constraints:
> >
> > - min: `0`
> >
> > (structure)
> >
> > > A cluster of similar user intents identified across sessions.
> > >
> > > clusterId -\> (integer) \[required\]
> > >
> > > > The unique identifier of the user intent cluster.
> > >
> > > name -\> (string) \[required\]
> > >
> > > > The name of the user intent cluster.
> > >
> > > description -\> (string) \[required\]
> > >
> > > > A description of the user intent pattern.
> > >
> > > affectedSessionCount -\> (integer) \[required\]
> > >
> > > > The number of sessions with this user intent.
> > >
> > > affectedSessions -\> (list) \[required\]
> > >
> > > > The list of sessions with this user intent.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0`
> > > >
> > > > (structure)
> > > >
> > > > > A session associated with a user intent cluster.
> > > > >
> > > > > sessionId -\> (string) \[required\]
> > > > >
> > > > > > The unique identifier of the session.
> > > > >
> > > > > userMessages -\> (list) \[required\]
> > > > >
> > > > > > The user messages from this session that contributed to the intent cluster.
> > > > > >
> > > > > > (string)

executionSummaryResult -\> (structure)

> The execution summary clustering results from insights, containing grouped execution patterns across evaluated sessions.
>
> executionSummaries -\> (list) \[required\]
>
> > The list of execution summary clusters identified across analyzed sessions.
> >
> > Constraints:
> >
> > - min: `0`
> >
> > (structure)
> >
> > > A cluster of similar execution patterns identified across sessions.
> > >
> > > clusterId -\> (integer) \[required\]
> > >
> > > > The unique identifier of the execution summary cluster.
> > >
> > > name -\> (string) \[required\]
> > >
> > > > The name of the execution pattern cluster.
> > >
> > > description -\> (string) \[required\]
> > >
> > > > A description of the execution pattern.
> > >
> > > affectedSessionCount -\> (integer) \[required\]
> > >
> > > > The number of sessions with this execution pattern.
> > >
> > > affectedSessions -\> (list) \[required\]
> > >
> > > > The list of sessions with this execution pattern.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0`
> > > >
> > > > (structure)
> > > >
> > > > > A session associated with an execution summary cluster.
> > > > >
> > > > > sessionId -\> (string) \[required\]
> > > > >
> > > > > > The unique identifier of the session.
> > > > >
> > > > > approachTaken -\> (string) \[required\]
> > > > >
> > > > > > The approach taken by the agent during this session.
> > > > >
> > > > > finalOutcome -\> (string) \[required\]
> > > > >
> > > > > > The final outcome of the session.

errorDetails -\> (list)

> The error details if the batch evaluation encountered failures.
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

description -\> (string)

> The description of the batch evaluation.
>
> Constraints:
>
> - min: `0`
> - max: `200`

updatedAt -\> (timestamp)

> The timestamp when the batch evaluation was last updated.

kmsKeyArn -\> (string)

> The ARN of the KMS key used to encrypt evaluation data.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`

- [← get-agent-card](get-agent-card.html "previous chapter (use the left arrow)") /
- [get-browser-session →](get-browser-session.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](get-browser-session.html "get-browser-session") \|
- [previous](get-agent-card.html "get-agent-card") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore](index.html) »
- [get-batch-evaluation]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

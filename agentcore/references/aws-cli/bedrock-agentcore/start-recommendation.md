---
title: aws bedrock-agentcore start-recommendation
description: \ [aws . bedrock-agentcore \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore/start-recommendation.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore](index.html#cli-aws-bedrock-agentcore) \]

# start-recommendation

## Description

Starts a recommendation job that analyzes agent traces and generates optimization suggestions for system prompts or tool descriptions to improve agent performance.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-2024-02-28/StartRecommendation)

`start-recommendation` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

      start-recommendation
    --name <value>
    [--description <value>]
    --type <value>
    --recommendation-config <value>
    [--kms-key-arn <value>]
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

> The name of the recommendation. Must be unique within your account.
>
> Constraints:
>
> - min: `0`
> - max: `100`
> - pattern: `[a-zA-Z][a-zA-Z0-9_-]{0,47}`

`--description` (string)

> The description of the recommendation.
>
> Constraints:
>
> - min: `0`
> - max: `4096`

`--type` (string) \[required\]

> The type of recommendation to generate. Valid values are `SYSTEM_PROMPT_RECOMMENDATION` for system prompt optimization or `TOOL_DESCRIPTION_RECOMMENDATION` for tool description optimization.
>
> Possible values:
>
> - `SYSTEM_PROMPT_RECOMMENDATION`
> - `TOOL_DESCRIPTION_RECOMMENDATION`

`--recommendation-config` (tagged union structure) \[required\]

> The configuration for the recommendation, including the input to optimize, agent traces to analyze, and evaluation settings.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `systemPromptRecommendationConfig`, `toolDescriptionRecommendationConfig`.
>
> systemPromptRecommendationConfig -\> (structure)
>
> > The configuration for a system prompt recommendation.
> >
> > systemPrompt -\> (tagged union structure) \[required\]
> >
> > > The current system prompt to optimize.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `text`, `configurationBundle`.
> > >
> > > text -\> (string)
> > >
> > > > The system prompt text provided inline.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `20000`
> > >
> > > configurationBundle -\> (structure)
> > >
> > > > The system prompt sourced from a configuration bundle version.
> > > >
> > > > bundleArn -\> (string) \[required\]
> > > >
> > > > > The Amazon Resource Name (ARN) of the configuration bundle.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
> > > >
> > > > versionId -\> (string) \[required\]
> > > >
> > > > > The version identifier of the configuration bundle.
> > > >
> > > > systemPromptJsonPath -\> (string) \[required\]
> > > >
> > > > > The JSON path within the configuration bundle that contains the system prompt.
> >
> > agentTraces -\> (tagged union structure) \[required\]
> >
> > > The agent traces to analyze for generating recommendations.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `sessionSpans`, `cloudwatchLogs`, `batchEvaluation`, `onlineEvaluation`.
> > >
> > > sessionSpans -\> (list)
> > >
> > > > Agent traces provided as inline session spans in OpenTelemetry format.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `20000`
> > > >
> > > > (document)
> > >
> > > cloudwatchLogs -\> (structure)
> > >
> > > > Agent traces read from CloudWatch Logs.
> > > >
> > > > logGroupArns -\> (list) \[required\]
> > > >
> > > > > The list of CloudWatch log group ARNs to read agent traces from.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `5`
> > > > >
> > > > > (string)
> > > >
> > > > serviceNames -\> (list) \[required\]
> > > >
> > > > > The list of service names to filter traces within the specified log groups.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `1`
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `256`
> > > > > > - pattern: `[a-zA-Z0-9._-]+`
> > > >
> > > > startTime -\> (timestamp) \[required\]
> > > >
> > > > > The start time of the time range to read traces from.
> > > >
> > > > endTime -\> (timestamp) \[required\]
> > > >
> > > > > The end time of the time range to read traces from.
> > > >
> > > > rule -\> (structure)
> > > >
> > > > > Optional rule configuration for filtering traces.
> > > > >
> > > > > filters -\> (list)
> > > > >
> > > > > > The list of filters to apply when reading agent traces.
> > > > > >
> > > > > > (structure)
> > > > > >
> > > > > > > A filter for narrowing down agent traces from CloudWatch Logs based on key-value comparisons.
> > > > > > >
> > > > > > > key -\> (string) \[required\]
> > > > > > >
> > > > > > > > The key or field name to filter on within the agent trace data.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `256`
> > > > > > > > - pattern: `[a-zA-Z0-9._-]+`
> > > > > > >
> > > > > > > operator -\> (string) \[required\]
> > > > > > >
> > > > > > > > The comparison operator to use for filtering.
> > > > > > > >
> > > > > > > > Possible values:
> > > > > > > >
> > > > > > > > - `Equals`
> > > > > > > > - `NotEquals`
> > > > > > > > - `GreaterThan`
> > > > > > > > - `LessThan`
> > > > > > > > - `GreaterThanOrEqual`
> > > > > > > > - `LessThanOrEqual`
> > > > > > > > - `Contains`
> > > > > > > > - `NotContains`
> > > > > > >
> > > > > > > value -\> (tagged union structure) \[required\]
> > > > > > >
> > > > > > > > The value to compare against using the specified operator.
> > > > > > > >
> > > > > > > > ### Note
> > > > > > > >
> > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `doubleValue`, `booleanValue`.
> > > > > > > >
> > > > > > > > stringValue -\> (string)
> > > > > > > >
> > > > > > > > > A string value for text-based filtering.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `0`
> > > > > > > > > - max: `1024`
> > > > > > > >
> > > > > > > > doubleValue -\> (double)
> > > > > > > >
> > > > > > > > > A numeric value for numerical filtering and comparisons.
> > > > > > > >
> > > > > > > > booleanValue -\> (boolean)
> > > > > > > >
> > > > > > > > > A boolean value for true/false filtering conditions.
> > >
> > > batchEvaluation -\> (structure)
> > >
> > > > Use a completed batch evaluation as the source of agent traces.
> > > >
> > > > batchEvaluationArn -\> (string) \[required\]
> > > >
> > > > > The ARN of the completed batch evaluation to use as the trace source.
> > >
> > > onlineEvaluation -\> (structure)
> > >
> > > > Agent traces from an online evaluation configuration over a specified time range.
> > > >
> > > > onlineEvaluationConfigArn -\> (string) \[required\]
> > > >
> > > > > The ARN of the online evaluation configuration to reuse sessions from.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:online-evaluation-config\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
> > > >
> > > > startTime -\> (timestamp) \[required\]
> > > >
> > > > > The start time of the time range. Only sessions evaluated at or after this timestamp are included.
> > > >
> > > > endTime -\> (timestamp) \[required\]
> > > >
> > > > > The end time of the time range. Only sessions evaluated before this timestamp are included.
> >
> > evaluationConfig -\> (structure)
> >
> > > The evaluation configuration specifying which evaluator to use for assessing recommendation quality.
> > >
> > > evaluators -\> (list) \[required\]
> > >
> > > > The list of evaluators to use for assessing recommendation quality.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `1`
> > > >
> > > > (structure)
> > > >
> > > > > A reference to an evaluator used for recommendation assessment.
> > > > >
> > > > > evaluatorArn -\> (string) \[required\]
> > > > >
> > > > > > The Amazon Resource Name (ARN) of the evaluator.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:evaluator\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}$|^arn:aws[a-zA-Z-]*:bedrock-agentcore:::evaluator/(Builtin|ThirdParty)\.[a-zA-Z0-9._-]+`
>
> toolDescriptionRecommendationConfig -\> (structure)
>
> > The configuration for a tool description recommendation.
> >
> > toolDescription -\> (tagged union structure) \[required\]
> >
> > > The current tool descriptions to optimize.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `toolDescriptionText`, `configurationBundle`.
> > >
> > > toolDescriptionText -\> (structure)
> > >
> > > > Tool descriptions provided as inline text.
> > > >
> > > > tools -\> (list) \[required\]
> > > >
> > > > > The list of tool descriptions to optimize.
> > > > >
> > > > > (structure)
> > > > >
> > > > > > A tool description input containing the tool name and its current description.
> > > > > >
> > > > > > toolName -\> (string) \[required\]
> > > > > >
> > > > > > > The name of the tool.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `256`
> > > > > > > - pattern: `[a-zA-Z0-9_\-\.]+`
> > > > > >
> > > > > > toolDescription -\> (tagged union structure) \[required\]
> > > > > >
> > > > > > > The current description of the tool to optimize.
> > > > > > >
> > > > > > > ### Note
> > > > > > >
> > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `text`.
> > > > > > >
> > > > > > > text -\> (string)
> > > > > > >
> > > > > > > > The tool description as inline text.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `20000`
> > >
> > > configurationBundle -\> (structure)
> > >
> > > > Tool descriptions sourced from a configuration bundle version.
> > > >
> > > > bundleArn -\> (string) \[required\]
> > > >
> > > > > The Amazon Resource Name (ARN) of the configuration bundle.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
> > > >
> > > > versionId -\> (string) \[required\]
> > > >
> > > > > The version identifier of the configuration bundle.
> > > >
> > > > tools -\> (list) \[required\]
> > > >
> > > > > The list of tool entries mapping tool names to their JSON paths within the bundle.
> > > > >
> > > > > (structure)
> > > > >
> > > > > > Maps a tool name to its JSON path within a configuration bundle.
> > > > > >
> > > > > > toolName -\> (string) \[required\]
> > > > > >
> > > > > > > The name of the tool.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `256`
> > > > > > > - pattern: `[a-zA-Z0-9_\-\.]+`
> > > > > >
> > > > > > toolDescriptionJsonPath -\> (string) \[required\]
> > > > > >
> > > > > > > The JSON path within the configuration bundle’s components that contains the tool description.
> >
> > agentTraces -\> (tagged union structure) \[required\]
> >
> > > The agent traces to analyze for generating tool description recommendations.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `sessionSpans`, `cloudwatchLogs`, `batchEvaluation`, `onlineEvaluation`.
> > >
> > > sessionSpans -\> (list)
> > >
> > > > Agent traces provided as inline session spans in OpenTelemetry format.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `20000`
> > > >
> > > > (document)
> > >
> > > cloudwatchLogs -\> (structure)
> > >
> > > > Agent traces read from CloudWatch Logs.
> > > >
> > > > logGroupArns -\> (list) \[required\]
> > > >
> > > > > The list of CloudWatch log group ARNs to read agent traces from.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `5`
> > > > >
> > > > > (string)
> > > >
> > > > serviceNames -\> (list) \[required\]
> > > >
> > > > > The list of service names to filter traces within the specified log groups.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `1`
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `256`
> > > > > > - pattern: `[a-zA-Z0-9._-]+`
> > > >
> > > > startTime -\> (timestamp) \[required\]
> > > >
> > > > > The start time of the time range to read traces from.
> > > >
> > > > endTime -\> (timestamp) \[required\]
> > > >
> > > > > The end time of the time range to read traces from.
> > > >
> > > > rule -\> (structure)
> > > >
> > > > > Optional rule configuration for filtering traces.
> > > > >
> > > > > filters -\> (list)
> > > > >
> > > > > > The list of filters to apply when reading agent traces.
> > > > > >
> > > > > > (structure)
> > > > > >
> > > > > > > A filter for narrowing down agent traces from CloudWatch Logs based on key-value comparisons.
> > > > > > >
> > > > > > > key -\> (string) \[required\]
> > > > > > >
> > > > > > > > The key or field name to filter on within the agent trace data.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `256`
> > > > > > > > - pattern: `[a-zA-Z0-9._-]+`
> > > > > > >
> > > > > > > operator -\> (string) \[required\]
> > > > > > >
> > > > > > > > The comparison operator to use for filtering.
> > > > > > > >
> > > > > > > > Possible values:
> > > > > > > >
> > > > > > > > - `Equals`
> > > > > > > > - `NotEquals`
> > > > > > > > - `GreaterThan`
> > > > > > > > - `LessThan`
> > > > > > > > - `GreaterThanOrEqual`
> > > > > > > > - `LessThanOrEqual`
> > > > > > > > - `Contains`
> > > > > > > > - `NotContains`
> > > > > > >
> > > > > > > value -\> (tagged union structure) \[required\]
> > > > > > >
> > > > > > > > The value to compare against using the specified operator.
> > > > > > > >
> > > > > > > > ### Note
> > > > > > > >
> > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `doubleValue`, `booleanValue`.
> > > > > > > >
> > > > > > > > stringValue -\> (string)
> > > > > > > >
> > > > > > > > > A string value for text-based filtering.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `0`
> > > > > > > > > - max: `1024`
> > > > > > > >
> > > > > > > > doubleValue -\> (double)
> > > > > > > >
> > > > > > > > > A numeric value for numerical filtering and comparisons.
> > > > > > > >
> > > > > > > > booleanValue -\> (boolean)
> > > > > > > >
> > > > > > > > > A boolean value for true/false filtering conditions.
> > >
> > > batchEvaluation -\> (structure)
> > >
> > > > Use a completed batch evaluation as the source of agent traces.
> > > >
> > > > batchEvaluationArn -\> (string) \[required\]
> > > >
> > > > > The ARN of the completed batch evaluation to use as the trace source.
> > >
> > > onlineEvaluation -\> (structure)
> > >
> > > > Agent traces from an online evaluation configuration over a specified time range.
> > > >
> > > > onlineEvaluationConfigArn -\> (string) \[required\]
> > > >
> > > > > The ARN of the online evaluation configuration to reuse sessions from.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:online-evaluation-config\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
> > > >
> > > > startTime -\> (timestamp) \[required\]
> > > >
> > > > > The start time of the time range. Only sessions evaluated at or after this timestamp are included.
> > > >
> > > > endTime -\> (timestamp) \[required\]
> > > >
> > > > > The end time of the time range. Only sessions evaluated before this timestamp are included.

JSON Syntax:

    {
      "systemPromptRecommendationConfig": {
        "systemPrompt": {
          "text": "string",
          "configurationBundle": {
            "bundleArn": "string",
            "versionId": "string",
            "systemPromptJsonPath": "string"
          }
        },
        "agentTraces": {
          "sessionSpans": [
            {...}
            ...
          ],
          "cloudwatchLogs": {
            "logGroupArns": ["string", ...],
            "serviceNames": ["string", ...],
            "startTime": timestamp,
            "endTime": timestamp,
            "rule": {
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
              ]
            }
          },
          "batchEvaluation": {
            "batchEvaluationArn": "string"
          },
          "onlineEvaluation": {
            "onlineEvaluationConfigArn": "string",
            "startTime": timestamp,
            "endTime": timestamp
          }
        },
        "evaluationConfig": {
          "evaluators": [
            {
              "evaluatorArn": "string"
            }
            ...
          ]
        }
      },
      "toolDescriptionRecommendationConfig": {
        "toolDescription": {
          "toolDescriptionText": {
            "tools": [
              {
                "toolName": "string",
                "toolDescription": {
                  "text": "string"
                }
              }
              ...
            ]
          },
          "configurationBundle": {
            "bundleArn": "string",
            "versionId": "string",
            "tools": [
              {
                "toolName": "string",
                "toolDescriptionJsonPath": "string"
              }
              ...
            ]
          }
        },
        "agentTraces": {
          "sessionSpans": [
            {...}
            ...
          ],
          "cloudwatchLogs": {
            "logGroupArns": ["string", ...],
            "serviceNames": ["string", ...],
            "startTime": timestamp,
            "endTime": timestamp,
            "rule": {
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
              ]
            }
          },
          "batchEvaluation": {
            "batchEvaluationArn": "string"
          },
          "onlineEvaluation": {
            "onlineEvaluationConfigArn": "string",
            "startTime": timestamp,
            "endTime": timestamp
          }
        }
      }
    }

`--kms-key-arn` (string)

> The ARN of the KMS key used to encrypt recommendation data. If provided, customer data is encrypted at rest with the specified key.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`

`--client-token` (string)

> A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.
>
> Constraints:
>
> - min: `33`
> - max: `256`
> - pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`

`--tags` (map)

> A map of tag keys and values to associate with the recommendation.
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

recommendationId -\> (string)

> The unique identifier of the created recommendation.
>
> Constraints:
>
> - pattern: `[0-9a-zA-Z_-]{1,48}-[0-9A-Z]{10}`

recommendationArn -\> (string)

> The Amazon Resource Name (ARN) of the created recommendation.
>
> Constraints:
>
> - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:recommendation/[0-9a-zA-Z_-]{1,48}-[0-9A-Z]{10}`

name -\> (string)

> The name of the recommendation.
>
> Constraints:
>
> - min: `0`
> - max: `100`
> - pattern: `[a-zA-Z][a-zA-Z0-9_-]{0,47}`

description -\> (string)

> The description of the recommendation.
>
> Constraints:
>
> - min: `0`
> - max: `4096`

type -\> (string)

> The type of recommendation.
>
> Possible values:
>
> - `SYSTEM_PROMPT_RECOMMENDATION`
> - `TOOL_DESCRIPTION_RECOMMENDATION`

recommendationConfig -\> (tagged union structure)

> The configuration for the recommendation.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `systemPromptRecommendationConfig`, `toolDescriptionRecommendationConfig`.
>
> systemPromptRecommendationConfig -\> (structure)
>
> > The configuration for a system prompt recommendation.
> >
> > systemPrompt -\> (tagged union structure) \[required\]
> >
> > > The current system prompt to optimize.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `text`, `configurationBundle`.
> > >
> > > text -\> (string)
> > >
> > > > The system prompt text provided inline.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `20000`
> > >
> > > configurationBundle -\> (structure)
> > >
> > > > The system prompt sourced from a configuration bundle version.
> > > >
> > > > bundleArn -\> (string) \[required\]
> > > >
> > > > > The Amazon Resource Name (ARN) of the configuration bundle.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
> > > >
> > > > versionId -\> (string) \[required\]
> > > >
> > > > > The version identifier of the configuration bundle.
> > > >
> > > > systemPromptJsonPath -\> (string) \[required\]
> > > >
> > > > > The JSON path within the configuration bundle that contains the system prompt.
> >
> > agentTraces -\> (tagged union structure) \[required\]
> >
> > > The agent traces to analyze for generating recommendations.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `sessionSpans`, `cloudwatchLogs`, `batchEvaluation`, `onlineEvaluation`.
> > >
> > > sessionSpans -\> (list)
> > >
> > > > Agent traces provided as inline session spans in OpenTelemetry format.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `20000`
> > > >
> > > > (document)
> > >
> > > cloudwatchLogs -\> (structure)
> > >
> > > > Agent traces read from CloudWatch Logs.
> > > >
> > > > logGroupArns -\> (list) \[required\]
> > > >
> > > > > The list of CloudWatch log group ARNs to read agent traces from.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `5`
> > > > >
> > > > > (string)
> > > >
> > > > serviceNames -\> (list) \[required\]
> > > >
> > > > > The list of service names to filter traces within the specified log groups.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `1`
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `256`
> > > > > > - pattern: `[a-zA-Z0-9._-]+`
> > > >
> > > > startTime -\> (timestamp) \[required\]
> > > >
> > > > > The start time of the time range to read traces from.
> > > >
> > > > endTime -\> (timestamp) \[required\]
> > > >
> > > > > The end time of the time range to read traces from.
> > > >
> > > > rule -\> (structure)
> > > >
> > > > > Optional rule configuration for filtering traces.
> > > > >
> > > > > filters -\> (list)
> > > > >
> > > > > > The list of filters to apply when reading agent traces.
> > > > > >
> > > > > > (structure)
> > > > > >
> > > > > > > A filter for narrowing down agent traces from CloudWatch Logs based on key-value comparisons.
> > > > > > >
> > > > > > > key -\> (string) \[required\]
> > > > > > >
> > > > > > > > The key or field name to filter on within the agent trace data.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `256`
> > > > > > > > - pattern: `[a-zA-Z0-9._-]+`
> > > > > > >
> > > > > > > operator -\> (string) \[required\]
> > > > > > >
> > > > > > > > The comparison operator to use for filtering.
> > > > > > > >
> > > > > > > > Possible values:
> > > > > > > >
> > > > > > > > - `Equals`
> > > > > > > > - `NotEquals`
> > > > > > > > - `GreaterThan`
> > > > > > > > - `LessThan`
> > > > > > > > - `GreaterThanOrEqual`
> > > > > > > > - `LessThanOrEqual`
> > > > > > > > - `Contains`
> > > > > > > > - `NotContains`
> > > > > > >
> > > > > > > value -\> (tagged union structure) \[required\]
> > > > > > >
> > > > > > > > The value to compare against using the specified operator.
> > > > > > > >
> > > > > > > > ### Note
> > > > > > > >
> > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `doubleValue`, `booleanValue`.
> > > > > > > >
> > > > > > > > stringValue -\> (string)
> > > > > > > >
> > > > > > > > > A string value for text-based filtering.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `0`
> > > > > > > > > - max: `1024`
> > > > > > > >
> > > > > > > > doubleValue -\> (double)
> > > > > > > >
> > > > > > > > > A numeric value for numerical filtering and comparisons.
> > > > > > > >
> > > > > > > > booleanValue -\> (boolean)
> > > > > > > >
> > > > > > > > > A boolean value for true/false filtering conditions.
> > >
> > > batchEvaluation -\> (structure)
> > >
> > > > Use a completed batch evaluation as the source of agent traces.
> > > >
> > > > batchEvaluationArn -\> (string) \[required\]
> > > >
> > > > > The ARN of the completed batch evaluation to use as the trace source.
> > >
> > > onlineEvaluation -\> (structure)
> > >
> > > > Agent traces from an online evaluation configuration over a specified time range.
> > > >
> > > > onlineEvaluationConfigArn -\> (string) \[required\]
> > > >
> > > > > The ARN of the online evaluation configuration to reuse sessions from.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:online-evaluation-config\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
> > > >
> > > > startTime -\> (timestamp) \[required\]
> > > >
> > > > > The start time of the time range. Only sessions evaluated at or after this timestamp are included.
> > > >
> > > > endTime -\> (timestamp) \[required\]
> > > >
> > > > > The end time of the time range. Only sessions evaluated before this timestamp are included.
> >
> > evaluationConfig -\> (structure)
> >
> > > The evaluation configuration specifying which evaluator to use for assessing recommendation quality.
> > >
> > > evaluators -\> (list) \[required\]
> > >
> > > > The list of evaluators to use for assessing recommendation quality.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `1`
> > > >
> > > > (structure)
> > > >
> > > > > A reference to an evaluator used for recommendation assessment.
> > > > >
> > > > > evaluatorArn -\> (string) \[required\]
> > > > >
> > > > > > The Amazon Resource Name (ARN) of the evaluator.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:evaluator\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}$|^arn:aws[a-zA-Z-]*:bedrock-agentcore:::evaluator/(Builtin|ThirdParty)\.[a-zA-Z0-9._-]+`
>
> toolDescriptionRecommendationConfig -\> (structure)
>
> > The configuration for a tool description recommendation.
> >
> > toolDescription -\> (tagged union structure) \[required\]
> >
> > > The current tool descriptions to optimize.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `toolDescriptionText`, `configurationBundle`.
> > >
> > > toolDescriptionText -\> (structure)
> > >
> > > > Tool descriptions provided as inline text.
> > > >
> > > > tools -\> (list) \[required\]
> > > >
> > > > > The list of tool descriptions to optimize.
> > > > >
> > > > > (structure)
> > > > >
> > > > > > A tool description input containing the tool name and its current description.
> > > > > >
> > > > > > toolName -\> (string) \[required\]
> > > > > >
> > > > > > > The name of the tool.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `256`
> > > > > > > - pattern: `[a-zA-Z0-9_\-\.]+`
> > > > > >
> > > > > > toolDescription -\> (tagged union structure) \[required\]
> > > > > >
> > > > > > > The current description of the tool to optimize.
> > > > > > >
> > > > > > > ### Note
> > > > > > >
> > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `text`.
> > > > > > >
> > > > > > > text -\> (string)
> > > > > > >
> > > > > > > > The tool description as inline text.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `20000`
> > >
> > > configurationBundle -\> (structure)
> > >
> > > > Tool descriptions sourced from a configuration bundle version.
> > > >
> > > > bundleArn -\> (string) \[required\]
> > > >
> > > > > The Amazon Resource Name (ARN) of the configuration bundle.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:configuration-bundle/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
> > > >
> > > > versionId -\> (string) \[required\]
> > > >
> > > > > The version identifier of the configuration bundle.
> > > >
> > > > tools -\> (list) \[required\]
> > > >
> > > > > The list of tool entries mapping tool names to their JSON paths within the bundle.
> > > > >
> > > > > (structure)
> > > > >
> > > > > > Maps a tool name to its JSON path within a configuration bundle.
> > > > > >
> > > > > > toolName -\> (string) \[required\]
> > > > > >
> > > > > > > The name of the tool.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `256`
> > > > > > > - pattern: `[a-zA-Z0-9_\-\.]+`
> > > > > >
> > > > > > toolDescriptionJsonPath -\> (string) \[required\]
> > > > > >
> > > > > > > The JSON path within the configuration bundle’s components that contains the tool description.
> >
> > agentTraces -\> (tagged union structure) \[required\]
> >
> > > The agent traces to analyze for generating tool description recommendations.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `sessionSpans`, `cloudwatchLogs`, `batchEvaluation`, `onlineEvaluation`.
> > >
> > > sessionSpans -\> (list)
> > >
> > > > Agent traces provided as inline session spans in OpenTelemetry format.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `20000`
> > > >
> > > > (document)
> > >
> > > cloudwatchLogs -\> (structure)
> > >
> > > > Agent traces read from CloudWatch Logs.
> > > >
> > > > logGroupArns -\> (list) \[required\]
> > > >
> > > > > The list of CloudWatch log group ARNs to read agent traces from.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `5`
> > > > >
> > > > > (string)
> > > >
> > > > serviceNames -\> (list) \[required\]
> > > >
> > > > > The list of service names to filter traces within the specified log groups.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `1`
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `256`
> > > > > > - pattern: `[a-zA-Z0-9._-]+`
> > > >
> > > > startTime -\> (timestamp) \[required\]
> > > >
> > > > > The start time of the time range to read traces from.
> > > >
> > > > endTime -\> (timestamp) \[required\]
> > > >
> > > > > The end time of the time range to read traces from.
> > > >
> > > > rule -\> (structure)
> > > >
> > > > > Optional rule configuration for filtering traces.
> > > > >
> > > > > filters -\> (list)
> > > > >
> > > > > > The list of filters to apply when reading agent traces.
> > > > > >
> > > > > > (structure)
> > > > > >
> > > > > > > A filter for narrowing down agent traces from CloudWatch Logs based on key-value comparisons.
> > > > > > >
> > > > > > > key -\> (string) \[required\]
> > > > > > >
> > > > > > > > The key or field name to filter on within the agent trace data.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `256`
> > > > > > > > - pattern: `[a-zA-Z0-9._-]+`
> > > > > > >
> > > > > > > operator -\> (string) \[required\]
> > > > > > >
> > > > > > > > The comparison operator to use for filtering.
> > > > > > > >
> > > > > > > > Possible values:
> > > > > > > >
> > > > > > > > - `Equals`
> > > > > > > > - `NotEquals`
> > > > > > > > - `GreaterThan`
> > > > > > > > - `LessThan`
> > > > > > > > - `GreaterThanOrEqual`
> > > > > > > > - `LessThanOrEqual`
> > > > > > > > - `Contains`
> > > > > > > > - `NotContains`
> > > > > > >
> > > > > > > value -\> (tagged union structure) \[required\]
> > > > > > >
> > > > > > > > The value to compare against using the specified operator.
> > > > > > > >
> > > > > > > > ### Note
> > > > > > > >
> > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `stringValue`, `doubleValue`, `booleanValue`.
> > > > > > > >
> > > > > > > > stringValue -\> (string)
> > > > > > > >
> > > > > > > > > A string value for text-based filtering.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `0`
> > > > > > > > > - max: `1024`
> > > > > > > >
> > > > > > > > doubleValue -\> (double)
> > > > > > > >
> > > > > > > > > A numeric value for numerical filtering and comparisons.
> > > > > > > >
> > > > > > > > booleanValue -\> (boolean)
> > > > > > > >
> > > > > > > > > A boolean value for true/false filtering conditions.
> > >
> > > batchEvaluation -\> (structure)
> > >
> > > > Use a completed batch evaluation as the source of agent traces.
> > > >
> > > > batchEvaluationArn -\> (string) \[required\]
> > > >
> > > > > The ARN of the completed batch evaluation to use as the trace source.
> > >
> > > onlineEvaluation -\> (structure)
> > >
> > > > Agent traces from an online evaluation configuration over a specified time range.
> > > >
> > > > onlineEvaluationConfigArn -\> (string) \[required\]
> > > >
> > > > > The ARN of the online evaluation configuration to reuse sessions from.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:online-evaluation-config\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
> > > >
> > > > startTime -\> (timestamp) \[required\]
> > > >
> > > > > The start time of the time range. Only sessions evaluated at or after this timestamp are included.
> > > >
> > > > endTime -\> (timestamp) \[required\]
> > > >
> > > > > The end time of the time range. Only sessions evaluated before this timestamp are included.

status -\> (string)

> The status of the recommendation.
>
> Possible values:
>
> - `PENDING`
> - `IN_PROGRESS`
> - `COMPLETED`
> - `FAILED`
> - `DELETING`

createdAt -\> (timestamp)

> The timestamp when the recommendation was created.

updatedAt -\> (timestamp)

> The timestamp when the recommendation was last updated.

- [← start-memory-extraction-job](start-memory-extraction-job.html "previous chapter (use the left arrow)") /
- [stop-batch-evaluation →](stop-batch-evaluation.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](stop-batch-evaluation.html "stop-batch-evaluation") \|
- [previous](start-memory-extraction-job.html "start-memory-extraction-job") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore](index.html) »
- [start-recommendation]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

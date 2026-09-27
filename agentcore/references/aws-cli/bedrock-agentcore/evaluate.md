---
title: aws bedrock-agentcore evaluate
description: \ [aws . bedrock-agentcore \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore/evaluate.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore](index.html#cli-aws-bedrock-agentcore) \]

# evaluate

## Description

Performs on-demand evaluation of agent traces using a specified evaluator. This synchronous API accepts traces in OpenTelemetry format and returns immediate scoring results with detailed explanations.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-2024-02-28/Evaluate)

`evaluate` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

      evaluate
    --evaluator-id <value>
    --evaluation-input <value>
    [--evaluation-target <value>]
    [--evaluation-reference-inputs <value>]
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

`--evaluator-id` (string) \[required\]

> The unique identifier of the evaluator to use for scoring. Can be a built-in evaluator (e.g., `Builtin.Helpfulness` , `Builtin.Correctness` ) or a custom evaluator Id created through the control plane API.
>
> Constraints:
>
> - min: `1`
> - max: `111`
> - pattern: `(Builtin\.[a-zA-Z0-9._-]+|ThirdParty\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})`

`--evaluation-input` (tagged union structure) \[required\]

> The input data containing agent session spans to be evaluated. Includes a list of spans in OpenTelemetry format from supported frameworks like Strands (AgentCore Runtime) or LangGraph with OpenInference instrumentation.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `sessionSpans`.
>
> sessionSpans -\> (list)
>
> > The collection of spans representing agent execution traces within a session. Each span contains detailed information about tool calls, model interactions, and other agent activities that can be evaluated for quality and performance.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `20000`
> >
> > (document)

JSON Syntax:

    {
      "sessionSpans": [
        {...}
        ...
      ]
    }

`--evaluation-target` (tagged union structure)

> The specific trace or span IDs to evaluate within the provided input. Allows targeting evaluation at different levels: individual tool calls, single request-response interactions (traces), or entire conversation sessions.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `spanIds`, `traceIds`.
>
> spanIds -\> (list)
>
> > The list of specific span IDs to evaluate within the provided traces. Used to target evaluation at individual tool calls or specific operations within the agent’s execution flow.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `10`
> >
> > (string)
> >
> > > Constraints:
> > >
> > > - min: `16`
> > > - max: `16`
>
> traceIds -\> (list)
>
> > The list of trace IDs to evaluate, representing complete request-response interactions. Used to evaluate entire conversation turns or specific agent interactions within a session.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `10`
> >
> > (string)
> >
> > > Constraints:
> > >
> > > - min: `32`
> > > - max: `32`

Shorthand Syntax:

    spanIds=string,string,traceIds=string,string

JSON Syntax:

    {
      "spanIds": ["string", ...],
      "traceIds": ["string", ...]
    }

`--evaluation-reference-inputs` (list)

> Ground truth data to compare against agent responses during evaluation. Allows to provide expected responses, assertions, and expected tool trajectories at different evaluation levels. Session-level reference inputs apply to the entire conversation, while trace-level reference inputs target specific request-response interactions identified by trace ID.
>
> Constraints:
>
> - min: `1`
> - max: `1000`
>
> (structure)
>
> > A reference input containing ground truth data for evaluation, scoped to a specific context level (session or trace) through its span context.
> >
> > context -\> (tagged union structure) \[required\]
> >
> > > The span context that identifies which session or trace this reference input applies to, used for correlating ground truth with agent output.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `spanContext`.
> > >
> > > spanContext -\> (structure)
> > >
> > > > The span context information that uniquely identifies the trace and span being evaluated, including session ID, trace ID, and span ID for precise targeting within the agent’s execution flow.
> > > >
> > > > sessionId -\> (string) \[required\]
> > > >
> > > > > The unique identifier of the session containing this span. Sessions represent complete conversation flows and are detected using configurable `SessionTimeoutMinutes` (default 15 minutes).
> > > >
> > > > traceId -\> (string)
> > > >
> > > > > The unique identifier of the trace containing this span. Traces represent individual request-response interactions within a session and group related spans together.
> > > >
> > > > spanId -\> (string)
> > > >
> > > > > The unique identifier of the specific span being referenced. Spans represent individual operations like tool calls, model invocations, or other discrete actions within the agent’s execution.
> >
> > expectedResponse -\> (tagged union structure)
> >
> > > The expected response for trace-level evaluation. Built-in evaluators that support this field compare the agent’s actual response against this value for assessment. Custom evaluators can access it through the `{expected_response}` placeholder in their instructions.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `text`.
> > >
> > > text -\> (string)
> > >
> > > > The text content of the ground truth data. Used for expected response text and assertion statements.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `100000`
> >
> > assertions -\> (list)
> >
> > > A list of assertion statements for session-level evaluation. Each assertion describes an expected behavior or outcome the agent should demonstrate during the session.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `100`
> > >
> > > (tagged union structure)
> > >
> > > > A content block for ground truth data in evaluation reference inputs. Supports text content for expected responses and assertions.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `text`.
> > > >
> > > > text -\> (string)
> > > >
> > > > > The text content of the ground truth data. Used for expected response text and assertion statements.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `100000`
> >
> > expectedTrajectory -\> (structure)
> >
> > > The expected tool call sequence for session-level trajectory evaluation. Contains a list of tool names representing the tools the agent is expected to invoke.
> > >
> > > toolNames -\> (list)
> > >
> > > > The list of tool names representing the expected tool call sequence.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0`
> > > > - max: `1000`
> > > >
> > > > (string)
> > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `500`

Shorthand Syntax:

    context={spanContext={sessionId=string,traceId=string,spanId=string}},expectedResponse={text=string},assertions=[{text=string},{text=string}],expectedTrajectory={toolNames=[string,string]} ...

JSON Syntax:

    [
      {
        "context": {
          "spanContext": {
            "sessionId": "string",
            "traceId": "string",
            "spanId": "string"
          }
        },
        "expectedResponse": {
          "text": "string"
        },
        "assertions": [
          {
            "text": "string"
          }
          ...
        ],
        "expectedTrajectory": {
          "toolNames": ["string", ...]
        }
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

evaluationResults -\> (list)

> The detailed evaluation results containing scores, explanations, and metadata. Includes the evaluator information, numerical or categorical ratings based on the evaluator’s rating scale, and token usage statistics for the evaluation process.
>
> (structure)
>
> > The comprehensive result of an evaluation containing the score, explanation, evaluator metadata, and execution details. Provides both quantitative ratings and qualitative insights about agent performance.
> >
> > evaluatorArn -\> (string) \[required\]
> >
> > > The Amazon Resource Name (ARN) of the evaluator used to generate this result. For custom evaluators, this is the full ARN; for built-in evaluators, this follows the pattern `Builtin.{EvaluatorName}` .
> > >
> > > Constraints:
> > >
> > > - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:evaluator\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}$|^arn:aws[a-zA-Z-]*:bedrock-agentcore:::evaluator/(Builtin|ThirdParty)\.[a-zA-Z0-9._-]+`
> >
> > evaluatorId -\> (string) \[required\]
> >
> > > The unique identifier of the evaluator that produced this result. This matches the `evaluatorId` provided in the evaluation request and can be used to identify which evaluator generated specific results.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `111`
> > > - pattern: `(Builtin\.[a-zA-Z0-9._-]+|ThirdParty\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})`
> >
> > evaluatorName -\> (string) \[required\]
> >
> > > The human-readable name of the evaluator used for this evaluation. For built-in evaluators, this is the descriptive name (e.g., “Helpfulness”, “Correctness”); for custom evaluators, this is the user-defined name.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `48`
> > > - pattern: `(Builtin\.[a-zA-Z0-9._-]+|ThirdParty\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9_]{0,47})`
> >
> > explanation -\> (string)
> >
> > > The detailed explanation provided by the evaluator describing the reasoning behind the assigned score. This qualitative feedback helps understand why specific ratings were given and provides actionable insights for improvement.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `2048`
> >
> > context -\> (tagged union structure) \[required\]
> >
> > > The contextual information associated with this evaluation result, including span context details that identify the specific traces and sessions that were evaluated.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `spanContext`.
> > >
> > > spanContext -\> (structure)
> > >
> > > > The span context information that uniquely identifies the trace and span being evaluated, including session ID, trace ID, and span ID for precise targeting within the agent’s execution flow.
> > > >
> > > > sessionId -\> (string) \[required\]
> > > >
> > > > > The unique identifier of the session containing this span. Sessions represent complete conversation flows and are detected using configurable `SessionTimeoutMinutes` (default 15 minutes).
> > > >
> > > > traceId -\> (string)
> > > >
> > > > > The unique identifier of the trace containing this span. Traces represent individual request-response interactions within a session and group related spans together.
> > > >
> > > > spanId -\> (string)
> > > >
> > > > > The unique identifier of the specific span being referenced. Spans represent individual operations like tool calls, model invocations, or other discrete actions within the agent’s execution.
> >
> > value -\> (double)
> >
> > > The numerical score assigned by the evaluator according to its configured rating scale. For numerical scales, this is a decimal value within the defined range. This field is not allowed for categorical scales.
> >
> > label -\> (string)
> >
> > > The categorical label assigned by the evaluator when using a categorical rating scale. This provides a human-readable description of the evaluation result (e.g., “Excellent”, “Good”, “Poor”) corresponding to the numerical value. For numerical scales, this field is optional and provides a natural language explanation of what the value means (e.g., value 0.5 = “Somewhat Helpful”).
> >
> > tokenUsage -\> (structure)
> >
> > > The token consumption statistics for this evaluation, including input tokens, output tokens, and total tokens used by the underlying language model during the evaluation process.
> > >
> > > inputTokens -\> (integer)
> > >
> > > > The number of tokens consumed for input processing during the evaluation. Includes tokens from the evaluation prompt, agent traces, and any additional context provided to the evaluator model.
> > >
> > > outputTokens -\> (integer)
> > >
> > > > The number of tokens generated by the evaluator model in its response. Includes tokens for the score, explanation, and any additional output produced during the evaluation process.
> > >
> > > totalTokens -\> (integer)
> > >
> > > > The total number of tokens consumed during the evaluation, calculated as the sum of input and output tokens. Used for cost calculation and rate limiting within the service limits.
> >
> > errorMessage -\> (string)
> >
> > > The error message describing what went wrong if the evaluation failed. Provides detailed information about evaluation failures to help diagnose and resolve issues with evaluator configuration or input data.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `2048`
> >
> > errorCode -\> (string)
> >
> > > The error code indicating the type of failure that occurred during evaluation. Used to programmatically identify and handle different categories of evaluation errors.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `1024`
> >
> > ignoredReferenceInputFields -\> (list)
> >
> > > The list of reference input field names that were provided but not used by the evaluator. Helps identify which ground truth data was not consumed during evaluation.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `100`
> > >
> > > (string)
> > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `1000`

- [← delete-recommendation](delete-recommendation.html "previous chapter (use the left arrow)") /
- [get-ab-test →](get-ab-test.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](get-ab-test.html "get-ab-test") \|
- [previous](delete-recommendation.html "delete-recommendation") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore](index.html) »
- [evaluate]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

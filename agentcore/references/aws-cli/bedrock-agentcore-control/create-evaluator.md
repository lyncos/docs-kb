---
title: aws bedrock-agentcore-control create-evaluator
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/create-evaluator.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# create-evaluator

## Description

Creates a custom evaluator for agent quality assessment. Custom evaluators can use either LLM-as-a-Judge configurations with user-defined prompts, rating scales, and model settings, or code-based configurations with customer-managed Lambda functions to evaluate agent performance at tool call, trace, or session levels.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/CreateEvaluator)

`create-evaluator` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

      create-evaluator
    [--client-token <value>]
    --evaluator-name <value>
    [--description <value>]
    --evaluator-config <value>
    --level <value>
    [--kms-key-arn <value>]
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

`--evaluator-name` (string) \[required\]

> The name of the evaluator. Must be unique within your account.
>
> Constraints:
>
> - pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`

`--description` (string)

> The description of the evaluator that explains its purpose and evaluation criteria.
>
> Constraints:
>
> - min: `1`
> - max: `200`

`--evaluator-config` (tagged union structure) \[required\]

> The configuration for the evaluator. Specify either LLM-as-a-Judge settings with instructions, rating scale, and model configuration, or code-based settings with a customer-managed Lambda function.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `llmAsAJudge`, `codeBased`, `derived`.
>
> llmAsAJudge -\> (structure)
>
> > The LLM-as-a-Judge configuration that uses a language model to evaluate agent performance based on custom instructions and rating scales.
> >
> > instructions -\> (string) \[required\]
> >
> > > The evaluation instructions that guide the language model in assessing agent performance, including criteria and evaluation guidelines.
> >
> > ratingScale -\> (tagged union structure) \[required\]
> >
> > > The rating scale that defines how the evaluator should score agent performance, either numerical or categorical.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `numerical`, `categorical`.
> > >
> > > numerical -\> (list)
> > >
> > > > The numerical rating scale with defined score values and descriptions for quantitative evaluation.
> > > >
> > > > (structure)
> > > >
> > > > > The definition of a numerical rating scale option that provides a numeric value with its description for evaluation scoring.
> > > > >
> > > > > definition -\> (string) \[required\]
> > > > >
> > > > > > The description that explains what this numerical rating represents and when it should be used.
> > > > >
> > > > > value -\> (double) \[required\]
> > > > >
> > > > > > The numerical value for this rating scale option.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `0`
> > > > >
> > > > > label -\> (string) \[required\]
> > > > >
> > > > > > The label or name that describes this numerical rating option.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `100`
> > >
> > > categorical -\> (list)
> > >
> > > > The categorical rating scale with named categories and definitions for qualitative evaluation.
> > > >
> > > > (structure)
> > > >
> > > > > The definition of a categorical rating scale option that provides a named category with its description for evaluation scoring.
> > > > >
> > > > > definition -\> (string) \[required\]
> > > > >
> > > > > > The description that explains what this categorical rating represents and when it should be used.
> > > > >
> > > > > label -\> (string) \[required\]
> > > > >
> > > > > > The label or name of this categorical rating option.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `100`
> >
> > modelConfig -\> (tagged union structure) \[required\]
> >
> > > The model configuration that specifies which foundation model to use and how to configure it for evaluation.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `bedrockEvaluatorModelConfig`, `responsesEvaluatorModelConfig`.
> > >
> > > bedrockEvaluatorModelConfig -\> (structure)
> > >
> > > > The Amazon Bedrock model configuration for evaluation.
> > > >
> > > > modelId -\> (string) \[required\]
> > > >
> > > > > The identifier of the Amazon Bedrock model to use for evaluation. Must be a supported foundation model available in your region.
> > > >
> > > > inferenceConfig -\> (structure)
> > > >
> > > > > The inference configuration parameters that control model behavior during evaluation, including temperature, token limits, and sampling settings.
> > > > >
> > > > > maxTokens -\> (integer)
> > > > >
> > > > > > The maximum number of tokens to generate in the model response during evaluation.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > >
> > > > > temperature -\> (float)
> > > > >
> > > > > > The temperature value that controls randomness in the model’s responses. Lower values produce more deterministic outputs.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `0`
> > > > > > - max: `1`
> > > > >
> > > > > topP -\> (float)
> > > > >
> > > > > > The top-p sampling parameter that controls the diversity of the model’s responses by limiting the cumulative probability of token choices.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `0`
> > > > > > - max: `1`
> > > > >
> > > > > stopSequences -\> (list)
> > > > >
> > > > > > The list of sequences that will cause the model to stop generating tokens when encountered.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `0`
> > > > > > - max: `2500`
> > > > > >
> > > > > > (string)
> > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > >
> > > > additionalModelRequestFields -\> (document)
> > > >
> > > > > Additional model-specific request fields to customize model behavior beyond the standard inference configuration.
> > >
> > > responsesEvaluatorModelConfig -\> (structure)
> > >
> > > > The OpenResponses model configuration for evaluation.
> > > >
> > > > modelId -\> (string) \[required\]
> > > >
> > > > > The identifier of the model to use for evaluation.
> > > >
> > > > maxOutputTokens -\> (integer)
> > > >
> > > > > The maximum number of tokens to generate in the model response, including visible output and reasoning tokens.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > >
> > > > temperature -\> (float)
> > > >
> > > > > The temperature value that controls randomness in the model’s responses. Lower values produce more deterministic outputs.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `0`
> > > > > - max: `2`
> > > >
> > > > topP -\> (float)
> > > >
> > > > > The top-p sampling parameter that controls the diversity of the model’s responses by limiting the cumulative probability of token choices.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `0`
> > > > > - max: `1`
> > > >
> > > > reasoning -\> (structure)
> > > >
> > > > > The reasoning configuration for reasoning models. Non-reasoning models ignore this configuration.
> > > > >
> > > > > effort -\> (string)
> > > > >
> > > > > > The level of reasoning effort the model applies when generating a response. For supported values, see the model provider’s documentation.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `64`
>
> codeBased -\> (tagged union structure)
>
> > Configuration for a code-based evaluator that uses a customer-managed Lambda function to programmatically assess agent performance.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `lambdaConfig`.
> >
> > lambdaConfig -\> (structure)
> >
> > > The Lambda function configuration for code-based evaluation.
> > >
> > > lambdaArn -\> (string) \[required\]
> > >
> > > > The Amazon Resource Name (ARN) of the Lambda function that implements the evaluation logic.
> > > >
> > > > Constraints:
> > > >
> > > > - pattern: `arn:(aws[a-zA-Z-]*)?:lambda:([a-z]{2}(-gov)?-[a-z]+-\d{1}):(\d{12}):function:([a-zA-Z0-9-_.]+)(:(\$LATEST|[a-zA-Z0-9-_]+))?`
> > >
> > > lambdaTimeoutInSeconds -\> (integer)
> > >
> > > > The timeout in seconds for the Lambda function invocation. Defaults to 60. Must be between 1 and 300.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `300`
>
> derived -\> (structure)
>
> > The configuration for an evaluator derived from an existing base evaluator (a built-in or third-party evaluator), run on your own model. The base evaluator supplies the prompt and scoring.
> >
> > baseEvaluatorId -\> (string) \[required\]
> >
> > > The identifier of the base evaluator whose logic to run (a `Builtin.*` or `ThirdParty.*` evaluator).
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `111`
> > > - pattern: `(Builtin\.[a-zA-Z0-9._-]+|ThirdParty\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})`
> >
> > modelConfig -\> (tagged union structure) \[required\]
> >
> > > The configuration of the evaluator model that you supply.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `bedrockEvaluatorModelConfig`, `responsesEvaluatorModelConfig`.
> > >
> > > bedrockEvaluatorModelConfig -\> (structure)
> > >
> > > > The Amazon Bedrock model configuration for evaluation.
> > > >
> > > > modelId -\> (string) \[required\]
> > > >
> > > > > The identifier of the Amazon Bedrock model to use for evaluation. Must be a supported foundation model available in your region.
> > > >
> > > > inferenceConfig -\> (structure)
> > > >
> > > > > The inference configuration parameters that control model behavior during evaluation, including temperature, token limits, and sampling settings.
> > > > >
> > > > > maxTokens -\> (integer)
> > > > >
> > > > > > The maximum number of tokens to generate in the model response during evaluation.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > >
> > > > > temperature -\> (float)
> > > > >
> > > > > > The temperature value that controls randomness in the model’s responses. Lower values produce more deterministic outputs.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `0`
> > > > > > - max: `1`
> > > > >
> > > > > topP -\> (float)
> > > > >
> > > > > > The top-p sampling parameter that controls the diversity of the model’s responses by limiting the cumulative probability of token choices.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `0`
> > > > > > - max: `1`
> > > > >
> > > > > stopSequences -\> (list)
> > > > >
> > > > > > The list of sequences that will cause the model to stop generating tokens when encountered.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `0`
> > > > > > - max: `2500`
> > > > > >
> > > > > > (string)
> > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > >
> > > > additionalModelRequestFields -\> (document)
> > > >
> > > > > Additional model-specific request fields to customize model behavior beyond the standard inference configuration.
> > >
> > > responsesEvaluatorModelConfig -\> (structure)
> > >
> > > > The OpenResponses model configuration for evaluation.
> > > >
> > > > modelId -\> (string) \[required\]
> > > >
> > > > > The identifier of the model to use for evaluation.
> > > >
> > > > maxOutputTokens -\> (integer)
> > > >
> > > > > The maximum number of tokens to generate in the model response, including visible output and reasoning tokens.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > >
> > > > temperature -\> (float)
> > > >
> > > > > The temperature value that controls randomness in the model’s responses. Lower values produce more deterministic outputs.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `0`
> > > > > - max: `2`
> > > >
> > > > topP -\> (float)
> > > >
> > > > > The top-p sampling parameter that controls the diversity of the model’s responses by limiting the cumulative probability of token choices.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `0`
> > > > > - max: `1`
> > > >
> > > > reasoning -\> (structure)
> > > >
> > > > > The reasoning configuration for reasoning models. Non-reasoning models ignore this configuration.
> > > > >
> > > > > effort -\> (string)
> > > > >
> > > > > > The level of reasoning effort the model applies when generating a response. For supported values, see the model provider’s documentation.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `64`

JSON Syntax:

    {
      "llmAsAJudge": {
        "instructions": "string",
        "ratingScale": {
          "numerical": [
            {
              "definition": "string",
              "value": double,
              "label": "string"
            }
            ...
          ],
          "categorical": [
            {
              "definition": "string",
              "label": "string"
            }
            ...
          ]
        },
        "modelConfig": {
          "bedrockEvaluatorModelConfig": {
            "modelId": "string",
            "inferenceConfig": {
              "maxTokens": integer,
              "temperature": float,
              "topP": float,
              "stopSequences": ["string", ...]
            },
            "additionalModelRequestFields": {...}
          },
          "responsesEvaluatorModelConfig": {
            "modelId": "string",
            "maxOutputTokens": integer,
            "temperature": float,
            "topP": float,
            "reasoning": {
              "effort": "string"
            }
          }
        }
      },
      "codeBased": {
        "lambdaConfig": {
          "lambdaArn": "string",
          "lambdaTimeoutInSeconds": integer
        }
      },
      "derived": {
        "baseEvaluatorId": "string",
        "modelConfig": {
          "bedrockEvaluatorModelConfig": {
            "modelId": "string",
            "inferenceConfig": {
              "maxTokens": integer,
              "temperature": float,
              "topP": float,
              "stopSequences": ["string", ...]
            },
            "additionalModelRequestFields": {...}
          },
          "responsesEvaluatorModelConfig": {
            "modelId": "string",
            "maxOutputTokens": integer,
            "temperature": float,
            "topP": float,
            "reasoning": {
              "effort": "string"
            }
          }
        }
      }
    }

`--level` (string) \[required\]

> The evaluation level that determines the scope of evaluation. Valid values are `TOOL_CALL` for individual tool invocations, `TRACE` for single request-response interactions, or `SESSION` for entire conversation sessions.
>
> Possible values:
>
> - `TOOL_CALL`
> - `TRACE`
> - `SESSION`

`--kms-key-arn` (string)

> The Amazon Resource Name (ARN) of a customer managed KMS key to use for encrypting sensitive evaluator data, including instructions and rating scale. If you don’t specify a KMS key, the evaluator data is encrypted with an Amazon Web Services owned key. Only symmetric encryption KMS keys are supported. For more information, see [Encryption at rest for AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-encryption.html) .
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`

`--tags` (map)

> A map of tag keys and values to assign to an AgentCore Evaluator. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.
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

evaluatorArn -\> (string)

> The Amazon Resource Name (ARN) of the created evaluator.
>
> Constraints:
>
> - pattern: `arn:aws[a-zA-Z-]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:evaluator\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`

evaluatorId -\> (string)

> The unique identifier of the created evaluator.
>
> Constraints:
>
> - min: `1`
> - max: `111`
> - pattern: `(Builtin\.[a-zA-Z0-9._-]+|ThirdParty\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+|[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10})`

createdAt -\> (timestamp)

> The timestamp when the evaluator was created.

status -\> (string)

> The status of the evaluator creation operation.
>
> Possible values:
>
> - `ACTIVE`
> - `CREATING`
> - `CREATE_FAILED`
> - `UPDATING`
> - `UPDATE_FAILED`
> - `DELETING`

- [← create-dataset-version](create-dataset-version.html "previous chapter (use the left arrow)") /
- [create-gateway →](create-gateway.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](create-gateway.html "create-gateway") \|
- [previous](create-dataset-version.html "create-dataset-version") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [create-evaluator]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

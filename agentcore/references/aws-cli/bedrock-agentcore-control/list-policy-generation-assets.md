---
title: aws bedrock-agentcore-control list-policy-generation-assets
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/list-policy-generation-assets.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# list-policy-generation-assets

## Description

Retrieves a list of generated policy assets from a policy generation request within the AgentCore Policy system. This operation returns the actual Dogwood policies and related artifacts produced by the AI-powered policy generation process, allowing users to review and select from multiple generated policy options.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/ListPolicyGenerationAssets)

`list-policy-generation-assets` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument. When using `--output`` ``text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `policyGenerationAssets`

## Synopsis

      list-policy-generation-assets
    --policy-generation-id <value>
    --policy-engine-id <value>
    [--starting-token <value>]
    [--page-size <value>]
    [--max-items <value>]
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

`--policy-generation-id` (string) \[required\]

> The unique identifier of the policy generation request whose assets are to be retrieved. This must be a valid generation ID from a previous [StartPolicyGeneration](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_StartPolicyGeneration.html) call that has completed processing.
>
> Constraints:
>
> - min: `12`
> - max: `59`
> - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`

`--policy-engine-id` (string) \[required\]

> The unique identifier of the policy engine associated with the policy generation request. This provides the context for the generation operation and ensures assets are retrieved from the correct policy engine.
>
> Constraints:
>
> - min: `12`
> - max: `59`
> - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`

`--starting-token` (string)

> A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.
>
> For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

> The size of each page to get in the AWS service call. This does not affect the number of items returned in the command’s output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.
>
> For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .
>
> Constraints:
>
> - min: `1`
> - max: `100`

`--max-items` (integer)

> The total number of items to return in the command’s output. If the total number of items available is more than the value specified, a `NextToken` is provided in the command’s output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.
>
> For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

policyGenerationAssets -\> (list)

> An array of generated policy assets including Dogwood policies and related artifacts from the AI-powered policy generation process. Each asset represents a different policy option or variation generated from the original natural language input.
>
> (structure)
>
> > Represents a generated policy asset from the AI-powered policy generation process within the AgentCore Policy system. Each asset contains a Dogwood policy statement generated from natural language input, along with associated metadata and analysis findings to help users evaluate and select the most appropriate policy option.
> >
> > policyGenerationAssetId -\> (string) \[required\]
> >
> > > The unique identifier for this generated policy asset within the policy generation request. This ID can be used to reference specific generated policy options when creating actual policies from the generation results.
> > >
> > > Constraints:
> > >
> > > - min: `12`
> > > - max: `59`
> > > - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`
> >
> > definition -\> (tagged union structure)
> >
> > > Represents the definition structure for policies within the AgentCore Policy system. This structure encapsulates different policy formats and languages that can be used to define access control rules.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `cedar`, `policyGeneration`, `policy`.
> > >
> > > cedar -\> (structure)
> > >
> > > > The Cedar policy definition within the policy definition structure. This contains the Cedar policy statement that defines the authorization logic using Cedar’s human-readable, analyzable policy language. Cedar policies specify principals (who can access), actions (what operations are allowed), resources (what can be accessed), and optional conditions for fine-grained control. Cedar provides a formal policy language designed for authorization with deterministic evaluation, making policies testable, reviewable, and auditable. All Cedar policies follow a default-deny model where actions are denied unless explicitly permitted, and forbid policies always override permit policies.
> > > >
> > > > statement -\> (string) \[required\]
> > > >
> > > > > The Cedar policy statement that defines the authorization logic. This statement follows Cedar syntax and specifies principals, actions, resources, and conditions that determine when access should be allowed or denied.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `35`
> > > > > - max: `10000`
> > >
> > > policyGeneration -\> (structure)
> > >
> > > > The generated policy asset information within the policy definition structure. This contains information identifying a generated policy asset from the AI-powered policy generation process within the AgentCore Policy system. Each asset contains a Dogwood policy statement generated from natural language input, along with associated metadata and analysis findings to help users evaluate and select the most appropriate policy option.
> > > >
> > > > policyGenerationId -\> (string) \[required\]
> > > >
> > > > > The unique identifier for this policy generation request.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `12`
> > > > > - max: `59`
> > > > > - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`
> > > >
> > > > policyGenerationAssetId -\> (string) \[required\]
> > > >
> > > > > The unique identifier for this generated policy asset within the policy generation request.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `12`
> > > > > - max: `59`
> > > > > - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`
> > >
> > > policy -\> (structure)
> > >
> > > > The Dogwood policy statement that defines the access control rules. This policy definition can include Dogwood policies and supports temporal conditions and information providers such as guardrails.
> > > >
> > > > statement -\> (string) \[required\]
> > > >
> > > > > The body of the AgentCore Cedar or Dogwood policy statement. Contains the policy logic, which can be a Cedar policy, a temporal policy, or a guardrails definition.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `35`
> > > > > - max: `10000`
> >
> > rawTextFragment -\> (string) \[required\]
> >
> > > The portion of the original natural language input that this generated policy asset addresses. This helps users understand which part of their policy description was translated into this specific Dogwood policy statement, enabling better policy selection and refinement. When a single natural language input describes multiple authorization requirements, the generation process creates separate policy assets for each requirement, with each asset’s rawTextFragment showing which requirement it addresses. Use this mapping to verify that all parts of your natural language input were correctly translated into Dogwood policies.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `2000`
> >
> > findings -\> (list) \[required\]
> >
> > > Analysis findings and insights related to this specific generated policy asset. These findings may include validation results, potential issues, or recommendations for improvement to help users evaluate the quality and appropriateness of the generated policy.
> > >
> > > (structure)
> > >
> > > > Represents a finding or issue discovered during policy generation or validation. Findings provide insights about potential problems, recommendations, or validation results from policy analysis operations. Finding types include: VALID (policy is ready to use), INVALID (policy has validation errors that must be fixed), NOT_TRANSLATABLE (input couldn’t be converted to policy), ALLOW_ALL (policy would allow all actions, potential security risk), ALLOW_NONE (policy would allow no actions, unusable), DENY_ALL (policy would deny all actions, may be too restrictive), and DENY_NONE (policy would deny no actions, ineffective). Review all findings before creating policies from generated assets to ensure they match your security requirements.
> > > >
> > > > type -\> (string)
> > > >
> > > > > The type or category of the finding. This classifies the finding as an error, warning, recommendation, or informational message to help users understand the severity and nature of the issue.
> > > > >
> > > > > Possible values:
> > > > >
> > > > > - `VALID`
> > > > > - `INVALID`
> > > > > - `NOT_TRANSLATABLE`
> > > > > - `ALLOW_ALL`
> > > > > - `ALLOW_NONE`
> > > > > - `DENY_ALL`
> > > > > - `DENY_NONE`
> > > >
> > > > description -\> (string)
> > > >
> > > > > A human-readable description of the finding. This provides detailed information about the issue, recommendation, or validation result to help users understand and address the finding.

nextToken -\> (string)

> A pagination token that can be used in subsequent [ListPolicyGenerationAssets](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyGenerationAssets.html) calls to retrieve additional assets. This token is only present when there are more generated policy assets available beyond the current response.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `\S*`

- [← list-policy-engines](list-policy-engines.html "previous chapter (use the left arrow)") /
- [list-policy-generation-summaries →](list-policy-generation-summaries.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](list-policy-generation-summaries.html "list-policy-generation-summaries") \|
- [previous](list-policy-engines.html "list-policy-engines") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [list-policy-generation-assets]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

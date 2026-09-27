---
title: aws bedrock-agentcore-control list-policies
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/list-policies.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# list-policies

## Description

Retrieves a list of policies within the AgentCore Policy engine. This operation supports pagination and filtering to help administrators manage and discover policies across policy engines. Results can be filtered by policy engine or resource associations.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/ListPolicies)

`list-policies` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument. When using `--output`` ``text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `policies`

## Synopsis

      list-policies
    --policy-engine-id <value>
    [--target-resource-scope <value>]
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

`--policy-engine-id` (string) \[required\]

> The identifier of the policy engine whose policies to retrieve.
>
> Constraints:
>
> - min: `12`
> - max: `59`
> - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`

`--target-resource-scope` (string)

> Optional filter to list policies that apply to a specific resource scope or resource type. This helps narrow down policy results to those relevant for particular Amazon Web Services resources, agent tools, or operational contexts within the policy engine ecosystem.
>
> Constraints:
>
> - min: `20`
> - max: `1011`

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

policies -\> (list)

> An array of policy objects that match the specified criteria. Each policy object contains the policy metadata, status, and key identifiers for further operations.
>
> Constraints:
>
> - min: `0`
> - max: `100`
>
> (structure)
>
> > Represents a complete policy resource within the AgentCore Policy system. Policies are ARN-able resources that contain Cedar or Dogwood policy statements and associated metadata for controlling agent behavior and access decisions. Each policy belongs to a policy engine and defines fine-grained authorization rules that are evaluated in real-time as agents interact with tools through Gateway. Policies use Cedar or Dogwood to specify who (principals based on OAuth claims like username, role, or scope) can perform what actions (tool calls) on which resources (Gateways), with optional conditions for attribute-based access control. Multiple policies can apply to a single request, with forbid-wins semantics ensuring that security restrictions are never accidentally overridden.
> >
> > policyId -\> (string) \[required\]
> >
> > > The unique identifier for the policy. This system-generated identifier consists of the user name plus a 10-character generated suffix and serves as the primary key for policy operations.
> > >
> > > Constraints:
> > >
> > > - min: `12`
> > > - max: `59`
> > > - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`
> >
> > name -\> (string) \[required\]
> >
> > > The customer-assigned immutable name for the policy. This human-readable identifier must be unique within the account and cannot exceed 48 characters.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `48`
> > > - pattern: `[A-Za-z][A-Za-z0-9_]*`
> >
> > policyEngineId -\> (string) \[required\]
> >
> > > The identifier of the policy engine that manages this policy. This establishes the policy engine context for policy evaluation and management.
> > >
> > > Constraints:
> > >
> > > - min: `12`
> > > - max: `59`
> > > - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`
> >
> > createdAt -\> (timestamp) \[required\]
> >
> > > The timestamp when the policy was originally created. This is automatically set by the service and used for auditing and lifecycle management.
> >
> > updatedAt -\> (timestamp) \[required\]
> >
> > > The timestamp when the policy was last modified. This tracks the most recent changes to the policy configuration or metadata.
> >
> > policyArn -\> (string) \[required\]
> >
> > > The Amazon Resource Name (ARN) of the policy. This globally unique identifier can be used for cross-service references and IAM policy statements.
> > >
> > > Constraints:
> > >
> > > - min: `96`
> > > - max: `203`
> > > - pattern: `arn:aws[-a-z]{0,7}:bedrock-agentcore:[a-z0-9-]{9,15}:[0-9]{12}:policy-engine/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}/policy/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}`
> >
> > status -\> (string) \[required\]
> >
> > > The current status of the policy.
> > >
> > > Possible values:
> > >
> > > - `CREATING`
> > > - `ACTIVE`
> > > - `UPDATING`
> > > - `DELETING`
> > > - `CREATE_FAILED`
> > > - `UPDATE_FAILED`
> > > - `DELETE_FAILED`
> >
> > enforcementMode -\> (string)
> >
> > > The current enforcement mode of the policy.
> > >
> > > Possible values:
> > >
> > > - `ACTIVE`
> > > - `LOG_ONLY`
> >
> > definition -\> (tagged union structure) \[required\]
> >
> > > The Cedar or Dogwood policy statement that defines the access control rules. This contains the actual policy logic used for agent behavior control and access decisions.
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
> > description -\> (string)
> >
> > > A human-readable description of the policy’s purpose and functionality. Limited to 4,096 characters, this helps administrators understand and manage the policy.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `4096`
> >
> > statusReasons -\> (list) \[required\]
> >
> > > Additional information about the policy status. This provides details about any failures or the current state of the policy lifecycle.
> > >
> > > (string)

nextToken -\> (string)

> A pagination token that can be used in subsequent ListPolicies calls to retrieve additional results. This token is only present when there are more results available.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `\S*`

- [← list-payment-managers](list-payment-managers.html "previous chapter (use the left arrow)") /
- [list-policy-engine-summaries →](list-policy-engine-summaries.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](list-policy-engine-summaries.html "list-policy-engine-summaries") \|
- [previous](list-payment-managers.html "list-payment-managers") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [list-policies]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

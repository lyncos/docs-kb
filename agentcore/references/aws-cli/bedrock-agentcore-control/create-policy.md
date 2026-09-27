---
title: aws bedrock-agentcore-control create-policy
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/create-policy.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# create-policy

## Description

Creates a policy within the AgentCore Policy system. Policies provide real-time, deterministic control over agentic interactions with AgentCore Gateway. Using Cedar or Dogwood, you can define fine-grained policies that specify which interactions with Gateway tools are permitted based on input parameters and OAuth claims, ensuring agents operate within defined boundaries and business rules. The policy is validated during creation against the Cedar schema generated from the Gateway’s tools’ input schemas, which defines the available tools, their parameters, and expected data types. This is an asynchronous operation. Use the [GetPolicy](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetPolicy.html) operation to poll the `status` field to track completion.

If the new policy is a temporal policy, creating it invalidates the policy engine’s active temporal sessions. For more information about temporal policy sessions, see [session-based temporal policies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-session-based-temporal.html) . The policy engine returns an HTTP 409 `ConflictException` to in-flight sessions. To resume, you must start a new session with a new session ID.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/CreatePolicy)

## Synopsis

      create-policy
    --name <value>
    --definition <value>
    [--description <value>]
    [--validation-mode <value>]
    [--enforcement-mode <value>]
    --policy-engine-id <value>
    [--client-token <value>]
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

> The customer-assigned immutable name for the policy. Must be unique within the account. This name is used for policy identification and cannot be changed after creation.
>
> Constraints:
>
> - min: `1`
> - max: `48`
> - pattern: `[A-Za-z][A-Za-z0-9_]*`

`--definition` (tagged union structure) \[required\]

> The Cedar or Dogwood policy statement that defines the access control rules. This contains the actual policy logic written in Cedar or Dogwood, specifying effect (permit or forbid), principals, actions, resources, and conditions for agent behavior control.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `cedar`, `policyGeneration`, `policy`.
>
> cedar -\> (structure)
>
> > The Cedar policy definition within the policy definition structure. This contains the Cedar policy statement that defines the authorization logic using Cedar’s human-readable, analyzable policy language. Cedar policies specify principals (who can access), actions (what operations are allowed), resources (what can be accessed), and optional conditions for fine-grained control. Cedar provides a formal policy language designed for authorization with deterministic evaluation, making policies testable, reviewable, and auditable. All Cedar policies follow a default-deny model where actions are denied unless explicitly permitted, and forbid policies always override permit policies.
> >
> > statement -\> (string) \[required\]
> >
> > > The Cedar policy statement that defines the authorization logic. This statement follows Cedar syntax and specifies principals, actions, resources, and conditions that determine when access should be allowed or denied.
> > >
> > > Constraints:
> > >
> > > - min: `35`
> > > - max: `10000`
>
> policyGeneration -\> (structure)
>
> > The generated policy asset information within the policy definition structure. This contains information identifying a generated policy asset from the AI-powered policy generation process within the AgentCore Policy system. Each asset contains a Dogwood policy statement generated from natural language input, along with associated metadata and analysis findings to help users evaluate and select the most appropriate policy option.
> >
> > policyGenerationId -\> (string) \[required\]
> >
> > > The unique identifier for this policy generation request.
> > >
> > > Constraints:
> > >
> > > - min: `12`
> > > - max: `59`
> > > - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`
> >
> > policyGenerationAssetId -\> (string) \[required\]
> >
> > > The unique identifier for this generated policy asset within the policy generation request.
> > >
> > > Constraints:
> > >
> > > - min: `12`
> > > - max: `59`
> > > - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`
>
> policy -\> (structure)
>
> > The Dogwood policy statement that defines the access control rules. This policy definition can include Dogwood policies and supports temporal conditions and information providers such as guardrails.
> >
> > statement -\> (string) \[required\]
> >
> > > The body of the AgentCore Cedar or Dogwood policy statement. Contains the policy logic, which can be a Cedar policy, a temporal policy, or a guardrails definition.
> > >
> > > Constraints:
> > >
> > > - min: `35`
> > > - max: `10000`

Shorthand Syntax:

    cedar={statement=string},policyGeneration={policyGenerationId=string,policyGenerationAssetId=string},policy={statement=string}

JSON Syntax:

    {
      "cedar": {
        "statement": "string"
      },
      "policyGeneration": {
        "policyGenerationId": "string",
        "policyGenerationAssetId": "string"
      },
      "policy": {
        "statement": "string"
      }
    }

`--description` (string)

> A human-readable description of the policy’s purpose and functionality (1-4,096 characters). This helps policy administrators understand the policy’s intent, business rules, and operational scope. Use this field to document why the policy exists, what business requirement it addresses, and any special considerations for maintenance. Clear descriptions are essential for policy governance, auditing, and troubleshooting.
>
> Constraints:
>
> - min: `1`
> - max: `4096`

`--validation-mode` (string)

> The validation mode for the policy creation. Determines how Cedar analyzer validation results are handled during policy creation. FAIL_ON_ANY_FINDINGS (default) runs the Cedar analyzer to validate the policy against the Cedar schema and tool context, failing creation if the analyzer detects any validation issues to ensure strict conformance. IGNORE_ALL_FINDINGS runs the Cedar analyzer but allows policy creation even if validation issues are detected, useful for testing or when the policy schema is evolving. Use FAIL_ON_ANY_FINDINGS for production policies to ensure correctness, and IGNORE_ALL_FINDINGS only when you understand and accept the analyzer findings.
>
> Possible values:
>
> - `FAIL_ON_ANY_FINDINGS`
> - `IGNORE_ALL_FINDINGS`

`--enforcement-mode` (string)

> The enforcement mode for the policy. Run this policy in `LOG_ONLY` mode to collect data on how it affects your application. Once you are satisfied with the data gathered, switch the policy to `ACTIVE` . Defaults to `ACTIVE` .
>
> Possible values:
>
> - `ACTIVE`
> - `LOG_ONLY`

`--policy-engine-id` (string) \[required\]

> The identifier of the policy engine which contains this policy. Policy engines group related policies and provide the execution context for policy evaluation.
>
> Constraints:
>
> - min: `12`
> - max: `59`
> - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`

`--client-token` (string)

> A unique, case-sensitive identifier to ensure the idempotency of the request. The AWS SDK automatically generates this token, so you don’t need to provide it in most cases. If you retry a request with the same client token, the service returns the same response without creating a duplicate policy.
>
> Constraints:
>
> - min: `33`
> - max: `256`
> - pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`

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

policyId -\> (string)

> The unique identifier for the created policy. This is a system-generated identifier consisting of the user name plus a 10-character generated suffix, used for all subsequent policy operations.
>
> Constraints:
>
> - min: `12`
> - max: `59`
> - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`

name -\> (string)

> The customer-assigned name of the created policy. This matches the name provided in the request and serves as the human-readable identifier for the policy.
>
> Constraints:
>
> - min: `1`
> - max: `48`
> - pattern: `[A-Za-z][A-Za-z0-9_]*`

policyEngineId -\> (string)

> The identifier of the policy engine that manages this policy. This confirms the policy engine assignment and is used for policy evaluation routing.
>
> Constraints:
>
> - min: `12`
> - max: `59`
> - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`

createdAt -\> (timestamp)

> The timestamp when the policy was created. This is automatically set by the service and used for auditing and lifecycle management.

updatedAt -\> (timestamp)

> The timestamp when the policy was last updated. For newly created policies, this matches the createdAt timestamp.

policyArn -\> (string)

> The Amazon Resource Name (ARN) of the created policy. This globally unique identifier can be used for cross-service references and IAM policy statements.
>
> Constraints:
>
> - min: `96`
> - max: `203`
> - pattern: `arn:aws[-a-z]{0,7}:bedrock-agentcore:[a-z0-9-]{9,15}:[0-9]{12}:policy-engine/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}/policy/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}`

status -\> (string)

> The current status of the policy. A status of `ACTIVE` indicates the policy is ready for use.
>
> Possible values:
>
> - `CREATING`
> - `ACTIVE`
> - `UPDATING`
> - `DELETING`
> - `CREATE_FAILED`
> - `UPDATE_FAILED`
> - `DELETE_FAILED`

enforcementMode -\> (string)

> The enforcement mode of the created policy.
>
> Possible values:
>
> - `ACTIVE`
> - `LOG_ONLY`

definition -\> (tagged union structure)

> The Cedar or Dogwood policy statement that was created. This is the validated policy definition that will be used for agent behavior control and access decisions.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `cedar`, `policyGeneration`, `policy`.
>
> cedar -\> (structure)
>
> > The Cedar policy definition within the policy definition structure. This contains the Cedar policy statement that defines the authorization logic using Cedar’s human-readable, analyzable policy language. Cedar policies specify principals (who can access), actions (what operations are allowed), resources (what can be accessed), and optional conditions for fine-grained control. Cedar provides a formal policy language designed for authorization with deterministic evaluation, making policies testable, reviewable, and auditable. All Cedar policies follow a default-deny model where actions are denied unless explicitly permitted, and forbid policies always override permit policies.
> >
> > statement -\> (string) \[required\]
> >
> > > The Cedar policy statement that defines the authorization logic. This statement follows Cedar syntax and specifies principals, actions, resources, and conditions that determine when access should be allowed or denied.
> > >
> > > Constraints:
> > >
> > > - min: `35`
> > > - max: `10000`
>
> policyGeneration -\> (structure)
>
> > The generated policy asset information within the policy definition structure. This contains information identifying a generated policy asset from the AI-powered policy generation process within the AgentCore Policy system. Each asset contains a Dogwood policy statement generated from natural language input, along with associated metadata and analysis findings to help users evaluate and select the most appropriate policy option.
> >
> > policyGenerationId -\> (string) \[required\]
> >
> > > The unique identifier for this policy generation request.
> > >
> > > Constraints:
> > >
> > > - min: `12`
> > > - max: `59`
> > > - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`
> >
> > policyGenerationAssetId -\> (string) \[required\]
> >
> > > The unique identifier for this generated policy asset within the policy generation request.
> > >
> > > Constraints:
> > >
> > > - min: `12`
> > > - max: `59`
> > > - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`
>
> policy -\> (structure)
>
> > The Dogwood policy statement that defines the access control rules. This policy definition can include Dogwood policies and supports temporal conditions and information providers such as guardrails.
> >
> > statement -\> (string) \[required\]
> >
> > > The body of the AgentCore Cedar or Dogwood policy statement. Contains the policy logic, which can be a Cedar policy, a temporal policy, or a guardrails definition.
> > >
> > > Constraints:
> > >
> > > - min: `35`
> > > - max: `10000`

description -\> (string)

> The human-readable description of the policy’s purpose and functionality. This helps administrators understand and manage the policy.
>
> Constraints:
>
> - min: `1`
> - max: `4096`

statusReasons -\> (list)

> Additional information about the policy status. This provides details about any failures or the current state of the policy creation process.
>
> (string)

- [← create-payment-manager](create-payment-manager.html "previous chapter (use the left arrow)") /
- [create-policy-engine →](create-policy-engine.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](create-policy-engine.html "create-policy-engine") \|
- [previous](create-payment-manager.html "create-payment-manager") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [create-policy]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

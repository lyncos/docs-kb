---
title: aws bedrock-agentcore-control update-policy
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/update-policy.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# update-policy

## Description

Updates an existing policy within the AgentCore Policy system. This operation allows modification of the policy description and definition while maintaining the policy’s identity. The updated policy is validated against the Cedar schema before being applied. This is an asynchronous operation. Use the `GetPolicy` operation to poll the `status` field to track completion.

If the updated policy is a temporal policy, the policy engine invalidates all active temporal sessions. If the update adds or removes temporal operators, the policy engine also invalidates active temporal sessions. For more information about temporal policy sessions, see [session-based temporal policies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-session-based-temporal.html) . The policy engine returns an HTTP 409 `ConflictException` to in-flight sessions. To resume, you must start a new session with a new session ID.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/UpdatePolicy)

## Synopsis

      update-policy
    --policy-engine-id <value>
    --policy-id <value>
    [--description <value>]
    [--definition <value>]
    [--validation-mode <value>]
    [--enforcement-mode <value>]
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

> The identifier of the policy engine that manages the policy to be updated. This ensures the policy is updated within the correct policy engine context.
>
> Constraints:
>
> - min: `12`
> - max: `59`
> - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`

`--policy-id` (string) \[required\]

> The unique identifier of the policy to be updated. This must be a valid policy ID that exists within the specified policy engine.
>
> Constraints:
>
> - min: `12`
> - max: `59`
> - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`

`--description` (structure)

> The new human-readable description for the policy. This optional field allows updating the policy’s documentation while keeping the same policy logic.
>
> optionalValue -\> (string)
>
> > Represents an optional value that is used to update the human-readable description of the resource. If not specified, it will clear the current description of the resource.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `4096`

Shorthand Syntax:

    optionalValue=string

JSON Syntax:

    {
      "optionalValue": "string"
    }

`--definition` (tagged union structure)

> The new Cedar or Dogwood policy statement that defines the access control rules. This replaces the existing policy definition with new logic while maintaining the policy’s identity.
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

`--validation-mode` (string)

> The validation mode for the policy update. Determines how Cedar analyzer validation results are handled during policy updates. FAIL_ON_ANY_FINDINGS runs the Cedar analyzer and fails the update if validation issues are detected, ensuring the policy conforms to the Cedar schema and tool context. IGNORE_ALL_FINDINGS runs the Cedar analyzer but allows updates despite validation warnings. Use FAIL_ON_ANY_FINDINGS to ensure policy correctness during updates, especially when modifying policy logic or conditions.
>
> Possible values:
>
> - `FAIL_ON_ANY_FINDINGS`
> - `IGNORE_ALL_FINDINGS`

`--enforcement-mode` (string)

> The enforcement mode for the policy. Run this policy in `LOG_ONLY` mode to collect data on how it affects your application. Once you are satisfied with the data gathered, switch the policy to `ACTIVE` . If you omit this field, the policy’s existing enforcement mode is unchanged.
>
> Possible values:
>
> - `ACTIVE`
> - `LOG_ONLY`

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

> The unique identifier of the updated policy.
>
> Constraints:
>
> - min: `12`
> - max: `59`
> - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`

name -\> (string)

> The name of the updated policy.
>
> Constraints:
>
> - min: `1`
> - max: `48`
> - pattern: `[A-Za-z][A-Za-z0-9_]*`

policyEngineId -\> (string)

> The identifier of the policy engine managing the updated policy.
>
> Constraints:
>
> - min: `12`
> - max: `59`
> - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`

createdAt -\> (timestamp)

> The original creation timestamp of the policy.

updatedAt -\> (timestamp)

> The timestamp when the policy was last updated.

policyArn -\> (string)

> The ARN of the updated policy.
>
> Constraints:
>
> - min: `96`
> - max: `203`
> - pattern: `arn:aws[-a-z]{0,7}:bedrock-agentcore:[a-z0-9-]{9,15}:[0-9]{12}:policy-engine/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}/policy/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}`

status -\> (string)

> The current status of the updated policy.
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

> The current enforcement mode of the updated policy.
>
> Possible values:
>
> - `ACTIVE`
> - `LOG_ONLY`

definition -\> (tagged union structure)

> The updated Cedar or Dogwood policy statement.
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

> The updated description of the policy.
>
> Constraints:
>
> - min: `1`
> - max: `4096`

statusReasons -\> (list)

> Additional information about the update status.
>
> (string)

- [← update-payment-manager](update-payment-manager.html "previous chapter (use the left arrow)") /
- [update-policy-engine →](update-policy-engine.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](update-policy-engine.html "update-policy-engine") \|
- [previous](update-payment-manager.html "update-payment-manager") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [update-policy]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

---
title: aws bedrock-agentcore-control delete-policy
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/delete-policy.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# delete-policy

## Description

Deletes an existing policy from the AgentCore Policy system. Once deleted, the policy can no longer be used for agent behavior control and all references to it become invalid. This is an asynchronous operation. Use the `GetPolicy` operation to poll the `status` field to track completion.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/DeletePolicy)

## Synopsis

      delete-policy
    --policy-engine-id <value>
    --policy-id <value>
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

> The identifier of the policy engine that manages the policy to be deleted. This ensures the policy is deleted from the correct policy engine context.
>
> Constraints:
>
> - min: `12`
> - max: `59`
> - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`

`--policy-id` (string) \[required\]

> The unique identifier of the policy to be deleted. This must be a valid policy ID that exists within the specified policy engine.
>
> Constraints:
>
> - min: `12`
> - max: `59`
> - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`

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

> The unique identifier of the policy being deleted. This confirms which policy the deletion operation targets.
>
> Constraints:
>
> - min: `12`
> - max: `59`
> - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`

name -\> (string)

> The customer-assigned name of the deleted policy. This confirms which policy was successfully removed from the system and matches the name that was originally assigned during policy creation.
>
> Constraints:
>
> - min: `1`
> - max: `48`
> - pattern: `[A-Za-z][A-Za-z0-9_]*`

policyEngineId -\> (string)

> The identifier of the policy engine from which the policy was deleted. This confirms the policy engine context for the deletion operation.
>
> Constraints:
>
> - min: `12`
> - max: `59`
> - pattern: `[A-Za-z][A-Za-z0-9_]*-[a-z0-9_]{10}`

createdAt -\> (timestamp)

> The timestamp when the deleted policy was originally created.

updatedAt -\> (timestamp)

> The timestamp when the deleted policy was last modified before deletion. This tracks the final state of the policy before it was removed from the system.

policyArn -\> (string)

> The Amazon Resource Name (ARN) of the deleted policy. This globally unique identifier confirms which policy resource was successfully removed.
>
> Constraints:
>
> - min: `96`
> - max: `203`
> - pattern: `arn:aws[-a-z]{0,7}:bedrock-agentcore:[a-z0-9-]{9,15}:[0-9]{12}:policy-engine/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}/policy/[a-zA-Z][a-zA-Z0-9-_]{0,47}-[a-zA-Z0-9_]{10}`

status -\> (string)

> The status of the policy deletion operation. This provides information about any issues that occurred during the deletion process.
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

> The enforcement mode of the deleted policy.
>
> Possible values:
>
> - `ACTIVE`
> - `LOG_ONLY`

definition -\> (tagged union structure)

> Represents the definition structure for policies within the AgentCore Policy system. This structure encapsulates different policy formats and languages that can be used to define access control rules.
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

> The human-readable description of the deleted policy.
>
> Constraints:
>
> - min: `1`
> - max: `4096`

statusReasons -\> (list)

> Additional information about the deletion status. This provides details about the deletion process or any issues that may have occurred.
>
> (string)

- [← delete-payment-manager](delete-payment-manager.html "previous chapter (use the left arrow)") /
- [delete-policy-engine →](delete-policy-engine.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](delete-policy-engine.html "delete-policy-engine") \|
- [previous](delete-payment-manager.html "delete-payment-manager") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [delete-policy]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

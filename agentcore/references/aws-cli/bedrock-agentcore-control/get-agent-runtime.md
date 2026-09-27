---
title: aws bedrock-agentcore-control get-agent-runtime
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/get-agent-runtime.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# get-agent-runtime

## Description

Gets an Amazon Bedrock AgentCore Runtime.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/GetAgentRuntime)

## Synopsis

      get-agent-runtime
    --agent-runtime-id <value>
    [--agent-runtime-version <value>]
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

`--agent-runtime-id` (string) \[required\]

> The unique identifier of the AgentCore Runtime to retrieve.
>
> Constraints:
>
> - pattern: `[a-zA-Z][a-zA-Z0-9_]{0,99}-[a-zA-Z0-9]{10}`

`--agent-runtime-version` (string)

> The version of the AgentCore Runtime to retrieve.
>
> Constraints:
>
> - min: `1`
> - max: `5`
> - pattern: `([1-9][0-9]{0,4})`

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

agentRuntimeArn -\> (string)

> The Amazon Resource Name (ARN) of the AgentCore Runtime.
>
> Constraints:
>
> - pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:runtime/[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}`

agentRuntimeName -\> (string)

> The name of the AgentCore Runtime.
>
> Constraints:
>
> - pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`

agentRuntimeId -\> (string)

> The unique identifier of the AgentCore Runtime.
>
> Constraints:
>
> - pattern: `[a-zA-Z][a-zA-Z0-9_]{0,99}-[a-zA-Z0-9]{10}`

agentRuntimeVersion -\> (string)

> The version of the AgentCore Runtime.
>
> Constraints:
>
> - min: `1`
> - max: `5`
> - pattern: `([1-9][0-9]{0,4})`

createdAt -\> (timestamp)

> The timestamp when the AgentCore Runtime was created.

lastUpdatedAt -\> (timestamp)

> The timestamp when the AgentCore Runtime was last updated.

roleArn -\> (string)

> The IAM role ARN that provides permissions for the AgentCore Runtime.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`

networkConfiguration -\> (structure)

> The network configuration for the AgentCore Runtime.
>
> networkMode -\> (string) \[required\]
>
> > The network mode for the AgentCore Runtime.
> >
> > Possible values:
> >
> > - `PUBLIC`
> > - `VPC`
>
> networkModeConfig -\> (structure)
>
> > The network mode configuration for the AgentCore Runtime.
> >
> > securityGroups -\> (list) \[required\]
> >
> > > The security groups associated with the VPC configuration.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `16`
> > >
> > > (string)
> > >
> > > > Constraints:
> > > >
> > > > - pattern: `sg-[0-9a-zA-Z]{8,17}`
> >
> > subnets -\> (list) \[required\]
> >
> > > The subnets associated with the VPC configuration.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `16`
> > >
> > > (string)
> > >
> > > > Constraints:
> > > >
> > > > - pattern: `subnet-[0-9a-zA-Z]{8,17}`
> >
> > requireServiceS3Endpoint -\> (boolean)
> >
> > > ### Note
> > >
> > > This field applies only to Agent Runtimes. It is not applicable to Browsers or Code Interpreters.
> > >
> > > Controls whether a service-managed Amazon S3 gateway endpoint is provisioned in the VPC network topology for the agent runtime. This gateway is used by Amazon Bedrock AgentCore Runtime to download code and container images during agent startup.
> > >
> > > Starting May 5, 2026, Amazon Bedrock AgentCore Runtime is gradually rolling out a change to how network isolation is configured for VPC mode agents. Agent runtimes created on or after this rollout will no longer include the service-managed Amazon S3 gateway. Instead, all network access, including to Amazon S3, is governed exclusively by your VPC configuration. This field cannot be set on agent runtimes created after the rollout. Passing this field in an `UpdateAgentRuntime` request for these agent runtimes returns a `ValidationException` .
> > >
> > > Agent runtimes created before the rollout are not affected and continue to operate with the service-managed Amazon S3 gateway. To enforce full VPC network isolation on these existing agent runtimes, set this field to `false` via the `UpdateAgentRuntime` API. Before opting out, ensure your VPC provides the Amazon S3 access required for agent startup. If this field is not specified or is set to `true` , the service-managed Amazon S3 gateway remains provisioned.
> > >
> > > This field is only supported in the `UpdateAgentRuntime` API for pre-rollout agent runtimes. Passing this field in a `CreateAgentRuntime` request returns a `ValidationException` .

status -\> (string)

> The current status of the AgentCore Runtime.
>
> Possible values:
>
> - `CREATING`
> - `CREATE_FAILED`
> - `UPDATING`
> - `UPDATE_FAILED`
> - `READY`
> - `DELETING`
> - `DELETE_FAILED`

lifecycleConfiguration -\> (structure)

> The life cycle configuration for the AgentCore Runtime.
>
> idleRuntimeSessionTimeout -\> (integer)
>
> > Timeout in seconds for idle runtime sessions. When a session remains idle for this duration, it will be automatically terminated. Default: 900 seconds (15 minutes).
> >
> > Constraints:
> >
> > - min: `60`
> > - max: `1209600`
>
> maxLifetime -\> (integer)
>
> > Maximum lifetime for the instance in seconds. Once reached, instances will be automatically terminated and replaced. Default: 28800 seconds (8 hours).
> >
> > Constraints:
> >
> > - min: `60`
> > - max: `1209600`

failureReason -\> (string)

> The reason for failure if the AgentCore Runtime is in a failed state.

description -\> (string)

> The description of the AgentCore Runtime.
>
> Constraints:
>
> - min: `1`
> - max: `4096`

workloadIdentityDetails -\> (structure)

> The workload identity details for the AgentCore Runtime.
>
> workloadIdentityArn -\> (string) \[required\]
>
> > The ARN associated with the workload identity.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `1024`

agentRuntimeArtifact -\> (tagged union structure)

> The artifact of the AgentCore Runtime.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `containerConfiguration`, `codeConfiguration`.
>
> containerConfiguration -\> (structure)
>
> > The container configuration for the agent artifact.
> >
> > containerUri -\> (string) \[required\]
> >
> > > The ECR URI of the container.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `1024`
> > > - pattern: `(([0-9]{12})\.dkr\.ecr\.([a-z0-9-]+)\.amazonaws\.com(\.cn)?|public\.ecr\.aws)/((?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*)(?::([^:@]{1,300}))?(?:@(.+))?`
>
> codeConfiguration -\> (structure)
>
> > The code configuration for the agent runtime artifact, including the source code location and execution settings.
> >
> > code -\> (tagged union structure) \[required\]
> >
> > > The source code location and configuration details.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `s3`.
> > >
> > > s3 -\> (structure)
> > >
> > > > The Amazon Amazon S3 object that contains the source code for the agent runtime.
> > > >
> > > > bucket -\> (string) \[required\]
> > > >
> > > > > The name of the Amazon S3 bucket. This bucket contains the stored data.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]`
> > > >
> > > > prefix -\> (string) \[required\]
> > > >
> > > > > The prefix for objects in the Amazon S3 bucket. This prefix is added to the object keys to organize the data.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `1024`
> > > >
> > > > versionId -\> (string)
> > > >
> > > > > The version ID of the Amazon Amazon S3 object. If not specified, the latest version of the object is used.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `3`
> > > > > - max: `1024`
> >
> > runtime -\> (string) \[required\]
> >
> > > The runtime environment for executing the agent code. Specify the programming language and version to use for the agent runtime. For valid values, see the list of supported runtimes.
> > >
> > > Possible values:
> > >
> > > - `PYTHON_3_10`
> > > - `PYTHON_3_11`
> > > - `PYTHON_3_12`
> > > - `PYTHON_3_13`
> > > - `PYTHON_3_14`
> > > - `NODE_22`
> >
> > entryPoint -\> (list) \[required\]
> >
> > > The entry point for the code execution, specifying the function or method that should be invoked when the code runs.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `2`
> > >
> > > (string)
> > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `128`

protocolConfiguration -\> (structure)

> The protocol configuration for an agent runtime. This structure defines how the agent runtime communicates with clients.
>
> serverProtocol -\> (string) \[required\]
>
> > The server protocol for the agent runtime. This field specifies which protocol the agent runtime uses to communicate with clients.
> >
> > Possible values:
> >
> > - `MCP`
> > - `HTTP`
> > - `A2A`
> > - `AGUI`

environmentVariables -\> (map)

> Environment variables set in the AgentCore Runtime environment.
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
> > - max: `100`
>
> value -\> (string)
>
> > Constraints:
> >
> > - min: `0`
> > - max: `5000`

authorizerConfiguration -\> (tagged union structure)

> The authorizer configuration for the AgentCore Runtime.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `customJWTAuthorizer`.
>
> customJWTAuthorizer -\> (structure)
>
> > The inbound JWT-based authorization, specifying how incoming requests should be authenticated.
> >
> > discoveryUrl -\> (string) \[required\]
> >
> > > This URL is used to fetch OpenID Connect configuration or authorization server metadata for validating incoming tokens.
> > >
> > > Constraints:
> > >
> > > - pattern: `.+/\.well-known/openid-configuration`
> >
> > allowedAudience -\> (list)
> >
> > > Represents individual audience values that are validated in the incoming JWT token validation process.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > >
> > > (string)
> >
> > allowedClients -\> (list)
> >
> > > Represents individual client IDs that are validated in the incoming JWT token validation process.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > >
> > > (string)
> >
> > allowedScopes -\> (list)
> >
> > > An array of scopes that are allowed to access the token.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > >
> > > (string)
> > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `255`
> > > > - pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
> >
> > advertisedScopeMapping -\> (map)
> >
> > > A map that associates each scope in `allowedScopes` with a corresponding advertised scope value. The advertised scope appears in OAuth protected resource metadata and `WWW-Authenticate` response headers. Use this parameter when the scope that clients request from your identity provider differs from the scope in the validated token. Each key is a scope from `allowedScopes` that the service uses for token validation. Each value is the corresponding scope that the service advertises to clients. Scopes without a mapping entry appear unchanged to clients.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `50`
> > >
> > > key -\> (string)
> > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `255`
> > > > - pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
> > >
> > > value -\> (string)
> > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `255`
> > > > - pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
> >
> > customClaims -\> (list)
> >
> > > An array of objects that define a custom claim validation name, value, and operation
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > >
> > > (structure)
> > >
> > > > Defines the name of a custom claim field and rules for finding matches to authenticate its value.
> > > >
> > > > inboundTokenClaimName -\> (string) \[required\]
> > > >
> > > > > The name of the custom claim field to check.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `255`
> > > > > - pattern: `[A-Za-z0-9_.-:]+`
> > > >
> > > > inboundTokenClaimValueType -\> (string) \[required\]
> > > >
> > > > > The data type of the claim value to check for.
> > > > >
> > > > > - Use `STRING` if you want to find an exact match to a string you define.
> > > > > - Use `STRING_ARRAY` if you want to fnd a match to at least one value in an array you define.
> > > > >
> > > > > Possible values:
> > > > >
> > > > > - `STRING`
> > > > > - `STRING_ARRAY`
> > > >
> > > > authorizingClaimMatchValue -\> (structure) \[required\]
> > > >
> > > > > Defines the value or values to match for and the relationship of the match.
> > > > >
> > > > > claimMatchValue -\> (tagged union structure) \[required\]
> > > > >
> > > > > > The value or values to match for.
> > > > > >
> > > > > > ### Note
> > > > > >
> > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `matchValueString`, `matchValueStringList`.
> > > > > >
> > > > > > matchValueString -\> (string)
> > > > > >
> > > > > > > The string value to match for.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> > > > > > > - pattern: `[A-Za-z0-9_.-]+`
> > > > > >
> > > > > > matchValueStringList -\> (list)
> > > > > >
> > > > > > > An array of strings to check for a match.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > >
> > > > > > > (string)
> > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > > > > - pattern: `[A-Za-z0-9_.-]+`
> > > > >
> > > > > claimMatchOperator -\> (string) \[required\]
> > > > >
> > > > > > Defines the relationship between the claim field value and the value or values you’re matching for.
> > > > > >
> > > > > > Possible values:
> > > > > >
> > > > > > - `EQUALS`
> > > > > > - `CONTAINS`
> > > > > > - `CONTAINS_ANY`
> >
> > privateEndpoint -\> (tagged union structure)
> >
> > > The private endpoint configuration for a gateway target. Defines how the gateway connects to private resources in your VPC.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `selfManagedLatticeResource`, `managedVpcResource`.
> > >
> > > selfManagedLatticeResource -\> (tagged union structure)
> > >
> > > > Configuration for connecting to a private resource using a self-managed VPC Lattice resource configuration.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `resourceConfigurationIdentifier`.
> > > >
> > > > resourceConfigurationIdentifier -\> (string)
> > > >
> > > > > The ARN or ID of the VPC Lattice resource configuration.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `20`
> > > > > - max: `2048`
> > > > > - pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`
> > >
> > > managedVpcResource -\> (structure)
> > >
> > > > Configuration for connecting to a private resource using a managed VPC Lattice resource. The gateway creates and manages the VPC Lattice resources on your behalf.
> > > >
> > > > vpcIdentifier -\> (string) \[required\]
> > > >
> > > > > The ID of the VPC that contains your private resource.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > >
> > > > subnetIds -\> (list) \[required\]
> > > >
> > > > > The subnet IDs within the VPC where the VPC Lattice resource gateway is placed.
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - pattern: `subnet-[0-9a-zA-Z]{8,17}`
> > > >
> > > > endpointIpAddressType -\> (string) \[required\]
> > > >
> > > > > The IP address type for the resource configuration endpoint.
> > > > >
> > > > > Possible values:
> > > > >
> > > > > - `IPV4`
> > > > > - `IPV6`
> > > >
> > > > securityGroupIds -\> (list)
> > > >
> > > > > The security group IDs to associate with the VPC Lattice resource gateway. If not specified, the default security group for the VPC is used.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `0`
> > > > > - max: `5`
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > >
> > > > tags -\> (map)
> > > >
> > > > > Tags to apply to the managed VPC Lattice resource gateway.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `0`
> > > > > - max: `50`
> > > > >
> > > > > key -\> (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `128`
> > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > >
> > > > > value -\> (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `0`
> > > > > > - max: `256`
> > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > >
> > > > routingDomain -\> (string)
> > > >
> > > > > An intermediate domain to use as the resource configuration endpoint instead of the actual target domain. Use this when you want to route traffic through an intermediate component such as a VPC endpoint or internal load balancer. For more information, see xref:lattice-vpc-egress-routing-domain\[Route traffic through an intermediate domain\].
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `3`
> > > > > - max: `255`
> >
> > privateEndpointOverrides -\> (list)
> >
> > > The private endpoint overrides for the custom JWT authorizer configuration.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `5`
> > >
> > > (structure)
> > >
> > > > A mapping of a specific domain to a private endpoint for secure connectivity through a VPC Lattice resource configuration.
> > > >
> > > > domain -\> (string) \[required\]
> > > >
> > > > > The domain to override with a private endpoint.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `253`
> > > >
> > > > privateEndpoint -\> (tagged union structure) \[required\]
> > > >
> > > > > The private endpoint configuration for the specified domain.
> > > > >
> > > > > ### Note
> > > > >
> > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `selfManagedLatticeResource`, `managedVpcResource`.
> > > > >
> > > > > selfManagedLatticeResource -\> (tagged union structure)
> > > > >
> > > > > > Configuration for connecting to a private resource using a self-managed VPC Lattice resource configuration.
> > > > > >
> > > > > > ### Note
> > > > > >
> > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `resourceConfigurationIdentifier`.
> > > > > >
> > > > > > resourceConfigurationIdentifier -\> (string)
> > > > > >
> > > > > > > The ARN or ID of the VPC Lattice resource configuration.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `20`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`
> > > > >
> > > > > managedVpcResource -\> (structure)
> > > > >
> > > > > > Configuration for connecting to a private resource using a managed VPC Lattice resource. The gateway creates and manages the VPC Lattice resources on your behalf.
> > > > > >
> > > > > > vpcIdentifier -\> (string) \[required\]
> > > > > >
> > > > > > > The ID of the VPC that contains your private resource.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > >
> > > > > > subnetIds -\> (list) \[required\]
> > > > > >
> > > > > > > The subnet IDs within the VPC where the VPC Lattice resource gateway is placed.
> > > > > > >
> > > > > > > (string)
> > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - pattern: `subnet-[0-9a-zA-Z]{8,17}`
> > > > > >
> > > > > > endpointIpAddressType -\> (string) \[required\]
> > > > > >
> > > > > > > The IP address type for the resource configuration endpoint.
> > > > > > >
> > > > > > > Possible values:
> > > > > > >
> > > > > > > - `IPV4`
> > > > > > > - `IPV6`
> > > > > >
> > > > > > securityGroupIds -\> (list)
> > > > > >
> > > > > > > The security group IDs to associate with the VPC Lattice resource gateway. If not specified, the default security group for the VPC is used.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `0`
> > > > > > > - max: `5`
> > > > > > >
> > > > > > > (string)
> > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > >
> > > > > > tags -\> (map)
> > > > > >
> > > > > > > Tags to apply to the managed VPC Lattice resource gateway.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `0`
> > > > > > > - max: `50`
> > > > > > >
> > > > > > > key -\> (string)
> > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `128`
> > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > > >
> > > > > > > value -\> (string)
> > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `0`
> > > > > > > > - max: `256`
> > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > >
> > > > > > routingDomain -\> (string)
> > > > > >
> > > > > > > An intermediate domain to use as the resource configuration endpoint instead of the actual target domain. Use this when you want to route traffic through an intermediate component such as a VPC endpoint or internal load balancer. For more information, see xref:lattice-vpc-egress-routing-domain\[Route traffic through an intermediate domain\].
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `3`
> > > > > > > - max: `255`
> >
> > allowedWorkloadConfiguration -\> (structure)
> >
> > > The configuration that restricts which workloads in the request’s identity chain are allowed to invoke the target, identified by their hosting environments and workload identities. At launch, this is supported only for AgentCore Runtime targets, and the allowed workloads are AgentCore Gateways.
> > >
> > > hostingEnvironments -\> (list)
> > >
> > > > The list of hosting environments whose workloads are allowed to invoke the target. At launch, the only supported hosting environment is AgentCore Gateway.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `10`
> > > >
> > > > (structure)
> > > >
> > > > > A hosting environment whose workloads are allowed to invoke the target. At launch, the only supported hosting environment is AgentCore Gateway.
> > > > >
> > > > > arn -\> (string) \[required\]
> > > > >
> > > > > > The Amazon Resource Name (ARN) of the hosting environment.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `20`
> > > > > > - max: `1011`
> > >
> > > workloadIdentities -\> (list)
> > >
> > > > The list of workload identities that are allowed to invoke the target.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `10`
> > > >
> > > > (string)
> > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `3`
> > > > > - max: `255`
> > > > > - pattern: `[A-Za-z0-9_.-]+`

requestHeaderConfiguration -\> (tagged union structure)

> Configuration for HTTP request headers that will be passed through to the runtime.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `requestHeaderAllowlist`.
>
> requestHeaderAllowlist -\> (list)
>
> > A list of HTTP request headers that are allowed to be passed through to the runtime.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `20`
> >
> > (string)
> >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `256`
> > > - pattern: `[A-Za-z][A-Za-z0-9_-]{0,255}`

metadataConfiguration -\> (structure)

> Configuration for microVM Metadata Service (MMDS) settings for the AgentCore Runtime.
>
> requireMMDSV2 -\> (boolean) \[required\]
>
> > Enables MMDSv2 (microVM Metadata Service Version 2) requirement for the agent runtime. When set to `true` , the runtime microVM will only accept MMDSv2 requests.

filesystemConfigurations -\> (list)

> The filesystem configurations mounted into the AgentCore Runtime.
>
> Constraints:
>
> - min: `0`
> - max: `5`
>
> (tagged union structure)
>
> > Configuration for a filesystem that can be mounted into the AgentCore Runtime.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `sessionStorage`, `s3FilesAccessPoint`, `efsAccessPoint`, `capacityProviderVolume`.
> >
> > sessionStorage -\> (structure)
> >
> > > Configuration for session storage. Session storage provides persistent storage that is preserved across AgentCore Runtime session invocations.
> > >
> > > mountPath -\> (string) \[required\]
> > >
> > > > The mount path for the session storage filesystem inside the AgentCore Runtime. The path must be under `/mnt` with exactly one subdirectory level (for example, `/mnt/data` ).
> > > >
> > > > Constraints:
> > > >
> > > > - min: `6`
> > > > - max: `200`
> > > > - pattern: `/mnt/[a-zA-Z0-9._-]+/?`
> >
> > s3FilesAccessPoint -\> (structure)
> >
> > > Configuration for an Amazon S3 Files access point to mount into the AgentCore Runtime.
> > >
> > > accessPointArn -\> (string) \[required\]
> > >
> > > > The ARN of the S3 Files access point to mount into the AgentCore Runtime.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0`
> > > > - max: `256`
> > > > - pattern: `arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}/access-point/fsap-[0-9a-f]{17,40}`
> > >
> > > mountPath -\> (string) \[required\]
> > >
> > > > The mount path for the S3 Files access point inside the AgentCore Runtime. The path must be under `/mnt` with exactly one subdirectory level (for example, `/mnt/data` ).
> > > >
> > > > Constraints:
> > > >
> > > > - min: `6`
> > > > - max: `200`
> > > > - pattern: `/mnt/[a-zA-Z0-9._-]+/?`
> >
> > efsAccessPoint -\> (structure)
> >
> > > Configuration for an Amazon EFS access point to mount into the AgentCore Runtime.
> > >
> > > accessPointArn -\> (string) \[required\]
> > >
> > > > The ARN of the EFS access point to mount into the AgentCore Runtime.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0`
> > > > - max: `128`
> > > > - pattern: `arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:access-point/fsap-[0-9a-f]{8,40}`
> > >
> > > mountPath -\> (string) \[required\]
> > >
> > > > The mount path for the EFS access point inside the AgentCore Runtime. The path must be under `/mnt` with exactly one subdirectory level (for example, `/mnt/data` ).
> > > >
> > > > Constraints:
> > > >
> > > > - min: `6`
> > > > - max: `200`
> > > > - pattern: `/mnt/[a-zA-Z0-9._-]+/?`
> >
> > capacityProviderVolume -\> (structure)
> >
> > > Configuration for a capacity provider volume to mount into the AgentCore Runtime. This mounts a persistent volume that is defined on the capacity provider, referenced by its logical name.
> > >
> > > volumeName -\> (string) \[required\]
> > >
> > > > The logical name of the capacity provider volume to mount. This name must match a volume that is defined in the capacity provider’s list of volumes.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `48`
> > > > - pattern: `[a-zA-Z][a-zA-Z0-9_-]{0,47}`
> > >
> > > mountPath -\> (string) \[required\]
> > >
> > > > The mount path for the capacity provider volume inside the AgentCore Runtime. The path must be under `/mnt` with exactly one subdirectory level (for example, `/mnt/data` ).
> > > >
> > > > Constraints:
> > > >
> > > > - min: `6`
> > > > - max: `200`
> > > > - pattern: `/mnt/[a-zA-Z0-9._-]+/?`

capacityProviderConfiguration -\> (structure)

> The capacity provider configuration for the AgentCore Runtime.
>
> capacityProviderArn -\> (string) \[required\]
>
> > The Amazon Resource Name (ARN) of the capacity provider to use for the AgentCore Runtime.
> >
> > Constraints:
> >
> > - pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:capacity-provider/[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}`

platformVersion -\> (string)

> The version of the runtime platform used by the AgentCore Runtime.
>
> Constraints:
>
> - min: `1`
> - max: `128`
> - pattern: `[^\s]+`

- [← delete-workload-identity](delete-workload-identity.html "previous chapter (use the left arrow)") /
- [get-agent-runtime-endpoint →](get-agent-runtime-endpoint.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](get-agent-runtime-endpoint.html "get-agent-runtime-endpoint") \|
- [previous](delete-workload-identity.html "delete-workload-identity") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [get-agent-runtime]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

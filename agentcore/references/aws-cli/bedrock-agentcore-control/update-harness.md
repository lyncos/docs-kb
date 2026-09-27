---
title: aws bedrock-agentcore-control update-harness
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/update-harness.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# update-harness

## Description

Operation to update a harness.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/UpdateHarness)

`update-harness` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

      update-harness
    --harness-id <value>
    [--client-token <value>]
    [--execution-role-arn <value>]
    [--environment <value>]
    [--environment-artifact <value>]
    [--environment-variables <value>]
    [--authorizer-configuration <value>]
    [--model <value>]
    [--system-prompt <value>]
    [--tools <value>]
    [--skills <value>]
    [--allowed-tools <value>]
    [--memory <value>]
    [--truncation <value>]
    [--hooks <value>]
    [--max-iterations <value>]
    [--max-tokens <value>]
    [--timeout-seconds <value>]
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

`--harness-id` (string) \[required\]

> The ID of the harness to update.
>
> Constraints:
>
> - pattern: `[a-zA-Z][a-zA-Z0-9_]{0,39}-[a-zA-Z0-9]{10}`

`--client-token` (string)

> A unique, case-sensitive identifier to ensure idempotency of the request.
>
> Constraints:
>
> - min: `33`
> - max: `256`
> - pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`

`--execution-role-arn` (string)

> The ARN of the IAM role that the harness assumes when running. If not specified, the existing value is retained.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`

`--environment` (tagged union structure)

> The compute environment configuration for the harness. If not specified, the existing value is retained.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `agentCoreRuntimeEnvironment`.
>
> agentCoreRuntimeEnvironment -\> (structure)
>
> > The AgentCore Runtime environment configuration.
> >
> > lifecycleConfiguration -\> (structure)
> >
> > > LifecycleConfiguration lets you manage the lifecycle of runtime sessions and resources in AgentCore Runtime. This configuration helps optimize resource utilization by automatically cleaning up idle sessions and preventing long-running instances from consuming resources indefinitely.
> > >
> > > idleRuntimeSessionTimeout -\> (integer)
> > >
> > > > Timeout in seconds for idle runtime sessions. When a session remains idle for this duration, it will be automatically terminated. Default: 900 seconds (15 minutes).
> > > >
> > > > Constraints:
> > > >
> > > > - min: `60`
> > > > - max: `1209600`
> > >
> > > maxLifetime -\> (integer)
> > >
> > > > Maximum lifetime for the instance in seconds. Once reached, instances will be automatically terminated and replaced. Default: 28800 seconds (8 hours).
> > > >
> > > > Constraints:
> > > >
> > > > - min: `60`
> > > > - max: `1209600`
> >
> > networkConfiguration -\> (structure)
> >
> > > SecurityConfig for the Agent.
> > >
> > > networkMode -\> (string) \[required\]
> > >
> > > > The network mode for the AgentCore Runtime.
> > > >
> > > > Possible values:
> > > >
> > > > - `PUBLIC`
> > > > - `VPC`
> > >
> > > networkModeConfig -\> (structure)
> > >
> > > > The network mode configuration for the AgentCore Runtime.
> > > >
> > > > securityGroups -\> (list) \[required\]
> > > >
> > > > > The security groups associated with the VPC configuration.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `16`
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - pattern: `sg-[0-9a-zA-Z]{8,17}`
> > > >
> > > > subnets -\> (list) \[required\]
> > > >
> > > > > The subnets associated with the VPC configuration.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `16`
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - pattern: `subnet-[0-9a-zA-Z]{8,17}`
> > > >
> > > > requireServiceS3Endpoint -\> (boolean)
> > > >
> > > > > ### Note
> > > > >
> > > > > This field applies only to Agent Runtimes. It is not applicable to Browsers or Code Interpreters.
> > > > >
> > > > > Controls whether a service-managed Amazon S3 gateway endpoint is provisioned in the VPC network topology for the agent runtime. This gateway is used by Amazon Bedrock AgentCore Runtime to download code and container images during agent startup.
> > > > >
> > > > > Starting May 5, 2026, Amazon Bedrock AgentCore Runtime is gradually rolling out a change to how network isolation is configured for VPC mode agents. Agent runtimes created on or after this rollout will no longer include the service-managed Amazon S3 gateway. Instead, all network access, including to Amazon S3, is governed exclusively by your VPC configuration. This field cannot be set on agent runtimes created after the rollout. Passing this field in an `UpdateAgentRuntime` request for these agent runtimes returns a `ValidationException` .
> > > > >
> > > > > Agent runtimes created before the rollout are not affected and continue to operate with the service-managed Amazon S3 gateway. To enforce full VPC network isolation on these existing agent runtimes, set this field to `false` via the `UpdateAgentRuntime` API. Before opting out, ensure your VPC provides the Amazon S3 access required for agent startup. If this field is not specified or is set to `true` , the service-managed Amazon S3 gateway remains provisioned.
> > > > >
> > > > > This field is only supported in the `UpdateAgentRuntime` API for pre-rollout agent runtimes. Passing this field in a `CreateAgentRuntime` request returns a `ValidationException` .
> >
> > filesystemConfigurations -\> (list)
> >
> > > The filesystem configurations for the runtime environment.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `5`
> > >
> > > (tagged union structure)
> > >
> > > > Configuration for a filesystem that can be mounted into the AgentCore Runtime.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `sessionStorage`, `s3FilesAccessPoint`, `efsAccessPoint`, `capacityProviderVolume`.
> > > >
> > > > sessionStorage -\> (structure)
> > > >
> > > > > Configuration for session storage. Session storage provides persistent storage that is preserved across AgentCore Runtime session invocations.
> > > > >
> > > > > mountPath -\> (string) \[required\]
> > > > >
> > > > > > The mount path for the session storage filesystem inside the AgentCore Runtime. The path must be under `/mnt` with exactly one subdirectory level (for example, `/mnt/data` ).
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `6`
> > > > > > - max: `200`
> > > > > > - pattern: `/mnt/[a-zA-Z0-9._-]+/?`
> > > >
> > > > s3FilesAccessPoint -\> (structure)
> > > >
> > > > > Configuration for an Amazon S3 Files access point to mount into the AgentCore Runtime.
> > > > >
> > > > > accessPointArn -\> (string) \[required\]
> > > > >
> > > > > > The ARN of the S3 Files access point to mount into the AgentCore Runtime.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `0`
> > > > > > - max: `256`
> > > > > > - pattern: `arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}/access-point/fsap-[0-9a-f]{17,40}`
> > > > >
> > > > > mountPath -\> (string) \[required\]
> > > > >
> > > > > > The mount path for the S3 Files access point inside the AgentCore Runtime. The path must be under `/mnt` with exactly one subdirectory level (for example, `/mnt/data` ).
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `6`
> > > > > > - max: `200`
> > > > > > - pattern: `/mnt/[a-zA-Z0-9._-]+/?`
> > > >
> > > > efsAccessPoint -\> (structure)
> > > >
> > > > > Configuration for an Amazon EFS access point to mount into the AgentCore Runtime.
> > > > >
> > > > > accessPointArn -\> (string) \[required\]
> > > > >
> > > > > > The ARN of the EFS access point to mount into the AgentCore Runtime.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `0`
> > > > > > - max: `128`
> > > > > > - pattern: `arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:access-point/fsap-[0-9a-f]{8,40}`
> > > > >
> > > > > mountPath -\> (string) \[required\]
> > > > >
> > > > > > The mount path for the EFS access point inside the AgentCore Runtime. The path must be under `/mnt` with exactly one subdirectory level (for example, `/mnt/data` ).
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `6`
> > > > > > - max: `200`
> > > > > > - pattern: `/mnt/[a-zA-Z0-9._-]+/?`
> > > >
> > > > capacityProviderVolume -\> (structure)
> > > >
> > > > > Configuration for a capacity provider volume to mount into the AgentCore Runtime. This mounts a persistent volume that is defined on the capacity provider, referenced by its logical name.
> > > > >
> > > > > volumeName -\> (string) \[required\]
> > > > >
> > > > > > The logical name of the capacity provider volume to mount. This name must match a volume that is defined in the capacity provider’s list of volumes.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `48`
> > > > > > - pattern: `[a-zA-Z][a-zA-Z0-9_-]{0,47}`
> > > > >
> > > > > mountPath -\> (string) \[required\]
> > > > >
> > > > > > The mount path for the capacity provider volume inside the AgentCore Runtime. The path must be under `/mnt` with exactly one subdirectory level (for example, `/mnt/data` ).
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `6`
> > > > > > - max: `200`
> > > > > > - pattern: `/mnt/[a-zA-Z0-9._-]+/?`

JSON Syntax:

    {
      "agentCoreRuntimeEnvironment": {
        "lifecycleConfiguration": {
          "idleRuntimeSessionTimeout": integer,
          "maxLifetime": integer
        },
        "networkConfiguration": {
          "networkMode": "PUBLIC"|"VPC",
          "networkModeConfig": {
            "securityGroups": ["string", ...],
            "subnets": ["string", ...],
            "requireServiceS3Endpoint": true|false
          }
        },
        "filesystemConfigurations": [
          {
            "sessionStorage": {
              "mountPath": "string"
            },
            "s3FilesAccessPoint": {
              "accessPointArn": "string",
              "mountPath": "string"
            },
            "efsAccessPoint": {
              "accessPointArn": "string",
              "mountPath": "string"
            },
            "capacityProviderVolume": {
              "volumeName": "string",
              "mountPath": "string"
            }
          }
          ...
        ]
      }
    }

`--environment-artifact` (structure)

> The environment artifact for the harness. Use the optionalValue wrapper to set a new value, or set it to null to clear the existing configuration.
>
> optionalValue -\> (tagged union structure)
>
> > The updated environment artifact value, or null to clear the existing configuration.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `containerConfiguration`.
> >
> > containerConfiguration -\> (structure)
> >
> > > Representation of a container configuration.
> > >
> > > containerUri -\> (string) \[required\]
> > >
> > > > The ECR URI of the container.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `1024`
> > > > - pattern: `(([0-9]{12})\.dkr\.ecr\.([a-z0-9-]+)\.amazonaws\.com(\.cn)?|public\.ecr\.aws)/((?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*)(?::([^:@]{1,300}))?(?:@(.+))?`

Shorthand Syntax:

    optionalValue={containerConfiguration={containerUri=string}}

JSON Syntax:

    {
      "optionalValue": {
        "containerConfiguration": {
          "containerUri": "string"
        }
      }
    }

`--environment-variables` (map)

> Environment variables to set in the harness runtime environment. If specified, this replaces all existing environment variables. If not specified, the existing value is retained.
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

Shorthand Syntax:

    KeyName1=string,KeyName2=string

JSON Syntax:

    {"string": "string"
      ...}

`--authorizer-configuration` (structure)

> Wrapper for updating an optional AuthorizerConfiguration field with PATCH semantics. When present in an update request, the authorizer configuration is replaced with optionalValue. When absent, the authorizer configuration is left unchanged. To unset, include the wrapper with optionalValue not specified.
>
> optionalValue -\> (tagged union structure)
>
> > The updated authorizer configuration value. If not specified, it will clear the current authorizer configuration of the resource.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `customJWTAuthorizer`.
> >
> > customJWTAuthorizer -\> (structure)
> >
> > > The inbound JWT-based authorization, specifying how incoming requests should be authenticated.
> > >
> > > discoveryUrl -\> (string) \[required\]
> > >
> > > > This URL is used to fetch OpenID Connect configuration or authorization server metadata for validating incoming tokens.
> > > >
> > > > Constraints:
> > > >
> > > > - pattern: `.+/\.well-known/openid-configuration`
> > >
> > > allowedAudience -\> (list)
> > >
> > > > Represents individual audience values that are validated in the incoming JWT token validation process.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > >
> > > > (string)
> > >
> > > allowedClients -\> (list)
> > >
> > > > Represents individual client IDs that are validated in the incoming JWT token validation process.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > >
> > > > (string)
> > >
> > > allowedScopes -\> (list)
> > >
> > > > An array of scopes that are allowed to access the token.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > >
> > > > (string)
> > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `255`
> > > > > - pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
> > >
> > > advertisedScopeMapping -\> (map)
> > >
> > > > A map that associates each scope in `allowedScopes` with a corresponding advertised scope value. The advertised scope appears in OAuth protected resource metadata and `WWW-Authenticate` response headers. Use this parameter when the scope that clients request from your identity provider differs from the scope in the validated token. Each key is a scope from `allowedScopes` that the service uses for token validation. Each value is the corresponding scope that the service advertises to clients. Scopes without a mapping entry appear unchanged to clients.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `50`
> > > >
> > > > key -\> (string)
> > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `255`
> > > > > - pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
> > > >
> > > > value -\> (string)
> > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `255`
> > > > > - pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
> > >
> > > customClaims -\> (list)
> > >
> > > > An array of objects that define a custom claim validation name, value, and operation
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > >
> > > > (structure)
> > > >
> > > > > Defines the name of a custom claim field and rules for finding matches to authenticate its value.
> > > > >
> > > > > inboundTokenClaimName -\> (string) \[required\]
> > > > >
> > > > > > The name of the custom claim field to check.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `255`
> > > > > > - pattern: `[A-Za-z0-9_.-:]+`
> > > > >
> > > > > inboundTokenClaimValueType -\> (string) \[required\]
> > > > >
> > > > > > The data type of the claim value to check for.
> > > > > >
> > > > > > - Use `STRING` if you want to find an exact match to a string you define.
> > > > > > - Use `STRING_ARRAY` if you want to fnd a match to at least one value in an array you define.
> > > > > >
> > > > > > Possible values:
> > > > > >
> > > > > > - `STRING`
> > > > > > - `STRING_ARRAY`
> > > > >
> > > > > authorizingClaimMatchValue -\> (structure) \[required\]
> > > > >
> > > > > > Defines the value or values to match for and the relationship of the match.
> > > > > >
> > > > > > claimMatchValue -\> (tagged union structure) \[required\]
> > > > > >
> > > > > > > The value or values to match for.
> > > > > > >
> > > > > > > ### Note
> > > > > > >
> > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `matchValueString`, `matchValueStringList`.
> > > > > > >
> > > > > > > matchValueString -\> (string)
> > > > > > >
> > > > > > > > The string value to match for.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > > > > - pattern: `[A-Za-z0-9_.-]+`
> > > > > > >
> > > > > > > matchValueStringList -\> (list)
> > > > > > >
> > > > > > > > An array of strings to check for a match.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > >
> > > > > > > > (string)
> > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `255`
> > > > > > > > > - pattern: `[A-Za-z0-9_.-]+`
> > > > > >
> > > > > > claimMatchOperator -\> (string) \[required\]
> > > > > >
> > > > > > > Defines the relationship between the claim field value and the value or values you’re matching for.
> > > > > > >
> > > > > > > Possible values:
> > > > > > >
> > > > > > > - `EQUALS`
> > > > > > > - `CONTAINS`
> > > > > > > - `CONTAINS_ANY`
> > >
> > > privateEndpoint -\> (tagged union structure)
> > >
> > > > The private endpoint configuration for a gateway target. Defines how the gateway connects to private resources in your VPC.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `selfManagedLatticeResource`, `managedVpcResource`.
> > > >
> > > > selfManagedLatticeResource -\> (tagged union structure)
> > > >
> > > > > Configuration for connecting to a private resource using a self-managed VPC Lattice resource configuration.
> > > > >
> > > > > ### Note
> > > > >
> > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `resourceConfigurationIdentifier`.
> > > > >
> > > > > resourceConfigurationIdentifier -\> (string)
> > > > >
> > > > > > The ARN or ID of the VPC Lattice resource configuration.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `20`
> > > > > > - max: `2048`
> > > > > > - pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`
> > > >
> > > > managedVpcResource -\> (structure)
> > > >
> > > > > Configuration for connecting to a private resource using a managed VPC Lattice resource. The gateway creates and manages the VPC Lattice resources on your behalf.
> > > > >
> > > > > vpcIdentifier -\> (string) \[required\]
> > > > >
> > > > > > The ID of the VPC that contains your private resource.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > >
> > > > > subnetIds -\> (list) \[required\]
> > > > >
> > > > > > The subnet IDs within the VPC where the VPC Lattice resource gateway is placed.
> > > > > >
> > > > > > (string)
> > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - pattern: `subnet-[0-9a-zA-Z]{8,17}`
> > > > >
> > > > > endpointIpAddressType -\> (string) \[required\]
> > > > >
> > > > > > The IP address type for the resource configuration endpoint.
> > > > > >
> > > > > > Possible values:
> > > > > >
> > > > > > - `IPV4`
> > > > > > - `IPV6`
> > > > >
> > > > > securityGroupIds -\> (list)
> > > > >
> > > > > > The security group IDs to associate with the VPC Lattice resource gateway. If not specified, the default security group for the VPC is used.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `0`
> > > > > > - max: `5`
> > > > > >
> > > > > > (string)
> > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > >
> > > > > tags -\> (map)
> > > > >
> > > > > > Tags to apply to the managed VPC Lattice resource gateway.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `0`
> > > > > > - max: `50`
> > > > > >
> > > > > > key -\> (string)
> > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `128`
> > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > >
> > > > > > value -\> (string)
> > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `0`
> > > > > > > - max: `256`
> > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > >
> > > > > routingDomain -\> (string)
> > > > >
> > > > > > An intermediate domain to use as the resource configuration endpoint instead of the actual target domain. Use this when you want to route traffic through an intermediate component such as a VPC endpoint or internal load balancer. For more information, see xref:lattice-vpc-egress-routing-domain\[Route traffic through an intermediate domain\].
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `3`
> > > > > > - max: `255`
> > >
> > > privateEndpointOverrides -\> (list)
> > >
> > > > The private endpoint overrides for the custom JWT authorizer configuration.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0`
> > > > - max: `5`
> > > >
> > > > (structure)
> > > >
> > > > > A mapping of a specific domain to a private endpoint for secure connectivity through a VPC Lattice resource configuration.
> > > > >
> > > > > domain -\> (string) \[required\]
> > > > >
> > > > > > The domain to override with a private endpoint.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `253`
> > > > >
> > > > > privateEndpoint -\> (tagged union structure) \[required\]
> > > > >
> > > > > > The private endpoint configuration for the specified domain.
> > > > > >
> > > > > > ### Note
> > > > > >
> > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `selfManagedLatticeResource`, `managedVpcResource`.
> > > > > >
> > > > > > selfManagedLatticeResource -\> (tagged union structure)
> > > > > >
> > > > > > > Configuration for connecting to a private resource using a self-managed VPC Lattice resource configuration.
> > > > > > >
> > > > > > > ### Note
> > > > > > >
> > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `resourceConfigurationIdentifier`.
> > > > > > >
> > > > > > > resourceConfigurationIdentifier -\> (string)
> > > > > > >
> > > > > > > > The ARN or ID of the VPC Lattice resource configuration.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `20`
> > > > > > > > - max: `2048`
> > > > > > > > - pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`
> > > > > >
> > > > > > managedVpcResource -\> (structure)
> > > > > >
> > > > > > > Configuration for connecting to a private resource using a managed VPC Lattice resource. The gateway creates and manages the VPC Lattice resources on your behalf.
> > > > > > >
> > > > > > > vpcIdentifier -\> (string) \[required\]
> > > > > > >
> > > > > > > > The ID of the VPC that contains your private resource.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > > >
> > > > > > > subnetIds -\> (list) \[required\]
> > > > > > >
> > > > > > > > The subnet IDs within the VPC where the VPC Lattice resource gateway is placed.
> > > > > > > >
> > > > > > > > (string)
> > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - pattern: `subnet-[0-9a-zA-Z]{8,17}`
> > > > > > >
> > > > > > > endpointIpAddressType -\> (string) \[required\]
> > > > > > >
> > > > > > > > The IP address type for the resource configuration endpoint.
> > > > > > > >
> > > > > > > > Possible values:
> > > > > > > >
> > > > > > > > - `IPV4`
> > > > > > > > - `IPV6`
> > > > > > >
> > > > > > > securityGroupIds -\> (list)
> > > > > > >
> > > > > > > > The security group IDs to associate with the VPC Lattice resource gateway. If not specified, the default security group for the VPC is used.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `0`
> > > > > > > > - max: `5`
> > > > > > > >
> > > > > > > > (string)
> > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > > >
> > > > > > > tags -\> (map)
> > > > > > >
> > > > > > > > Tags to apply to the managed VPC Lattice resource gateway.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `0`
> > > > > > > > - max: `50`
> > > > > > > >
> > > > > > > > key -\> (string)
> > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `128`
> > > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > > > >
> > > > > > > > value -\> (string)
> > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `0`
> > > > > > > > > - max: `256`
> > > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > > >
> > > > > > > routingDomain -\> (string)
> > > > > > >
> > > > > > > > An intermediate domain to use as the resource configuration endpoint instead of the actual target domain. Use this when you want to route traffic through an intermediate component such as a VPC endpoint or internal load balancer. For more information, see xref:lattice-vpc-egress-routing-domain\[Route traffic through an intermediate domain\].
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `3`
> > > > > > > > - max: `255`
> > >
> > > allowedWorkloadConfiguration -\> (structure)
> > >
> > > > The configuration that restricts which workloads in the request’s identity chain are allowed to invoke the target, identified by their hosting environments and workload identities. At launch, this is supported only for AgentCore Runtime targets, and the allowed workloads are AgentCore Gateways.
> > > >
> > > > hostingEnvironments -\> (list)
> > > >
> > > > > The list of hosting environments whose workloads are allowed to invoke the target. At launch, the only supported hosting environment is AgentCore Gateway.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `10`
> > > > >
> > > > > (structure)
> > > > >
> > > > > > A hosting environment whose workloads are allowed to invoke the target. At launch, the only supported hosting environment is AgentCore Gateway.
> > > > > >
> > > > > > arn -\> (string) \[required\]
> > > > > >
> > > > > > > The Amazon Resource Name (ARN) of the hosting environment.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `20`
> > > > > > > - max: `1011`
> > > >
> > > > workloadIdentities -\> (list)
> > > >
> > > > > The list of workload identities that are allowed to invoke the target.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `10`
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `3`
> > > > > > - max: `255`
> > > > > > - pattern: `[A-Za-z0-9_.-]+`

JSON Syntax:

    {
      "optionalValue": {
        "customJWTAuthorizer": {
          "discoveryUrl": "string",
          "allowedAudience": ["string", ...],
          "allowedClients": ["string", ...],
          "allowedScopes": ["string", ...],
          "advertisedScopeMapping": {"string": "string"
            ...},
          "customClaims": [
            {
              "inboundTokenClaimName": "string",
              "inboundTokenClaimValueType": "STRING"|"STRING_ARRAY",
              "authorizingClaimMatchValue": {
                "claimMatchValue": {
                  "matchValueString": "string",
                  "matchValueStringList": ["string", ...]
                },
                "claimMatchOperator": "EQUALS"|"CONTAINS"|"CONTAINS_ANY"
              }
            }
            ...
          ],
          "privateEndpoint": {
            "selfManagedLatticeResource": {
              "resourceConfigurationIdentifier": "string"
            },
            "managedVpcResource": {
              "vpcIdentifier": "string",
              "subnetIds": ["string", ...],
              "endpointIpAddressType": "IPV4"|"IPV6",
              "securityGroupIds": ["string", ...],
              "tags": {"string": "string"
                ...},
              "routingDomain": "string"
            }
          },
          "privateEndpointOverrides": [
            {
              "domain": "string",
              "privateEndpoint": {
                "selfManagedLatticeResource": {
                  "resourceConfigurationIdentifier": "string"
                },
                "managedVpcResource": {
                  "vpcIdentifier": "string",
                  "subnetIds": ["string", ...],
                  "endpointIpAddressType": "IPV4"|"IPV6",
                  "securityGroupIds": ["string", ...],
                  "tags": {"string": "string"
                    ...},
                  "routingDomain": "string"
                }
              }
            }
            ...
          ],
          "allowedWorkloadConfiguration": {
            "hostingEnvironments": [
              {
                "arn": "string"
              }
              ...
            ],
            "workloadIdentities": ["string", ...]
          }
        }
      }
    }

`--model` (tagged union structure)

> The model configuration for the harness. If not specified, the existing value is retained.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `bedrockModelConfig`, `openAiModelConfig`, `geminiModelConfig`, `liteLlmModelConfig`.
>
> bedrockModelConfig -\> (structure)
>
> > Configuration for an Amazon Bedrock model.
> >
> > modelId -\> (string) \[required\]
> >
> > > The Bedrock model ID.
> >
> > maxTokens -\> (integer)
> >
> > > The maximum number of tokens to allow in the generated response per model call.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> >
> > temperature -\> (float)
> >
> > > The temperature to set when calling the model.
> > >
> > > Constraints:
> > >
> > > - min: `0.0`
> > > - max: `2.0`
> >
> > topP -\> (float)
> >
> > > The topP set when calling the model.
> > >
> > > Constraints:
> > >
> > > - min: `0.0`
> > > - max: `1.0`
> >
> > apiFormat -\> (string)
> >
> > > The API format to use when calling the Bedrock provider.
> > >
> > > Possible values:
> > >
> > > - `converse_stream`
> > > - `responses`
> > > - `chat_completions`
> >
> > additionalParams -\> (document)
> >
> > > Provider-specific parameters passed through to the model provider unchanged.
>
> openAiModelConfig -\> (structure)
>
> > Configuration for an OpenAI model.
> >
> > modelId -\> (string) \[required\]
> >
> > > The OpenAI model ID.
> >
> > apiKeyArn -\> (string) \[required\]
> >
> > > The ARN of your OpenAI API key on AgentCore Identity.
> > >
> > > Constraints:
> > >
> > > - pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+`
> >
> > apiBase -\> (string)
> >
> > > Optional custom endpoint URL for an OpenAI-compatible endpoint.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `16383`
> >
> > maxTokens -\> (integer)
> >
> > > The maximum number of tokens to allow in the generated response per model call.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> >
> > temperature -\> (float)
> >
> > > The temperature to set when calling the model.
> > >
> > > Constraints:
> > >
> > > - min: `0.0`
> > > - max: `2.0`
> >
> > topP -\> (float)
> >
> > > The topP set when calling the model.
> > >
> > > Constraints:
> > >
> > > - min: `0.0`
> > > - max: `1.0`
> >
> > apiFormat -\> (string)
> >
> > > The API format to use when calling the OpenAI provider.
> > >
> > > Possible values:
> > >
> > > - `chat_completions`
> > > - `responses`
> >
> > additionalParams -\> (document)
> >
> > > Provider-specific parameters passed through to the model provider unchanged.
>
> geminiModelConfig -\> (structure)
>
> > Configuration for a Google Gemini model.
> >
> > modelId -\> (string) \[required\]
> >
> > > The Gemini model ID.
> >
> > apiKeyArn -\> (string) \[required\]
> >
> > > The ARN of your Gemini API key on AgentCore Identity.
> > >
> > > Constraints:
> > >
> > > - pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+`
> >
> > maxTokens -\> (integer)
> >
> > > The maximum number of tokens to allow in the generated response per model call.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> >
> > temperature -\> (float)
> >
> > > The temperature to set when calling the model.
> > >
> > > Constraints:
> > >
> > > - min: `0.0`
> > > - max: `2.0`
> >
> > topP -\> (float)
> >
> > > The topP set when calling the model.
> > >
> > > Constraints:
> > >
> > > - min: `0.0`
> > > - max: `1.0`
> >
> > topK -\> (integer)
> >
> > > The topK set when calling the model.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `500`
> >
> > additionalParams -\> (document)
> >
> > > Provider-specific parameters passed through to the Gemini model provider unchanged.
>
> liteLlmModelConfig -\> (structure)
>
> > The LiteLLM model configuration for connecting to third-party model providers.
> >
> > modelId -\> (string) \[required\]
> >
> > > The LiteLLM model identifier (e.g., “anthropic/claude-3-sonnet”).
> >
> > apiKeyArn -\> (string)
> >
> > > The ARN of the API key in AgentCore Identity for authenticating with the model provider.
> > >
> > > Constraints:
> > >
> > > - pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+`
> >
> > apiBase -\> (string)
> >
> > > The base URL for the model provider’s API endpoint.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `16383`
> >
> > maxTokens -\> (integer)
> >
> > > The maximum number of tokens to allow in the generated response per iteration.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> >
> > temperature -\> (float)
> >
> > > The temperature to set when calling the model.
> > >
> > > Constraints:
> > >
> > > - min: `0.0`
> > > - max: `2.0`
> >
> > topP -\> (float)
> >
> > > The topP set when calling the model.
> > >
> > > Constraints:
> > >
> > > - min: `0.0`
> > > - max: `1.0`
> >
> > additionalParams -\> (document)
> >
> > > Provider-specific parameters passed through to the model provider unchanged.

Shorthand Syntax:

    bedrockModelConfig={modelId=string,maxTokens=integer,temperature=float,topP=float,apiFormat=string},openAiModelConfig={modelId=string,apiKeyArn=string,apiBase=string,maxTokens=integer,temperature=float,topP=float,apiFormat=string},geminiModelConfig={modelId=string,apiKeyArn=string,maxTokens=integer,temperature=float,topP=float,topK=integer},liteLlmModelConfig={modelId=string,apiKeyArn=string,apiBase=string,maxTokens=integer,temperature=float,topP=float}

JSON Syntax:

    {
      "bedrockModelConfig": {
        "modelId": "string",
        "maxTokens": integer,
        "temperature": float,
        "topP": float,
        "apiFormat": "converse_stream"|"responses"|"chat_completions",
        "additionalParams": {...}
      },
      "openAiModelConfig": {
        "modelId": "string",
        "apiKeyArn": "string",
        "apiBase": "string",
        "maxTokens": integer,
        "temperature": float,
        "topP": float,
        "apiFormat": "chat_completions"|"responses",
        "additionalParams": {...}
      },
      "geminiModelConfig": {
        "modelId": "string",
        "apiKeyArn": "string",
        "maxTokens": integer,
        "temperature": float,
        "topP": float,
        "topK": integer,
        "additionalParams": {...}
      },
      "liteLlmModelConfig": {
        "modelId": "string",
        "apiKeyArn": "string",
        "apiBase": "string",
        "maxTokens": integer,
        "temperature": float,
        "topP": float,
        "additionalParams": {...}
      }
    }

`--system-prompt` (list)

> The system prompt that defines the agent’s behavior. If not specified, the existing value is retained.
>
> (tagged union structure)
>
> > A content block in the system prompt.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `text`.
> >
> > text -\> (string)
> >
> > > The text content of the system prompt block.
> > >
> > > Constraints:
> > >
> > > - min: `1`

Shorthand Syntax:

    text=string ...

JSON Syntax:

    [
      {
        "text": "string"
      }
      ...
    ]

`--tools` (list)

> The tools available to the agent. If specified, this replaces all existing tools. If not specified, the existing value is retained.
>
> (structure)
>
> > A tool available to the agent loop.
> >
> > type -\> (string) \[required\]
> >
> > > The type of tool.
> > >
> > > Possible values:
> > >
> > > - `remote_mcp`
> > > - `agentcore_browser`
> > > - `agentcore_gateway`
> > > - `inline_function`
> > > - `agentcore_code_interpreter`
> >
> > name -\> (string)
> >
> > > Unique name for the tool. If not provided, a name will be inferred or generated.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `64`
> > > - pattern: `[a-zA-Z0-9_-]+`
> >
> > config -\> (tagged union structure)
> >
> > > Tool-specific configuration.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `remoteMcp`, `agentCoreBrowser`, `agentCoreGateway`, `inlineFunction`, `agentCoreCodeInterpreter`.
> > >
> > > remoteMcp -\> (structure)
> > >
> > > > Configuration for remote MCP server.
> > > >
> > > > url -\> (string) \[required\]
> > > >
> > > > > URL of the MCP endpoint.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `16383`
> > > >
> > > > headers -\> (map)
> > > >
> > > > > Custom headers to include when connecting to the remote MCP server.
> > > > >
> > > > > key -\> (string)
> > > > >
> > > > > > The key of an HTTP header.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `16383`
> > > > >
> > > > > value -\> (string)
> > > > >
> > > > > > The value of an HTTP header.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `16383`
> > >
> > > agentCoreBrowser -\> (structure)
> > >
> > > > Configuration for AgentCore Browser.
> > > >
> > > > browserArn -\> (string)
> > > >
> > > > > If not populated, the built-in Browser ARN is used.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:(aws|[0-9]{12}):browser(-custom)?/(aws\.browser\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})`
> > >
> > > agentCoreGateway -\> (structure)
> > >
> > > > Configuration for AgentCore Gateway.
> > > >
> > > > gatewayArn -\> (string) \[required\]
> > > >
> > > > > The ARN of the desired AgentCore Gateway.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}`
> > > >
> > > > outboundAuth -\> (tagged union structure)
> > > >
> > > > > How harness authenticates to this Gateway. Defaults to AWS_IAM (SigV4) if omitted.
> > > > >
> > > > > ### Note
> > > > >
> > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `awsIam`, `none`, `oauth`.
> > > > >
> > > > > awsIam -\> (structure)
> > > > >
> > > > > > SigV4-sign requests using the agent’s execution role.
> > > > >
> > > > > none -\> (structure)
> > > > >
> > > > > > No authentication.
> > > > >
> > > > > oauth -\> (structure)
> > > > >
> > > > > > Use OAuth credentials for outbound authentication to the gateway.
> > > > > >
> > > > > > providerArn -\> (string) \[required\]
> > > > > >
> > > > > > > The Amazon Resource Name (ARN) of the OAuth credential provider. This ARN identifies the provider in Amazon Web Services.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - pattern: `arn:([^:]*):([^:]*):([^:]*):([0-9]{12})?:(.+)`
> > > > > >
> > > > > > scopes -\> (list) \[required\]
> > > > > >
> > > > > > > The OAuth scopes for the credential provider. These scopes define the level of access requested from the OAuth provider.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `0`
> > > > > > > - max: `100`
> > > > > > >
> > > > > > > (string)
> > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `64`
> > > > > >
> > > > > > customParameters -\> (map)
> > > > > >
> > > > > > > The custom parameters for the OAuth credential provider. These parameters provide additional configuration for the OAuth authentication process.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `10`
> > > > > > >
> > > > > > > key -\> (string)
> > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `256`
> > > > > > >
> > > > > > > value -\> (string)
> > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `2048`
> > > > > >
> > > > > > grantType -\> (string)
> > > > > >
> > > > > > > Specifies the kind of credentials to use for authorization:
> > > > > > >
> > > > > > > - `CLIENT_CREDENTIALS` - Authorization with a client ID and secret.
> > > > > > > - `AUTHORIZATION_CODE` - Authorization with a token that is specific to an individual end user.
> > > > > > > - `TOKEN_EXCHANGE` - Authorization using on-behalf-of token exchange. An inbound user token is exchanged for a downstream access token scoped to the target audience.
> > > > > > >
> > > > > > > Possible values:
> > > > > > >
> > > > > > > - `CLIENT_CREDENTIALS`
> > > > > > > - `AUTHORIZATION_CODE`
> > > > > > > - `TOKEN_EXCHANGE`
> > > > > >
> > > > > > defaultReturnUrl -\> (string)
> > > > > >
> > > > > > > The URL where the end user’s browser is redirected after obtaining the authorization code. Generally points to the customer’s application.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `\w+:(\/?\/?)[^\s]+`
> > >
> > > inlineFunction -\> (structure)
> > >
> > > > Configuration for an inline function tool.
> > > >
> > > > description -\> (string) \[required\]
> > > >
> > > > > Description of what the tool does, provided to the model.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `4096`
> > > >
> > > > inputSchema -\> (document) \[required\]
> > > >
> > > > > JSON Schema describing the tool’s input parameters.
> > >
> > > agentCoreCodeInterpreter -\> (structure)
> > >
> > > > Configuration for AgentCore Code Interpreter.
> > > >
> > > > codeInterpreterArn -\> (string)
> > > >
> > > > > If not populated, the built-in Code Interpreter ARN is used.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:(aws|[0-9]{12}):code-interpreter(-custom)?/(aws\.codeinterpreter\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})`

JSON Syntax:

    [
      {
        "type": "remote_mcp"|"agentcore_browser"|"agentcore_gateway"|"inline_function"|"agentcore_code_interpreter",
        "name": "string",
        "config": {
          "remoteMcp": {
            "url": "string",
            "headers": {"string": "string"
              ...}
          },
          "agentCoreBrowser": {
            "browserArn": "string"
          },
          "agentCoreGateway": {
            "gatewayArn": "string",
            "outboundAuth": {
              "awsIam": {

              },
              "none": {

              },
              "oauth": {
                "providerArn": "string",
                "scopes": ["string", ...],
                "customParameters": {"string": "string"
                  ...},
                "grantType": "CLIENT_CREDENTIALS"|"AUTHORIZATION_CODE"|"TOKEN_EXCHANGE",
                "defaultReturnUrl": "string"
              }
            }
          },
          "inlineFunction": {
            "description": "string",
            "inputSchema": {...}
          },
          "agentCoreCodeInterpreter": {
            "codeInterpreterArn": "string"
          }
        }
      }
      ...
    ]

`--skills` (list)

> The skills available to the agent. If specified, this replaces all existing skills. If not specified, the existing value is retained.
>
> (tagged union structure)
>
> > A skill available to the agent.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `path`, `s3`, `git`, `awsSkills`.
> >
> > path -\> (string)
> >
> > > The filesystem path to the skill definition.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `4096`
> >
> > s3 -\> (structure)
> >
> > > An S3 source containing the skill.
> > >
> > > uri -\> (string) \[required\]
> > >
> > > > The S3 URI pointing to the skill directory (e.g., s3://bucket/skills/my-skill/).
> > > >
> > > > Constraints:
> > > >
> > > > - min: `5`
> > > > - max: `16383`
> > > > - pattern: `s3://.*`
> >
> > git -\> (structure)
> >
> > > A git repository containing the skill.
> > >
> > > url -\> (string) \[required\]
> > >
> > > > The HTTPS URL of the git repository.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `8`
> > > > - max: `16383`
> > > > - pattern: `https://[^#@]+`
> > >
> > > path -\> (string)
> > >
> > > > Subdirectory within the repository containing the skill.
> > >
> > > auth -\> (structure)
> > >
> > > > Authentication configuration for private repositories.
> > > >
> > > > credentialArn -\> (string) \[required\]
> > > >
> > > > > The ARN of the credential in AgentCore Identity containing the password or personal access token.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+`
> > > >
> > > > username -\> (string)
> > > >
> > > > > Username for authentication. Defaults to ‘oauth2’ if not specified.
> >
> > awsSkills -\> (structure)
> >
> > > AWS Skills baked into the harness’s underlying Runtime.
> > >
> > > paths -\> (list)
> > >
> > > > Optionally filter allowed skills with glob syntax, e.g., \[‘core-skills/[\*](#id1)’\].
> > > >
> > > > (string)
> > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `4096`
> > > > > - pattern: `([^*?\[\]]|\*)+`

Shorthand Syntax:

    path=string,s3={uri=string},git={url=string,path=string,auth={credentialArn=string,username=string}},awsSkills={paths=[string,string]} ...

JSON Syntax:

    [
      {
        "path": "string",
        "s3": {
          "uri": "string"
        },
        "git": {
          "url": "string",
          "path": "string",
          "auth": {
            "credentialArn": "string",
            "username": "string"
          }
        },
        "awsSkills": {
          "paths": ["string", ...]
        }
      }
      ...
    ]

`--allowed-tools` (list)

> The tools that the agent is allowed to use. If specified, this replaces all existing allowed tools. If not specified, the existing value is retained.
>
> (string)
>
> > Constraints:
> >
> > - min: `1`
> > - max: `64`
> > - pattern: `(\*|@?[^/]+(/[^/]+)?)`

Syntax:

    "string" "string" ...

`--memory` (structure)

> The AgentCore Memory configuration. Use the optionalValue wrapper to set a new value, or set it to null to clear the existing configuration.
>
> optionalValue -\> (tagged union structure)
>
> > The updated memory configuration value, or null to clear the existing configuration.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `agentCoreMemoryConfiguration`, `managedMemoryConfiguration`, `disabled`.
> >
> > agentCoreMemoryConfiguration -\> (structure)
> >
> > > The AgentCore Memory configuration.
> > >
> > > arn -\> (string) \[required\]
> > >
> > > > The ARN of the AgentCore Memory resource.
> > > >
> > > > Constraints:
> > > >
> > > > - pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
> > >
> > > actorId -\> (string)
> > >
> > > > The actor ID for memory operations.
> > >
> > > messagesCount -\> (integer)
> > >
> > > > The number of messages to retrieve from memory.
> > >
> > > retrievalConfig -\> (map)
> > >
> > > > The retrieval configuration for long-term memory, mapping namespace path templates to retrieval settings.
> > > >
> > > > key -\> (string)
> > > >
> > > > value -\> (structure)
> > > >
> > > > > Configuration for memory retrieval within a namespace.
> > > > >
> > > > > topK -\> (integer)
> > > > >
> > > > > > The maximum number of memory entries to retrieve.
> > > > >
> > > > > relevanceScore -\> (float)
> > > > >
> > > > > > The minimum relevance score for retrieved memories.
> > > > >
> > > > > strategyId -\> (string)
> > > > >
> > > > > > The ID of the retrieval strategy to use.
> >
> > managedMemoryConfiguration -\> (structure)
> >
> > > Harness creates and manages a memory resource in the customer’s account.
> > >
> > > arn -\> (string)
> > >
> > > > The ARN of the managed AgentCore Memory resource. Read-only on Get, ignored on Create/Update input.
> > > >
> > > > Constraints:
> > > >
> > > > - pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
> > >
> > > strategies -\> (list)
> > >
> > > > Strategy types to enable. Defaults to \[SEMANTIC, SUMMARIZATION\].
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `4`
> > > >
> > > > (string)
> > > >
> > > > > Possible values:
> > > > >
> > > > > - `SEMANTIC`
> > > > > - `SUMMARIZATION`
> > > > > - `USER_PREFERENCE`
> > > > > - `EPISODIC`
> > >
> > > eventExpiryDuration -\> (integer)
> > >
> > > > Event retention in days. Defaults to 30.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `3`
> > > > - max: `365`
> > >
> > > encryptionKeyArn -\> (string)
> > >
> > > > Customer-managed KMS key. Defaults to AWS-owned key. Not updatable after creation.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `2048`
> > > > - pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`
> >
> > disabled -\> (structure)
> >
> > > Explicitly opt out of memory.

JSON Syntax:

    {
      "optionalValue": {
        "agentCoreMemoryConfiguration": {
          "arn": "string",
          "actorId": "string",
          "messagesCount": integer,
          "retrievalConfig": {"string": {
                "topK": integer,
                "relevanceScore": float,
                "strategyId": "string"
              }
            ...}
        },
        "managedMemoryConfiguration": {
          "arn": "string",
          "strategies": ["SEMANTIC"|"SUMMARIZATION"|"USER_PREFERENCE"|"EPISODIC", ...],
          "eventExpiryDuration": integer,
          "encryptionKeyArn": "string"
        },
        "disabled": {

        }
      }
    }

`--truncation` (structure)

> The truncation configuration for managing conversation context. If not specified, the existing value is retained.
>
> strategy -\> (string) \[required\]
>
> > The truncation strategy to use.
> >
> > Possible values:
> >
> > - `sliding_window`
> > - `summarization`
> > - `none`
>
> config -\> (tagged union structure)
>
> > The strategy-specific configuration.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `slidingWindow`, `summarization`.
> >
> > slidingWindow -\> (structure)
> >
> > > Configuration for sliding window truncation.
> > >
> > > messagesCount -\> (integer)
> > >
> > > > The number of recent messages to retain in the context window.
> >
> > summarization -\> (structure)
> >
> > > Configuration for summarization-based truncation.
> > >
> > > summaryRatio -\> (float)
> > >
> > > > The ratio of content to summarize.
> > >
> > > preserveRecentMessages -\> (integer)
> > >
> > > > The number of recent messages to preserve without summarization.
> > >
> > > summarizationSystemPrompt -\> (string)
> > >
> > > > The system prompt used for generating summaries.

Shorthand Syntax:

    strategy=string,config={slidingWindow={messagesCount=integer},summarization={summaryRatio=float,preserveRecentMessages=integer,summarizationSystemPrompt=string}}

JSON Syntax:

    {
      "strategy": "sliding_window"|"summarization"|"none",
      "config": {
        "slidingWindow": {
          "messagesCount": integer
        },
        "summarization": {
          "summaryRatio": float,
          "preserveRecentMessages": integer,
          "summarizationSystemPrompt": "string"
        }
      }
    }

`--hooks` (list)

> The lifecycle hooks to run at defined points in the agent loop. If specified, this replaces all existing hooks. If not specified, the existing hooks are retained.
>
> Constraints:
>
> - min: `0`
> - max: `20`
>
> (tagged union structure)
>
> > A lifecycle hook configuration. Specify one hook type.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `beforeInvocation`, `afterInvocation`, `beforeToolCall`, `afterToolCall`.
> >
> > beforeInvocation -\> (structure)
> >
> > > A hook that runs before an invocation begins.
> > >
> > > name -\> (string) \[required\]
> > >
> > > > The name of the hook.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `64`
> > > > - pattern: `[a-zA-Z0-9_-]+`
> > >
> > > target -\> (tagged union structure) \[required\]
> > >
> > > > The target that receives the hook event.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `lambda`, `sns`, `eventBridge`.
> > > >
> > > > lambda -\> (structure)
> > > >
> > > > > A Lambda hook target that invokes an AWS Lambda function synchronously and waits for its response.
> > > > >
> > > > > arn -\> (string) \[required\]
> > > > >
> > > > > > The ARN of the Lambda function to invoke.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `20`
> > > > > > - max: `2048`
> > > > > > - pattern: `arn:aws(-[^:]+)?:lambda:[a-z0-9-]+:[0-9]{12}:function:.+`
> > > > >
> > > > > timeoutSeconds -\> (integer)
> > > > >
> > > > > > The maximum number of seconds to wait for the Lambda function response. The default is 60 seconds.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `900`
> > > > >
> > > > > failureMode -\> (string)
> > > > >
> > > > > > The behavior when the Lambda function times out, returns an error, or returns an invalid response. The default is `DENY` .
> > > > > >
> > > > > > Possible values:
> > > > > >
> > > > > > - `allow`
> > > > > > - `deny`
> > > >
> > > > sns -\> (structure)
> > > >
> > > > > An Amazon SNS hook target that publishes the hook event without waiting for a response.
> > > > >
> > > > > arn -\> (string) \[required\]
> > > > >
> > > > > > The ARN of the Amazon SNS topic to publish hook events to.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `20`
> > > > > > - max: `2048`
> > > > > > - pattern: `arn:aws(-[^:]+)?:sns:[a-z0-9-]+:[0-9]{12}:.+`
> > > >
> > > > eventBridge -\> (structure)
> > > >
> > > > > An Amazon EventBridge hook target that sends the hook event without waiting for a response.
> > > > >
> > > > > arn -\> (string) \[required\]
> > > > >
> > > > > > The ARN of the Amazon EventBridge event bus to send hook events to.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `20`
> > > > > > - max: `2048`
> > > > > > - pattern: `arn:aws(-[^:]+)?:events:[a-z0-9-]+:[0-9]{12}:event-bus/.+`
> >
> > afterInvocation -\> (structure)
> >
> > > A hook that runs after an invocation completes.
> > >
> > > name -\> (string) \[required\]
> > >
> > > > The name of the hook.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `64`
> > > > - pattern: `[a-zA-Z0-9_-]+`
> > >
> > > target -\> (tagged union structure) \[required\]
> > >
> > > > The target that receives the hook event.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `lambda`, `sns`, `eventBridge`.
> > > >
> > > > lambda -\> (structure)
> > > >
> > > > > A Lambda hook target that invokes an AWS Lambda function synchronously and waits for its response.
> > > > >
> > > > > arn -\> (string) \[required\]
> > > > >
> > > > > > The ARN of the Lambda function to invoke.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `20`
> > > > > > - max: `2048`
> > > > > > - pattern: `arn:aws(-[^:]+)?:lambda:[a-z0-9-]+:[0-9]{12}:function:.+`
> > > > >
> > > > > timeoutSeconds -\> (integer)
> > > > >
> > > > > > The maximum number of seconds to wait for the Lambda function response. The default is 60 seconds.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `900`
> > > > >
> > > > > failureMode -\> (string)
> > > > >
> > > > > > The behavior when the Lambda function times out, returns an error, or returns an invalid response. The default is `DENY` .
> > > > > >
> > > > > > Possible values:
> > > > > >
> > > > > > - `allow`
> > > > > > - `deny`
> > > >
> > > > sns -\> (structure)
> > > >
> > > > > An Amazon SNS hook target that publishes the hook event without waiting for a response.
> > > > >
> > > > > arn -\> (string) \[required\]
> > > > >
> > > > > > The ARN of the Amazon SNS topic to publish hook events to.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `20`
> > > > > > - max: `2048`
> > > > > > - pattern: `arn:aws(-[^:]+)?:sns:[a-z0-9-]+:[0-9]{12}:.+`
> > > >
> > > > eventBridge -\> (structure)
> > > >
> > > > > An Amazon EventBridge hook target that sends the hook event without waiting for a response.
> > > > >
> > > > > arn -\> (string) \[required\]
> > > > >
> > > > > > The ARN of the Amazon EventBridge event bus to send hook events to.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `20`
> > > > > > - max: `2048`
> > > > > > - pattern: `arn:aws(-[^:]+)?:events:[a-z0-9-]+:[0-9]{12}:event-bus/.+`
> >
> > beforeToolCall -\> (structure)
> >
> > > A hook that runs before the agent calls a tool.
> > >
> > > name -\> (string) \[required\]
> > >
> > > > The name of the hook.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `64`
> > > > - pattern: `[a-zA-Z0-9_-]+`
> > >
> > > target -\> (tagged union structure) \[required\]
> > >
> > > > The target that receives the hook event.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `lambda`, `sns`, `eventBridge`.
> > > >
> > > > lambda -\> (structure)
> > > >
> > > > > A Lambda hook target that invokes an AWS Lambda function synchronously and waits for its response.
> > > > >
> > > > > arn -\> (string) \[required\]
> > > > >
> > > > > > The ARN of the Lambda function to invoke.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `20`
> > > > > > - max: `2048`
> > > > > > - pattern: `arn:aws(-[^:]+)?:lambda:[a-z0-9-]+:[0-9]{12}:function:.+`
> > > > >
> > > > > timeoutSeconds -\> (integer)
> > > > >
> > > > > > The maximum number of seconds to wait for the Lambda function response. The default is 60 seconds.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `900`
> > > > >
> > > > > failureMode -\> (string)
> > > > >
> > > > > > The behavior when the Lambda function times out, returns an error, or returns an invalid response. The default is `DENY` .
> > > > > >
> > > > > > Possible values:
> > > > > >
> > > > > > - `allow`
> > > > > > - `deny`
> > > >
> > > > sns -\> (structure)
> > > >
> > > > > An Amazon SNS hook target that publishes the hook event without waiting for a response.
> > > > >
> > > > > arn -\> (string) \[required\]
> > > > >
> > > > > > The ARN of the Amazon SNS topic to publish hook events to.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `20`
> > > > > > - max: `2048`
> > > > > > - pattern: `arn:aws(-[^:]+)?:sns:[a-z0-9-]+:[0-9]{12}:.+`
> > > >
> > > > eventBridge -\> (structure)
> > > >
> > > > > An Amazon EventBridge hook target that sends the hook event without waiting for a response.
> > > > >
> > > > > arn -\> (string) \[required\]
> > > > >
> > > > > > The ARN of the Amazon EventBridge event bus to send hook events to.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `20`
> > > > > > - max: `2048`
> > > > > > - pattern: `arn:aws(-[^:]+)?:events:[a-z0-9-]+:[0-9]{12}:event-bus/.+`
> >
> > afterToolCall -\> (structure)
> >
> > > A hook that runs after a tool call completes.
> > >
> > > name -\> (string) \[required\]
> > >
> > > > The name of the hook.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `64`
> > > > - pattern: `[a-zA-Z0-9_-]+`
> > >
> > > target -\> (tagged union structure) \[required\]
> > >
> > > > The target that receives the hook event.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `lambda`, `sns`, `eventBridge`.
> > > >
> > > > lambda -\> (structure)
> > > >
> > > > > A Lambda hook target that invokes an AWS Lambda function synchronously and waits for its response.
> > > > >
> > > > > arn -\> (string) \[required\]
> > > > >
> > > > > > The ARN of the Lambda function to invoke.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `20`
> > > > > > - max: `2048`
> > > > > > - pattern: `arn:aws(-[^:]+)?:lambda:[a-z0-9-]+:[0-9]{12}:function:.+`
> > > > >
> > > > > timeoutSeconds -\> (integer)
> > > > >
> > > > > > The maximum number of seconds to wait for the Lambda function response. The default is 60 seconds.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `900`
> > > > >
> > > > > failureMode -\> (string)
> > > > >
> > > > > > The behavior when the Lambda function times out, returns an error, or returns an invalid response. The default is `DENY` .
> > > > > >
> > > > > > Possible values:
> > > > > >
> > > > > > - `allow`
> > > > > > - `deny`
> > > >
> > > > sns -\> (structure)
> > > >
> > > > > An Amazon SNS hook target that publishes the hook event without waiting for a response.
> > > > >
> > > > > arn -\> (string) \[required\]
> > > > >
> > > > > > The ARN of the Amazon SNS topic to publish hook events to.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `20`
> > > > > > - max: `2048`
> > > > > > - pattern: `arn:aws(-[^:]+)?:sns:[a-z0-9-]+:[0-9]{12}:.+`
> > > >
> > > > eventBridge -\> (structure)
> > > >
> > > > > An Amazon EventBridge hook target that sends the hook event without waiting for a response.
> > > > >
> > > > > arn -\> (string) \[required\]
> > > > >
> > > > > > The ARN of the Amazon EventBridge event bus to send hook events to.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `20`
> > > > > > - max: `2048`
> > > > > > - pattern: `arn:aws(-[^:]+)?:events:[a-z0-9-]+:[0-9]{12}:event-bus/.+`

JSON Syntax:

    [
      {
        "beforeInvocation": {
          "name": "string",
          "target": {
            "lambda": {
              "arn": "string",
              "timeoutSeconds": integer,
              "failureMode": "allow"|"deny"
            },
            "sns": {
              "arn": "string"
            },
            "eventBridge": {
              "arn": "string"
            }
          }
        },
        "afterInvocation": {
          "name": "string",
          "target": {
            "lambda": {
              "arn": "string",
              "timeoutSeconds": integer,
              "failureMode": "allow"|"deny"
            },
            "sns": {
              "arn": "string"
            },
            "eventBridge": {
              "arn": "string"
            }
          }
        },
        "beforeToolCall": {
          "name": "string",
          "target": {
            "lambda": {
              "arn": "string",
              "timeoutSeconds": integer,
              "failureMode": "allow"|"deny"
            },
            "sns": {
              "arn": "string"
            },
            "eventBridge": {
              "arn": "string"
            }
          }
        },
        "afterToolCall": {
          "name": "string",
          "target": {
            "lambda": {
              "arn": "string",
              "timeoutSeconds": integer,
              "failureMode": "allow"|"deny"
            },
            "sns": {
              "arn": "string"
            },
            "eventBridge": {
              "arn": "string"
            }
          }
        }
      }
      ...
    ]

`--max-iterations` (integer)

> The maximum number of iterations the agent loop can execute per invocation. If not specified, the existing value is retained.

`--max-tokens` (integer)

> The maximum total number of output tokens the agent can generate across all model calls within a single invocation. If not specified, the existing value is retained.

`--timeout-seconds` (integer)

> The maximum duration in seconds for the agent loop execution per invocation. If not specified, the existing value is retained.

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

harness -\> (structure)

> The updated harness.
>
> harnessId -\> (string) \[required\]
>
> > The ID of the harness.
> >
> > Constraints:
> >
> > - pattern: `[a-zA-Z][a-zA-Z0-9_]{0,39}-[a-zA-Z0-9]{10}`
>
> harnessName -\> (string) \[required\]
>
> > The name of the harness.
> >
> > Constraints:
> >
> > - pattern: `[a-zA-Z][a-zA-Z0-9_]{0,39}`
>
> arn -\> (string) \[required\]
>
> > The ARN of the harness.
> >
> > Constraints:
> >
> > - pattern: `arn:([^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:harness/[a-zA-Z][a-zA-Z0-9_]{0,39}-[a-zA-Z0-9]{10}`
>
> status -\> (string) \[required\]
>
> > The status of the harness.
> >
> > Possible values:
> >
> > - `CREATING`
> > - `CREATE_FAILED`
> > - `UPDATING`
> > - `UPDATE_FAILED`
> > - `READY`
> > - `DELETING`
> > - `DELETE_FAILED`
>
> harnessVersion -\> (string)
>
> > The version of the harness. Incremented on every successful UpdateHarness.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `5`
> > - pattern: `([1-9][0-9]{0,4})`
>
> executionRoleArn -\> (string) \[required\]
>
> > IAM role the harness assumes when running.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `2048`
> > - pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`
>
> createdAt -\> (timestamp) \[required\]
>
> > The createdAt time of the harness.
>
> updatedAt -\> (timestamp) \[required\]
>
> > The updatedAt time of the harness.
>
> model -\> (tagged union structure) \[required\]
>
> > The configuration of the default model used by the Harness.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `bedrockModelConfig`, `openAiModelConfig`, `geminiModelConfig`, `liteLlmModelConfig`.
> >
> > bedrockModelConfig -\> (structure)
> >
> > > Configuration for an Amazon Bedrock model.
> > >
> > > modelId -\> (string) \[required\]
> > >
> > > > The Bedrock model ID.
> > >
> > > maxTokens -\> (integer)
> > >
> > > > The maximum number of tokens to allow in the generated response per model call.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > >
> > > temperature -\> (float)
> > >
> > > > The temperature to set when calling the model.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0.0`
> > > > - max: `2.0`
> > >
> > > topP -\> (float)
> > >
> > > > The topP set when calling the model.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0.0`
> > > > - max: `1.0`
> > >
> > > apiFormat -\> (string)
> > >
> > > > The API format to use when calling the Bedrock provider.
> > > >
> > > > Possible values:
> > > >
> > > > - `converse_stream`
> > > > - `responses`
> > > > - `chat_completions`
> > >
> > > additionalParams -\> (document)
> > >
> > > > Provider-specific parameters passed through to the model provider unchanged.
> >
> > openAiModelConfig -\> (structure)
> >
> > > Configuration for an OpenAI model.
> > >
> > > modelId -\> (string) \[required\]
> > >
> > > > The OpenAI model ID.
> > >
> > > apiKeyArn -\> (string) \[required\]
> > >
> > > > The ARN of your OpenAI API key on AgentCore Identity.
> > > >
> > > > Constraints:
> > > >
> > > > - pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+`
> > >
> > > apiBase -\> (string)
> > >
> > > > Optional custom endpoint URL for an OpenAI-compatible endpoint.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `16383`
> > >
> > > maxTokens -\> (integer)
> > >
> > > > The maximum number of tokens to allow in the generated response per model call.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > >
> > > temperature -\> (float)
> > >
> > > > The temperature to set when calling the model.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0.0`
> > > > - max: `2.0`
> > >
> > > topP -\> (float)
> > >
> > > > The topP set when calling the model.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0.0`
> > > > - max: `1.0`
> > >
> > > apiFormat -\> (string)
> > >
> > > > The API format to use when calling the OpenAI provider.
> > > >
> > > > Possible values:
> > > >
> > > > - `chat_completions`
> > > > - `responses`
> > >
> > > additionalParams -\> (document)
> > >
> > > > Provider-specific parameters passed through to the model provider unchanged.
> >
> > geminiModelConfig -\> (structure)
> >
> > > Configuration for a Google Gemini model.
> > >
> > > modelId -\> (string) \[required\]
> > >
> > > > The Gemini model ID.
> > >
> > > apiKeyArn -\> (string) \[required\]
> > >
> > > > The ARN of your Gemini API key on AgentCore Identity.
> > > >
> > > > Constraints:
> > > >
> > > > - pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+`
> > >
> > > maxTokens -\> (integer)
> > >
> > > > The maximum number of tokens to allow in the generated response per model call.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > >
> > > temperature -\> (float)
> > >
> > > > The temperature to set when calling the model.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0.0`
> > > > - max: `2.0`
> > >
> > > topP -\> (float)
> > >
> > > > The topP set when calling the model.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0.0`
> > > > - max: `1.0`
> > >
> > > topK -\> (integer)
> > >
> > > > The topK set when calling the model.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0`
> > > > - max: `500`
> > >
> > > additionalParams -\> (document)
> > >
> > > > Provider-specific parameters passed through to the Gemini model provider unchanged.
> >
> > liteLlmModelConfig -\> (structure)
> >
> > > The LiteLLM model configuration for connecting to third-party model providers.
> > >
> > > modelId -\> (string) \[required\]
> > >
> > > > The LiteLLM model identifier (e.g., “anthropic/claude-3-sonnet”).
> > >
> > > apiKeyArn -\> (string)
> > >
> > > > The ARN of the API key in AgentCore Identity for authenticating with the model provider.
> > > >
> > > > Constraints:
> > > >
> > > > - pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+`
> > >
> > > apiBase -\> (string)
> > >
> > > > The base URL for the model provider’s API endpoint.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `16383`
> > >
> > > maxTokens -\> (integer)
> > >
> > > > The maximum number of tokens to allow in the generated response per iteration.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > >
> > > temperature -\> (float)
> > >
> > > > The temperature to set when calling the model.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0.0`
> > > > - max: `2.0`
> > >
> > > topP -\> (float)
> > >
> > > > The topP set when calling the model.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0.0`
> > > > - max: `1.0`
> > >
> > > additionalParams -\> (document)
> > >
> > > > Provider-specific parameters passed through to the model provider unchanged.
>
> systemPrompt -\> (list) \[required\]
>
> > The system prompt of the harness.
> >
> > (tagged union structure)
> >
> > > A content block in the system prompt.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `text`.
> > >
> > > text -\> (string)
> > >
> > > > The text content of the system prompt block.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
>
> tools -\> (list) \[required\]
>
> > The tools of the harness.
> >
> > (structure)
> >
> > > A tool available to the agent loop.
> > >
> > > type -\> (string) \[required\]
> > >
> > > > The type of tool.
> > > >
> > > > Possible values:
> > > >
> > > > - `remote_mcp`
> > > > - `agentcore_browser`
> > > > - `agentcore_gateway`
> > > > - `inline_function`
> > > > - `agentcore_code_interpreter`
> > >
> > > name -\> (string)
> > >
> > > > Unique name for the tool. If not provided, a name will be inferred or generated.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `64`
> > > > - pattern: `[a-zA-Z0-9_-]+`
> > >
> > > config -\> (tagged union structure)
> > >
> > > > Tool-specific configuration.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `remoteMcp`, `agentCoreBrowser`, `agentCoreGateway`, `inlineFunction`, `agentCoreCodeInterpreter`.
> > > >
> > > > remoteMcp -\> (structure)
> > > >
> > > > > Configuration for remote MCP server.
> > > > >
> > > > > url -\> (string) \[required\]
> > > > >
> > > > > > URL of the MCP endpoint.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `16383`
> > > > >
> > > > > headers -\> (map)
> > > > >
> > > > > > Custom headers to include when connecting to the remote MCP server.
> > > > > >
> > > > > > key -\> (string)
> > > > > >
> > > > > > > The key of an HTTP header.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `16383`
> > > > > >
> > > > > > value -\> (string)
> > > > > >
> > > > > > > The value of an HTTP header.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `16383`
> > > >
> > > > agentCoreBrowser -\> (structure)
> > > >
> > > > > Configuration for AgentCore Browser.
> > > > >
> > > > > browserArn -\> (string)
> > > > >
> > > > > > If not populated, the built-in Browser ARN is used.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:(aws|[0-9]{12}):browser(-custom)?/(aws\.browser\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})`
> > > >
> > > > agentCoreGateway -\> (structure)
> > > >
> > > > > Configuration for AgentCore Gateway.
> > > > >
> > > > > gatewayArn -\> (string) \[required\]
> > > > >
> > > > > > The ARN of the desired AgentCore Gateway.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - pattern: `arn:aws(|-cn|-us-gov):bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}`
> > > > >
> > > > > outboundAuth -\> (tagged union structure)
> > > > >
> > > > > > How harness authenticates to this Gateway. Defaults to AWS_IAM (SigV4) if omitted.
> > > > > >
> > > > > > ### Note
> > > > > >
> > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `awsIam`, `none`, `oauth`.
> > > > > >
> > > > > > awsIam -\> (structure)
> > > > > >
> > > > > > > SigV4-sign requests using the agent’s execution role.
> > > > > >
> > > > > > none -\> (structure)
> > > > > >
> > > > > > > No authentication.
> > > > > >
> > > > > > oauth -\> (structure)
> > > > > >
> > > > > > > Use OAuth credentials for outbound authentication to the gateway.
> > > > > > >
> > > > > > > providerArn -\> (string) \[required\]
> > > > > > >
> > > > > > > > The Amazon Resource Name (ARN) of the OAuth credential provider. This ARN identifies the provider in Amazon Web Services.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - pattern: `arn:([^:]*):([^:]*):([^:]*):([0-9]{12})?:(.+)`
> > > > > > >
> > > > > > > scopes -\> (list) \[required\]
> > > > > > >
> > > > > > > > The OAuth scopes for the credential provider. These scopes define the level of access requested from the OAuth provider.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `0`
> > > > > > > > - max: `100`
> > > > > > > >
> > > > > > > > (string)
> > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `64`
> > > > > > >
> > > > > > > customParameters -\> (map)
> > > > > > >
> > > > > > > > The custom parameters for the OAuth credential provider. These parameters provide additional configuration for the OAuth authentication process.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `10`
> > > > > > > >
> > > > > > > > key -\> (string)
> > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `256`
> > > > > > > >
> > > > > > > > value -\> (string)
> > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `2048`
> > > > > > >
> > > > > > > grantType -\> (string)
> > > > > > >
> > > > > > > > Specifies the kind of credentials to use for authorization:
> > > > > > > >
> > > > > > > > - `CLIENT_CREDENTIALS` - Authorization with a client ID and secret.
> > > > > > > > - `AUTHORIZATION_CODE` - Authorization with a token that is specific to an individual end user.
> > > > > > > > - `TOKEN_EXCHANGE` - Authorization using on-behalf-of token exchange. An inbound user token is exchanged for a downstream access token scoped to the target audience.
> > > > > > > >
> > > > > > > > Possible values:
> > > > > > > >
> > > > > > > > - `CLIENT_CREDENTIALS`
> > > > > > > > - `AUTHORIZATION_CODE`
> > > > > > > > - `TOKEN_EXCHANGE`
> > > > > > >
> > > > > > > defaultReturnUrl -\> (string)
> > > > > > >
> > > > > > > > The URL where the end user’s browser is redirected after obtaining the authorization code. Generally points to the customer’s application.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `2048`
> > > > > > > > - pattern: `\w+:(\/?\/?)[^\s]+`
> > > >
> > > > inlineFunction -\> (structure)
> > > >
> > > > > Configuration for an inline function tool.
> > > > >
> > > > > description -\> (string) \[required\]
> > > > >
> > > > > > Description of what the tool does, provided to the model.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `4096`
> > > > >
> > > > > inputSchema -\> (document) \[required\]
> > > > >
> > > > > > JSON Schema describing the tool’s input parameters.
> > > >
> > > > agentCoreCodeInterpreter -\> (structure)
> > > >
> > > > > Configuration for AgentCore Code Interpreter.
> > > > >
> > > > > codeInterpreterArn -\> (string)
> > > > >
> > > > > > If not populated, the built-in Code Interpreter ARN is used.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:(aws|[0-9]{12}):code-interpreter(-custom)?/(aws\.codeinterpreter\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})`
>
> skills -\> (list) \[required\]
>
> > The skills of the harness.
> >
> > (tagged union structure)
> >
> > > A skill available to the agent.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `path`, `s3`, `git`, `awsSkills`.
> > >
> > > path -\> (string)
> > >
> > > > The filesystem path to the skill definition.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `4096`
> > >
> > > s3 -\> (structure)
> > >
> > > > An S3 source containing the skill.
> > > >
> > > > uri -\> (string) \[required\]
> > > >
> > > > > The S3 URI pointing to the skill directory (e.g., s3://bucket/skills/my-skill/).
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `5`
> > > > > - max: `16383`
> > > > > - pattern: `s3://.*`
> > >
> > > git -\> (structure)
> > >
> > > > A git repository containing the skill.
> > > >
> > > > url -\> (string) \[required\]
> > > >
> > > > > The HTTPS URL of the git repository.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `8`
> > > > > - max: `16383`
> > > > > - pattern: `https://[^#@]+`
> > > >
> > > > path -\> (string)
> > > >
> > > > > Subdirectory within the repository containing the skill.
> > > >
> > > > auth -\> (structure)
> > > >
> > > > > Authentication configuration for private repositories.
> > > > >
> > > > > credentialArn -\> (string) \[required\]
> > > > >
> > > > > > The ARN of the credential in AgentCore Identity containing the password or personal access token.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/apikeycredentialprovider/[a-zA-Z0-9-.]+`
> > > > >
> > > > > username -\> (string)
> > > > >
> > > > > > Username for authentication. Defaults to ‘oauth2’ if not specified.
> > >
> > > awsSkills -\> (structure)
> > >
> > > > AWS Skills baked into the harness’s underlying Runtime.
> > > >
> > > > paths -\> (list)
> > > >
> > > > > Optionally filter allowed skills with glob syntax, e.g., \[‘core-skills/[\*](#id3)’\].
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `4096`
> > > > > > - pattern: `([^*?\[\]]|\*)+`
>
> allowedTools -\> (list) \[required\]
>
> > The allowed tools of the harness. All tools are allowed by default.
> >
> > (string)
> >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `64`
> > > - pattern: `(\*|@?[^/]+(/[^/]+)?)`
>
> truncation -\> (structure) \[required\]
>
> > Configuration for truncating model context.
> >
> > strategy -\> (string) \[required\]
> >
> > > The truncation strategy to use.
> > >
> > > Possible values:
> > >
> > > - `sliding_window`
> > > - `summarization`
> > > - `none`
> >
> > config -\> (tagged union structure)
> >
> > > The strategy-specific configuration.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `slidingWindow`, `summarization`.
> > >
> > > slidingWindow -\> (structure)
> > >
> > > > Configuration for sliding window truncation.
> > > >
> > > > messagesCount -\> (integer)
> > > >
> > > > > The number of recent messages to retain in the context window.
> > >
> > > summarization -\> (structure)
> > >
> > > > Configuration for summarization-based truncation.
> > > >
> > > > summaryRatio -\> (float)
> > > >
> > > > > The ratio of content to summarize.
> > > >
> > > > preserveRecentMessages -\> (integer)
> > > >
> > > > > The number of recent messages to preserve without summarization.
> > > >
> > > > summarizationSystemPrompt -\> (string)
> > > >
> > > > > The system prompt used for generating summaries.
>
> environment -\> (tagged union structure) \[required\]
>
> > The compute environment on which the Harness runs.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `agentCoreRuntimeEnvironment`.
> >
> > agentCoreRuntimeEnvironment -\> (structure)
> >
> > > The AgentCore Runtime environment configuration.
> > >
> > > agentRuntimeArn -\> (string) \[required\]
> > >
> > > > The ARN of the underlying AgentCore Runtime.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `20`
> > > > - max: `1011`
> > >
> > > agentRuntimeName -\> (string) \[required\]
> > >
> > > > The name of the underlying AgentCore Runtime.
> > >
> > > agentRuntimeId -\> (string) \[required\]
> > >
> > > > The ID of the underlying AgentCore Runtime.
> > >
> > > lifecycleConfiguration -\> (structure) \[required\]
> > >
> > > > LifecycleConfiguration lets you manage the lifecycle of runtime sessions and resources in AgentCore Runtime. This configuration helps optimize resource utilization by automatically cleaning up idle sessions and preventing long-running instances from consuming resources indefinitely.
> > > >
> > > > idleRuntimeSessionTimeout -\> (integer)
> > > >
> > > > > Timeout in seconds for idle runtime sessions. When a session remains idle for this duration, it will be automatically terminated. Default: 900 seconds (15 minutes).
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `60`
> > > > > - max: `1209600`
> > > >
> > > > maxLifetime -\> (integer)
> > > >
> > > > > Maximum lifetime for the instance in seconds. Once reached, instances will be automatically terminated and replaced. Default: 28800 seconds (8 hours).
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `60`
> > > > > - max: `1209600`
> > >
> > > networkConfiguration -\> (structure) \[required\]
> > >
> > > > SecurityConfig for the Agent.
> > > >
> > > > networkMode -\> (string) \[required\]
> > > >
> > > > > The network mode for the AgentCore Runtime.
> > > > >
> > > > > Possible values:
> > > > >
> > > > > - `PUBLIC`
> > > > > - `VPC`
> > > >
> > > > networkModeConfig -\> (structure)
> > > >
> > > > > The network mode configuration for the AgentCore Runtime.
> > > > >
> > > > > securityGroups -\> (list) \[required\]
> > > > >
> > > > > > The security groups associated with the VPC configuration.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `16`
> > > > > >
> > > > > > (string)
> > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - pattern: `sg-[0-9a-zA-Z]{8,17}`
> > > > >
> > > > > subnets -\> (list) \[required\]
> > > > >
> > > > > > The subnets associated with the VPC configuration.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `16`
> > > > > >
> > > > > > (string)
> > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - pattern: `subnet-[0-9a-zA-Z]{8,17}`
> > > > >
> > > > > requireServiceS3Endpoint -\> (boolean)
> > > > >
> > > > > > ### Note
> > > > > >
> > > > > > This field applies only to Agent Runtimes. It is not applicable to Browsers or Code Interpreters.
> > > > > >
> > > > > > Controls whether a service-managed Amazon S3 gateway endpoint is provisioned in the VPC network topology for the agent runtime. This gateway is used by Amazon Bedrock AgentCore Runtime to download code and container images during agent startup.
> > > > > >
> > > > > > Starting May 5, 2026, Amazon Bedrock AgentCore Runtime is gradually rolling out a change to how network isolation is configured for VPC mode agents. Agent runtimes created on or after this rollout will no longer include the service-managed Amazon S3 gateway. Instead, all network access, including to Amazon S3, is governed exclusively by your VPC configuration. This field cannot be set on agent runtimes created after the rollout. Passing this field in an `UpdateAgentRuntime` request for these agent runtimes returns a `ValidationException` .
> > > > > >
> > > > > > Agent runtimes created before the rollout are not affected and continue to operate with the service-managed Amazon S3 gateway. To enforce full VPC network isolation on these existing agent runtimes, set this field to `false` via the `UpdateAgentRuntime` API. Before opting out, ensure your VPC provides the Amazon S3 access required for agent startup. If this field is not specified or is set to `true` , the service-managed Amazon S3 gateway remains provisioned.
> > > > > >
> > > > > > This field is only supported in the `UpdateAgentRuntime` API for pre-rollout agent runtimes. Passing this field in a `CreateAgentRuntime` request returns a `ValidationException` .
> > >
> > > filesystemConfigurations -\> (list)
> > >
> > > > The filesystem configurations for the runtime environment.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0`
> > > > - max: `5`
> > > >
> > > > (tagged union structure)
> > > >
> > > > > Configuration for a filesystem that can be mounted into the AgentCore Runtime.
> > > > >
> > > > > ### Note
> > > > >
> > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `sessionStorage`, `s3FilesAccessPoint`, `efsAccessPoint`, `capacityProviderVolume`.
> > > > >
> > > > > sessionStorage -\> (structure)
> > > > >
> > > > > > Configuration for session storage. Session storage provides persistent storage that is preserved across AgentCore Runtime session invocations.
> > > > > >
> > > > > > mountPath -\> (string) \[required\]
> > > > > >
> > > > > > > The mount path for the session storage filesystem inside the AgentCore Runtime. The path must be under `/mnt` with exactly one subdirectory level (for example, `/mnt/data` ).
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `6`
> > > > > > > - max: `200`
> > > > > > > - pattern: `/mnt/[a-zA-Z0-9._-]+/?`
> > > > >
> > > > > s3FilesAccessPoint -\> (structure)
> > > > >
> > > > > > Configuration for an Amazon S3 Files access point to mount into the AgentCore Runtime.
> > > > > >
> > > > > > accessPointArn -\> (string) \[required\]
> > > > > >
> > > > > > > The ARN of the S3 Files access point to mount into the AgentCore Runtime.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `0`
> > > > > > > - max: `256`
> > > > > > > - pattern: `arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}/access-point/fsap-[0-9a-f]{17,40}`
> > > > > >
> > > > > > mountPath -\> (string) \[required\]
> > > > > >
> > > > > > > The mount path for the S3 Files access point inside the AgentCore Runtime. The path must be under `/mnt` with exactly one subdirectory level (for example, `/mnt/data` ).
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `6`
> > > > > > > - max: `200`
> > > > > > > - pattern: `/mnt/[a-zA-Z0-9._-]+/?`
> > > > >
> > > > > efsAccessPoint -\> (structure)
> > > > >
> > > > > > Configuration for an Amazon EFS access point to mount into the AgentCore Runtime.
> > > > > >
> > > > > > accessPointArn -\> (string) \[required\]
> > > > > >
> > > > > > > The ARN of the EFS access point to mount into the AgentCore Runtime.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `0`
> > > > > > > - max: `128`
> > > > > > > - pattern: `arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:access-point/fsap-[0-9a-f]{8,40}`
> > > > > >
> > > > > > mountPath -\> (string) \[required\]
> > > > > >
> > > > > > > The mount path for the EFS access point inside the AgentCore Runtime. The path must be under `/mnt` with exactly one subdirectory level (for example, `/mnt/data` ).
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `6`
> > > > > > > - max: `200`
> > > > > > > - pattern: `/mnt/[a-zA-Z0-9._-]+/?`
> > > > >
> > > > > capacityProviderVolume -\> (structure)
> > > > >
> > > > > > Configuration for a capacity provider volume to mount into the AgentCore Runtime. This mounts a persistent volume that is defined on the capacity provider, referenced by its logical name.
> > > > > >
> > > > > > volumeName -\> (string) \[required\]
> > > > > >
> > > > > > > The logical name of the capacity provider volume to mount. This name must match a volume that is defined in the capacity provider’s list of volumes.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `48`
> > > > > > > - pattern: `[a-zA-Z][a-zA-Z0-9_-]{0,47}`
> > > > > >
> > > > > > mountPath -\> (string) \[required\]
> > > > > >
> > > > > > > The mount path for the capacity provider volume inside the AgentCore Runtime. The path must be under `/mnt` with exactly one subdirectory level (for example, `/mnt/data` ).
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `6`
> > > > > > > - max: `200`
> > > > > > > - pattern: `/mnt/[a-zA-Z0-9._-]+/?`
>
> environmentArtifact -\> (tagged union structure)
>
> > The environment artifact (e.g., container) in which the Harness operates.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `containerConfiguration`.
> >
> > containerConfiguration -\> (structure)
> >
> > > Representation of a container configuration.
> > >
> > > containerUri -\> (string) \[required\]
> > >
> > > > The ECR URI of the container.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `1024`
> > > > - pattern: `(([0-9]{12})\.dkr\.ecr\.([a-z0-9-]+)\.amazonaws\.com(\.cn)?|public\.ecr\.aws)/((?:[a-z0-9]+(?:[._-][a-z0-9]+)*/)*[a-z0-9]+(?:[._-][a-z0-9]+)*)(?::([^:@]{1,300}))?(?:@(.+))?`
>
> environmentVariables -\> (map)
>
> > Environment variables exposed in the environment in which the harness operates.
> >
> > Constraints:
> >
> > - min: `0`
> > - max: `50`
> >
> > key -\> (string)
> >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `100`
> >
> > value -\> (string)
> >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `5000`
>
> authorizerConfiguration -\> (tagged union structure)
>
> > Represents inbound authorization configuration options used to authenticate incoming requests.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `customJWTAuthorizer`.
> >
> > customJWTAuthorizer -\> (structure)
> >
> > > The inbound JWT-based authorization, specifying how incoming requests should be authenticated.
> > >
> > > discoveryUrl -\> (string) \[required\]
> > >
> > > > This URL is used to fetch OpenID Connect configuration or authorization server metadata for validating incoming tokens.
> > > >
> > > > Constraints:
> > > >
> > > > - pattern: `.+/\.well-known/openid-configuration`
> > >
> > > allowedAudience -\> (list)
> > >
> > > > Represents individual audience values that are validated in the incoming JWT token validation process.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > >
> > > > (string)
> > >
> > > allowedClients -\> (list)
> > >
> > > > Represents individual client IDs that are validated in the incoming JWT token validation process.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > >
> > > > (string)
> > >
> > > allowedScopes -\> (list)
> > >
> > > > An array of scopes that are allowed to access the token.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > >
> > > > (string)
> > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `255`
> > > > > - pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
> > >
> > > advertisedScopeMapping -\> (map)
> > >
> > > > A map that associates each scope in `allowedScopes` with a corresponding advertised scope value. The advertised scope appears in OAuth protected resource metadata and `WWW-Authenticate` response headers. Use this parameter when the scope that clients request from your identity provider differs from the scope in the validated token. Each key is a scope from `allowedScopes` that the service uses for token validation. Each value is the corresponding scope that the service advertises to clients. Scopes without a mapping entry appear unchanged to clients.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `50`
> > > >
> > > > key -\> (string)
> > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `255`
> > > > > - pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
> > > >
> > > > value -\> (string)
> > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `255`
> > > > > - pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
> > >
> > > customClaims -\> (list)
> > >
> > > > An array of objects that define a custom claim validation name, value, and operation
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > >
> > > > (structure)
> > > >
> > > > > Defines the name of a custom claim field and rules for finding matches to authenticate its value.
> > > > >
> > > > > inboundTokenClaimName -\> (string) \[required\]
> > > > >
> > > > > > The name of the custom claim field to check.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `255`
> > > > > > - pattern: `[A-Za-z0-9_.-:]+`
> > > > >
> > > > > inboundTokenClaimValueType -\> (string) \[required\]
> > > > >
> > > > > > The data type of the claim value to check for.
> > > > > >
> > > > > > - Use `STRING` if you want to find an exact match to a string you define.
> > > > > > - Use `STRING_ARRAY` if you want to fnd a match to at least one value in an array you define.
> > > > > >
> > > > > > Possible values:
> > > > > >
> > > > > > - `STRING`
> > > > > > - `STRING_ARRAY`
> > > > >
> > > > > authorizingClaimMatchValue -\> (structure) \[required\]
> > > > >
> > > > > > Defines the value or values to match for and the relationship of the match.
> > > > > >
> > > > > > claimMatchValue -\> (tagged union structure) \[required\]
> > > > > >
> > > > > > > The value or values to match for.
> > > > > > >
> > > > > > > ### Note
> > > > > > >
> > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `matchValueString`, `matchValueStringList`.
> > > > > > >
> > > > > > > matchValueString -\> (string)
> > > > > > >
> > > > > > > > The string value to match for.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > > > > - pattern: `[A-Za-z0-9_.-]+`
> > > > > > >
> > > > > > > matchValueStringList -\> (list)
> > > > > > >
> > > > > > > > An array of strings to check for a match.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > >
> > > > > > > > (string)
> > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `255`
> > > > > > > > > - pattern: `[A-Za-z0-9_.-]+`
> > > > > >
> > > > > > claimMatchOperator -\> (string) \[required\]
> > > > > >
> > > > > > > Defines the relationship between the claim field value and the value or values you’re matching for.
> > > > > > >
> > > > > > > Possible values:
> > > > > > >
> > > > > > > - `EQUALS`
> > > > > > > - `CONTAINS`
> > > > > > > - `CONTAINS_ANY`
> > >
> > > privateEndpoint -\> (tagged union structure)
> > >
> > > > The private endpoint configuration for a gateway target. Defines how the gateway connects to private resources in your VPC.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `selfManagedLatticeResource`, `managedVpcResource`.
> > > >
> > > > selfManagedLatticeResource -\> (tagged union structure)
> > > >
> > > > > Configuration for connecting to a private resource using a self-managed VPC Lattice resource configuration.
> > > > >
> > > > > ### Note
> > > > >
> > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `resourceConfigurationIdentifier`.
> > > > >
> > > > > resourceConfigurationIdentifier -\> (string)
> > > > >
> > > > > > The ARN or ID of the VPC Lattice resource configuration.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `20`
> > > > > > - max: `2048`
> > > > > > - pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`
> > > >
> > > > managedVpcResource -\> (structure)
> > > >
> > > > > Configuration for connecting to a private resource using a managed VPC Lattice resource. The gateway creates and manages the VPC Lattice resources on your behalf.
> > > > >
> > > > > vpcIdentifier -\> (string) \[required\]
> > > > >
> > > > > > The ID of the VPC that contains your private resource.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > >
> > > > > subnetIds -\> (list) \[required\]
> > > > >
> > > > > > The subnet IDs within the VPC where the VPC Lattice resource gateway is placed.
> > > > > >
> > > > > > (string)
> > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - pattern: `subnet-[0-9a-zA-Z]{8,17}`
> > > > >
> > > > > endpointIpAddressType -\> (string) \[required\]
> > > > >
> > > > > > The IP address type for the resource configuration endpoint.
> > > > > >
> > > > > > Possible values:
> > > > > >
> > > > > > - `IPV4`
> > > > > > - `IPV6`
> > > > >
> > > > > securityGroupIds -\> (list)
> > > > >
> > > > > > The security group IDs to associate with the VPC Lattice resource gateway. If not specified, the default security group for the VPC is used.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `0`
> > > > > > - max: `5`
> > > > > >
> > > > > > (string)
> > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > >
> > > > > tags -\> (map)
> > > > >
> > > > > > Tags to apply to the managed VPC Lattice resource gateway.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `0`
> > > > > > - max: `50`
> > > > > >
> > > > > > key -\> (string)
> > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `128`
> > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > >
> > > > > > value -\> (string)
> > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `0`
> > > > > > > - max: `256`
> > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > >
> > > > > routingDomain -\> (string)
> > > > >
> > > > > > An intermediate domain to use as the resource configuration endpoint instead of the actual target domain. Use this when you want to route traffic through an intermediate component such as a VPC endpoint or internal load balancer. For more information, see xref:lattice-vpc-egress-routing-domain\[Route traffic through an intermediate domain\].
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `3`
> > > > > > - max: `255`
> > >
> > > privateEndpointOverrides -\> (list)
> > >
> > > > The private endpoint overrides for the custom JWT authorizer configuration.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0`
> > > > - max: `5`
> > > >
> > > > (structure)
> > > >
> > > > > A mapping of a specific domain to a private endpoint for secure connectivity through a VPC Lattice resource configuration.
> > > > >
> > > > > domain -\> (string) \[required\]
> > > > >
> > > > > > The domain to override with a private endpoint.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `253`
> > > > >
> > > > > privateEndpoint -\> (tagged union structure) \[required\]
> > > > >
> > > > > > The private endpoint configuration for the specified domain.
> > > > > >
> > > > > > ### Note
> > > > > >
> > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `selfManagedLatticeResource`, `managedVpcResource`.
> > > > > >
> > > > > > selfManagedLatticeResource -\> (tagged union structure)
> > > > > >
> > > > > > > Configuration for connecting to a private resource using a self-managed VPC Lattice resource configuration.
> > > > > > >
> > > > > > > ### Note
> > > > > > >
> > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `resourceConfigurationIdentifier`.
> > > > > > >
> > > > > > > resourceConfigurationIdentifier -\> (string)
> > > > > > >
> > > > > > > > The ARN or ID of the VPC Lattice resource configuration.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `20`
> > > > > > > > - max: `2048`
> > > > > > > > - pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`
> > > > > >
> > > > > > managedVpcResource -\> (structure)
> > > > > >
> > > > > > > Configuration for connecting to a private resource using a managed VPC Lattice resource. The gateway creates and manages the VPC Lattice resources on your behalf.
> > > > > > >
> > > > > > > vpcIdentifier -\> (string) \[required\]
> > > > > > >
> > > > > > > > The ID of the VPC that contains your private resource.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > > >
> > > > > > > subnetIds -\> (list) \[required\]
> > > > > > >
> > > > > > > > The subnet IDs within the VPC where the VPC Lattice resource gateway is placed.
> > > > > > > >
> > > > > > > > (string)
> > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - pattern: `subnet-[0-9a-zA-Z]{8,17}`
> > > > > > >
> > > > > > > endpointIpAddressType -\> (string) \[required\]
> > > > > > >
> > > > > > > > The IP address type for the resource configuration endpoint.
> > > > > > > >
> > > > > > > > Possible values:
> > > > > > > >
> > > > > > > > - `IPV4`
> > > > > > > > - `IPV6`
> > > > > > >
> > > > > > > securityGroupIds -\> (list)
> > > > > > >
> > > > > > > > The security group IDs to associate with the VPC Lattice resource gateway. If not specified, the default security group for the VPC is used.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `0`
> > > > > > > > - max: `5`
> > > > > > > >
> > > > > > > > (string)
> > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > > >
> > > > > > > tags -\> (map)
> > > > > > >
> > > > > > > > Tags to apply to the managed VPC Lattice resource gateway.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `0`
> > > > > > > > - max: `50`
> > > > > > > >
> > > > > > > > key -\> (string)
> > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `128`
> > > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > > > >
> > > > > > > > value -\> (string)
> > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `0`
> > > > > > > > > - max: `256`
> > > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > > >
> > > > > > > routingDomain -\> (string)
> > > > > > >
> > > > > > > > An intermediate domain to use as the resource configuration endpoint instead of the actual target domain. Use this when you want to route traffic through an intermediate component such as a VPC endpoint or internal load balancer. For more information, see xref:lattice-vpc-egress-routing-domain\[Route traffic through an intermediate domain\].
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `3`
> > > > > > > > - max: `255`
> > >
> > > allowedWorkloadConfiguration -\> (structure)
> > >
> > > > The configuration that restricts which workloads in the request’s identity chain are allowed to invoke the target, identified by their hosting environments and workload identities. At launch, this is supported only for AgentCore Runtime targets, and the allowed workloads are AgentCore Gateways.
> > > >
> > > > hostingEnvironments -\> (list)
> > > >
> > > > > The list of hosting environments whose workloads are allowed to invoke the target. At launch, the only supported hosting environment is AgentCore Gateway.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `10`
> > > > >
> > > > > (structure)
> > > > >
> > > > > > A hosting environment whose workloads are allowed to invoke the target. At launch, the only supported hosting environment is AgentCore Gateway.
> > > > > >
> > > > > > arn -\> (string) \[required\]
> > > > > >
> > > > > > > The Amazon Resource Name (ARN) of the hosting environment.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `20`
> > > > > > > - max: `1011`
> > > >
> > > > workloadIdentities -\> (list)
> > > >
> > > > > The list of workload identities that are allowed to invoke the target.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `10`
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `3`
> > > > > > - max: `255`
> > > > > > - pattern: `[A-Za-z0-9_.-]+`
>
> memory -\> (tagged union structure)
>
> > AgentCore Memory instance configuration for short and long term memory.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `agentCoreMemoryConfiguration`, `managedMemoryConfiguration`, `disabled`.
> >
> > agentCoreMemoryConfiguration -\> (structure)
> >
> > > The AgentCore Memory configuration.
> > >
> > > arn -\> (string) \[required\]
> > >
> > > > The ARN of the AgentCore Memory resource.
> > > >
> > > > Constraints:
> > > >
> > > > - pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
> > >
> > > actorId -\> (string)
> > >
> > > > The actor ID for memory operations.
> > >
> > > messagesCount -\> (integer)
> > >
> > > > The number of messages to retrieve from memory.
> > >
> > > retrievalConfig -\> (map)
> > >
> > > > The retrieval configuration for long-term memory, mapping namespace path templates to retrieval settings.
> > > >
> > > > key -\> (string)
> > > >
> > > > value -\> (structure)
> > > >
> > > > > Configuration for memory retrieval within a namespace.
> > > > >
> > > > > topK -\> (integer)
> > > > >
> > > > > > The maximum number of memory entries to retrieve.
> > > > >
> > > > > relevanceScore -\> (float)
> > > > >
> > > > > > The minimum relevance score for retrieved memories.
> > > > >
> > > > > strategyId -\> (string)
> > > > >
> > > > > > The ID of the retrieval strategy to use.
> >
> > managedMemoryConfiguration -\> (structure)
> >
> > > Harness creates and manages a memory resource in the customer’s account.
> > >
> > > arn -\> (string)
> > >
> > > > The ARN of the managed AgentCore Memory resource. Read-only on Get, ignored on Create/Update input.
> > > >
> > > > Constraints:
> > > >
> > > > - pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`
> > >
> > > strategies -\> (list)
> > >
> > > > Strategy types to enable. Defaults to \[SEMANTIC, SUMMARIZATION\].
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `4`
> > > >
> > > > (string)
> > > >
> > > > > Possible values:
> > > > >
> > > > > - `SEMANTIC`
> > > > > - `SUMMARIZATION`
> > > > > - `USER_PREFERENCE`
> > > > > - `EPISODIC`
> > >
> > > eventExpiryDuration -\> (integer)
> > >
> > > > Event retention in days. Defaults to 30.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `3`
> > > > - max: `365`
> > >
> > > encryptionKeyArn -\> (string)
> > >
> > > > Customer-managed KMS key. Defaults to AWS-owned key. Not updatable after creation.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `2048`
> > > > - pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`
> >
> > disabled -\> (structure)
> >
> > > Explicitly opt out of memory.
>
> hooks -\> (list)
>
> > The lifecycle hooks configured for the harness.
> >
> > Constraints:
> >
> > - min: `0`
> > - max: `20`
> >
> > (tagged union structure)
> >
> > > A lifecycle hook configuration. Specify one hook type.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `beforeInvocation`, `afterInvocation`, `beforeToolCall`, `afterToolCall`.
> > >
> > > beforeInvocation -\> (structure)
> > >
> > > > A hook that runs before an invocation begins.
> > > >
> > > > name -\> (string) \[required\]
> > > >
> > > > > The name of the hook.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `64`
> > > > > - pattern: `[a-zA-Z0-9_-]+`
> > > >
> > > > target -\> (tagged union structure) \[required\]
> > > >
> > > > > The target that receives the hook event.
> > > > >
> > > > > ### Note
> > > > >
> > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `lambda`, `sns`, `eventBridge`.
> > > > >
> > > > > lambda -\> (structure)
> > > > >
> > > > > > A Lambda hook target that invokes an AWS Lambda function synchronously and waits for its response.
> > > > > >
> > > > > > arn -\> (string) \[required\]
> > > > > >
> > > > > > > The ARN of the Lambda function to invoke.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `20`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `arn:aws(-[^:]+)?:lambda:[a-z0-9-]+:[0-9]{12}:function:.+`
> > > > > >
> > > > > > timeoutSeconds -\> (integer)
> > > > > >
> > > > > > > The maximum number of seconds to wait for the Lambda function response. The default is 60 seconds.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `900`
> > > > > >
> > > > > > failureMode -\> (string)
> > > > > >
> > > > > > > The behavior when the Lambda function times out, returns an error, or returns an invalid response. The default is `DENY` .
> > > > > > >
> > > > > > > Possible values:
> > > > > > >
> > > > > > > - `allow`
> > > > > > > - `deny`
> > > > >
> > > > > sns -\> (structure)
> > > > >
> > > > > > An Amazon SNS hook target that publishes the hook event without waiting for a response.
> > > > > >
> > > > > > arn -\> (string) \[required\]
> > > > > >
> > > > > > > The ARN of the Amazon SNS topic to publish hook events to.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `20`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `arn:aws(-[^:]+)?:sns:[a-z0-9-]+:[0-9]{12}:.+`
> > > > >
> > > > > eventBridge -\> (structure)
> > > > >
> > > > > > An Amazon EventBridge hook target that sends the hook event without waiting for a response.
> > > > > >
> > > > > > arn -\> (string) \[required\]
> > > > > >
> > > > > > > The ARN of the Amazon EventBridge event bus to send hook events to.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `20`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `arn:aws(-[^:]+)?:events:[a-z0-9-]+:[0-9]{12}:event-bus/.+`
> > >
> > > afterInvocation -\> (structure)
> > >
> > > > A hook that runs after an invocation completes.
> > > >
> > > > name -\> (string) \[required\]
> > > >
> > > > > The name of the hook.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `64`
> > > > > - pattern: `[a-zA-Z0-9_-]+`
> > > >
> > > > target -\> (tagged union structure) \[required\]
> > > >
> > > > > The target that receives the hook event.
> > > > >
> > > > > ### Note
> > > > >
> > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `lambda`, `sns`, `eventBridge`.
> > > > >
> > > > > lambda -\> (structure)
> > > > >
> > > > > > A Lambda hook target that invokes an AWS Lambda function synchronously and waits for its response.
> > > > > >
> > > > > > arn -\> (string) \[required\]
> > > > > >
> > > > > > > The ARN of the Lambda function to invoke.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `20`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `arn:aws(-[^:]+)?:lambda:[a-z0-9-]+:[0-9]{12}:function:.+`
> > > > > >
> > > > > > timeoutSeconds -\> (integer)
> > > > > >
> > > > > > > The maximum number of seconds to wait for the Lambda function response. The default is 60 seconds.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `900`
> > > > > >
> > > > > > failureMode -\> (string)
> > > > > >
> > > > > > > The behavior when the Lambda function times out, returns an error, or returns an invalid response. The default is `DENY` .
> > > > > > >
> > > > > > > Possible values:
> > > > > > >
> > > > > > > - `allow`
> > > > > > > - `deny`
> > > > >
> > > > > sns -\> (structure)
> > > > >
> > > > > > An Amazon SNS hook target that publishes the hook event without waiting for a response.
> > > > > >
> > > > > > arn -\> (string) \[required\]
> > > > > >
> > > > > > > The ARN of the Amazon SNS topic to publish hook events to.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `20`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `arn:aws(-[^:]+)?:sns:[a-z0-9-]+:[0-9]{12}:.+`
> > > > >
> > > > > eventBridge -\> (structure)
> > > > >
> > > > > > An Amazon EventBridge hook target that sends the hook event without waiting for a response.
> > > > > >
> > > > > > arn -\> (string) \[required\]
> > > > > >
> > > > > > > The ARN of the Amazon EventBridge event bus to send hook events to.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `20`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `arn:aws(-[^:]+)?:events:[a-z0-9-]+:[0-9]{12}:event-bus/.+`
> > >
> > > beforeToolCall -\> (structure)
> > >
> > > > A hook that runs before the agent calls a tool.
> > > >
> > > > name -\> (string) \[required\]
> > > >
> > > > > The name of the hook.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `64`
> > > > > - pattern: `[a-zA-Z0-9_-]+`
> > > >
> > > > target -\> (tagged union structure) \[required\]
> > > >
> > > > > The target that receives the hook event.
> > > > >
> > > > > ### Note
> > > > >
> > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `lambda`, `sns`, `eventBridge`.
> > > > >
> > > > > lambda -\> (structure)
> > > > >
> > > > > > A Lambda hook target that invokes an AWS Lambda function synchronously and waits for its response.
> > > > > >
> > > > > > arn -\> (string) \[required\]
> > > > > >
> > > > > > > The ARN of the Lambda function to invoke.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `20`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `arn:aws(-[^:]+)?:lambda:[a-z0-9-]+:[0-9]{12}:function:.+`
> > > > > >
> > > > > > timeoutSeconds -\> (integer)
> > > > > >
> > > > > > > The maximum number of seconds to wait for the Lambda function response. The default is 60 seconds.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `900`
> > > > > >
> > > > > > failureMode -\> (string)
> > > > > >
> > > > > > > The behavior when the Lambda function times out, returns an error, or returns an invalid response. The default is `DENY` .
> > > > > > >
> > > > > > > Possible values:
> > > > > > >
> > > > > > > - `allow`
> > > > > > > - `deny`
> > > > >
> > > > > sns -\> (structure)
> > > > >
> > > > > > An Amazon SNS hook target that publishes the hook event without waiting for a response.
> > > > > >
> > > > > > arn -\> (string) \[required\]
> > > > > >
> > > > > > > The ARN of the Amazon SNS topic to publish hook events to.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `20`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `arn:aws(-[^:]+)?:sns:[a-z0-9-]+:[0-9]{12}:.+`
> > > > >
> > > > > eventBridge -\> (structure)
> > > > >
> > > > > > An Amazon EventBridge hook target that sends the hook event without waiting for a response.
> > > > > >
> > > > > > arn -\> (string) \[required\]
> > > > > >
> > > > > > > The ARN of the Amazon EventBridge event bus to send hook events to.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `20`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `arn:aws(-[^:]+)?:events:[a-z0-9-]+:[0-9]{12}:event-bus/.+`
> > >
> > > afterToolCall -\> (structure)
> > >
> > > > A hook that runs after a tool call completes.
> > > >
> > > > name -\> (string) \[required\]
> > > >
> > > > > The name of the hook.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `64`
> > > > > - pattern: `[a-zA-Z0-9_-]+`
> > > >
> > > > target -\> (tagged union structure) \[required\]
> > > >
> > > > > The target that receives the hook event.
> > > > >
> > > > > ### Note
> > > > >
> > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `lambda`, `sns`, `eventBridge`.
> > > > >
> > > > > lambda -\> (structure)
> > > > >
> > > > > > A Lambda hook target that invokes an AWS Lambda function synchronously and waits for its response.
> > > > > >
> > > > > > arn -\> (string) \[required\]
> > > > > >
> > > > > > > The ARN of the Lambda function to invoke.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `20`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `arn:aws(-[^:]+)?:lambda:[a-z0-9-]+:[0-9]{12}:function:.+`
> > > > > >
> > > > > > timeoutSeconds -\> (integer)
> > > > > >
> > > > > > > The maximum number of seconds to wait for the Lambda function response. The default is 60 seconds.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `900`
> > > > > >
> > > > > > failureMode -\> (string)
> > > > > >
> > > > > > > The behavior when the Lambda function times out, returns an error, or returns an invalid response. The default is `DENY` .
> > > > > > >
> > > > > > > Possible values:
> > > > > > >
> > > > > > > - `allow`
> > > > > > > - `deny`
> > > > >
> > > > > sns -\> (structure)
> > > > >
> > > > > > An Amazon SNS hook target that publishes the hook event without waiting for a response.
> > > > > >
> > > > > > arn -\> (string) \[required\]
> > > > > >
> > > > > > > The ARN of the Amazon SNS topic to publish hook events to.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `20`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `arn:aws(-[^:]+)?:sns:[a-z0-9-]+:[0-9]{12}:.+`
> > > > >
> > > > > eventBridge -\> (structure)
> > > > >
> > > > > > An Amazon EventBridge hook target that sends the hook event without waiting for a response.
> > > > > >
> > > > > > arn -\> (string) \[required\]
> > > > > >
> > > > > > > The ARN of the Amazon EventBridge event bus to send hook events to.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `20`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `arn:aws(-[^:]+)?:events:[a-z0-9-]+:[0-9]{12}:event-bus/.+`
>
> maxIterations -\> (integer)
>
> > The maximum number of iterations in the agent loop allowed before exiting per invocation.
>
> maxTokens -\> (integer)
>
> > The maximum total number of output tokens the agent can generate across all model calls within a single invocation.
>
> timeoutSeconds -\> (integer)
>
> > The maximum duration per invocation.
>
> failureReason -\> (string)
>
> > Reason why create or update operations fail.

- [← update-gateway-target](update-gateway-target.html "previous chapter (use the left arrow)") /
- [update-harness-endpoint →](update-harness-endpoint.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](update-harness-endpoint.html "update-harness-endpoint") \|
- [previous](update-gateway-target.html "update-gateway-target") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [update-harness]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

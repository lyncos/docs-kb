---
title: aws bedrock-agentcore-control get-payment-manager
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/get-payment-manager.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# get-payment-manager

## Description

Retrieves information about a specific payment manager.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/GetPaymentManager)

## Synopsis

      get-payment-manager
    --payment-manager-id <value>
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

`--payment-manager-id` (string) \[required\]

> The unique identifier of the payment manager to retrieve.
>
> Constraints:
>
> - min: `12`
> - max: `211`
> - pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`

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

paymentManagerArn -\> (string)

> The Amazon Resource Name (ARN) of the payment manager.
>
> Constraints:
>
> - min: `66`
> - max: `2048`
> - pattern: `arn:(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:payment-manager/([0-9a-z][-]?){1,48}-[a-z0-9]{10}`

paymentManagerId -\> (string)

> The unique identifier of the payment manager.
>
> Constraints:
>
> - min: `12`
> - max: `211`
> - pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}`

name -\> (string)

> The name of the payment manager.
>
> Constraints:
>
> - min: `1`
> - max: `48`
> - pattern: `[a-zA-Z][a-zA-Z0-9]{0,47}`

description -\> (string)

> The description of the payment manager.
>
> Constraints:
>
> - min: `1`
> - max: `4096`
> - pattern: `[^\p{C}]*`

authorizerType -\> (string)

> The type of authorizer used by the payment manager.
>
> - `CUSTOM_JWT` - Authorize with a bearer token.
> - `AWS_IAM` - Authorize with your Amazon Web Services IAM credentials.
>
> Possible values:
>
> - `CUSTOM_JWT`
> - `AWS_IAM`

authorizerConfiguration -\> (tagged union structure)

> Represents inbound authorization configuration options used to authenticate incoming requests.
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

roleArn -\> (string)

> The Amazon Resource Name (ARN) of the IAM role associated with the payment manager.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`

workloadIdentityDetails -\> (structure)

> The information about the workload identity.
>
> workloadIdentityArn -\> (string) \[required\]
>
> > The ARN associated with the workload identity.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `1024`

createdAt -\> (timestamp)

> The timestamp when the payment manager was created.

lastUpdatedAt -\> (timestamp)

> The timestamp when the payment manager was last updated.

status -\> (string)

> The current status of the payment manager. Possible values include `CREATING` , `READY` , `UPDATING` , `DELETING` , `CREATE_FAILED` , `UPDATE_FAILED` , and `DELETE_FAILED` .
>
> Possible values:
>
> - `CREATING`
> - `UPDATING`
> - `DELETING`
> - `READY`
> - `CREATE_FAILED`
> - `UPDATE_FAILED`
> - `DELETE_FAILED`

tags -\> (map)

> The tags associated with the payment manager.
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

kmsKeyArn -\> (string)

> The Amazon Resource Name (ARN) of the KMS key used to encrypt sensitive payment manager data at rest, if configured.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`

- [← get-payment-credential-provider](get-payment-credential-provider.html "previous chapter (use the left arrow)") /
- [get-policy →](get-policy.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](get-policy.html "get-policy") \|
- [previous](get-payment-credential-provider.html "get-payment-credential-provider") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [get-payment-manager]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

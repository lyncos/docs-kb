---
title: aws agent-registry-control create-registry
description: \ [aws . agent-registry-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / agent-registry-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/agent-registry-control/create-registry.html
fetched: '2026-09-26'
tags:
- agent-registry
- agent-registry-control
- agentcore
- aws-cli
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [agent-registry-control](index.html#cli-aws-agent-registry-control) \]

# create-registry

## Description

Creates a new registry, a catalog that organizes registry records and defines their discovery authorization and record approval behavior. Creation is asynchronous: the registry begins in the CREATING status and becomes usable once it reaches READY.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/agent-registry-control-2025-12-01/CreateRegistry)

## Synopsis

      create-registry
    --name <value>
    [--description <value>]
    [--encryption-configuration <value>]
    [--discovery-configuration <value>]
    [--client-token <value>]
    [--tags <value>]
    [--approval-configuration <value>]
    [--auto-detection-configuration <value>]
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

> The name of the registry
>
> Constraints:
>
> - min: `1`
> - max: `64`
> - pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`

`--description` (string)

> The description of the registry
>
> Constraints:
>
> - min: `1`
> - max: `4096`

`--encryption-configuration` (structure)

> The optional server-side encryption configuration for the registry. When you provide this field, the specified customer-managed Amazon Web Services KMS key encrypts the registry’s content. Omit this field to use an Amazon Web Services-owned encryption key. You cannot change the encryption configuration after registry creation.
>
> kmsKeyArn -\> (string) \[required\]
>
> > The Amazon Resource Name (ARN) of the customer-managed Amazon Web Services KMS key used to encrypt the registry’s content. The key must be a symmetric encryption key in the same Amazon Web Services account and Region as the registry.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `2048`
> > - pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`

Shorthand Syntax:

    kmsKeyArn=string

JSON Syntax:

    {
      "kmsKeyArn": "string"
    }

`--discovery-configuration` (structure)

> Discovery configuration for the registry
>
> authorizerConfiguration -\> (tagged union structure)
>
> > The authorizer configuration for the registry. Required when authorizerType is CUSTOM_JWT.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `customJWTAuthorizer`.
> >
> > customJWTAuthorizer -\> (structure)
> >
> > > Configuration for a custom JWT authorizer.
> > >
> > > discoveryUrl -\> (string) \[required\]
> > >
> > > > The OpenID Connect discovery URL used to retrieve the identity provider’s metadata and signing keys.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `2048`
> > > > - pattern: `.+/\.well-known/openid-configuration`
> > >
> > > allowedAudience -\> (list)
> > >
> > > > The audience values accepted during JWT validation. A token is rejected if none of its audience claims match.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > >
> > > > (string)
> > > >
> > > > > An audience value that an inbound JWT must contain to be authorized.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `255`
> > >
> > > allowedClients -\> (list)
> > >
> > > > The client identifiers accepted during JWT validation. A token is rejected if it was not issued to one of these clients.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > >
> > > > (string)
> > > >
> > > > > A client identifier that an inbound JWT must be issued to in order to be authorized.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `255`
> > >
> > > allowedScopes -\> (list)
> > >
> > > > The scopes accepted during JWT validation. A token is rejected if it does not carry one of these scopes.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > >
> > > > (string)
> > > >
> > > > > A scope value that an inbound JWT must carry to be authorized.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `255`
> > > > > - pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
> > >
> > > customClaims -\> (list)
> > >
> > > > Additional custom claim validations applied to the inbound JWT.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > >
> > > > (structure)
> > > >
> > > > > A validation rule applied to a single claim of an inbound JWT.
> > > > >
> > > > > inboundTokenClaimName -\> (string) \[required\]
> > > > >
> > > > > > The name of the claim in the inbound token to validate.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `255`
> > > > > > - pattern: `[A-Za-z0-9_.-:]+`
> > > > >
> > > > > inboundTokenClaimValueType -\> (string) \[required\]
> > > > >
> > > > > > The value type of the claim in the inbound token, either a string or an array of strings.
> > > > > >
> > > > > > Possible values:
> > > > > >
> > > > > > - `STRING`
> > > > > > - `STRING_ARRAY`
> > > > >
> > > > > authorizingClaimMatchValue -\> (structure) \[required\]
> > > > >
> > > > > > The value and match operator used to authorize the claim.
> > > > > >
> > > > > > claimMatchValue -\> (tagged union structure) \[required\]
> > > > > >
> > > > > > > The expected value or values that the claim is compared against.
> > > > > > >
> > > > > > > ### Note
> > > > > > >
> > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `matchValueString`, `matchValueStringList`.
> > > > > > >
> > > > > > > matchValueString -\> (string)
> > > > > > >
> > > > > > > > A single string value to match the claim against.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > > > > - pattern: `[A-Za-z0-9_.:/-]+`
> > > > > > >
> > > > > > > matchValueStringList -\> (list)
> > > > > > >
> > > > > > > > A list of string values to match the claim against.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > >
> > > > > > > > (string)
> > > > > > > >
> > > > > > > > > A single value used to match a claim during JWT validation.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `255`
> > > > > > > > > - pattern: `[A-Za-z0-9_.:/-]+`
> > > > > >
> > > > > > claimMatchOperator -\> (string) \[required\]
> > > > > >
> > > > > > > The operator used to compare the claim value against the expected value.
> > > > > > >
> > > > > > > Possible values:
> > > > > > >
> > > > > > > - `EQUALS`
> > > > > > > - `CONTAINS`
> > > > > > > - `CONTAINS_ANY`
> > >
> > > privateEndpoint -\> (tagged union structure)
> > >
> > > > The private endpoint used to reach the identity provider’s discovery URL over a private network path.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `selfManagedLatticeResource`, `managedVpcResource`.
> > > >
> > > > selfManagedLatticeResource -\> (tagged union structure)
> > > >
> > > > > A private endpoint backed by a self-managed VPC Lattice resource configuration.
> > > > >
> > > > > ### Note
> > > > >
> > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `resourceConfigurationIdentifier`.
> > > > >
> > > > > resourceConfigurationIdentifier -\> (string)
> > > > >
> > > > > > The identifier of the VPC Lattice resource configuration, specified as a resource configuration ID or ARN.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `20`
> > > > > > - max: `2048`
> > > > > > - pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`
> > > >
> > > > managedVpcResource -\> (structure)
> > > >
> > > > > A private endpoint backed by a service-managed VPC resource.
> > > > >
> > > > > vpcIdentifier -\> (string) \[required\]
> > > > >
> > > > > > The identifier of the VPC in which the private endpoint is provisioned.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `10`
> > > > > > - max: `48`
> > > > > > - pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > >
> > > > > subnetIds -\> (list) \[required\]
> > > > >
> > > > > > The identifiers of the subnets in which the private endpoint network interfaces are placed.
> > > > > >
> > > > > > (string)
> > > > > >
> > > > > > > Subnet identifier
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `15`
> > > > > > > - max: `24`
> > > > > > > - pattern: `subnet-[0-9a-zA-Z]{8,17}`
> > > > >
> > > > > endpointIpAddressType -\> (string) \[required\]
> > > > >
> > > > > > The IP address type used by the private endpoint, either IPV4 or IPV6.
> > > > > >
> > > > > > Possible values:
> > > > > >
> > > > > > - `IPV4`
> > > > > > - `IPV6`
> > > > >
> > > > > securityGroupIds -\> (list)
> > > > >
> > > > > > The identifiers of the security groups associated with the private endpoint network interfaces.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `0`
> > > > > > - max: `5`
> > > > > >
> > > > > > (string)
> > > > > >
> > > > > > > The identifier of a security group.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `10`
> > > > > > > - max: `48`
> > > > > > > - pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > >
> > > > > tags -\> (map)
> > > > >
> > > > > > The tags applied to the service-managed VPC resource.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `50`
> > > > > >
> > > > > > key -\> (string)
> > > > > >
> > > > > > > Key of a tag.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `128`
> > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > >
> > > > > > value -\> (string)
> > > > > >
> > > > > > > Value of a tag.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `0`
> > > > > > > - max: `256`
> > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > >
> > > > > routingDomain -\> (string)
> > > > >
> > > > > > The routing domain used to resolve traffic through the private endpoint.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `3`
> > > > > > - max: `255`
> > >
> > > privateEndpointOverrides -\> (list)
> > >
> > > > Per-domain private endpoint overrides that route specific identity provider domains through distinct private endpoints.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0`
> > > > - max: `5`
> > > >
> > > > (structure)
> > > >
> > > > > A mapping of a domain to the private endpoint used to reach it.
> > > > >
> > > > > domain -\> (string) \[required\]
> > > > >
> > > > > > The domain name to which this private endpoint override applies.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `253`
> > > > >
> > > > > privateEndpoint -\> (tagged union structure) \[required\]
> > > > >
> > > > > > The private endpoint used to reach the specified domain.
> > > > > >
> > > > > > ### Note
> > > > > >
> > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `selfManagedLatticeResource`, `managedVpcResource`.
> > > > > >
> > > > > > selfManagedLatticeResource -\> (tagged union structure)
> > > > > >
> > > > > > > A private endpoint backed by a self-managed VPC Lattice resource configuration.
> > > > > > >
> > > > > > > ### Note
> > > > > > >
> > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `resourceConfigurationIdentifier`.
> > > > > > >
> > > > > > > resourceConfigurationIdentifier -\> (string)
> > > > > > >
> > > > > > > > The identifier of the VPC Lattice resource configuration, specified as a resource configuration ID or ARN.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `20`
> > > > > > > > - max: `2048`
> > > > > > > > - pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`
> > > > > >
> > > > > > managedVpcResource -\> (structure)
> > > > > >
> > > > > > > A private endpoint backed by a service-managed VPC resource.
> > > > > > >
> > > > > > > vpcIdentifier -\> (string) \[required\]
> > > > > > >
> > > > > > > > The identifier of the VPC in which the private endpoint is provisioned.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `10`
> > > > > > > > - max: `48`
> > > > > > > > - pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > > >
> > > > > > > subnetIds -\> (list) \[required\]
> > > > > > >
> > > > > > > > The identifiers of the subnets in which the private endpoint network interfaces are placed.
> > > > > > > >
> > > > > > > > (string)
> > > > > > > >
> > > > > > > > > Subnet identifier
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `15`
> > > > > > > > > - max: `24`
> > > > > > > > > - pattern: `subnet-[0-9a-zA-Z]{8,17}`
> > > > > > >
> > > > > > > endpointIpAddressType -\> (string) \[required\]
> > > > > > >
> > > > > > > > The IP address type used by the private endpoint, either IPV4 or IPV6.
> > > > > > > >
> > > > > > > > Possible values:
> > > > > > > >
> > > > > > > > - `IPV4`
> > > > > > > > - `IPV6`
> > > > > > >
> > > > > > > securityGroupIds -\> (list)
> > > > > > >
> > > > > > > > The identifiers of the security groups associated with the private endpoint network interfaces.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `0`
> > > > > > > > - max: `5`
> > > > > > > >
> > > > > > > > (string)
> > > > > > > >
> > > > > > > > > The identifier of a security group.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `10`
> > > > > > > > > - max: `48`
> > > > > > > > > - pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > > >
> > > > > > > tags -\> (map)
> > > > > > >
> > > > > > > > The tags applied to the service-managed VPC resource.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `50`
> > > > > > > >
> > > > > > > > key -\> (string)
> > > > > > > >
> > > > > > > > > Key of a tag.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `128`
> > > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > > > >
> > > > > > > > value -\> (string)
> > > > > > > >
> > > > > > > > > Value of a tag.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `0`
> > > > > > > > > - max: `256`
> > > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > > >
> > > > > > > routingDomain -\> (string)
> > > > > > >
> > > > > > > > The routing domain used to resolve traffic through the private endpoint.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `3`
> > > > > > > > - max: `255`
>
> authorizerType -\> (string)
>
> > The type of authorizer that controls how consumers access the registry’s search and MCP invoke operations.
> >
> > Possible values:
> >
> > - `CUSTOM_JWT`
> > - `AWS_IAM`

JSON Syntax:

    {
      "authorizerConfiguration": {
        "customJWTAuthorizer": {
          "discoveryUrl": "string",
          "allowedAudience": ["string", ...],
          "allowedClients": ["string", ...],
          "allowedScopes": ["string", ...],
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
          ]
        }
      },
      "authorizerType": "CUSTOM_JWT"|"AWS_IAM"
    }

`--client-token` (string)

> A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.
>
> Constraints:
>
> - min: `33`
> - max: `256`
> - pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`

`--tags` (map)

> Tags to associate with the registry
>
> Constraints:
>
> - min: `1`
> - max: `50`
>
> key -\> (string)
>
> > Key of a tag.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `128`
> > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
>
> value -\> (string)
>
> > Value of a tag.
> >
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

`--approval-configuration` (structure)

> Approval configuration for registry records
>
> autoApprovalRules -\> (list)
>
> > The rules that determine which registry records are automatically approved on submission. When omitted or empty, submitted records require manual review.
> >
> > Constraints:
> >
> > - min: `0`
> > - max: `10`
> >
> > (string)
> >
> > > Possible values:
> > >
> > > - `APPROVE_ALL`

Shorthand Syntax:

    autoApprovalRules=string,string

JSON Syntax:

    {
      "autoApprovalRules": ["APPROVE_ALL", ...]
    }

`--auto-detection-configuration` (structure)

> The optional auto-detection configuration for the registry. When provided, the registry is automatically populated with resources discovered according to the configuration. Omit this field for registries whose records are managed exclusively through the Agent Registry Control API.
>
> scope -\> (string) \[required\]
>
> > The source from which resources are detected. For example, `ORGANIZATION` sources resources from all member accounts of an Amazon Web Services organization.
> >
> > Possible values:
> >
> > - `ORGANIZATION`
>
> enabled -\> (boolean) \[required\]
>
> > Specifies whether auto-detection is requested for the registry. Setting this to `true` is necessary but not sufficient for auto-detection to become active; the preconditions of the configured scope must also be met.

Shorthand Syntax:

    scope=string,enabled=boolean

JSON Syntax:

    {
      "scope": "ORGANIZATION",
      "enabled": true|false
    }

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

registryArn -\> (string)

> The ARN of the created registry
>
> Constraints:
>
> - min: `46`
> - max: `2048`
> - pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}`

- [← agent-registry-control](index.html "previous chapter (use the left arrow)") /
- [create-registry-record →](create-registry-record.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](create-registry-record.html "create-registry-record") \|
- [previous](index.html "agent-registry-control") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [agent-registry-control](index.html) »
- [create-registry]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

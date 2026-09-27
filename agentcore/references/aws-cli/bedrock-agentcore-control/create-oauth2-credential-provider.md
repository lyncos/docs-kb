---
title: aws bedrock-agentcore-control create-oauth2-credential-provider
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/create-oauth2-credential-provider.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# create-oauth2-credential-provider

## Description

Creates a new OAuth2 credential provider.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/CreateOauth2CredentialProvider)

## Synopsis

      create-oauth2-credential-provider
    --name <value>
    --credential-provider-vendor <value>
    --oauth2-provider-config-input <value>
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

`--name` (string) \[required\]

> The name of the OAuth2 credential provider. The name must be unique within your account.
>
> Constraints:
>
> - min: `1`
> - max: `128`
> - pattern: `[a-zA-Z0-9\-_]+`

`--credential-provider-vendor` (string) \[required\]

> The vendor of the OAuth2 credential provider. This specifies which OAuth2 implementation to use.
>
> Possible values:
>
> - `GoogleOauth2`
> - `GithubOauth2`
> - `SlackOauth2`
> - `SalesforceOauth2`
> - `MicrosoftOauth2`
> - `CustomOauth2`
> - `AtlassianOauth2`
> - `LinkedinOauth2`
> - `XOauth2`
> - `OktaOauth2`
> - `OneLoginOauth2`
> - `PingOneOauth2`
> - `FacebookOauth2`
> - `YandexOauth2`
> - `RedditOauth2`
> - `ZoomOauth2`
> - `TwitchOauth2`
> - `SpotifyOauth2`
> - `DropboxOauth2`
> - `NotionOauth2`
> - `HubspotOauth2`
> - `CyberArkOauth2`
> - `FusionAuthOauth2`
> - `Auth0Oauth2`
> - `CognitoOauth2`

`--oauth2-provider-config-input` (tagged union structure) \[required\]

> The configuration settings for the OAuth2 provider, including client ID, client secret, and other vendor-specific settings.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `customOauth2ProviderConfig`, `googleOauth2ProviderConfig`, `githubOauth2ProviderConfig`, `slackOauth2ProviderConfig`, `salesforceOauth2ProviderConfig`, `microsoftOauth2ProviderConfig`, `atlassianOauth2ProviderConfig`, `linkedinOauth2ProviderConfig`, `includedOauth2ProviderConfig`.
>
> customOauth2ProviderConfig -\> (structure)
>
> > The configuration for a custom OAuth2 provider.
> >
> > oauthDiscovery -\> (tagged union structure) \[required\]
> >
> > > The OAuth2 discovery information for the custom provider.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `discoveryUrl`, `authorizationServerMetadata`.
> > >
> > > discoveryUrl -\> (string)
> > >
> > > > The discovery URL for the OAuth2 provider.
> > > >
> > > > Constraints:
> > > >
> > > > - pattern: `.+/\.well-known/(openid-configuration|oauth-authorization-server)`
> > >
> > > authorizationServerMetadata -\> (structure)
> > >
> > > > The authorization server metadata for the OAuth2 provider.
> > > >
> > > > issuer -\> (string) \[required\]
> > > >
> > > > > The issuer URL for the OAuth2 authorization server.
> > > >
> > > > authorizationEndpoint -\> (string) \[required\]
> > > >
> > > > > The authorization endpoint URL for the OAuth2 authorization server.
> > > >
> > > > tokenEndpoint -\> (string) \[required\]
> > > >
> > > > > The token endpoint URL for the OAuth2 authorization server.
> > > >
> > > > responseTypes -\> (list)
> > > >
> > > > > The supported response types for the OAuth2 authorization server.
> > > > >
> > > > > (string)
> > > >
> > > > tokenEndpointAuthMethods -\> (list)
> > > >
> > > > > The authentication methods supported by the token endpoint. This specifies how clients can authenticate when requesting tokens from the authorization server.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `2`
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - pattern: `(client_secret_post|client_secret_basic)`
> >
> > clientId -\> (string)
> >
> > > The client ID for the custom OAuth2 provider.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `256`
> >
> > clientSecret -\> (string)
> >
> > > The client secret for the custom OAuth2 provider.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `2048`
> >
> > clientSecretConfig -\> (structure)
> >
> > > A reference to the Amazon Web Services Secrets Manager secret that stores the client secret. This includes the secret ID and the JSON key used to extract the client secret value from the secret. Required when `clientSecretSource` is set to `EXTERNAL` .
> > >
> > > secretId -\> (string) \[required\]
> > >
> > > > The ID of the Amazon Web Services Secrets Manager secret that stores the secret value.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `2048`
> > >
> > > jsonKey -\> (string) \[required\]
> > >
> > > > The JSON key used to extract the secret value from the Amazon Web Services Secrets Manager secret.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `128`
> >
> > clientSecretSource -\> (string)
> >
> > > The source type of the client secret. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in Amazon Web Services Secrets Manager.
> > >
> > > Possible values:
> > >
> > > - `MANAGED`
> > > - `EXTERNAL`
> >
> > onBehalfOfTokenExchangeConfig -\> (structure)
> >
> > > The configuration for on-behalf-of token exchange. This enables authentication flows that use RFC 8693 token exchange or RFC 7523 JWT authorization grants.
> > >
> > > grantType -\> (string) \[required\]
> > >
> > > > The grant type for the on-behalf-of token exchange.
> > > >
> > > > Possible values:
> > > >
> > > > - `TOKEN_EXCHANGE`
> > > > - `JWT_AUTHORIZATION_GRANT`
> > >
> > > tokenExchangeGrantTypeConfig -\> (structure)
> > >
> > > > Configuration specific to the TOKEN_EXCHANGE grant type (RFC 8693).
> > > >
> > > > actorTokenContent -\> (string) \[required\]
> > > >
> > > > > The content type for the actor token in the token exchange.
> > > > >
> > > > > Possible values:
> > > > >
> > > > > - `NONE`
> > > > > - `M2M`
> > > > > - `AWS_IAM_ID_TOKEN_JWT`
> > > >
> > > > actorTokenScopes -\> (list)
> > > >
> > > > > The scopes for the actor token. Only valid when actorTokenContent is M2M.
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `128`
> >
> > clientAuthenticationMethod -\> (string)
> >
> > > The client authentication method to use when authenticating with the token endpoint.
> > >
> > > Possible values:
> > >
> > > - `CLIENT_SECRET_BASIC`
> > > - `CLIENT_SECRET_POST`
> > > - `AWS_IAM_ID_TOKEN_JWT`
> > > - `PRIVATE_KEY_JWT`
> >
> > privateKeyJwtConfig -\> (structure)
> >
> > > The private_key_jwt client authentication configuration for this credential provider. When specified, the credential provider uses JWT client assertions to authenticate with the token endpoint.
> > >
> > > privateKeySource -\> (tagged union structure)
> > >
> > > > The private key source for the JWT client assertion.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `kmsKeySource`.
> > > >
> > > > kmsKeySource -\> (structure)
> > > >
> > > > > The KMS key source for the JWT client assertion.
> > > > >
> > > > > kmsKeyArn -\> (string) \[required\]
> > > > >
> > > > > > The Amazon Resource Name (ARN) of the KMS key used to sign the JWT client assertion. The key must be an asymmetric key with key usage SIGN_VERIFY and a key spec compatible with the configured signing algorithm.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `2048`
> > > > > > - pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`
> > >
> > > signingAlgorithm -\> (string)
> > >
> > > > The algorithm used to sign the JWT client assertion. Valid values are `RS256` , `PS256` , and `ES256` .
> > > >
> > > > Possible values:
> > > >
> > > > - `RS256`
> > > > - `PS256`
> > > > - `ES256`
> > >
> > > additionalHeaderClaims -\> (map)
> > >
> > > > A map of additional claims to include in the JWT client assertion header. Standard header claims such as `alg` and `typ` cannot be added.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `10`
> > > >
> > > > key -\> (string)
> > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `255`
> > > > > - pattern: `[A-Za-z0-9_.:#-]+`
> > > >
> > > > value -\> (string)
> > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `2048`
> > >
> > > additionalPayloadClaims -\> (map)
> > >
> > > > A map of additional claims to include in the JWT client assertion payload. Payload claims generated by the service, such as `iss` , `sub` , `jti` , and `exp` , cannot be added.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `10`
> > > >
> > > > key -\> (string)
> > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `255`
> > > > > - pattern: `[A-Za-z0-9_.:#-]+`
> > > >
> > > > value -\> (string)
> > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `2048`
> >
> > privateEndpoint -\> (tagged union structure)
> >
> > > The default private endpoint for the custom OAuth2 provider, enabling secure connectivity through a VPC Lattice resource configuration.
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
> > > The private endpoint overrides for the custom OAuth2 provider configuration.
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
>
> googleOauth2ProviderConfig -\> (structure)
>
> > The configuration for a Google OAuth2 provider.
> >
> > clientId -\> (string) \[required\]
> >
> > > The client ID for the Google OAuth2 provider.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `256`
> >
> > clientSecret -\> (string)
> >
> > > The client secret for the Google OAuth2 provider.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `2048`
> >
> > clientSecretConfig -\> (structure)
> >
> > > A reference to the Amazon Web Services Secrets Manager secret that stores the client secret. This includes the secret ID and the JSON key used to extract the client secret value from the secret. Required when `clientSecretSource` is set to `EXTERNAL` .
> > >
> > > secretId -\> (string) \[required\]
> > >
> > > > The ID of the Amazon Web Services Secrets Manager secret that stores the secret value.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `2048`
> > >
> > > jsonKey -\> (string) \[required\]
> > >
> > > > The JSON key used to extract the secret value from the Amazon Web Services Secrets Manager secret.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `128`
> >
> > clientSecretSource -\> (string)
> >
> > > The source type of the client secret. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in Amazon Web Services Secrets Manager.
> > >
> > > Possible values:
> > >
> > > - `MANAGED`
> > > - `EXTERNAL`
>
> githubOauth2ProviderConfig -\> (structure)
>
> > The configuration for a GitHub OAuth2 provider.
> >
> > clientId -\> (string) \[required\]
> >
> > > The client ID for the GitHub OAuth2 provider.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `256`
> >
> > clientSecret -\> (string)
> >
> > > The client secret for the GitHub OAuth2 provider.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `2048`
> >
> > clientSecretConfig -\> (structure)
> >
> > > A reference to the Amazon Web Services Secrets Manager secret that stores the client secret. This includes the secret ID and the JSON key used to extract the client secret value from the secret. Required when `clientSecretSource` is set to `EXTERNAL` .
> > >
> > > secretId -\> (string) \[required\]
> > >
> > > > The ID of the Amazon Web Services Secrets Manager secret that stores the secret value.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `2048`
> > >
> > > jsonKey -\> (string) \[required\]
> > >
> > > > The JSON key used to extract the secret value from the Amazon Web Services Secrets Manager secret.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `128`
> >
> > clientSecretSource -\> (string)
> >
> > > The source type of the client secret. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in Amazon Web Services Secrets Manager.
> > >
> > > Possible values:
> > >
> > > - `MANAGED`
> > > - `EXTERNAL`
>
> slackOauth2ProviderConfig -\> (structure)
>
> > The configuration for a Slack OAuth2 provider.
> >
> > clientId -\> (string) \[required\]
> >
> > > The client ID for the Slack OAuth2 provider.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `256`
> >
> > clientSecret -\> (string)
> >
> > > The client secret for the Slack OAuth2 provider.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `2048`
> >
> > clientSecretConfig -\> (structure)
> >
> > > A reference to the Amazon Web Services Secrets Manager secret that stores the client secret. This includes the secret ID and the JSON key used to extract the client secret value from the secret. Required when `clientSecretSource` is set to `EXTERNAL` .
> > >
> > > secretId -\> (string) \[required\]
> > >
> > > > The ID of the Amazon Web Services Secrets Manager secret that stores the secret value.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `2048`
> > >
> > > jsonKey -\> (string) \[required\]
> > >
> > > > The JSON key used to extract the secret value from the Amazon Web Services Secrets Manager secret.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `128`
> >
> > clientSecretSource -\> (string)
> >
> > > The source type of the client secret. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in Amazon Web Services Secrets Manager.
> > >
> > > Possible values:
> > >
> > > - `MANAGED`
> > > - `EXTERNAL`
>
> salesforceOauth2ProviderConfig -\> (structure)
>
> > The configuration for a Salesforce OAuth2 provider.
> >
> > clientId -\> (string) \[required\]
> >
> > > The client ID for the Salesforce OAuth2 provider.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `256`
> >
> > clientSecret -\> (string)
> >
> > > The client secret for the Salesforce OAuth2 provider.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `2048`
> >
> > clientSecretConfig -\> (structure)
> >
> > > A reference to the Amazon Web Services Secrets Manager secret that stores the client secret. This includes the secret ID and the JSON key used to extract the client secret value from the secret. Required when `clientSecretSource` is set to `EXTERNAL` .
> > >
> > > secretId -\> (string) \[required\]
> > >
> > > > The ID of the Amazon Web Services Secrets Manager secret that stores the secret value.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `2048`
> > >
> > > jsonKey -\> (string) \[required\]
> > >
> > > > The JSON key used to extract the secret value from the Amazon Web Services Secrets Manager secret.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `128`
> >
> > clientSecretSource -\> (string)
> >
> > > The source type of the client secret. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in Amazon Web Services Secrets Manager.
> > >
> > > Possible values:
> > >
> > > - `MANAGED`
> > > - `EXTERNAL`
>
> microsoftOauth2ProviderConfig -\> (structure)
>
> > The configuration for a Microsoft OAuth2 provider.
> >
> > clientId -\> (string) \[required\]
> >
> > > The client ID for the Microsoft OAuth2 provider.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `256`
> >
> > clientSecret -\> (string)
> >
> > > The client secret for the Microsoft OAuth2 provider.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `2048`
> >
> > clientSecretConfig -\> (structure)
> >
> > > A reference to the Amazon Web Services Secrets Manager secret that stores the client secret. This includes the secret ID and the JSON key used to extract the client secret value from the secret. Required when `clientSecretSource` is set to `EXTERNAL` .
> > >
> > > secretId -\> (string) \[required\]
> > >
> > > > The ID of the Amazon Web Services Secrets Manager secret that stores the secret value.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `2048`
> > >
> > > jsonKey -\> (string) \[required\]
> > >
> > > > The JSON key used to extract the secret value from the Amazon Web Services Secrets Manager secret.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `128`
> >
> > clientSecretSource -\> (string)
> >
> > > The source type of the client secret. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in Amazon Web Services Secrets Manager.
> > >
> > > Possible values:
> > >
> > > - `MANAGED`
> > > - `EXTERNAL`
> >
> > tenantId -\> (string)
> >
> > > The Microsoft Entra ID (formerly Azure AD) tenant ID for your organization. This identifies the specific tenant within Microsoft’s identity platform where your application is registered.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `2048`
>
> atlassianOauth2ProviderConfig -\> (structure)
>
> > Configuration settings for Atlassian OAuth2 provider integration.
> >
> > clientId -\> (string) \[required\]
> >
> > > The client ID for the Atlassian OAuth2 provider. This identifier is assigned by Atlassian when you register your application.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `256`
> >
> > clientSecret -\> (string)
> >
> > > The client secret for the Atlassian OAuth2 provider. This secret is assigned by Atlassian and used along with the client ID to authenticate your application.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `2048`
> >
> > clientSecretConfig -\> (structure)
> >
> > > A reference to the Amazon Web Services Secrets Manager secret that stores the client secret. This includes the secret ID and the JSON key used to extract the client secret value from the secret. Required when `clientSecretSource` is set to `EXTERNAL` .
> > >
> > > secretId -\> (string) \[required\]
> > >
> > > > The ID of the Amazon Web Services Secrets Manager secret that stores the secret value.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `2048`
> > >
> > > jsonKey -\> (string) \[required\]
> > >
> > > > The JSON key used to extract the secret value from the Amazon Web Services Secrets Manager secret.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `128`
> >
> > clientSecretSource -\> (string)
> >
> > > The source type of the client secret for the Atlassian OAuth2 provider. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in Amazon Web Services Secrets Manager.
> > >
> > > Possible values:
> > >
> > > - `MANAGED`
> > > - `EXTERNAL`
>
> linkedinOauth2ProviderConfig -\> (structure)
>
> > Configuration settings for LinkedIn OAuth2 provider integration.
> >
> > clientId -\> (string) \[required\]
> >
> > > The client ID for the LinkedIn OAuth2 provider. This identifier is assigned by LinkedIn when you register your application.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `256`
> >
> > clientSecret -\> (string)
> >
> > > The client secret for the LinkedIn OAuth2 provider. This secret is assigned by LinkedIn and used along with the client ID to authenticate your application.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `2048`
> >
> > clientSecretConfig -\> (structure)
> >
> > > A reference to the Amazon Web Services Secrets Manager secret that stores the client secret. This includes the secret ID and the JSON key used to extract the client secret value from the secret. Required when `clientSecretSource` is set to `EXTERNAL` .
> > >
> > > secretId -\> (string) \[required\]
> > >
> > > > The ID of the Amazon Web Services Secrets Manager secret that stores the secret value.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `2048`
> > >
> > > jsonKey -\> (string) \[required\]
> > >
> > > > The JSON key used to extract the secret value from the Amazon Web Services Secrets Manager secret.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `128`
> >
> > clientSecretSource -\> (string)
> >
> > > The source type of the client secret. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in Amazon Web Services Secrets Manager.
> > >
> > > Possible values:
> > >
> > > - `MANAGED`
> > > - `EXTERNAL`
>
> includedOauth2ProviderConfig -\> (structure)
>
> > The configuration for a non-custom OAuth2 provider. This includes settings for supported OAuth2 providers that have built-in integration support.
> >
> > clientId -\> (string) \[required\]
> >
> > > The client ID for the supported OAuth2 provider. This identifier is assigned by the OAuth2 provider when you register your application.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `256`
> >
> > clientSecret -\> (string)
> >
> > > The client secret for the supported OAuth2 provider. This secret is assigned by the OAuth2 provider and used along with the client ID to authenticate your application.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `2048`
> >
> > clientSecretConfig -\> (structure)
> >
> > > A reference to the Amazon Web Services Secrets Manager secret that stores the client secret. This includes the secret ID and the JSON key used to extract the client secret value from the secret. Required when `clientSecretSource` is set to `EXTERNAL` .
> > >
> > > secretId -\> (string) \[required\]
> > >
> > > > The ID of the Amazon Web Services Secrets Manager secret that stores the secret value.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `2048`
> > >
> > > jsonKey -\> (string) \[required\]
> > >
> > > > The JSON key used to extract the secret value from the Amazon Web Services Secrets Manager secret.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `128`
> >
> > clientSecretSource -\> (string)
> >
> > > The source type of the client secret. Use `MANAGED` if the secret is managed by the service, or `EXTERNAL` if you manage the secret yourself in Amazon Web Services Secrets Manager.
> > >
> > > Possible values:
> > >
> > > - `MANAGED`
> > > - `EXTERNAL`
> >
> > issuer -\> (string)
> >
> > > Token issuer of your isolated OAuth2 application tenant. This URL identifies the authorization server that issues tokens for this provider.
> >
> > authorizationEndpoint -\> (string)
> >
> > > OAuth2 authorization endpoint for your isolated OAuth2 application tenant. This is where users are redirected to authenticate and authorize access to their resources.
> >
> > tokenEndpoint -\> (string)
> >
> > > OAuth2 token endpoint for your isolated OAuth2 application tenant. This is where authorization codes are exchanged for access tokens.

JSON Syntax:

    {
      "customOauth2ProviderConfig": {
        "oauthDiscovery": {
          "discoveryUrl": "string",
          "authorizationServerMetadata": {
            "issuer": "string",
            "authorizationEndpoint": "string",
            "tokenEndpoint": "string",
            "responseTypes": ["string", ...],
            "tokenEndpointAuthMethods": ["string", ...]
          }
        },
        "clientId": "string",
        "clientSecret": "string",
        "clientSecretConfig": {
          "secretId": "string",
          "jsonKey": "string"
        },
        "clientSecretSource": "MANAGED"|"EXTERNAL",
        "onBehalfOfTokenExchangeConfig": {
          "grantType": "TOKEN_EXCHANGE"|"JWT_AUTHORIZATION_GRANT",
          "tokenExchangeGrantTypeConfig": {
            "actorTokenContent": "NONE"|"M2M"|"AWS_IAM_ID_TOKEN_JWT",
            "actorTokenScopes": ["string", ...]
          }
        },
        "clientAuthenticationMethod": "CLIENT_SECRET_BASIC"|"CLIENT_SECRET_POST"|"AWS_IAM_ID_TOKEN_JWT"|"PRIVATE_KEY_JWT",
        "privateKeyJwtConfig": {
          "privateKeySource": {
            "kmsKeySource": {
              "kmsKeyArn": "string"
            }
          },
          "signingAlgorithm": "RS256"|"PS256"|"ES256",
          "additionalHeaderClaims": {"string": "string"
            ...},
          "additionalPayloadClaims": {"string": "string"
            ...}
        },
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
      },
      "googleOauth2ProviderConfig": {
        "clientId": "string",
        "clientSecret": "string",
        "clientSecretConfig": {
          "secretId": "string",
          "jsonKey": "string"
        },
        "clientSecretSource": "MANAGED"|"EXTERNAL"
      },
      "githubOauth2ProviderConfig": {
        "clientId": "string",
        "clientSecret": "string",
        "clientSecretConfig": {
          "secretId": "string",
          "jsonKey": "string"
        },
        "clientSecretSource": "MANAGED"|"EXTERNAL"
      },
      "slackOauth2ProviderConfig": {
        "clientId": "string",
        "clientSecret": "string",
        "clientSecretConfig": {
          "secretId": "string",
          "jsonKey": "string"
        },
        "clientSecretSource": "MANAGED"|"EXTERNAL"
      },
      "salesforceOauth2ProviderConfig": {
        "clientId": "string",
        "clientSecret": "string",
        "clientSecretConfig": {
          "secretId": "string",
          "jsonKey": "string"
        },
        "clientSecretSource": "MANAGED"|"EXTERNAL"
      },
      "microsoftOauth2ProviderConfig": {
        "clientId": "string",
        "clientSecret": "string",
        "clientSecretConfig": {
          "secretId": "string",
          "jsonKey": "string"
        },
        "clientSecretSource": "MANAGED"|"EXTERNAL",
        "tenantId": "string"
      },
      "atlassianOauth2ProviderConfig": {
        "clientId": "string",
        "clientSecret": "string",
        "clientSecretConfig": {
          "secretId": "string",
          "jsonKey": "string"
        },
        "clientSecretSource": "MANAGED"|"EXTERNAL"
      },
      "linkedinOauth2ProviderConfig": {
        "clientId": "string",
        "clientSecret": "string",
        "clientSecretConfig": {
          "secretId": "string",
          "jsonKey": "string"
        },
        "clientSecretSource": "MANAGED"|"EXTERNAL"
      },
      "includedOauth2ProviderConfig": {
        "clientId": "string",
        "clientSecret": "string",
        "clientSecretConfig": {
          "secretId": "string",
          "jsonKey": "string"
        },
        "clientSecretSource": "MANAGED"|"EXTERNAL",
        "issuer": "string",
        "authorizationEndpoint": "string",
        "tokenEndpoint": "string"
      }
    }

`--tags` (map)

> A map of tag keys and values to assign to the OAuth2 credential provider. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.
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

clientSecretArn -\> (structure)

> The Amazon Resource Name (ARN) of the client secret in Amazon Web Services Secrets Manager.
>
> secretArn -\> (string) \[required\]
>
> > The Amazon Resource Name (ARN) of the secret in Amazon Web Services Secrets Manager.
> >
> > Constraints:
> >
> > - pattern: `arn:(aws|aws-us-gov):secretsmanager:[A-Za-z0-9-]{1,64}:[0-9]{12}:secret:[a-zA-Z0-9-_/+=.@!]+`

clientSecretJsonKey -\> (string)

> The JSON key used to extract the client secret value from the Amazon Web Services Secrets Manager secret.
>
> Constraints:
>
> - min: `1`
> - max: `128`

clientSecretSource -\> (string)

> The source type of the client secret. Either `MANAGED` if the secret is managed by the service, or `EXTERNAL` if managed by the user in Amazon Web Services Secrets Manager.
>
> Possible values:
>
> - `MANAGED`
> - `EXTERNAL`

name -\> (string)

> The name of the OAuth2 credential provider.
>
> Constraints:
>
> - min: `1`
> - max: `128`
> - pattern: `[a-zA-Z0-9\-_]+`

credentialProviderArn -\> (string)

> The Amazon Resource Name (ARN) of the OAuth2 credential provider.
>
> Constraints:
>
> - pattern: `arn:(aws|aws-us-gov):acps:[A-Za-z0-9-]{1,64}:[0-9]{12}:token-vault/[a-zA-Z0-9-.]+/oauth2credentialprovider/[a-zA-Z0-9-.]+`

callbackUrl -\> (string)

> Callback URL to register on the OAuth2 credential provider as an allowed callback URL. This URL is where the OAuth2 authorization server redirects users after they complete the authorization flow.

oauth2ProviderConfigOutput -\> (tagged union structure)

> Contains the output configuration for an OAuth2 provider.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `customOauth2ProviderConfig`, `googleOauth2ProviderConfig`, `githubOauth2ProviderConfig`, `slackOauth2ProviderConfig`, `salesforceOauth2ProviderConfig`, `microsoftOauth2ProviderConfig`, `atlassianOauth2ProviderConfig`, `linkedinOauth2ProviderConfig`, `includedOauth2ProviderConfig`.
>
> customOauth2ProviderConfig -\> (structure)
>
> > The output configuration for a custom OAuth2 provider.
> >
> > oauthDiscovery -\> (tagged union structure) \[required\]
> >
> > > The OAuth2 discovery information for the custom provider.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `discoveryUrl`, `authorizationServerMetadata`.
> > >
> > > discoveryUrl -\> (string)
> > >
> > > > The discovery URL for the OAuth2 provider.
> > > >
> > > > Constraints:
> > > >
> > > > - pattern: `.+/\.well-known/(openid-configuration|oauth-authorization-server)`
> > >
> > > authorizationServerMetadata -\> (structure)
> > >
> > > > The authorization server metadata for the OAuth2 provider.
> > > >
> > > > issuer -\> (string) \[required\]
> > > >
> > > > > The issuer URL for the OAuth2 authorization server.
> > > >
> > > > authorizationEndpoint -\> (string) \[required\]
> > > >
> > > > > The authorization endpoint URL for the OAuth2 authorization server.
> > > >
> > > > tokenEndpoint -\> (string) \[required\]
> > > >
> > > > > The token endpoint URL for the OAuth2 authorization server.
> > > >
> > > > responseTypes -\> (list)
> > > >
> > > > > The supported response types for the OAuth2 authorization server.
> > > > >
> > > > > (string)
> > > >
> > > > tokenEndpointAuthMethods -\> (list)
> > > >
> > > > > The authentication methods supported by the token endpoint. This specifies how clients can authenticate when requesting tokens from the authorization server.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `2`
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - pattern: `(client_secret_post|client_secret_basic)`
> >
> > clientId -\> (string)
> >
> > > The client ID for the custom OAuth2 provider.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `256`
> >
> > onBehalfOfTokenExchangeConfig -\> (structure)
> >
> > > The configuration for on-behalf-of token exchange.
> > >
> > > grantType -\> (string) \[required\]
> > >
> > > > The grant type for the on-behalf-of token exchange.
> > > >
> > > > Possible values:
> > > >
> > > > - `TOKEN_EXCHANGE`
> > > > - `JWT_AUTHORIZATION_GRANT`
> > >
> > > tokenExchangeGrantTypeConfig -\> (structure)
> > >
> > > > Configuration specific to the TOKEN_EXCHANGE grant type (RFC 8693).
> > > >
> > > > actorTokenContent -\> (string) \[required\]
> > > >
> > > > > The content type for the actor token in the token exchange.
> > > > >
> > > > > Possible values:
> > > > >
> > > > > - `NONE`
> > > > > - `M2M`
> > > > > - `AWS_IAM_ID_TOKEN_JWT`
> > > >
> > > > actorTokenScopes -\> (list)
> > > >
> > > > > The scopes for the actor token. Only valid when actorTokenContent is M2M.
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `128`
> >
> > clientAuthenticationMethod -\> (string)
> >
> > > The client authentication method used when authenticating with the token endpoint.
> > >
> > > Possible values:
> > >
> > > - `CLIENT_SECRET_BASIC`
> > > - `CLIENT_SECRET_POST`
> > > - `AWS_IAM_ID_TOKEN_JWT`
> > > - `PRIVATE_KEY_JWT`
> >
> > privateEndpoint -\> (tagged union structure)
> >
> > > The default private endpoint for the custom OAuth2 provider, enabling secure connectivity through a VPC Lattice resource configuration.
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
> > > The private endpoint overrides for the custom OAuth2 provider configuration.
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
> > privateKeyJwtConfig -\> (structure)
> >
> > > The configuration for private_key_jwt client authentication used by this OAuth2 credential provider.
> > >
> > > privateKeySource -\> (tagged union structure)
> > >
> > > > The private key source for the JWT client assertion.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `kmsKeySource`.
> > > >
> > > > kmsKeySource -\> (structure)
> > > >
> > > > > The KMS key source for the JWT client assertion.
> > > > >
> > > > > kmsKeyArn -\> (string) \[required\]
> > > > >
> > > > > > The Amazon Resource Name (ARN) of the KMS key used to sign the JWT client assertion. The key must be an asymmetric key with key usage SIGN_VERIFY and a key spec compatible with the configured signing algorithm.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `2048`
> > > > > > - pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`
> > >
> > > signingAlgorithm -\> (string)
> > >
> > > > The algorithm used to sign the JWT client assertion. Valid values are `RS256` , `PS256` , and `ES256` .
> > > >
> > > > Possible values:
> > > >
> > > > - `RS256`
> > > > - `PS256`
> > > > - `ES256`
> > >
> > > additionalHeaderClaims -\> (map)
> > >
> > > > A map of additional claims to include in the JWT client assertion header. Standard header claims such as `alg` and `typ` cannot be added.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `10`
> > > >
> > > > key -\> (string)
> > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `255`
> > > > > - pattern: `[A-Za-z0-9_.:#-]+`
> > > >
> > > > value -\> (string)
> > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `2048`
> > >
> > > additionalPayloadClaims -\> (map)
> > >
> > > > A map of additional claims to include in the JWT client assertion payload. Payload claims generated by the service, such as `iss` , `sub` , `jti` , and `exp` , cannot be added.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `10`
> > > >
> > > > key -\> (string)
> > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `255`
> > > > > - pattern: `[A-Za-z0-9_.:#-]+`
> > > >
> > > > value -\> (string)
> > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `2048`
>
> googleOauth2ProviderConfig -\> (structure)
>
> > The output configuration for a Google OAuth2 provider.
> >
> > oauthDiscovery -\> (tagged union structure) \[required\]
> >
> > > The OAuth2 discovery information for the Google provider.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `discoveryUrl`, `authorizationServerMetadata`.
> > >
> > > discoveryUrl -\> (string)
> > >
> > > > The discovery URL for the OAuth2 provider.
> > > >
> > > > Constraints:
> > > >
> > > > - pattern: `.+/\.well-known/(openid-configuration|oauth-authorization-server)`
> > >
> > > authorizationServerMetadata -\> (structure)
> > >
> > > > The authorization server metadata for the OAuth2 provider.
> > > >
> > > > issuer -\> (string) \[required\]
> > > >
> > > > > The issuer URL for the OAuth2 authorization server.
> > > >
> > > > authorizationEndpoint -\> (string) \[required\]
> > > >
> > > > > The authorization endpoint URL for the OAuth2 authorization server.
> > > >
> > > > tokenEndpoint -\> (string) \[required\]
> > > >
> > > > > The token endpoint URL for the OAuth2 authorization server.
> > > >
> > > > responseTypes -\> (list)
> > > >
> > > > > The supported response types for the OAuth2 authorization server.
> > > > >
> > > > > (string)
> > > >
> > > > tokenEndpointAuthMethods -\> (list)
> > > >
> > > > > The authentication methods supported by the token endpoint. This specifies how clients can authenticate when requesting tokens from the authorization server.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `2`
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - pattern: `(client_secret_post|client_secret_basic)`
> >
> > clientId -\> (string)
> >
> > > The client ID for the Google OAuth2 provider.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `256`
>
> githubOauth2ProviderConfig -\> (structure)
>
> > The output configuration for a GitHub OAuth2 provider.
> >
> > oauthDiscovery -\> (tagged union structure) \[required\]
> >
> > > The OAuth2 discovery information for the GitHub provider.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `discoveryUrl`, `authorizationServerMetadata`.
> > >
> > > discoveryUrl -\> (string)
> > >
> > > > The discovery URL for the OAuth2 provider.
> > > >
> > > > Constraints:
> > > >
> > > > - pattern: `.+/\.well-known/(openid-configuration|oauth-authorization-server)`
> > >
> > > authorizationServerMetadata -\> (structure)
> > >
> > > > The authorization server metadata for the OAuth2 provider.
> > > >
> > > > issuer -\> (string) \[required\]
> > > >
> > > > > The issuer URL for the OAuth2 authorization server.
> > > >
> > > > authorizationEndpoint -\> (string) \[required\]
> > > >
> > > > > The authorization endpoint URL for the OAuth2 authorization server.
> > > >
> > > > tokenEndpoint -\> (string) \[required\]
> > > >
> > > > > The token endpoint URL for the OAuth2 authorization server.
> > > >
> > > > responseTypes -\> (list)
> > > >
> > > > > The supported response types for the OAuth2 authorization server.
> > > > >
> > > > > (string)
> > > >
> > > > tokenEndpointAuthMethods -\> (list)
> > > >
> > > > > The authentication methods supported by the token endpoint. This specifies how clients can authenticate when requesting tokens from the authorization server.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `2`
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - pattern: `(client_secret_post|client_secret_basic)`
> >
> > clientId -\> (string)
> >
> > > The client ID for the GitHub OAuth2 provider.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `256`
>
> slackOauth2ProviderConfig -\> (structure)
>
> > The output configuration for a Slack OAuth2 provider.
> >
> > oauthDiscovery -\> (tagged union structure) \[required\]
> >
> > > The OAuth2 discovery information for the Slack provider.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `discoveryUrl`, `authorizationServerMetadata`.
> > >
> > > discoveryUrl -\> (string)
> > >
> > > > The discovery URL for the OAuth2 provider.
> > > >
> > > > Constraints:
> > > >
> > > > - pattern: `.+/\.well-known/(openid-configuration|oauth-authorization-server)`
> > >
> > > authorizationServerMetadata -\> (structure)
> > >
> > > > The authorization server metadata for the OAuth2 provider.
> > > >
> > > > issuer -\> (string) \[required\]
> > > >
> > > > > The issuer URL for the OAuth2 authorization server.
> > > >
> > > > authorizationEndpoint -\> (string) \[required\]
> > > >
> > > > > The authorization endpoint URL for the OAuth2 authorization server.
> > > >
> > > > tokenEndpoint -\> (string) \[required\]
> > > >
> > > > > The token endpoint URL for the OAuth2 authorization server.
> > > >
> > > > responseTypes -\> (list)
> > > >
> > > > > The supported response types for the OAuth2 authorization server.
> > > > >
> > > > > (string)
> > > >
> > > > tokenEndpointAuthMethods -\> (list)
> > > >
> > > > > The authentication methods supported by the token endpoint. This specifies how clients can authenticate when requesting tokens from the authorization server.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `2`
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - pattern: `(client_secret_post|client_secret_basic)`
> >
> > clientId -\> (string)
> >
> > > The client ID for the Slack OAuth2 provider.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `256`
>
> salesforceOauth2ProviderConfig -\> (structure)
>
> > The output configuration for a Salesforce OAuth2 provider.
> >
> > oauthDiscovery -\> (tagged union structure) \[required\]
> >
> > > The OAuth2 discovery information for the Salesforce provider.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `discoveryUrl`, `authorizationServerMetadata`.
> > >
> > > discoveryUrl -\> (string)
> > >
> > > > The discovery URL for the OAuth2 provider.
> > > >
> > > > Constraints:
> > > >
> > > > - pattern: `.+/\.well-known/(openid-configuration|oauth-authorization-server)`
> > >
> > > authorizationServerMetadata -\> (structure)
> > >
> > > > The authorization server metadata for the OAuth2 provider.
> > > >
> > > > issuer -\> (string) \[required\]
> > > >
> > > > > The issuer URL for the OAuth2 authorization server.
> > > >
> > > > authorizationEndpoint -\> (string) \[required\]
> > > >
> > > > > The authorization endpoint URL for the OAuth2 authorization server.
> > > >
> > > > tokenEndpoint -\> (string) \[required\]
> > > >
> > > > > The token endpoint URL for the OAuth2 authorization server.
> > > >
> > > > responseTypes -\> (list)
> > > >
> > > > > The supported response types for the OAuth2 authorization server.
> > > > >
> > > > > (string)
> > > >
> > > > tokenEndpointAuthMethods -\> (list)
> > > >
> > > > > The authentication methods supported by the token endpoint. This specifies how clients can authenticate when requesting tokens from the authorization server.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `2`
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - pattern: `(client_secret_post|client_secret_basic)`
> >
> > clientId -\> (string)
> >
> > > The client ID for the Salesforce OAuth2 provider.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `256`
>
> microsoftOauth2ProviderConfig -\> (structure)
>
> > The output configuration for a Microsoft OAuth2 provider.
> >
> > oauthDiscovery -\> (tagged union structure) \[required\]
> >
> > > The OAuth2 discovery information for the Microsoft provider.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `discoveryUrl`, `authorizationServerMetadata`.
> > >
> > > discoveryUrl -\> (string)
> > >
> > > > The discovery URL for the OAuth2 provider.
> > > >
> > > > Constraints:
> > > >
> > > > - pattern: `.+/\.well-known/(openid-configuration|oauth-authorization-server)`
> > >
> > > authorizationServerMetadata -\> (structure)
> > >
> > > > The authorization server metadata for the OAuth2 provider.
> > > >
> > > > issuer -\> (string) \[required\]
> > > >
> > > > > The issuer URL for the OAuth2 authorization server.
> > > >
> > > > authorizationEndpoint -\> (string) \[required\]
> > > >
> > > > > The authorization endpoint URL for the OAuth2 authorization server.
> > > >
> > > > tokenEndpoint -\> (string) \[required\]
> > > >
> > > > > The token endpoint URL for the OAuth2 authorization server.
> > > >
> > > > responseTypes -\> (list)
> > > >
> > > > > The supported response types for the OAuth2 authorization server.
> > > > >
> > > > > (string)
> > > >
> > > > tokenEndpointAuthMethods -\> (list)
> > > >
> > > > > The authentication methods supported by the token endpoint. This specifies how clients can authenticate when requesting tokens from the authorization server.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `2`
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - pattern: `(client_secret_post|client_secret_basic)`
> >
> > clientId -\> (string)
> >
> > > The client ID for the Microsoft OAuth2 provider.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `256`
>
> atlassianOauth2ProviderConfig -\> (structure)
>
> > The configuration details for the Atlassian OAuth2 provider.
> >
> > oauthDiscovery -\> (tagged union structure) \[required\]
> >
> > > Contains the discovery information for an OAuth2 provider.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `discoveryUrl`, `authorizationServerMetadata`.
> > >
> > > discoveryUrl -\> (string)
> > >
> > > > The discovery URL for the OAuth2 provider.
> > > >
> > > > Constraints:
> > > >
> > > > - pattern: `.+/\.well-known/(openid-configuration|oauth-authorization-server)`
> > >
> > > authorizationServerMetadata -\> (structure)
> > >
> > > > The authorization server metadata for the OAuth2 provider.
> > > >
> > > > issuer -\> (string) \[required\]
> > > >
> > > > > The issuer URL for the OAuth2 authorization server.
> > > >
> > > > authorizationEndpoint -\> (string) \[required\]
> > > >
> > > > > The authorization endpoint URL for the OAuth2 authorization server.
> > > >
> > > > tokenEndpoint -\> (string) \[required\]
> > > >
> > > > > The token endpoint URL for the OAuth2 authorization server.
> > > >
> > > > responseTypes -\> (list)
> > > >
> > > > > The supported response types for the OAuth2 authorization server.
> > > > >
> > > > > (string)
> > > >
> > > > tokenEndpointAuthMethods -\> (list)
> > > >
> > > > > The authentication methods supported by the token endpoint. This specifies how clients can authenticate when requesting tokens from the authorization server.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `2`
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - pattern: `(client_secret_post|client_secret_basic)`
> >
> > clientId -\> (string)
> >
> > > The client ID for the Atlassian OAuth2 provider.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `256`
>
> linkedinOauth2ProviderConfig -\> (structure)
>
> > The configuration details for the LinkedIn OAuth2 provider.
> >
> > oauthDiscovery -\> (tagged union structure) \[required\]
> >
> > > Contains the discovery information for an OAuth2 provider.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `discoveryUrl`, `authorizationServerMetadata`.
> > >
> > > discoveryUrl -\> (string)
> > >
> > > > The discovery URL for the OAuth2 provider.
> > > >
> > > > Constraints:
> > > >
> > > > - pattern: `.+/\.well-known/(openid-configuration|oauth-authorization-server)`
> > >
> > > authorizationServerMetadata -\> (structure)
> > >
> > > > The authorization server metadata for the OAuth2 provider.
> > > >
> > > > issuer -\> (string) \[required\]
> > > >
> > > > > The issuer URL for the OAuth2 authorization server.
> > > >
> > > > authorizationEndpoint -\> (string) \[required\]
> > > >
> > > > > The authorization endpoint URL for the OAuth2 authorization server.
> > > >
> > > > tokenEndpoint -\> (string) \[required\]
> > > >
> > > > > The token endpoint URL for the OAuth2 authorization server.
> > > >
> > > > responseTypes -\> (list)
> > > >
> > > > > The supported response types for the OAuth2 authorization server.
> > > > >
> > > > > (string)
> > > >
> > > > tokenEndpointAuthMethods -\> (list)
> > > >
> > > > > The authentication methods supported by the token endpoint. This specifies how clients can authenticate when requesting tokens from the authorization server.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `2`
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - pattern: `(client_secret_post|client_secret_basic)`
> >
> > clientId -\> (string)
> >
> > > The client ID for the LinkedIn OAuth2 provider.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `256`
>
> includedOauth2ProviderConfig -\> (structure)
>
> > The configuration for a non-custom OAuth2 provider. This includes the configuration details for supported OAuth2 providers that have built-in integration support.
> >
> > oauthDiscovery -\> (tagged union structure) \[required\]
> >
> > > Contains the discovery information for an OAuth2 provider.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `discoveryUrl`, `authorizationServerMetadata`.
> > >
> > > discoveryUrl -\> (string)
> > >
> > > > The discovery URL for the OAuth2 provider.
> > > >
> > > > Constraints:
> > > >
> > > > - pattern: `.+/\.well-known/(openid-configuration|oauth-authorization-server)`
> > >
> > > authorizationServerMetadata -\> (structure)
> > >
> > > > The authorization server metadata for the OAuth2 provider.
> > > >
> > > > issuer -\> (string) \[required\]
> > > >
> > > > > The issuer URL for the OAuth2 authorization server.
> > > >
> > > > authorizationEndpoint -\> (string) \[required\]
> > > >
> > > > > The authorization endpoint URL for the OAuth2 authorization server.
> > > >
> > > > tokenEndpoint -\> (string) \[required\]
> > > >
> > > > > The token endpoint URL for the OAuth2 authorization server.
> > > >
> > > > responseTypes -\> (list)
> > > >
> > > > > The supported response types for the OAuth2 authorization server.
> > > > >
> > > > > (string)
> > > >
> > > > tokenEndpointAuthMethods -\> (list)
> > > >
> > > > > The authentication methods supported by the token endpoint. This specifies how clients can authenticate when requesting tokens from the authorization server.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `2`
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - pattern: `(client_secret_post|client_secret_basic)`
> >
> > clientId -\> (string)
> >
> > > The client ID for the supported OAuth2 provider.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `256`

status -\> (string)

> The current status of the OAuth2 credential provider.
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

- [← create-memory](create-memory.html "previous chapter (use the left arrow)") /
- [create-online-evaluation-config →](create-online-evaluation-config.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](create-online-evaluation-config.html "create-online-evaluation-config") \|
- [previous](create-memory.html "create-memory") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [create-oauth2-credential-provider]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

---
title: aws agent-registry-control update-registry-record
description: \ [aws . agent-registry-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / agent-registry-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/agent-registry-control/update-registry-record.html
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

# update-registry-record

## Description

Updates a registry record. The update is asynchronous: the record is returned with the UPDATING status while it is processed. Fields that use update wrappers follow PATCH semantics: omit the field to leave it unchanged.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/agent-registry-control-2025-12-01/UpdateRegistryRecord)

## Synopsis

      update-registry-record
    --registry-id <value>
    --record-id <value>
    [--name <value>]
    [--display-name <value>]
    [--description <value>]
    [--record-type <value>]
    [--descriptors <value>]
    [--record-version <value>]
    [--trigger-synchronization | --no-trigger-synchronization]
    [--provenance <value>]
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

`--registry-id` (string) \[required\]

> The identifier of the registry containing the record (ARN or ID)
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`

`--record-id` (string) \[required\]

> The identifier of the registry record to update (ARN or ID)
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `(arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/)?[a-zA-Z0-9]{12}`

`--name` (string)

> The updated name of the registry record. Omit to leave the name unchanged.
>
> Constraints:
>
> - min: `1`
> - max: `255`
> - pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`

`--display-name` (structure)

> The updated display name of the registry record. Omit to leave the display name unchanged; provide an empty wrapper to unset it.
>
> optionalValue -\> (string)
>
> > The value to set for this field. Omit the wrapper to leave the field unchanged.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `255`

Shorthand Syntax:

    optionalValue=string

JSON Syntax:

    {
      "optionalValue": "string"
    }

`--description` (structure)

> The updated description of the registry record. Omit to leave the description unchanged; provide an empty wrapper to unset it.
>
> optionalValue -\> (string)
>
> > The value to set for this field. Omit the wrapper to leave the field unchanged.
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

`--record-type` (string)

> The updated type of the registry record. Omit to leave the record type unchanged.
>
> Possible values:
>
> - `MCP`
> - `AGENT`
> - `CUSTOM`
> - `SKILL`
> - `GATEWAY`

`--descriptors` (structure)

> The updated typed descriptor content for the registry record. Omit to leave the descriptors unchanged.
>
> optionalValue -\> (structure)
>
> > The value to set for this field. Omit the wrapper to leave the field unchanged.
> >
> > mcpServer -\> (structure)
> >
> > > The patch for the MCP server descriptor.
> > >
> > > optionalValue -\> (structure)
> > >
> > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > >
> > > > data -\> (structure)
> > > >
> > > > > The patch for the descriptor’s data field.
> > > > >
> > > > > optionalValue -\> (string)
> > > > >
> > > > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `102400`
> > > >
> > > > dataSchemaVersion -\> (structure)
> > > >
> > > > > The patch for the descriptor’s data schema version field.
> > > > >
> > > > > optionalValue -\> (string)
> > > > >
> > > > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `255`
> > > >
> > > > source -\> (structure)
> > > >
> > > > > The patch for the descriptor’s source field.
> > > > >
> > > > > optionalValue -\> (structure)
> > > > >
> > > > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > > > >
> > > > > > fromUrl -\> (structure)
> > > > > >
> > > > > > > URL-based descriptor source, populated when descriptor content is synchronized from a URL.
> > > > > > >
> > > > > > > url -\> (string) \[required\]
> > > > > > >
> > > > > > > > The URL from which the descriptor content is retrieved.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `2048`
> > > > > > > > - pattern: `https://.*`
> > > > > > >
> > > > > > > credentialProviderConfigurations -\> (list)
> > > > > > >
> > > > > > > > The credential providers used to authenticate when fetching descriptor content from the source URL.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `0`
> > > > > > > > - max: `1`
> > > > > > > >
> > > > > > > > (structure)
> > > > > > > >
> > > > > > > > > A credential provider configuration that specifies how to authenticate when fetching descriptor content from a registry record’s source URL.
> > > > > > > > >
> > > > > > > > > credentialProviderType -\> (string) \[required\]
> > > > > > > > >
> > > > > > > > > > The type of credential provider.
> > > > > > > > > >
> > > > > > > > > > Possible values:
> > > > > > > > > >
> > > > > > > > > > - `OAUTH`
> > > > > > > > > > - `IAM`
> > > > > > > > >
> > > > > > > > > credentialProvider -\> (tagged union structure) \[required\]
> > > > > > > > >
> > > > > > > > > > The credential provider details corresponding to the specified credential provider type.
> > > > > > > > > >
> > > > > > > > > > ### Note
> > > > > > > > > >
> > > > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `oauthCredentialProvider`, `iamCredentialProvider`.
> > > > > > > > > >
> > > > > > > > > > oauthCredentialProvider -\> (structure)
> > > > > > > > > >
> > > > > > > > > > > The OAuth 2.0 credential provider details.
> > > > > > > > > > >
> > > > > > > > > > > providerArn -\> (string) \[required\]
> > > > > > > > > > >
> > > > > > > > > > > > The Amazon Resource Name (ARN) of the OAuth 2.0 credential provider resource in Amazon Bedrock AgentCore Identity.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > - max: `2048`
> > > > > > > > > > > > - pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:.*`
> > > > > > > > > > >
> > > > > > > > > > > grantType -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > The OAuth 2.0 grant type used to obtain access tokens.
> > > > > > > > > > > >
> > > > > > > > > > > > Possible values:
> > > > > > > > > > > >
> > > > > > > > > > > > - `CLIENT_CREDENTIALS`
> > > > > > > > > > >
> > > > > > > > > > > scopes -\> (list)
> > > > > > > > > > >
> > > > > > > > > > > > The OAuth 2.0 scopes to request when obtaining access tokens.
> > > > > > > > > > > >
> > > > > > > > > > > > (string)
> > > > > > > > > > >
> > > > > > > > > > > customParameters -\> (map)
> > > > > > > > > > >
> > > > > > > > > > > > Additional parameters to include in the OAuth 2.0 token request.
> > > > > > > > > > > >
> > > > > > > > > > > > key -\> (string)
> > > > > > > > > > > >
> > > > > > > > > > > > value -\> (string)
> > > > > > > > > >
> > > > > > > > > > iamCredentialProvider -\> (structure)
> > > > > > > > > >
> > > > > > > > > > > The IAM role credential provider details.
> > > > > > > > > > >
> > > > > > > > > > > roleArn -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > The Amazon Resource Name (ARN) of the IAM role to assume for request signing.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `20`
> > > > > > > > > > > > - max: `2048`
> > > > > > > > > > > > - pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
> > > > > > > > > > >
> > > > > > > > > > > service -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > The service name to use for request signing, such as execute-api.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > - max: `128`
> > > > > > > > > > > > - pattern: `[a-zA-Z0-9_-]+`
> > > > > > > > > > >
> > > > > > > > > > > region -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > The Amazon Web Services Region to use for request signing. If not specified, the Region is derived from the source URL hostname, falling back to the Region of the registry.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > - max: `64`
> > > > > > > > > > > > - pattern: `[a-z0-9-]+`
> > > >
> > > > additionalData -\> (structure)
> > > >
> > > > > The patch for the descriptor’s additional data field.
> > > > >
> > > > > optionalValue -\> (structure)
> > > > >
> > > > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > > > >
> > > > > > tools -\> (structure)
> > > > > >
> > > > > > > The patch for the MCP tools descriptor field.
> > > > > > >
> > > > > > > optionalValue -\> (structure)
> > > > > > >
> > > > > > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > > > > > >
> > > > > > > > data -\> (structure)
> > > > > > > >
> > > > > > > > > The patch for the descriptor’s data field.
> > > > > > > > >
> > > > > > > > > optionalValue -\> (string)
> > > > > > > > >
> > > > > > > > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > > > > > > > >
> > > > > > > > > > Constraints:
> > > > > > > > > >
> > > > > > > > > > - min: `1`
> > > > > > > > > > - max: `102400`
> > > > > > > >
> > > > > > > > dataSchemaVersion -\> (structure)
> > > > > > > >
> > > > > > > > > The patch for the descriptor’s data schema version field.
> > > > > > > > >
> > > > > > > > > optionalValue -\> (string)
> > > > > > > > >
> > > > > > > > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > > > > > > > >
> > > > > > > > > > Constraints:
> > > > > > > > > >
> > > > > > > > > > - min: `1`
> > > > > > > > > > - max: `255`
> >
> > a2aAgentCard -\> (structure)
> >
> > > The patch for the A2A agent card descriptor.
> > >
> > > optionalValue -\> (structure)
> > >
> > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > >
> > > > data -\> (structure)
> > > >
> > > > > The patch for the descriptor’s data field.
> > > > >
> > > > > optionalValue -\> (string)
> > > > >
> > > > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `102400`
> > > >
> > > > dataSchemaVersion -\> (structure)
> > > >
> > > > > The patch for the descriptor’s data schema version field.
> > > > >
> > > > > optionalValue -\> (string)
> > > > >
> > > > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `255`
> > > >
> > > > source -\> (structure)
> > > >
> > > > > The patch for the descriptor’s source field.
> > > > >
> > > > > optionalValue -\> (structure)
> > > > >
> > > > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > > > >
> > > > > > fromUrl -\> (structure)
> > > > > >
> > > > > > > URL-based descriptor source, populated when descriptor content is synchronized from a URL.
> > > > > > >
> > > > > > > url -\> (string) \[required\]
> > > > > > >
> > > > > > > > The URL from which the descriptor content is retrieved.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `2048`
> > > > > > > > - pattern: `https://.*`
> > > > > > >
> > > > > > > credentialProviderConfigurations -\> (list)
> > > > > > >
> > > > > > > > The credential providers used to authenticate when fetching descriptor content from the source URL.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `0`
> > > > > > > > - max: `1`
> > > > > > > >
> > > > > > > > (structure)
> > > > > > > >
> > > > > > > > > A credential provider configuration that specifies how to authenticate when fetching descriptor content from a registry record’s source URL.
> > > > > > > > >
> > > > > > > > > credentialProviderType -\> (string) \[required\]
> > > > > > > > >
> > > > > > > > > > The type of credential provider.
> > > > > > > > > >
> > > > > > > > > > Possible values:
> > > > > > > > > >
> > > > > > > > > > - `OAUTH`
> > > > > > > > > > - `IAM`
> > > > > > > > >
> > > > > > > > > credentialProvider -\> (tagged union structure) \[required\]
> > > > > > > > >
> > > > > > > > > > The credential provider details corresponding to the specified credential provider type.
> > > > > > > > > >
> > > > > > > > > > ### Note
> > > > > > > > > >
> > > > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `oauthCredentialProvider`, `iamCredentialProvider`.
> > > > > > > > > >
> > > > > > > > > > oauthCredentialProvider -\> (structure)
> > > > > > > > > >
> > > > > > > > > > > The OAuth 2.0 credential provider details.
> > > > > > > > > > >
> > > > > > > > > > > providerArn -\> (string) \[required\]
> > > > > > > > > > >
> > > > > > > > > > > > The Amazon Resource Name (ARN) of the OAuth 2.0 credential provider resource in Amazon Bedrock AgentCore Identity.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > - max: `2048`
> > > > > > > > > > > > - pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:.*`
> > > > > > > > > > >
> > > > > > > > > > > grantType -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > The OAuth 2.0 grant type used to obtain access tokens.
> > > > > > > > > > > >
> > > > > > > > > > > > Possible values:
> > > > > > > > > > > >
> > > > > > > > > > > > - `CLIENT_CREDENTIALS`
> > > > > > > > > > >
> > > > > > > > > > > scopes -\> (list)
> > > > > > > > > > >
> > > > > > > > > > > > The OAuth 2.0 scopes to request when obtaining access tokens.
> > > > > > > > > > > >
> > > > > > > > > > > > (string)
> > > > > > > > > > >
> > > > > > > > > > > customParameters -\> (map)
> > > > > > > > > > >
> > > > > > > > > > > > Additional parameters to include in the OAuth 2.0 token request.
> > > > > > > > > > > >
> > > > > > > > > > > > key -\> (string)
> > > > > > > > > > > >
> > > > > > > > > > > > value -\> (string)
> > > > > > > > > >
> > > > > > > > > > iamCredentialProvider -\> (structure)
> > > > > > > > > >
> > > > > > > > > > > The IAM role credential provider details.
> > > > > > > > > > >
> > > > > > > > > > > roleArn -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > The Amazon Resource Name (ARN) of the IAM role to assume for request signing.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `20`
> > > > > > > > > > > > - max: `2048`
> > > > > > > > > > > > - pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
> > > > > > > > > > >
> > > > > > > > > > > service -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > The service name to use for request signing, such as execute-api.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > - max: `128`
> > > > > > > > > > > > - pattern: `[a-zA-Z0-9_-]+`
> > > > > > > > > > >
> > > > > > > > > > > region -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > The Amazon Web Services Region to use for request signing. If not specified, the Region is derived from the source URL hostname, falling back to the Region of the registry.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > - max: `64`
> > > > > > > > > > > > - pattern: `[a-z0-9-]+`
> >
> > agentSkillsDefinition -\> (structure)
> >
> > > The patch for the agent skills definition descriptor.
> > >
> > > optionalValue -\> (structure)
> > >
> > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > >
> > > > data -\> (structure)
> > > >
> > > > > The patch for the descriptor’s data field.
> > > > >
> > > > > optionalValue -\> (string)
> > > > >
> > > > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `102400`
> > > >
> > > > dataSchemaVersion -\> (structure)
> > > >
> > > > > The patch for the descriptor’s data schema version field.
> > > > >
> > > > > optionalValue -\> (string)
> > > > >
> > > > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `255`
> > > >
> > > > additionalData -\> (structure)
> > > >
> > > > > The patch for the descriptor’s additional data field.
> > > > >
> > > > > optionalValue -\> (structure)
> > > > >
> > > > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > > > >
> > > > > > skillMd -\> (structure)
> > > > > >
> > > > > > > The patch for the agent skills markdown descriptor field.
> > > > > > >
> > > > > > > optionalValue -\> (structure)
> > > > > > >
> > > > > > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > > > > > >
> > > > > > > > data -\> (structure)
> > > > > > > >
> > > > > > > > > The patch for the descriptor’s data field.
> > > > > > > > >
> > > > > > > > > optionalValue -\> (string)
> > > > > > > > >
> > > > > > > > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > > > > > > > >
> > > > > > > > > > Constraints:
> > > > > > > > > >
> > > > > > > > > > - min: `1`
> > > > > > > > > > - max: `102400`
> > > > > > > >
> > > > > > > > dataSchemaVersion -\> (structure)
> > > > > > > >
> > > > > > > > > The patch for the descriptor’s data schema version field.
> > > > > > > > >
> > > > > > > > > optionalValue -\> (string)
> > > > > > > > >
> > > > > > > > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > > > > > > > >
> > > > > > > > > > Constraints:
> > > > > > > > > >
> > > > > > > > > > - min: `1`
> > > > > > > > > > - max: `255`
> > > > > > > >
> > > > > > > > source -\> (structure)
> > > > > > > >
> > > > > > > > > The patch for the descriptor’s source field.
> > > > > > > > >
> > > > > > > > > optionalValue -\> (structure)
> > > > > > > > >
> > > > > > > > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > > > > > > > >
> > > > > > > > > > fromUrl -\> (structure)
> > > > > > > > > >
> > > > > > > > > > > URL-based descriptor source, populated when descriptor content is synchronized from a URL.
> > > > > > > > > > >
> > > > > > > > > > > url -\> (string) \[required\]
> > > > > > > > > > >
> > > > > > > > > > > > The URL from which the descriptor content is retrieved.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > - max: `2048`
> > > > > > > > > > > > - pattern: `https://.*`
> > > > > > > > > > >
> > > > > > > > > > > credentialProviderConfigurations -\> (list)
> > > > > > > > > > >
> > > > > > > > > > > > The credential providers used to authenticate when fetching descriptor content from the source URL.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `0`
> > > > > > > > > > > > - max: `1`
> > > > > > > > > > > >
> > > > > > > > > > > > (structure)
> > > > > > > > > > > >
> > > > > > > > > > > > > A credential provider configuration that specifies how to authenticate when fetching descriptor content from a registry record’s source URL.
> > > > > > > > > > > > >
> > > > > > > > > > > > > credentialProviderType -\> (string) \[required\]
> > > > > > > > > > > > >
> > > > > > > > > > > > > > The type of credential provider.
> > > > > > > > > > > > > >
> > > > > > > > > > > > > > Possible values:
> > > > > > > > > > > > > >
> > > > > > > > > > > > > > - `OAUTH`
> > > > > > > > > > > > > > - `IAM`
> > > > > > > > > > > > >
> > > > > > > > > > > > > credentialProvider -\> (tagged union structure) \[required\]
> > > > > > > > > > > > >
> > > > > > > > > > > > > > The credential provider details corresponding to the specified credential provider type.
> > > > > > > > > > > > > >
> > > > > > > > > > > > > > ### Note
> > > > > > > > > > > > > >
> > > > > > > > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `oauthCredentialProvider`, `iamCredentialProvider`.
> > > > > > > > > > > > > >
> > > > > > > > > > > > > > oauthCredentialProvider -\> (structure)
> > > > > > > > > > > > > >
> > > > > > > > > > > > > > > The OAuth 2.0 credential provider details.
> > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > providerArn -\> (string) \[required\]
> > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > > The Amazon Resource Name (ARN) of the OAuth 2.0 credential provider resource in Amazon Bedrock AgentCore Identity.
> > > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > > Constraints:
> > > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > > > > > - max: `2048`
> > > > > > > > > > > > > > > > - pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:.*`
> > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > grantType -\> (string)
> > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > > The OAuth 2.0 grant type used to obtain access tokens.
> > > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > > Possible values:
> > > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > > - `CLIENT_CREDENTIALS`
> > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > scopes -\> (list)
> > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > > The OAuth 2.0 scopes to request when obtaining access tokens.
> > > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > > (string)
> > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > customParameters -\> (map)
> > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > > Additional parameters to include in the OAuth 2.0 token request.
> > > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > > key -\> (string)
> > > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > > value -\> (string)
> > > > > > > > > > > > > >
> > > > > > > > > > > > > > iamCredentialProvider -\> (structure)
> > > > > > > > > > > > > >
> > > > > > > > > > > > > > > The IAM role credential provider details.
> > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > roleArn -\> (string)
> > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > > The Amazon Resource Name (ARN) of the IAM role to assume for request signing.
> > > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > > Constraints:
> > > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > > - min: `20`
> > > > > > > > > > > > > > > > - max: `2048`
> > > > > > > > > > > > > > > > - pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
> > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > service -\> (string)
> > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > > The service name to use for request signing, such as execute-api.
> > > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > > Constraints:
> > > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > > > > > - max: `128`
> > > > > > > > > > > > > > > > - pattern: `[a-zA-Z0-9_-]+`
> > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > region -\> (string)
> > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > > The Amazon Web Services Region to use for request signing. If not specified, the Region is derived from the source URL hostname, falling back to the Region of the registry.
> > > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > > Constraints:
> > > > > > > > > > > > > > > >
> > > > > > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > > > > > - max: `64`
> > > > > > > > > > > > > > > > - pattern: `[a-z0-9-]+`
> >
> > custom -\> (structure)
> >
> > > The patch for the custom descriptor.
> > >
> > > optionalValue -\> (structure)
> > >
> > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > >
> > > > data -\> (structure)
> > > >
> > > > > The patch for the descriptor’s data field.
> > > > >
> > > > > optionalValue -\> (string)
> > > > >
> > > > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `102400`
> >
> > http -\> (structure)
> >
> > > The patch for the HTTP descriptor.
> > >
> > > optionalValue -\> (structure)
> > >
> > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > >
> > > > source -\> (structure)
> > > >
> > > > > The patch for the descriptor’s source field.
> > > > >
> > > > > optionalValue -\> (structure)
> > > > >
> > > > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > > > >
> > > > > > fromUrl -\> (structure)
> > > > > >
> > > > > > > URL-based descriptor source, populated when descriptor content is synchronized from a URL.
> > > > > > >
> > > > > > > url -\> (string) \[required\]
> > > > > > >
> > > > > > > > The URL from which the descriptor content is retrieved.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `2048`
> > > > > > > > - pattern: `https://.*`
> > > > > > >
> > > > > > > credentialProviderConfigurations -\> (list)
> > > > > > >
> > > > > > > > The credential providers used to authenticate when fetching descriptor content from the source URL.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `0`
> > > > > > > > - max: `1`
> > > > > > > >
> > > > > > > > (structure)
> > > > > > > >
> > > > > > > > > A credential provider configuration that specifies how to authenticate when fetching descriptor content from a registry record’s source URL.
> > > > > > > > >
> > > > > > > > > credentialProviderType -\> (string) \[required\]
> > > > > > > > >
> > > > > > > > > > The type of credential provider.
> > > > > > > > > >
> > > > > > > > > > Possible values:
> > > > > > > > > >
> > > > > > > > > > - `OAUTH`
> > > > > > > > > > - `IAM`
> > > > > > > > >
> > > > > > > > > credentialProvider -\> (tagged union structure) \[required\]
> > > > > > > > >
> > > > > > > > > > The credential provider details corresponding to the specified credential provider type.
> > > > > > > > > >
> > > > > > > > > > ### Note
> > > > > > > > > >
> > > > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `oauthCredentialProvider`, `iamCredentialProvider`.
> > > > > > > > > >
> > > > > > > > > > oauthCredentialProvider -\> (structure)
> > > > > > > > > >
> > > > > > > > > > > The OAuth 2.0 credential provider details.
> > > > > > > > > > >
> > > > > > > > > > > providerArn -\> (string) \[required\]
> > > > > > > > > > >
> > > > > > > > > > > > The Amazon Resource Name (ARN) of the OAuth 2.0 credential provider resource in Amazon Bedrock AgentCore Identity.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > - max: `2048`
> > > > > > > > > > > > - pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:.*`
> > > > > > > > > > >
> > > > > > > > > > > grantType -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > The OAuth 2.0 grant type used to obtain access tokens.
> > > > > > > > > > > >
> > > > > > > > > > > > Possible values:
> > > > > > > > > > > >
> > > > > > > > > > > > - `CLIENT_CREDENTIALS`
> > > > > > > > > > >
> > > > > > > > > > > scopes -\> (list)
> > > > > > > > > > >
> > > > > > > > > > > > The OAuth 2.0 scopes to request when obtaining access tokens.
> > > > > > > > > > > >
> > > > > > > > > > > > (string)
> > > > > > > > > > >
> > > > > > > > > > > customParameters -\> (map)
> > > > > > > > > > >
> > > > > > > > > > > > Additional parameters to include in the OAuth 2.0 token request.
> > > > > > > > > > > >
> > > > > > > > > > > > key -\> (string)
> > > > > > > > > > > >
> > > > > > > > > > > > value -\> (string)
> > > > > > > > > >
> > > > > > > > > > iamCredentialProvider -\> (structure)
> > > > > > > > > >
> > > > > > > > > > > The IAM role credential provider details.
> > > > > > > > > > >
> > > > > > > > > > > roleArn -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > The Amazon Resource Name (ARN) of the IAM role to assume for request signing.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `20`
> > > > > > > > > > > > - max: `2048`
> > > > > > > > > > > > - pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
> > > > > > > > > > >
> > > > > > > > > > > service -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > The service name to use for request signing, such as execute-api.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > - max: `128`
> > > > > > > > > > > > - pattern: `[a-zA-Z0-9_-]+`
> > > > > > > > > > >
> > > > > > > > > > > region -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > The Amazon Web Services Region to use for request signing. If not specified, the Region is derived from the source URL hostname, falling back to the Region of the registry.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > - max: `64`
> > > > > > > > > > > > - pattern: `[a-z0-9-]+`
> >
> > agui -\> (structure)
> >
> > > The patch for the AG-UI descriptor.
> > >
> > > optionalValue -\> (structure)
> > >
> > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > >
> > > > source -\> (structure)
> > > >
> > > > > The patch for the descriptor’s source field.
> > > > >
> > > > > optionalValue -\> (structure)
> > > > >
> > > > > > The value to set for this field. Omit the wrapper to leave the field unchanged.
> > > > > >
> > > > > > fromUrl -\> (structure)
> > > > > >
> > > > > > > URL-based descriptor source, populated when descriptor content is synchronized from a URL.
> > > > > > >
> > > > > > > url -\> (string) \[required\]
> > > > > > >
> > > > > > > > The URL from which the descriptor content is retrieved.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `2048`
> > > > > > > > - pattern: `https://.*`
> > > > > > >
> > > > > > > credentialProviderConfigurations -\> (list)
> > > > > > >
> > > > > > > > The credential providers used to authenticate when fetching descriptor content from the source URL.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `0`
> > > > > > > > - max: `1`
> > > > > > > >
> > > > > > > > (structure)
> > > > > > > >
> > > > > > > > > A credential provider configuration that specifies how to authenticate when fetching descriptor content from a registry record’s source URL.
> > > > > > > > >
> > > > > > > > > credentialProviderType -\> (string) \[required\]
> > > > > > > > >
> > > > > > > > > > The type of credential provider.
> > > > > > > > > >
> > > > > > > > > > Possible values:
> > > > > > > > > >
> > > > > > > > > > - `OAUTH`
> > > > > > > > > > - `IAM`
> > > > > > > > >
> > > > > > > > > credentialProvider -\> (tagged union structure) \[required\]
> > > > > > > > >
> > > > > > > > > > The credential provider details corresponding to the specified credential provider type.
> > > > > > > > > >
> > > > > > > > > > ### Note
> > > > > > > > > >
> > > > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `oauthCredentialProvider`, `iamCredentialProvider`.
> > > > > > > > > >
> > > > > > > > > > oauthCredentialProvider -\> (structure)
> > > > > > > > > >
> > > > > > > > > > > The OAuth 2.0 credential provider details.
> > > > > > > > > > >
> > > > > > > > > > > providerArn -\> (string) \[required\]
> > > > > > > > > > >
> > > > > > > > > > > > The Amazon Resource Name (ARN) of the OAuth 2.0 credential provider resource in Amazon Bedrock AgentCore Identity.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > - max: `2048`
> > > > > > > > > > > > - pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:.*`
> > > > > > > > > > >
> > > > > > > > > > > grantType -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > The OAuth 2.0 grant type used to obtain access tokens.
> > > > > > > > > > > >
> > > > > > > > > > > > Possible values:
> > > > > > > > > > > >
> > > > > > > > > > > > - `CLIENT_CREDENTIALS`
> > > > > > > > > > >
> > > > > > > > > > > scopes -\> (list)
> > > > > > > > > > >
> > > > > > > > > > > > The OAuth 2.0 scopes to request when obtaining access tokens.
> > > > > > > > > > > >
> > > > > > > > > > > > (string)
> > > > > > > > > > >
> > > > > > > > > > > customParameters -\> (map)
> > > > > > > > > > >
> > > > > > > > > > > > Additional parameters to include in the OAuth 2.0 token request.
> > > > > > > > > > > >
> > > > > > > > > > > > key -\> (string)
> > > > > > > > > > > >
> > > > > > > > > > > > value -\> (string)
> > > > > > > > > >
> > > > > > > > > > iamCredentialProvider -\> (structure)
> > > > > > > > > >
> > > > > > > > > > > The IAM role credential provider details.
> > > > > > > > > > >
> > > > > > > > > > > roleArn -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > The Amazon Resource Name (ARN) of the IAM role to assume for request signing.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `20`
> > > > > > > > > > > > - max: `2048`
> > > > > > > > > > > > - pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
> > > > > > > > > > >
> > > > > > > > > > > service -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > The service name to use for request signing, such as execute-api.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > - max: `128`
> > > > > > > > > > > > - pattern: `[a-zA-Z0-9_-]+`
> > > > > > > > > > >
> > > > > > > > > > > region -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > The Amazon Web Services Region to use for request signing. If not specified, the Region is derived from the source URL hostname, falling back to the Region of the registry.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > - max: `64`
> > > > > > > > > > > > - pattern: `[a-z0-9-]+`

JSON Syntax:

    {
      "optionalValue": {
        "mcpServer": {
          "optionalValue": {
            "data": {
              "optionalValue": "string"
            },
            "dataSchemaVersion": {
              "optionalValue": "string"
            },
            "source": {
              "optionalValue": {
                "fromUrl": {
                  "url": "string",
                  "credentialProviderConfigurations": [
                    {
                      "credentialProviderType": "OAUTH"|"IAM",
                      "credentialProvider": {
                        "oauthCredentialProvider": {
                          "providerArn": "string",
                          "grantType": "CLIENT_CREDENTIALS",
                          "scopes": ["string", ...],
                          "customParameters": {"string": "string"
                            ...}
                        },
                        "iamCredentialProvider": {
                          "roleArn": "string",
                          "service": "string",
                          "region": "string"
                        }
                      }
                    }
                    ...
                  ]
                }
              }
            },
            "additionalData": {
              "optionalValue": {
                "tools": {
                  "optionalValue": {
                    "data": {
                      "optionalValue": "string"
                    },
                    "dataSchemaVersion": {
                      "optionalValue": "string"
                    }
                  }
                }
              }
            }
          }
        },
        "a2aAgentCard": {
          "optionalValue": {
            "data": {
              "optionalValue": "string"
            },
            "dataSchemaVersion": {
              "optionalValue": "string"
            },
            "source": {
              "optionalValue": {
                "fromUrl": {
                  "url": "string",
                  "credentialProviderConfigurations": [
                    {
                      "credentialProviderType": "OAUTH"|"IAM",
                      "credentialProvider": {
                        "oauthCredentialProvider": {
                          "providerArn": "string",
                          "grantType": "CLIENT_CREDENTIALS",
                          "scopes": ["string", ...],
                          "customParameters": {"string": "string"
                            ...}
                        },
                        "iamCredentialProvider": {
                          "roleArn": "string",
                          "service": "string",
                          "region": "string"
                        }
                      }
                    }
                    ...
                  ]
                }
              }
            }
          }
        },
        "agentSkillsDefinition": {
          "optionalValue": {
            "data": {
              "optionalValue": "string"
            },
            "dataSchemaVersion": {
              "optionalValue": "string"
            },
            "additionalData": {
              "optionalValue": {
                "skillMd": {
                  "optionalValue": {
                    "data": {
                      "optionalValue": "string"
                    },
                    "dataSchemaVersion": {
                      "optionalValue": "string"
                    },
                    "source": {
                      "optionalValue": {
                        "fromUrl": {
                          "url": "string",
                          "credentialProviderConfigurations": [
                            {
                              "credentialProviderType": "OAUTH"|"IAM",
                              "credentialProvider": {
                                "oauthCredentialProvider": {
                                  "providerArn": "string",
                                  "grantType": "CLIENT_CREDENTIALS",
                                  "scopes": ["string", ...],
                                  "customParameters": {"string": "string"
                                    ...}
                                },
                                "iamCredentialProvider": {
                                  "roleArn": "string",
                                  "service": "string",
                                  "region": "string"
                                }
                              }
                            }
                            ...
                          ]
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "custom": {
          "optionalValue": {
            "data": {
              "optionalValue": "string"
            }
          }
        },
        "http": {
          "optionalValue": {
            "source": {
              "optionalValue": {
                "fromUrl": {
                  "url": "string",
                  "credentialProviderConfigurations": [
                    {
                      "credentialProviderType": "OAUTH"|"IAM",
                      "credentialProvider": {
                        "oauthCredentialProvider": {
                          "providerArn": "string",
                          "grantType": "CLIENT_CREDENTIALS",
                          "scopes": ["string", ...],
                          "customParameters": {"string": "string"
                            ...}
                        },
                        "iamCredentialProvider": {
                          "roleArn": "string",
                          "service": "string",
                          "region": "string"
                        }
                      }
                    }
                    ...
                  ]
                }
              }
            }
          }
        },
        "agui": {
          "optionalValue": {
            "source": {
              "optionalValue": {
                "fromUrl": {
                  "url": "string",
                  "credentialProviderConfigurations": [
                    {
                      "credentialProviderType": "OAUTH"|"IAM",
                      "credentialProvider": {
                        "oauthCredentialProvider": {
                          "providerArn": "string",
                          "grantType": "CLIENT_CREDENTIALS",
                          "scopes": ["string", ...],
                          "customParameters": {"string": "string"
                            ...}
                        },
                        "iamCredentialProvider": {
                          "roleArn": "string",
                          "service": "string",
                          "region": "string"
                        }
                      }
                    }
                    ...
                  ]
                }
              }
            }
          }
        }
      }
    }

`--record-version` (string)

> The updated version of the registry record. Omit to leave the version unchanged.
>
> Constraints:
>
> - min: `1`
> - max: `255`
> - pattern: `[a-zA-Z0-9.-]+`

`--trigger-synchronization` \| `--no-trigger-synchronization` (boolean)

> Whether to trigger synchronization of the record’s descriptor content from its source

`--provenance` (list)

> List of provenance entries on a registry record. Capped at one entry today: a record carries a single DETECTED_FROM lineage. Modeled as a list so additional relations can be unlocked post-GA by raising this bound without a breaking shape change.
>
> Constraints:
>
> - min: `0`
> - max: `1`
>
> (structure)
>
> > One provenance entry describing the lineage of a registry record.
> >
> > relation -\> (string) \[required\]
> >
> > > The relationship between the registry record and its provenance source.
> > >
> > > Possible values:
> > >
> > > - `DETECTED_FROM`
> >
> > sourceId -\> (string) \[required\]
> >
> > > The identifier of the upstream source that the registry record was detected from.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `2048`
> > > - pattern: `arn:aws(-[^:]+)?:[a-zA-Z0-9-]+:[a-z0-9-]*:[0-9]{12}:.+`
> >
> > sourceType -\> (string)
> >
> > > The type of the upstream source that the registry record was detected from.
> > >
> > > Possible values:
> > >
> > > - `AWS::BedrockAgentCore::Runtime`
> > > - `AWS::BedrockAgentCore::Gateway`
> >
> > sourceDetails -\> (tagged union structure)
> >
> > > Additional details about the upstream source that the registry record was detected from, such as the AgentCore Gateway or Runtime configuration. The populated member corresponds to the source type.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `agentcoreRuntime`, `agentcoreGateway`.
> > >
> > > agentcoreRuntime -\> (structure)
> > >
> > > > Source details for a record auto-detected from an AgentCore Runtime resource.
> > > >
> > > > protocolConfiguration -\> (structure)
> > > >
> > > > > Protocol configuration for an AgentCore Runtime.
> > > > >
> > > > > serverProtocol -\> (string)
> > > > >
> > > > > > The server protocol used by an AgentCore Runtime.
> > > > > >
> > > > > > Possible values:
> > > > > >
> > > > > > - `HTTP`
> > > > > > - `A2A`
> > > > > > - `MCP`
> > > > > > - `AGUI`
> > > >
> > > > authorizerConfiguration -\> (tagged union structure)
> > > >
> > > > > The authorizer configuration for a registry. Exactly one member is set.
> > > > >
> > > > > ### Note
> > > > >
> > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `customJWTAuthorizer`.
> > > > >
> > > > > customJWTAuthorizer -\> (structure)
> > > > >
> > > > > > Configuration for a custom JWT authorizer.
> > > > > >
> > > > > > discoveryUrl -\> (string) \[required\]
> > > > > >
> > > > > > > The OpenID Connect discovery URL used to retrieve the identity provider’s metadata and signing keys.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `.+/\.well-known/openid-configuration`
> > > > > >
> > > > > > allowedAudience -\> (list)
> > > > > >
> > > > > > > The audience values accepted during JWT validation. A token is rejected if none of its audience claims match.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > >
> > > > > > > (string)
> > > > > > >
> > > > > > > > An audience value that an inbound JWT must contain to be authorized.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > >
> > > > > > allowedClients -\> (list)
> > > > > >
> > > > > > > The client identifiers accepted during JWT validation. A token is rejected if it was not issued to one of these clients.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > >
> > > > > > > (string)
> > > > > > >
> > > > > > > > A client identifier that an inbound JWT must be issued to in order to be authorized.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > >
> > > > > > allowedScopes -\> (list)
> > > > > >
> > > > > > > The scopes accepted during JWT validation. A token is rejected if it does not carry one of these scopes.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > >
> > > > > > > (string)
> > > > > > >
> > > > > > > > A scope value that an inbound JWT must carry to be authorized.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > > > > - pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
> > > > > >
> > > > > > customClaims -\> (list)
> > > > > >
> > > > > > > Additional custom claim validations applied to the inbound JWT.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > >
> > > > > > > (structure)
> > > > > > >
> > > > > > > > A validation rule applied to a single claim of an inbound JWT.
> > > > > > > >
> > > > > > > > inboundTokenClaimName -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The name of the claim in the inbound token to validate.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `255`
> > > > > > > > > - pattern: `[A-Za-z0-9_.-:]+`
> > > > > > > >
> > > > > > > > inboundTokenClaimValueType -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The value type of the claim in the inbound token, either a string or an array of strings.
> > > > > > > > >
> > > > > > > > > Possible values:
> > > > > > > > >
> > > > > > > > > - `STRING`
> > > > > > > > > - `STRING_ARRAY`
> > > > > > > >
> > > > > > > > authorizingClaimMatchValue -\> (structure) \[required\]
> > > > > > > >
> > > > > > > > > The value and match operator used to authorize the claim.
> > > > > > > > >
> > > > > > > > > claimMatchValue -\> (tagged union structure) \[required\]
> > > > > > > > >
> > > > > > > > > > The expected value or values that the claim is compared against.
> > > > > > > > > >
> > > > > > > > > > ### Note
> > > > > > > > > >
> > > > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `matchValueString`, `matchValueStringList`.
> > > > > > > > > >
> > > > > > > > > > matchValueString -\> (string)
> > > > > > > > > >
> > > > > > > > > > > A single string value to match the claim against.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `1`
> > > > > > > > > > > - max: `255`
> > > > > > > > > > > - pattern: `[A-Za-z0-9_.:/-]+`
> > > > > > > > > >
> > > > > > > > > > matchValueStringList -\> (list)
> > > > > > > > > >
> > > > > > > > > > > A list of string values to match the claim against.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `1`
> > > > > > > > > > >
> > > > > > > > > > > (string)
> > > > > > > > > > >
> > > > > > > > > > > > A single value used to match a claim during JWT validation.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > - max: `255`
> > > > > > > > > > > > - pattern: `[A-Za-z0-9_.:/-]+`
> > > > > > > > >
> > > > > > > > > claimMatchOperator -\> (string) \[required\]
> > > > > > > > >
> > > > > > > > > > The operator used to compare the claim value against the expected value.
> > > > > > > > > >
> > > > > > > > > > Possible values:
> > > > > > > > > >
> > > > > > > > > > - `EQUALS`
> > > > > > > > > > - `CONTAINS`
> > > > > > > > > > - `CONTAINS_ANY`
> > > > > >
> > > > > > privateEndpoint -\> (tagged union structure)
> > > > > >
> > > > > > > The private endpoint used to reach the identity provider’s discovery URL over a private network path.
> > > > > > >
> > > > > > > ### Note
> > > > > > >
> > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `selfManagedLatticeResource`, `managedVpcResource`.
> > > > > > >
> > > > > > > selfManagedLatticeResource -\> (tagged union structure)
> > > > > > >
> > > > > > > > A private endpoint backed by a self-managed VPC Lattice resource configuration.
> > > > > > > >
> > > > > > > > ### Note
> > > > > > > >
> > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `resourceConfigurationIdentifier`.
> > > > > > > >
> > > > > > > > resourceConfigurationIdentifier -\> (string)
> > > > > > > >
> > > > > > > > > The identifier of the VPC Lattice resource configuration, specified as a resource configuration ID or ARN.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `20`
> > > > > > > > > - max: `2048`
> > > > > > > > > - pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`
> > > > > > >
> > > > > > > managedVpcResource -\> (structure)
> > > > > > >
> > > > > > > > A private endpoint backed by a service-managed VPC resource.
> > > > > > > >
> > > > > > > > vpcIdentifier -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The identifier of the VPC in which the private endpoint is provisioned.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `10`
> > > > > > > > > - max: `48`
> > > > > > > > > - pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > > > >
> > > > > > > > subnetIds -\> (list) \[required\]
> > > > > > > >
> > > > > > > > > The identifiers of the subnets in which the private endpoint network interfaces are placed.
> > > > > > > > >
> > > > > > > > > (string)
> > > > > > > > >
> > > > > > > > > > Subnet identifier
> > > > > > > > > >
> > > > > > > > > > Constraints:
> > > > > > > > > >
> > > > > > > > > > - min: `15`
> > > > > > > > > > - max: `24`
> > > > > > > > > > - pattern: `subnet-[0-9a-zA-Z]{8,17}`
> > > > > > > >
> > > > > > > > endpointIpAddressType -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The IP address type used by the private endpoint, either IPV4 or IPV6.
> > > > > > > > >
> > > > > > > > > Possible values:
> > > > > > > > >
> > > > > > > > > - `IPV4`
> > > > > > > > > - `IPV6`
> > > > > > > >
> > > > > > > > securityGroupIds -\> (list)
> > > > > > > >
> > > > > > > > > The identifiers of the security groups associated with the private endpoint network interfaces.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `0`
> > > > > > > > > - max: `5`
> > > > > > > > >
> > > > > > > > > (string)
> > > > > > > > >
> > > > > > > > > > The identifier of a security group.
> > > > > > > > > >
> > > > > > > > > > Constraints:
> > > > > > > > > >
> > > > > > > > > > - min: `10`
> > > > > > > > > > - max: `48`
> > > > > > > > > > - pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > > > >
> > > > > > > > tags -\> (map)
> > > > > > > >
> > > > > > > > > The tags applied to the service-managed VPC resource.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `50`
> > > > > > > > >
> > > > > > > > > key -\> (string)
> > > > > > > > >
> > > > > > > > > > Key of a tag.
> > > > > > > > > >
> > > > > > > > > > Constraints:
> > > > > > > > > >
> > > > > > > > > > - min: `1`
> > > > > > > > > > - max: `128`
> > > > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > > > > >
> > > > > > > > > value -\> (string)
> > > > > > > > >
> > > > > > > > > > Value of a tag.
> > > > > > > > > >
> > > > > > > > > > Constraints:
> > > > > > > > > >
> > > > > > > > > > - min: `0`
> > > > > > > > > > - max: `256`
> > > > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > > > >
> > > > > > > > routingDomain -\> (string)
> > > > > > > >
> > > > > > > > > The routing domain used to resolve traffic through the private endpoint.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `3`
> > > > > > > > > - max: `255`
> > > > > >
> > > > > > privateEndpointOverrides -\> (list)
> > > > > >
> > > > > > > Per-domain private endpoint overrides that route specific identity provider domains through distinct private endpoints.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `0`
> > > > > > > - max: `5`
> > > > > > >
> > > > > > > (structure)
> > > > > > >
> > > > > > > > A mapping of a domain to the private endpoint used to reach it.
> > > > > > > >
> > > > > > > > domain -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The domain name to which this private endpoint override applies.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `253`
> > > > > > > >
> > > > > > > > privateEndpoint -\> (tagged union structure) \[required\]
> > > > > > > >
> > > > > > > > > The private endpoint used to reach the specified domain.
> > > > > > > > >
> > > > > > > > > ### Note
> > > > > > > > >
> > > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `selfManagedLatticeResource`, `managedVpcResource`.
> > > > > > > > >
> > > > > > > > > selfManagedLatticeResource -\> (tagged union structure)
> > > > > > > > >
> > > > > > > > > > A private endpoint backed by a self-managed VPC Lattice resource configuration.
> > > > > > > > > >
> > > > > > > > > > ### Note
> > > > > > > > > >
> > > > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `resourceConfigurationIdentifier`.
> > > > > > > > > >
> > > > > > > > > > resourceConfigurationIdentifier -\> (string)
> > > > > > > > > >
> > > > > > > > > > > The identifier of the VPC Lattice resource configuration, specified as a resource configuration ID or ARN.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `20`
> > > > > > > > > > > - max: `2048`
> > > > > > > > > > > - pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`
> > > > > > > > >
> > > > > > > > > managedVpcResource -\> (structure)
> > > > > > > > >
> > > > > > > > > > A private endpoint backed by a service-managed VPC resource.
> > > > > > > > > >
> > > > > > > > > > vpcIdentifier -\> (string) \[required\]
> > > > > > > > > >
> > > > > > > > > > > The identifier of the VPC in which the private endpoint is provisioned.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `10`
> > > > > > > > > > > - max: `48`
> > > > > > > > > > > - pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > > > > > >
> > > > > > > > > > subnetIds -\> (list) \[required\]
> > > > > > > > > >
> > > > > > > > > > > The identifiers of the subnets in which the private endpoint network interfaces are placed.
> > > > > > > > > > >
> > > > > > > > > > > (string)
> > > > > > > > > > >
> > > > > > > > > > > > Subnet identifier
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `15`
> > > > > > > > > > > > - max: `24`
> > > > > > > > > > > > - pattern: `subnet-[0-9a-zA-Z]{8,17}`
> > > > > > > > > >
> > > > > > > > > > endpointIpAddressType -\> (string) \[required\]
> > > > > > > > > >
> > > > > > > > > > > The IP address type used by the private endpoint, either IPV4 or IPV6.
> > > > > > > > > > >
> > > > > > > > > > > Possible values:
> > > > > > > > > > >
> > > > > > > > > > > - `IPV4`
> > > > > > > > > > > - `IPV6`
> > > > > > > > > >
> > > > > > > > > > securityGroupIds -\> (list)
> > > > > > > > > >
> > > > > > > > > > > The identifiers of the security groups associated with the private endpoint network interfaces.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `0`
> > > > > > > > > > > - max: `5`
> > > > > > > > > > >
> > > > > > > > > > > (string)
> > > > > > > > > > >
> > > > > > > > > > > > The identifier of a security group.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `10`
> > > > > > > > > > > > - max: `48`
> > > > > > > > > > > > - pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > > > > > >
> > > > > > > > > > tags -\> (map)
> > > > > > > > > >
> > > > > > > > > > > The tags applied to the service-managed VPC resource.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `1`
> > > > > > > > > > > - max: `50`
> > > > > > > > > > >
> > > > > > > > > > > key -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > Key of a tag.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > - max: `128`
> > > > > > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > > > > > > >
> > > > > > > > > > > value -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > Value of a tag.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `0`
> > > > > > > > > > > > - max: `256`
> > > > > > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > > > > > >
> > > > > > > > > > routingDomain -\> (string)
> > > > > > > > > >
> > > > > > > > > > > The routing domain used to resolve traffic through the private endpoint.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `3`
> > > > > > > > > > > - max: `255`
> > > >
> > > > workloadIdentityDetails -\> (structure)
> > > >
> > > > > Workload identity details associated with a source resource.
> > > > >
> > > > > workloadIdentityArn -\> (string) \[required\]
> > > > >
> > > > > > The Amazon Resource Name (ARN) of the workload identity associated with the source resource.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `1024`
> > >
> > > agentcoreGateway -\> (structure)
> > >
> > > > Source details for a record auto-detected from an AgentCore Gateway resource.
> > > >
> > > > protocolType -\> (string)
> > > >
> > > > > The protocol type of an AgentCore Gateway.
> > > > >
> > > > > Possible values:
> > > > >
> > > > > - `MCP`
> > > >
> > > > authorizerType -\> (string)
> > > >
> > > > > The type of authorizer configured on the AgentCore Gateway resource that the registry record was detected from.
> > > >
> > > > authorizerConfiguration -\> (tagged union structure)
> > > >
> > > > > The authorizer configuration for a registry. Exactly one member is set.
> > > > >
> > > > > ### Note
> > > > >
> > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `customJWTAuthorizer`.
> > > > >
> > > > > customJWTAuthorizer -\> (structure)
> > > > >
> > > > > > Configuration for a custom JWT authorizer.
> > > > > >
> > > > > > discoveryUrl -\> (string) \[required\]
> > > > > >
> > > > > > > The OpenID Connect discovery URL used to retrieve the identity provider’s metadata and signing keys.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `.+/\.well-known/openid-configuration`
> > > > > >
> > > > > > allowedAudience -\> (list)
> > > > > >
> > > > > > > The audience values accepted during JWT validation. A token is rejected if none of its audience claims match.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > >
> > > > > > > (string)
> > > > > > >
> > > > > > > > An audience value that an inbound JWT must contain to be authorized.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > >
> > > > > > allowedClients -\> (list)
> > > > > >
> > > > > > > The client identifiers accepted during JWT validation. A token is rejected if it was not issued to one of these clients.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > >
> > > > > > > (string)
> > > > > > >
> > > > > > > > A client identifier that an inbound JWT must be issued to in order to be authorized.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > >
> > > > > > allowedScopes -\> (list)
> > > > > >
> > > > > > > The scopes accepted during JWT validation. A token is rejected if it does not carry one of these scopes.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > >
> > > > > > > (string)
> > > > > > >
> > > > > > > > A scope value that an inbound JWT must carry to be authorized.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > > > > - pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
> > > > > >
> > > > > > customClaims -\> (list)
> > > > > >
> > > > > > > Additional custom claim validations applied to the inbound JWT.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > >
> > > > > > > (structure)
> > > > > > >
> > > > > > > > A validation rule applied to a single claim of an inbound JWT.
> > > > > > > >
> > > > > > > > inboundTokenClaimName -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The name of the claim in the inbound token to validate.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `255`
> > > > > > > > > - pattern: `[A-Za-z0-9_.-:]+`
> > > > > > > >
> > > > > > > > inboundTokenClaimValueType -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The value type of the claim in the inbound token, either a string or an array of strings.
> > > > > > > > >
> > > > > > > > > Possible values:
> > > > > > > > >
> > > > > > > > > - `STRING`
> > > > > > > > > - `STRING_ARRAY`
> > > > > > > >
> > > > > > > > authorizingClaimMatchValue -\> (structure) \[required\]
> > > > > > > >
> > > > > > > > > The value and match operator used to authorize the claim.
> > > > > > > > >
> > > > > > > > > claimMatchValue -\> (tagged union structure) \[required\]
> > > > > > > > >
> > > > > > > > > > The expected value or values that the claim is compared against.
> > > > > > > > > >
> > > > > > > > > > ### Note
> > > > > > > > > >
> > > > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `matchValueString`, `matchValueStringList`.
> > > > > > > > > >
> > > > > > > > > > matchValueString -\> (string)
> > > > > > > > > >
> > > > > > > > > > > A single string value to match the claim against.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `1`
> > > > > > > > > > > - max: `255`
> > > > > > > > > > > - pattern: `[A-Za-z0-9_.:/-]+`
> > > > > > > > > >
> > > > > > > > > > matchValueStringList -\> (list)
> > > > > > > > > >
> > > > > > > > > > > A list of string values to match the claim against.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `1`
> > > > > > > > > > >
> > > > > > > > > > > (string)
> > > > > > > > > > >
> > > > > > > > > > > > A single value used to match a claim during JWT validation.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > - max: `255`
> > > > > > > > > > > > - pattern: `[A-Za-z0-9_.:/-]+`
> > > > > > > > >
> > > > > > > > > claimMatchOperator -\> (string) \[required\]
> > > > > > > > >
> > > > > > > > > > The operator used to compare the claim value against the expected value.
> > > > > > > > > >
> > > > > > > > > > Possible values:
> > > > > > > > > >
> > > > > > > > > > - `EQUALS`
> > > > > > > > > > - `CONTAINS`
> > > > > > > > > > - `CONTAINS_ANY`
> > > > > >
> > > > > > privateEndpoint -\> (tagged union structure)
> > > > > >
> > > > > > > The private endpoint used to reach the identity provider’s discovery URL over a private network path.
> > > > > > >
> > > > > > > ### Note
> > > > > > >
> > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `selfManagedLatticeResource`, `managedVpcResource`.
> > > > > > >
> > > > > > > selfManagedLatticeResource -\> (tagged union structure)
> > > > > > >
> > > > > > > > A private endpoint backed by a self-managed VPC Lattice resource configuration.
> > > > > > > >
> > > > > > > > ### Note
> > > > > > > >
> > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `resourceConfigurationIdentifier`.
> > > > > > > >
> > > > > > > > resourceConfigurationIdentifier -\> (string)
> > > > > > > >
> > > > > > > > > The identifier of the VPC Lattice resource configuration, specified as a resource configuration ID or ARN.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `20`
> > > > > > > > > - max: `2048`
> > > > > > > > > - pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`
> > > > > > >
> > > > > > > managedVpcResource -\> (structure)
> > > > > > >
> > > > > > > > A private endpoint backed by a service-managed VPC resource.
> > > > > > > >
> > > > > > > > vpcIdentifier -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The identifier of the VPC in which the private endpoint is provisioned.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `10`
> > > > > > > > > - max: `48`
> > > > > > > > > - pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > > > >
> > > > > > > > subnetIds -\> (list) \[required\]
> > > > > > > >
> > > > > > > > > The identifiers of the subnets in which the private endpoint network interfaces are placed.
> > > > > > > > >
> > > > > > > > > (string)
> > > > > > > > >
> > > > > > > > > > Subnet identifier
> > > > > > > > > >
> > > > > > > > > > Constraints:
> > > > > > > > > >
> > > > > > > > > > - min: `15`
> > > > > > > > > > - max: `24`
> > > > > > > > > > - pattern: `subnet-[0-9a-zA-Z]{8,17}`
> > > > > > > >
> > > > > > > > endpointIpAddressType -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The IP address type used by the private endpoint, either IPV4 or IPV6.
> > > > > > > > >
> > > > > > > > > Possible values:
> > > > > > > > >
> > > > > > > > > - `IPV4`
> > > > > > > > > - `IPV6`
> > > > > > > >
> > > > > > > > securityGroupIds -\> (list)
> > > > > > > >
> > > > > > > > > The identifiers of the security groups associated with the private endpoint network interfaces.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `0`
> > > > > > > > > - max: `5`
> > > > > > > > >
> > > > > > > > > (string)
> > > > > > > > >
> > > > > > > > > > The identifier of a security group.
> > > > > > > > > >
> > > > > > > > > > Constraints:
> > > > > > > > > >
> > > > > > > > > > - min: `10`
> > > > > > > > > > - max: `48`
> > > > > > > > > > - pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > > > >
> > > > > > > > tags -\> (map)
> > > > > > > >
> > > > > > > > > The tags applied to the service-managed VPC resource.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `50`
> > > > > > > > >
> > > > > > > > > key -\> (string)
> > > > > > > > >
> > > > > > > > > > Key of a tag.
> > > > > > > > > >
> > > > > > > > > > Constraints:
> > > > > > > > > >
> > > > > > > > > > - min: `1`
> > > > > > > > > > - max: `128`
> > > > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > > > > >
> > > > > > > > > value -\> (string)
> > > > > > > > >
> > > > > > > > > > Value of a tag.
> > > > > > > > > >
> > > > > > > > > > Constraints:
> > > > > > > > > >
> > > > > > > > > > - min: `0`
> > > > > > > > > > - max: `256`
> > > > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > > > >
> > > > > > > > routingDomain -\> (string)
> > > > > > > >
> > > > > > > > > The routing domain used to resolve traffic through the private endpoint.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `3`
> > > > > > > > > - max: `255`
> > > > > >
> > > > > > privateEndpointOverrides -\> (list)
> > > > > >
> > > > > > > Per-domain private endpoint overrides that route specific identity provider domains through distinct private endpoints.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `0`
> > > > > > > - max: `5`
> > > > > > >
> > > > > > > (structure)
> > > > > > >
> > > > > > > > A mapping of a domain to the private endpoint used to reach it.
> > > > > > > >
> > > > > > > > domain -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The domain name to which this private endpoint override applies.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `253`
> > > > > > > >
> > > > > > > > privateEndpoint -\> (tagged union structure) \[required\]
> > > > > > > >
> > > > > > > > > The private endpoint used to reach the specified domain.
> > > > > > > > >
> > > > > > > > > ### Note
> > > > > > > > >
> > > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `selfManagedLatticeResource`, `managedVpcResource`.
> > > > > > > > >
> > > > > > > > > selfManagedLatticeResource -\> (tagged union structure)
> > > > > > > > >
> > > > > > > > > > A private endpoint backed by a self-managed VPC Lattice resource configuration.
> > > > > > > > > >
> > > > > > > > > > ### Note
> > > > > > > > > >
> > > > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `resourceConfigurationIdentifier`.
> > > > > > > > > >
> > > > > > > > > > resourceConfigurationIdentifier -\> (string)
> > > > > > > > > >
> > > > > > > > > > > The identifier of the VPC Lattice resource configuration, specified as a resource configuration ID or ARN.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `20`
> > > > > > > > > > > - max: `2048`
> > > > > > > > > > > - pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`
> > > > > > > > >
> > > > > > > > > managedVpcResource -\> (structure)
> > > > > > > > >
> > > > > > > > > > A private endpoint backed by a service-managed VPC resource.
> > > > > > > > > >
> > > > > > > > > > vpcIdentifier -\> (string) \[required\]
> > > > > > > > > >
> > > > > > > > > > > The identifier of the VPC in which the private endpoint is provisioned.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `10`
> > > > > > > > > > > - max: `48`
> > > > > > > > > > > - pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > > > > > >
> > > > > > > > > > subnetIds -\> (list) \[required\]
> > > > > > > > > >
> > > > > > > > > > > The identifiers of the subnets in which the private endpoint network interfaces are placed.
> > > > > > > > > > >
> > > > > > > > > > > (string)
> > > > > > > > > > >
> > > > > > > > > > > > Subnet identifier
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `15`
> > > > > > > > > > > > - max: `24`
> > > > > > > > > > > > - pattern: `subnet-[0-9a-zA-Z]{8,17}`
> > > > > > > > > >
> > > > > > > > > > endpointIpAddressType -\> (string) \[required\]
> > > > > > > > > >
> > > > > > > > > > > The IP address type used by the private endpoint, either IPV4 or IPV6.
> > > > > > > > > > >
> > > > > > > > > > > Possible values:
> > > > > > > > > > >
> > > > > > > > > > > - `IPV4`
> > > > > > > > > > > - `IPV6`
> > > > > > > > > >
> > > > > > > > > > securityGroupIds -\> (list)
> > > > > > > > > >
> > > > > > > > > > > The identifiers of the security groups associated with the private endpoint network interfaces.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `0`
> > > > > > > > > > > - max: `5`
> > > > > > > > > > >
> > > > > > > > > > > (string)
> > > > > > > > > > >
> > > > > > > > > > > > The identifier of a security group.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `10`
> > > > > > > > > > > > - max: `48`
> > > > > > > > > > > > - pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > > > > > >
> > > > > > > > > > tags -\> (map)
> > > > > > > > > >
> > > > > > > > > > > The tags applied to the service-managed VPC resource.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `1`
> > > > > > > > > > > - max: `50`
> > > > > > > > > > >
> > > > > > > > > > > key -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > Key of a tag.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > - max: `128`
> > > > > > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > > > > > > >
> > > > > > > > > > > value -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > Value of a tag.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `0`
> > > > > > > > > > > > - max: `256`
> > > > > > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > > > > > >
> > > > > > > > > > routingDomain -\> (string)
> > > > > > > > > >
> > > > > > > > > > > The routing domain used to resolve traffic through the private endpoint.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `3`
> > > > > > > > > > > - max: `255`
> > > >
> > > > workloadIdentityDetails -\> (structure)
> > > >
> > > > > Workload identity details associated with a source resource.
> > > > >
> > > > > workloadIdentityArn -\> (string) \[required\]
> > > > >
> > > > > > The Amazon Resource Name (ARN) of the workload identity associated with the source resource.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `1024`

JSON Syntax:

    [
      {
        "relation": "DETECTED_FROM",
        "sourceId": "string",
        "sourceType": "AWS::BedrockAgentCore::Runtime"|"AWS::BedrockAgentCore::Gateway",
        "sourceDetails": {
          "agentcoreRuntime": {
            "protocolConfiguration": {
              "serverProtocol": "HTTP"|"A2A"|"MCP"|"AGUI"
            },
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
            "workloadIdentityDetails": {
              "workloadIdentityArn": "string"
            }
          },
          "agentcoreGateway": {
            "protocolType": "MCP",
            "authorizerType": "string",
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
            "workloadIdentityDetails": {
              "workloadIdentityArn": "string"
            }
          }
        }
      }
      ...
    ]

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

> The Amazon Resource Name (ARN) of the parent registry that owns the record.
>
> Constraints:
>
> - min: `46`
> - max: `2048`
> - pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}`

recordArn -\> (string)

> The Amazon Resource Name (ARN) of the registry record.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}`

recordId -\> (string)

> The unique identifier of the registry record.
>
> Constraints:
>
> - min: `12`
> - max: `12`
> - pattern: `[a-zA-Z0-9]{12}`

name -\> (string)

> The name of the registry record. Names are unique within a registry.
>
> Constraints:
>
> - min: `1`
> - max: `255`
> - pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`

displayName -\> (string)

> The human-readable display name of the registry record.
>
> Constraints:
>
> - min: `1`
> - max: `255`

description -\> (string)

> A description of the registry record.
>
> Constraints:
>
> - min: `1`
> - max: `4096`

recordType -\> (string)

> The type of the registry record, such as MCP, AGENT, SKILL, or CUSTOM.
>
> Possible values:
>
> - `MCP`
> - `AGENT`
> - `CUSTOM`
> - `SKILL`
> - `GATEWAY`

descriptors -\> (structure)

> The typed descriptors that define the content of the registry record.
>
> mcpServer -\> (structure)
>
> > The MCP server descriptor, populated when the record type is MCP.
> >
> > data -\> (string)
> >
> > > The MCP server descriptor content, serialized as descriptor payload data.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `102400`
> >
> > dataSchemaVersion -\> (string)
> >
> > > The schema version of the descriptor payload.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `255`
> >
> > additionalData -\> (structure)
> >
> > > Additional data associated with the MCP server descriptor, such as tool definitions.
> > >
> > > tools -\> (structure)
> > >
> > > > The MCP tools descriptor that defines the tools exposed by the MCP server.
> > > >
> > > > data -\> (string)
> > > >
> > > > > The MCP tools descriptor content, serialized as descriptor payload data.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `102400`
> > > >
> > > > dataSchemaVersion -\> (string)
> > > >
> > > > > The schema version of the descriptor payload.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `255`
> >
> > source -\> (structure)
> >
> > > The optional source configuration used to synchronize the MCP server descriptor content.
> > >
> > > fromUrl -\> (structure)
> > >
> > > > URL-based descriptor source, populated when descriptor content is synchronized from a URL.
> > > >
> > > > url -\> (string) \[required\]
> > > >
> > > > > The URL from which the descriptor content is retrieved.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `2048`
> > > > > - pattern: `https://.*`
> > > >
> > > > credentialProviderConfigurations -\> (list)
> > > >
> > > > > The credential providers used to authenticate when fetching descriptor content from the source URL.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `0`
> > > > > - max: `1`
> > > > >
> > > > > (structure)
> > > > >
> > > > > > A credential provider configuration that specifies how to authenticate when fetching descriptor content from a registry record’s source URL.
> > > > > >
> > > > > > credentialProviderType -\> (string) \[required\]
> > > > > >
> > > > > > > The type of credential provider.
> > > > > > >
> > > > > > > Possible values:
> > > > > > >
> > > > > > > - `OAUTH`
> > > > > > > - `IAM`
> > > > > >
> > > > > > credentialProvider -\> (tagged union structure) \[required\]
> > > > > >
> > > > > > > The credential provider details corresponding to the specified credential provider type.
> > > > > > >
> > > > > > > ### Note
> > > > > > >
> > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `oauthCredentialProvider`, `iamCredentialProvider`.
> > > > > > >
> > > > > > > oauthCredentialProvider -\> (structure)
> > > > > > >
> > > > > > > > The OAuth 2.0 credential provider details.
> > > > > > > >
> > > > > > > > providerArn -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The Amazon Resource Name (ARN) of the OAuth 2.0 credential provider resource in Amazon Bedrock AgentCore Identity.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `2048`
> > > > > > > > > - pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:.*`
> > > > > > > >
> > > > > > > > grantType -\> (string)
> > > > > > > >
> > > > > > > > > The OAuth 2.0 grant type used to obtain access tokens.
> > > > > > > > >
> > > > > > > > > Possible values:
> > > > > > > > >
> > > > > > > > > - `CLIENT_CREDENTIALS`
> > > > > > > >
> > > > > > > > scopes -\> (list)
> > > > > > > >
> > > > > > > > > The OAuth 2.0 scopes to request when obtaining access tokens.
> > > > > > > > >
> > > > > > > > > (string)
> > > > > > > >
> > > > > > > > customParameters -\> (map)
> > > > > > > >
> > > > > > > > > Additional parameters to include in the OAuth 2.0 token request.
> > > > > > > > >
> > > > > > > > > key -\> (string)
> > > > > > > > >
> > > > > > > > > value -\> (string)
> > > > > > >
> > > > > > > iamCredentialProvider -\> (structure)
> > > > > > >
> > > > > > > > The IAM role credential provider details.
> > > > > > > >
> > > > > > > > roleArn -\> (string)
> > > > > > > >
> > > > > > > > > The Amazon Resource Name (ARN) of the IAM role to assume for request signing.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `20`
> > > > > > > > > - max: `2048`
> > > > > > > > > - pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
> > > > > > > >
> > > > > > > > service -\> (string)
> > > > > > > >
> > > > > > > > > The service name to use for request signing, such as execute-api.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `128`
> > > > > > > > > - pattern: `[a-zA-Z0-9_-]+`
> > > > > > > >
> > > > > > > > region -\> (string)
> > > > > > > >
> > > > > > > > > The Amazon Web Services Region to use for request signing. If not specified, the Region is derived from the source URL hostname, falling back to the Region of the registry.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `64`
> > > > > > > > > - pattern: `[a-z0-9-]+`
>
> a2aAgentCard -\> (structure)
>
> > The A2A agent card descriptor, populated when the record type is AGENT.
> >
> > data -\> (string)
> >
> > > The A2A agent card content, serialized as descriptor payload data.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `102400`
> >
> > dataSchemaVersion -\> (string)
> >
> > > The schema version of the descriptor payload.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `255`
> >
> > source -\> (structure)
> >
> > > The optional source configuration used to synchronize the A2A agent card descriptor content.
> > >
> > > fromUrl -\> (structure)
> > >
> > > > URL-based descriptor source, populated when descriptor content is synchronized from a URL.
> > > >
> > > > url -\> (string) \[required\]
> > > >
> > > > > The URL from which the descriptor content is retrieved.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `2048`
> > > > > - pattern: `https://.*`
> > > >
> > > > credentialProviderConfigurations -\> (list)
> > > >
> > > > > The credential providers used to authenticate when fetching descriptor content from the source URL.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `0`
> > > > > - max: `1`
> > > > >
> > > > > (structure)
> > > > >
> > > > > > A credential provider configuration that specifies how to authenticate when fetching descriptor content from a registry record’s source URL.
> > > > > >
> > > > > > credentialProviderType -\> (string) \[required\]
> > > > > >
> > > > > > > The type of credential provider.
> > > > > > >
> > > > > > > Possible values:
> > > > > > >
> > > > > > > - `OAUTH`
> > > > > > > - `IAM`
> > > > > >
> > > > > > credentialProvider -\> (tagged union structure) \[required\]
> > > > > >
> > > > > > > The credential provider details corresponding to the specified credential provider type.
> > > > > > >
> > > > > > > ### Note
> > > > > > >
> > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `oauthCredentialProvider`, `iamCredentialProvider`.
> > > > > > >
> > > > > > > oauthCredentialProvider -\> (structure)
> > > > > > >
> > > > > > > > The OAuth 2.0 credential provider details.
> > > > > > > >
> > > > > > > > providerArn -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The Amazon Resource Name (ARN) of the OAuth 2.0 credential provider resource in Amazon Bedrock AgentCore Identity.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `2048`
> > > > > > > > > - pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:.*`
> > > > > > > >
> > > > > > > > grantType -\> (string)
> > > > > > > >
> > > > > > > > > The OAuth 2.0 grant type used to obtain access tokens.
> > > > > > > > >
> > > > > > > > > Possible values:
> > > > > > > > >
> > > > > > > > > - `CLIENT_CREDENTIALS`
> > > > > > > >
> > > > > > > > scopes -\> (list)
> > > > > > > >
> > > > > > > > > The OAuth 2.0 scopes to request when obtaining access tokens.
> > > > > > > > >
> > > > > > > > > (string)
> > > > > > > >
> > > > > > > > customParameters -\> (map)
> > > > > > > >
> > > > > > > > > Additional parameters to include in the OAuth 2.0 token request.
> > > > > > > > >
> > > > > > > > > key -\> (string)
> > > > > > > > >
> > > > > > > > > value -\> (string)
> > > > > > >
> > > > > > > iamCredentialProvider -\> (structure)
> > > > > > >
> > > > > > > > The IAM role credential provider details.
> > > > > > > >
> > > > > > > > roleArn -\> (string)
> > > > > > > >
> > > > > > > > > The Amazon Resource Name (ARN) of the IAM role to assume for request signing.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `20`
> > > > > > > > > - max: `2048`
> > > > > > > > > - pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
> > > > > > > >
> > > > > > > > service -\> (string)
> > > > > > > >
> > > > > > > > > The service name to use for request signing, such as execute-api.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `128`
> > > > > > > > > - pattern: `[a-zA-Z0-9_-]+`
> > > > > > > >
> > > > > > > > region -\> (string)
> > > > > > > >
> > > > > > > > > The Amazon Web Services Region to use for request signing. If not specified, the Region is derived from the source URL hostname, falling back to the Region of the registry.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `64`
> > > > > > > > > - pattern: `[a-z0-9-]+`
>
> agentSkillsDefinition -\> (structure)
>
> > The agent skills definition descriptor, populated when the record type is SKILL.
> >
> > data -\> (string)
> >
> > > The agent skills definition content, serialized as descriptor payload data.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `102400`
> >
> > dataSchemaVersion -\> (string)
> >
> > > The schema version of the descriptor payload.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `255`
> >
> > additionalData -\> (structure)
> >
> > > Additional data associated with the agent skills definition descriptor.
> > >
> > > skillMd -\> (structure)
> > >
> > > > The markdown skill content associated with an agent skills definition.
> > > >
> > > > data -\> (string)
> > > >
> > > > > The agent skills markdown content, serialized as descriptor payload data.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `102400`
> > > >
> > > > dataSchemaVersion -\> (string)
> > > >
> > > > > The schema version of the descriptor payload.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `255`
> > > >
> > > > source -\> (structure)
> > > >
> > > > > The optional source configuration used to synchronize the agent skills markdown content.
> > > > >
> > > > > fromUrl -\> (structure)
> > > > >
> > > > > > URL-based descriptor source, populated when descriptor content is synchronized from a URL.
> > > > > >
> > > > > > url -\> (string) \[required\]
> > > > > >
> > > > > > > The URL from which the descriptor content is retrieved.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `https://.*`
> > > > > >
> > > > > > credentialProviderConfigurations -\> (list)
> > > > > >
> > > > > > > The credential providers used to authenticate when fetching descriptor content from the source URL.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `0`
> > > > > > > - max: `1`
> > > > > > >
> > > > > > > (structure)
> > > > > > >
> > > > > > > > A credential provider configuration that specifies how to authenticate when fetching descriptor content from a registry record’s source URL.
> > > > > > > >
> > > > > > > > credentialProviderType -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The type of credential provider.
> > > > > > > > >
> > > > > > > > > Possible values:
> > > > > > > > >
> > > > > > > > > - `OAUTH`
> > > > > > > > > - `IAM`
> > > > > > > >
> > > > > > > > credentialProvider -\> (tagged union structure) \[required\]
> > > > > > > >
> > > > > > > > > The credential provider details corresponding to the specified credential provider type.
> > > > > > > > >
> > > > > > > > > ### Note
> > > > > > > > >
> > > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `oauthCredentialProvider`, `iamCredentialProvider`.
> > > > > > > > >
> > > > > > > > > oauthCredentialProvider -\> (structure)
> > > > > > > > >
> > > > > > > > > > The OAuth 2.0 credential provider details.
> > > > > > > > > >
> > > > > > > > > > providerArn -\> (string) \[required\]
> > > > > > > > > >
> > > > > > > > > > > The Amazon Resource Name (ARN) of the OAuth 2.0 credential provider resource in Amazon Bedrock AgentCore Identity.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `1`
> > > > > > > > > > > - max: `2048`
> > > > > > > > > > > - pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:.*`
> > > > > > > > > >
> > > > > > > > > > grantType -\> (string)
> > > > > > > > > >
> > > > > > > > > > > The OAuth 2.0 grant type used to obtain access tokens.
> > > > > > > > > > >
> > > > > > > > > > > Possible values:
> > > > > > > > > > >
> > > > > > > > > > > - `CLIENT_CREDENTIALS`
> > > > > > > > > >
> > > > > > > > > > scopes -\> (list)
> > > > > > > > > >
> > > > > > > > > > > The OAuth 2.0 scopes to request when obtaining access tokens.
> > > > > > > > > > >
> > > > > > > > > > > (string)
> > > > > > > > > >
> > > > > > > > > > customParameters -\> (map)
> > > > > > > > > >
> > > > > > > > > > > Additional parameters to include in the OAuth 2.0 token request.
> > > > > > > > > > >
> > > > > > > > > > > key -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > value -\> (string)
> > > > > > > > >
> > > > > > > > > iamCredentialProvider -\> (structure)
> > > > > > > > >
> > > > > > > > > > The IAM role credential provider details.
> > > > > > > > > >
> > > > > > > > > > roleArn -\> (string)
> > > > > > > > > >
> > > > > > > > > > > The Amazon Resource Name (ARN) of the IAM role to assume for request signing.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `20`
> > > > > > > > > > > - max: `2048`
> > > > > > > > > > > - pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
> > > > > > > > > >
> > > > > > > > > > service -\> (string)
> > > > > > > > > >
> > > > > > > > > > > The service name to use for request signing, such as execute-api.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `1`
> > > > > > > > > > > - max: `128`
> > > > > > > > > > > - pattern: `[a-zA-Z0-9_-]+`
> > > > > > > > > >
> > > > > > > > > > region -\> (string)
> > > > > > > > > >
> > > > > > > > > > > The Amazon Web Services Region to use for request signing. If not specified, the Region is derived from the source URL hostname, falling back to the Region of the registry.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `1`
> > > > > > > > > > > - max: `64`
> > > > > > > > > > > - pattern: `[a-z0-9-]+`
>
> custom -\> (structure)
>
> > The custom descriptor, populated when the record type is CUSTOM.
> >
> > data -\> (string)
> >
> > > The custom descriptor content, serialized as descriptor payload data.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `102400`
>
> http -\> (structure)
>
> > The HTTP descriptor, populated for records detected from an HTTP protocol source.
> >
> > source -\> (structure)
> >
> > > The source configuration that defines where descriptor content is retrieved from.
> > >
> > > fromUrl -\> (structure)
> > >
> > > > URL-based descriptor source, populated when descriptor content is synchronized from a URL.
> > > >
> > > > url -\> (string) \[required\]
> > > >
> > > > > The URL from which the descriptor content is retrieved.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `2048`
> > > > > - pattern: `https://.*`
> > > >
> > > > credentialProviderConfigurations -\> (list)
> > > >
> > > > > The credential providers used to authenticate when fetching descriptor content from the source URL.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `0`
> > > > > - max: `1`
> > > > >
> > > > > (structure)
> > > > >
> > > > > > A credential provider configuration that specifies how to authenticate when fetching descriptor content from a registry record’s source URL.
> > > > > >
> > > > > > credentialProviderType -\> (string) \[required\]
> > > > > >
> > > > > > > The type of credential provider.
> > > > > > >
> > > > > > > Possible values:
> > > > > > >
> > > > > > > - `OAUTH`
> > > > > > > - `IAM`
> > > > > >
> > > > > > credentialProvider -\> (tagged union structure) \[required\]
> > > > > >
> > > > > > > The credential provider details corresponding to the specified credential provider type.
> > > > > > >
> > > > > > > ### Note
> > > > > > >
> > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `oauthCredentialProvider`, `iamCredentialProvider`.
> > > > > > >
> > > > > > > oauthCredentialProvider -\> (structure)
> > > > > > >
> > > > > > > > The OAuth 2.0 credential provider details.
> > > > > > > >
> > > > > > > > providerArn -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The Amazon Resource Name (ARN) of the OAuth 2.0 credential provider resource in Amazon Bedrock AgentCore Identity.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `2048`
> > > > > > > > > - pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:.*`
> > > > > > > >
> > > > > > > > grantType -\> (string)
> > > > > > > >
> > > > > > > > > The OAuth 2.0 grant type used to obtain access tokens.
> > > > > > > > >
> > > > > > > > > Possible values:
> > > > > > > > >
> > > > > > > > > - `CLIENT_CREDENTIALS`
> > > > > > > >
> > > > > > > > scopes -\> (list)
> > > > > > > >
> > > > > > > > > The OAuth 2.0 scopes to request when obtaining access tokens.
> > > > > > > > >
> > > > > > > > > (string)
> > > > > > > >
> > > > > > > > customParameters -\> (map)
> > > > > > > >
> > > > > > > > > Additional parameters to include in the OAuth 2.0 token request.
> > > > > > > > >
> > > > > > > > > key -\> (string)
> > > > > > > > >
> > > > > > > > > value -\> (string)
> > > > > > >
> > > > > > > iamCredentialProvider -\> (structure)
> > > > > > >
> > > > > > > > The IAM role credential provider details.
> > > > > > > >
> > > > > > > > roleArn -\> (string)
> > > > > > > >
> > > > > > > > > The Amazon Resource Name (ARN) of the IAM role to assume for request signing.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `20`
> > > > > > > > > - max: `2048`
> > > > > > > > > - pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
> > > > > > > >
> > > > > > > > service -\> (string)
> > > > > > > >
> > > > > > > > > The service name to use for request signing, such as execute-api.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `128`
> > > > > > > > > - pattern: `[a-zA-Z0-9_-]+`
> > > > > > > >
> > > > > > > > region -\> (string)
> > > > > > > >
> > > > > > > > > The Amazon Web Services Region to use for request signing. If not specified, the Region is derived from the source URL hostname, falling back to the Region of the registry.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `64`
> > > > > > > > > - pattern: `[a-z0-9-]+`
>
> agui -\> (structure)
>
> > The AG-UI descriptor, populated for records detected from an AG-UI protocol source.
> >
> > source -\> (structure)
> >
> > > The source configuration that defines where descriptor content is retrieved from.
> > >
> > > fromUrl -\> (structure)
> > >
> > > > URL-based descriptor source, populated when descriptor content is synchronized from a URL.
> > > >
> > > > url -\> (string) \[required\]
> > > >
> > > > > The URL from which the descriptor content is retrieved.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `2048`
> > > > > - pattern: `https://.*`
> > > >
> > > > credentialProviderConfigurations -\> (list)
> > > >
> > > > > The credential providers used to authenticate when fetching descriptor content from the source URL.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `0`
> > > > > - max: `1`
> > > > >
> > > > > (structure)
> > > > >
> > > > > > A credential provider configuration that specifies how to authenticate when fetching descriptor content from a registry record’s source URL.
> > > > > >
> > > > > > credentialProviderType -\> (string) \[required\]
> > > > > >
> > > > > > > The type of credential provider.
> > > > > > >
> > > > > > > Possible values:
> > > > > > >
> > > > > > > - `OAUTH`
> > > > > > > - `IAM`
> > > > > >
> > > > > > credentialProvider -\> (tagged union structure) \[required\]
> > > > > >
> > > > > > > The credential provider details corresponding to the specified credential provider type.
> > > > > > >
> > > > > > > ### Note
> > > > > > >
> > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `oauthCredentialProvider`, `iamCredentialProvider`.
> > > > > > >
> > > > > > > oauthCredentialProvider -\> (structure)
> > > > > > >
> > > > > > > > The OAuth 2.0 credential provider details.
> > > > > > > >
> > > > > > > > providerArn -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The Amazon Resource Name (ARN) of the OAuth 2.0 credential provider resource in Amazon Bedrock AgentCore Identity.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `2048`
> > > > > > > > > - pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:.*`
> > > > > > > >
> > > > > > > > grantType -\> (string)
> > > > > > > >
> > > > > > > > > The OAuth 2.0 grant type used to obtain access tokens.
> > > > > > > > >
> > > > > > > > > Possible values:
> > > > > > > > >
> > > > > > > > > - `CLIENT_CREDENTIALS`
> > > > > > > >
> > > > > > > > scopes -\> (list)
> > > > > > > >
> > > > > > > > > The OAuth 2.0 scopes to request when obtaining access tokens.
> > > > > > > > >
> > > > > > > > > (string)
> > > > > > > >
> > > > > > > > customParameters -\> (map)
> > > > > > > >
> > > > > > > > > Additional parameters to include in the OAuth 2.0 token request.
> > > > > > > > >
> > > > > > > > > key -\> (string)
> > > > > > > > >
> > > > > > > > > value -\> (string)
> > > > > > >
> > > > > > > iamCredentialProvider -\> (structure)
> > > > > > >
> > > > > > > > The IAM role credential provider details.
> > > > > > > >
> > > > > > > > roleArn -\> (string)
> > > > > > > >
> > > > > > > > > The Amazon Resource Name (ARN) of the IAM role to assume for request signing.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `20`
> > > > > > > > > - max: `2048`
> > > > > > > > > - pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
> > > > > > > >
> > > > > > > > service -\> (string)
> > > > > > > >
> > > > > > > > > The service name to use for request signing, such as execute-api.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `128`
> > > > > > > > > - pattern: `[a-zA-Z0-9_-]+`
> > > > > > > >
> > > > > > > > region -\> (string)
> > > > > > > >
> > > > > > > > > The Amazon Web Services Region to use for request signing. If not specified, the Region is derived from the source URL hostname, falling back to the Region of the registry.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `64`
> > > > > > > > > - pattern: `[a-z0-9-]+`

recordVersion -\> (string)

> The version identifier of the registry record.
>
> Constraints:
>
> - min: `1`
> - max: `255`
> - pattern: `[a-zA-Z0-9.-]+`

status -\> (string)

> The lifecycle status of the registry record.
>
> Possible values:
>
> - `DRAFT`
> - `PENDING_APPROVAL`
> - `APPROVED`
> - `REJECTED`
> - `DEPRECATED`
> - `CREATING`
> - `UPDATING`
> - `CREATE_FAILED`
> - `UPDATE_FAILED`

createdAt -\> (timestamp)

> The timestamp when the registry record was created.

updatedAt -\> (timestamp)

> The timestamp when the registry record was last updated.

statusReason -\> (string)

> The reason for the current status. Typically populated when the status indicates a failure state.

provenance -\> (list)

> List of provenance entries on a registry record. Capped at one entry today: a record carries a single DETECTED_FROM lineage. Modeled as a list so additional relations can be unlocked post-GA by raising this bound without a breaking shape change.
>
> Constraints:
>
> - min: `0`
> - max: `1`
>
> (structure)
>
> > One provenance entry describing the lineage of a registry record.
> >
> > relation -\> (string) \[required\]
> >
> > > The relationship between the registry record and its provenance source.
> > >
> > > Possible values:
> > >
> > > - `DETECTED_FROM`
> >
> > sourceId -\> (string) \[required\]
> >
> > > The identifier of the upstream source that the registry record was detected from.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `2048`
> > > - pattern: `arn:aws(-[^:]+)?:[a-zA-Z0-9-]+:[a-z0-9-]*:[0-9]{12}:.+`
> >
> > sourceType -\> (string)
> >
> > > The type of the upstream source that the registry record was detected from.
> > >
> > > Possible values:
> > >
> > > - `AWS::BedrockAgentCore::Runtime`
> > > - `AWS::BedrockAgentCore::Gateway`
> >
> > sourceDetails -\> (tagged union structure)
> >
> > > Additional details about the upstream source that the registry record was detected from, such as the AgentCore Gateway or Runtime configuration. The populated member corresponds to the source type.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `agentcoreRuntime`, `agentcoreGateway`.
> > >
> > > agentcoreRuntime -\> (structure)
> > >
> > > > Source details for a record auto-detected from an AgentCore Runtime resource.
> > > >
> > > > protocolConfiguration -\> (structure)
> > > >
> > > > > Protocol configuration for an AgentCore Runtime.
> > > > >
> > > > > serverProtocol -\> (string)
> > > > >
> > > > > > The server protocol used by an AgentCore Runtime.
> > > > > >
> > > > > > Possible values:
> > > > > >
> > > > > > - `HTTP`
> > > > > > - `A2A`
> > > > > > - `MCP`
> > > > > > - `AGUI`
> > > >
> > > > authorizerConfiguration -\> (tagged union structure)
> > > >
> > > > > The authorizer configuration for a registry. Exactly one member is set.
> > > > >
> > > > > ### Note
> > > > >
> > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `customJWTAuthorizer`.
> > > > >
> > > > > customJWTAuthorizer -\> (structure)
> > > > >
> > > > > > Configuration for a custom JWT authorizer.
> > > > > >
> > > > > > discoveryUrl -\> (string) \[required\]
> > > > > >
> > > > > > > The OpenID Connect discovery URL used to retrieve the identity provider’s metadata and signing keys.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `.+/\.well-known/openid-configuration`
> > > > > >
> > > > > > allowedAudience -\> (list)
> > > > > >
> > > > > > > The audience values accepted during JWT validation. A token is rejected if none of its audience claims match.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > >
> > > > > > > (string)
> > > > > > >
> > > > > > > > An audience value that an inbound JWT must contain to be authorized.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > >
> > > > > > allowedClients -\> (list)
> > > > > >
> > > > > > > The client identifiers accepted during JWT validation. A token is rejected if it was not issued to one of these clients.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > >
> > > > > > > (string)
> > > > > > >
> > > > > > > > A client identifier that an inbound JWT must be issued to in order to be authorized.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > >
> > > > > > allowedScopes -\> (list)
> > > > > >
> > > > > > > The scopes accepted during JWT validation. A token is rejected if it does not carry one of these scopes.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > >
> > > > > > > (string)
> > > > > > >
> > > > > > > > A scope value that an inbound JWT must carry to be authorized.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > > > > - pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
> > > > > >
> > > > > > customClaims -\> (list)
> > > > > >
> > > > > > > Additional custom claim validations applied to the inbound JWT.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > >
> > > > > > > (structure)
> > > > > > >
> > > > > > > > A validation rule applied to a single claim of an inbound JWT.
> > > > > > > >
> > > > > > > > inboundTokenClaimName -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The name of the claim in the inbound token to validate.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `255`
> > > > > > > > > - pattern: `[A-Za-z0-9_.-:]+`
> > > > > > > >
> > > > > > > > inboundTokenClaimValueType -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The value type of the claim in the inbound token, either a string or an array of strings.
> > > > > > > > >
> > > > > > > > > Possible values:
> > > > > > > > >
> > > > > > > > > - `STRING`
> > > > > > > > > - `STRING_ARRAY`
> > > > > > > >
> > > > > > > > authorizingClaimMatchValue -\> (structure) \[required\]
> > > > > > > >
> > > > > > > > > The value and match operator used to authorize the claim.
> > > > > > > > >
> > > > > > > > > claimMatchValue -\> (tagged union structure) \[required\]
> > > > > > > > >
> > > > > > > > > > The expected value or values that the claim is compared against.
> > > > > > > > > >
> > > > > > > > > > ### Note
> > > > > > > > > >
> > > > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `matchValueString`, `matchValueStringList`.
> > > > > > > > > >
> > > > > > > > > > matchValueString -\> (string)
> > > > > > > > > >
> > > > > > > > > > > A single string value to match the claim against.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `1`
> > > > > > > > > > > - max: `255`
> > > > > > > > > > > - pattern: `[A-Za-z0-9_.:/-]+`
> > > > > > > > > >
> > > > > > > > > > matchValueStringList -\> (list)
> > > > > > > > > >
> > > > > > > > > > > A list of string values to match the claim against.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `1`
> > > > > > > > > > >
> > > > > > > > > > > (string)
> > > > > > > > > > >
> > > > > > > > > > > > A single value used to match a claim during JWT validation.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > - max: `255`
> > > > > > > > > > > > - pattern: `[A-Za-z0-9_.:/-]+`
> > > > > > > > >
> > > > > > > > > claimMatchOperator -\> (string) \[required\]
> > > > > > > > >
> > > > > > > > > > The operator used to compare the claim value against the expected value.
> > > > > > > > > >
> > > > > > > > > > Possible values:
> > > > > > > > > >
> > > > > > > > > > - `EQUALS`
> > > > > > > > > > - `CONTAINS`
> > > > > > > > > > - `CONTAINS_ANY`
> > > > > >
> > > > > > privateEndpoint -\> (tagged union structure)
> > > > > >
> > > > > > > The private endpoint used to reach the identity provider’s discovery URL over a private network path.
> > > > > > >
> > > > > > > ### Note
> > > > > > >
> > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `selfManagedLatticeResource`, `managedVpcResource`.
> > > > > > >
> > > > > > > selfManagedLatticeResource -\> (tagged union structure)
> > > > > > >
> > > > > > > > A private endpoint backed by a self-managed VPC Lattice resource configuration.
> > > > > > > >
> > > > > > > > ### Note
> > > > > > > >
> > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `resourceConfigurationIdentifier`.
> > > > > > > >
> > > > > > > > resourceConfigurationIdentifier -\> (string)
> > > > > > > >
> > > > > > > > > The identifier of the VPC Lattice resource configuration, specified as a resource configuration ID or ARN.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `20`
> > > > > > > > > - max: `2048`
> > > > > > > > > - pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`
> > > > > > >
> > > > > > > managedVpcResource -\> (structure)
> > > > > > >
> > > > > > > > A private endpoint backed by a service-managed VPC resource.
> > > > > > > >
> > > > > > > > vpcIdentifier -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The identifier of the VPC in which the private endpoint is provisioned.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `10`
> > > > > > > > > - max: `48`
> > > > > > > > > - pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > > > >
> > > > > > > > subnetIds -\> (list) \[required\]
> > > > > > > >
> > > > > > > > > The identifiers of the subnets in which the private endpoint network interfaces are placed.
> > > > > > > > >
> > > > > > > > > (string)
> > > > > > > > >
> > > > > > > > > > Subnet identifier
> > > > > > > > > >
> > > > > > > > > > Constraints:
> > > > > > > > > >
> > > > > > > > > > - min: `15`
> > > > > > > > > > - max: `24`
> > > > > > > > > > - pattern: `subnet-[0-9a-zA-Z]{8,17}`
> > > > > > > >
> > > > > > > > endpointIpAddressType -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The IP address type used by the private endpoint, either IPV4 or IPV6.
> > > > > > > > >
> > > > > > > > > Possible values:
> > > > > > > > >
> > > > > > > > > - `IPV4`
> > > > > > > > > - `IPV6`
> > > > > > > >
> > > > > > > > securityGroupIds -\> (list)
> > > > > > > >
> > > > > > > > > The identifiers of the security groups associated with the private endpoint network interfaces.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `0`
> > > > > > > > > - max: `5`
> > > > > > > > >
> > > > > > > > > (string)
> > > > > > > > >
> > > > > > > > > > The identifier of a security group.
> > > > > > > > > >
> > > > > > > > > > Constraints:
> > > > > > > > > >
> > > > > > > > > > - min: `10`
> > > > > > > > > > - max: `48`
> > > > > > > > > > - pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > > > >
> > > > > > > > tags -\> (map)
> > > > > > > >
> > > > > > > > > The tags applied to the service-managed VPC resource.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `50`
> > > > > > > > >
> > > > > > > > > key -\> (string)
> > > > > > > > >
> > > > > > > > > > Key of a tag.
> > > > > > > > > >
> > > > > > > > > > Constraints:
> > > > > > > > > >
> > > > > > > > > > - min: `1`
> > > > > > > > > > - max: `128`
> > > > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > > > > >
> > > > > > > > > value -\> (string)
> > > > > > > > >
> > > > > > > > > > Value of a tag.
> > > > > > > > > >
> > > > > > > > > > Constraints:
> > > > > > > > > >
> > > > > > > > > > - min: `0`
> > > > > > > > > > - max: `256`
> > > > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > > > >
> > > > > > > > routingDomain -\> (string)
> > > > > > > >
> > > > > > > > > The routing domain used to resolve traffic through the private endpoint.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `3`
> > > > > > > > > - max: `255`
> > > > > >
> > > > > > privateEndpointOverrides -\> (list)
> > > > > >
> > > > > > > Per-domain private endpoint overrides that route specific identity provider domains through distinct private endpoints.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `0`
> > > > > > > - max: `5`
> > > > > > >
> > > > > > > (structure)
> > > > > > >
> > > > > > > > A mapping of a domain to the private endpoint used to reach it.
> > > > > > > >
> > > > > > > > domain -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The domain name to which this private endpoint override applies.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `253`
> > > > > > > >
> > > > > > > > privateEndpoint -\> (tagged union structure) \[required\]
> > > > > > > >
> > > > > > > > > The private endpoint used to reach the specified domain.
> > > > > > > > >
> > > > > > > > > ### Note
> > > > > > > > >
> > > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `selfManagedLatticeResource`, `managedVpcResource`.
> > > > > > > > >
> > > > > > > > > selfManagedLatticeResource -\> (tagged union structure)
> > > > > > > > >
> > > > > > > > > > A private endpoint backed by a self-managed VPC Lattice resource configuration.
> > > > > > > > > >
> > > > > > > > > > ### Note
> > > > > > > > > >
> > > > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `resourceConfigurationIdentifier`.
> > > > > > > > > >
> > > > > > > > > > resourceConfigurationIdentifier -\> (string)
> > > > > > > > > >
> > > > > > > > > > > The identifier of the VPC Lattice resource configuration, specified as a resource configuration ID or ARN.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `20`
> > > > > > > > > > > - max: `2048`
> > > > > > > > > > > - pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`
> > > > > > > > >
> > > > > > > > > managedVpcResource -\> (structure)
> > > > > > > > >
> > > > > > > > > > A private endpoint backed by a service-managed VPC resource.
> > > > > > > > > >
> > > > > > > > > > vpcIdentifier -\> (string) \[required\]
> > > > > > > > > >
> > > > > > > > > > > The identifier of the VPC in which the private endpoint is provisioned.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `10`
> > > > > > > > > > > - max: `48`
> > > > > > > > > > > - pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > > > > > >
> > > > > > > > > > subnetIds -\> (list) \[required\]
> > > > > > > > > >
> > > > > > > > > > > The identifiers of the subnets in which the private endpoint network interfaces are placed.
> > > > > > > > > > >
> > > > > > > > > > > (string)
> > > > > > > > > > >
> > > > > > > > > > > > Subnet identifier
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `15`
> > > > > > > > > > > > - max: `24`
> > > > > > > > > > > > - pattern: `subnet-[0-9a-zA-Z]{8,17}`
> > > > > > > > > >
> > > > > > > > > > endpointIpAddressType -\> (string) \[required\]
> > > > > > > > > >
> > > > > > > > > > > The IP address type used by the private endpoint, either IPV4 or IPV6.
> > > > > > > > > > >
> > > > > > > > > > > Possible values:
> > > > > > > > > > >
> > > > > > > > > > > - `IPV4`
> > > > > > > > > > > - `IPV6`
> > > > > > > > > >
> > > > > > > > > > securityGroupIds -\> (list)
> > > > > > > > > >
> > > > > > > > > > > The identifiers of the security groups associated with the private endpoint network interfaces.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `0`
> > > > > > > > > > > - max: `5`
> > > > > > > > > > >
> > > > > > > > > > > (string)
> > > > > > > > > > >
> > > > > > > > > > > > The identifier of a security group.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `10`
> > > > > > > > > > > > - max: `48`
> > > > > > > > > > > > - pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > > > > > >
> > > > > > > > > > tags -\> (map)
> > > > > > > > > >
> > > > > > > > > > > The tags applied to the service-managed VPC resource.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `1`
> > > > > > > > > > > - max: `50`
> > > > > > > > > > >
> > > > > > > > > > > key -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > Key of a tag.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > - max: `128`
> > > > > > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > > > > > > >
> > > > > > > > > > > value -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > Value of a tag.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `0`
> > > > > > > > > > > > - max: `256`
> > > > > > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > > > > > >
> > > > > > > > > > routingDomain -\> (string)
> > > > > > > > > >
> > > > > > > > > > > The routing domain used to resolve traffic through the private endpoint.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `3`
> > > > > > > > > > > - max: `255`
> > > >
> > > > workloadIdentityDetails -\> (structure)
> > > >
> > > > > Workload identity details associated with a source resource.
> > > > >
> > > > > workloadIdentityArn -\> (string) \[required\]
> > > > >
> > > > > > The Amazon Resource Name (ARN) of the workload identity associated with the source resource.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `1024`
> > >
> > > agentcoreGateway -\> (structure)
> > >
> > > > Source details for a record auto-detected from an AgentCore Gateway resource.
> > > >
> > > > protocolType -\> (string)
> > > >
> > > > > The protocol type of an AgentCore Gateway.
> > > > >
> > > > > Possible values:
> > > > >
> > > > > - `MCP`
> > > >
> > > > authorizerType -\> (string)
> > > >
> > > > > The type of authorizer configured on the AgentCore Gateway resource that the registry record was detected from.
> > > >
> > > > authorizerConfiguration -\> (tagged union structure)
> > > >
> > > > > The authorizer configuration for a registry. Exactly one member is set.
> > > > >
> > > > > ### Note
> > > > >
> > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `customJWTAuthorizer`.
> > > > >
> > > > > customJWTAuthorizer -\> (structure)
> > > > >
> > > > > > Configuration for a custom JWT authorizer.
> > > > > >
> > > > > > discoveryUrl -\> (string) \[required\]
> > > > > >
> > > > > > > The OpenID Connect discovery URL used to retrieve the identity provider’s metadata and signing keys.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `.+/\.well-known/openid-configuration`
> > > > > >
> > > > > > allowedAudience -\> (list)
> > > > > >
> > > > > > > The audience values accepted during JWT validation. A token is rejected if none of its audience claims match.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > >
> > > > > > > (string)
> > > > > > >
> > > > > > > > An audience value that an inbound JWT must contain to be authorized.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > >
> > > > > > allowedClients -\> (list)
> > > > > >
> > > > > > > The client identifiers accepted during JWT validation. A token is rejected if it was not issued to one of these clients.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > >
> > > > > > > (string)
> > > > > > >
> > > > > > > > A client identifier that an inbound JWT must be issued to in order to be authorized.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > >
> > > > > > allowedScopes -\> (list)
> > > > > >
> > > > > > > The scopes accepted during JWT validation. A token is rejected if it does not carry one of these scopes.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > >
> > > > > > > (string)
> > > > > > >
> > > > > > > > A scope value that an inbound JWT must carry to be authorized.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `255`
> > > > > > > > - pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
> > > > > >
> > > > > > customClaims -\> (list)
> > > > > >
> > > > > > > Additional custom claim validations applied to the inbound JWT.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > >
> > > > > > > (structure)
> > > > > > >
> > > > > > > > A validation rule applied to a single claim of an inbound JWT.
> > > > > > > >
> > > > > > > > inboundTokenClaimName -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The name of the claim in the inbound token to validate.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `255`
> > > > > > > > > - pattern: `[A-Za-z0-9_.-:]+`
> > > > > > > >
> > > > > > > > inboundTokenClaimValueType -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The value type of the claim in the inbound token, either a string or an array of strings.
> > > > > > > > >
> > > > > > > > > Possible values:
> > > > > > > > >
> > > > > > > > > - `STRING`
> > > > > > > > > - `STRING_ARRAY`
> > > > > > > >
> > > > > > > > authorizingClaimMatchValue -\> (structure) \[required\]
> > > > > > > >
> > > > > > > > > The value and match operator used to authorize the claim.
> > > > > > > > >
> > > > > > > > > claimMatchValue -\> (tagged union structure) \[required\]
> > > > > > > > >
> > > > > > > > > > The expected value or values that the claim is compared against.
> > > > > > > > > >
> > > > > > > > > > ### Note
> > > > > > > > > >
> > > > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `matchValueString`, `matchValueStringList`.
> > > > > > > > > >
> > > > > > > > > > matchValueString -\> (string)
> > > > > > > > > >
> > > > > > > > > > > A single string value to match the claim against.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `1`
> > > > > > > > > > > - max: `255`
> > > > > > > > > > > - pattern: `[A-Za-z0-9_.:/-]+`
> > > > > > > > > >
> > > > > > > > > > matchValueStringList -\> (list)
> > > > > > > > > >
> > > > > > > > > > > A list of string values to match the claim against.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `1`
> > > > > > > > > > >
> > > > > > > > > > > (string)
> > > > > > > > > > >
> > > > > > > > > > > > A single value used to match a claim during JWT validation.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > - max: `255`
> > > > > > > > > > > > - pattern: `[A-Za-z0-9_.:/-]+`
> > > > > > > > >
> > > > > > > > > claimMatchOperator -\> (string) \[required\]
> > > > > > > > >
> > > > > > > > > > The operator used to compare the claim value against the expected value.
> > > > > > > > > >
> > > > > > > > > > Possible values:
> > > > > > > > > >
> > > > > > > > > > - `EQUALS`
> > > > > > > > > > - `CONTAINS`
> > > > > > > > > > - `CONTAINS_ANY`
> > > > > >
> > > > > > privateEndpoint -\> (tagged union structure)
> > > > > >
> > > > > > > The private endpoint used to reach the identity provider’s discovery URL over a private network path.
> > > > > > >
> > > > > > > ### Note
> > > > > > >
> > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `selfManagedLatticeResource`, `managedVpcResource`.
> > > > > > >
> > > > > > > selfManagedLatticeResource -\> (tagged union structure)
> > > > > > >
> > > > > > > > A private endpoint backed by a self-managed VPC Lattice resource configuration.
> > > > > > > >
> > > > > > > > ### Note
> > > > > > > >
> > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `resourceConfigurationIdentifier`.
> > > > > > > >
> > > > > > > > resourceConfigurationIdentifier -\> (string)
> > > > > > > >
> > > > > > > > > The identifier of the VPC Lattice resource configuration, specified as a resource configuration ID or ARN.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `20`
> > > > > > > > > - max: `2048`
> > > > > > > > > - pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`
> > > > > > >
> > > > > > > managedVpcResource -\> (structure)
> > > > > > >
> > > > > > > > A private endpoint backed by a service-managed VPC resource.
> > > > > > > >
> > > > > > > > vpcIdentifier -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The identifier of the VPC in which the private endpoint is provisioned.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `10`
> > > > > > > > > - max: `48`
> > > > > > > > > - pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > > > >
> > > > > > > > subnetIds -\> (list) \[required\]
> > > > > > > >
> > > > > > > > > The identifiers of the subnets in which the private endpoint network interfaces are placed.
> > > > > > > > >
> > > > > > > > > (string)
> > > > > > > > >
> > > > > > > > > > Subnet identifier
> > > > > > > > > >
> > > > > > > > > > Constraints:
> > > > > > > > > >
> > > > > > > > > > - min: `15`
> > > > > > > > > > - max: `24`
> > > > > > > > > > - pattern: `subnet-[0-9a-zA-Z]{8,17}`
> > > > > > > >
> > > > > > > > endpointIpAddressType -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The IP address type used by the private endpoint, either IPV4 or IPV6.
> > > > > > > > >
> > > > > > > > > Possible values:
> > > > > > > > >
> > > > > > > > > - `IPV4`
> > > > > > > > > - `IPV6`
> > > > > > > >
> > > > > > > > securityGroupIds -\> (list)
> > > > > > > >
> > > > > > > > > The identifiers of the security groups associated with the private endpoint network interfaces.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `0`
> > > > > > > > > - max: `5`
> > > > > > > > >
> > > > > > > > > (string)
> > > > > > > > >
> > > > > > > > > > The identifier of a security group.
> > > > > > > > > >
> > > > > > > > > > Constraints:
> > > > > > > > > >
> > > > > > > > > > - min: `10`
> > > > > > > > > > - max: `48`
> > > > > > > > > > - pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > > > >
> > > > > > > > tags -\> (map)
> > > > > > > >
> > > > > > > > > The tags applied to the service-managed VPC resource.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `50`
> > > > > > > > >
> > > > > > > > > key -\> (string)
> > > > > > > > >
> > > > > > > > > > Key of a tag.
> > > > > > > > > >
> > > > > > > > > > Constraints:
> > > > > > > > > >
> > > > > > > > > > - min: `1`
> > > > > > > > > > - max: `128`
> > > > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > > > > >
> > > > > > > > > value -\> (string)
> > > > > > > > >
> > > > > > > > > > Value of a tag.
> > > > > > > > > >
> > > > > > > > > > Constraints:
> > > > > > > > > >
> > > > > > > > > > - min: `0`
> > > > > > > > > > - max: `256`
> > > > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > > > >
> > > > > > > > routingDomain -\> (string)
> > > > > > > >
> > > > > > > > > The routing domain used to resolve traffic through the private endpoint.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `3`
> > > > > > > > > - max: `255`
> > > > > >
> > > > > > privateEndpointOverrides -\> (list)
> > > > > >
> > > > > > > Per-domain private endpoint overrides that route specific identity provider domains through distinct private endpoints.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `0`
> > > > > > > - max: `5`
> > > > > > >
> > > > > > > (structure)
> > > > > > >
> > > > > > > > A mapping of a domain to the private endpoint used to reach it.
> > > > > > > >
> > > > > > > > domain -\> (string) \[required\]
> > > > > > > >
> > > > > > > > > The domain name to which this private endpoint override applies.
> > > > > > > > >
> > > > > > > > > Constraints:
> > > > > > > > >
> > > > > > > > > - min: `1`
> > > > > > > > > - max: `253`
> > > > > > > >
> > > > > > > > privateEndpoint -\> (tagged union structure) \[required\]
> > > > > > > >
> > > > > > > > > The private endpoint used to reach the specified domain.
> > > > > > > > >
> > > > > > > > > ### Note
> > > > > > > > >
> > > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `selfManagedLatticeResource`, `managedVpcResource`.
> > > > > > > > >
> > > > > > > > > selfManagedLatticeResource -\> (tagged union structure)
> > > > > > > > >
> > > > > > > > > > A private endpoint backed by a self-managed VPC Lattice resource configuration.
> > > > > > > > > >
> > > > > > > > > > ### Note
> > > > > > > > > >
> > > > > > > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `resourceConfigurationIdentifier`.
> > > > > > > > > >
> > > > > > > > > > resourceConfigurationIdentifier -\> (string)
> > > > > > > > > >
> > > > > > > > > > > The identifier of the VPC Lattice resource configuration, specified as a resource configuration ID or ARN.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `20`
> > > > > > > > > > > - max: `2048`
> > > > > > > > > > > - pattern: `((rcfg-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:resourceconfiguration/rcfg-[0-9a-z]{17}))`
> > > > > > > > >
> > > > > > > > > managedVpcResource -\> (structure)
> > > > > > > > >
> > > > > > > > > > A private endpoint backed by a service-managed VPC resource.
> > > > > > > > > >
> > > > > > > > > > vpcIdentifier -\> (string) \[required\]
> > > > > > > > > >
> > > > > > > > > > > The identifier of the VPC in which the private endpoint is provisioned.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `10`
> > > > > > > > > > > - max: `48`
> > > > > > > > > > > - pattern: `vpc-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > > > > > >
> > > > > > > > > > subnetIds -\> (list) \[required\]
> > > > > > > > > >
> > > > > > > > > > > The identifiers of the subnets in which the private endpoint network interfaces are placed.
> > > > > > > > > > >
> > > > > > > > > > > (string)
> > > > > > > > > > >
> > > > > > > > > > > > Subnet identifier
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `15`
> > > > > > > > > > > > - max: `24`
> > > > > > > > > > > > - pattern: `subnet-[0-9a-zA-Z]{8,17}`
> > > > > > > > > >
> > > > > > > > > > endpointIpAddressType -\> (string) \[required\]
> > > > > > > > > >
> > > > > > > > > > > The IP address type used by the private endpoint, either IPV4 or IPV6.
> > > > > > > > > > >
> > > > > > > > > > > Possible values:
> > > > > > > > > > >
> > > > > > > > > > > - `IPV4`
> > > > > > > > > > > - `IPV6`
> > > > > > > > > >
> > > > > > > > > > securityGroupIds -\> (list)
> > > > > > > > > >
> > > > > > > > > > > The identifiers of the security groups associated with the private endpoint network interfaces.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `0`
> > > > > > > > > > > - max: `5`
> > > > > > > > > > >
> > > > > > > > > > > (string)
> > > > > > > > > > >
> > > > > > > > > > > > The identifier of a security group.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `10`
> > > > > > > > > > > > - max: `48`
> > > > > > > > > > > > - pattern: `sg-(([0-9a-z]{8})|([0-9a-z]{17}))`
> > > > > > > > > >
> > > > > > > > > > tags -\> (map)
> > > > > > > > > >
> > > > > > > > > > > The tags applied to the service-managed VPC resource.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `1`
> > > > > > > > > > > - max: `50`
> > > > > > > > > > >
> > > > > > > > > > > key -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > Key of a tag.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `1`
> > > > > > > > > > > > - max: `128`
> > > > > > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > > > > > > >
> > > > > > > > > > > value -\> (string)
> > > > > > > > > > >
> > > > > > > > > > > > Value of a tag.
> > > > > > > > > > > >
> > > > > > > > > > > > Constraints:
> > > > > > > > > > > >
> > > > > > > > > > > > - min: `0`
> > > > > > > > > > > > - max: `256`
> > > > > > > > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > > > > > > >
> > > > > > > > > > routingDomain -\> (string)
> > > > > > > > > >
> > > > > > > > > > > The routing domain used to resolve traffic through the private endpoint.
> > > > > > > > > > >
> > > > > > > > > > > Constraints:
> > > > > > > > > > >
> > > > > > > > > > > - min: `3`
> > > > > > > > > > > - max: `255`
> > > >
> > > > workloadIdentityDetails -\> (structure)
> > > >
> > > > > Workload identity details associated with a source resource.
> > > > >
> > > > > workloadIdentityArn -\> (string) \[required\]
> > > > >
> > > > > > The Amazon Resource Name (ARN) of the workload identity associated with the source resource.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `1024`

createdByAutoDetection -\> (boolean)

> Specifies whether the registry record was created by auto-detection. `true` indicates the record was automatically created by the service based on the registry’s auto-detection configuration; `false` indicates the record was created through a control-plane API call.

createdBy -\> (string)

> The ID of the Amazon Web Services account that created the registry record.
>
> Constraints:
>
> - min: `12`
> - max: `12`
> - pattern: `[0-9]{12}`

- [← update-registry](update-registry.html "previous chapter (use the left arrow)") /
- [update-registry-record-status →](update-registry-record-status.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](update-registry-record-status.html "update-registry-record-status") \|
- [previous](update-registry.html "update-registry") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [agent-registry-control](index.html) »
- [update-registry-record]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

---
title: aws bedrock-agentcore-control create-registry-record
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/create-registry-record.html
fetched: '2026-09-26'
tags:
- agent-registry
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# create-registry-record

## Description

Creates a new registry record within the specified registry. A registry record represents an individual AI resource’s metadata in the registry. This could be an MCP server (and associated tools), A2A agent, agent skill, or a custom resource with a custom schema.

The record is processed asynchronously and returns HTTP 202 Accepted.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/CreateRegistryRecord)

## Synopsis

      create-registry-record
    --registry-id <value>
    --name <value>
    [--description <value>]
    --descriptor-type <value>
    [--descriptors <value>]
    [--record-version <value>]
    [--synchronization-type <value>]
    [--synchronization-configuration <value>]
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

`--registry-id` (string) \[required\]

> The identifier of the registry where the record will be created. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `(arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/)?[a-zA-Z0-9]{12,16}`

`--name` (string) \[required\]

> The name of the registry record.
>
> Constraints:
>
> - min: `1`
> - max: `255`
> - pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`

`--description` (string)

> A description of the registry record.
>
> Constraints:
>
> - min: `1`
> - max: `4096`

`--descriptor-type` (string) \[required\]

> The descriptor type of the registry record.
>
> - `MCP` - Model Context Protocol descriptor for MCP-compatible servers and tools.
> - `A2A` - Agent-to-Agent protocol descriptor.
> - `CUSTOM` - Custom descriptor type for resources such as APIs, Lambda functions, or servers not conforming to a standard protocol.
> - `AGENT_SKILLS` - Agent skills descriptor for defining agent skill definitions.
>
> Possible values:
>
> - `MCP`
> - `A2A`
> - `CUSTOM`
> - `AGENT_SKILLS`

`--descriptors` (structure)

> The descriptor-type-specific configuration containing the resource schema and metadata. The structure of this field depends on the `descriptorType` you specify.
>
> mcp -\> (structure)
>
> > The Model Context Protocol (MCP) descriptor configuration. Use this when the `descriptorType` is `MCP` .
> >
> > server -\> (structure)
> >
> > > The MCP server definition, containing the server configuration and schema as defined by the MCP protocol specification.
> > >
> > > schemaVersion -\> (string)
> > >
> > > > The schema version of the server definition based on the MCP protocol specification. If not specified, the version is auto-detected from the content.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `255`
> > >
> > > inlineContent -\> (string)
> > >
> > > > The JSON content containing the MCP server definition, conforming to the MCP protocol specification.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `102400`
> >
> > tools -\> (structure)
> >
> > > The MCP tools definition, containing the tools available on the MCP server as defined by the MCP protocol specification.
> > >
> > > protocolVersion -\> (string)
> > >
> > > > The protocol version of the tools definition based on the MCP protocol specification. If not specified, the version is auto-detected from the content.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `255`
> > >
> > > inlineContent -\> (string)
> > >
> > > > The JSON content containing the MCP tools definition, conforming to the MCP protocol specification.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `102400`
>
> a2a -\> (structure)
>
> > The Agent-to-Agent (A2A) protocol descriptor configuration. Use this when the `descriptorType` is `A2A` .
> >
> > agentCard -\> (structure)
> >
> > > The agent card definition for the A2A agent, as defined by the A2A protocol specification.
> > >
> > > schemaVersion -\> (string)
> > >
> > > > The schema version of the agent card based on the A2A protocol specification.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `255`
> > >
> > > inlineContent -\> (string)
> > >
> > > > The JSON content containing the A2A agent card definition, conforming to the A2A protocol specification.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `102400`
>
> custom -\> (structure)
>
> > The custom descriptor configuration. Use this when the `descriptorType` is `CUSTOM` .
> >
> > inlineContent -\> (string)
> >
> > > The custom descriptor content as a valid JSON document. You can define any custom schema that describes your resource.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `102400`
>
> agentSkills -\> (structure)
>
> > The agent skills descriptor configuration. Use this when the `descriptorType` is `AGENT_SKILLS` .
> >
> > skillMd -\> (structure)
> >
> > > The optional skill markdown definition describing the agent’s skills in a human-readable format.
> > >
> > > inlineContent -\> (string)
> > >
> > > > The markdown content describing the agent’s skills in a human-readable format.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `102400`
> >
> > skillDefinition -\> (structure)
> >
> > > The structured skill definition with schema version and content.
> > >
> > > schemaVersion -\> (string)
> > >
> > > > The version of the skill definition schema.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `255`
> > >
> > > inlineContent -\> (string)
> > >
> > > > The JSON content containing the structured skill definition.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `102400`

Shorthand Syntax:

    mcp={server={schemaVersion=string,inlineContent=string},tools={protocolVersion=string,inlineContent=string}},a2a={agentCard={schemaVersion=string,inlineContent=string}},custom={inlineContent=string},agentSkills={skillMd={inlineContent=string},skillDefinition={schemaVersion=string,inlineContent=string}}

JSON Syntax:

    {
      "mcp": {
        "server": {
          "schemaVersion": "string",
          "inlineContent": "string"
        },
        "tools": {
          "protocolVersion": "string",
          "inlineContent": "string"
        }
      },
      "a2a": {
        "agentCard": {
          "schemaVersion": "string",
          "inlineContent": "string"
        }
      },
      "custom": {
        "inlineContent": "string"
      },
      "agentSkills": {
        "skillMd": {
          "inlineContent": "string"
        },
        "skillDefinition": {
          "schemaVersion": "string",
          "inlineContent": "string"
        }
      }
    }

`--record-version` (string)

> The version of the registry record. Use this to track different versions of the record’s content.
>
> Constraints:
>
> - min: `1`
> - max: `255`
> - pattern: `[a-zA-Z0-9.-]+`

`--synchronization-type` (string)

> The type of synchronization to use for keeping the record metadata up to date from an external source. Possible values include `FROM_URL` and `NONE` .
>
> Possible values:
>
> - `URL`

`--synchronization-configuration` (structure)

> The configuration for synchronizing registry record metadata from an external source, such as a URL-based MCP server.
>
> fromUrl -\> (structure)
>
> > Configuration for synchronizing from a URL-based source.
> >
> > url -\> (string) \[required\]
> >
> > > The HTTPS URL of the MCP server to synchronize from.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `2048`
> > > - pattern: `https://.*`
> >
> > credentialProviderConfigurations -\> (list)
> >
> > > Optional list of credential provider configurations for authenticating with the MCP server. At most one credential provider configuration can be specified.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `1`
> > >
> > > (structure)
> > >
> > > > A pairing of a credential provider type with its corresponding provider details for authenticating with external sources.
> > > >
> > > > credentialProviderType -\> (string) \[required\]
> > > >
> > > > > The type of credential provider.
> > > > >
> > > > > - `OAUTH` - OAuth-based authentication.
> > > > > - `IAM` - Amazon Web Services IAM-based authentication using SigV4 signing.
> > > > >
> > > > > Possible values:
> > > > >
> > > > > - `OAUTH`
> > > > > - `IAM`
> > > >
> > > > credentialProvider -\> (tagged union structure) \[required\]
> > > >
> > > > > The credential provider configuration details. The structure depends on the `credentialProviderType` .
> > > > >
> > > > > ### Note
> > > > >
> > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `oauthCredentialProvider`, `iamCredentialProvider`.
> > > > >
> > > > > oauthCredentialProvider -\> (structure)
> > > > >
> > > > > > The OAuth credential provider configuration for authenticating with the external source.
> > > > > >
> > > > > > providerArn -\> (string) \[required\]
> > > > > >
> > > > > > > The Amazon Resource Name (ARN) of the OAuth credential provider resource.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:.*`
> > > > > >
> > > > > > grantType -\> (string)
> > > > > >
> > > > > > > The OAuth grant type. Currently only `CLIENT_CREDENTIALS` is supported.
> > > > > > >
> > > > > > > Possible values:
> > > > > > >
> > > > > > > - `CLIENT_CREDENTIALS`
> > > > > >
> > > > > > scopes -\> (list)
> > > > > >
> > > > > > > The OAuth scopes to request during authentication.
> > > > > > >
> > > > > > > (string)
> > > > > >
> > > > > > customParameters -\> (map)
> > > > > >
> > > > > > > Additional custom parameters for the OAuth flow.
> > > > > > >
> > > > > > > key -\> (string)
> > > > > > >
> > > > > > > value -\> (string)
> > > > >
> > > > > iamCredentialProvider -\> (structure)
> > > > >
> > > > > > The IAM credential provider configuration for authenticating with the external source using SigV4 signing.
> > > > > >
> > > > > > roleArn -\> (string)
> > > > > >
> > > > > > > The Amazon Resource Name (ARN) of the IAM role to assume for SigV4 signing.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `20`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:role/.+`
> > > > > >
> > > > > > service -\> (string)
> > > > > >
> > > > > > > The SigV4 signing service name (for example, `execute-api` or `bedrock-agentcore` ).
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `128`
> > > > > > > - pattern: `[a-zA-Z0-9_-]+`
> > > > > >
> > > > > > region -\> (string)
> > > > > >
> > > > > > > The Amazon Web Services region for SigV4 signing (for example, `us-west-2` ). If not specified, the region is extracted from the MCP server URL hostname, with fallback to the service’s own region.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `64`
> > > > > > > - pattern: `[a-z0-9-]+`

JSON Syntax:

    {
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

`--client-token` (string)

> A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don’t specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn’t return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) .
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

recordArn -\> (string)

> The Amazon Resource Name (ARN) of the created registry record.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}`

status -\> (string)

> The status of the registry record. Set to `CREATING` while the asynchronous workflow is in progress.
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

- [← create-registry](create-registry.html "previous chapter (use the left arrow)") /
- [create-workload-identity →](create-workload-identity.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](create-workload-identity.html "create-workload-identity") \|
- [previous](create-registry.html "create-registry") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [create-registry-record]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

---
title: aws bedrock-agentcore-control create-consent-portal
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/create-consent-portal.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# create-consent-portal

## Description

Creates a new consent portal.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/CreateConsentPortal)

## Synopsis

      create-consent-portal
    --execution-role-arn <value>
    --idp-config <value>
    --name <value>
    --sources <value>
    [--description <value>]
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

`--execution-role-arn` (string) \[required\]

> The Amazon Resource Name (ARN) of the IAM role that the consent portal assumes to access the resources defined in its sources.
>
> Constraints:
>
> - pattern: `arn:aws(-[a-z-]+)?:iam::[0-9]{12}:role/[a-zA-Z0-9+=,.@\-_/]+`

`--idp-config` (structure) \[required\]

> The identity provider configuration that the consent portal uses to authenticate end users.
>
> credentialProviderArn -\> (string) \[required\]
>
> > The Amazon Resource Name (ARN) of the OAuth2 credential provider used to authenticate end users to the consent portal.
> >
> > Constraints:
> >
> > - pattern: `arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b|aws-iso-e|aws-iso-f|aws-eusc):bedrock-agentcore:[a-z0-9-]{1,32}:[0-9]{12}:token-vault/[a-zA-Z0-9_-]{1,64}/oauth2credentialprovider/[a-zA-Z0-9_-]{1,128}`
>
> scopes -\> (list) \[required\]
>
> > The OAuth2 scopes that the consent portal requests when authenticating end users.
> >
> > Constraints:
> >
> > - min: `1`
> >
> > (string)
> >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `255`
> > > - pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
>
> audience -\> (string)
>
> > The audience value that the consent portal includes when requesting tokens from the identity provider.

Shorthand Syntax:

    credentialProviderArn=string,scopes=string,string,audience=string

JSON Syntax:

    {
      "credentialProviderArn": "string",
      "scopes": ["string", ...],
      "audience": "string"
    }

`--name` (string) \[required\]

> The name of the consent portal. The name must be unique within your account.
>
> Constraints:
>
> - min: `1`
> - max: `50`
> - pattern: `[a-zA-Z0-9_-]{1,50}`

`--sources` (list) \[required\]

> The resources served by the consent portal. Currently, we only support type `agentcore-gateway` .
>
> Constraints:
>
> - min: `1`
> - max: `1`
>
> (structure)
>
> > A resource served by the consent portal.
> >
> > identifier -\> (string) \[required\]
> >
> > > The identifier of the source resource. For an `agentcore-gateway` source, this is the gateway ID or its Amazon Resource Name (ARN).
> > >
> > > Constraints:
> > >
> > > - pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}$|^arn:aws(-[a-z-]+)?:bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}`
> >
> > type -\> (string) \[required\]
> >
> > > The type of the source resource.
> > >
> > > Possible values:
> > >
> > > - `agentcore-gateway`

Shorthand Syntax:

    identifier=string,type=string ...

JSON Syntax:

    [
      {
        "identifier": "string",
        "type": "agentcore-gateway"
      }
      ...
    ]

`--description` (string)

> The description of the consent portal.
>
> Constraints:
>
> - min: `0`
> - max: `512`

`--tags` (map)

> A map of tag keys and values to assign to the consent portal. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.
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

sources -\> (list)

> The resources served by the consent portal.
>
> Constraints:
>
> - min: `1`
> - max: `1`
>
> (structure)
>
> > A resource served by the consent portal.
> >
> > identifier -\> (string) \[required\]
> >
> > > The identifier of the source resource. For an `agentcore-gateway` source, this is the gateway ID or its Amazon Resource Name (ARN).
> > >
> > > Constraints:
> > >
> > > - pattern: `([0-9a-z][-]?){1,100}-[0-9a-z]{10}$|^arn:aws(-[a-z-]+)?:bedrock-agentcore:[a-z0-9-]{1,20}:[0-9]{12}:gateway/([0-9a-z][-]?){1,48}-[a-z0-9]{10}`
> >
> > type -\> (string) \[required\]
> >
> > > The type of the source resource.
> > >
> > > Possible values:
> > >
> > > - `agentcore-gateway`

consentPortalArn -\> (string)

> The Amazon Resource Name (ARN) of the consent portal.
>
> Constraints:
>
> - pattern: `arn:aws[^:]*:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:consent-portal/[a-zA-Z0-9\-_]{1,50}-[A-Za-z0-9]{10}`

consentPortalId -\> (string)

> The unique identifier of the consent portal.
>
> Constraints:
>
> - pattern: `[a-zA-Z0-9\-_]{1,50}-[A-Za-z0-9]{10}`

createdAt -\> (timestamp)

> The timestamp for when the consent portal was created.

description -\> (string)

> The description of the consent portal.
>
> Constraints:
>
> - min: `0`
> - max: `512`

executionRoleArn -\> (string)

> The Amazon Resource Name (ARN) of the IAM role that the consent portal assumes to access the resources defined in its sources.
>
> Constraints:
>
> - pattern: `arn:aws(-[a-z-]+)?:iam::[0-9]{12}:role/[a-zA-Z0-9+=,.@\-_/]+`

idpConfig -\> (structure)

> The identity provider configuration that the consent portal uses to authenticate end users.
>
> credentialProviderArn -\> (string) \[required\]
>
> > The Amazon Resource Name (ARN) of the OAuth2 credential provider used to authenticate end users to the consent portal.
> >
> > Constraints:
> >
> > - pattern: `arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b|aws-iso-e|aws-iso-f|aws-eusc):bedrock-agentcore:[a-z0-9-]{1,32}:[0-9]{12}:token-vault/[a-zA-Z0-9_-]{1,64}/oauth2credentialprovider/[a-zA-Z0-9_-]{1,128}`
>
> scopes -\> (list) \[required\]
>
> > The OAuth2 scopes that the consent portal requests when authenticating end users.
> >
> > Constraints:
> >
> > - min: `1`
> >
> > (string)
> >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `255`
> > > - pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
>
> audience -\> (string)
>
> > The audience value that the consent portal includes when requesting tokens from the identity provider.

name -\> (string)

> The name of the consent portal.
>
> Constraints:
>
> - min: `1`
> - max: `50`
> - pattern: `[a-zA-Z0-9_-]{1,50}`

portalUrl -\> (string)

> The URL used to access the consent portal.
>
> Constraints:
>
> - min: `1`
> - max: `2000`

status -\> (string)

> The current status of the consent portal.
>
> Possible values:
>
> - `CREATING`
> - `ACTIVE`
> - `UPDATING`
> - `UPDATE_FAILED`
> - `DELETING`
> - `FAILED`

statusReason -\> (string)

> A message that provides additional information about the current status of the consent portal.
>
> Constraints:
>
> - min: `1`
> - max: `1024`

updatedAt -\> (timestamp)

> The timestamp for when the consent portal was last updated.

- [← create-configuration-bundle](create-configuration-bundle.html "previous chapter (use the left arrow)") /
- [create-dataset →](create-dataset.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](create-dataset.html "create-dataset") \|
- [previous](create-configuration-bundle.html "create-configuration-bundle") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [create-consent-portal]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

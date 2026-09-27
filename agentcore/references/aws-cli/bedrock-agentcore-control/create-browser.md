---
title: aws bedrock-agentcore-control create-browser
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/create-browser.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# create-browser

## Description

Creates a custom browser.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/CreateBrowser)

## Synopsis

      create-browser
    --name <value>
    [--description <value>]
    [--execution-role-arn <value>]
    --network-configuration <value>
    [--recording <value>]
    [--browser-signing <value>]
    [--enterprise-policies <value>]
    [--certificates <value>]
    [--filesystem-configurations <value>]
    [--client-token <value>]
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

> The name of the browser. The name must be unique within your account.
>
> Constraints:
>
> - pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`

`--description` (string)

> The description of the browser.
>
> Constraints:
>
> - min: `1`
> - max: `4096`

`--execution-role-arn` (string)

> The Amazon Resource Name (ARN) of the IAM role that provides permissions for the browser to access Amazon Web Services services.
>
> Constraints:
>
> - min: `1`
> - max: `2048`
> - pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`

`--network-configuration` (structure) \[required\]

> The network configuration for the browser. This configuration specifies the network mode for the browser.
>
> networkMode -\> (string) \[required\]
>
> > The network mode for the browser. This field specifies how the browser connects to the network.
> >
> > Possible values:
> >
> > - `PUBLIC`
> > - `VPC`
>
> vpcConfig -\> (structure)
>
> > The VPC configuration for the browser. This configuration is required when the network mode is set to `VPC` .
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

Shorthand Syntax:

    networkMode=string,vpcConfig={securityGroups=[string,string],subnets=[string,string],requireServiceS3Endpoint=boolean}

JSON Syntax:

    {
      "networkMode": "PUBLIC"|"VPC",
      "vpcConfig": {
        "securityGroups": ["string", ...],
        "subnets": ["string", ...],
        "requireServiceS3Endpoint": true|false
      }
    }

`--recording` (structure)

> The recording configuration for the browser. When enabled, browser sessions are recorded and stored in the specified Amazon S3 location.
>
> enabled -\> (boolean)
>
> > Indicates whether recording is enabled for the browser. When set to true, browser sessions are recorded.
>
> s3Location -\> (structure)
>
> > The Amazon S3 location where browser recordings are stored. This location contains the recorded browser sessions.
> >
> > bucket -\> (string) \[required\]
> >
> > > The name of the Amazon S3 bucket. This bucket contains the stored data.
> > >
> > > Constraints:
> > >
> > > - pattern: `[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]`
> >
> > prefix -\> (string) \[required\]
> >
> > > The prefix for objects in the Amazon S3 bucket. This prefix is added to the object keys to organize the data.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `1024`
> >
> > versionId -\> (string)
> >
> > > The version ID of the Amazon Amazon S3 object. If not specified, the latest version of the object is used.
> > >
> > > Constraints:
> > >
> > > - min: `3`
> > > - max: `1024`

Shorthand Syntax:

    enabled=boolean,s3Location={bucket=string,prefix=string,versionId=string}

JSON Syntax:

    {
      "enabled": true|false,
      "s3Location": {
        "bucket": "string",
        "prefix": "string",
        "versionId": "string"
      }
    }

`--browser-signing` (structure)

> The browser signing configuration that enables cryptographic agent identification using HTTP message signatures for web bot authentication.
>
> enabled -\> (boolean) \[required\]
>
> > Specifies whether browser signing is enabled. When enabled, the browser will cryptographically sign HTTP requests to identify itself as an AI agent to bot control vendors.

Shorthand Syntax:

    enabled=boolean

JSON Syntax:

    {
      "enabled": true|false
    }

`--enterprise-policies` (list)

> A list of enterprise policy files for the browser.
>
> Constraints:
>
> - min: `0`
> - max: `100`
>
> (structure)
>
> > Browser enterprise policy configuration.
> >
> > location -\> (tagged union structure) \[required\]
> >
> > > The location of the enterprise policy file.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `s3`.
> > >
> > > s3 -\> (structure)
> > >
> > > > The Amazon S3 location for storing data. This structure defines where in Amazon S3 data is stored.
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
> > type -\> (string)
> >
> > > The type of browser enterprise policy. Available values are `MANAGED` and `RECOMMENDED` .
> > >
> > > Possible values:
> > >
> > > - `MANAGED`
> > > - `RECOMMENDED`

Shorthand Syntax:

    location={s3={bucket=string,prefix=string,versionId=string}},type=string ...

JSON Syntax:

    [
      {
        "location": {
          "s3": {
            "bucket": "string",
            "prefix": "string",
            "versionId": "string"
          }
        },
        "type": "MANAGED"|"RECOMMENDED"
      }
      ...
    ]

`--certificates` (list)

> A list of certificates to install in the browser.
>
> Constraints:
>
> - min: `1`
> - max: `200`
>
> (structure)
>
> > A certificate to install in the browser or code interpreter.
> >
> > location -\> (tagged union structure) \[required\]
> >
> > > The location of the certificate.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `secretsManager`.
> > >
> > > secretsManager -\> (structure)
> > >
> > > > The Amazon Web Services Secrets Manager location of the certificate.
> > > >
> > > > secretArn -\> (string) \[required\]
> > > >
> > > > > The ARN of the Amazon Web Services Secrets Manager secret containing the certificate.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `arn:aws(-[a-z-]+)?:secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9/_+=.@-]+`

Shorthand Syntax:

    location={secretsManager={secretArn=string}} ...

JSON Syntax:

    [
      {
        "location": {
          "secretsManager": {
            "secretArn": "string"
          }
        }
      }
      ...
    ]

`--filesystem-configurations` (list)

> The file system configurations to mount into the browser. Use these configurations to mount your own Amazon Simple Storage Service (Amazon S3) Files or Amazon Elastic File System (Amazon EFS) access points. Your sessions can then access your data. If you don’t specify this field, no file systems are mounted.
>
> Constraints:
>
> - min: `0`
> - max: `10`
>
> (tagged union structure)
>
> > Specifies a file system to mount into the session by providing exactly one of the following:
> >
> > - `s3FilesConfiguration` - Mounts an Amazon Simple Storage Service (Amazon S3) Files access point.
> > - `efsConfiguration` - Mounts an Amazon Elastic File System (Amazon EFS) access point.
> >
> > ### Note
> >
> > This is a Tagged Union structure. Only one of the following top level keys can be set: `s3FilesConfiguration`, `efsConfiguration`.
> >
> > s3FilesConfiguration -\> (structure)
> >
> > > The configuration for mounting your own Amazon Simple Storage Service (Amazon S3) Files access point into the session.
> > >
> > > accessPointArn -\> (string) \[required\]
> > >
> > > > The Amazon Resource Name (ARN) of the Amazon Simple Storage Service (Amazon S3) Files access point to mount.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0`
> > > > - max: `256`
> > > > - pattern: `arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}/access-point/fsap-[0-9a-f]{17,40}`
> > >
> > > mountPath -\> (string) \[required\]
> > >
> > > > The absolute path within the session at which the access point is mounted, for example `/mnt/s3data` . Each mount path must be unique across all file system configurations in the session.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `6`
> > > > - max: `200`
> > > > - pattern: `/mnt/[a-zA-Z0-9._-]+/?`
> > >
> > > fileSystemArn -\> (string) \[required\]
> > >
> > > > The Amazon Resource Name (ARN) of the Amazon Simple Storage Service (Amazon S3) Files file system that owns the access point.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0`
> > > > - max: `256`
> > > > - pattern: `arn:aws[-a-z]*:s3files:[a-z0-9-]+:[0-9]{12}:file-system/fs-[0-9a-f]{17,40}`
> >
> > efsConfiguration -\> (structure)
> >
> > > The configuration for mounting your own Amazon Elastic File System (Amazon EFS) access point into the session.
> > >
> > > accessPointArn -\> (string) \[required\]
> > >
> > > > The Amazon Resource Name (ARN) of the Amazon Elastic File System (Amazon EFS) access point to mount.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0`
> > > > - max: `128`
> > > > - pattern: `arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:access-point/fsap-[0-9a-f]{8,40}`
> > >
> > > mountPath -\> (string) \[required\]
> > >
> > > > The absolute path within the session at which the access point is mounted, for example `/mnt/efs` . Each mount path must be unique across all file system configurations in the session.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `6`
> > > > - max: `200`
> > > > - pattern: `/mnt/[a-zA-Z0-9._-]+/?`
> > >
> > > fileSystemArn -\> (string) \[required\]
> > >
> > > > The Amazon Resource Name (ARN) of the Amazon Elastic File System (Amazon EFS) file system that owns the access point.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `0`
> > > > - max: `256`
> > > > - pattern: `arn:aws[-a-z]*:elasticfilesystem:[a-z0-9-]+:[0-9]{12}:file-system/fs-[0-9a-f]{8,40}`

Shorthand Syntax:

    s3FilesConfiguration={accessPointArn=string,mountPath=string,fileSystemArn=string},efsConfiguration={accessPointArn=string,mountPath=string,fileSystemArn=string} ...

JSON Syntax:

    [
      {
        "s3FilesConfiguration": {
          "accessPointArn": "string",
          "mountPath": "string",
          "fileSystemArn": "string"
        },
        "efsConfiguration": {
          "accessPointArn": "string",
          "mountPath": "string",
          "fileSystemArn": "string"
        }
      }
      ...
    ]

`--client-token` (string)

> A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request but does not return an error.
>
> Constraints:
>
> - min: `33`
> - max: `256`
> - pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`

`--tags` (map)

> A map of tag keys and values to assign to the browser. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.
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

browserId -\> (string)

> The unique identifier of the created browser.
>
> Constraints:
>
> - pattern: `(aws\.browser\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})`

browserArn -\> (string)

> The Amazon Resource Name (ARN) of the created browser.
>
> Constraints:
>
> - pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:(aws|[0-9]{12}):browser(-custom)?/(aws\.browser\.v1|[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10})`

createdAt -\> (timestamp)

> The timestamp when the browser was created.

status -\> (string)

> The current status of the browser.
>
> Possible values:
>
> - `CREATING`
> - `CREATE_FAILED`
> - `READY`
> - `DELETING`
> - `DELETE_FAILED`
> - `DELETED`

- [← create-api-key-credential-provider](create-api-key-credential-provider.html "previous chapter (use the left arrow)") /
- [create-browser-profile →](create-browser-profile.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](create-browser-profile.html "create-browser-profile") \|
- [previous](create-api-key-credential-provider.html "create-api-key-credential-provider") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [create-browser]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

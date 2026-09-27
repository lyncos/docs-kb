---
title: aws bedrock-agentcore start-browser-session
description: \ [aws . bedrock-agentcore \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore/start-browser-session.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore](index.html#cli-aws-bedrock-agentcore) \]

# start-browser-session

## Description

Creates and initializes a browser session in Amazon Bedrock AgentCore. The session enables agents to navigate and interact with web content, extract information from websites, and perform web-based tasks as part of their response generation.

To create a session, you must specify a browser identifier and a name. You can also configure the viewport dimensions to control the visible area of web content. The session remains active until it times out or you explicitly stop it using the `StopBrowserSession` operation.

The following operations are related to `StartBrowserSession` :

- [GetBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html)
- [UpdateBrowserStream](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_UpdateBrowserStream.html)
- [SaveBrowserSessionProfile](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_SaveBrowserSessionProfile.html)
- [StopBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html)
- [InvokeBrowser](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeBrowser.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-2024-02-28/StartBrowserSession)

## Synopsis

      start-browser-session
    [--trace-id <value>]
    [--trace-parent <value>]
    --browser-identifier <value>
    [--name <value>]
    [--session-timeout-seconds <value>]
    [--view-port <value>]
    [--extensions <value>]
    [--profile-configuration <value>]
    [--proxy-configuration <value>]
    [--enterprise-policies <value>]
    [--certificates <value>]
    [--filesystem-configurations <value>]
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

`--trace-id` (string)

> The trace identifier for request tracking.
>
> Constraints:
>
> - min: `0`
> - max: `1024`

`--trace-parent` (string)

> The parent trace information for distributed tracing.
>
> Constraints:
>
> - min: `0`
> - max: `1024`

`--browser-identifier` (string) \[required\]

> The unique identifier of the browser to use for this session. This identifier specifies which browser environment to initialize for the session.

`--name` (string)

> The name of the browser session. This name helps you identify and manage the session. The name does not need to be unique.
>
> Constraints:
>
> - min: `1`
> - max: `100`

`--session-timeout-seconds` (integer)

> The duration in seconds (time-to-live) after which the session automatically terminates, regardless of ongoing activity. Defaults to 3600 seconds (1 hour). Recommended minimum: 60 seconds. Maximum allowed: 28,800 seconds (8 hours).
>
> Constraints:
>
> - min: `1`
> - max: `28800`

`--view-port` (structure)

> The dimensions of the browser viewport for this session. This determines the visible area of the web content and affects how web pages are rendered. If not specified, Amazon Bedrock AgentCore uses a default viewport size.
>
> width -\> (integer) \[required\]
>
> > The width of the viewport in pixels. This value determines the horizontal dimension of the visible area. Valid values range from 800 to 1920 pixels.
> >
> > Constraints:
> >
> > - min: `320`
> > - max: `3840`
>
> height -\> (integer) \[required\]
>
> > The height of the viewport in pixels. This value determines the vertical dimension of the visible area. Valid values range from 600 to 1080 pixels.
> >
> > Constraints:
> >
> > - min: `240`
> > - max: `2160`

Shorthand Syntax:

    width=integer,height=integer

JSON Syntax:

    {
      "width": integer,
      "height": integer
    }

`--extensions` (list)

> A list of browser extensions to load into the browser session.
>
> Constraints:
>
> - min: `1`
> - max: `10`
>
> (structure)
>
> > Browser extension configuration.
> >
> > location -\> (tagged union structure) \[required\]
> >
> > > The location where the browser extension files are stored. This specifies the source from which the extension will be loaded and installed.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `s3`.
> > >
> > > s3 -\> (structure)
> > >
> > > > The Amazon S3 location of the resource. Use this when the resource is stored in an Amazon S3 bucket.
> > > >
> > > > bucket -\> (string) \[required\]
> > > >
> > > > > The name of the Amazon S3 bucket where the resource is stored.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `3`
> > > > > - max: `63`
> > > > > - pattern: `[a-z0-9][a-z0-9.-]*[a-z0-9]`
> > > >
> > > > prefix -\> (string) \[required\]
> > > >
> > > > > The name of the Amazon S3 prefix/key where the resource is stored.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `1024`
> > > >
> > > > versionId -\> (string)
> > > >
> > > > > The name of the Amazon S3 version ID where the resource is stored (Optional).
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `1024`

Shorthand Syntax:

    location={s3={bucket=string,prefix=string,versionId=string}} ...

JSON Syntax:

    [
      {
        "location": {
          "s3": {
            "bucket": "string",
            "prefix": "string",
            "versionId": "string"
          }
        }
      }
      ...
    ]

`--profile-configuration` (structure)

> The browser profile configuration to use for this session. A browser profile contains persistent data such as cookies and local storage that can be reused across multiple browser sessions. If specified, the session initializes with the profile’s stored data, enabling continuity for tasks that require authentication or personalized settings.
>
> profileIdentifier -\> (string) \[required\]
>
> > The unique identifier of the browser profile. This identifier is used to reference the profile when starting new browser sessions or saving session data to the profile.
> >
> > Constraints:
> >
> > - pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}`

Shorthand Syntax:

    profileIdentifier=string

JSON Syntax:

    {
      "profileIdentifier": "string"
    }

`--proxy-configuration` (structure)

> Optional proxy configuration for routing browser traffic through customer-specified proxy servers. When provided, enables HTTP Basic authentication via Amazon Web Services Secrets Manager and domain-based routing rules. Requires `secretsmanager:GetSecretValue` IAM permission for the specified secret ARNs.
>
> proxies -\> (list) \[required\]
>
> > An array of 1-5 proxy server configurations for domain-based routing. Each proxy can specify which domains it handles via `domainPatterns` , enabling flexible routing of different traffic through different proxies based on destination domain.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `5`
> >
> > (tagged union structure)
> >
> > > Union type representing different proxy configurations. Currently supports external customer-managed proxies.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `externalProxy`.
> > >
> > > externalProxy -\> (structure)
> > >
> > > > Configuration for an external customer-managed proxy server.
> > > >
> > > > server -\> (string) \[required\]
> > > >
> > > > > The hostname of the proxy server. Must be a valid DNS hostname (maximum 253 characters).
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `253`
> > > > > - pattern: `[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*`
> > > >
> > > > port -\> (integer) \[required\]
> > > >
> > > > > The port number of the proxy server. Valid range: 1-65535.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `65535`
> > > >
> > > > domainPatterns -\> (list)
> > > >
> > > > > Optional array of domain patterns that should route through this specific proxy. Supports `.example.com` for subdomain matching (matches any subdomain of example.com) or `example.com` for exact domain matching. If omitted, this proxy acts as a catch-all for domains not matched by other proxies. Maximum 100 patterns per proxy, each up to 253 characters.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `100`
> > > > >
> > > > > (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `253`
> > > > > > - pattern: `(\.)?[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*`
> > > >
> > > > credentials -\> (tagged union structure)
> > > >
> > > > > Optional authentication credentials for the proxy server. If omitted, the proxy is accessed without authentication (useful for IP-allowlisted proxies).
> > > > >
> > > > > ### Note
> > > > >
> > > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `basicAuth`.
> > > > >
> > > > > basicAuth -\> (structure)
> > > > >
> > > > > > HTTP Basic Authentication credentials (username and password) stored in Amazon Web Services Secrets Manager.
> > > > > >
> > > > > > secretArn -\> (string) \[required\]
> > > > > >
> > > > > > > The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret containing proxy credentials. The secret must be a JSON object with `username` and `password` string fields that meet validation requirements. The caller must have `secretsmanager:GetSecretValue` permission for this ARN. Example secret format: `{"username":`` ``"proxy_user",`` ``"password":`` ``"secure_password"}`
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - pattern: `arn:aws(-[a-z-]+)?:secretsmanager:[a-z0-9-]+:[0-9]{12}:secret:[a-zA-Z0-9/_+=.@-]+`
>
> bypass -\> (structure)
>
> > Optional configuration for domains that should bypass all proxies and connect directly to their destination, like the internet. Takes precedence over all proxy routing rules.
> >
> > domainPatterns -\> (list)
> >
> > > Array of domain patterns that should bypass the proxy. Supports `.amazonaws.com` for subdomain matching or `amazonaws.com` for exact domain matching. Requests to these domains connect directly without using any proxy. Maximum 253 characters per pattern.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `100`
> > >
> > > (string)
> > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `253`
> > > > - pattern: `(\.)?[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?)*`

JSON Syntax:

    {
      "proxies": [
        {
          "externalProxy": {
            "server": "string",
            "port": integer,
            "domainPatterns": ["string", ...],
            "credentials": {
              "basicAuth": {
                "secretArn": "string"
              }
            }
          }
        }
        ...
      ],
      "bypass": {
        "domainPatterns": ["string", ...]
      }
    }

`--enterprise-policies` (list)

> A list of files containing enterprise policies for the browser.
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
> > > > The Amazon S3 location of the resource. Use this when the resource is stored in an Amazon S3 bucket.
> > > >
> > > > bucket -\> (string) \[required\]
> > > >
> > > > > The name of the Amazon S3 bucket where the resource is stored.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `3`
> > > > > - max: `63`
> > > > > - pattern: `[a-z0-9][a-z0-9.-]*[a-z0-9]`
> > > >
> > > > prefix -\> (string) \[required\]
> > > >
> > > > > The name of the Amazon S3 prefix/key where the resource is stored.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `1024`
> > > >
> > > > versionId -\> (string)
> > > >
> > > > > The name of the Amazon S3 version ID where the resource is stored (Optional).
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `1024`
> >
> > type -\> (string)
> >
> > > The enterprise policy type. See BrowserEnterprisePolicyType.
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

> A list of certificates to install in the browser session.
>
> Constraints:
>
> - min: `1`
> - max: `200`
>
> (structure)
>
> > A certificate to install in the browser or code interpreter session.
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

> The file system configurations to mount into the browser session. Use these configurations to mount your own Amazon Simple Storage Service (Amazon S3) Files or Amazon Elastic File System (Amazon EFS) access points. Your session can then read and write your data. If you don’t specify this field, no additional file systems are mounted.
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

> A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error. This parameter helps prevent the creation of duplicate sessions if there are temporary network issues.
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

browserIdentifier -\> (string)

> The identifier of the browser.

sessionId -\> (string)

> The unique identifier of the created browser session.
>
> Constraints:
>
> - pattern: `[0-9a-zA-Z]{1,40}`

createdAt -\> (timestamp)

> The timestamp when the browser session was created.

streams -\> (structure)

> The streams associated with this browser session. These include the automation stream and live view stream.
>
> automationStream -\> (structure) \[required\]
>
> > The stream that enables programmatic control of the browser. This stream allows agents to perform actions such as navigating to URLs, clicking elements, and filling forms.
> >
> > streamEndpoint -\> (string) \[required\]
> >
> > > The endpoint URL for the automation stream. This URL is used to establish a WebSocket connection to the stream for sending commands and receiving responses.
> > >
> > > Constraints:
> > >
> > > - min: `10`
> > > - max: `512`
> >
> > streamStatus -\> (string) \[required\]
> >
> > > The current status of the automation stream. This indicates whether the stream is available for use. Possible values include ACTIVE, CONNECTING, and DISCONNECTED.
> > >
> > > Possible values:
> > >
> > > - `ENABLED`
> > > - `DISABLED`
>
> liveViewStream -\> (structure)
>
> > The stream that provides a visual representation of the browser content. This stream allows agents to observe the current state of the browser, including rendered web pages and visual elements.
> >
> > streamEndpoint -\> (string)
> >
> > > The endpoint URL for the live view stream. This URL is used to establish a connection to receive visual updates from the browser session.
> > >
> > > Constraints:
> > >
> > > - min: `10`
> > > - max: `512`

- [← start-batch-evaluation](start-batch-evaluation.html "previous chapter (use the left arrow)") /
- [start-code-interpreter-session →](start-code-interpreter-session.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](start-code-interpreter-session.html "start-code-interpreter-session") \|
- [previous](start-batch-evaluation.html "start-batch-evaluation") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore](index.html) »
- [start-browser-session]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

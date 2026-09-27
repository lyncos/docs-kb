---
title: aws bedrock-agentcore invoke-agent-runtime
description: \ [aws . bedrock-agentcore \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore/invoke-agent-runtime.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore](index.html#cli-aws-bedrock-agentcore) \]

# invoke-agent-runtime

## Description

Sends a request to an agent or tool hosted in an Amazon Bedrock AgentCore Runtime and receives responses in real-time.

To invoke an agent, you can specify either the AgentCore Runtime ARN or the agent ID with an account ID, and provide a payload containing your request. When you use the agent ID instead of the full ARN, you don’t need to URL-encode the identifier. You can optionally specify a qualifier to target a specific endpoint of the agent.

This operation supports streaming responses, allowing you to receive partial responses as they become available. We recommend using pagination to ensure that the operation returns quickly and successfully when processing large responses.

For example code, see [Invoke an AgentCore Runtime agent](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-invoke-agent.html) .

If you’re integrating your agent with OAuth, you can’t use the Amazon Web Services SDK to call `InvokeAgentRuntime` . Instead, make a HTTPS request to `InvokeAgentRuntime` . For an example, see [Authenticate and authorize with Inbound Auth and Outbound Auth](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html) .

To use this operation, you must have the `bedrock-agentcore:InvokeAgentRuntime` permission. If you are making a call to `InvokeAgentRuntime` on behalf of a user ID with the `X-Amzn-Bedrock-AgentCore-Runtime-User-Id` header, You require permissions to both actions (`bedrock-agentcore:InvokeAgentRuntime` and `bedrock-agentcore:InvokeAgentRuntimeForUser` ).

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-2024-02-28/InvokeAgentRuntime)

## Synopsis

      invoke-agent-runtime
    [--content-type <value>]
    [--accept <value>]
    [--mcp-session-id <value>]
    [--runtime-session-id <value>]
    [--mcp-protocol-version <value>]
    [--mcp-method <value>]
    [--mcp-name <value>]
    [--runtime-user-id <value>]
    [--trace-id <value>]
    [--trace-parent <value>]
    [--trace-state <value>]
    [--baggage <value>]
    --agent-runtime-arn <value>
    [--qualifier <value>]
    [--account-id <value>]
    --payload <value>
    <outfile>
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

`--content-type` (string)

> The MIME type of the input data in the payload. This tells the agent runtime how to interpret the payload data. Common values include application/json for JSON data.
>
> Constraints:
>
> - min: `1`
> - max: `256`

`--accept` (string)

> The desired MIME type for the response from the agent runtime. This tells the agent runtime what format to use for the response data. Common values include application/json for JSON data.
>
> Constraints:
>
> - min: `1`
> - max: `256`

`--mcp-session-id` (string)

> The identifier of the MCP session.
>
> Constraints:
>
> - min: `1`
> - max: `1024`

`--runtime-session-id` (string)

> The identifier of the runtime session.
>
> Constraints:
>
> - min: `33`
> - max: `256`

`--mcp-protocol-version` (string)

> The version of the MCP protocol being used.
>
> Constraints:
>
> - min: `1`
> - max: `1024`

`--mcp-method` (string)

> The MCP method being invoked. For example, `tools/call` , `resources/read` , or `prompts/get` .
>
> Constraints:
>
> - min: `1`
> - max: `1024`

`--mcp-name` (string)

> The name of the MCP resource, tool, or prompt being accessed. The value depends on the method:
>
> - `tools/call` – The tool name.
> - `resources/read` – The resource URI.
> - `prompts/get` – The prompt name.
>
> Constraints:
>
> - min: `1`
> - max: `1024`

`--runtime-user-id` (string)

> The identifier of the runtime user.
>
> Constraints:
>
> - min: `1`
> - max: `1024`

`--trace-id` (string)

> The trace identifier for request tracking.
>
> Constraints:
>
> - min: `0`
> - max: `128`

`--trace-parent` (string)

> The parent trace information for distributed tracing.
>
> Constraints:
>
> - min: `0`
> - max: `128`

`--trace-state` (string)

> The trace state information for distributed tracing.
>
> Constraints:
>
> - min: `0`
> - max: `512`

`--baggage` (string)

> Additional context information for distributed tracing.
>
> Constraints:
>
> - min: `0`
> - max: `8192`

`--agent-runtime-arn` (string) \[required\]

> The identifier of the agent runtime to invoke. You can specify either the full Amazon Web Services Resource Name (ARN) or the agent ID. If you use the agent ID, you must also provide the `accountId` query parameter.

`--qualifier` (string)

> The qualifier to use for the agent runtime. This is an endpoint name that points to a specific version. If not specified, Amazon Bedrock AgentCore uses the default endpoint of the agent runtime.

`--account-id` (string)

> The identifier of the Amazon Web Services account for the agent runtime resource. This parameter is required when you specify an agent ID instead of the full ARN for `agentRuntimeArn` .
>
> Constraints:
>
> - pattern: `[0-9]{12}`

`--payload` (blob) \[required\]

> The input data to send to the agent runtime. The format of this data depends on the specific agent configuration and must match the specified content type. For most agents, this is a JSON object containing the user’s request.
>
> Constraints:
>
> - min: `0`
> - max: `100000000`

`outfile` (string) \[required\] Filename where the content will be saved

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

runtimeSessionId -\> (string)

> The identifier of the runtime session.
>
> Constraints:
>
> - min: `1`
> - max: `100`
> - pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`

mcpSessionId -\> (string)

> The identifier of the MCP session.
>
> Constraints:
>
> - min: `1`
> - max: `100`
> - pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`

mcpProtocolVersion -\> (string)

> The version of the MCP protocol being used.

traceId -\> (string)

> The trace identifier for request tracking.

traceParent -\> (string)

> The parent trace information for distributed tracing.

traceState -\> (string)

> The trace state information for distributed tracing.

baggage -\> (string)

> Additional context information for distributed tracing.

contentType -\> (string)

> The MIME type of the response data. This indicates how to interpret the response data. Common values include application/json for JSON data.

response -\> (streaming blob)

> The response data from the agent runtime. The format of this data depends on the specific agent configuration and the requested accept type. For most agents, this is a JSON object containing the agent’s response to the user’s request.

statusCode -\> (integer)

> The HTTP status code of the response. A status code of 200 indicates a successful operation. Other status codes indicate various error conditions.

- [← ingest-data](ingest-data.html "previous chapter (use the left arrow)") /
- [invoke-browser →](invoke-browser.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](invoke-browser.html "invoke-browser") \|
- [previous](ingest-data.html "ingest-data") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore](index.html) »
- [invoke-agent-runtime]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

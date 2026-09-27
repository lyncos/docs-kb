---
title: aws bedrock-agentcore invoke-browser
description: \ [aws . bedrock-agentcore \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore/invoke-browser.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore](index.html#cli-aws-bedrock-agentcore) \]

# invoke-browser

## Description

Invokes an operating system-level action on a browser session in Amazon Bedrock AgentCore. This operation provides direct OS-level control over browser sessions, enabling mouse actions, keyboard input, and screenshots that the WebSocket-based Chrome DevTools Protocol (CDP) cannot handle — such as interacting with print dialogs, context menus, and JavaScript alerts.

You send a request with exactly one action in the `BrowserAction` union, and receive a corresponding result in the `BrowserActionResult` union.

The following operations are related to `InvokeBrowser` :

- [StartBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html)
- [GetBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html)
- [StopBrowserSession](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-2024-02-28/InvokeBrowser)

## Synopsis

      invoke-browser
    --browser-identifier <value>
    --session-id <value>
    --action <value>
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

`--browser-identifier` (string) \[required\]

> The unique identifier of the browser associated with the session. This must match the identifier used when creating the session with `StartBrowserSession` .

`--session-id` (string) \[required\]

> The unique identifier of the browser session on which to perform the action. This must be an active session created with `StartBrowserSession` .
>
> Constraints:
>
> - pattern: `[0-9a-zA-Z]{1,40}`

`--action` (tagged union structure) \[required\]

> The browser action to perform. Exactly one member of the `BrowserAction` union must be set per request.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `mouseClick`, `mouseMove`, `mouseDrag`, `mouseScroll`, `keyType`, `keyPress`, `keyShortcut`, `screenshot`.
>
> mouseClick -\> (structure)
>
> > Click at the specified coordinates.
> >
> > x -\> (integer) \[required\]
> >
> > > The X coordinate on screen where the click occurs.
> >
> > y -\> (integer) \[required\]
> >
> > > The Y coordinate on screen where the click occurs.
> >
> > button -\> (string)
> >
> > > The mouse button to use. Defaults to `LEFT` .
> > >
> > > Possible values:
> > >
> > > - `LEFT`
> > > - `RIGHT`
> > > - `MIDDLE`
> >
> > clickCount -\> (integer)
> >
> > > The number of clicks to perform. Valid range: 1–10. Defaults to 1.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `10`
>
> mouseMove -\> (structure)
>
> > Move the cursor to the specified coordinates.
> >
> > x -\> (integer) \[required\]
> >
> > > The target X coordinate on screen.
> >
> > y -\> (integer) \[required\]
> >
> > > The target Y coordinate on screen.
>
> mouseDrag -\> (structure)
>
> > Drag from a start position to an end position.
> >
> > endX -\> (integer) \[required\]
> >
> > > The ending X coordinate for the drag.
> >
> > endY -\> (integer) \[required\]
> >
> > > The ending Y coordinate for the drag.
> >
> > startX -\> (integer) \[required\]
> >
> > > The starting X coordinate for the drag.
> >
> > startY -\> (integer) \[required\]
> >
> > > The starting Y coordinate for the drag.
> >
> > button -\> (string)
> >
> > > The mouse button to use for the drag. Defaults to `LEFT` .
> > >
> > > Possible values:
> > >
> > > - `LEFT`
> > > - `RIGHT`
> > > - `MIDDLE`
>
> mouseScroll -\> (structure)
>
> > Scroll at the specified position.
> >
> > x -\> (integer) \[required\]
> >
> > > The X coordinate on screen where the scroll occurs.
> >
> > y -\> (integer) \[required\]
> >
> > > The Y coordinate on screen where the scroll occurs.
> >
> > deltaX -\> (integer)
> >
> > > The horizontal scroll delta. Valid range: -1000 to 1000.
> > >
> > > Constraints:
> > >
> > > - min: `-1000`
> > > - max: `1000`
> >
> > deltaY -\> (integer)
> >
> > > The vertical scroll delta. Valid range: -1000 to 1000. Negative values scroll down.
> > >
> > > Constraints:
> > >
> > > - min: `-1000`
> > > - max: `1000`
>
> keyType -\> (structure)
>
> > Type a string of text.
> >
> > text -\> (string) \[required\]
> >
> > > The text string to type. Maximum length: 10,000 characters.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `10000`
>
> keyPress -\> (structure)
>
> > Press a key one or more times.
> >
> > key -\> (string) \[required\]
> >
> > > The key name to press (for example, `enter` , `tab` , `escape` ).
> >
> > presses -\> (integer)
> >
> > > The number of times to press the key. Valid range: 1–100. Defaults to 1.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `100`
>
> keyShortcut -\> (structure)
>
> > Press a key combination.
> >
> > keys -\> (list) \[required\]
> >
> > > The key combination to press (for example, `["ctrl",`` ``"s"]` ). Maximum 5 keys.
> > >
> > > Constraints:
> > >
> > > - min: `1`
> > > - max: `5`
> > >
> > > (string)
>
> screenshot -\> (structure)
>
> > Capture a full-screen screenshot.
> >
> > format -\> (string)
> >
> > > The image format for the screenshot. Defaults to `PNG` .
> > >
> > > Possible values:
> > >
> > > - `PNG`

Shorthand Syntax:

    mouseClick={x=integer,y=integer,button=string,clickCount=integer},mouseMove={x=integer,y=integer},mouseDrag={endX=integer,endY=integer,startX=integer,startY=integer,button=string},mouseScroll={x=integer,y=integer,deltaX=integer,deltaY=integer},keyType={text=string},keyPress={key=string,presses=integer},keyShortcut={keys=[string,string]},screenshot={format=string}

JSON Syntax:

    {
      "mouseClick": {
        "x": integer,
        "y": integer,
        "button": "LEFT"|"RIGHT"|"MIDDLE",
        "clickCount": integer
      },
      "mouseMove": {
        "x": integer,
        "y": integer
      },
      "mouseDrag": {
        "endX": integer,
        "endY": integer,
        "startX": integer,
        "startY": integer,
        "button": "LEFT"|"RIGHT"|"MIDDLE"
      },
      "mouseScroll": {
        "x": integer,
        "y": integer,
        "deltaX": integer,
        "deltaY": integer
      },
      "keyType": {
        "text": "string"
      },
      "keyPress": {
        "key": "string",
        "presses": integer
      },
      "keyShortcut": {
        "keys": ["string", ...]
      },
      "screenshot": {
        "format": "PNG"
      }
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

result -\> (tagged union structure)

> The result of the browser action. The member set in the result corresponds to the action that was performed.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `mouseClick`, `mouseMove`, `mouseDrag`, `mouseScroll`, `keyType`, `keyPress`, `keyShortcut`, `screenshot`.
>
> mouseClick -\> (structure)
>
> > The result of a mouse click action.
> >
> > status -\> (string) \[required\]
> >
> > > The status of the action execution.
> > >
> > > Possible values:
> > >
> > > - `SUCCESS`
> > > - `FAILED`
> >
> > error -\> (string)
> >
> > > The error message. Present only when the action failed.
>
> mouseMove -\> (structure)
>
> > The result of a mouse move action.
> >
> > status -\> (string) \[required\]
> >
> > > The status of the action execution.
> > >
> > > Possible values:
> > >
> > > - `SUCCESS`
> > > - `FAILED`
> >
> > error -\> (string)
> >
> > > The error message. Present only when the action failed.
>
> mouseDrag -\> (structure)
>
> > The result of a mouse drag action.
> >
> > status -\> (string) \[required\]
> >
> > > The status of the action execution.
> > >
> > > Possible values:
> > >
> > > - `SUCCESS`
> > > - `FAILED`
> >
> > error -\> (string)
> >
> > > The error message. Present only when the action failed.
>
> mouseScroll -\> (structure)
>
> > The result of a mouse scroll action.
> >
> > status -\> (string) \[required\]
> >
> > > The status of the action execution.
> > >
> > > Possible values:
> > >
> > > - `SUCCESS`
> > > - `FAILED`
> >
> > error -\> (string)
> >
> > > The error message. Present only when the action failed.
>
> keyType -\> (structure)
>
> > The result of a key type action.
> >
> > status -\> (string) \[required\]
> >
> > > The status of the action execution.
> > >
> > > Possible values:
> > >
> > > - `SUCCESS`
> > > - `FAILED`
> >
> > error -\> (string)
> >
> > > The error message. Present only when the action failed.
>
> keyPress -\> (structure)
>
> > The result of a key press action.
> >
> > status -\> (string) \[required\]
> >
> > > The status of the action execution.
> > >
> > > Possible values:
> > >
> > > - `SUCCESS`
> > > - `FAILED`
> >
> > error -\> (string)
> >
> > > The error message. Present only when the action failed.
>
> keyShortcut -\> (structure)
>
> > The result of a key shortcut action.
> >
> > status -\> (string) \[required\]
> >
> > > The status of the action execution.
> > >
> > > Possible values:
> > >
> > > - `SUCCESS`
> > > - `FAILED`
> >
> > error -\> (string)
> >
> > > The error message. Present only when the action failed.
>
> screenshot -\> (structure)
>
> > The result of a screenshot action.
> >
> > status -\> (string) \[required\]
> >
> > > The status of the action execution.
> > >
> > > Possible values:
> > >
> > > - `SUCCESS`
> > > - `FAILED`
> >
> > error -\> (string)
> >
> > > The error message. Present only when the action failed.
> >
> > data -\> (blob)
> >
> > > The base64-encoded image data. Present only when the action succeeded.

sessionId -\> (string)

> The unique identifier of the browser session on which the action was performed.
>
> Constraints:
>
> - pattern: `[0-9a-zA-Z]{1,40}`

- [← invoke-agent-runtime](invoke-agent-runtime.html "previous chapter (use the left arrow)") /
- [list-ab-tests →](list-ab-tests.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](list-ab-tests.html "list-ab-tests") \|
- [previous](invoke-agent-runtime.html "invoke-agent-runtime") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore](index.html) »
- [invoke-browser]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).

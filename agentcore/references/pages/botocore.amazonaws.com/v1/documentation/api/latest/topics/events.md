---
title: Botocore Events[¶](#botocore-events "Link to this heading")
description: Botocore will emit events during various parts of its execution. Users of the library can register handlers (callables) for these events, such that whenever an event is emitted, all registered handlers for the event will be called. This allows you to customize and extend the beha
product: Amazon Bedrock AgentCore
section: References / botocore.amazonaws.com
source_url: https://botocore.amazonaws.com/v1/documentation/api/latest/topics/events.html
fetched: '2026-09-26'
tags:
- agentcore
- botocore-amazonaws-com
- reference
- related
referenced_by:
- runtime-header-allowlist.md
conversion: pandoc
---

# Botocore Events[¶](#botocore-events "Link to this heading")

Botocore will emit events during various parts of its execution. Users of the library can register handlers (callables) for these events, such that whenever an event is emitted, all registered handlers for the event will be called. This allows you to customize and extend the behavior of botocore without having to modify the internals. This document covers this event system in detail.

## Session Events[¶](#session-events "Link to this heading")

The main interface for events is through the `botocore.session.Session` class. The `Session` object allows you to register and unregister handlers to events.

## Event Types[¶](#event-types "Link to this heading")

The list below shows all of the events emitted by botocore. In some cases, the events are listed as `event-name.<service-id>.<operations>`, in which `<service-id>` and `<operation>` are replaced with a specific service identifier operation, for example `event-name.s3.ListObjects`.

- `'before-send.<service-id>.<operation>'`

### before-send[¶](#before-send "Link to this heading")

Full Event Name:  
`'before-send.<service>.<operation>'`

Description:  
This event is emitted when the operation has been fully serialized, signed, and is ready to be sent across the wire. This event allows the finalized request to be inspected and allows a response to be returned that fufills the request. If no response is returned botocore will fulfill the request as normal.

Keyword Arguments Emitted:  
type request:  
[`AWSPreparedRequest`](../reference/awsrequest.html#botocore.awsrequest.AWSPreparedRequest "botocore.awsrequest.AWSPreparedRequest")

param params:  
An object representing the properties of an HTTP request.

Expected Return Value:  
None or an instance of [`AWSResponse`](../reference/awsrequest.html#botocore.awsrequest.AWSResponse "botocore.awsrequest.AWSResponse")

## Event Emission[¶](#event-emission "Link to this heading")

When an event is emitted, the handlers are invoked in the order that they were registered.

## Service ID[¶](#service-id "Link to this heading")

To get the service id from a service client use the following:

    import botocore
    import botocore.session

    session = botocore.session.Session()
    client = session.create_client('elbv2')
    service_event_name = client.meta.service_model.service_id.hyphenize()

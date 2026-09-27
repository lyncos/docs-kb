---
title: Private Certificate + Public Domain
description: '**Note:** The guidance in this document is intended for **workshop and learning purposes only**. For production deployments, please adhere to your organization''s security policies, DNS management practices, and certificate lifecycle requirements.'
product: Amazon Bedrock AgentCore
section: References / repo / agentcore-samples
source_url: https://github.com/awslabs/agentcore-samples/blob/e1a55b3/01-features/07-centralize-and-govern-your-ai-infrastructure/01-gateway/03-private-connectivity/connect-gateway-to-private-resources/00-prerequisites/concepts/private-certificate-public-domain.md
fetched: '2026-09-26'
tags:
- agentcore
- agentcore-samples
- reference
---

<!-- Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->

# Private Certificate + Public Domain

> **Note:** The guidance in this document is intended for **workshop and learning purposes only**. For production deployments, please adhere to your organization's security policies, DNS management practices, and certificate lifecycle requirements.

## Overview

| Component | Type | Description |
|-----------|------|-------------|
| **Certificate** | Private (AWS Private CA) | Trusted only by systems configured to trust your CA |
| **Domain** | Public (Route 53 public hosted zone) | Resolves globally via public DNS |

## What does this mean?

Your domain is publicly resolvable, but the TLS certificate is issued by a private Certificate Authority (e.g., [AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html)). Only clients that have your CA's root certificate installed will trust the connection.

## Limitation with AgentCore Gateway

AgentCore Gateway **does not support private certificates**. When AgentCore connects to your endpoint, it validates the TLS certificate against public root CAs only. A private certificate will cause a TLS handshake failure.

## Workaround

To use a private certificate with AgentCore Gateway, place a load balancer with a **public certificate** in front of your resource:

```
AgentCore Gateway
  → VPC Lattice → Resource Gateway ENIs
    → Load Balancer (public cert, TLS termination)
      → Your resource (private cert or plain HTTP)
```

The load balancer terminates TLS with the public cert, then forwards traffic to your backend. Your backend can use a private cert for internal communication if needed, but AgentCore only sees the public cert on the load balancer.

In practice, this becomes the [Public Certificate + Public Domain](./public-certificate-public-domain.md) or [Public Certificate + Private Domain](./public-certificate-private-domain.md) pattern.

## When would you use a private certificate?

- **Between internal services** (not involving AgentCore): microservice-to-microservice mTLS
- **Behind a load balancer**: the LB terminates public TLS, backend uses private TLS
- **Compliance requirements**: your organization mandates certificates from an internal CA for backend encryption

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](../LICENSE.txt) file for details.
